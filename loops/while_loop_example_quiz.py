
import time # lets us use things to do with time

countdown = 10

print('Launching Shuttle in ')

while countdown > 0:
  print(f'{countdown}...')
  time.sleep(1) # this 'pauses' the script for 1 second
  
  #subtract 1 from countdown
  countdown -= 1

print('BLAST OFF')


