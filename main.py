from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.pickers import MDDatePicker
import database
from datetime import datetime
from kivymd.uix.selectioncontrol import MDCheckbox
from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivy.uix.scrollview import ScrollView


from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock

class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create a BoxLayout to hold the background image and other widgets
        layout = BoxLayout(orientation='vertical')

        # Add the background image
        background_image = Image(source=r'C:\Users\SHUBHAM NEGI\Pictures\Saved Pictures\Wallpapers\wall18.jpg', allow_stretch=True)
        layout.add_widget(background_image)

        # Add your other widgets on top of the background
        label = MDLabel(text='My App Splash Screen', halign='center', theme_text_color='Secondary', font_style='H4')
        layout.add_widget(label)

        self.add_widget(layout)

        Clock.schedule_once(self.goto_main_screen, 3)

    def goto_main_screen(self, dt):
        self.manager.current = 'main'




class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = MDLabel(text='This is the Main Screen', halign='center', font_style='H4')
        layout.add_widget(label)

        button1 = MDRaisedButton(text='Screen 1', on_release=self.goto_screen1)
        button2 = MDRaisedButton(text='Screen 2', on_release=self.goto_screen2)
        button3 = MDRaisedButton(text='Screen 3', on_release=self.goto_screen3)

        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)

        self.add_widget(layout)

    def goto_screen1(self, instance):
        self.manager.current = 'screen1'
    
    def goto_screen2(self, instance):
        self.manager.current = 'screen2'
    
    def goto_screen3(self, instance):
        self.manager.current = 'screen3'


class Screen1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.username_input = MDTextField(hint_text='Name')
        self.university_roll_no = MDTextField(hint_text='University Roll No')
        self.phoneNo_input = MDTextField(hint_text='Phone No')
        self.emailId_input = MDTextField(hint_text='Email Id')
        self.raised_button = Button(text='Choose Age', background_normal='', background_color=(0.2, 0.6, 1, 1))
        self.raised_button.bind(on_press=self.open_popup)
        self.result_label = MDLabel(
            text="",
            theme_text_color="Primary",
            font_style="Body1"
        )

        self.register_button = Button(text='Register', size_hint=(None, None))
        self.register_button.bind(on_press=self.register)


        layout.add_widget(self.username_input)
        layout.add_widget(self.university_roll_no)
        layout.add_widget(self.phoneNo_input)
        layout.add_widget(self.emailId_input)
        layout.add_widget(self.result_label)
        layout.add_widget(self.register_button)
        layout.add_widget(self.raised_button)

        back_button = MDRaisedButton(text='Back to Main Screen', on_release=self.goto_main_screen)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def open_popup(self, instance):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save)
        date_dialog.open()
    
    def on_save(self, instance, value, date_range):
        birth_year = value.year
        today_year = datetime.today().year
        print(birth_year,today_year)
        age = today_year - birth_year
        self.result_label.text = f"{age}"

    def register(self, instance):
        data = {
            'name': self.username_input.text,
            'university_no': self.university_roll_no.text,
            'email': self.emailId_input.text,
            'age': int(self.result_label.text),
            'phone_no': self.phoneNo_input.text
        }
        
        database.dbms_enter(data)

    def goto_main_screen(self, instance):
        self.manager.current = 'main'


class Screen2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        
        self.university_roll_no = MDTextField(hint_text='University Roll No')

        self.StudentName = MDLabel(
            text="",
            theme_text_color="Primary",
            font_style="Body1"
        )
        self.Id = MDLabel(
            text="",
            theme_text_color="Primary",
            font_style="Body1"
        )
        self.emial = MDLabel(
            text="",
            theme_text_color="Primary",
            font_style="Body1"
        )
        self.age = MDLabel(
            text="",
            theme_text_color="Primary",
            font_style="Body1"
        )
        self.number = MDLabel(
            text="",
            theme_text_color="Primary",
            font_style="Body1"
        )

        self.raised_button = Button(text='Get Detail', background_normal='', background_color=(0.2, 0.6, 1, 1))
        self.raised_button.bind(on_press=self.open_popup)

        self.back_button = MDRaisedButton(text='Back to Main Screen', on_release=self.goto_main_screen)
        

        layout.add_widget(self.university_roll_no)
        layout.add_widget(self.StudentName)
        layout.add_widget(self.Id)
        layout.add_widget(self.emial)
        layout.add_widget(self.age)
        layout.add_widget(self.raised_button)
        layout.add_widget(self.back_button)

        self.add_widget(layout)

    def open_popup(self, instance):
        print("addSense")
        recieve=database.dbms_out(self.university_roll_no.text)

        
        self.StudentName.text=recieve[0]
        self.Id.text=recieve[1]
        self.emial.text=recieve[2]
        self.age.text=str(recieve[3])
        self.number.text=recieve[4]

    def goto_main_screen(self, instance):
        self.manager.current = 'main'


