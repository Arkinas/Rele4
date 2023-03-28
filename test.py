html='''
<html lang="ru">
              <style>
                place{position: absolute; top: 50px; left: 40%;}
                 .datch{margin-left: 43%;}
                 .txt {text-align: center;}
                 .button1 {
                    padding: 1.3em 3em;
                    font-size: 12px;
                    width: 150px;
                    text-transform: uppercase;
                    letter-spacing: 2.5px;
                    font-weight: 500;
                    color: #000;
                    background-color: #c2c2c2;
                    border: none;
                    border-radius: 45px;
                    box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);
                    transition: all 0.3s ease 0s;
                    cursor: pointer;
                    outline: none;
                    }

                .button1:hover {
                     background-color: #23c483;
                    box-shadow: 0px 15px 20px rgba(46, 229, 157, 0.4);
                    color: #fff;
                    }

                .button1:focus{
                    background-color: #23c483;
                    box-shadow: 0px 15px 20px rgba(46, 229, 157, 0.4);
                    color: #fff;
                }
                .button1:active {
                    transform: translateY(-1px);
                }
                
                
                .button2 {
                    padding: 1.3em 3em;
                    font-size: 12px;
                    width: 150px;
                    text-transform: uppercase;
                    letter-spacing: 2.5px;
                    font-weight: 500;
                    color: #000;
                    background-color: #c2c2c2;
                    border: none;
                    border-radius: 45px;
                    box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);
                    transition: all 0.3s ease 0s;
                    cursor: pointer;
                    outline: none;
                }

                .button2:hover {
                    background-color: #c43623;
                    box-shadow: 0px 15px 20px rgba(255, 3, 3, 0.4);
                    color: #fff;
                }
                .button2:focus {
                    background-color: #c43623;
                    box-shadow: 0px 15px 20px rgba(255, 3, 3, 0.4);
                    color: #fff;
                }
                .button2:active {
                transform: translateY(-1px);
                }
                table {width: 100%; border-collapse: collapse;}
                table td {padding: 12px 16px;}
                table thead tr {font-weight: bold; border-top: 1px solid #e8e9eb;}
                table tr {border-bottom: 1px solid #e8e9eb;}
                table tbody tr:hover {background: #e8f6ff;}
                .clear {
                clear: both;
                }

                .checkBox {
                display: block;
                cursor: pointer;
                width: 10px;
                height: 10px;
                border: 3px solid rgba(255, 255, 255, 0);
                border-radius: 4px;
                position: relative;
                overflow: hidden;
                box-shadow: 0px 0px 0px 2px #050505;
                }

                .checkBox div {
                width: 60px;
                height: 60px;
                background-color: #030303;
                top: -52px;
                left: -52px;
                position: absolute;
                transform: rotateZ(45deg);
                z-index: 100;
                }

                .checkBox input[type=checkbox]:checked + div {
                left: -10px;
                top: -10px;
                }

                .checkBox input[type=checkbox] {
                position: absolute;
                left: 50px;
                visibility: hidden;
                }

                .transition {
                transition: 300ms ease;
                }
            </style>
              <script type="text/javascript" charset="utf-8">
                    function httpPostAsync(method, params, callback) {
                        var xmlHttp = new XMLHttpRequest();
                        xmlHttp.onreadystatechange = function() { 
                            if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
                                callback(xmlHttp.responseText);
                            else
                                callback(`Error ${xmlHttp.status}`)
                        }
                        xmlHttp.open("POST", window.location.href + method, true);
                        xmlHttp.setRequestHeader("Content-Type", "application/json");
                        xmlHttp.send(params);
                    }
                    
                    function ledOn() {
                        document.getElementById("textstatus").textContent = "Выключено";
                        httpPostAsync("led1", JSON.stringify({ "on": true }), function(resp) { 
                            document.getElementById("textstatus0").textContent = `Выключено`;
                        });
                    }

                    function ledOff() {
                        document.getElementById("textstatus").textContent = "Включено";
                        httpPostAsync("led1", JSON.stringify({ "on": false }), function(resp) { 
                            document.getElementById("textstatus").textContent = `Включено`;
                        });
                    }
                    
                    function ledOn1() {
                        document.getElementById("textstatus1").textContent = "Включено";
                        httpPostAsync("led2", JSON.stringify({ "on": true }), function(resp) { 
                            document.getElementById("textstatus1").textContent = `Выключено`;
                        });
                    }

                    function ledOff1() {
                        document.getElementById("textstatus1").textContent = "Выключено";
                        httpPostAsync("led2", JSON.stringify({ "on": false }), function(resp) { 
                            document.getElementById("textstatus1").textContent = `Включено`;
                        });
                    }
                    
                    function ledOn2() {
                        document.getElementById("textstatus2").textContent = "Включено";
                        httpPostAsync("led3", JSON.stringify({ "on": true }), function(resp) { 
                            document.getElementById("textstatus2").textContent = `Выключено`;
                        });
                    }

                    function ledOff2() {
                        document.getElementById("textstatus2").textContent = "Выключено";
                        httpPostAsync("led3", JSON.stringify({ "on": false }), function(resp) { 
                            document.getElementById("textstatus2").textContent = `Включено`;
                        });
                    }
                    function ledTime(){
                        document.getElementById("textstatus3").textContent =" ";
                        httpPostAsync("time", JSON.stringify({ "on":false }), function(resp) {
                            document.getElementById("textstatus3").textContent = ` `;
                            });
                    }
                    function alerted(){
                        var rt1 = document.getElementById("ch1");
                        if (rt1.checked){
                            ledTime();
                        }else{
                            ledOn1();
                            ledOn2();
                            ledOn();
                        } 
                     }
                    function getDate()
                    {
                    var date = new Date();
                    var hours = date.getHours();
                    var minutes = date.getMinutes();
                    var seconds = date.getSeconds();
                    if(seconds < 10)
                    {
                    seconds = '0' + seconds;
                    }
                    document.getElementById('timedisplay').innerHTML = hours + ':' + minutes + ':' + seconds;
                    }
                    setInterval(getDate, 0);
                    
                    
            </script>
              <head>
                  <meta http-equiv="content-type" content="text/html; charset=UTF-8">
                  <meta charset="utf-8">
              </head>
              <body>
                 <h2 style="text-align: center;">Управление фермой</h2>
                 <a style="margin-left: 5%; font-size: 125%;">Управление реле</a><br></br>
                 <ul class="place">
                 <h4 style="margin-left: 115px;">1-й ярус</h4>
                 <button class="button1" onclick="ledOff();">Вкл</button>
                 <button class="button2" onclick="ledOn();">Выкл</button><span id="textstatus">⠀</span>
                 <p>
                 <h4 style="margin-left: 100px;">2-й и 3-й ярус</h4>
                 <button class="button1" onclick="ledO ff1();">Вкл</button>
                 <button class="button2" onclick="ledOn1();">Выкл</button><span id="textstatus1">⠀</span>
                 <p>
                 <h4 style="margin-left: 125px;">Насос</h4>
                 <button class="button1" onclick="ledOff2();">Вкл</button>
                 <button class="button2" onclick="ledOn2();">Выкл</button><span id="textstatus2">⠀</span>
                 <p>
                 <button class="button1" onclick="ledTime();">Таймер</button>
                 <p>
                 <span id="textstatus3"></span>
                </ul>
                <h2 style="position:absolute;top: 50; left: 50%">Информация датчиков</h2>
                <p style="position:absolute;top: 150; left: 40%">Температура : {{ temper1 }}</p>
                <p style="position:absolute;top: 170; left: 40%">Влажность : {{ vlash1 }}</p>
                <div style="position: absolute; top: 600px; left: 48.5%;" id="timedisplay"></div>
              </body>
            </html>
              </body>
            </html>
'''
from http.server import BaseHTTPRequestHandler, HTTPServer

