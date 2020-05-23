from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__)

products = {
  "sku01": { "id": "sku01", "name": "Pen", 'desc':' a great pen', "price": 15, 'img':'https://cdn.shopify.com/s/files/1/0013/9676/8815/products/k-497_1800x1800.png?v=1541660898'},
  "sku02": { "id": "sku02", "name": "Cup", 'desc':' a colorful cup', "price": 80, 'img':'https://dictionary.cambridge.org/zht/images/thumb/cup_noun_002_09489.jpg?version=5.0.74'},
  "sku03": { "id": "sku03", "name": "Notebook", 'desc':' a useful notebook', "price": 25, 'img':'https://mylamy.com.tw/wp-content/uploads/WEB_BANNER_LAMY_PAPER_01-1a.jpg'},
  "sku04": { "id": "sku04", "name": "pencil", 'desc':' a pretty pencil', "price": 10, 'img':'https://image.shutterstock.com/image-vector/vector-realistic-yellow-wooden-pencil-260nw-785835241.jpg'}
  
}


cart = [
    { 'id': 'sku01', 'num': 5},
    { 'id': 'sku02', 'num': 3},
    { 'id': 'sku03', 'num': 2},
    { 'id': 'sku04', 'num': 1},
]


@app.route("/")
def shop():
    title = 'My shop website'
    total = 0
 
    for item in cart:
        prod = products.get(item['id'])
        total += int(prod.get('price')) * int(item.get('num')) 
    return render_template('shop.html', title=title, products=products, cart=cart, total=total)

@app.route("/product/<id>")
def product(id):
    pd = products[id]
    return render_template('product.html', product=pd)

'''
@app.route("/cart/edit", methods = ['GET', 'POST'])
def cartEdit():
    if request.method == 'POST':
      pen = int(request.form['pen'])
      cup = int(request.form['cup'])
      notebook = int(request.form['notebook'])
      pencil = int(request.form['pencil'])
      cart[0]['num'] = pen
      cart[1]['num'] = cup
      cart[2]['num'] = notebook
      cart[3]['num'] = pencil
      return redirect('/')   
    return render_template("cart-edit.html", cart=cart)


@app.route('/product/<id>/edit', methods = ['GET', 'POST'])
def edit(id):
    prod = products[id]
    errors = {}
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        img = request.form['img']
        desc = request.form['desc']
        if not name:
            errors['name'] = 'name should not be empty'
        if not price:
            errors['price'] = 'price should not be empty'     
        if not img:
            errors['img'] = 'image should not be empty'
        if not desc:
            errors['desc'] = 'description shoulf not be empty'
        if len(errors) == 0:
            prod['name'] = request.form['name']
            prod['price'] = int(request.form['price'])
            prod['img'] = request.form['img']
            prod['desc'] = request.form['desc']
            return redirect('/product/' + id)

    return render_template('product-edit.html', product=prod, errors=errors)
'''
