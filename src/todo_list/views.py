from django.shortcuts import render

# Create your views here.
def mainApp(request):
    return render(request, 'todo_list/index.html', {})
