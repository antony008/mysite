from jinja2 import Template

def catcatHTML():
    with open('catcat.html', encoding="utf-8") as f:
        s = f.read()
    return s

def main():
    image_list = [
        {'title': 'cat1', 'url':'https://stickershop.line-scdn.net/stickershop/v1/product/9284063/LINEStorePC/main.png'},
        {'title': 'cat2', 'url':'https://2.bp.blogspot.com/-Y53VpFoLXr4/XA8bfVYm8lI/AAAAAAAMUow/irqcmerQYtYKrNrS6zN33UpN6HFHb62OgCLcBGAs/s1600/AS0004692_01.gif'},
        {'title': 'cat3', 'url':'https://66.media.tumblr.com/28e8756395b4dab2032226f984957df6/tumblr_o7ku9e7MiH1umk6azo1_1280.jpg'}
    ]
    tmpl = Template(catcatHTML()) 
    print(tmpl.render({'image': image_list}))

main()