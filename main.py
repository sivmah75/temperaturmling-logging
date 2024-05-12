def on_button_pressed_a():
    basic.show_number(input.temperature())
    datalogger.log(datalogger.create_cv("temperatur", input.temperature()))
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

datalogger.set_column_titles("temperatur")

def on_forever():
    pass
basic.forever(on_forever)
