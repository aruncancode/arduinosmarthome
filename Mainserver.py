from flask import Flask, render_template, request
from ESP import ESP


app = Flask(__name__)

esp1 = ESP("esp1", "id")
esp1.components = {"LED1": "5", "LED2": "6"}

esp2 = ESP("esp2", "id")
esp2.components = {"LED3": "5", "LED4": "6"}

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        if request.form.get('LED1'):
            esp1.request_page('LED1', request.form['LED1'])
        elif request.form.get('LED2'):
            esp1.request_page('LED2', request.form['LED2'])
        elif request.form.get('LED3'):
            esp2.request_page('LED3', request.form['LED3'])
        elif request.form.get('LED4'):
            esp2.request_page('LED4', request.form['LED4'])
    return render_template("gui.html", led1=esp1.boot_status('LED1'), led2=esp1.boot_status('LED2'), 
    led3=esp2.boot_status('LED3'), led4=esp2.boot_status('LED4'), esp1status=esp1.esp_status(), esp2status=esp2.esp_status())

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=1000)


    