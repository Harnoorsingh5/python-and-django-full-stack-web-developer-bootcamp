from django.shortcuts import render, get_object_or_404, redirect
from blog import models
from blog.forms import PostForm, CommentForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required #using decorators
from django.contrib.auth.mixins import LoginRequiredMixin #using mixins
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class AboutView(TemplateView):
    template_name = 'blog/about.html'


##############################
'''POST'''
##############################

'''
    List and Detail Views
'''
class PostListView(ListView):
    model = models.Post
    template_name = 'blog/post_list.html'

    '''
        get_queryset; is doing a SQL query on my table
        This is python's version of writing SQL query 
         __lte (less than equal to) : it is a lookup in Django : __lookuptype
         order_by (for sorting) '-' in the start of published_date represents that order is in descending order
         filter (is like where clause)
    '''
    def get_queryset(self):
        return models.Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    
class PostDetailView(DetailView):
    model = models.Post
    template_name = 'blog/post_detail.html'


'''
    CRUD Views
'''
class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = models.Post
    template_name = 'blog/post_form.html'

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = models.Post
    template_name = 'blog/post_form.html'

class PostDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    model = models.Post
    success_url = reverse_lazy("blog:post_list")
    template_name = 'blog/post_confirm_del.html'
'''
    List View
'''
class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = models.Post
    template_name = 'blog/post_draft_list.html'

    def get_queryset(self):
        return models.Post.objects.filter(published_date__isnull=True).order_by('create_date')



##############################
'''POST PUBLISH'''
##############################
@login_required
def post_publish(request, pk):
    post = get_object_or_404(models.Post, pk=pk) # either get that post object or a 404 page incase post does not exist
    post.publish()
    return redirect('blog:post_detail', pk=pk)


##############################
'''COMMENT'''
##############################
@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(models.Post, pk=pk) # either get that post object or a 404 page incase post does not exist
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post # attaching this comment to particular post (as post is foreign key in Comment Model)
            comment.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form':form})            

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(models.Comment, pk=pk) # either get that Comment object or a 404 page incase comment does not exist
    comment.approve()
    return redirect('blog:post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(models.Comment, pk=pk) # either get that Comment object or a 404 page incase comment does not exist
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog:post_detail', pk=post_pk)
    
'''
For function based views->
    using this @login_required decorator Django makes sure that logout page or the particular 
    page is only hit if the user is logged into the website
    make the task easy for programmers.
For class based views->
    we use mixins i.e; LoginRequiredMixin
'''

