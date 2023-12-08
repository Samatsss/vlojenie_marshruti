from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.contrib.auth import authenticate
from django.core.serializers.json import DjangoJSONEncoder

def index(request):
    return HttpResponse("Главная Страница")

def posts(request):
    return HttpResponse("Тут находятся все посты")

def post(request, id):
    return HttpResponse(f"Пост: {id}")

def top(request):
    return HttpResponse("Популярные посты")

def last(request):
    return HttpResponse("Последние опубликованные посты")

def all(request):
    return HttpResponse("Весь набор постов")

def comments(request, id):
    return HttpResponse(f"Комментарий о посте: {id}")

def likes(request, id):
    return HttpResponse(f"Поставить лайк посту: {id}")

def user(request):
    age = request.GET.get("age")
    name = request.GET.get("name")
    return HttpResponse(f"<h2>Имя: {name} Возраст: {age}</h2>")

def about(request):
    return HttpResponse('About')

def contacts(request):
    return HttpResponseRedirect('/about')

def details(request):
    return HttpResponsePermanentRedirect('/')


def access_page(request):
    username = request.GET.get('username')
    password = request.GET.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None and user.username == 'admin':
        return HttpResponse("Все норм")
    else:
        response = HttpResponse("Unauthorized")
        response.status_code = 401
        return response
# При обращении к /access/?username=admin&password=admin, вы должны получить "Все норм"


def json(request):
    bob = Person("Bob", 45)
    return JsonResponse(bob, safe=False, encoder=PersonEncoder)

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

class PersonEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {"name": obj.name, "age": obj.age}
        return super().default(obj)


def set(request):
    username = request.GET.get("username", "Undefined")
    response = HttpResponse(f"Hello {username}")
    response.set_cookie("username", username)
    return response

def get(request):
    username = request.COOKIES["username"]
    return HttpResponse(f"Hello {username}")