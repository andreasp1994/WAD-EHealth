from django.shortcuts import render

# Create your views here.
def index(request):

    context_dict={}

    response = render(request,'explorer/index.html', context_dict)

    return response
    
def results(request):
    context_dict={'results':[{'title':'Google','url':'http://www.google.co.uk'},{'title':'Amazon','url':'http://www.amazon.co.uk'}], ## Do we need this? hmm
                  'bing':[{'title':'Google','url':'http://www.google.co.uk'}],
                  'medLine':[{'title':'Amazon','url':'http://www.amazon.co.uk'}],
                  'healthFinder':{} 
                 } ## Placeholder until search function can be implemented
    
    response = render(request,'explorer/results.html',context_dict)      ## can be used.
    
    return response