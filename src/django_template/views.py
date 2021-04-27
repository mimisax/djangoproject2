from django.shortcuts import render
from . models import BookStore

# Create your views here.

def home_view(request):
    book = BookStore.objects.get(year_published=2030)
    book_author = BookStore.objects.get(book_author="Chinua Achebe")
    all_books = BookStore.objects.all()
    #food = "Bread"
    return render(
        request,
        "home.html",
        #{"food": food}
        {
            "book":book,
            "book_author":book_author,
            "all_books": all_books,
            }
    )

# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


from .models import Post
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})