from django.shortcuts import render

# Create your views here.
def one(request):
    return render(request, 'ware/one.html')
    

def two(request):
    return render(request, 'ware/two.html')
    
    
def three(request):
    return render(request, 'ware/three.html')