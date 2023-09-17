from django.http import HttpResponse
import jsonpickle
import os
from base64 import b64encode, b64decode
from uuid import uuid1


# The User Class which assigns a random ID to each connection
class UserID:
    def __init__(self, uuid=None):
        self.uuid = str(uuid1())

    def __str__(self):
        return self.uuid


def index(request):
    user_obj = request.COOKIES.get('uuid')
    if user_obj is None:
        msg = "Seems like you didn't have a cookie. No worries! I'll set one now!"
        response = HttpResponse(msg)
        user_obj = UserID()
        user_obj = jsonpickle.dumps(user_obj)
        b64 = b64encode(user_obj.encode('utf-8')).decode('utf-8')
        response.set_cookie('uuid', b64)
        return response
    else:
        user_obj = jsonpickle.decode(b64decode(user_obj))
        return HttpResponse("Hey there! {}!".format(user_obj.uuid))
