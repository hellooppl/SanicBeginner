from sanic import Sanic
from sanic.response import text, json

app = Sanic(__name__)

if __name__ == "__main__":
    app.run(debug=True)