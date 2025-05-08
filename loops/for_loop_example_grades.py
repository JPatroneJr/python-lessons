# lets assume a teacher applies a curve on the grade
# we start out with a list of grades that all the students got on the test

list_of_grades = [54,65,77,81,90,52,64,12,56]

# lets print out all their grades before the curve
print('original grades...')
for grade in list_of_grades:
  print(grade)


# the curve came out to giving everyone an extra ten points. 
# lets use a for to apply the curve
curve = 10

# index is sometimes shortened as idx
for idx in list_of_grades:
  grade += curve

# This has manipulated the list_of_grades variable assigned in line 4

# lets see what the new grades are
print('new grades...')
for grade in list_of_grades:
  print(grade)
  