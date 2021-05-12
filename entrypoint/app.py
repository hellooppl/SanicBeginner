from sanic import Sanic
from sanic.response import text, json

app = Sanic(__name__)


@app.route('/test',methods=["POST","PUT","GET"])
async def handler(request):
    if request.method == "POST":
        print(request.json["delivery_id"])
        return text('accepted')
    return text('OKAYY......')


if __name__ == "__main__":
    app.run(debug=True)