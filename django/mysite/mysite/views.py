__author__ = 'mehow'
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
import sys
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
import socket
import simplejson

def get(self, request, *args, **kwargs):
    return HttpResponse('Hello, World!')


def index(request):

    template = loader.get_template('control/index.html')
    context = RequestContext(request,
    {

        'jakkolwiek':'dupa'

    })
    return HttpResponse(template.render(context))

def control(request,device,action):

    if request.user.is_authenticated():
        action_table={"blink":0,"off":1,"on":2,"toggle":3}
        device = int(device)
        msg_code=chr(device*4+action_table[action] + 65)
        print msg_code

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("192.168.0.12", 9090))
        s.sendall(str(msg_code))
        s.close()

    else:
        body_text = "Not Logged in!"

    #template = loader.get_template('control_panel/control.html')

    return HttpResponse('OK')
def login_page(request):

    if not request.user.is_authenticated():
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            context = RequestContext(request,
            {
            'status': "Login Success!"
            })
            #redirect to success page

        else:
            context = RequestContext(request,
            {
            'status': "Login Failed!"
            })

        template = loader.get_template('control/login.html')

        return HttpResponse(template.render(context))

    else:
        #todo: already logged in
        template = loader.get_template('control/login.html')


        context = RequestContext(request,
        {
        'status': "Already logged in!"
        })


        return HttpResponse(template.render(context))

def logout_page(request):
    logout(request)
    template = loader.get_template('control/logout.html')
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))
def send_light(request):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.0.12", 9090))
    s.sendall("Z\n")

    response = s.recv(4)
    s.close()
    response = response.replace("\n","")

    serialized_data = simplejson.dumps({"value": response})
    return HttpResponse(serialized_data, content_type="application/json")


