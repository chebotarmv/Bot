# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .bot_config import *

import json, vk


@csrf_exempt
def index(request):
    if (request.method == "POST"):
        data = json.loads(request.body)
        if (data['type'] == 'confirmation'):
            return HttpResponse(confirmation_token, content_type="text/plain", status=200)
        if (data['type'] == 'message_new'):
            session = vk.Session()
            api = vk.API(session, v=5.5)
            user_id = data['object']['user_id']
            api.messages.send(access_token = token, user_id = str(user_id), message = "Hello, I'm bot!")
            return HttpResponse('ok', content_type="text/plain", status=200)
    else:
        return HttpResponse('see you :)')