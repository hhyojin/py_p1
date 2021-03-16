from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.db import connection # DB SQL 이용
from collections import namedtuple # dictfetchall(cursor) 에서 사용


def dictfetchall(cursor):
    # "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def index(request):
    with connection.cursor() as cursor:
        cursor.execute("select user, user_email from m_user")
        user_list = dictfetchall(cursor)
        cursor.close()

    context = {'user_list': user_list}

    return render(request, 'user/user.html', context)