'''
The two import things to know about indexing are
- each 'item' in a list is assigned a number
- THEY ALWAYS START AT 0
'''

grocery_list = ['apples','pickles','apple jacks','bread','turducken']

for idx in range(len(grocery_list)):
  print(f'{str(idx)} - {grocery_list[idx]}')

  

'''
lets break this down

len(grocery_list)
the length of grocery list is 5 because there are 5 of it

then we have range(len(grocery_list))
the pythonic range of 5 is 0-4 - 0,1,2,3,4

so calling the name of the list and the numeric index of the item 
grocery_list[0] will return 'apples'
'''