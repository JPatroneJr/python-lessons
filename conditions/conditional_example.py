# py age_example.py
'''

Conditionals-
Computers do what you tell them to do and when. So how do we tell them?
Conditionals, also referred to as Control Flow, and most often called 'ifs'
let us control where we point the program to go.
we do this with If, Else, and Else If.
In python these are typed as,
  if, elif, else
  
  
-----------------------------------------------------------
Indentation-  
Many languages use sometimes complicated/confusing ways to tell lines apart. 
Python uses indentation to make these more distinct. 
This can be one of the harder things to get a handle on.

In the case of 'ifs' the conditional line will end with a colon and the next line will be indented.
every line at that level of indentation applies to that conditional line

upon returning to the original indentation level the if statement has been exited



if age >= 30:
  print('Ok Boomer')
else:
  print('youre not my mom')

'youre not my mom' WILL ONLY PRINT if age is less than 30 
and vice versa for 'Ok Boomer'
--------------------------------------
Basic Conditional Operators
==  Equal to
!=  Not equal to
>  Greater than
<  Less than
>=   Greater than or equal to
<=   Less than or equal to
'''

name = 'Arthur'
age = 28

# you can think of the print statements as ad-libs for fun
print(f'Hi, My name is {name}')
print(f'I am {age} which means...')

if age >= 18:
  print('I can vote')
else:
  print('I cannot vote')
  
print('and')

if age >= 21:
  print('I can consume alcohol')
else:
  print('I cannot consume alcohol')
  
  
# QUIZ
'''
In the if statements above the numbers 18 and 21 can also be variables.
What if in a different country the drinking age was 18 and the voting age was 25?
Format this to use variables instead in age_example_quiz.py
'''