from flask import Flask, redirect, url_for, request, render_template, session
from models import *
from controllers import *

app = Flask(__name__)
app.secret_key = "123Vivalalgerie"

delivery_controller = DeliveryController.getInstance()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/request_delivery", methods=["POST", "GET"])
def request_delivery():
    if request.method == "POST":
        delivery_controller.extract_delivery(request.form)
        return redirect(url_for('deliveries'))
    
    else:
        return render_template("request_delivery.html")
    
@app.route('/deliveries')
def deliveries():
    return render_template("deliveries.html", deliveries=delivery_controller.deliveries)


if __name__ == "__main__":
    app.run()
