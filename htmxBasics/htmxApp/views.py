from django.shortcuts import render
import requests

def users(request):
    data = requests.get('http://127.0.0.1:8000/api/personnel')
    users = data.json()
    first_names = ", ".join(user["first_name"] for user in users)
    context = {'first_names': first_names}
    return render(request, 'htmxApp/index.html', context)
