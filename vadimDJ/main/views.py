from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница CURVA BOBER',
        'values': ['Бобры', 'Телки', 'Бабки'],
        'obj': {
            '1': "One",
            '2': "Two",
            '3': "Three",
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    data = {
        'title': 'О нас',
        'values': ['Сасные', 'Крутые', 'Жоские']
    }
    return render(request, 'main/about.html', data)
