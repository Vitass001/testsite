from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.views import LoginView
from django.views.decorators.http import require_GET

from .models import Product
from django.shortcuts import render, redirect, get_object_or_404

from .models import Post
from .forms import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required, user_passes_test
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
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


from django.db.models import Q
from django.shortcuts import render
from .models import Post, Property


def user_has_admin_login(user):
    return user.username == "admin"



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




# def post_create(request):
#     property_form = PropertyForm(request.POST or None)
#     post_form = PostForm(request.POST or None)
#
#     if request.method == 'POST' and property_form.is_valid() and post_form.is_valid():
#         # зберегти property_form та post_form до бази даних
#         property = Property.objects.get(id=request.POST['company'])
#         post = post_form.save(commit=False)
#         post.company = property
#         post.save()
#         return redirect('post_detail', Legal_Entity=post_form.instance.Legal_Entity)
#     else:
#         property_form = PropertyForm()
#         post_form = PostForm
#
#     return render(request, 'mainapp/post_create.html', { 'post_form': post_form})




@login_required
def post_create(request):

    post_form = PostForm(request.POST or None)

    if request.method == 'POST' :
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()

            return redirect('post_detail', Legal_Entity=form.instance.Legal_Entity, property=form.instance.property, Camera_Name=form.instance.Camera_Name )
    else:
        form = PostForm()

    return render(request, 'mainapp/post_create.html', {'form': form, 'post_form':post_form }, )









@login_required
def create_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect(all_posts)
    else:
        form = PropertyForm()

    return render(request, 'mainapp/create_property.html', {'form': form }, )


@login_required
def create_Legal_Entity(request):
    if request.method == 'POST':
        form = LegalForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect(all_posts)
    else:
        form = LegalForm()

    return render(request, 'mainapp/create_Legal_Entity.html', {'form': form }, )


@login_required
def property_list_ajax(request):
    Legal_Entity = request.GET.get('Legal_Entity')
    properties = Property.objects.filter(Legal_Entity=Legal_Entity).values('id', 'property')
    return JsonResponse({'properties': list(properties)})



@login_required
def calculator(request):

    return render(request, 'mainapp/calculator.html')


@login_required
def post_detail(request, Legal_Entity, Camera_Name, property):
    # post = get_object_or_404(Post, Legal_Entity = Legal_Entity)
    post = get_object_or_404(Post, Legal_Entity=Legal_Entity, Camera_Name=Camera_Name, property=property  )
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
def post_detail_old(request, Legal_Entity, Camera_Name, property):

    post = get_object_or_404(Post, Legal_Entity=Legal_Entity, Camera_Name=Camera_Name, property=property  )

    return render(request, 'mainapp/post_detail_old.html', {'post': post,})

@login_required
def all_posts(request):
    posts = Post.objects.order_by('-pub_date')

    # search_query = request.GET.get('search', '')
    # if search_query:
    #     fil_post = Post.objects.filter(title_name__icontains=search_query)
    # else:
    #     fil_post = Post.objects.all()



    return render(request, 'mainapp/all_posts.html', {'posts': posts})

@login_required
def search(request):
    query = request.GET.get('q')
    query_parts = query.split('-')

    if len(query_parts) == 1:
        posts = Post.objects.filter(
            Q(Legal_Entity__icontains=query) |
            Q(property__icontains=query) |
            Q(Camera_Name__icontains=query)
        )

    elif len(query_parts) == 2:
        posts = Post.objects.filter(
            property__icontains=query_parts[1],
        )

    else:
        posts = Post.objects.filter(
            Legal_Entity__icontains=query_parts[0],
            property__icontains=query_parts[1],
            Camera_Name__icontains=query_parts[2],
        )

    context = {
        'query': query,
        'posts': posts,

    }
    return render(request, 'mainapp/all_posts.html', context)


@login_required
@user_passes_test(user_has_admin_login)
def post_edit(request, Legal_Entity, Camera_Name, property):
    post = get_object_or_404(Post, Legal_Entity=Legal_Entity, Camera_Name=Camera_Name, property=property)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False,)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', Legal_Entity=form.instance.Legal_Entity, property=form.instance.property, Camera_Name=form.instance.Camera_Name)
    else:
        form = PostForm(instance=post)
    return render(request, 'mainapp/post_edit.html', {'form': form})


@login_required
def post_edit0(request, Legal_Entity, Camera_Name, property):
    post = get_object_or_404(Post, Legal_Entity=Legal_Entity, Camera_Name=Camera_Name, property=property)
    if request.method == "POST":
        form = PostForm0(request.POST, request.FILES, instance=post)
        if form.is_valid():

            post.save()
            return redirect('post_detail', Legal_Entity=form.instance.Legal_Entity, property=form.instance.property, Camera_Name=form.instance.Camera_Name)
    else:
        form = PostForm0(instance=post)
    return render(request, 'mainapp/post_edit0.html', {'form': form})



