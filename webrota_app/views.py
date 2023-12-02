from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from django.conf import settings

from .forms import MyForm
from .models import Shifting




def get_google_calendar_service():
    credentials = service_account.Credentials.from_service_account_file(
        settings.GOOGLE_CALENDAR_JSON_KEYFILE_PATH,
        scopes = ['https://www.googleapis.com/auth/calendar'],
    )

    # Create a Google Calendar API service
    service = build('calendar', 'v3', credentials=credentials)
    return service

def google_calendar(request):
    service = get_google_calendar_service()
    shifts = Shifting.objects.all()
    events = []
    for shift in shifts:
        events.append({
            'summary': 'Shift',
            'description': '{{ shift.user }}'
        })
    #event = service.events().insert(calendarId='primary', body=events).execute()
    #print(f'Event created: {event.get("htmlLink")}')
    context = {'calendar_url': shifts}
    return render(request,'google_calendar.html', context)

def home(request):
    if request.method =='POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # user = request.POST['user']
            # date = request.POST['date']
            # shift = request.POST['shift']
            user = form.cleaned_data['user']
            date = request.POST['date']
            shift = form.cleaned_data['shift']

            form = Shifting.objects.create(user = user, date = date, shift = shift)
            #form = form.save()
            return render(request, 'calendar.html', {'form':form})
    else:
        form = MyForm()
    return render(request, 'base.html',{'form':form})

def calendar(request):
    form = MyForm(request.POST)

    if form.is_valid():
        user = form.cleaned_data['user']
        date = form.cleaned_data['date']
        shift = form.cleaned_data['shift']

        #date_new = datetime.strptime(date, '%Y-%m-%d').date()#%d %b %Y
        #date = datetime.strftime('%Y-%m-%d')

        


        #form = Shifting.objects.create(user = user, date = date, shift = shift)
        form = Shifting(user = user, date = date, shift = shift)
        form.save()


    
    form = Shifting.objects.all()
    return render(request, 'calendar.html', {'form': form})
