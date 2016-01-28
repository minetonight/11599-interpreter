#-*-coding:utf8;-*-
#qpy:2
#qpy:kivy

from kivy.app import App
# from kivy.uix.button import Button

class NumerologyApp(App):
    
    def on_pause(self):
        # when you are going on pause, don't forget to stop using resources 
        return True

    def on_resume(self):
        # reactivate when you are back to the app
        pass


NumerologyApp().run()

