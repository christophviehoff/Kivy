import RPi.GPIO as GPIO
from kivy.clock import Clock

timer1=True


def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT, initial=True)
    GPIO.setup(19, GPIO.OUT, initial=True)
    GPIO.setup(20, GPIO.OUT, initial=True)


def red():
    GPIO.output(18,False)
    GPIO.output(19,True)
    GPIO.output(20,True)

def green():
    GPIO.output(18,True)
    GPIO.output(19,False)
    GPIO.output(20,True)

def blue():
    GPIO.output(18,True)
    GPIO.output(19,True)
    GPIO.output(20,False)

def white():
    GPIO.output(18,False)
    GPIO.output(19,False)
    GPIO.output(20,False)

def yellow():
    GPIO.output(18,False)
    GPIO.output(19,False)
    GPIO.output(20,True)

def set(rgb):
    GPIO.output(18,int(rgb[0]))
    GPIO.output(19,int(rgb[1]))
    GPIO.output(20,int(rgb[2]))

def reset():
    GPIO.output(18,True)
    GPIO.output(19,True)
    GPIO.output(20,True)


def flash_red():
    def flash(dt):
        global timer1
        timer1^=True
        if timer1:
            red()
        else:
            reset()
    def flash_reset(dt):
        Clock.unschedule(blink)
        reset()

    blink=Clock.schedule_interval(flash, 0.5)
    Clock.schedule_once(flash_reset, 5)


def cleanup():
    GPIO.cleanup()

print "[GPIO %s        ] [Import      ] Importing rgb_module" %GPIO.VERSION
print "[PI VERSION %s      ] [Import      ] Importing rgb_module" %GPIO.RPI_REVISION