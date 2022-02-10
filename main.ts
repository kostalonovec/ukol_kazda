pins.touchSetMode(TouchTarget.P1, TouchTargetMode.Capacitive)
pins.touchSetMode(TouchTarget.P2, TouchTargetMode.Capacitive)
let is_pin1 = input.pinIsPressed(TouchPin.P1)
let is_pin2 = input.pinIsPressed(TouchPin.P2)
let hrac1 = false
let hrac2 = false
let podvodnik1 = false
let podvodnik2 = false
let zahajeni = false
// mezery slouží pro větší přehlednost
// první tlačítko
input.onPinPressed(TouchPin.P1, function on_pin_pressed_p1() {
    
    hrac1 = true
})
// druhý tlačítko
input.onPinPressed(TouchPin.P2, function on_pin_pressed_p2() {
    
    hrac2 = true
})
forever(function on_forever() {
    
    if (zahajeni == false && hrac1) {
        podvodnik1 = true
    } else if (zahajeni == false && hrac2) {
        podvodnik2 = true
    } else if (hrac1 && hrac2 && zahajeni) {
        basic.showString("R")
        basic.pause(3000)
        control.reset()
    } else if (hrac1 && zahajeni) {
        basic.showNumber(1)
        basic.pause(3000)
        control.reset()
    } else if (hrac2 && zahajeni) {
        basic.showNumber(2)
        basic.pause(3000)
        control.reset()
    }
    
})
control.inBackground(function vyhodnoceni() {
    
    let time = randint(3000, 10000)
    basic.pause(time)
    if (podvodnik1 == false && podvodnik1 == false) {
        basic.showLeds(`
            # # # # #
            # . . . .
            # # # # #
            . . . . #
            # # # # #
            `)
        music.playTone(Note.C, music.beat(1500))
        zahajeni = true
    }
    
    if (podvodnik1 && podvodnik2) {
        basic.showString("C")
        basic.pause(3000)
        control.reset()
    } else if (podvodnik2) {
        basic.showString("A")
        basic.pause(3000)
        control.reset()
    } else if (podvodnik1) {
        basic.showString("B")
        basic.pause(3000)
        control.reset()
    }
    
})
