from django.shortcuts import render
from django.views import generic, View
from .models import SubCategory, Category
from posts.models import Post
from django.http import HttpResponse
from paginator.paginators import Paginator

# Create your views here.


class SubCategoryListView(Paginator, generic.TemplateView):
    template_name = "pages/category.html"
    queryset = Post
    model = SubCategory
    page_kwargs = "page"
    paginate_by = 10
    context_object_name = "posts"

    def get_object(self, **kwargs):
        return self.model.objects.get(
            category__name__icontains=kwargs.get("category_slug"), id=kwargs.get("pk")
        )

    def get_related_posts(self, **kwargs):
        return self.queryset.objects.filter(
            topic__sub_category__name__icontains=self.get_object(**kwargs).name
        ).all()

    def gq_queryset(self,**kwargs):
        return self.get_related_posts(**kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(SubCategoryListView, self).get_context_data(**kwargs)
        context["sub"] = self.get_object(**kwargs)
        # context["posts"] = (
        #     self.get_related_posts(**kwargs).order_by("?").order_by("-createdAt")
        # )
        return context


class CategoryDetailView(View):
    queryset = Category
    def get_object(self, **kwargs):
        return self.queryset.objects.get(
            category__name__icontains=kwargs.get("slug"), id=kwargs.get("pk")
        )
        # category_detail
    def get(self, request,*args, **kwargs):
        return HttpResponse(self.get_object(**kwargs))

