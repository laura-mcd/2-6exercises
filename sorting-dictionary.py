#sorting exercises
#exercise 1
#sort strings
strs = ['aa', 'BB', 'zz', 'CC']
print(sorted(strs))  ## ['BB', 'CC', 'aa', 'zz'] (case sensitive)
print(sorted(strs, reverse=True))   ## ['zz', 'aa', 'CC', 'BB']

#exercise 2
#sort by itemgetter
from operator import itemgetter

# (first name, last name, score) tuples
grade = [('Freddy', 'Frank', 3), ('Anil', 'Frank', 100), ('Anil', 'Wang', 24)]
#sort by last name
sorted(grade, key=itemgetter(1,0)) # [('Anil', 'Frank', 100), ('Freddy', 'Frank', 3), ('Anil', 'Wang', 24)]
#sort by last name (reversed)
sorted(grade, key=itemgetter(0,-1)) #[('Anil', 'Wang', 24), ('Anil', 'Frank', 100), ('Freddy', 'Frank', 3)]

#exercise 3
#sort tuples
#define tuple
tuple = (1, 2, 'hi')
print(len(tuple))  ## 3
#print value 2 of tuple (3rd element)
print(tuple[2])    ## hi
#tuple[2] = 'bye'  ## NO, tuples cannot be changed
tuple = (1, 2, 'bye')  ## this works
print(tuple)  ## (1, 2, 'bye')

#dictionary exercises
#exercise 1
#build dictionary
  ## Can build up a dict by starting with the empty dict {}
  ## and storing key/value pairs into the dict like this:
  ## dict[key] = value-for-that-key
dict = {}
dict['a'] = 'alpha'
dict['g'] = 'gamma'
dict['o'] = 'omega'

print(dict) ## {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}

print(dict['a'])     ## Simple lookup, returns 'alpha'
dict['a'] = 6       ## Put new key/value into dict
'a' in dict         ## True
## print(dict['z'])                  ## Throws KeyError
if 'z' in dict: print(dict['z'])     ## Avoid KeyError
print(dict.get('z'))  ## None (instead of KeyError)

#exercise 2
#format with %
#build dictionary
h = {}
h['word'] = 'garfield'
h['count'] = 42
#dictionary = {word: 'garfield', count: 42}
s = 'I want %(count)d copies of %(word)s' % h  # %d for int, %s for string
# 'I want 42 copies of garfield'

#exercise 3
#del operator
var = 6
#delete variable 6
del var  
#define list
list = ['a', 'b', 'c', 'd']
del list[0]     ## Delete first element
del list[-2:]   ## Delete last two elements
print(list)      ## ['b']
#define dictionary
dict = {'a':1, 'b':2, 'c':3}
del dict['b']   ## Delete 'b' entry
print(dict)      ## {'a':1, 'c':3}