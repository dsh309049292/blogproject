from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category, Tag, Img
from PIL import Image
def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context = {'post_list' : post_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk = pk)
    return render(request, 'blog/detail.html', context = {'post' :post})

def ocr(request):
    if request.method == 'POST':
        new_img = Img(img = request.FILES.get('file_head'), name = request.FILES.get('file_head').name)
        new_img.save()
    return render(request, 'blog/OCR.html')