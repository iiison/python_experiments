if 1 == 1 :
    some_var = 23

print(some_var)
print('*************************************************')

# nonlocal tests
def main_fxn() :
    par_var = 32

    def child_fx():
        test = 23
        global some_var
        some_var *= 2

        def grand_child_fx():
            nonlocal test
            test = 'new value'

            nonlocal par_var

            par_var = 322

        grand_child_fx()
        print(test)

    child_fx()
    print(some_var)

main_fxn()
print('*************************************************')
