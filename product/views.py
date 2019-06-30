from django.shortcuts import render, redirect
from .models import Product, Movie
import pdb

# Create your views here.
def main(request):
    return render(request, 'product/main.html')
    

def list(request):
    product = Product.objects.all()
    context = {
        'product': product,
    }
    return render(request, 'product/list.html', context)
    
    
def kind(request):
    movie = Movie.objects.all()
    return render(request, 'product/kind.html', {'movie': movie})


def movie(request):
    if request.method == "POST":
        title = request.POST.get('title')
        time = request.POST.get('time')
        seat = request.POST.get('seat')
        movie = Movie(title = title, time = time, seat = seat)
        movie.save()
        return redirect('kind')
    return render(request, 'product/movie.html')


def create(request):
    loop_range = range(1, 16)
    loop_alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    if request.method == "POST":
        title = request.POST.get('title')
        time = request.POST.get('time')
        
        for index in loop_range:
            for alphabet in loop_alphabets:
                req = request.POST.get('seat{}-{}'.format(index, alphabet))
                if req is not None:
                    seat = "{}행 {}열".format(index, alphabet)
        product = Product(title = title, time = time, seat = seat)
        product.save()
        return redirect('list')
    context = {
        'loop_range': loop_range,
        'loop_alphabets': loop_alphabets
    } # 아 건들지마셈?? 안 건드림  ㅇㅇ 아무것도 하지말고 있어보셈
    ## 여기 이렇게 range(1, 16) 하면 1~15 가 tuple 이라는 형태로 담기고
    ## 알파벳을 저렇게 배열로 담겨준다음에 저걸 create.html에서 쓸수있게 던져준거임 ㅇㅋ? 아하 이해함
    ## context 라는 변수에다가 dictonary type 으로 담아서
    return render(request,'product/create.html', context)
                                                # 여기서 context로 던져준거임 ㅇㅋㅇㅋ create.html로 오셈
                                                


