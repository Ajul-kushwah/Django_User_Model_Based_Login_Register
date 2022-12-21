from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    #path('login_page',views.login,name="login"),
    path('register_page',views.register,name="register"),

    path('login/', LoginView.as_view(template_name='accounts/login.html'), name="login_url"),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name="logout_url"),

]