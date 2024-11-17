from flask import Flask, render_template,redirect,url_for,request,flash
from models import db, Purchase, Items, Company, Sales, add_cmpy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import desc


app =Flask(__name__)
app.secret_key='pottyshop'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()
    add_cmpy()

#Home
@app.route('/')
def home():
    company=Company.query.first()
    items=Items.query.all()
    purchase=Purchase.query.all()
    return render_template('index.html',company=company,items=items,purchase=purchase)

#To Add Items
@app.route('/add_items',methods=['POST','GET'])
def add_items():
    if request.method=='POST':
        item_name=request.form['item_name'].strip().upper()
        if Items.query.filter_by(item_name=item_name).first() :
            flash('item already exist','error')
        else:
            db.session.add(Items(item_name=item_name))
            db.session.commit()
            flash('item added successfully','success')
            return redirect(url_for("add_items"))
    return render_template('add_items.html')


#To Purchase Product
@app.route('/purchase', methods=['GET', 'POST'])
def purchase():
    company = Company.query.first() 
    items = Items.query.all() 
    if request.method == 'POST':
        selected_item_id = request.form.get('item_id')
        qty = int(request.form.get('qty', 0))
        rate = float(request.form.get('rate', 0.0))
        amount = qty * rate
        if company.cash_bal >= amount:
            item = Items.query.get(selected_item_id)
            
            if item:
                db.session.add(Purchase(pitem_id=selected_item_id, qty=qty, rate=rate, amount=amount))
                item.item_qty += qty
                item.item_lastpur = rate 
                if item.item_lastsale is not None: 
                    item.item_lastsale = 0
                    item.item_profit=0
            
                company.cash_bal -= amount
                db.session.commit()
                flash('Purchase successful!', 'success')
            else:
                flash('Item does not exist!', 'error')
        else:
            flash('Insufficient cash balance!', 'error')
        
        return redirect(url_for('purchase'))
    return render_template('purchase.html', company=company, items=items)

#To purchase item by id
@app.route('/purchase/<int:id>', methods=['GET', 'POST'])
def purchase_item(id):
    item = Items.query.get(id)
    company = Company.query.first() 

    if not item:
        flash("Item not found.")
        return redirect(url_for('purchase'))

    if request.method == 'POST':
        qty = int(request.form['qty'])
        rate = float(request.form['rate'])
        amount = qty * rate
        if company.cash_bal >= amount:
            purchase = Purchase(pitem_id=item.item_id, qty=qty, rate=rate, amount=amount)
            db.session.add(purchase)
            item.item_qty += qty
            item.item_lastpur = rate 

            if item.item_lastsale is not None:
                item.item_lastsale = 0
                item.item_profit = 0
            company.cash_bal -= amount
            db.session.commit()
            return redirect(url_for('home'))
        else:
            flash('Insufficient cash balance!', 'error')
            return redirect(url_for('purchase_item',id=id))
    return render_template('purchase_id.html', item=item)

#To sale the items  
@app.route('/sales', methods=['GET', 'POST'])
def sale():
    company = Company.query.first() 
    items = Items.query.all() 
    
    if request.method == 'POST':
        selected_item_id = request.form.get('item_id')
        qty = int(request.form.get('qty', 0))
        rate = float(request.form.get('rate', 0.0))
        amount = qty * rate
        item = Items.query.get(selected_item_id)
        if item and item.item_qty >= qty:
            item.item_qty -= qty
            item.item_lastsale = rate  
            if item.item_lastpur is not None:  
                purchase_price = item.item_lastpur
                profit_percentage = int(((rate - purchase_price) / purchase_price) * 100)
                item.item_profit = profit_percentage  
            db.session.add(Sales(s_item_id=selected_item_id, s_qty=qty, s_rate=rate, s_amount=amount))
            company.cash_bal += amount
            db.session.commit()
            flash('Sale successful!', 'success')
        else:
            flash('Not enough stock or item does not exist!', 'error')
        
        return redirect(url_for('sale'))
    return render_template('sales.html', company=company, items=items)

#to sale the item by id
@app.route('/sale/<int:id>', methods=['GET', 'POST'])
def sale_item(id):
    item = Items.query.get(id)
    company = Company.query.first()  
    if not item:
        flash("Item not found.")
        return redirect(url_for('sale'))
    
    if request.method == 'POST':
        qty = int(request.form['qty'])
        rate = float(request.form['rate'])
        amount = qty * rate
        if item.item_qty >= qty:
            sale = Sales(s_item_id=item.item_id, s_qty=qty, s_rate=rate, s_amount=amount)
            db.session.add(sale)
            item.item_qty -= qty
            item.item_lastsale = rate  
            if item.item_lastpur is not None:
                purchase_price = item.item_lastpur
                profit_percentage = int(((rate - purchase_price) / purchase_price) * 100)
                item.item_profit = profit_percentage  

            company.cash_bal += amount
            db.session.commit()
            return redirect(url_for('home'))
        else:
            flash('Not enough stock!', 'error')
            return redirect(url_for('sale_item',id=id))
    return render_template('sale_id.html', item=item)


#To view the purchase history
@app.route('/purchase_history')
def purchase_history():
    purchase_history = db.session.query(Purchase, Items).join(Items, Purchase.pitem_id == Items.item_id).all()
    return render_template('purchase_history.html',new_his=purchase_history)

#To view the sale history
@app.route('/sales_history')
def sale_history():
    new_his=db.session.query(Sales,Items).join(Items,Sales.s_item_id == Items.item_id).all()
    return render_template('sales_history.html',new_his=new_his)

#To edit the item 
@app.route('/edit_item/<int:id>', methods=['POST', 'GET'])
def edit_item(id):
    items = Items.query.get_or_404(id)
    if request.method == 'POST':
        item_name = request.form['item_name'].strip().upper()
        existing_item = Items.query.filter(Items.item_name == item_name, Items.item_id != id).first()
        if existing_item:
            flash('Item with this name already exists.', 'error')
        else:
            items.item_name = item_name
            db.session.commit()
            return redirect(url_for("home"))
    return render_template('edit_item.html', items=items)


if __name__=='__main__':
    app.run(debug=True)