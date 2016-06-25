# File name: layouts.py
import kivy
kivy.require('1.9.2')
import time
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

from hardware import conveyor

class MyGridLayout(GridLayout):
    message = ObjectProperty(None)

    def cb_msg_bit1(self):
        self.message.text = 'conveyor fwd event callback'
        conveyor.fwd()
    def cb_msg_bit2(self):
        self.message.text = 'conveyor rev event callback'
        conveyor.rev()
    def cb_msg_bit3(self):
        self.message.text = 'conveyor stop event callback'
        conveyor.stop()
    def cb_msg_bit4(self):
        self.message.text = 'conveyor reset event callback'
        conveyor.reset()
    def cb_msg_bit5(self):
        self.message.text = 'conveyor index event callback'
    def cb_msg_bit6(self):
        self.message.text = 'bit 6 event callback'
    def cb_msg_bit7(self):
        self.message.text = 'bit 7 event callback'
    def cb_msg_bit8(self):
        self.message.text = 'bit 8 event callback'
    def cb_msg_bit9(self):
        self.message.text = 'bit 9 event callback'
    def cb_msg_bit10(self):
        self.message.text = 'bit 10 event callback'
    def cb_msg_bit11(self):
        self.message.text = 'bit 11 event callback'
    def cb_msg_bit12(self):
        self.message.text = 'bit 12 event callback'
    def cb_msg_bit13(self):
        self.message.text = 'bit 13 event callback'
    def cb_msg_bit14(self):
        self.message.text = 'bit 14 event callback'
    def cb_msg_bit15(self):
        self.message.text = 'bit 15 event callback'
    def cb_msg_bit16(self):
        self.message.text = 'bit 16 event callback'

class MainApp(App):

    def build(self):
        return MyGridLayout()

if __name__=="__main__":
    x=True
    y=True
    # dt means delta-time
    def my_timer1(dt):
        global x
        x^=True
        if x:
            print "tick"
        else:
            print "tock"

    def my_timer2(dt):
        global y
        y^=True
        if y:
            print "on"
        else:
            print "off"



    # call my_callback every 4 seconds
    Clock.schedule_interval(my_timer1, .5)
    Clock.schedule_interval(my_timer2, 2)

    try:
        conveyor.init()

        MainApp().run()
    finally:
        conveyor.cleanup()