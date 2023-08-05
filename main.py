from microbit import *
import utime

# Count presses
def read_operation():
    start = utime.ticks_ms()
    global presses
    global operation_accepted
    presses = 1

    # If the time between presses is greater than 600ms, return
    while utime.ticks_diff(utime.ticks_ms(), start) < 600:
        if button_a.was_pressed():
            start = utime.ticks_ms()
            presses = presses + 1

    if presses >= 1 and presses <= 4:
        operation_accepted = 1
    else:
        display.scroll("Invalid operation")

# Main
while True:
    presses = -1
    operation_accepted = 0

    display.show(Image.ARROW_W)

    while not operation_accepted:
        if button_a.was_pressed():
            read_operation()

    sleep(300)

