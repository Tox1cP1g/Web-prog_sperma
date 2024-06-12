from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Articles

# Create your views here.


def like_task(request, article_id):
    task = Articles.objects.get(pk=article_id)
    task.likes_count += 1
    task.save()
    return JsonResponse({'likes': task.likes_count})


def get_likes_count(request):
    articles = Articles.objects.all()

    res = {i.pk: i.likes_count for i in articles}

    return JsonResponse({'result': res})
