from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse

import json
import logging
from main import forms as f


def index(request):
    return render(request, template_name='index.html')


def contact_us(request):
    if request.method == 'POST':
        form = f.ContactFormF(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, template_name='contact_us.html', context={"form": form})
    else:
        return render(request, template_name='contact_us.html')


def about_us(request):
    return render(request, template_name='about_us.html')


def profile(request):
    return render(request, template_name='profile.html')


def traceback(request):
    if not request.body:
        return render(request, template_name='base.html')

    comp = intr.Interpreter()
    prequest = json.loads(request.body)

    if prequest['type'] == 'initial':
        comp.code(prequest['text'])

    logging.basicConfig(filename="logs/traceback.log", level=logging.DEBUG)

    resp = JsonResponse(comp.run(prequest['text']))
    resp['Access-Control-Allow-Origin'] = 'null'

    return resp


def join_session(request):
    return render(request, template_name='join_session.html')