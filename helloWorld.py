from math import pi
# import math.pi as pie
# import math

import input_method

string_var = "20"

print("Yo YO! " + string_var)
print(type(string_var))

# string_var = str(90)
string_var = 90
print type(string_var)
# print "Say man! this is the number value " + str(string_var)

str_ = "honey singh mera bhai hai!"
# print str_[3:10]

another = 232
formatted = 'some shit {}, and then some more {}'.format(string_var, str_)

# observe that %s converts digit to string, basically, str() fxn
formattedOld = "some shit %s, and then some more %s" % (string_var, another)
print formatted
print formattedOld

# In operator:
print "H" in str_
print "Q" not in str_


triple = """BC Gazab
LE BC or Gazab \t(tab) or je to BC matlab next he level"""
print triple

# String methods
print str_.capitalize()
print str_

print str_.count('h', 5, len(str_))
print str_.endswith('h', 5, len(str_))

print str_.startswith('h')
# Slice the string and then check if string starts with 'h'
print str_.startswith('h', 5, len(str_))

print str_.find('h', 3, 20)


print "AGB32".isalnum() # NO SPACES
print " AGB32".isalnum() # NO SPACES

print "AGB32".isalpha() # NO SPACES
print " AGB32".isalpha() # NO SPACES
print "AGB".isalpha() # NO SPACES

# Lists
ls = [3, 2, 'yep!']
print ls
print len(ls)

ls[1] = 'yeah!'
# ls[3] = 32 # throws error out of range

print ls
print ls[1:35]

for i in ls:
    print i # MIND THE INDENTATION

if 3 in ls:
    print "Found 3 in list"

copy_ls = ls

# List methods
ls.append('okay.')
print ls

ls.insert(2, 'custom')
print ls

ls.extend([1, 2, 3])
print ls

ls.append([1, 2, 3])
print ls

ls.extend([1, 2, 3])
ls.remove(1)
print ls

ls.pop(ls.index('custom'))
print ls

print "OMG, list are saved as references!"
print copy_ls

# Tuples
tup = (1, 2, 3)
tup2 = (3, 2, 1)
print tup

list_to_tuple = tuple(ls)
print ls # ls is still a list
print list_to_tuple

print tup + tup2

# Dictionaly - Objects
dic = {
    "val" : 1,
    "val2" : 23
}
print dic

dic = {
    "val" : 1,
    "val2" : 23
    # "val" : 11, = Syntax Error
}
# print dic

print pi

print(input_method.name_teller())

