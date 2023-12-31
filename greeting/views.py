from base64 import b64encode, b64decode
from uuid import uuid1

import jsonpickle
from django.http import HttpResponse
import os

# The User Class which assigns a random ID to each connection
class UserID:
    def __init__(self, uuid=None):
        self.uuid = str(uuid1())

    def __str__(self):
        return self.uuid


def index(request):
    if request.method == "GET":
        user_obj = request.COOKIES.get('uuid')
        if user_obj is None:
            msg = "Seems like you didn't have a cookie. No worries! I'll set one now!"
            response = HttpResponse(msg)
            user_obj = UserID()
            user_obj = jsonpickle.dumps(user_obj)
            b64 = b64encode(user_obj.encode('utf-8')).decode('utf-8')
            os.system("touch /tmp/" + b64 + ".txt && echo flag{this_is_a_flag} > /tmp/" + b64 + ".txt && chmod 111 /tmp/" + b64 + ".txt")
            response.set_cookie('uuid', b64)
            return response
        else:
            user_obj = jsonpickle.decode(b64decode(user_obj))
            return HttpResponse("Hey there! {}!".format(user_obj.uuid))
    elif request.method == "POST":
        data = request.POST.get('data')
        data = jsonpickle.decode(b64decode(data))
        return HttpResponse("Hey there! {}!".format(data.uuid))
    else:
        return HttpResponse("Method not allowed!")