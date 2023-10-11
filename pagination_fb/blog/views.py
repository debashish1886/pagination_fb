from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post

def post_list(request):
    all_post=Post.objects.all().order_by('id')
    paginator=Paginator(all_post,3,orphans=1)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request,"base.html",{'page_obj':page_obj})
