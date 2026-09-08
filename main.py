from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.title = "آلة حاسبة بايثون"
        self.formula = ""
        
        root = BoxLayout(orientation="vertical", padding=15, spacing=15)
        
        # شاشة العرض
        self.solution = TextInput(
            font_size=40,
            readonly=True,
            halign="right",
            multiline=False,
            size_hint=(1, 0.25)
        )
        root.add_widget(self.solution)
        
        # الأزرار
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["C", "0", "=", "+"]
        ]
        
        for row in buttons:
            h_layout = BoxLayout(spacing=10)
            for label in row:
                button = Button(
                    text=label,
                    font_size=30,
                    background_color=(0.2, 0.6, 0.8, 1) if label != "C" else (0.8, 0.2, 0.2, 1)
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            root.add_widget(h_layout)
            
        return root

    def on_button_press(self, instance):
        txt = instance.text
        if txt == "C":
            self.formula = ""
            self.solution.text = "0"
        elif txt == "=":
            try:
                res = str(eval(self.formula))
                self.solution.text = res
                self.formula = res
            except Exception:
                self.solution.text = "خطأ"
                self.formula = ""
        else:
            if self.formula == "" and txt in "+-*/0":
                return
            self.formula += txt
            self.solution.text = self.formula

if __name__ == "__main__":
    CalculatorApp().run()
