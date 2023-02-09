from django.contrib.sitemaps import Sitemap

from .models import Post


class PostSitemap(Sitemap):
    """Site map."""

    changefreq = "weekly"
    priority = 0.8

    def items(self) -> Post:
        """All active posts."""

        return Post.objects.filter(status=1)

    def lastmod(self, obj) -> Post:
        """Updated posts."""

        return obj.updated_on

    # def location(self, item):
    #     return reverse(item)
