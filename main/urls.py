from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),
    path("storelogin", views.storelogin, name="storelogin"),
    path('first_intro/', views.first_intro, name='first_intro'),
    path('second_my/', views.second_my, name='second_my'),
    path('third_pchange/', views.third_pchange, name='third_pchange'),
    path('blog/', views.blog, name='blog'),
    path("userpage/", views.userpage, name="userpage"),
    path("storepass/", views.storepass, name="storepass"),
    path("gift/",views.gift, name="gift"),
    path("sendgift/", views.sendgift, name="sendgift"),
    path("buygifticon/",views.buygifticon, name="buygifticon"),
    path("nopoint/", views.nopoint, name="nopoint"),
    path("honeytip/", views.honeytip, name="honeytip"),
]