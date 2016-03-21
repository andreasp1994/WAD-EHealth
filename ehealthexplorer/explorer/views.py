from django.shortcuts import render
from explorer.bing_search import run_bing_query
from explorer.medLine_search import run_medline_query
from explorer.healthFinder_search import run_healthfinder_query
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user
from models import Category, Page, User
from operator import itemgetter
from datetime import datetime
from django.contrib.auth.decorators import login_required

@csrf_exempt
def index(request):

    context_dict = {}


    medicine_list = ['Lipitor','Nexium','Plavix','Advair','Abilify','Seroquel',
                    'Singulair','Crestor','Actos']
    context_dict['medicines'] = medicine_list

    response = render(request,'explorer/index.html', context_dict )
    return response

@csrf_exempt
def results(request):
    read_lower = 0.0
    read_upper = 100.0
    pol_lower = -1.0
    pol_max = 1.0
    sub_upper = 0.0
    sub_upper = 1.0

    search_term = request.GET['q']
    query = search_term.strip()
    

    ############################################
    # Subjectivity, Polarity, readability values
    ############################################
    read_lower = float(request.GET['rl'])
    read_upper = float(request.GET['ru'])

    sub_lower = float(request.GET['sl'])
    sub_upper = float(request.GET['su'])

    pol_lower = float(request.GET['pl'])
    pol_upper = float(request.GET['pu'])

    bing_results=[]
    medLine_results=[]
    healthFinder_results=[]

    if query:
        try:
            bing_results = run_bing_query(query, read_lower, read_upper,
                                pol_lower, pol_upper, sub_lower, sub_upper)
        except: 
            print "Bing search failed"
            
        try:  
            medLine_results = run_medline_query(query, read_lower, read_upper,
                                 pol_lower, pol_upper, sub_lower, sub_upper)
        except:
            print "Medline search failed"
            
        try:
            healthFinder_results = run_healthfinder_query(query, read_lower, read_upper,
                                pol_lower, pol_upper, sub_lower, sub_upper)
        except:
            print "HealthFinder Search failed"

    main_list = (bing_results + medLine_results + healthFinder_results)
    main_list = sorted(main_list, key=itemgetter('read'), reverse=True)
    context_dict={'results':main_list, 
                  'bing':bing_results,
                  'medLine':medLine_results,
                  'healthFinder':healthFinder_results }

    if request.user.is_authenticated():
        category_list = Category.objects.filter(user=get_user(request))
        context_dict['categories'] = category_list
    context_dict['query'] = query

    context_dict['rl'] = read_lower
    context_dict['ru'] = read_upper
    context_dict['sl'] = sub_lower
    context_dict['su'] = sub_upper
    context_dict['pl'] = pol_lower
    context_dict['pu'] = pol_upper

    response = render(request,'explorer/results.html',context_dict)   
    return response

def results_sidebar(request):
    context_dict={}
    response = render(request, 'explorer/results_sidebar.html', context_dict)
    return response

@login_required
def favourites_sidebar(request):
    context_dict={}

    task = request.GET.get('task',"")
    if (task == "AJAX_ADD_CATEGORY"):
            print task
            try:
                cat_name = "New Category "
                cat_name += str(Category.objects.filter(user=get_user(request)).count())
                searcher = request.user
                cat = Category.objects.create(name=cat_name,user=searcher)
                cat.save()
            except Exception as e:
                print e
    elif (task == "AJAX_DELETE_CATEGORY"):

            id = request.GET['id']
            cat = Category.objects.filter(id=id)
            cat.delete()

    elif (task == "AJAX_SHARE_CATEGORY"):
            id = request.GET['id']
            cat = Category.objects.filter(id=id).get()

            if (cat.shared == False):
                cat.shared = True
                cat.time_shared = datetime.now()
            else:
                cat.shared = False
            cat.save()

    elif (task == "AJAX_RENAME_CATEGORY"):
            id = request.GET['id']
            new_name = request.GET['name']
            cat = Category.objects.filter(id=id).get()
            cat.name=new_name
            cat.save()

    elif (task == "AJAX_DELETE_FAVOURITE"):
            id = request.GET['id']
            page = Page.objects.filter(id=id).get()
            page.delete()

    elif (task == "AJAX_SAVE_TO"):
            c = Category.objects.filter(user=get_user(request),name=request.GET['name']).get()
            page = Page.objects.create(category=c,title=request.GET['title'])
            page.summary = request.GET['summary']
            page.url = request.GET['url']
            page.flesch_score = request.GET['read']
            page.polarity_score = request.GET['pola']
            page.subjectivity_score = request.GET['subj']
            page.save()

    #Load categories and pages
    if request.user.is_authenticated():
        category_list = Category.objects.filter(user=get_user(request))
        for cat in category_list:
            cat.saved = Page.objects.filter(category=cat)
        context_dict['categories'] = category_list

    response = render(request, 'explorer/favourites_sidebar.html', context_dict)

    return response

@login_required
def search_sidebar(request):

    context_dict={}

    medicine_list = ['Lipitor','Nexium','Plavix','Advair','Abilify','Seroquel',
                    'Singulair','Crestor','Actos']
    context_dict['medicines'] = medicine_list

    treatments_procedures_list = ['Antinuclear Antibody Test','CAT Scan','Chemotherapy','Colonoscopy','Complete Blood Count',
                         'Coronary Artery Bypass Graft (CABG)','Cortisone Injection','Creatinine Blood Test',
                         'Electrolytes','Lap Band Surgery (Gastric Banding)','Liver Blood Test','MRI Scan',
                         'Thyroid Blood Tests','Total Hip Replacement','Total Knee Replacement','Tuberculosis Skin Test (PPD Skin Test)',
                         'Ultrasound']
    context_dict['treatandproc'] = treatments_procedures_list

    response = render(request, 'explorer/search_sidebar.html', context_dict)
    return response

@login_required
def profile_sidebar(request):

    context_dict ={}
    response = render(request, 'explorer/profile_sidebar.html', context_dict)
    return response

@login_required
def settings_sidebar(request):

    context_dict = {}

    if request.method == "POST":
        task = request.POST['task']
        if task == "AJAX_UPDATE":

            username = request.POST['username']
            email = request.POST['email']

            u = User.objects.filter(username=request.user.username).first()
            u.username = username
            u.email = email
            u.save()


    response = render(request, 'explorer/settings_sidebar.html', context_dict)
    return response


def search_categories(request):

    context_dict = {}

    query = request.GET.get('q')

    if query == None:
        query = ""

    context_dict['query'] = query

    if (query == ""):
        shared_categories = Category.objects.filter(shared=True)
    else:
        shared_categories = Category.objects.filter(shared=True, name__contains=query)

    for cat in shared_categories:
            cat.saved = Page.objects.filter(category=cat)

    context_dict['shared_categories']=shared_categories

    response = render(request, 'explorer/search_categories.html',context_dict)
    return response