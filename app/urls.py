from .views import app, item_views, purchase_views, get_single_item, \
    update_single_item, delete_s_item, item_create, purchase_create, get_single_purchase,\
    update_single_purchase,delete_single_purchase

app.add_url_rule('/purchase', view_func=purchase_views, methods=['GET', ], endpoint='purchase')
app.add_url_rule('/purchase/create', view_func=purchase_create, methods=['GET', 'POST'], endpoint='purchase_create')
app.add_url_rule('/purchase/<int:purchase_id>', view_func=get_single_purchase,methods=['GET','POST'], endpoint='get_purchase')
app.add_url_rule('/purchase/<int:purchase_id>/update', view_func=update_single_purchase,methods=['GET','POST'], endpoint='update_purchase')
app.add_url_rule('/purchase/<int:purchase_id>/delete', view_func=delete_single_purchase,methods=['GET','POST'], endpoint='delete_purchase')

app.add_url_rule('/item', view_func=item_views, methods=['GET', ], endpoint='item')
app.add_url_rule('/item/create', view_func=item_create, methods=['GET', 'POST'], endpoint='create_item')
app.add_url_rule('/item/<int:item_id>', view_func=get_single_item, methods=['GET', ], endpoint='single_item')
app.add_url_rule('/item/<int:item_id>/update', view_func=update_single_item, methods=['GET', 'POST'],
                 endpoint='update_single_item')
app.add_url_rule('/item/<int:item_id>/delete', view_func=delete_s_item, methods=['GET', 'POST'],
                 endpoint='delete_s_item')
