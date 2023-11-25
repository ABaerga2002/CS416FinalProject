from django.shortcuts import render, redirect
import requests
from datetime import datetime
from django.contrib import messages
from .models import EventList


def get_events(location, search_term):
    try:
        url = "https://app.ticketmaster.com/discovery/v2/events.json"

        params = {
            "city": location,
            "classificationName": search_term,
            "API_KEY": "GCKxxpg0KUZXuCTZsYllPo2bAjvYz9Xh",
            "sort": "date,asc"
        }

        response = requests.get(url, params=params)

        response.raise_for_status()

        data = response.json()

        return data
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

        return None


def index(request):
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
            current_events = events['results']

            event_list = []

        for event in current_events:
            eventName = event["_embedded"]["events"][event]["name"]
            imageURL = event["_embedded"]["events"][event]["images"][0]["url"]
            eventDate = event["_embedded"]["events"][event]["dates"]["start"]["dateTime"]
            venueName = event["_embedded"]["events"][event]["_embedded"]["venues"][0]["name"]
            venueCity = event["_embedded"]["events"][event]["_embedded"]["venues"][0]["city"]["name"]
            venueState = event["_embedded"]["events"][event]["_embedded"]["venues"][0]["state"]["name"]
            venueAdd = event["_embedded"]["events"][event]["_embedded"]["venues"][0]["address"]["line1"]
            eventURL = event["_embedded"]["events"][event]["url"]

            date_object = datetime.strptime(eventDate[:10], "%Y-%m-%d")
            eventDate = date_object.strftime("%a %b %d %Y")
            time_object = datetime.strptime(eventDate[:6], "%I:%M%p %Z")
            eventTime = time_object.strftime("%H:%M %Z")

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

        context = {'events': event_list}
        return render(request, 'ticketmaster/index.html', context)

    return render(request, "ticketmaster/index.html")


