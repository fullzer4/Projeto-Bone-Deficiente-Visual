#def sensor()

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

global pinoTrigger = 17
global pinoEcho = 18
global GPIO.setup(pinoTrigger, GPIO.OUT)
global GPIO.setup(pinoEcho, GPIO.IN)

def sensor():
  try:
    while True:
      GPIO.output(pinoTrigger,False)
      time.sleep(1)
      GPIO.output(pinoTrigger,True)
      time.sleep(0.0001)
      GPIO.output(pinoTrigger,False)
      tempoI = time.time()
      while GPIO.input(pinoecho)==0:
        tempoI = time.time()
        while GPIO.input(pinoecho)==1:
          tempoF = time.time()
    
  tempocorrido = tempoF - tempoI
  distancia = (tempocorrido)/2 * 34326 

  print("Distancia: ",distancia)
  return(distancia)
  time.sleep(0.5)

while True:
  if sensor() < 80:
    GPIO.output(buzina,True)
    time.sleep(30)
    GPIO.output(buzina,False)
