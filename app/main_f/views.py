from django.shortcuts import render
from main_f.models import Message, User_list
from main_f.forms import MessageForm, UserForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import requests


def index(request):
    args = {}
    args['user_form'] = UserForm()
    args['message_form'] = MessageForm()
    if request.session.get('name', None) == '':
        del request.session['name']
    return render(request, 'main_f/index.html', args)


@csrf_exempt
def message(request):
    if request.POST:
        reciever = request.POST.get('data_1', '')
        text = request.POST.get('data_2', '')

        try:
            url = 'http://jsonplaceholder.typicode.com/users'
            params = dict(username=reciever)
            resp = requests.get(url=url, params=params)
            data = json.loads(resp.text)
            message = Message(
                reciever=reciever, text=text, additional=data[0]["email"]
            )
            message.save()
            return JsonResponse({'status': 'send message'})
        except:
            message = Message(
                status='nobody gets it', reciever=reciever, text=text
            )
            message.save()
            return JsonResponse({'status': 'wrong reciever'})
    else:
        return JsonResponse({'status': 'failed post'})


@csrf_exempt
def user_in(request):
    if request.POST:
        username = request.POST.get('data_1', '')
        password = request.POST.get('data_2', '')
        try:
            obj = User_list.objects.get(login=username, password=password)
            request.session['name'] = username
            return JsonResponse({'status': 'login success'})
        except User_list.DoesNotExist:
            if User_list.objects.filter(login=username):
                return JsonResponse({'status': 'wrong password'})
            else:
                obj = User_list(login=username, password=password)
                obj.save()
                request.session['name'] = username
                return JsonResponse({'status': 'registration success'})
    else:
        return JsonResponse({'status': 'failed post'})


@csrf_exempt
def user_out(request):
    if request.session.get('name'):
        del request.session['name']
    return JsonResponse({'status': 'logout'})
