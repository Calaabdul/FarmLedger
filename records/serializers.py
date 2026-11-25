from rest_framework import serializers
from .models import Category, Produce


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'description']



class ProduceSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Produce
        fields = [  # noqa: RUF012
            'id',
            'owner',
            'category',
            'category_name',
            'name',
            'quantity',
            'unit',
            'price_per_unit',
            'description',
            'date_recorded',
            'updated_at',
        ]

        read_only_fields = [  # noqa: RUF012
            'id',
            'owner',
            'date_recorded',
            'updated_at',
        ]
