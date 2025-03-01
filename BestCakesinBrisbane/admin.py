
from flask import Blueprint
from . import db
from .models import Category, Cake, Order
from datetime import datetime


bp = Blueprint('admin', __name__, url_prefix='/admin/')

# function to put some seed data in the database


@bp.route('/dbseed/')
def dbseed():
    type1 = Category(name='chocolate', image='Chocolate.jpg',
                     description='''Chocolate''')
    type2 = Category(name='cheesecake', image='Salted-Caramel-Cheesecake3-1.jpg',
                     description='''Cheesecake''')
    type3 = Category(name='partycake', image='Birthday-cake-6',
                     description='''Party Cake''')
    type4 = Category(name='rainbowcake', image='sliced-rainbow-cake.jpg',
                     description='''Rainbow Cake''')

    try:
        db.session.add(type1)
        db.session.add(type2)
        db.session.add(type3)
        db.session.add(type4)
        db.session.commit()
    except:
        return 'There was an issue adding the types in dbseed function'

    c1 = Cake(type_id=type1.id, image='strawberry-chocolate-cake-1.jpg', price=30.00,
              date=datetime.datetime(2020, 5, 17),
              name='Strawberry Chocolate cake',
              description='Chocolate Sponge layered with Chocolate Cream and Strawberry Pulp. Topped with Chocolate Ganache and Fresh Strawberries.')
    c2 = Cake(type_id=type1.id, image='celebration_chocolate_26103_16x9.jpg', price=30.00,
              date=datetime.datetime(2020, 2, 1),
              name='Dark Chocolate Mousse Cake',
              description='Chocolate sponge triple layered with Chocolate Mousse. Topped with Fresh cream and Fresh Strawberries.')
    c3 = Cake(type_id=type2.id, image='_2559_20Continental_cheesecake_vanilla.jpg', price=30.00,
              date=datetime.datetime(2020, 3, 10),
              name='French Glaze Vanilla',
              description='Our classic continental cheesecake topped with a French vanilla glaze. Decorated with cream cheese icing, Belgian white choc shards and gold pearls.')
    c4 = Cake(type_id=type2.id, image='_2545_20Baked_cheesecake_berry.jpg', price=30.00,
              date=datetime.datetime(2020, 8, 1),
              name='Wildberry Baked',
              description='A vanilla cheesecake, with swirls of berry compote baked on a graham biscuit base. Finished with fresh strawberries and blueberries and a wildberry flavoured mousse.')
    c5 = Cake(type_id=type3.id, image='Birthday-cake-6.jpg', price=30.00,
              date=datetime.datetime(2020, 4, 20),
              name='Birthday Cake',
              description='Covered in frosting finish with chocolate drip. Colours can be changed to suit your celebration. Fresh Flowers need to be supplied from a florist (taped & wired).')
    c6 = Cake(type_id=type3.id, image='71ae-wYwUQL._AC_SX679_.jpg', price=30.00,
              date=datetime.datetime(2021, 1, 2),
              name='Birthday Party Cupcakes',
              description='These brilliant Birthday Cupcakes for the kids will put a smile on every face at your next birthday!.')
    c7 = Cake(type_id=type4.id, image='1552683774324.jpg', price=30.00,
              date=datetime.datetime(2020, 11, 1),
              name='Rainbow Cake',
              description='The sweetest mini celebration cake! Five layers of colorful, moist cake with vanilla frosting and a confetti of rainbow sprinkles.')
    c8 = Cake(type_id=type4.id, image='f2d29a10-8cf2-42cc-ac82-0ff43862394a.jpg', price=30.00,
              date=datetime.datetime(2020, 4, 1),
              name='Rainbow Cake Roll',
              description='A bright and colorful rainbow cake roll filled with a whipped rainbow chip frosting filling.')

    try:
        db.session.add(c1)
        db.session.add(c2)
        db.session.add(c3)
        db.session.add(c4)
        db.session.add(c5)
        db.session.add(c6)
        db.session.add(c7)
        db.session.add(c8)
        db.session.commit()
    except:
        return 'There was an issue adding a cake in dbseed function'

    return 'DATA LOADED'
