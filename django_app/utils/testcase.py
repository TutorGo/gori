from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from rest_framework.test import APILiveServerTestCase

from member.models import Tutor
from talent.models import Talent, Location, Registration, Curriculum, Review, Question, Reply
from utils.upload import image_upload
from rest_framework.test import APILiveServerTestCase

User = get_user_model()


class APITestListVerify(APILiveServerTestCase):
    def verify_util(self, data, keys):
        response_list = data
        field_list = keys
        for field_item in field_list:
            self.assertIn(field_item, response_list)


class APITestUserLogin(object):
    test_user = 'test{}'
    test_password1 = 'testpw12'
    test_password2 = 'testpw12'
    test_name = 'testname{}'

    def create_user_and_login(self):
        user = self.create_user()
        data = {
            'username': user.username,
            'password': 'testpw12',
        }
        url = reverse('api:member:rest_login')
        response = self.client.post(url, data, format='json')
        return user

    def create_user(self, number=1):
        users = []
        for i in range(number):
            username = self.test_user.format(i)
            name = self.test_name.format(i)

            data = {
                'username': username,
                'password1': self.test_password1,
                'password2': self.test_password2,
                'name': name,
            }
            url = reverse('api:member:user-signup')
            response = self.client.post(url, data, format='json')
            user = User.objects.get(username=username)
            if number == 1:
                return user
            users.append(user)
        return users

    def obtain_token(self, number=1):
        tokens = []
        users = self.create_user(number)
        if number == 1:
            data = {
                'username': users.username,
                'password': 'testpw12',
            }
            user_token_url = reverse('api:member:user-token')
            response = self.client.post(user_token_url, data, format='json')
            return users, response.data.get('token')
        for user in users:
            data = {
                'username': user.username,
                'password': 'testpw12',
            }
            user_token_url = reverse('api:member:user-token')
            response = self.client.post(user_token_url, data, format='json')
            # if number ==1:
            #     return user, response.data.get('token')
            tokens.append(response.data.get('token'))

        return users, tokens

    def register_tutor(self, user, token=None):
        test_image = image_upload()
        data = {
            "user": user,
            "is_verified": True,
            "verification_method": 'UN',
            "verification_images": test_image
        }
        tutor_create_url = reverse('api:member:tutor-register')
        response = self.client.post(tutor_create_url, data, format="multipart", HTTP_AUTHORIZATION='Token ' + token)
        tutor = Tutor.objects.get(user=user)
        return tutor

    def create_talent(self, tutor, token=None):
        test_image = image_upload()
        data = {
            'tutor': tutor,
            'title': 'test',
            'category': 'COM',
            'type': '0',
            'cover_image': test_image,
            'tutor_info': 'test',
            'class_info': 'test',
            'price_per_hour': '10000',
            'hours_per_class': '1000',
            'number_of_class': '10',
            'tutor_message': 'test_message'

        }
        url = reverse('api:talent:create')
        response = self.client.post(url, data, HTTP_AUTHORIZATION='Token ' + token)
        talent = Talent.objects.last()
        talent.is_verified = True
        talent.save()
        return talent

    def create_location(self, talent, token=None):
        region = 'KN'
        day = "MO"
        time = "12-16,18-20"
        data = {
            "talent_pk": talent.pk,
            "region": region,
            "specific_location": 'NEGO',
            "extra_fee": 'Y',
            "day": day,
            "time": time,
        }
        url = reverse('api:talent:location-create')
        response = self.client.post(url, data, HTTP_AUTHORIZATION='Token ' + token)
        location = Location.objects.get(region=region, day=day, time=time)
        return location

    def create_curriculum(self, talent, token=None):
        test_image = image_upload()
        data = {
            'talent_pk': talent.pk,
            'information': 'test_information',
            'image': test_image,
        }
        url = reverse('api:talent:curriculum-create')
        response = self.client.post(url, data, HTTP_AUTHORIZATION='Token ' + token)
        curriculum = Curriculum.objects.get(talent_id=talent.pk)
        return curriculum

    def create_review(self, talent, token=None):
        data = {
            'talent_pk': talent.pk,
            'curriculum': 5,
            'readiness': 5,
            'timeliness': 5,
            'delivery': 5,
            'friendliness': 5,
            'comment': 'test_comment'
        }
        url = reverse('api:talent:review-create')
        response = self.client.post(url, data, HTTP_AUTHORIZATION='Token ' + token)
        review = Review.objects.get(talent_id=talent.pk)
        return review

    def create_question(self, talent, token=None):
        data = {
            'talent_pk': talent.pk,
            'content': 'test_content',
        }
        url = reverse('api:talent:question-create')
        response = self.client.post(url, data, HTTP_AUTHORIZATION='Token ' + token)
        question = Question.objects.get(talent_id=talent.pk)
        return question

    def create_reply(self, question, token=None):
        data = {
            'question_pk': question.pk,
            'content': 'test_content'
        }
        url = reverse('api:talent:reply-create')
        response = self.client.post(url, data, HTTP_AUTHORIZATION='Token ' + token)
        reply = Reply.objects.get(question_id=question.pk)
        return reply

    def create_registration(self, location, token=None):
        user = Token.objects.get(key=token).user
        data = {
            "location_pk": location.pk,
            "student_level": 1,
            "message_to_tutor": "잘부탁드립니다 user{}".format(user.pk),
        }
        url = reverse('api:talent:registration-create')
        response = self.client.post(url, data, HTTP_AUTHORIZATION='Token ' + token)
        user.refresh_from_db()
        registration = Registration.objects.get(student=user, talent_location=location)
        return registration
