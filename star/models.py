from django.db.models import Model, UUIDField, CharField, FloatField
class Star(Model):
    id = UUIDField(primary_key=True)
    name = CharField(max_length=45)
    constellation = CharField(max_length=45)
    absolute_magnitude = FloatField()
    apparent_magnitude = FloatField()
    distance = FloatField()

