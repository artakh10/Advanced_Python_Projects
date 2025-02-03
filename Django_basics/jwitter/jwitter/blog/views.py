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