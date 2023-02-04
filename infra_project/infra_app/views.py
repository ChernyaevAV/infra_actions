from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось. Запустил приложение в докере'
                        'на удаленном сервере!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
