#-*-coding:utf8;-*-
#qpy:2
#qpy:kivy
from platform import platform

from kivy.core.window import Window
from kivy.core.clipboard import Clipboard
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.button import Button
from random import randint as rint
from os.path import join, dirname

from numerology import CardCalculator
from interpreter import CardInterpreter
from meaningHelper import archiveReading, pastebinShare

class GridButton(Button):
   controller = None


class Controller(BoxLayout):
    
    debug = False
    debug = True
    
    t_name = ObjectProperty() 
    g_type = StringProperty() 
    popupText = StringProperty()
    popup = ObjectProperty()
    filePopup  = ObjectProperty()
    t_date = ObjectProperty()
    
    def on_archive(self):
        curdir = dirname(__file__)
        filename = join(curdir, "archives") 
        	
        self.filePopup.filechooser.rootpath = filename
        self.filePopup.open()
        
        
    def loadArchive(self, filename ):
        #populate form
        if self.debug:
            print filename
            
        self.t_name.text = str(filename) 
        self.t_date.text = str(filename) 
        self.g_type = 'date' 
        
        
        
    def gridButtonPress(self, btn):
        
        if self.debug:
            print("grid Button press")
            print("btn is " + str(btn.name) )
        
        if btn.name == 'full_meaning':
            meaning = self.fullInfo 
        else:
            meaning = self.cardReader.getMeaning(btn.name)
        
        self.popupText = meaning
        self.popup.title = "Значение за " + str(btn.name)
        self.popup.open()
    
    
    def gridButtonRelease(self, btn):
        pass
    
    
    def share(self):
        #read form
        name = self.t_name.text.strip() 
        birthday = self.t_date.text.strip()
        g_type = self.g_type
        
        url = pastebinShare(g_type, birthday, name, self.fullInfo)
        t = self.ids["t_share"]
        t.text = url
        Clipboard.copy(url)
        #t.select_all()
        #t.copy() 
    
    def processInput(self):
        #read form
        if self.debug:
            print("name was %s") % (self.t_name.text) 
            print("date was %s") % (self.t_date.text) 
            print("type was %s") % (self.g_type)
            
            if self.g_type == '':
                self.g_type = "date" 
            
        #read form
        name = self.t_name.text.strip() 
        birthday = self.t_date.text.strip()
        g_type = self.g_type
        
        if len(birthday) == 8:
            calculator = CardCalculator(birthday)

            self.updateWidgets(calculator)

            # log reading
            self.cardReader = CardInterpreter(calculator, g_type)
            self.fullInfo = self.cardReader.getFullInterpretation()
            
            archiveReading(g_type, birthday, name, self.fullInfo)
        
        if self.debug:
            self.t_date.text = "%02d%02d%s" % (rint(1, 28), rint(1, 12), rint(1950, 2020))
                    
    
    def updateWidgets(self, calc): 
        
        #labelStr = '21111985 = 28 = 10\n                       -2\n                      26 = 8'
        labelStr = '%s = %s = %s\n                       %s\n                      %s = %s'
        
        self.ids['date_number'].text = str(calc.personalDate) 
        self.ids["cardStr_label"].text = labelStr % (calc.birthday, calc.personalNumber, calc.personalNumberSimplified, calc.adjustment, calc.adjusted, calc.adjustedSimple, ) 
        self.ids["personal_number"].text = str(calc.personalNumberSimplified) 
        
        self.ids["0"].text = "0" * calc.card[0]
        
        self.ids["1"].text = "1" * calc.card[1]
        self.ids["2"].text = "2" * calc.card[2]
        self.ids["3"].text = "3" * calc.card[3]
        
        self.ids["4"].text = "4" * calc.card[4]
        self.ids["5"].text = "5" * calc.card[5]
        self.ids["6"].text = "6" * calc.card[6]
        
        self.ids["7"].text = "7" * calc.card[7]
        self.ids["8"].text = "8" * calc.card[8]
        self.ids["9"].text = "9" * calc.card[9]
        
        
        self.ids["t_share"].text = '' 
#eof class


class NumerologyApp(App):
    
    def build(self):
        self.bind(on_start = self.post_build_init)
    
        controller = Controller()
        GridButton.controller = controller
        self.controller = controller 
        return controller
    
    
    def post_build_init(self, *args):
        
        #pstr = platform() 
        #if pstr == 'android':
        if True:
            import android
            android.map_key(android.KEYCODE_MENU, 1000)
            android.map_key(android.KEYCODE_BACK, 1001)
            #android.map_key(android.KEYCODE_HOME, 1002)
            #android.map_key(android.KEYCODE_SEARCH, 1003)
        
        Window.bind(on_keyboard=self.hook_keyboard)
        
        
    def on_pause(self):
        # when you are going on pause, don't forget to stop using resources 
        return True

    def on_resume(self):
        # reactivate when you are back to the app
        pass
    
    def hook_keyboard(self, window, key, *largs):
        screen = self.controller.ids.sm.current
        if key in [27, 1001] : # BACK
            if self.controller.debug:
                print(screen) 
                print "popup state" 
                print( self.controller.popup.isOpen ) 
            
            if self.controller.popup.isOpen:
                self.controller.popup.dismiss()
            elif screen == 'cardScreen':
                sm = self.controller.ids.sm
                sm.transition.direction = 'right'
                sm.current = 'dataInputScreen' 
            else:
                self.stop() 
                
        elif key == 1000: # menu, open archives, share via pasteBin
            if screen == 'dataInputScreen':
                self.controller.on_archive()
            elif screen == 'cardScreen':
                pass
                # TODO
                # pastebin dev key 8fa8dc71c640f0159758990f8e3ab5e6
                # via twitter login
        
        else:
            pass
            

NumerologyApp().run()