# from basket.models import Lessons
#
#
# def baskets(request):
#     user = request.user
#     return {'pay_lessons': Basket.objects.filter(user=user) if user.is_authenticated else []}