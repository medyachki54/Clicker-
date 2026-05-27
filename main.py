from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
import random

class ClickerGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)
        
        self.score = 0
        
        # Заголовок
        self.label = Label(
            text="Счет: 0", 
            font_size=60, 
            color=(1, 1, 1, 1)
        )
        self.add_widget(self.label)
        
        # Кнопка кликера
        self.btn = Button(
            text="КЛИК!", 
            font_size=40,
            background_color=(0.2, 0.6, 1, 1)
        )
        self.btn.bind(on_press=self.add_point)
        self.add_widget(self.btn)

    def add_point(self, instance):
        self.score += 1
        self.label.text = f"Счет: {self.score}"
        
        # Случайный цвет фона при каждом клике
        Window.clearcolor = (random.random(), random.random(), random.random(), 1)

class MyApp(App):
    def build(self):
        return ClickerGame()

if __name__ == '__main__':
    MyApp().run()
