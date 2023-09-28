from flask import Flask

app = Flask("myProject")


@app.route('/hello')
def functionality():
    return "HELLO"


app.run(debug=True, host='127.0.0.1', port=12121)
