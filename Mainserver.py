from flask import Flask, render_template, request
from ESP import ESP


app = Flask(__name__)

esp1 = ESP("esp1", "4d2a4b6j7")
esp1.components = {"LED1": "5", 'LM35':'A0'}

esp2 = ESP("esp2", "4d2a4b6j8")
esp2.components = {"LED2": "5"}


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        if request.form.get('LED1'):
            esp1.request_page('LED1', request.form['LED1'])
        elif request.form.get('LED2'):
            esp2.request_page('LED2', request.form['LED2'])
    return render_template(
        "gui.html",
        led1=esp1.boot_status('LED1'),
        led2=esp2.boot_status('LED2'))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=1000)
