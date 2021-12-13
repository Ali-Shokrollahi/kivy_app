from time import sleep
import os
import math
from multiprocessing import Process
from speedtest import Speedtest
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty, NumericProperty

try:
    st = Speedtest()
except:
    st = None


class MyLayout(Widget):

    state = ObjectProperty(None)
    download = ObjectProperty(None)

    upload = ObjectProperty(None)

    popup = Popup(title='Test popup',
                  content=Label(
                      text='Getting Data from Server../\nPlease wait', font_size=20),
                  size_hint=(None, None), size=(300, 300))

    def btn(self):

        self.popup.open()

    def btnD(self):
        if st is None:
            self.download.text = "failed connecting to the server"
            self.upload.text = "failed connecting to the server"

        else:
            d = st.download()
            self.download.text = "Download Speed : " + \
                str(round(d/1000000, 2))+" Mb"

        self.popup.dismiss()

    def btnU(self):
        if st is None:
            self.download.text = "failed connecting to the server"
            self.upload.text = "failed connecting to the server"
        else:
            u = st.upload()
            self.upload.text = "Upload Speed : "+str(round(u/1000000, 2))+" Mb"

        self.popup.dismiss()

    def ll(self):
        self.state.text = "sdfsdf"


class myApp(App):
    def build(self):
        screen = MyLayout()

        return screen


if __name__ == '__main__':

    myApp().run()
