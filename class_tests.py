class MyClass:
    """A simple example class"""
    some_var = 222
    shared_var = 'I am shared bro!'
    shared_list = []

    def __init__(self, custom_value, name):
        self.some_var = custom_value
        self.name = name

    def helper(self):
        return 'help'

    def change_shared(self, val):
        self.shared_var = val

    def change_shared_list(self, val):
        self.shared_list.append(val)

print(MyClass.__doc__)

instance = MyClass(23, 'name')

instance.new_val = 29

instance2 = MyClass('soni', 'bharat')

print(instance.some_var)
print(instance2.some_var)

'''
# This will  throw error, IT'S Not JavaScript
print(instance2.new_val) 
'''

print(instance.new_val)
print(instance)

# Adding method to prototype
def new_method (self) : # This self thingy is very important for class methods. You will always have to add self as first param
    print('I am from prototype', self.some_var)

MyClass.new_method = new_method
MyClass.data = 'Soni'

instance.new_method()
instance2.new_method()

print(instance.data)
print(instance2.data)

instance.data = 32

print(instance.data)
print(instance2.data)

inst_custom_fx = instance.new_method

inst_custom_fx() # So, this is not exactly JS, the reference of this/self persists

instance.new_method = 'Ghanta'

print(instance.new_method)
print(instance2.new_method)

print('***************************************************************')

print(instance.shared_var)
instance.change_shared('New val')
print(instance.shared_var)
print(instance2.shared_var)

instance.change_shared_list('new Item')
print(instance.shared_list)
print(instance2.shared_list)

