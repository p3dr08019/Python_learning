from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout):

    def __init__(self):
        super(LoginScreen, self).__init__(**kwargs)

class MyApp(App):

    def build(self):
        return LoginScreen(self)

if __name__ == '__main__':
    MyApp().run()
pass
'''
class Cadastro:
    nome_completo = str()
    cpf = int()
    

    def sacar():

    return

    def depositar():
    
    return
'''

