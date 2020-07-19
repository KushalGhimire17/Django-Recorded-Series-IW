from django.db import models

class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    is_active = models.BooleanField(default=False)

    # To demonstrate addition of fields and handling migrations with default and null
    bio = models.CharField(max_length=200, default="Default bio")
    test = models.CharField(max_length=100, null=True)

    # charfield, emailfield, textfield accepts empty string
    # to avoid empty data in name and email fields
    def save(self, **kwargs):
        self.full_clean()
        return super().save(**kwargs)
