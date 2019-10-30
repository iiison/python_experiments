from sty import fg, bg, rs

def input_taker(val_count, val = 0):
    message = 'Enter Value {}: '.format(val_count) if val == 0 else 'Enter Value {}({}): '.format(val_count, val)

    value = input(message)
    fmt_value = ''
    try:
        fmt_value = float(value) if value != '' else val
        print(fmt_value)

    except:
        print(fg.red + 'Think again, do you really think "{}" is a number?'.format(value) + fg.rs)
        fmt_value = input_taker(val_count)
        
    return fmt_value

def addition(val_1, val_2):
    return val_1 + val_2

def subtraction(val_1, val_2):
    return val_1 - val_2

def multiplication(val_1, val_2):
    return val_1 * val_2

def division(val_1, val_2):
    return val_1 / val_2

def operation_selector():
    operation = str(input('Select Operation(+, -, *, /): '))
    operation = '+' if operation == '' else operation

    operation_map = {
        '+' : addition,
        '-' : subtraction,
        '*' : multiplication,
        '/' : division
    }

    selected_operation = ''

    try :
        selected_operation = operation_map[operation]
    except : 
        print(fg.red + 'So, you are one of those who likes to try different stuff, huh?' + fg.rs)
        print(fg.red + 'I\'m not gonna get you away with this, enter the right operation'  + fg.rs)
        selected_operation = operation_selector()

    return selected_operation

