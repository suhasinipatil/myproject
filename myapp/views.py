from django.http import JsonResponse
import json
import os
from django.conf import settings

def get_data(request):
    # Assuming the JSON file is in the same directory as views.py
    with open(os.path.join(settings.BASE_DIR, 'myapp', 'data.json')) as f:
        data = json.load(f)
    return JsonResponse(data)


from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World!")
