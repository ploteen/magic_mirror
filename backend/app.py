from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

port_num = "8000"
host_addr = "0.0.0.0"

if __name__ == "__main__":
    app.run(host=host_addr,port=port_num,debug=True)