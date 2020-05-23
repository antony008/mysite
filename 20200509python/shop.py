from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__)

products = {
  "sku01": { "id": "sku01", "name": "Pen", 'desc':' a great pen', "price": 15, 'img':'https://cdn.shopify.com/s/files/1/0013/9676/8815/products/k-497_1800x1800.png?v=1541660898'},
  "sku02": { "id": "sku02", "name": "Cup", 'desc':' a colorful cup', "price": 80, 'img':'https://dictionary.cambridge.org/zht/images/thumb/cup_noun_002_09489.jpg?version=5.0.74'},
  "sku03": { "id": "sku03", "name": "Notebook", 'desc':' a useful notebook', "price": 25, 'img':'https://mylamy.com.tw/wp-content/uploads/WEB_BANNER_LAMY_PAPER_01-1a.jpg'},
  "sku04": { "id": "sku04", "name": "pencil", 'desc':' a pretty pencil', "price": 10, 'img':'https://image.shutterstock.com/image-vector/vector-realistic-yellow-wooden-pencil-260nw-785835241.jpg'}
  
}


mycart={
    'sku01':3
}

@app.route("/")
def shop():
    title = 'My shop website'
    total = 0
 
    for item in cart:
        prod = products.get(item['id'])
        total += int(prod.get('price')) * int(item.get('num')) 
    return render_template('shop.html', title=title, products=products, mycart=mycart, total=total)

@app.route("/product/<id>")
def product(id):
    pd = products[id]
    return render_template('product.html', product=pd)


@app.route("/cart")
def cartView():
    return render_template('cart.html', mycart=mycart, products=products)


@app.route("/add-cart/<sid>")
def addCart(sid):
    mycart[sid] = mycart.get(sid, 0) + 1
    return redirect("/cart")


