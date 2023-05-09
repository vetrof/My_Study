from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from basket.models import Basket
from lessons.models import Lessons, LessonsCategory, OrderingLessons, \
    Pay_lessons
from order.models import Order
from users.models import User
from access.views import access_check


class IndexView(ListView):
    template_name = 'lessons/index.html'
    model = Lessons
    ordering = '-id'
    paginate_by = 3


class LessonsView(ListView):
    template_name = 'lessons/lessons.html'
    model = Lessons
    ordering = '-id'
    paginate_by = 12

    # add filtered result
    def get_queryset(self):
        queryset = super(LessonsView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(
            category_id=category_id) if category_id else queryset

    # add 'categories' to object list
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(LessonsView, self).get_context_data()

        user = self.request.user
        if user.username:
            context['pay_user'] = Pay_lessons.objects.filter(user=user)
            context['pay_lesson_id'] = Pay_lessons.objects.filter(user=user).values_list('lesson', flat=True)
            return context
        else:
            # pass
            # context['pay_user'] = Pay_lessons.objects.filter(user=user)
            # context['orderingLessons'] = OrderingLessons.objects.all()
            return context


class LessonsCardView(DetailView):
    template_name = 'lessons/lesson_card.html'
    model = Lessons

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(LessonsCardView, self).get_context_data()

        context['access'] = False
        context['in_basket'] = False

        kwargs_data = kwargs.get('object', None)
        user = self.request.user
        current_video_id = kwargs_data.id
        access_flag = access_check(self.request, current_video_id)

        if access_flag:
            context['access'] = True

        if user.username:
            context['pay_user'] = Pay_lessons.objects.filter(user=user)
            return context
        else:
            return context


class MyLessonsCardView(DetailView):
    template_name = 'lessons/my_lessons_card.html'
    model = Lessons

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MyLessonsCardView, self).get_context_data()
        user = self.request.user
        if user.username:
            context['pay_user'] = Pay_lessons.objects.filter(user=user)
            return context
        else:
            return context


class LiveLessonsView(TemplateView):
    template_name = 'lessons/live_lessons.html'


class FreeLessonsView(ListView):
    template_name = 'lessons/free_lessons.html'
    model = Lessons
    ordering = '-id'
    paginate_by = 12

    def get_queryset(self):
        queryset = super(FreeLessonsView, self).get_queryset()
        # return queryset.filter(free=True)
        return queryset.filter(price=0)


class AboutView(TemplateView):
    template_name = 'lessons/about.html'


class ContactsView(TemplateView):
    template_name = 'lessons/contacts.html'


class MyLessonsView(ListView):
    template_name = 'lessons/my_lessons.html'
    model = Pay_lessons

    def get_queryset(self):
        queryset = super(MyLessonsView, self).get_queryset()
        user = self.request.user
        print(user)
        return queryset.filter(user=user)

# class MyLessonsView(ListView):
#     template_name = 'lessons/my_lessons.html'
#     model = Pay_lessons
#
#     def get_queryset(self):
#         queryset = super(MyLessonsView, self).get_queryset()
#         user = self.request.user
#         print(user)
#         return queryset.filter(user=user)
