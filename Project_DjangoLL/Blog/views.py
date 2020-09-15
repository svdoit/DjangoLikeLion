from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog

# Create your views here.
def guestbook(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    #블로그 모든 글들을 대상으로
   
    paginator = Paginator(blog_list, 3)
    #블로그 객체 세 개를 한 페이지로 자르기
   
    page = request.GET.get('page')
    #request된 페이지번호가 뭔지를 알아내고 (request페이지를 변수에 담아내고)
    
    posts = paginator.get_page(page)
    #request된 페이지 번호의 페이지를 얻어온 뒤 posts에 넣어 사전형으로 return 해준다
    return render(request, 'blog.html', {'blogs':blogs, 'posts':posts})

def blogDetailView(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogDetail.html', {'blog_detail':blog_detail})