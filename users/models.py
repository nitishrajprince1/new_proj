from django.db import models

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    password_hash = models.CharField(max_length=255)
    password_salt = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    time_remaining = models.SmallIntegerField()
    last_time_remaining_update = models.DateTimeField(auto_now=True)
    banked_time = models.SmallIntegerField()
    coins_remaining = models.SmallIntegerField()
    register_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    lifecycle_status = models.SmallIntegerField()
    notes = models.CharField(max_length=255)
    subscription_status = models.SmallIntegerField()

    class Meta:
        managed = True
        db_table = "user"

class Person(models.Model):
    person_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    passport_num_hash = models.CharField(max_length=255)
    passport_num_salt = models.CharField(max_length=255)
    passport_photo_ref = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = "person"

class UserLoginLog(models.Model):
    user_login_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=255, null=True)
    login_datetime = models.DateTimeField(null=True)
    logout_datetime = models.DateTimeField(null=True)
    login_success_flg = models.BooleanField(null=True)
    login_fail_reason_id = models.SmallIntegerField(null=True)
    facial_analysis_video_ref = models.CharField(max_length=255, null=True)

    class Meta:
        managed = True
        db_table = "user_login_log"
