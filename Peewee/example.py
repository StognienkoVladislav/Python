
from peewee import *
from datetime import date

db = SqliteDatabase('people.db')


class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db


class Pet(Model):
    owner = ForeignKeyField(Person, backref="pets")
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db


db.connect()
db.create_tables([Person, Pet])

uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15))
uncle_bob.save()

grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1))
herb = Person.create(name='Herb', birthday=date(1950, 5, 5))

grandma.name = 'Grandma L.'
grandma.save()


bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')

herb_mittens.delete_instance()


herb_fido.owner = uncle_bob
herb_fido.save()


print(Person.select().where(Person.name == 'Grandma L.').get())
print(Person.get(Person.name == 'Grandma L.'))

for person in Person.select():
    print(person.name)

query = Pet.select().where(Pet.animal_type == 'cat')
for pet in query:
    print(pet.name, pet.owner.name)

##################################################
query = (Pet
         .select(Pet, Person)
         .join(Person)
         .where(Pet.animal_type == 'cat'))

for pet in query:
    print(pet.name, pet.owner.name)
##################################################

for pet in Pet.select().join(Person).where(Person.name == 'Bob'):
    print(pet.name)

for pet in Pet.select().where(Pet.owner == uncle_bob):
    print(pet.name)


# Sorting
for pet in Pet.select().where(Pet.owner == uncle_bob).order_by(Pet.name):
    print(pet.name)

for person in Person.select().order_by(Person.birthday.desc()):
    print(person.name, person.birthday)


# Combining filter expressions
d1940 = date(1940, 1, 1)
d1960 = date(1960, 1, 1)
query = (Person
         .select()
         .where((Person.birthday < d1940) | (Person.birthday > d1960)))

for person in query:
    print(person.name, person.birthday)


# Aggregates and Prefetch

for person in Person.select():
    print(person.name, person.pets.count(), 'pets')

