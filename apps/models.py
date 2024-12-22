from django.db.models import Model, CharField, DateField, ManyToManyField


class Genre(Model):
       name = CharField(max_length=255)

class Film(Model):
    title = CharField(max_length=255)
    released_data = DateField(auto_now=True)
    genre = ManyToManyField(Genre)

#     assddadsad

