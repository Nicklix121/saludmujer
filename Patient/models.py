import mongoengine as me

class Patient(me.Document):
    first_name = me.StringField(max_length=100, required=True)
    last_name = me.StringField(max_length=100, required=True)
    run = me.StringField(required=True, unique=True)
    email = me.EmailField()
    phone = me.StringField()
    birth_date = me.DateField()
    gender = me.StringField(choices=["F", "M", "Otro"])
    region = me.StringField()
    city = me.StringField()
    address = me.StringField()
    health_provider = me.StringField()
    created_at = me.DateTimeField()
    updated_at = me.DateTimeField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
