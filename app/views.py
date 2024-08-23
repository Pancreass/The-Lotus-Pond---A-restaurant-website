from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .models import Menu,CartItem,Feedback
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request,'index.html')

@login_required(login_url='login')
def about(request):
    return render(request,'about.html')

@login_required(login_url='login')
def SampleMenu(request):
    menu=Menu.objects.all
    context={'menu':menu}
    return render(request,'sampleMenu.html',context)

@login_required(login_url='login')
def viewCart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'viewcart.html', {'cart_items': cart_items})

def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pswd = request.POST.get('password')
        user=authenticate(request,username=username , password =pswd)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("username or password is incorrect!!")
    return render(request,"login.html")

def signup(request):
    if request.method =='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        pswd=request.POST.get('password')
        pswd2=request.POST.get('password2')
        
        if pswd!=pswd2:
            return HttpResponse("your password and confirm password are not same")
        else:
            if User.objects.filter(username=username).exists():
                return HttpResponse("Username already exists")
            else:
                myuser=User.objects.create_user(username,email,pswd)
                myuser.save()
                return redirect('login')
    return render(request,"signup.html")
    


def add_to_cart(request, item_id):
    menu_item = Menu.objects.get(pk=item_id)
    user = request.user
    cart_item, created = CartItem.objects.get_or_create(user=request.user,menu_item=menu_item)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('SampleMenu')

def increment_quantity(request, item_id):
    cart_item = get_object_or_404(CartItem, pk=item_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

def decrement_quantity(request, item_id):
    cart_item = get_object_or_404(CartItem, pk=item_id)
    if cart_item.quantity > 0:
        cart_item.quantity -= 1
        cart_item.save()
    if cart_item.quantity == 0:
        cart_item.delete()
    return redirect('cart')

def Logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def FeedbackForm(request):
    if request.method == 'POST':
        name = request.POST.get('NAME')
        email = request.POST.get('email')
        feedback_message = request.POST.get('feedback')
        Feedback.objects.create(name=name, email=email, feedback=feedback_message)
        return redirect('feedbackDisplay')
    
    return render(request, "feedbackForm.html")

@login_required(login_url='login')
def FeedbackDisplay(request):
    feedback_data = Feedback.objects.all()
    return render(request, "feedbackDisplay.html", {'feedback_data': feedback_data})
