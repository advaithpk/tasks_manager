from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from datetime import date,datetime
import requests
from rest_framework.renderers import JSONRenderer
from .serializers import TaskSerializer

# Create your views here.

@login_required
def main(request):
    api_url = 'http://127.0.0.1:8000/main/employees'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        employees = data
    else:
        print(f"Error: {response.status_code}")
        employees = []
    
    return render(request, 'main.html', {'employees': employees})

def emptasks(request):
    user_id = request.GET.get('user_id')
    api_url = f'http://127.0.0.1:8000/main/employees/{user_id}'
    response = requests.get(api_url)
    today = datetime.today().date()
    
    current_user = request.user.username

    if response.status_code == 200:
        tasks_data = response.json()
        serializer = TaskSerializer(data=tasks_data, many=True)
        if serializer.is_valid():
            tasks = serializer.validated_data
            for task in tasks:
                task_date = task['date']
                days_remaining = (task_date - today).days
                task['days_remaining'] = days_remaining
        else:
            print(serializer.errors)
            tasks = []
    else:
        print(f"Error: {response.status_code}")
        tasks = []

    return render(request, 'employee.html', {'tasks': tasks, 'current_user': current_user})

def logout(request):
    auth.logout(request)
    return redirect('/')