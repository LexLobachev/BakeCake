import datetime
from django.contrib.auth.views import LoginView
from django.shortcuts import render

from more_itertools import chunked

from django.views.generic import TemplateView


from order.models import Order
from .models import Cake

CASTOM_CAKE = {
    'Levels': ['не выбрано', '1', '2', '3'],
    'Forms': ['не выбрано', 'Круг', 'Квадрат', 'Прямоугольник'],
    'Toppings': ['не выбрано', 'Без топпинга', 'Белый соус', 'Карамельный', 'Кленовый', 'Черничный',
                 'Молочный шоколад', 'Клубничный'],
    'Berries': ['нет', 'Ежевика', 'Малина', 'Голубика', 'Клубника'],
    'Decors': ['нет', 'Фисташки', 'Безе', 'Фундук', 'Пекан', 'Маршмеллоу', 'Марципан'],
}


def create_order(results):
    levels = CASTOM_CAKE['Levels'][int(results["LEVELS"])]
    forms = CASTOM_CAKE['Forms'][int(results["FORM"])]
    topping = CASTOM_CAKE['Toppings'][int(results["TOPPING"])]
    berries = 'Без ягод'
    if "BERRIES" in results:
        berries = CASTOM_CAKE['Berries'][int(results["BERRIES"])]
    decor = 'Без декора'
    if "DECOR" in results:
        decor = CASTOM_CAKE['Decors'][int(results["DECOR"])]
    words = results["WORDS"]
    comment = results["COMMENTS"]
    name = results["NAME"]
    phone = results["PHONE"]
    email = results["EMAIL"]
    address = results["ADDRESS"]
    date_time_str = f'{results["DATE"]} {results["TIME"]}'
    date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')
    deliv_date = date_time_obj.date()
    deliv_time = date_time_obj.time()
    deliv_comment = results["DELIVCOMMENTS"]
    price = results["PRICE"]

    Order.objects.create(
        name=name,
        price=price,
        phonenumber=phone,
        address=address,
        comment=comment,
        delivery_date=deliv_date,
        delivery_time=deliv_time,
        levels=levels,
        form=forms,
        topping=topping,
        berries=berries,
        decor=decor,
        inscription=words,
        deliv_comment=deliv_comment,
        email=email
    )


def index(request):
    if "TOPPING" in request.GET:
        results = request.GET
        create_order(results)
    return render(request, 'index.html')


def show_catalog(request):
    columns_count = 2
    cakes = Cake.objects.all()
    page_columns = list(chunked(cakes, columns_count))
    return render(request, template_name='catalog.html', context={
        'page_columns': page_columns,
    })


def show_main_page(request):
    return render(request, 'index.html')

