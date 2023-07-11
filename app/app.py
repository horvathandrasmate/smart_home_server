from flask import Flask
app = Flask(__name__)
import RPi.GPIO as GPIO 

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 

GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


@app.route('/')
def hello():
	return GPIO.input(12)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)
