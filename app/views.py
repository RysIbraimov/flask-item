import datetime
from flask import render_template, request,redirect,url_for,flash
from . import app, db
from .models import Purchase, Item
from .forms import PurchaseForm, ItemForm


# @app.route('/client', methods=['GET', 'POST'])
def item_views():
    title = 'Список товаров'
    items = Item.query.all()
    return render_template('items.html', items=items,title=title)

def item_create():
    title = 'Добавление товара'
    form = ItemForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            item = Item()
            form.populate_obj(item)
            db.session.add(item)
            db.session.commit()
            flash(f'Товар под номером {item.id} успешнр добавлен', 'success')
            return redirect(url_for('item'))
        else:
            for field,errors in form.errors.items():
                for error in errors:
                    flash(f'Ошибка в поле {field} текст : {error}', 'danger')

    return render_template('item_form.html',form=form,title=title)


# @app.route('/purchase', methods=['GET', 'POST'])
def purchase_views():
    title = 'Список покупателей'
    purchases = Purchase.query.all()


    return render_template('purchase.html', purchases=purchases, title=title)


def purchase_create():
    title = 'Добавить клиента'
    form = PurchaseForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            purchase = Purchase()
            form.populate_obj(purchase)
            db.session.add(purchase)
            db.session.commit()
            flash(f'Успешно товар продан покупателю {purchase.id} успешнo добавлен', 'success')
            return redirect(url_for('purchase'))
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f'{field} {error}', 'danger')
    return render_template('purchase_form.html', form=form, title=title)


def get_single_purchase(purchase_id):
    purchase = Purchase.query.filter_by(id=purchase_id).first()
    return render_template('get_single_purchase.html',purchase=purchase)

def update_single_purchase(purchase_id):
    purchase = Purchase.query.filter_by(id=purchase_id).first()
    form = PurchaseForm(request.form, obj=purchase)
    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(purchase)
            db.session.commit()
            flash(f'Klient : {purchase.id} obnavlen', 'success')
            return redirect(url_for('single_item',purchase_id=purchase.id))
        else:
            for field,errors in form.errors.items():
                for error in errors:
                    flash(f'Ошибка в поле {field} текст : {error}', 'danger')

    return render_template('purchase_form.html', form=form)



def delete_single_purchase(purchase_id):
    purchase = Purchase.query.filter_by(id=purchase_id).first()
    if request.method == 'GET':
        return render_template('delete_single_purchase.html',purchase=purchase)
    if request.method == 'POST':
        db.session.delete(purchase)
        db.session.commit()
        return redirect(url_for('purchase'))



def get_single_item(item_id):
    item = Item.query.filter_by(id=item_id).first()
    return render_template('single_item.html', item=item)



def update_single_item(item_id):
    item = Item.query.filter_by(id=item_id).first()
    form = ItemForm(request.form, obj=item)
    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(item)
            db.session.commit()
            flash(f'tovar : {item.id} obnavlen', 'success')
            return redirect(url_for('single_item',item_id=item.id))
        else:
            for field,errors in form.errors.items():
                for error in errors:
                    flash(f'Ошибка в поле {field} текст : {error}', 'danger')

    return render_template('item_form.html', form=form, item=item)


def delete_s_item(item_id):
    item = Item.query.filter_by(id=item_id).first()
    if request.method == 'GET':
        return render_template('delete_item.html',item=item)
    if request.method == 'POST':
        db.session.delete(item)
        db.session.commit()
        return redirect(url_for('item'))
