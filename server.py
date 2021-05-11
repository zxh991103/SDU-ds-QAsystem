
from flask import Flask, render_template
from flask_cors import *
def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)  # 设置跨域

    return app


app = create_app()
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/robot")
def robotindex():
    return render_template("index.html")


@app.route("/ask/<question>")
def talk(question=None):

    from _4_predict.prefromgraph import answer

    print(question)
    ans = answer(question)


    print(ans)

    return ans









if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=True)