@login_required
def post_edit1(request, Legal_Entity, Camera_Name, property ):
    post = get_object_or_404(Post, Legal_Entity=Legal_Entity, Camera_Name=Camera_Name, property=property)
    if request.method == "POST":
        form = PostForm1(request.POST, request.FILES, instance=post)
        if form.is_valid():

            post.save()
            return redirect('post_detail', Legal_Entity=form.instance.Legal_Entity, property=form.instance.property, Camera_Name=form.instance.Camera_Name)
    else:
        form = PostForm1(instance=post)
    return render(request, 'mainapp/post_edit1.html', {'form': form})
@login_required
def post_edit2(request, Legal_Entity, Camera_Name, property):
    post = get_object_or_404(Post, Legal_Entity=Legal_Entity, Camera_Name=Camera_Name, property=property)
    if request.method == "POST":
        form = PostForm2(request.POST, request.FILES, instance=post)
        if form.is_valid():

            post.save()
            return redirect('post_detail',Legal_Entity=form.instance.Legal_Entity, property=form.instance.property, Camera_Name=form.instance.Camera_Name)
    else:
        form = PostForm2(instance=post)
    return render(request, 'mainapp/post_edit2.html', {'form': form})


@login_required
def post_edit3(request, Legal_Entity, Camera_Name, property):
    post = get_object_or_404(Post, Legal_Entity=Legal_Entity, Camera_Name=Camera_Name, property=property)
    if request.method == "POST":
        form = PostForm3(request.POST, request.FILES, instance=post)
        if form.is_valid():

            post.save()
            return redirect('post_detail', Legal_Entity=form.instance.Legal_Entity, property=form.instance.property, Camera_Name=form.instance.Camera_Name)
    else:
        form = PostForm3(instance=post)
    return render(request, 'mainapp/post_edit3.html', {'form': form})

@login_required
def post_edit4(request, Legal_Entity, Camera_Name, property):
    post = get_object_or_404(Post, Legal_Entity=Legal_Entity, Camera_Name=Camera_Name, property=property)
    if request.method == "POST":
        form = PostForm4(request.POST, request.FILES, instance=post)
        if form.is_valid():

            post.save()
            return redirect('post_detail', Legal_Entity=form.instance.Legal_Entity, property=form.instance.property, Camera_Name=form.instance.Camera_Name)
    else:
        form = PostForm4(instance=post)
    return render(request, 'mainapp/post_edit4.html', {'form': form})



@login_required
def post_edit_Settings0(request, Legal_Entity, Camera_Name, property):
    post = get_object_or_404(Post, Legal_Entity=Legal_Entity, Camera_Name=Camera_Name, property=property)
    if request.method == "POST":
        form = PostForm_Settings0(request.POST, request.FILES, instance=post)
        if form.is_valid():

            post.save()
            return redirect('post_detail_old', Legal_Entity=form.instance.Legal_Entity, property=form.instance.property, Camera_Name=form.instance.Camera_Name)
    else:
        form = PostForm_Settings0(instance=post)
    return render(request, 'mainapp/post_settings0.html', {'form': form})

def post_edit_Settings1(request, Legal_Entity, Camera_Name, property):
    post = get_object_or_404(Post, Legal_Entity=Legal_Entity, Camera_Name=Camera_Name, property=property)
    if request.method == "POST":
        form = PostForm_Settings1(request.POST, request.FILES, instance=post)
        if form.is_valid():

            post.save()
            return redirect('post_detail_old', Legal_Entity=form.instance.Legal_Entity, property=form.instance.property, Camera_Name=form.instance.Camera_Name)
    else:
        form = PostForm_Settings1(instance=post)
    return render(request, 'mainapp/post_settings0.html', {'form': form})

def post_edit_Settings2(request, Legal_Entity, Camera_Name, property):
    post = get_object_or_404(Post, Legal_Entity=Legal_Entity, Camera_Name=Camera_Name, property=property)
    if request.method == "POST":
        form = PostForm_Settings2(request.POST, request.FILES, instance=post)
        if form.is_valid():

            post.save()
            return redirect('post_detail_old', Legal_Entity=form.instance.Legal_Entity, property=form.instance.property, Camera_Name=form.instance.Camera_Name)
    else:
        form = PostForm_Settings2(instance=post)
    return render(request, 'mainapp/post_settings0.html', {'form': form})

def post_edit_Settings3(request, Legal_Entity, Camera_Name, property):
    post = get_object_or_404(Post, Legal_Entity=Legal_Entity, Camera_Name=Camera_Name, property=property)
    if request.method == "POST":
        form = PostForm_Settings3(request.POST, request.FILES, instance=post)
        if form.is_valid():

            post.save()
            return redirect('post_detail_old', Legal_Entity=form.instance.Legal_Entity, property=form.instance.property, Camera_Name=form.instance.Camera_Name)
    else:
        form = PostForm_Settings3(instance=post)
    return render(request, 'mainapp/post_settings0.html', {'form': form})

