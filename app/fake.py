from operator import length_hint
from random import randint
from sqlalchemy.exc import IntegrityError
from faker import Faker
from . import db
from .models import Listing,User

def usersGE(count=10):
    fake = Faker('ge_GE')
    games = ['Tennis', 'Call of Duty: Vanguard', 'Water Polo', 'Chess', 'Minecraft', 'GTA5', 'Volleyball', 'Beachvolley', 'Forza Horizon 5', 'Basket Ball', 'Stardew Valley']
    platforms = ['Physical', 'PC', 'Xbox', 'Playstation', 'Nintendo']
    i = 0
    while i < count:
        bio_length = randint(100, 500)
        u = User(email=fake.email(),
            role_id = 2,
            username=fake.user_name(),
            password='password',
            confirmed=True,
            bio=fake.text(bio_length),
            country='Germany',
            city=fake.city())
        db.session.add(u)
        try:
            db.session.commit()
            l = 0
            while l < randint(1, 5):
                header_length = randint(30, 120)
                info_length = randint(100, 300)
                listing = Listing(user_id=u.id,
                                  header=fake.text(header_length),
                                  game=fake.word(ext_word_list=games),
                                  platform=fake.word(ext_word_list=platforms),
                                  info=fake.text(info_length))
                db.session.add(listing)
                db.session.commit()
                l += 1
            i += 1
        except IntegrityError:
            db.session.rollback()

def usersFI(count=10):
    fake = Faker('fi_FI')
    games = ['Tennis', 'Call of Duty: Vanguard', 'Water Polo', 'Chess', 'Minecraft', 'GTA5', 'Volleyball', 'Beachvolley', 'Forza Horizon 5', 'Basket Ball', 'Stardew Valley']
    platforms = ['Physical', 'PC', 'Xbox', 'Playstation', 'Nintendo']
    i = 0
    while i < count:
        bio_length = randint(100, 500)
        u = User(email=fake.email(),
            role_id = 2,
            username=fake.user_name(),
            password='password',
            confirmed=True,
            bio=fake.text(bio_length),
            country='Finland',
            city=fake.city())
        db.session.add(u)
        try:
            db.session.commit()
            l = 0
            while l < randint(1, 5):
                header_length = randint(30, 120)
                info_length = randint(100, 300)
                listing = Listing(user_id=u.id,
                                  header=fake.text(header_length),
                                  game=fake.word(ext_word_list=games),
                                  platform=fake.word(ext_word_list=platforms),
                                  info=fake.text(info_length))
                db.session.add(listing)
                db.session.commit()
                l += 1
            i += 1
        except IntegrityError:
            db.session.rollback()

def usersGB(count=10):
    fake = Faker('en_GB')
    games = ['Tennis', 'Call of Duty: Vanguard', 'Water Polo', 'Chess', 'Minecraft', 'GTA5', 'Volleyball', 'Beachvolley', 'Forza Horizon 5', 'Basket Ball', 'Stardew Valley']
    platforms = ['Physical', 'PC', 'Xbox', 'Playstation', 'Nintendo']
    i = 0
    while i < count:
        bio_length = randint(100, 500)
        u = User(email=fake.email(),
            role_id = 2,
            username=fake.user_name(),
            password='password',
            confirmed=True,
            bio=fake.text(bio_length),
            country='United Kingdom of Great Britain and Northern Ireland',
            city=fake.city())
        db.session.add(u)
        try:
            db.session.commit()
            l = 0
            while l < randint(1, 5):
                header_length = randint(30, 120)
                info_length = randint(100, 300)
                listing = Listing(user_id=u.id,
                                  header=fake.text(header_length),
                                  game=fake.word(ext_word_list=games),
                                  platform=fake.word(ext_word_list=platforms),
                                  info=fake.text(info_length))
                db.session.add(listing)
                db.session.commit()
                l += 1
            i += 1
        except IntegrityError:
            db.session.rollback()