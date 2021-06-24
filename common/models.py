from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE


class Character(models.Model):
    pass


class User(AbstractUser):
    # 기본 User 모델은 username, email, password, last_login 등 제공
    # 성별과 마일리지, 레벨, 소개글, 캐릭터 추가
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_UNKNOWN = 2
    GENDER_CHOICES = [(GENDER_MALE, '남성'), (GENDER_FEMALE, '여성'), (GENDER_UNKNOWN, '숨기기')]
    name = models.CharField(blank=False, null=False, max_length=100)
    nickname = models.CharField(blank=False, null=False, max_length=100)
    gender = models.IntegerField(choices=GENDER_CHOICES, blank=False, null=False, default=3)
    email = models.EmailField(null=False, blank=False)
    mileage = models.PositiveIntegerField(default=0)
    level = models.PositiveSmallIntegerField(default=1)
    content = models.TextField(default='소개글이 없습니다.')
    # character = models.OneToOneField(Character, on_delete=CASCADE)


class Profile(models.Model):
    # 유저와 1:1 대응
    user = models.OneToOneField(User, on_delete=CASCADE)
    # 유저의 소개글
    content = models.TextField()
    # 이후 유저의 사진이나 링크, 참여 내역 등을 추가 가능


class Rank(models.Model):
    pass
