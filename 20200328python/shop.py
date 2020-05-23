from flask import Flask, render_template
app = Flask(__name__)

products = {
  "sku01": { "id": "sku01", "name": "Pen", "price": 15 },
  "sku02": { "id": "sku02", "name": "Cup", "price": 80 },
  "sku03": { "id": "sku03", "name": "Notebook", "price": 25 },
  "sku04": { "id": "sku04", "name": "pencil", "price": 10 },
  
}
image =  {"sku01": "https://cdn.shopify.com/s/files/1/0013/9676/8815/products/k-497_1800x1800.png?v=1541660898",
            "sku02": "https://dictionary.cambridge.org/zht/images/thumb/cup_noun_002_09489.jpg?version=5.0.74", 
            "sku03": "https://mylamy.com.tw/wp-content/uploads/WEB_BANNER_LAMY_PAPER_01-1a.jpg", 
            "sku04": "https://image.shutterstock.com/image-vector/vector-realistic-yellow-wooden-pencil-260nw-785835241.jpg" }

cart = [
    { 'id': 'sku01', 'num': 5},
    { 'id': 'sku03', 'num': 3}
]


@app.route("/")
def shop():
    title = 'My shop website'
    subtitle = 'you can shop here'
    #image = image[id]
    total = 0
    for item in cart:
        prod = products.get(item['id'])
        total += int(prod.get('price')) * int(item.get('num'))
    

    return render_template('shop.html', title=title, subtitle=subtitle, products=products, image=image, cart=cart, total=total)

@app.route("/product/<id>")
def product(id):
    p = products[id]
    #image = image[id]
    return render_template("product.html", product=p, image=image)