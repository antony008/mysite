

<div class="container">
    <table class="table">
    <tr>
        <th>name</th>
        <th>Number</th>
        <th>price</th>
        <th>total</th>
    </tr>

{% for item in cart %}
{% set prod = products.get(item['id'])%}
<tr>
    <td>{{ prod.name }}</td>
    <td>{{ item.num }}</td>
    <td>{{ prod.price }}</td>
    <td>{{ item.num * prod.price }}</td>
</tr>
{% endfor %}    
</table>
</div>

<h2>y cart total: {{total}}</h2>



<a href="/cart/edit">CartEdit</a>


<a href="/product/<id>/edit">ProductEdit</a>