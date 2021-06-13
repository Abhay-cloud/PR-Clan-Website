from django.shortcuts import render, HttpResponse, redirect
from weekly.models import WeeklyResult
from weekly.templatetags import extras
import math
# Create your views here.
def weeklyHome(request):
    no_of_posts = 7
    page = request.GET.get('pageno')
    if page is None:
        page = 1
    else:
        page = int(page)
    # print(page)
    
    length = len(WeeklyResult.objects.all())
    allPosts = WeeklyResult.objects.all().order_by('-timeStamp')[(page-1)*no_of_posts:page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    
    if page<math.ceil(length/no_of_posts):
        nxt = page + 1
    else:
        nxt = None




    context ={'allPosts':allPosts, 'prev':prev , 'nxt':nxt}
    return render(request, 'weekly/weeklyHome.html',context)

def weeklyResults(request, slug):
    # return render(request, 'daily/dailyResults.html')
    post = WeeklyResult.objects.filter(slug=slug).first()
    
    context = {'post':post}
    return render(request, 'weekly/weeklyResults.html',context)