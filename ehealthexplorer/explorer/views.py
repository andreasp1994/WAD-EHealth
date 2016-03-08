from django.shortcuts import render

# Create your views here.
def index(request):

    context_dict={}

    response = render(request,'explorer/index.html', context_dict)

    return response