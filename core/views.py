from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy
from .models import *
from django.core.exceptions import PermissionDenied
from django.shortcuts import render,redirect
from .forms import *

class Home(TemplateView):
  template_name = "home.html"

class PostCreateView(CreateView):
  model = Post
  template_name = "post/post_form.html"
  fields = ['title', 'description']
  success_url = reverse_lazy('post_list')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(PostCreateView, self).form_valid(form)

class PostListView(ListView):
  model = Post
  template_name = "post/post_list.html"

class PostDetailView(DetailView):
  model = Post
  template_name = 'post/post_detail.html'

  def get_context_data(self, **kwargs):
    context = super(PostDetailView, self).get_context_data(**kwargs)
    post = Post.objects.get(id=self.kwargs['pk'])
    comments = Comment.objects.filter(post=post)
    context['comments'] = comments
    return context

class PostUpdateView(UpdateView):
  model = Post
  template_name = 'post/post_form.html'
  fields = ['title', 'description']

  def get_object(self, *args, **kwargs):
    object = super(PostUpdateView, self).get_object(*args, **kwargs)
    if object.user != self.request.user:
      raise PermissionDenied()
    return object

class PostDeleteView(DeleteView):
  model = Post
  template_name = 'post/post_confirm_delete.html'
  success_url = reverse_lazy('post_list')

  def get_object(self, *args, **kwargs):
    object = super(PostDeleteView, self).get_object(*args, **kwargs)
    if object.user != self.request.user:
      raise PermissionDenied()
      return object

class CommentCreateView(CreateView):
  model = Comment
  template_name = "comment/comment_form.html"
  fields = ['text']

  def get_success_url(self):
    return self.object.post.get_absolute_url()

  def form_valid(self, form):
    form.instance.user = self.request.user
    form.instance.post = Post.objects.get(id=self.kwargs['pk'])
    return super(CommentCreateView, self).form_valid(form)

class CommentUpdateView(UpdateView):
  model = Comment
  pk_url_kwarg = 'comment_pk'
  template_name = 'comment/comment_form.html'
  fields = ['text']

  def get_object(self, *args, **kwargs):
    object = super(CommentUpdateView, self).get_object(*args, **kwargs)
    if object.user != self.request.user:
      raise PermissionDenied()
      return object

  def get_success_url(self):
    return self.object.post.get_absolute_url()

class CommentDeleteView(DeleteView):
  model = Comment
  pk_url_kwarg = 'comment_pk'
  template_name = 'comment/comment_confirm_delete.html'

  def get_success_url(self):
    return self.object.post.get_absolute_url()

  def get_object(self, *args, **kwargs):
    object = super(CommentDeleteView, self).get_object(*args, **kwargs)
    if object.user != self.request.user:
      raise PermissionDenied()
      return object

class VoteFormView(FormView):
  form_class = VoteForm

  def form_valid(self, form):
    user = self.request.user
    post = Post.objects.get(pk=form.data["post"])
    prev_votes = Vote.objects.filter(user=user, post=post)
    has_voted = (prev_votes.count()>0)
    if not has_voted:
      Vote.objects.create(user=user, post=post)
    else:
      prev_votes[0].delete()
    return redirect('post_list')