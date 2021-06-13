from django.shortcuts import render, HttpResponse, redirect
from daily.models import DailyResult
from daily.templatetags import extras
import math
# Create your views here.
def dailyHome(request):
    no_of_posts = 7
    page = request.GET.get('pageno')
    if page is None:
        page = 1
    else:
        page = int(page)
    # print(page)
    
    length = len(DailyResult.objects.all())
    allPosts = DailyResult.objects.all().order_by('-timeStamp')[(page-1)*no_of_posts:page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    
    if page<math.ceil(length/no_of_posts):
        nxt = page + 1
    else:
        nxt = None




    context ={'allPosts':allPosts, 'prev':prev , 'nxt':nxt}
    return render(request, 'daily/dailyHome.html',context)

def dailyResults(request, slug):
    # return render(request, 'daily/dailyResults.html')
    post = DailyResult.objects.filter(slug=slug).first()
    
    context = {'post':post}
    return render(request, 'daily/dailyResults.html', context)