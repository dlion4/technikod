from category.models import Category, SubCategory, Topic, Tag
from posts.models import Post, Tip
from django.contrib.sites.shortcuts import get_current_site
from tokens.models import TinyMceApiKey


def get_categories(request):
    return dict(
        nav_categories=Category.objects.all().order_by("?")[:8],
        footer_categories=Category.objects.all().order_by("-id")[:5],
        editors_choice=Post.objects.filter(is_editors_choice=True)
        .all()
        .order_by("-createdAt")[:10],
        recents=Post.objects.is_recent().all().order_by("-createdAt")[:8],
        popular=Post.objects.is_popular().order_by("?")[:4],
        recent=Post.objects.is_recent().order_by("?")[:4],
        side_categories=Category.objects.all().order_by("-id")[:5],
        lim_tags=Tag.objects.all().order_by("?")[:10],
        tips=Tip.objects.all().order_by("?"),
    )

def sites_context_data(request):
    if request.is_secure():
        protocol="https"
    protocol = "http"
    return dict(
        site_domain=get_current_site(request).domain,
        protocol=protocol,
        site_social_fab="https://www.facebook.com/",
        site_social_twitter="https://www.twitter.com/",
        site_social_youtube="https://www.youtube.com/",
        site_social_instagram="https://www.Instagram.com/",
        # tinymce key
        tinymce_apikey=TinyMceApiKey.objects.filter(is_active=True).latest()
    )
