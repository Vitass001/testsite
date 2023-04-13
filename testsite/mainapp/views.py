from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.views import LoginView
from .models import Product
from django.shortcuts import render, redirect, get_object_or_404

from .models import Post
from .forms import PostForm, PostForm1, PostForm2, PostForm3, PostForm4, PostForm5, PostForm6, PostForm7, PostForm8, PostForm9, PostForm10
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm
from math import atan
import math

from django.core.files.storage import FileSystemStorage
# from django_filters.views import FilterView
# from .models import MyModel
# from .filters import MyModelFilter


from django.db.models import Q
from django.shortcuts import render
from .models import Post








def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Ви успішно увійшли в систему!')
                return redirect(home_page)
            else:
                messages.error(request, 'Невірне ім\'я користувача або пароль.')
    else:
        form = LoginForm()
    return render(request, 'mainapp/login.html', {'form': form})


def home_page(request):
    return render(request, 'mainapp/home_page.html',)

@login_required
def post_create(request):

    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES or None)
        # form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()

            # photo = form.cleaned_data['image']
            # # Створюємо новий об'єкт моделі MyModel і зберігаємо фото в полі photo
            # post = Post.objects.create(photo=photo)
            # Перенаправляємо користувача на сторінку зі списком фотографій або виводимо повідомлення про успішне завантаження фото.



            return redirect('post_detail', Legal_Entity=form.instance.Legal_Entity)
    else:
        form = PostForm()

    return render(request, 'mainapp/post_create.html', {'form': form,}, )


def calculator(request):

    return render(request, 'mainapp/calculator.html')












@login_required
def post_detail(request, Legal_Entity):
    post = get_object_or_404(Post, Legal_Entity = Legal_Entity)

    # oll_result = {'result1': result1}
    # if post.category == 'A':
    #     numb1 = 2.6
    #     numb2 = 53
    #     numb3 = 2560
    #     result1 = math.atan((post.camera_height - 1.5) / num3) * 180 / 3.14159
    #     result2 = num3 * math.tan((numb2 - (numb2 - numb1) * num4 / 100) * math.pi / 180)
    #     result3 = (numb3 / result2) / 6.25
    # oll_result = {'result1': result1, 'result2' : result2,'result3': result3 }
    return render(request, 'mainapp/post_detail.html', {'post': post,})





@login_required
def all_posts(request):
    posts = Post.objects.order_by('-pub_date')

    # search_query = request.GET.get('search', '')
    # if search_query:
    #     fil_post = Post.objects.filter(title_name__icontains=search_query)
    # else:
    #     fil_post = Post.objects.all()



    return render(request, 'mainapp/all_posts.html', {'posts': posts})


def search(request):
    query = request.GET.get('q')
    posts = Post.objects.filter(Legal_Entity__icontains=query)
    context = {
        'query': query,
        'posts': posts
    }
    return render(request, 'mainapp/all_posts.html', context)

def post_edit(request, Legal_Entity):
    post = get_object_or_404(Post, Legal_Entity=Legal_Entity)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False,)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', Legal_Entity=post.Legal_Entity)
    else:
        form = PostForm(instance=post)
    return render(request, 'mainapp/post_edit.html', {'form': form})


def post_edit1(request, Legal_Entity):
    post = get_object_or_404(Post, Legal_Entity=Legal_Entity)
    if request.method == "POST":
        form = PostForm1(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False,)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', Legal_Entity=post.Legal_Entity)
    else:
        form = PostForm1(instance=post)
    return render(request, 'mainapp/post_edit1.html', {'form': form})

def post_edit2(request, Legal_Entity):
    post = get_object_or_404(Post, Legal_Entity=Legal_Entity)
    if request.method == "POST":
        form = PostForm2(request.POST, request.FILES, instance=post)
        if form.is_valid():

            post.save()
            return redirect('post_detail', Legal_Entity=post.Legal_Entity)
    else:
        form = PostForm2(instance=post)
    return render(request, 'mainapp/post_edit2.html', {'form': form})



