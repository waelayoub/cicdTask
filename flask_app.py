from flask import Flask

app = Flask("myProject")


@app.route('/hello')
def functionality():
    return "HELLO"


app.run(debug=True, host='0.0.0.0', port=12121)
