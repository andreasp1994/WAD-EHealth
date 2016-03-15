from django.shortcuts import render
from explorer.bing_search import run_query
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from models import Category

@csrf_exempt
def index(request):

    context_dict = {}

    if request.method == "POST":

        task = request.POST['task']

        if (task == "AJAX_ADD_CATEGORY"):
            cat_name = request.POST['name']
            try:
                cat = Category.objects.create(name=cat_name,user=None)
            except Exception as e:
                print e


            # cat.save()

        return HttpResponse(json.dumps({'message': task}))

    #Load categories from database:
    category_list = Category.objects.all()
    context_dict['categories'] = category_list

    response = render(request,'explorer/index.html', context_dict)
    return response

def results(request):

    # bing_results=[{'title':'Google',
                   # 'url':'http://www.google.co.uk',
                   # 'summary':'A search engine for searching things',
                   # 'read':9,
                   # 'pola':5,
                   # 'subj':3}]
    bing_results=[]

    query = 'flu'.strip()       ## PLACEHOLDER todo
    
    if query:
        bing_results= run_query(query)

    medLine_results=[{'title':'Amazon',
                      'url':'http://www.amazon.co.uk',
                      'summary':'A place to buy stuff',
                      'read':3,
                      'pola':6,
                      'subj':4}]
    healthFinder_results=[]

    context_dict={'results':bing_results + medLine_results + healthFinder_results, 
                  'bing':bing_results,
                  'medLine':medLine_results,
                  'healthFinder':healthFinder_results 
                 } ## Placeholder until search function can be implemented
    

    response = render(request,'explorer/results.html',context_dict)   
    return response

def favourites_sidebar(request):

    context_dict={}

    response = render(request, 'explorer/favourites_sidebar.html', context_dict)

    return response

def search_sidebar(request):

    context_dict={}

    response = render(request, 'explorer/search_sidebar.html', context_dict)

    return response

def history_sidebar(request):

    context_dict = {}

    response = render(request, 'explorer/history_sidebar.html', context_dict)

    return response

def profile_sidebar(request):

    context_dict ={}

    response = render(request, 'explorer/profile_sidebar.html', context_dict)

    return response

def settings_sidebar(request):

    context_dict = {}

    response = render(request, 'explorer/settings_sidebar.html', context_dict)

    return response
