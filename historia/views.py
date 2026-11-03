from django.shortcuts import render




def inicio(request):
    return render(request, 'historia/inicio.html')




def bosque(request):
    return render(request, 'historia/bosque.html')




def torre(request):
    return render(request, 'historia/torre.html')




def final_bueno(request):
    return render(request, 'historia/final_bueno.html')




def final_malo(request):
    return render(request, 'historia/final_malo.html')
