def on_button_pressed_a():
    global 放烟花
    放烟花 = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global 放烟花
    放烟花 = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

放烟花 = 0
放烟花 = 0
basic.show_icon(IconNames.ROLLERSKATE)

def on_forever():
    if 放烟花 == 1:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . # . .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . # . .
            . . # . .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . # . .
            . . # . .
            """)
        basic.show_leds("""
            . . . . .
            . . # . .
            . # # # .
            . . # . .
            . . # . .
            """)
        basic.show_leds("""
            . . # . .
            . # # # .
            # # # # #
            . # # # .
            . . # . .
            """)
        basic.show_leds("""
            . . . . .
            . . # . .
            . # # # .
            # # # # #
            . # # # .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . # # # .
            # # # # #
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . # . .
            . # # # .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . # . .
            """)
basic.forever(on_forever)

def on_forever2():
    if 放烟花 == 1:
        music.play_melody("G B A G C5 B A B ", 120)
basic.forever(on_forever2)
