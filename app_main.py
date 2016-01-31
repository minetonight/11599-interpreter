#-*-coding:utf8;-*-
#qpy:2
#qpy:kivy

from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.button import Button

from numerology import CardCalculator
from interpreter import CardInterpreter

from meaningHelper import archiveReading, getMeaning

class GridButton(Button):
   controller = None


class Controller(BoxLayout):
    
    debug = False
    #debug = True
    
    t_name = ObjectProperty() 
    g_type = StringProperty() 
    t_date = ObjectProperty()
    
    
    def on_archive(self):
        #populate form
        self.t_name.text = "Username" 
        self.t_date.text = "xxyyzzzz" 
        self.g_type = 'event' 
        
        
    def on_loadArchive(self):
        pass 
        
        
    def gridButtonPress(self, btn):
        # getMeaning       
        #print(NumbersInterpreter.getDateInterpretation(self.calculator.personalDate)) 
        #print(NumbersInterpreter.getPersonalNumberInterpretation(self.calculator.personalNumberSimplified)) 

        cardReader = CardInterpreter(self.calculator.card)
        
        
        print("grid Button press")
        print("btn is " + str(btn.name) )
        self.ids[btn.name].text += '1'
        #self.ids["GB2"].text = "PUSH"
    
    
    def gridButtonRelease(self, btn):
        pass
    
    
    def processInput(self):
        #read form
        print("name was %s") % (self.t_name.text) 
        print("date was %s") % (self.t_date.text) 
        print("type was %s") % (self.g_type)
        
        #read form
        name = self.t_name.text.strip() 
        birthday = self.t_date.text.strip()
        g_type = self.g_type
        
        if len(birthday) == 8:
            self.calculator = CardCalculator(birthday)

            self.updateWidgets()

            # log reading
            cardReader = CardInterpreter(self.calculator.card)
            cardReader.getFullInterpretation()

            archiveReading()
    
    
    
    def updateWidgets(self): 
        calc = self.calculator 
        
        #labelStr = '21111985 = 28 = 10\n                       -2\n                      26 = 8'
        labelStr = '%s = %s = %s\n                       %s\n                      %s = %s'
        
        self.ids['date_number'].text = str(calc.personalDate) 
        self.ids["cardStr_label"].text = labelStr % (calc.birthday, calc.personalNumber, calc.personalNumberSimplified, calc.adjustment, calc.adjusted, calc.adjustedSimple, ) 
        self.ids["personal_number"].text = str(calc.personalNumberSimplified) 
        
        self.ids["zero"].text = "0" * calc.card[0]
        
        self.ids["one"].text = "1" * calc.card[1]
        self.ids["two"].text = "2" * calc.card[2]
        self.ids["three"].text = "3" * calc.card[3]
        
        self.ids["four"].text = "4" * calc.card[4]
        self.ids["five"].text = "5" * calc.card[5]
        self.ids["six"].text = "6" * calc.card[6]
        
        self.ids["seven"].text = "7" * calc.card[7]
        self.ids["eight"].text = "8" * calc.card[8]
        self.ids["nine"].text = "9" * calc.card[9]
        
        
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

