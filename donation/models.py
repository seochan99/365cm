from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.
class Donate(models.Model):
    id = models.AutoField(primary_key=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    hair_length = models.IntegerField(validators=[MinValueValidator(25)], null=False)
    HAIR_CONDITION = (
        ('high', 'high'),
        ('middle', 'middle'),
        ('low', 'low'),
    )
    hair_condition = models.CharField(choices=HAIR_CONDITION, max_length=50, null=True, blank=True)
    body = models.TextField()
    image=models.ImageField(upload_to="image/", default=None, null=True, blank=True)
    donate_member = models.ManyToManyField(
        User, related_name="donate_member", through="member"
    )  # 가입된 유저들
    approved = models.BooleanField(default=False)
    beststory = models.IntegerField(null=True)

    def summary(self):
        return self.body[:30]


class member(models.Model):
    Donate = models.ForeignKey(Donate, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)