class Screen3(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = MDBoxLayout(orientation="vertical")
        
        scroll_view = ScrollView()  # To make sure all content is visible if there are many checkboxes
        
        grid_layout = MDGridLayout(cols=1, row_force_default=True, row_default_height=50, size_hint_y=None)
        grid_layout.bind(minimum_height=grid_layout.setter('height'))
        
        self.Id = MDTextField(
            hint_text='University Roll No',
            padding=(20, 10, 20, 10)
        )

        self.checkbox1 = MDCheckbox(active=False, size_hint=(None, None), size=(48, 48))
        self.label1 = MDLabel(text="Name", valign="center")
        self.text_field1 = MDTextField(disabled=True)
        
        self.checkbox2 = MDCheckbox(active=False, size_hint=(None, None), size=(48, 48))
        self.label2 = MDLabel(text="EmailId", valign="center")
        self.text_field2 = MDTextField(disabled=True)
        
        self.checkbox3 = MDCheckbox(active=False, size_hint=(None, None), size=(48, 48))
        self.label3 = MDLabel(text="Age", valign="center")
        self.text_field3 = MDTextField(disabled=True)
        
        self.checkbox4 = MDCheckbox(active=False, size_hint=(None, None), size=(48, 48))
        self.label4 = MDLabel(text="Phone No", valign="center")
        self.text_field4 = MDTextField(disabled=True)
        
        def on_checkbox_active(checkbox, value, text_field):
            text_field.disabled = not value
        
        self.checkbox2.bind(active=lambda instance, value: on_checkbox_active(self.checkbox2, value, self.text_field2))
        self.checkbox1.bind(active=lambda instance, value: on_checkbox_active(self.checkbox1, value, self.text_field1))
        self.checkbox3.bind(active=lambda instance, value: on_checkbox_active(self.checkbox3, value, self.text_field3))
        self.checkbox4.bind(active=lambda instance, value: on_checkbox_active(self.checkbox4, value, self.text_field4))
        

        grid_layout.add_widget(self.Id)

        grid_layout.add_widget(self.label1)
        grid_layout.add_widget(self.checkbox1)
        grid_layout.add_widget(self.text_field1)
        
        grid_layout.add_widget(self.label2)
        grid_layout.add_widget(self.checkbox2)
        grid_layout.add_widget(self.text_field2)
        
        grid_layout.add_widget(self.label3)
        grid_layout.add_widget(self.checkbox3)
        grid_layout.add_widget(self.text_field3)
        
        grid_layout.add_widget(self.label4)
        grid_layout.add_widget(self.checkbox4)
        grid_layout.add_widget(self.text_field4)


        self.back_button = MDRaisedButton(text='Back to Main Screen', on_release=self.goto_main_screen)

        self.register_button = Button(text='Register', size_hint=(None, None))
        self.register_button.bind(on_press=self.register)

        scroll_view.add_widget(grid_layout)
        layout.add_widget(scroll_view)
        layout.add_widget(self.register_button)
        layout.add_widget(self.back_button)
        
        self.add_widget(layout)

    def register(self, instance):
        if self.checkbox1.active:
            text1=self.text_field1.text
        if self.checkbox2.active:
            text2=self.text_field2.text 
        if self.checkbox3.active:
            text3=self.text_field3.text 
        if self.checkbox4.active:
            text4=self.text_field4.text 
        
        data={}
        if(self.checkbox1.active):
            data['name']=text1
        if(self.checkbox2.active):
            data['email']=text2
        if self.checkbox3.active:
            data['age']=int(text3)
        if self.checkbox4.active:
            data['phone_no']=text4

        database.dbms_update(data,self.Id.text)

    def goto_main_screen(self, instance):
        self.manager.current = 'main'


class MyApp(MDApp):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(SplashScreen(name='splash'))
        self.sm.add_widget(MainScreen(name='main'))
        self.sm.add_widget(Screen1(name='screen1'))
        self.sm.add_widget(Screen2(name='screen2'))
        self.sm.add_widget(Screen3(name='screen3'))
        return self.sm


if __name__ == '__main__':
    MyApp().run()
