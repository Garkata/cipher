from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from cezur import cezur
from cezur import caesar_decrypt
from adbash import ADbash
from vigenere import vigenere
from vigenere import vigenere_decrypt
from ColumnarTransposition import columnar_encrypt
from ColumnarTransposition import columnar_decrypt
from railfence import rail_fence_encrypt
from railfence import rail_fence_decrypt
from route import encrypt_custom_route_cipher 
from route import decrypt_custom_route_cipher
from MORSE_CODE import encrypt_to_morse
from MORSE_CODE import decrypt_from_morse
from playf import playfair_encrypt
from playf import playfair_decrypt
from skip import skip
from bifid import bifid
from decryptbifid import bifid_decrypt
Window.size = (320, 480)
Window.clearcolor = (1, 0.95, 0.88, 1)
on_spinner = 'mazna'
textche= 'mazna'
kluch='mazna'
shifrovano='mazna'
class CipherApp(App):
    def popup(self):
        
        popup_layout = BoxLayout(orientation='vertical')
        popup = Popup(title="",
                      content=popup_layout,
                      size_hint=(None, None),
                      size=(300, 400),
                      pos_hint = {"x":-0.02,"y":0.2},
                      auto_dismiss=True)
        popup.background_color = (1, 0.95, 0.88, 1)
        popup.separator_color = (1, 0.95, 0.88, 1)
        img = Image(source='',size=(300,300))
   #     duma = Label(text='asdasdas',size=(100,50))
        popup_layout.add_widget(img)
  #      popup_layout.add_widget(duma)
        if(self.on_spinner =='Adbash'):
          img.source='adbash.png'
        if(self.on_spinner =='Bifid'):
            img.source='bifid.jpg'
        if(self.on_spinner=='Caesar'):
            img.source='Ceasar.png'
        if(self.on_spinner=='Columnar Transposition'):
            img.source='columnar-transposition.png'
        if(self.on_spinner=='Morse code'):
            img.source='morse-code.webp'
        if(self.on_spinner=='Playfair'):
            img.source='playfair.png'
        if(self.on_spinner=='Rail fence'):
            img.source='rail_fence.png'
        if(self.on_spinner=='Route'):
            img.source='route.jpg'
        if(self.on_spinner=='Skip'):
            img.source='skip.png'
        if(self.on_spinner=='Vigenère'):
            img.source='vigenerevisuals.png'
        popup.open()
        

    def build(self):
        # Root vertical layout
        root = FloatLayout()
        root.canvas.before.clear()
        # Title
        liniq = Button(
            background_color = [0.29,0.56,0.89,1],
            text=" Cipher Tool ",
            background_normal="",
            background_down="",
            size_hint=(1,0.07),
            pos_hint={'x': 0, 'y':0.93},
            )
        root.add_widget(liniq)
        
        obqsnenie = Button(
            background_color = [0.29,0.56,0.89,1],
            background_normal="",
            size_hint_x=(0.4),
            size_hint_y=(0.13),
            pos_hint={'x':0.7,'y':0.87},
            text="Obqsnen")
        obqsnenie.bind(on_press=lambda instance: self.popup())
        root.add_widget(obqsnenie)        
        
        # Input text
        self.input_text = TextInput(
            hint_text='Enter text here...',
            size_hint=(0.85, 0.2),
            pos_hint={'x':0.075,'y':0.60},
            background_color=[1,1,1,1],
            foreground_color=[0.2,0.2,0.2,1],
            multiline=True,
            padding=[10,10,10,10],
            font_size=18
        )
        
        

        # Cipher type spinner + key input container

        self.cipher_spinner = Spinner(
            text='Caesar',
            values=['Adbash','Bifid','Caesar','Columnar Transposition','Morse code','Playfair','Rail fence','Route','Skip', 'Vigenère'],
            background_normal="",
            background_down="",
            size_hint=(0.35,0.08),
            pos_hint={'x':0.075,'y':0.5},
            background_color=[0.29,0.56,0.89,1],
            color=[1,1,1,1],
            font_size=16
        )
        
        self.cipher_spinner.bind(text=self.on_spinner_select)
             
        self.key_input = TextInput(
            text='3',
            hint_text='Key',
            size_hint=(0.4, 0.08),
            pos_hint={'x':0.525,'y':0.5},
            multiline=False,
            background_color=[1,1,1,1],
            foreground_color=[0.2,0.2,0.2,1],
            font_size=16,
            padding=[10,10,10,10]
        )
        self.kluch= self.key_input.text
        


        # Buttons container

        encrypt_btn = Button(
            text='Encrypt 🔐',
            background_normal="",
            size_hint=(0.40, 0.12),
            pos_hint={'x':0.075,'y':0.3},
            background_color=[0.29, 0.56, 0.89, 1],
            color=[1,1,1,1],
            font_size=18
        )
        encrypt_btn.bind(on_press=self.encrypt_text)

        decrypt_btn = Button(
            text='Decrypt 🔓',
            background_normal="",
            size_hint=(0.40, 0.12),
            pos_hint={'x':0.525,'y':0.3},
            background_color=[0.29, 0.56, 0.89, 1],
            color=[1,1,1,1],
            font_size=18
        )
        decrypt_btn.bind(on_press=self.decrypt_text)
        root.add_widget(decrypt_btn)
        root.add_widget(encrypt_btn)


        self.output_text = TextInput(
            readonly=True,
            size_hint=(0.85, 0.2),
            pos_hint={'x':0.075,'y':0.03},
            height=120,
            background_color=[1,1,1,1],
            foreground_color=[0.2,0.2,0.2,1],
            multiline=True,
            padding=[10,10,10,10],
            font_size=18
        )
        bg = Image(source="Frame1.png",size_hint=(1,1))
        root.add_widget(bg)
        root.add_widget(self.output_text)
        root.add_widget(self.cipher_spinner)
        root.add_widget(self.input_text)
        root.add_widget(self.key_input)
        return root

    def encrypt_text(self, instance):
        self.textche=self.input_text.text
        self.kluch=self.key_input.text
        if(self.on_spinner=='Adbash'):
            self.output_text.text=ADbash(self.textche)        
        if(self.on_spinner=='Caesar'):
            self.shifrovano= cezur(self.textche,int(self.kluch))
            self.output_text.text = self.shifrovano
        if(self.on_spinner=='Columnar Transposition'):
            self.output_text.text= columnar_encrypt(self.textche,self.kluch)
        if(self.on_spinner=='Vigenère'):
            self.output_text.text=vigenere(self.textche,self.kluch)
        if(self.on_spinner=='Rail fence'):
            self.output_text.text=rail_fence_encrypt(self.textche,int(self.kluch))
        if(self.on_spinner=='Route'):
            self.output_text.text=encrypt_custom_route_cipher(self.textche)
        if(self.on_spinner=='Playfair'):
            self.output_text.text=playfair_encrypt(self.textche,str(self.kluch))
        if(self.on_spinner=='Morse code'):
            self.output_text.text=encrypt_to_morse(self.textche)
        if(self.on_spinner=='Skip'):
            self.output_text.text=skip(self.textche,int(self.kluch))
        if(self.on_spinner=='Bifid'):
            self.output_text.text=bifid(str(self.textche))



    def decrypt_text(self, instance):
        self.textche=self.input_text.text
        self.kluch=self.key_input.text
        if(self.on_spinner=='Route'):
            self.output_text.text=decrypt_custom_route_cipher(self.textche)
        if(self.on_spinner=='Skip'):
            self.output_text.text=skip(self.textche,int(self.kluch))
        if(self.on_spinner=='Adbash'):
            self.output_text.text=ADbash(self.textche)  
        if(self.on_spinner=='Caesar'):
            self.output_text.text = caesar_decrypt(self.textche,int(self.kluch))
        if(self.on_spinner=='Vigenère'):
            self.output_text.text=vigenere_decrypt(self.textche,self.kluch)
        if(self.on_spinner=='Rail fence'):
            self.output_text.text=rail_fence_decrypt(self.textche,int(self.kluch))
        if(self.on_spinner=='Columnar Transposition'):
            self.output_text.text= columnar_decrypt(self.textche,self.kluch)
        if(self.on_spinner=='Playfair'):
            self.output_text.text=playfair_decrypt(self.textche,str(self.kluch))
        if(self.on_spinner=='Morse code'):
            self.output_text.text=decrypt_from_morse(self.textche)
        if(self.on_spinner=='Bifid'):
            self.output_text.text=bifid_decrypt(str(self.textche))
    
    def on_spinner_select(self, cypher_spinner,text):
        if(text=='Adbash'):
           self.key_input.disabled =True
           self.key_input.opacity = 0.5
           self.on_spinner='Adbash'
           return 'Adbash'
        if(text=='Bifid'):
           self.key_input.disabled =True
           self.key_input.opacity = 0.5
           self.on_spinner='Bifid'
           return 'Bifid'
        if(text=='Caesar'):
           self.key_input.disabled =False
           self.key_input.opacity = 1
           self.on_spinner='Caesar'
           return 'Caesar'
        if(text=='Columnar Transposition'):
           self.key_input.disabled =False
           self.key_input.opacity = 1
           self.on_spinner='Columnar Transposition'
           return 'Columnar Transposition'
        if(text=='Morse code'):
           self.key_input.disabled =True
           self.key_input.opacity = 0.5
           self.on_spinner='Morse code'
           return 'Morse code'
        if(text=='Playfair'):
           self.key_input.disabled =False
           self.key_input.opacity = 1
           self.on_spinner='Playfair'
           return 'Playfair'
        if(text=='Rail fence'):
           self.key_input.disabled =False
           self.key_input.opacity = 1
           self.on_spinner='Rail fence'
           return 'Rail fence'
        if(text=='Route'):
           self.key_input.disabled =True
           self.key_input.opacity = 0.5
           self.on_spinner='Route'
           return 'Route'
        if(text=='Skip'):
           self.key_input.disabled =False
           self.key_input.opacity = 1
           self.on_spinner='Skip'
           return 'Skip'
        if(text=='Vigenère'):
           self.key_input.disabled =False
           self.key_input.opacity = 1
           self.on_spinner='Vigenère'
           return 'Vigenère'  

    on_spinner=on_spinner_select          


        
if __name__ == '__main__':
    CipherApp().run()


    asd