from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def greet(request, name=""):
    if name == "":
        return HttpResponse(f"Hello Stranger!")
    
    else:
        return HttpResponse(f"Hello {name}!")
    

# list of tuples
# each tuple broken down by (pattern, view_name)
# Return the view_name of the first pattern that exactly matches path
def resolve_url(path:str, urlpatterns:list):
    
    flag = 0 
    
    for item in urlpatterns:
        
        if path == item[0]:
            return urlpatterns[flag][1]
              

        flag += 1
        
    return "404"