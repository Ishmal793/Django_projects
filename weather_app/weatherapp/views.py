from django.shortcuts import render
import requests
import datetime
from django.contrib import messages



# AIzaSyDkPHl5Oa62ZWnoQLJ2NeAq3-Twm9VZIHw
def home(request):
    if request.method == "POST":
        city = request.POST.get('city')
    else:
        city ="Gujranwala"

    API_KEY = "6483bd1bd35c7a15eb1ab9f92671b39e"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    API_KEY_google ='AIzaSyDkPHl5Oa62ZWnoQLJ2NeAq3-Twm9VZIHw'
    SEARCH_ENGINE_ID='c6b85dfca35224de0'

    query = city + " 1920x1080"
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY_google}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"
     
    data = requests.get(city_url).json()
    count = 1
    search_items=data.get("items")
    image_urls=search_items[1]['link']
    try:

        response = requests.get(url)
        data = response.json()
        # Example of extracting some data:
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        day= datetime.date.today()
        context = {
        'city': city,
        'temp': temp,
        'description': description,
        'icon': icon,
        'day':day,
        'exception_occurred':False,
        'image_urls':image_urls,


    }
        return render(request, 'index.html', context)
    except:
        exception_occurred=True
        messages.error(request,'enter data not available in API')
        day= datetime.date.today()
        context = {
            'city': 'Gujranwla',
            'temp': 25,
            'description': 'clear sky',
            'icon': '01d' ,
            'day':day,
            'exception_occurred':exception_occurred,
        }
        return render(request, 'index.html', context)
        


