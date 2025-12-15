from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import auth
from .models import Game, CartItem 


# Create your views here.

def index(request):
    games = Game.objects.all()
    return render(request, 'index.html', {'games': games})


def register(request):
    if request.method == 'POST':
        em = request.POST['email']
        fn = request.POST['fname']
        ln = request.POST['lname']
        un = request.POST['uname']
        p1 = request.POST['pass1']
        p2 = request.POST['pass2']

        print("VALUES:", em, fn, ln, un, p1, p2)    

        if p1 == p2:
            user = auth.get_user_model().objects.create_user(email=em, first_name=fn, last_name=ln, username=un, password=p1)
            user.save()
            print('User created successfully!')
            return redirect('/login/')
        else:
            print('Password not matching!!')
            return redirect('/register/')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        un = request.POST['uname']
        p1 = request.POST['pass1']
        user = auth.authenticate(username=un, password=p1)
        # print(un,p1)
        # return
        if user is not None:
            auth.login(request,user)
            print('Login successful!')
            return redirect('/')
        else:
            print('Invalid username or password!!')
            redirect('/login/')

    return render(request,'login.html')

def contact(request):
    return render(request,'contact.html')

def logout(request): 
    auth.logout(request)
    print('Logout successfully!') 
    return redirect('/login/') 

def about(request):
    return render(request, 'about.html')


def shop(request):
    games = Game.objects.all()
    return render(request, 'shop.html', {'games': games})

def add_to_cart(request, game_id):
    game = get_object_or_404(Game, id=game_id)

    # check if already in cart
    cart_item, created = CartItem.objects.get_or_create(game=game)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')

def cart(request):
    cart_items = CartItem.objects.all()
    total_cost = sum(item.total_price() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_cost': total_cost})

def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('cart')

def update_cart(request):
    if request.method == "POST":
        cart_items = CartItem.objects.all()

        for item in cart_items:
            new_qty = request.POST.get(f"quantity_{item.id}")
            if new_qty and int(new_qty) > 0:
                item.quantity = int(new_qty)
                item.save()

    return redirect('cart')

def checkout(request):
    cart_items = CartItem.objects.all()
    total_cost = sum(item.total_price() for item in cart_items)

    return render(request, 'checkout.html', {'cart_items': cart_items, 'total_cost': total_cost})
