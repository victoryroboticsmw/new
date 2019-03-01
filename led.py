led = LED(23)
button = Button(3)

button.when_pressed = led.on
button.when_released = led.off

pause()
