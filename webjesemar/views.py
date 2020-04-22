from django.shortcuts import render

# Create your views here.

def webjesemar_list(request):
    return render(request, 'blog/webjesemar_list.html', {})