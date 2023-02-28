from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import AuthenticationForm
from . forms import CustomerSignUpForm
from django.contrib.auth import login, authenticate
from store.models import *
from django.contrib.auth.decorators import login_required
# from django.core.files.storage import FileSystemStorage
# Create your views here.
def login(request):
    if request.method == 'POST':
        form= AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = username)
            pas = authenticate(password= password)
            if user is not None and pas is not None:
                login(request, user, pas)
                return redirect('home')
            else:
                return redirect('login')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form':form})
        
def register(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            customer_group = Group.objects.get(name= 'Customer')
            customer_group.user_set.add(signup_user)
            return redirect("{% url 'login'%}")
    else:
         form = CustomerSignUpForm() 
    return   render(request, 'registration/register.html', {'form':form})    


# def logout(request):
#     form = ClientSignUpForm(request.POST)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             signup_user = User.objects.get(username=username)
#             client_group = Group.objects.get(name='Client')
#             client_group.user_set.add(signup_user)
#         else:
#             form = ClientSignUpForm()
#     return render(request, 'registration/register.html', {'form': form})

# def add_product(request):
#    # context = {}
#     if request.method == "GET":
#         form = ProductCreateForm()
#         return render(request, 'accounts/clients/add_product.html', {'form': form})

#     else:
#         form = ProductCreateForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.image = request.FILES['image']
#             form.save()
#         return render(request, "accounts/clients/add_product.html")
    
# def customer_logout(request):
#     logout(request)
#     return redirect('customer_login')

# @login_required(redirect_field_name='next', login_url='customer_login')
# def orderHistory(request):
#     if request.user.is_authenticated:
#         email = str(request.user.email)
#         order_details = Order.objects.filter(emailAddress=email)
#     return render(request, 'store/orders_list.html', {'order_details': order_details})


# def client_login(request):
#     return render(request, 'accounts/clients/login.html')



# def client_portal(request):
#     return render(request, 'accounts/clients/dashboard.html')


# @login_required(redirect_field_name='next', login_url='customer_login')
# def portal_admin(request):
#     products = Product.objects.all()
#     return render(request, 'accounts/clients/portal.html', {'products': products})

# def products(request):
#     return render(request, 'accounts/clients/products.html')

# def docs(request):
#     return render(request, 'accounts/docs/faqs.html')