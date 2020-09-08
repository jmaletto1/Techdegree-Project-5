import datetime
from peewee import *

DATABASE = SqliteDatabase('journals.db')


class Journal(Model):
    j_id = IntegerField(primary_key=True)
    title = TextField(unique=True)
    date = DateTimeField(default=datetime.datetime.now)
    time_spent = IntegerField
    learnt = TextField
    resources = TextField

    class Meta:
        database = DATABASE

    @classmethod
    def add_entry(cls, title, date, time_spent, learnt, resources):
        try:
            with DATABASE.transaction():
                cls.create(
                    title=title,
                    date=date,
                    time_spent=time_spent,
                    learnt=learnt,
                    resources=resources
                )
        except IntegrityError:
            raise ValueError("This entry already exists!")


def initialise():
    DATABASE.connect()
    DATABASE.create_tables([Journal], safe=True)
    DATABASE.close()
