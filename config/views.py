from django.shortcuts import render
import datetime

def page1(request):
    time = datetime.datetime.now().strftime('%H:%M:%S.%f')[:-4]
    context = {
        "time": time
    }
    return render(request, "page1.html", context)

def page2(request):
    date = datetime.datetime.now().date()
    context = {
        "date": date
    }
    return render(request, "page2.html", context)

def page3(request):
    return render(request, "page3.html")