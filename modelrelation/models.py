"""REC65
    OneToOne:>>> Parent to child: <parent_obj>.<child class lower name>.<child_attributes>
            >>> user.userdetail.age
            >>> Child to Parent: <child_obj>.<foreign_attribute>.<parent_attributes>
            >>> detail.user_relation.name
    ForeignKey:>>> Parent to Child: <parent_obj>.<child class lower name>_set.<child_attributes>
               >>> address.userdetail_set.all()
               >>> Child to Parent: <child_obj>.<foreign_attribute>.<parent_attribute>
               >>> detail.address.street
    ManyToMany:
            >>> nepal = Country.objects.create(name="Nepal")
            >>> shyam = UserDetail.objects.get(user_Relation_id=3)
            >>> shyam.country.add(nepal)
            >>> shyam.country.remove(nepal)
"""

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)

class Address(models.Model):
    street = models.CharField(max_length=100)

class Country(models.Model):
    name = models.CharField(max_length=100)

class UserDetail(models.Model):
    age = models.IntegerField()
    user_relation = models.OneToOneField(User, on_delete=models.CASCADE)
    # address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, related_name="useraddress_set")
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    country = models.ManyToManyField(Country)

class BaseModel(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        abstract = True

class Informarion(BaseModel):
    info = models.CharField(max_length=100)
    bio = models.TextField()