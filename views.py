from coder_news import models
from django.http import HttpResponse, JsonResponse
import random


def add_user(request):
    username = request.GET.get('username', '')
    password = request.GET.get('password', '')
    try:
        models.User.objects.create(username=username, password=password)
    except:
        return HttpResponse("用户名已存在！")
    return HttpResponse("username="+username+"password"+password)


def login(request):
    username = request.GET.get('username', '')
    password = request.GET.get('password', '')
    print(username)
    print(password)
    try:
        models.User.objects.get(username__exact=username, password__exact=password)
    except:
        return HttpResponse("用户名或密码错误！")
    return HttpResponse("登录成功！")


def find_topic(request):
    category = request.GET.get('categoryArray', '')
    category = category.split(",")
    amount = int(request.GET.get('infoAmount', ''))
    r = random.randint(1, 50)
    count = int(amount/len(category))
    news = {"list": []}
    i = 1
    for cat in category:
        print(cat)
        if i == len(category):
            print(i)
            topic = models.Info.objects.filter(category=cat)[r:amount-count*(i-1)+r].values("title", "url", "imageURL", "category")
        else:
            topic = models.Info.objects.filter(category=cat)[r:r+count].values("title", "url", "imageURL", "category")
        news["list"].append(list(topic))
        i += 1
    return JsonResponse(news, json_dumps_params={'ensure_ascii': False}, safe=False)
    # return HttpResponse('topic:'+topic.topic+'\nurl:'+topic.url)

