from django.shortcuts import render, HttpResponse, redirect
from daily.models import DailyResult
from weekly.models import WeeklyResult
from home.models import Application
from django.contrib import messages
from news.models import News

# Create your views here.
def home(request):
    daily = DailyResult.objects.all().order_by('-timeStamp')
    weekly = WeeklyResult.objects.all().order_by('-timeStamp')
    news = News.objects.all()
    context = {'daily':daily,'weekly':weekly, 'news':news}
    
    return render(request, 'home/home.html',context)

def about(request):
    # return HttpResponse('About')
    return render(request, 'home/about.html')


def search(request):
    query = request.GET['query']
        
    daily = DailyResult.objects.all()
    weekly =WeeklyResult.objects.all()
    if len(query)>100:
            dailyPosts = DailyResult.objects.none()
            weeklyPosts = WeeklyResult.objects.none()
    else:
        # allPosts = Post.objects.all()
            dailyPosts = DailyResult.objects.filter(title__icontains=query)
            weeklyPosts = WeeklyResult.objects.filter(title__icontains=query)
            allPosts = dailyPosts.union(weeklyPosts).order_by('-timeStamp')

    if allPosts.count() == 0:
            messages.error(request, 'Please input correct search term')
    params = {'dailyPosts':dailyPosts , 'query':query, 'weeklyPosts':weeklyPosts,'allPosts':allPosts}
    return render(request, 'home/search.html',params)

# def application(request):

#     if request.method == 'POST':
#         username = request.POST['username']
#         timezone = request.POST['timezone']
#         country = request.POST['country']
#         age = request.POST['age']
#         Why_do_you_think_you_should_become_a_mod = request.POST['content']
#         How_long_can_you_be_active_on_the_server_everyday = request.POST['activetime']
#         past_experience = request.POST['pastexperience']
#         What_would_you_do_if_you_are_the_only_Mod_online_and_see_some_of_your_teammates_bullying_someone = request.POST['action1']
#         What_would_you_do_if_someone_breaks_the_rules = request.POST['action2']
#         What_would_you_do_if_someone_uses_N_word = request.POST['action3']
#         What_would_you_do_if_someone_pinging_mods_for_no_reason = request.POST['action4']
#         What_would_you_do_if_someone_starts_unnecessary_drama = request.POST['action5']

#         if len(username)<5 or len(timezone)<2 or len(country)<2 or len(age)<0 or len(Why_do_you_think_you_should_become_a_mod)<15 or len(How_long_can_you_be_active_on_the_server_everyday)<0 or len(past_experience)<1 or len(What_would_you_do_if_you_are_the_only_Mod_online_and_see_some_of_your_teammates_bullying_someone)<10 or len(What_would_you_do_if_someone_uses_N_word)<10 or len(What_would_you_do_if_someone_starts_unnecessary_drama)<10 or len(What_would_you_do_if_someone_pinging_mods_for_no_reason)<10 or len(What_would_you_do_if_someone_breaks_the_rules)<10:
#             return HttpResponse('<h1>Please fill the form correctly <a href="/apply">Back to the application page</a><h1>')

#         else:
#             apply = Application(username=username, timezone=timezone, country=country, age=age, Why_do_you_think_you_should_become_a_mod=Why_do_you_think_you_should_become_a_mod, How_long_can_you_be_active_on_the_server_everyday=How_long_can_you_be_active_on_the_server_everyday, past_experience=past_experience, What_would_you_do_if_you_are_the_only_Mod_online_and_see_some_of_your_teammates_bullying_someone=What_would_you_do_if_you_are_the_only_Mod_online_and_see_some_of_your_teammates_bullying_someone, What_would_you_do_if_someone_breaks_the_rules=What_would_you_do_if_someone_breaks_the_rules, What_would_you_do_if_someone_uses_N_word= What_would_you_do_if_someone_uses_N_word,What_would_you_do_if_someone_pinging_mods_for_no_reason=What_would_you_do_if_someone_pinging_mods_for_no_reason, What_would_you_do_if_someone_starts_unnecessary_drama=What_would_you_do_if_someone_starts_unnecessary_drama)
#             apply.save()
#             # messages.success(request , 'Your message has been sent.')
#             return HttpResponse("<h1>Your mod application has been successfully sent to our mods for review. We'll contact you shortly.<h1>")
        
#     return render(request, 'home/apply.html')

def application(request):
    return render(request, "home/appclosed.html")

def newyear(request):
    return render(request, "home/happynewyear.html")

def nitro(request):
    return render(request, "home/nitro.html")