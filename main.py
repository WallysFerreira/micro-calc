from microbit import *
import utime

# Count presses
def read_operation():
    start = utime.ticks_ms()
    global presses
    global operation_accepted
    presses = 1

    # If the time between presses is greater than 600ms, stop reading
    while utime.ticks_diff(utime.ticks_ms(), start) < 600:
        if button_a.was_pressed():
            start = utime.ticks_ms()
            presses += 1

    if presses >= 1 and presses <= 4:
        operation_accepted = 1
    else:
        display.scroll("Invalid operation")

    return presses

# Read 4-bit operators bit by bit from right to left
def read_operators():
    op = 0b1000

    display.clear()

    for count in range(3, -1, -1):
        pressed = False
        str = ""

        # Show which bit is going to be read
        for bit_idx in range(1, 5):
            if bit_idx == count + 1:
                str += "x"
            elif bit_idx > count:
                str = "{}{}".format(str, (op >> (4 - bit_idx) & 1))
            else:
                str += "0"

        display.scroll(str)

        # Read that bit
        while (not pressed):
            display.scroll("...")
            if button_a.was_pressed():
                op = op & ~(1 << (3 - count))
                pressed = True
            elif button_b.was_pressed():
                op = op | (1 << (3 - count))
                pressed = True

    return op

def calculate(op1, op2, operation):
    if operation == 1:
        return op1 + op2
    elif operation == 2:
        return op1 - op2
    elif operation == 3:
        return op1 * op2
    elif operation == 4:
        return op1 / op2


# Main
while True:
    operation_symbol = ["+", "-", "*", "/"]
    presses = -1
    operation_accepted = 0

    display.show(Image.ARROW_W)

    while not operation_accepted:
        if button_a.was_pressed():
            operation = read_operation()

    op1 = read_operators()
    op2 = read_operators()

    display.scroll("{} {} {}".format(op1, operation_symbol[operation - 1], op2))

    start = utime.ticks_ms()
    # Show result for 2 seconds
    while utime.ticks_diff(utime.ticks_ms(), start) < 2000:
        display.show(str(calculate(op1, op2, operation)))

    sleep(300)

