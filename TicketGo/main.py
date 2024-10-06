import os
from random import choice, randint
import django
from django.core.paginator import Paginator
from datetime import datetime, timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TicketGo.settings")
django.setup()

from api.models import Bus, Company

states = [
    # 'Вінниця', 'Дніпро', 'Донецьк', 'Житомир',
    # 'Запоріжжя', 'Івано-Франківськ', 'Київ', 'Кропивницький',
    # 'Луганськ', 'Луцьк', 'Львів', 'Миколаїв',
    # 'Одеса', 'Полтава', 'Рівне', 'Суми',
    # 'Тернопіль', 'Ужгород', 'Харків', 'Херсон',
    # 'Хмельницький', 'Черкаси', 'Чернівці', 'Чернігів'
]

# companies = Company.objects.all()

paginator_objects = Paginator(states, 4)
# print(paginator_objects.count)
# print(paginator_objects.num_pages)
for i in paginator_objects:
    print(i.object_list)
# print(choice(companies))
# print(datetime.now())
# print(datetime.now() + timedelta(days=1, hours=-3))
#
# print(Bus.objects.get(id=1).departure_time)

# for i in range(3):
#     # old_town = choice(states)
#     # new_town = choice(states)
#     # while old_town == new_town:
#     #     new_town = choice(states)
#
#     old_town = 'Чернігів'
#     new_town = 'Черкаси'
#     print(old_town, '-->', new_town)
#
#     Bus.objects.create(
#         company_name=choice(companies),
#         from_location=old_town,
#         to_location=new_town,
#         departure_time=datetime.now(),
#         arrival_time=datetime.now() + timedelta(days=1, hours=-3),
#         price=choice(range(10, 20)),
#         available_seats=choice([35, 40, 45]),
#         wi_fi_availability=choice(['No', 'Yes']),
#         socket_availability=choice(['No', 'Yes']),
#         toilets_available=choice(['No', 'Yes']),
#         conditioner_available=choice(['No', 'Yes'])
#     )
