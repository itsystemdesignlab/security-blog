from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

STATUS = ((0, "Draft"), (1, "Publish"))


class Post(models.Model):
    """Post Model."""

    title = models.CharField(max_length=200, unique=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self) -> str:
        """Get absolute url of post."""
        from django.urls import reverse

        return reverse("post_detail", kwargs={"slug": str(self.slug)})


class Comment(models.Model):
    """Comment Model."""

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)


class About(models.Model):
    """About model."""

    title = models.TextField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return self.title

class Policy(models.Model):
    """policy model."""

    title = models.TextField(max_length=80)
    body = models.TextField()
    policy = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return self.title

class Contact(models.Model):
    """Contact model."""

    name = models.CharField(max_length=80)
    email = models.EmailField()
    address = models.TextField()
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True
    )  # Validators should be a list
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return self.name