try:
    import math
    import threading
    import RPi.GPIO as GPIO
    import serial
    import time
    import struct
    import json
    import random
    import datetime
    import board
    import adafruit_dht
    import django.shortcuts 

    
except ModuleNotFoundError:
    pass

three = 26
two = 20
one = 21
pumpPinLower = 12
pumpPinUpper = 27
dhtDevice = adafruit_dht.DHT22(board.D17)
RLOAD = 10.0 
RZERO = 76.63
PARA = 116.6020682
PARB = 2.769034857
ATMOCO2 = 400
t = dhtDevice.temperature
h = dhtDevice.humidity

GPIO.setmode(GPIO.BCM)
#Setting GPIO
GPIO.setwarnings(False)
GPIO.setup(three,GPIO.OUT)
GPIO.setup(two,GPIO.OUT)
GPIO.setup(one,GPIO.OUT)
GPIO.setup(pumpPinLower,GPIO.OUT)
GPIO.setup(pumpPinUpper,GPIO.OUT)

GPIO.output(three, 1)
GPIO.output(two, 1)
GPIO.output(one, 1)

def raspberrypi_init2():
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(one, GPIO.OUT)
    except:
        pass
def raspberrypi_init1():
    try: 
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(two, GPIO.OUT)
    except:
        pass
