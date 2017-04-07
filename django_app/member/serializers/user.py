from django.contrib.auth import get_user_model
from rest_framework import serializers

from member.models import Tutor
from talent.models import Registration, Location, Talent

__all__ = (
    'UserSerializer',
    'TutorSerializer',
    # 'MyWishListSerializer',
)

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    user_type = serializers.SerializerMethodField(read_only=True)
    user_id = serializers.CharField(
        read_only=True, source='username')
    received_registrations = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = (
            'pk',
            'user_id',
            'name',
            'nickname',
            'cellphone',
            'user_type',
            'is_tutor',
            'is_staff',
            'is_active',
            'profile_image',
            'joined_date',
            'last_login',
            'received_registrations',
        )

    def get_user_type(self, obj):
        return obj.get_user_type_display()

    def get_received_registrations(self, obj):
        """
        location가 참조하는 talent의 tutor_id가
        현재 obj(로그인 유저)와 일치하는 지 판단
        즉, location이 현재 유저의 것인지 판단.

        해당 location의 registered_student 목록을 받아온다.
        목록을 리스트로 변환하고, none 객체를 제거한다.
        (아무도 등록하지 않은 location의 경우 none을 반환한다.)

        목록의 카운트를 반환한다.

        :param obj: request.user
        :return:
        """
        registered_students = Location.objects.filter(talent__tutor_id=obj.id).values_list('registered_student',
                                                                                           flat=True)
        list_registered_students = list(registered_students)
        while True:
            try:
                list_registered_students.remove(None)
            except:
                break
        return len(list_registered_students)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])

        user.save()
        return user


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class TutorSerializer(DynamicFieldsModelSerializer):
    user_id = serializers.CharField(
        read_only=True, source='user.username')
    name = serializers.CharField(
        read_only=True, source='user.name'
    )
    cellphone = serializers.CharField(
        read_only=True, source='user.cellphone'
    )
    profile_image = serializers.ImageField(
        read_only=True, source='user.profile_image')
    nickname = serializers.CharField(read_only=True, source='user.nickname')

    class Meta:
        model = Tutor
        fields = (
            'pk',
            'user_id',
            'name',
            'nickname',
            'is_verified',
            'profile_image',
            'cellphone',
        )
