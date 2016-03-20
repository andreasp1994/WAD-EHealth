from django.shortcuts import render
from explorer.bing_search import run_bing_query
from explorer.medLine_search import run_medline_query
from explorer.healthFinder_search import run_healthfinder_query
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user
from models import Category, Searcher
from operator import itemgetter

@csrf_exempt
def index(request):

    context_dict = {}

    if request.user.is_authenticated():
        if request.method == "POST":
            print "Post request"
            task = request.POST.get('task',None)
            if task != None:
                if (task == "AJAX_ADD_CATEGORY"):

                    try:
                        cat_name = request.POST['name']
                        cat_name += str(Category.objects.filter(user=get_user(request)).count())
                        searcher = request.user
                        cat = Category.objects.create(name=cat_name,user=searcher)
                        cat.save()
                    except Exception as e:
                        print e

                elif (task == "AJAX_DELETE_CATEGORY"):
                    id = request.POST['id']
                    cat = Category.objects.filter(id=id)
                    cat.delete()

                elif (task == "AJAX_SHARE_CATEGORY"):
                    id = request.POST['id']
                    cat = Category.objects.filter(id=id).get()

                    if (cat.shared == False):
                        cat.shared = True
                    else:
                        cat.shared = False
                    cat.save()

                elif (task == "AJAX_RENAME_CATEGORY"):
                    id = request.POST['id']
                    new_name = request.POST['new_name']
                    cat = Category.objects.filter(id=id).get()
                    cat.name=new_name
                    cat.save()

                return HttpResponse(json.dumps({'message': task}))

        #Load categories from database:
        category_list = Category.objects.filter(user=request.user)
        context_dict['categories'] = category_list


    response = render(request,'explorer/index.html', context_dict )
    return response


def results(request):

    search_term = request.POST['query']
    query = search_term.strip()
    
    bing_results=[]
    medLine_results=[]
    healthFinder_results=[]

    if query:
        bing_results = run_bing_query(query)
        medLine_results = run_medline_query(query)
        try:
            healthFinder_results = run_healthfinder_query(query)
        except TypeError as e:
            print "Search failed: ", e
    main_list = (bing_results + medLine_results + healthFinder_results)
    main_list = sorted(main_list, key=itemgetter('read'), reverse=True)
    context_dict={'results':main_list, 
                  'bing':bing_results,
                  'medLine':medLine_results,
                  'healthFinder':healthFinder_results 
                 } ## Placeholder until search function can be implemented
    

    response = render(request,'explorer/results.html',context_dict)   
    return response

def favourites_sidebar(request):

    context_dict={}

    if request.user.is_authenticated():
        category_list = Category.objects.filter(user=get_user(request))
        context_dict['categories'] = category_list

    response = render(request, 'explorer/favourites_sidebar.html', context_dict)

    return response

def search_sidebar(request):

    context_dict={}

    response = render(request, 'explorer/search_sidebar.html', context_dict)

    return response

def profile_sidebar(request):

    context_dict ={}

    response = render(request, 'explorer/profile_sidebar.html', context_dict)

    return response

def settings_sidebar(request):

    context_dict = {}

    response = render(request, 'explorer/settings_sidebar.html', context_dict)

    return response
