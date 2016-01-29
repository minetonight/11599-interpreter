#-*-coding:utf8;-*-
#qpy:2
#qpy:kivy

from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.button import Button


class GridButton(Button):
   controller = None


class Controller(BoxLayout):
    
    t_name = ObjectProperty() 
    g_type = StringProperty() 
    t_date = ObjectProperty()
    
    
    def on_archive(self):
        #read form
        print("name was %s") % (self.t_name.text) 
        print("date was %s") % (self.t_date.text) 
        print("type was %s") % (self.g_type) 
        
        #populate form
        self.t_name.text = "Username" 
        self.t_date.text = "xxyyzzzz" 
        self.g_type = 'event' 
        
        
    def on_loadArchive(self):
        pass 
        
        
    def gridButtonPress(self, btn):
        print("grid Button press")
        print("btn is " + str(btn.name) )
        self.ids[btn.name].text += '1'
    
    
    def gridButtonRelease(self, btn):
        pass
    
    
    
#eof class



class NumerologyApp(App):
    
    def build(self):
        controller = Controller()
        GridButton.controller = controller
        return controller
    
    def on_pause(self):
        # when you are going on pause, don't forget to stop using resources 
        return True

    def on_resume(self):
        # reactivate when you are back to the app
        pass
    
    

NumerologyApp().run()

