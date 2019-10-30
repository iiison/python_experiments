def v():
    print('Yep, this shit works.')

dic = {
    'a' : 'val',
    'test' : v,
    23 : '23 as strting',
    'b' : 'some value here too'
}

print(dic.get('a'))
result = dic.get('b', 'Not available!')

print(result)

print ('---------------------------------------')

# Iteration using for loop:
for key in dic :
    print('{} <===> {}'.format(key, dic.get(key)))

print ('---------------------------------------')

all_keys = list(dic.keys()) 
length = len(all_keys)
i = 0

while ( i < length ) :
    print('{} <===> {}'.format(i, all_keys[i]))
    i += 1
print ('---------------------------------------')

for i in range(0, length) :
    print('{} --- {}'.format(i, all_keys[i]))
print ('---------------------------------------')

pritn(dic['vs'])

