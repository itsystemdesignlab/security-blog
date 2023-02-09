from django.shortcuts import get_object_or_404, render
from django.views import generic

from .forms import CommentForm, ContactForm
from .models import About, Post, Contact, Policy


class PostList(generic.ListView):
    """Post list generic list view."""

    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 8


# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'


class AboutList(generic.ListView):
    """About list generic view."""

    queryset = About.objects.all()
    template_name = "about.html"


def post_detail(request, slug):
    """
    Post Detail.
        :param request: Request object.
        :param slug: Slug name.
        :return: Detail of post.
    """
    template_name = "post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    # Comment posted
    if request.method == "POST":
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

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )

class ContactList(generic.ListView):
    """Contact list generic view."""
    queryset = Contact.objects.all()
    template_name = "contact.html"

class PolicyList(generic.ListView):
    """Policy list generic view."""
    queryset = Policy.objects.all()
    template_name = "policy.html"


def contact(request):
    """
    Post Detail.
        :param request: Request object.
        :param slug: Slug name.
        :return: Detail of post.
    """
    template_name = "contact.html"
    # Comment posted
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():

            # Create Comment object but don't save to database yet
            new_contact = contact_form.save(commit=False)
            # Save the comment to the database
            new_contact.save()
    else:
        contact_form = ContactForm()

    return render(
        request,
        template_name,
        {
            "contact_form": contact_form,
        },
    )
