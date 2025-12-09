def on_received_number(receivedNumber):
    global env2
    env2 = randint(1, 6)
    basic.show_number(env2)
    if env2 > env:
        basic.show_icon(IconNames.HAPPY)
    else:
        basic.show_icon(IconNames.SAD)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global env
    env = randint(1, 6)
    basic.show_number(env)
    radio.send_number(env)
input.on_button_pressed(Button.A, on_button_pressed_a)

env = 0
env2 = 0
radio.set_group(1)

def on_forever():
    pass
basic.forever(on_forever)
