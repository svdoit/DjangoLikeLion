from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required

# Create your views here.
def guestbook(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    #블로그 모든 글들을 대상으로
   
    paginator = Paginator(blog_list, 5)
    #블로그 객체 세 개를 한 페이지로 자르기
   
    page = request.GET.get('page')
    #request된 페이지번호가 뭔지를 알아내고 (request페이지를 변수에 담아내고)
    
    posts = paginator.get_page(page)
    #request된 페이지 번호의 페이지를 얻어온 뒤 posts에 넣어 사전형으로 return 해준다
    return render(request, 'blog.html', {'blogs':blogs, 'posts':posts})

def blogDetailView(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogDetail.html', {'blog_detail':blog_detail})


def blogNewView(request):
    return render(request, 'blogNew.html')

def blogCreateView(request):
    if request.method == "POST":
        blog_create = Blog()

        blog_create.title = request.POST.get('title')
        blog_create.body = request.POST.get('body')
        blog_create.writer = request.user.first_name
        blog_create.pub_date = timezone.datetime.now()
        blog_create.image = request.FILES.get('image')
        blog_create.save()

        return redirect('/guestbook/'+str(blog_create.id))

def update(request, blog_id):
    blog_update = get_object_or_404(Blog, pk = blog_id)

    if request.user == blog_update.writer:
            
        if request.method == 'POST':
            if 'image' in request.FILES:
                blog_update.image = request.FILES['image']
            blog_update.title = request.POST['title']
            blog_update.body = request.POST['body']
            blog_update.writer = request.POST['writer']

            blog_update.save()

            return redirect('/guestbook/', blog_update.id)
      
        else:
            return render(request, 'blogUpdate.html', {'blog_update' : blog_update })
    
    raise PermissionDenied

def delete(request, blog_id):
    blog_delete = get_object_or_404(Blog, pk = blog_id)
    if request.user == blog_delete.writer:
        blog_delete.delete()
        return redirect('guestbook')
    raise PermissionDenied
