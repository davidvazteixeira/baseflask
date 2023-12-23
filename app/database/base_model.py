from app import app
from peewee import *
import datetime

def make_table_name(model_class):
    model_name = model_class.__name__
    return model_name.lower() + 's'

class BareModel(Model):
    class Meta:
        legacy_table_names=False
        database = app.db
        table_function = make_table_name
        primary_key = False

class SimpleModel(Model):
    class Meta:
        legacy_table_names=False
        database = app.db
        table_function = make_table_name

    id = PrimaryKeyField(null=False)
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=None, null = True)

    def save(self, *args, **kwargs):
        if not self.id == None:
            self.updated_at = datetime.datetime.now()
        return super(SimpleModel, self).save(*args, **kwargs)