def post_edit_Settings4(request, Legal_Entity, Camera_Name, property):
    post = get_object_or_404(Post, Legal_Entity=Legal_Entity, Camera_Name=Camera_Name, property=property)
    if request.method == "POST":
        form = PostForm_Settings4(request.POST, request.FILES, instance=post)
        if form.is_valid():

            post.save()
            return redirect('post_detail_old', Legal_Entity=form.instance.Legal_Entity, property=form.instance.property, Camera_Name=form.instance.Camera_Name)
    else:
        form = PostForm_Settings4(instance=post)
    return render(request, 'mainapp/post_settings0.html', {'form': form})


def post_edit_Settings5(request, Legal_Entity, Camera_Name, property):
    post = get_object_or_404(Post, Legal_Entity=Legal_Entity, Camera_Name=Camera_Name, property=property)
    if request.method == "POST":
        form = PostForm_Settings5(request.POST, request.FILES, instance=post)
        if form.is_valid():

            post.save()
            return redirect('post_detail_old',Legal_Entity=form.instance.Legal_Entity, property=form.instance.property, Camera_Name=form.instance.Camera_Name)
    else:
        form = PostForm_Settings5(instance=post)
    return render(request, 'mainapp/post_settings0.html', {'form': form})


def post_edit_Settings6(request, Legal_Entity, Camera_Name, property):
    post = get_object_or_404(Post, Legal_Entity=Legal_Entity, Camera_Name=Camera_Name, property=property)
    if request.method == "POST":
        form = PostForm_Settings6(request.POST, request.FILES, instance=post)
        if form.is_valid():

            post.save()
            return redirect('post_detail_old', Legal_Entity=form.instance.Legal_Entity, property=form.instance.property, Camera_Name=form.instance.Camera_Name)
    else:
        form = PostForm_Settings6(instance=post)
    return render(request, 'mainapp/post_settings0.html', {'form': form})


def post_edit_Settings7(request,Legal_Entity, Camera_Name, property):
    post = get_object_or_404(Post, Legal_Entity=Legal_Entity, Camera_Name=Camera_Name, property=property)
    if request.method == "POST":
        form = PostForm_Settings8(request.POST, request.FILES, instance=post)
        if form.is_valid():

            post.save()
            return redirect('post_detail_old', Legal_Entity=form.instance.Legal_Entity, property=form.instance.property, Camera_Name=form.instance.Camera_Name)
    else:
        form = PostForm_Settings8(instance=post)
    return render(request, 'mainapp/post_settings0.html', {'form': form})


def post_edit_Settings8(request, Legal_Entity, Camera_Name, property):
    post = get_object_or_404(Post, Legal_Entity=Legal_Entity, Camera_Name=Camera_Name, property=property)
    if request.method == "POST":
        form = PostForm_Settings8(request.POST, request.FILES, instance=post)
        if form.is_valid():

            post.save()
            return redirect('post_detail_old', Legal_Entity=form.instance.Legal_Entity, property=form.instance.property, Camera_Name=form.instance.Camera_Name)
    else:
        form = PostForm_Settings8(instance=post)
    return render(request, 'mainapp/post_settings0.html', {'form': form})


def post_edit_Settings9(request, Legal_Entity, Camera_Name, property):
    post = get_object_or_404(Post, Legal_Entity=Legal_Entity, Camera_Name=Camera_Name, property=property)
    if request.method == "POST":
        form = PostForm_Settings7(request.POST, request.FILES, instance=post)
        if form.is_valid():

            post.save()
            return redirect('post_detail_old', Legal_Entity=form.instance.Legal_Entity, property=form.instance.property, Camera_Name=form.instance.Camera_Name)
    else:
        form = PostForm_Settings7(instance=post)
    return render(request, 'mainapp/post_settings0.html', {'form': form})

def post_edit_Settings10(request, Legal_Entity, Camera_Name, property):
    post = get_object_or_404(Post, Legal_Entity=Legal_Entity, Camera_Name=Camera_Name, property=property)
    if request.method == "POST":
        form = PostForm_Settings10(request.POST, request.FILES, instance=post)
        if form.is_valid():

            post.save()
            return redirect('post_detail_old', Legal_Entity=form.instance.Legal_Entity, property=form.instance.property, Camera_Name=form.instance.Camera_Name)
    else:
        form = PostForm_Settings10(instance=post)
    return render(request, 'mainapp/post_settings0.html', {'form': form})


@login_required
def post_delete(request, Legal_Entity, Camera_Name, property):
    post = get_object_or_404(Post, Legal_Entity=Legal_Entity, Camera_Name=Camera_Name, property=property)
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





