from sty import fg, bg, rs

import input_taker

def calculator(prev_val = 0):
    val_1 = input_taker.input_taker(1, prev_val)
    val_2 = input_taker.input_taker(2)
    operation = input_taker.operation_selector()
    output =  operation(val_1, val_2)

    confirmation = 'The Output is {}'.format(output)

    print(bg.blue + fg.white + confirmation + fg.white + bg.rs)

    should_countinue = input('Shall we keep going? (Y/n) :')
    should_countinue = 'y' if should_countinue == '' else should_countinue

    if(should_countinue == 'y' or should_countinue == 'Y'):
        calculator(int(output))


calculator()

# keep the last result alive for next calculation
# clear prvious output

