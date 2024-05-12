input.onButtonPressed(Button.A, function () {
    basic.showNumber(input.temperature())
    datalogger.log(datalogger.createCV("temperatur", input.temperature()))
    basic.clearScreen()
})
datalogger.setColumnTitles("temperatur")
basic.forever(function () {
	
})
