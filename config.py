import RPi.GPIO as GPIO
import time
import os
import random
os.system('cls' if os.name == 'nt' else 'clear')

GPIO.setmode(GPIO.BCM)

GPIO.setup(7, GPIO.)
GPIO.setup(8, GPIO.OUT))
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

def parar():
  GPIO.output(7,False)
  GPIO.output(8,False)
  GPIO.output(9,False)
  GPIO.output(10,False)
def frente():
  GPIO.output(7,False)
  GPIO.output(8,True)
  GPIO.output(9,False)
  GPIO.output(10,True)
def direita():
  GPIO.output(7,False)
  GPIO.output(8,True)
  GPIO.output(9,True)
  GPIO.output(10,False)
def esquerda():
  GPIO.output(7,True)
  GPIO.output(8,False)
  GPIO.output(9,False)
  GPIO.output(10,True)

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

  print("Distancia: ",distancia)
  time.sleep(0.5)
lista = [esquerda, direita]

try:
  while True:

    if(distancia()<10):
      parar()
      tras()
      time.sleep(0.3)
      random.choice(lista)()
      time.sleep(0.3)
    else:
      frente()

  parar()