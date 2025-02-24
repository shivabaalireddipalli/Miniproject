from django.urls import path
from .import views
urlpatterns=[
    path('',views.home,name='home'),
    path('Login',views.Loginpage,name='Loginpage'),
    path('div',views.divpage,name='divpage'),
    path('consumer',views.consumerpage,name='conspage'),
    path('agent',views.agentpage,name='agentpage'),
    path('contactus',views.contactus,name='contactus'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('Cart1',views.CartPage,name='cartpage'),
    path('cropreg',views.cropregi,name='repeat1'),
    path('Farmer',views.farmerreg,name='farmer1'),
    path('agentin',views.agentsignin,name='signup'),
    path('consumerin',views.consumersignin,name='signup'),
    path('feedback',views.feedbackp,name='feedbackp'),
    path('Cart2',views.Addelements,name='Addelements'),
    path('Cart3',views.ItemsCart,name='ItemsCart'),
    path('Login1',views.login,name='login'),
    path('Thankyou',views.Thankyou1,name='Thankyou'),
    path('homeback',views.backpage,name='bakcpage'),
    path('logout1',views.logout1,name='logout1'),
    path('farmerf',views.fetchfarmer,name='fetchfarmer'),
    path('agentf',views.fetchagent,name='agent'),
    path('consumerf',views.fetchconsumer,name='fetchconsumer'),
    path('contactFetch',views.fetchcontact,name='fetchcontact'),
    path('feedback1',views.Feedback1,name='feedback1'),
    path('crop',views.cropfetch,name='cropfetch'),
    path('Bagitems',views.Checkout,name='Checkout'),
    path('Cartsignup',views.Cartsignup,name='Cartsignup'),
    path('CartSignup',views.CartSignup,name="CartsignUp"),
    path('CartLogin',views.CartLogin,name='CartLogin'),
    path('checkout',views.itemout,name='itemout'),
    path('delete',views.Removeitems,name='Removeitems'),
]