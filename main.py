from flask import Flask, Response
from checkout_controller import CheckoutController

app = Flask(__name__)
controller = CheckoutController()


@app.route('/newCheckout')
def new_checkout():
    controller.clear_checkout()
    return Response("OK", status=200, mimetype='text/plain')


@app.route('/add/<item>')
def add_item(item):
    return Response("Item added", status=200, mimetype='text/plain') \
        if controller.add_item(item) \
        else Response("Item not found", status=400, mimetype='text/plain')


@app.route('/getTotal')
def get_total():
    return Response(f"Total {controller.get_total()} €", status=200, mimetype='text/plain')


if __name__ == '__main__':
    app.run()
