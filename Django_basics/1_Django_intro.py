'''
Specifically for the Advanced Python Programming Course
Author: Arta Khosravi
Last Update: Feb. 2025
'''
"""
PART 1:
"""
'''
For making a really simple pseudo-twitter, we need a user password login page, postings, etc.
Django set up an admin system and so on.
'''
'''
Necessary codes/commands for terminal/powershell:
~ mkdir jwitter
~ cd jwitter
~ py -m venv venv
~ Set-ExecutionPolicy Unrestricted -Scope Process
~ venv/Scripts/activate
~ py -m pip install django
~ django-admin startproject jwitter
~ django-admin
~ cd jwitter
~ code . (to see your code)
~ python manage.py starapp blog #starting a minimal project with an app inside
~ python manage.py runserver
#It'll give you an https adress such as this : http://127.0.0.1:8000/
that means the installation was successful.
'''
'''
In the "blog" app under jwitter/jwitter/blog, there's a file called views.
we can write : 
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("hi there.")
#It'll print hi there when there are no html pages.
'''
'''
Under jwitter/jwitter/blog/url.py (a new file):
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index')
]
'''
'''
Under jwitter/jwitter/jwitter/urls.py:
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('blog/', include('blog.url')),# new
    path('admin/', admin.site.urls),
]
'''
'''
Don't forget to run the:
python manage.py runserver
command in the powershell!
'''




"""
PART 2:
"""
'''
Now to give the user the ability to create posts:
In jwitter/jwitter/blog/models.py:
class post(models.Model):
    text = models.CharField(max_length=480)
    #as in maximum character length will be 480 letters, just like twitter.
'''
'''
COMMANDS in powershell:
 python manage.py makemigrations blog 
 #When I've changed my model, I'm gonna correct its-
 #-migration andchanges the database as it sees fit.
 #The default database is db.sqlite3. File based and simple.
output: No installed app with label 'blog'.
Thus, we need to create the blog app.

IN jwitter/jwitter/settings.py:
in the INSTALLED_APPS:
add 'blog.apps.BlogConfig',
and retry.
'''
'''
Now to work with the database, in powershell:
 python manage.py migrate
 #changes the database according to the model.
'''
'''
python manage.py createsuperuser:
Username: leave blank to use your C:'s username.
Email address: enter your email address.
Password: Enter your password.
Then, the superuser will be created.
This way, after running the server, and entering "http://127.0.0.1:8000/admin/",
you can login to your django. You can add Groups, Users, and etc.
'''
'''
I can in the admin of blog's app, say that add my post to admin.
so in jwitter/jwitter/blog/admin.py:
from .models import post
admin.site.register(post)

--- it is ran automatically in the powershell, and my post is added
in the admin section of the website.

It is important to note that the models mentioned here mean the concept of databases.
As in the class that was added.

By reloading the site/admin website, the post section is added and I can add a post.
But it will still not be shown on the ./blog part of the website.
'''
'''
For the post to appear on website/blog, I need to change ./blog/view:

from django.shortcuts import render
from django.http import HttpResponse
from blog.models import post
# Create your views here.
def index(request):
    ret = '<body>' #defining an html
    all_posts = post.objects.all() #show all the objects posted/created
    for posts in all_posts:
        ret = ret + '<p>' + posts.text + '</p>'
        #in each par, write the text of the post.
    ret = ret + '</body>'
    return HttpResponse(ret)

After re-running the website, your post which was created in the admin of django will appear! yay!
'''