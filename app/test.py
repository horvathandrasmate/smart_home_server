import RPi.GPIO as GPIO 
from time import sleep 
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 
a=15
b=14
c=23
d=24
e=25
f=16
g=20
h=21
i=2
j=3
k=17
l=27
m=22
n=6
o=5
p=26

num = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p]

for i in num:
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, False) 
    sleep(2) 
    GPIO.output(i, True)

import RPi.GPIO as GPIO 
from time import sleep 
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 

GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while True:
    print(GPIO.input(12))