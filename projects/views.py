from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def project_list(request):
    # return HttpResponse("<h1>Hello Everyone!</h1>")
    return render(request, 'projects/index.html')