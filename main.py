pins.touch_set_mode(TouchTarget.P1, TouchTargetMode.CAPACITIVE)
pins.touch_set_mode(TouchTarget.P2, TouchTargetMode.CAPACITIVE)

is_pin1 = input.pin_is_pressed(TouchPin.P1)
is_pin2 = input.pin_is_pressed(TouchPin.P2)

hrac1 = False
hrac2 = False

podvodnik1 = False
podvodnik2 = False

zahajeni = False

#mezery slouží pro větší přehlednost

def on_pin_pressed_p1():
    global hrac1
    hrac1 = True
    #první tlačítko

input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)
def on_pin_pressed_p2():
    global hrac2
    hrac2 = True
    #druhý tlačítko

input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)
def on_forever():
    global zahajeni, hrac1, hrac2 ,podvodnik1, podvodnik2

    if zahajeni == False and hrac1:
        podvodnik1 = True

    if zahajeni == False and hrac2:
        podvodnik2 = True

    if hrac1 and hrac2 and zahajeni:

        basic.show_string("REMIZA")
        basic.pause(3000)
        control.reset()

    elif hrac1 and zahajeni:

        basic.show_number(1)
        basic.pause(3000)
        control.reset()
    elif hrac2 and zahajeni:

        basic.show_number(2)
        basic.pause(3000)
        control.reset()

forever(on_forever)

def na_background():

    global hrac1, hrac2, zahajeni
    time = randint(3000, 10000)
    basic.pause(time)
    basic.show_leds("""
        # # # # #
        # . . . .
        # # # # #
        . . . . #
        # # # # #
        """)
    music.play_tone(Note.C, music.beat(1500))

    if podvodnik1 and podvodnik2:
            basic.show_string("C")
            basic.pause(3000)
            control.reset()

    elif podvodnik2:
            basic.show_string("A")
            basic.pause(3000)
            control.reset()

    elif podvodnik1:
            basic.show_string("B")
            basic.pause(3000)
            control.reset()

    zahajeni = True
control.in_background(na_background)