def raspberrypi_init():
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(three, GPIO.OUT)
    except:
        pass

def rasperrypi_pinout(pin: int, value: bool):
    print("Включенно" if value else "Выключенно")
    try:
        GPIO.output(pin, value)
    except:
        pass

def rasperrypi_cleanup():
    try:
        GPIO.cleanup()
    except:
        pass


class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET request, path:", self.path)
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))
        else:
            self.send_error(404, "Page Not Found {}".format(self.path))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        try:
            print("POST request, path:", self.path, "body:", body.decode('utf-8'))
            if self.path == "/led1":
                data_dict = json.loads(body.decode('utf-8'))
                print()
                if 'on' in data_dict:
                    rasperrypi_pinout(one, data_dict['on'])
                    
            if self.path == "/led2":
                data_dict = json.loads(body.decode('utf-8'))
                if 'on' in data_dict:
                    rasperrypi_pinout(two, data_dict['on'])
                    
            if self.path == "/led3":
                data_dict = json.loads(body.decode('utf-8'))
                if 'on' in data_dict:
                    rasperrypi_pinout(three, data_dict['on'])
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b"OK")
            if self.path =="/time":
                data_dict = json.loads(body.decode('utf-8'))
                if 'on' in data_dict:
                    def timer_start():
                        t1 = threading.Timer(4.0, timer_go)
                        t1.start()
                    def timer_go():
                        GPIO.output(one, 1)
                        GPIO.output(two, 1)
                        GPIO.output(three, 1)
                    def timer_out():
                        GPIO.output(one, 0)
                        GPIO.output(two, 0)
                        GPIO.output(three, 0)
                    data123 = datetime.datetime.today().strftime("%w")
                    hours123 = datetime.datetime.today().strftime("%H:%M")
                    if data123 == "4": 
                        timer_start()
                        timer_out()
                    if data123 == "1":
                        timer_start()
                        timer_out()
            else:
                self.send_response(400, 'Bad Request: Method does not exist')
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
        except Exception as err:
            print("do_POST exception: %s" % str(err))
    
     
