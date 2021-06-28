from django.shortcuts import render


# Create your views here.

# def home(request):
#     return HttpResponse('<h1>HomePage</h1>')

def home(request):
    return render(request, 'home.html' )

def about(request):
    return render(request, 'about.html' )

def single_blog(request):
    return render(request, 'blog-single.html' )

def blog(request):
    return render(request, 'blog.html' )

def contact(request):
    return render(request, 'contact.html' )                   


def portfolio(request):
    return render(request, 'page-portfolio.html' )

def project_detail(request):
    return render(request, 'page-project-detail.html' )

def service_detail(request):
    return render(request, 'page-service-detail.html' )

def services(request):
    return render(request, 'page-services.html')

def shop_cart(request):
    return render(request, 'page-shop-cart.html')

def single_shop(request):
    return render(request, 'page-shop-single.html')

def shop_page(request):
    return render(request, 'page-shop.html')         