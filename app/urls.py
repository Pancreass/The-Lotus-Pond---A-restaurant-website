from django.urls import path
from . import views

urlpatterns = [
    path('',views.Login,name="login"),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('sampleMenu/',views.SampleMenu,name='SampleMenu'),
    path('cart/',views.viewCart,name='cart'),
    path('signup/',views.signup,name="signup"),
    path('logout/',views.Logout,name="logout"),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('increment_quantity/<int:item_id>/', views.increment_quantity, name='increment_quantity'),
    path('decrement_quantity/<int:item_id>/', views.decrement_quantity, name='decrement_quantity'),
    path('feedbackForm/', views.FeedbackForm,name='feedbackForm'),
    path('feedbackDisplay/', views.FeedbackDisplay, name="feedbackDisplay"),
]
