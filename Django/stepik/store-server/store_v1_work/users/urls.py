# path('login/', login, name='login'),
#     path('registration/', registration, name='registration'),
from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import profile, login, registration, logout, \
    EmailVerificationView

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
    path('verify/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='email_verification'),

]

