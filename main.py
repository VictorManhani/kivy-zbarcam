from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

class Home(BoxLayout):
    pass

Builder.load_string('''
#:import ZBarCam zbarcam.ZBarCam
#:import ZBarSymbol pyzbar.pyzbar.ZBarSymbol

<Home>:
    orientation: 'vertical'
    ZBarCam:
        id: zbarcam
        # optional, by default checks all types
        code_types: ZBarSymbol.QRCODE, ZBarSymbol.EAN13
    Label:
        size_hint: None, None
        size: self.texture_size[0], 50
        text: ', '.join([str(symbol.data) for symbol in zbarcam.symbols])
''')

class ZBarCamApp(App):
    def build(self):
        return Home()

if __name__ == '__main__':
    ZBarCamApp().run()