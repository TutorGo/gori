from django.contrib.auth import get_user_model
from rest_framework import serializers

from talent.serializers import TalentShortInfoSerializer

User = get_user_model()

__all__ = (
    'MyWishListSerializer',
)


class MyWishListSerializer(serializers.ModelSerializer):
    talent = TalentShortInfoSerializer(many=True, source='talent_set')

    class Meta:
        model = User
        fields = (
            'name',
            'nickname',
            'cellphone',
            'profile_image',
            'joined_date',
            'talent',
        )
#
# class WishListSerializer(serializers.ModelSerializer):
#    talent = serializers.PrimaryKeyRelatedField(queryset=Talent.objects.all(), write_only=True)
#    talent_title = serializers.PrimaryKeyRelatedField(read_only=True, source='talent.title')
#    user = serializers.PrimaryKeyRelatedField(queryset=GoriUser.objects.all(), write_only=True)
#    user_name = serializers.PrimaryKeyRelatedField(read_only=True, source='user.name')
#
#    class Meta:
#        model = WishList
#        fields = (
#            'talent',
#            'talent_title',
#            'user_name',
#            'user',
#            'added_date'
#        )
#        validators = [
#            serializers.UniqueTogetherValidator(
#                queryset=WishList.objects.all(),
#                fields=('talent', 'user'),
#                message=("이미 추가한 수업 입니다.")
#            )
#        ]