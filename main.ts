radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    
    env2 = randint(1, 6)
    basic.showNumber(env2)
    if (env2 > env) {
        basic.showIcon(IconNames.Happy)
    } else {
        basic.showIcon(IconNames.Sad)
    }
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    env = randint(1, 6)
    basic.showNumber(env)
    radio.sendNumber(env)
})
let env = 0
let env2 = 0
radio.setGroup(1)
basic.forever(function on_forever() {
    
})
