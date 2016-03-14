from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def searcher_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)

                context_dict={}

                response = render(request, 'explorer/login_sidebar.html', context_dict)

                return response
            else:
                return HttpResponse("Your account is disabled.")

                context_dict={}

                response = render(request, 'explorer/search_sidebar.html', context_dict)

                return response
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
            context_dict={}

            response = render(request, 'explorer/login_sidebar.html', context_dict)

            return response




@login_required
def user_logout(request):

    logout(request)

    context_dict={}

    response = render(request, 'explorer/search_sidebar.html', context_dict)

    return response
