from sanic import Sanic
import os
from sanic.response import text, json
from ..domain.models import Delivery, Shipping
from ..service_layer import services, abstract


app = Sanic(__name__)

@app.route("/shipping", methods=['GET', 'POST'])
def add_new_agent(request):
    services.add_shipping(validated_data=abstract.AddShipping(
        category=request.json["category"],
        cost=request.json["cost"],
        regionId=request.json["regionId"],
        orderId=request.json["orderId"],
        insurance=request.json["insurance"],
        date_to_ship= request.json["date_to_ship"]
    ))
    return Text("success")


if __name__ == "__main__":
    s = os.path.abspath("service_layer")
    print(s)
    app.run(debug=True)