def server_thread(port):
    server_address = ('', port)
    httpd = HTTPServer(server_address, ServerHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

if __name__ == '__main__':

    port = 3333
    print("Стартовал сервер с портом: %d" % port)
    
def myfunc():
    server_thread(port)
thr1 = threading.Thread(target = myfunc).start()

k=struct.pack('B', 0xff)

ser = serial.Serial(port="/dev/ttyS0",baudrate =9600)


def text21(str):
    command = 't6.txt="' + str + '"'
    ser.write(command.encode())
    ser.write(k)
    ser.write(k)
    ser.write(k)
def text1(str):
    command = 't7.txt="' + str + '"'
    ser.write(command.encode())
    ser.write(k)
    ser.write(k)
    ser.write(k)
def text2(str):
    command = 't8.txt="' + str + '"'
    ser.write(command.encode())
    ser.write(k)
    ser.write(k)
    ser.write(k)
def text3(str):
    command = 't9.txt="' + str + '"'
    ser.write(command.encode())
    ser.write(k)
    ser.write(k)
    ser.write(k)

#status tombol
global tombol1_sts
global tombol2_sts
global tombol3_sts

tombol1_sts=False
tombol2_sts=False
tombol3_sts=False

time.sleep(1)

print("Ферма готова к работе!")

def pump():
    pumpStart = threading.Timer(1.0,doPump)
    pumpStart.start()
def doPump():
    if GPIO.input(pumpPinLower) and GPIO.input(pumpPinUpper):
        print('Воды нет')
    elif not GPIO.input(pumpPinLower) and not GPIO.input(pumpPinUpper):
        print('Воды достаточно')
    elif not GPIO.input(pumpPinLower):
        print('Воды мало')
    pump()
def temp1():
    temp2 = threading.Timer(1.0 , tempgo)
    temp2.start()
def tempgo():
    temp1()
    while True:
        try:
            temperature_c = dhtDevice.temperature
            humidity = dhtDevice.humidity
            time.sleep(2)
            text21(("{} C ".format(temperature_c)))
            text1(("{} % ".format(humidity)))
            break    
        except RuntimeError as error:
            print(error.args[0])
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error
temp1()
def ras1():
    ras2=threading.Timer(5.0,getResistance)
    ras2.start()
def getResistance():
    ras1()
    return ((1023./69) - 1.)*RLOAD
def ras3():
    ras4=threading.Timer(5.0,getPPM)
    ras4.start()
    
def getPPM():
    ras3()
    return PARA * math.pow((getResistance()/RZERO),+h/t)
    

def map():
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def co21():
    timerk=threading.Timer(1.0,co2)
    timerk.start()

def co2():
    ras3()
    ras1()
    co21()
    while True:
        try:
            ppm = getPPM()
            text2("{} ppm".format(round((ppm))))
            break    
        except RuntimeError as error:
            print(error.args[0])
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error   
co21()
while True:
    received_data = ser.read()              #read serial port
    time.sleep(0.03)
    data_left = ser.inWaiting()             #check for remaining byte
    received_data += ser.read(data_left)
    #print(received_data) #print received data
    ser.write(received_data)    
    try:
        output = received_data
        if output:
            if output == b'rele2\r':
                print("Не найден №1")
                if tombol1_sts==False:
                    print("Реле №1 включено")
                    #turn on relay1
                    GPIO.output(two, 0)
                    tombol1_sts = True
                else:
                    GPIO.output(two, 1)
                    print("Реле №1 выключено")
                    tombol1_sts = False
                    
            if output == b'rele3\r':
                print("Не найден №2")
                if tombol2_sts==False:
                    print("Реле №2 включено")
                    #turn on relay2
                    GPIO.output(one, 0)
                    tombol2_sts = True
                else:
                    GPIO.output(one, 1)
                    print("Реле №2 выключено")
                    tombol2_sts = False
            
            if output == b'rele1\r':
                print("Не найден №3")
                if tombol3_sts==False:
                    print("Реле №3 включено")
                    #turn on relay3
                    GPIO.output(three, 0)
                    tombol3_sts = True
                else:
                    GPIO.output(three, 1)
                    print("Реле №3 выключено")
                    tombol3_sts = False
            if output == b'off\x0b':
                    GPIO.output(one, 1)
                    GPIO.output(two, 1)
                    GPIO.output(three, 1)
                    print("Все реле выключены")
                    tombol1_sts = False
                    tombol2_sts = False
                    tombol3_sts = False
            if output == b'time1\r':
                print("Таймер включён")
                GPIO.output(one,0)
                time.sleep(3)
                GPIO.output(one,1)
                print("Таймер выключён")
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
        pass

 