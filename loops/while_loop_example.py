'''
while loops are mixed with conditionals

so the loop will only execute its instructions while the condition is true
'''

import time # lets us use things to do with time

countdown = 10

print('Launching Shuttle in ')

while countdown > 0:
  print(f'{countdown}...')
  time.sleep(1) # this 'pauses' the script for 1 second
  
  #subtract 1 from countdown
  countdown -= 1

print('BLAST OFF')


# QUIZ TIME
# can you make it so that when the countdown gets to two one of the astronauts says - 'is it too late to...'?
# head over to the quiz file and have at it.