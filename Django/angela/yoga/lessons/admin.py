from django.contrib import admin

from lessons.models import Lessons, LessonsCategory, OrderingLessons, \
    Pay_lessons


@admin.register(LessonsCategory)
class LessonsCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Lessons)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stripe_product_price_id')
    # fields = ()
    list_filter = ["active", 'price']


@admin.register(OrderingLessons)
class OrderingLessonsAdmin(admin.ModelAdmin):
    list_display = ('user',  'id_lesson', 'video_link')


@admin.register(Pay_lessons)
class PaylessonsAdmin(admin.ModelAdmin):
    list_display = ('user',  'lesson')
