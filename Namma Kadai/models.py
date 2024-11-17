from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta, datetime

db=SQLAlchemy()


def get():
    return (datetime.utcnow()+timedelta(hours=5, minutes=30)).replace(microsecond=0)

class Company(db.Model):
    cmpy_id = db.Column(db.Integer, primary_key=True)
    cmpy_name = db.Column(db.String(150), nullable=False, default="Namma Kadai")
    cash_bal = db.Column(db.Integer, default=1000.00)


class Items(db.Model):
    item_id=db.Column(db.Integer, primary_key=True)
    item_name=db.Column(db.String(150),nullable=False, unique=True)
    item_qty=db.Column(db.Integer, default=0)
    item_lastpur=db.Column(db.Float)
    item_lastsale=db.Column(db.Float)
    item_profit=db.Column(db.Integer)

class Purchase(db.Model):
    pur_id=db.Column(db.Integer, primary_key=True)
    pur_time = db.Column(db.DateTime, default=get)
    pitem_id=db.Column(db.Integer, db.ForeignKey('items.item_id'),nullable=False)
    qty=db.Column(db.Integer,nullable=False)
    rate=db.Column(db.Float, nullable=False)
    amount=db.Column(db.Float)

class Sales(db.Model):
    sale_id=db.Column(db.Integer, primary_key=True)
    sale_time=db.Column(db.DateTime, default=get)
    s_item_id=db.Column(db.Integer, db.ForeignKey('items.item_id'),nullable=False)
    s_qty=db.Column(db.Integer, db.ForeignKey('purchase.qty'),nullable=False)
    s_rate=db.Column(db.Float, db.ForeignKey('purchase.rate'),nullable=False)
    s_amount=db.Column(db.Float,db.ForeignKey('purchase.amount'),nullable=False)

def add_cmpy():
     def_cmpy=Company.query.filter_by(cmpy_name="Namma Kadai").first()
     if not def_cmpy:
          new_cmpy=Company(cmpy_name="Namma Kadai", cash_bal=1000.00)
          db.session.add(new_cmpy)
          db.session.commit()