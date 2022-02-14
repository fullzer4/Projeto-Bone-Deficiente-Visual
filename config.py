import RPi.GPIO as GPIO
import time
import os
import random
os.system('cls' if os.name == 'nt' else 'clear')

GPIO.setmode(GPIO.BCM)
pinoTrigger = 17
pinoEcho = 18

GPIO.setup(pinoTrigger, GPIO.OUT)
GPIO.setup(pinoEcho, GPIO.IN)

def sensor():
  try:
    while True:
      GPIO.output(pinoTrigger,False)
      time.sleep(1)
      GPIO.output(pinoTrigger,True)
      time.sleep(0.000001)
      GPIO.output(pinoTrigger,False)
      tempoI = time.time()
      while GPIO.input(pinoecho)==0:
        tempoI = time.time()
      while GPIO.input(pinoecho)==1:
        tempoF = time.time()
    
  tempocorrido = tempoF - tempoI
  distancia = (tempocorrido)/2 * 34326 
  return distancia
