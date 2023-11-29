from kivymd.app import MDApp
from kivy.clock import Clock
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivy.lang.builder import Builder
from geeznum import GeezNumber


Window.size = (300, 500)

screen_helper = """
MDScreenManager:
    SplashScreen:

    MainScreen:

<SplashScreen>:
    _md_bg_color:(0,0,0)
    name:'splash'
    Image:
        source:'img/adwa1888.png'
        pos_hint:{'center_x':0.5, 'center_y':0.55}
        size_hint:(0.5,0.5)
        

<MainScreen>:
    name:'main'
    Image:
        source:'img/to_geez_logo.png'
        size_hint:(0.5,0.5)
        pos_hint:{'center_x':0.5, 'center_y':0.8}
    BoxLayout:
        orientation:'horizontal'
        ScrollView:
            pos_hint:{'center_x':0.5, 'center_y':0.2}
            MDLabel:
                id:answer_label
                text:''
                font_name:'fonts/nyala.ttf'
                halign:'center'
                pos_hint:{'center_x':0.5, 'center_y':0.2}
                font_size:100
                color:'#282f39'
    MDTextField:
        id:user_input
        hint_text:'Enter A Number'
        current_hint_text_color:0,0,0,1
        helper_text:'Enter numerical Value'
        helper_text_mode: 'on_focus'
        pos_hint:{'center_x':0.5, 'center_y':0.6}
        input_filter: "int"
        color_mode: 'custom'
        size_hint_x: 0.5
        on_text_validate:
            from geeznum import GeezNumber
            geez = GeezNumber() 
            answer_label.text ='Enter A Number First' if user_input.text == '' else geez.to_geez(int(user_input.text))
            answer_label.font_size = 20 if answer_label.text == 'Enter A Number First' else 50
    MDFillRoundFlatIconButton:
        icon: "rotate-left"
        pos_hint:{'center_x':0.5, 'center_y':0.4}
        text: "CONVERT"
        width: dp(280)
        on_release:
            from geeznum import GeezNumber
            geez = GeezNumber() 
            answer_label.text ='Enter A Number First' if user_input.text == '' else geez.to_geez(int(user_input.text))
            answer_label.font_size = 20 if answer_label.text == 'Enter A Number First' else 50
    
"""

class SplashScreen(MDScreen):
    def on_enter(self):
        Clock.schedule_once(self.transition_to_next_screen, 5)

    def transition_to_next_screen(self, dt):
        self.manager.transition.direction = 'left'
        self.manager.current = 'main'

class MainScreen(MDScreen):
    pass

sm = MDScreenManager()
sm.add_widget(SplashScreen(name = 'splash'))
sm.add_widget(MainScreen(name = 'main'))

class ToGeez(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        screen = Builder.load_string(screen_helper)
        return screen
    def convert(self):
        print('by')
    
if __name__ == "__main__":
    ToGeez().run()