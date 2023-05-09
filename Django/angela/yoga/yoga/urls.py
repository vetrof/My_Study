from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

# from cart.views import cart_add
from basket.views import basket_add, basket_remove
from lessons.views import IndexView, LessonsView, LiveLessonsView, \
    FreeLessonsView, AboutView, ContactsView, LessonsCardView, MyLessonsView, \
    MyLessonsCardView
from order.views import OrderCreateView, OrderSuccessView, OrderCanceledView, \
    stripe_webhook_view, OrdersListView, OrderDetailView
from users.views import LoginUserView, UserRegistrationView
from cabinet.views import CabinetView
from videostream.views import get_streaming_video

urlpatterns = [

    path('admin/', admin.site.urls),

    # lessons
    path('', IndexView.as_view(), name='index'),
    path('lessons/', LessonsView.as_view(), name='lessons'),
    path('live_lessons/', LiveLessonsView.as_view(), name='live_lessons'),
    path('free_lessons/', FreeLessonsView.as_view(), name='free_lessons'),
    path('lessons_card/<int:pk>/', LessonsCardView.as_view(), name='lessons_card'),
    path('about/', AboutView.as_view(), name='about'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('my_lessons/', MyLessonsView.as_view(), name='my_lessons'),
    path('my_lessons_card/<int:pk>/', MyLessonsCardView.as_view(), name='my_lessons_card'),

    # user
    path('login/', LoginUserView.as_view(), name='login'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # cabinet
    path('cabinet/<int:pk>/', login_required(CabinetView.as_view()), name='cabinet'),
    path('basket/add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket/remove/<int:basket_id>/', basket_remove, name='basket_remove'),

    # orders
    path('order-create/', OrderCreateView.as_view(), name='order_create'),
    path('order_success/', OrderSuccessView.as_view(), name='order_success'),
    path('order_canceled/', OrderCanceledView.as_view(), name='order_canceled'),
    path('orders_list/', OrdersListView.as_view(), name='orders_list'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order'),

    # stripe
    path('webhook/stripe/', stripe_webhook_view, name='stripe_webhook'),

    # video-stream
    path('stream/<int:pk>/', get_streaming_video, name='stream'),


    # temp
    # path('test', test_add, name='test_add'),

]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)