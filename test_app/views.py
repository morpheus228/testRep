from django.views import View
from django.http import HttpResponse


class WebHook(View):

    def post(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')