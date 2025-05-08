# py for_loop_example.py
'''
for loops!

for this first example lets go grocery shopping!




The format of a for loop is incredibly helpful when understood

the format is
  for x in y:
  
in this case y is the variable that is a list

it is import to note, x can be LITERALLY ANYTHING
I suggest you use the singular noun for what is in the list

for number in numbers
for player in team
for item in grocery_list

the first variable is a variable that will change every loop
the second variable is the thing that you will loop over

'''



# grocery list
# this is a data type called 'list', we will go over it later
# for now literally think of a list

grocery_list = ['apples','pickles','apple jacks','bread','turducken']

# when grocery shopping you cant just make everything appear in front of you at once.
# we have to go get ONE thing at a time


# lets get instructions on what to get when
for item in grocery_list:
  print(f'Remember to buy {item}')