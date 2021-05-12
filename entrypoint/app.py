from sanic import Sanic
from sanic.response import text, json
from . import service_layer,abstract

app = Sanic(__name__)


@app.route('/test',methods=["POST","PUT","GET"])
async def handler(request):
    if request.method == "POST":
        print(request.json["delivery_id"])
        return text('accepted')
    return text('OKAYY......')

@app.route("/agent", methods=['GET', 'POST'])
def add_new_agent(request):
    service.add_shipping(validated_data=abstract.AddShipping(
        category='food',
        cost='202',
        regionId=10,
        orderId=22,
        insurance=55.2,
        date_to_ship= "2010-8-10"
    ))
    return Text("success")


if __name__ == "__main__":
    app.run(debug=True)