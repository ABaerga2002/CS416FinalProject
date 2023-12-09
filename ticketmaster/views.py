from django.shortcuts import render, redirect
import requests
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import UserRegistrationForm
from .models import EventList


def register_veiws(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('ticketmaster-index')
    else:
        form = UserCreationForm(request.POST or None)
    context = {'form': form}
    return render(request, "ticketmaster/register.html", context)

def login_veiws(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('ticketmaster-index')
    else:
        form = AuthenticationForm(request.POST or None)

    context = {'form': form}
    return render(request, "ticketmaster/login.html", context)

def index(request):
    EventList.objects.all().delete()
    if request.method == 'POST':

        location = request.POST['city_term']
        searchTerm = request.POST['event_term']

        if not location or not searchTerm:
            messages.info(request, 'One or more fields are empty. Please enter all search information.')
            return redirect('ticketmaster-index')

        events = get_events(location, searchTerm)

        if events is None:
            messages.info(request, 'The server encountered an issue while fetching data. Please try again later.')
            return redirect('ticketmaster-index')

        else:
            print(events)
            eventCheck = events['page']['totalElements']
            if eventCheck is 0:
                messages.info(request, 'No results were found.')
                return redirect('ticketmaster-index')
            current_events = events['_embedded']["events"]

            event_list = []

        for event in current_events:
            eventName = event["name"]
            print(eventName)
            imageURL = event["images"][0]["url"]
            print(imageURL)
            if 'dates' in event and 'start' in event['dates'] and 'dateTime' in event['dates']['start']:
                eventDate = event["dates"]["start"]["dateTime"]
                date_object = datetime.strptime(eventDate, "%Y-%m-%dT%H:%M:%SZ")
                eventDate = date_object.strftime("%a %b %d %Y")
                print(eventDate)

                eventTime = event["dates"]["start"]["localTime"]

                if eventDate:
                    try:
                        timeObject = datetime.strptime(eventTime, "%H:%M:%S")
                        eventTime = timeObject.strftime("%I:%M %p")
                        print(eventTime)
                    except ValueError:
                        eventTime = "N/A"
                        print(eventTime)

            venueName = event["_embedded"]["venues"][0]["name"]
            print(venueName)
            venueCity = event["_embedded"]["venues"][0]["city"]["name"]
            print(venueCity)
            venueState = event["_embedded"]["venues"][0]["state"]["name"]
            print(venueState)
            venueAdd = event["_embedded"]["venues"][0]["address"]["line1"]
            print(venueAdd)
            eventURL = event["url"]
            print(eventURL)

            EventList.objects.create(eventName=eventName, eventDate=eventDate, eventTime=eventTime, eventURL=eventURL)

            event_details = {
                'eventName': eventName,
                'imageURL': imageURL,
                'eventDate': eventDate,
                'eventTime': eventTime,
                'venueName': venueName,
                'venueCity': venueCity,
                'venueState': venueState,
                'venueAdd': venueAdd,
                'eventURL': eventURL
            }

            event_list.append(event_details)

        context = {'eventList': event_list}
        return render(request, 'ticketmaster/index.html', context)

    return render(request, "ticketmaster/index.html")


def get_events(location, search_term):
    try:
        url = "https://app.ticketmaster.com/discovery/v2/events.json"

        params = {
            "city": location,
            "classificationName": search_term,
            "apikey": "GCKxxpg0KUZXuCTZsYllPo2bAjvYz9Xh",
            "sort": "date,asc"
        }

        response = requests.get(url, params=params)

        response.raise_for_status()

        data = response.json()

        return data

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

        return None


def logout_veiws(request):
    logout(request)
    return redirect('ticketmaster-index')