def post_edit3(request, Legal_Entity):
    post = get_object_or_404(Post, Legal_Entity=Legal_Entity)
    if request.method == "POST":
        form = PostForm3(request.POST, request.FILES, instance=post)
        if form.is_valid():

            post.save()
            return redirect('post_detail', Legal_Entity=post.Legal_Entity)
    else:
        form = PostForm3(instance=post)
    return render(request, 'mainapp/post_edit3.html', {'form': form})


def post_edit4(request, Legal_Entity):
    post = get_object_or_404(Post, Legal_Entity=Legal_Entity)
    if request.method == "POST":
        form = PostForm4(request.POST, request.FILES, instance=post)
        if form.is_valid():

            post.save()
            return redirect('post_detail', Legal_Entity=post.Legal_Entity)
    else:
        form = PostForm4(instance=post)
    return render(request, 'mainapp/post_edit4.html', {'form': form})


def post_edit5(request, Legal_Entity):
    post = get_object_or_404(Post, Legal_Entity=Legal_Entity)
    if request.method == "POST":
        form = PostForm5(request.POST, request.FILES, instance=post)
        if form.is_valid():

            post.save()
            return redirect('post_detail', Legal_Entity=post.Legal_Entity)
    else:
        form = PostForm5(instance=post)
    return render(request, 'mainapp/post_edit5.html', {'form': form})


def post_edit6(request, Legal_Entity):
    post = get_object_or_404(Post, Legal_Entity=Legal_Entity)
    if request.method == "POST":
        form = PostForm6(request.POST, request.FILES, instance=post)
        if form.is_valid():

            post.save()
            return redirect('post_detail', Legal_Entity=post.Legal_Entity)
    else:
        form = PostForm6(instance=post)
    return render(request, 'mainapp/post_edit6.html', {'form': form})


def post_edit7(request, Legal_Entity):
    post = get_object_or_404(Post, Legal_Entity=Legal_Entity)
    if request.method == "POST":
        form = PostForm7(request.POST, request.FILES, instance=post)
        if form.is_valid():

            post.save()
            return redirect('post_detail', Legal_Entity=post.Legal_Entity)
    else:
        form = PostForm7(instance=post)
    return render(request, 'mainapp/post_edit7.html', {'form': form})


def post_edit8(request, Legal_Entity):
    post = get_object_or_404(Post, Legal_Entity=Legal_Entity)
    if request.method == "POST":
        form = PostForm8(request.POST, request.FILES, instance=post)
        if form.is_valid():

            post.save()
            return redirect('post_detail', Legal_Entity=post.Legal_Entity)
    else:
        form = PostForm8(instance=post)
    return render(request, 'mainapp/post_edit8.html', {'form': form})


def post_edit9(request, Legal_Entity):
    post = get_object_or_404(Post, Legal_Entity=Legal_Entity)
    if request.method == "POST":
        form = PostForm9(request.POST, request.FILES, instance=post)
        if form.is_valid():

            post.save()
            return redirect('post_detail', Legal_Entity=post.Legal_Entity)
    else:
        form = PostForm9(instance=post)
    return render(request, 'mainapp/post_edit9.html', {'form': form})


def post_edit10(request, Legal_Entity):
    post = get_object_or_404(Post, Legal_Entity=Legal_Entity)
    if request.method == "POST":
        form = PostForm10(request.POST, request.FILES, instance=post)
        if form.is_valid():

            post.save()
            return redirect('post_detail', Legal_Entity=post.Legal_Entity)
    else:
        form = PostForm10(instance=post)
    return render(request, 'mainapp/post_edit10.html', {'form': form})









def post_delete(request, Legal_Entity):
    post = get_object_or_404(Post, Legal_Entity=Legal_Entity)
    if request.method == 'POST':
        post.delete()
        return redirect('all_posts')
    return render(request, 'mainapp/post_confirm_delete.html', {'post': post})

# def post_delete1(request, title):
#     post = get_object_or_404(Post, title=title)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('all_posts')
#     return render(request, 'mainapp/post_confirm_delete1.html', {'post': post})
#
# def post_delete2(request, title):
#     post = get_object_or_404(Post, title=title)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('all_posts')
#     return render(request, 'mainapp/post_confirm_delete2.html', {'post': post})





