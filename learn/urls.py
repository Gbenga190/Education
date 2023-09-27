from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name="index"),
    path('about',views.about, name="about"),
    path('blog',views.blog, name="blog"),
    path('programming_language',views.programming_language, name="programming_language"),
    path('artificial_intelligence',views.artificial_intelligence, name="artificial_intelligence"),
    path('business_proposal',views.business_proposal, name="business_proposal"),
    path('cyber_security',views.cyber_security, name="cyber_security"),
    path('register/', views.register, name="register"),
    path('user_login/', views.user_login, name="user_login"),
    path('subscribe',views.subscribe, name="subscribe"),
    path('user_logout/', views.user_logout, name="user_logout"),
]