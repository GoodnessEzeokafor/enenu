from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.db.models import Count
from .forms import CommentForm
# from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

# Create your views here.


def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 2)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        #If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html',{
        'page':page,
        'posts':posts,
    })


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, 
                            slug=post,
                            publish__year=year,
                            publish__month=month,
                            publish__day=day)
    # List of active comments
    comments = post.comments.filter(active=True) # using the related_name in the many-to-one relationship filter acording to the active comment
    new_comment = None
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # Create comment object but don't save to the database
            new_comment = comment_form.save(commit=False)
            #Assign the current post to the comment
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    # post_tags_ids = post.tags.values_list('id', flat=True)
    # similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    # similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]
    return render(request, 'blog/post/detail.html', {
        'post':post,
        'new_comment':new_comment,
        'comment_form':comment_form,
        'comments':comments,
        # 'similar_posts':similar_posts
    })

    
