from django.shortcuts import render

# Create your views here.
def index(request):

    context_dict={}

    response = render(request,'explorer/index.html', context_dict)

    return response
    
def results(request):
    context_dict={'results':[{'title':'google','url':'http://www.google.co.uk'}]}   ## Placeholder until search function
    response = render(request,'explorer/results.html',context_dict)                 ## can be used.
    return response