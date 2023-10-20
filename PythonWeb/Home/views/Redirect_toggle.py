from django.shortcuts import render
def redirectToggle(request):
    return render (request, 'onofftracking.html')
