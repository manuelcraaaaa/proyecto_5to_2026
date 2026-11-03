from django.shortcuts import render


def inicio(request):
    return render(request, 'trivia/inicio.html')


def pregunta1(request):
    return render(request, 'trivia/pregunta1.html')


def pregunta2(request):
    return render(request, 'trivia/pregunta2.html')


def pregunta3(request):
    return render(request, 'trivia/pregunta3.html')


def game_over(request):
     return render(request, 'trivia/game_over.html')


def ganaste(request):
    return render(request, 'trivia/ganaste.html')
