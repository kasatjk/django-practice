from django.shortcuts import render

def home(request):
    """Головна сторінка порталу."""
    return render(request, "shell.html")

def about_city(request):
    """Головна сторінка розділу 'Про місто (Одеса)'."""
    return render(request, "about-city.html")

def city_facts(request):
    """Підрозділ: Цікаві факти про місто."""
    return render(request, "city-facts.html")

def city_data(request):
    """Підрозділ: Дані та статистика міста."""
    return render(request, "city-data.html")

def about_me(request):
    """Головна сторінка розділу 'Про мене'."""
    return render(request, "about-me.html")

def me_bio(request):
    """Підрозділ: Біографія."""
    return render(request, "me-bio.html")

def me_facts(request):
    """Підрозділ: Цікаві факти про мене."""
    return render(request, "me-facts.html")
