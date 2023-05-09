from rest_framework import fields, serializers

from products.models import Basket, Product, ProductCategory


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', queryset=ProductCategory.objects.all())
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'quantity', 'image', 'category')


class BasketSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    summ = fields.FloatField(required=False)#  summ - метод в модели Basket
    total_sum = fields.SerializerMethodField() #  total_sum - метод  квери сете корзины
    total_quantity = fields.SerializerMethodField()
#
    class Meta:
        model = Basket
        fields = ('id', 'product', 'quantity', 'summ', 'total_sum', 'total_quantity', 'created_timestamp')
        read_only_fields = ('created_timestamp',)
#
    def get_total_sum(self, obj):
        return Basket.objects.filter(user_id=obj.user.id).total_sum()# total_sum - метод  квери сете корзины
#
    def get_total_quantity(self, obj):
        return Basket.objects.filter(user_id=obj.user.id).total_quantity()
