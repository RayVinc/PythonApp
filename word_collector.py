import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import random
from kivy.graphics.texture import Texture
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle
from kivy.graphics import Rectangle, Color

#1, 0.87, 0, 1 yellow
#0.94, 0.55, 0 , 1 orange


class MyRoot(BoxLayout):

    def __init__(self, **kwargs):
        super(MyRoot, self).__init__(**kwargs)
        
        with self.canvas.before:
            Color(0.94, 0.55, 0, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def gradient_texture(self):
        texture = Texture.create(size=(2, 2), colorfmt='rgba')
        # Convert the normalized colors to 8-bit format
        top_color = [int(255 * x) for x in (1, 0.87, 0, 1)]
        bottom_color = [int(255 * x) for x in (0.94, 0.55, 0, 1)]

        # Flatten the colors to a single list
        pixels = top_color + bottom_color
        texture.blit_buffer(bytearray(pixels), colorfmt='rgba', bufferfmt='ubyte')
        return texture

    def generate_numbers(self):
        # Generate 6 random numbers between 1 and 49
        numbers = sorted(random.sample(range(1, 50), 6))
        
        # Generate the "Superzahl" between 0 and 9
        superzahl = random.randint(0, 9)
        
        # Assigning the generated numbers to the labels
        for i, num in enumerate(numbers):
            getattr(self, f'num_{i + 1}').text = str(num)

        self.superzahl.text = f'Superzahl {superzahl}'

class LotteryNumbers(App):

    def build(self):
        return MyRoot()

if __name__ == "__main__":
    LotteryNumbers().run()
