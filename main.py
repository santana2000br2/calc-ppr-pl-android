from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from calculos import calcular_janeiro, calcular_julho

class Tela(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=20, spacing=10, **kwargs)

        self.add_widget(Label(text="Calc PPR / PL", font_size=22))
        self.add_widget(Label(text="Aroldo Santana", font_size=12))

        self.salario = TextInput(hint_text="Salário Bruto", input_filter="float")
        self.pl = TextInput(hint_text="PL (em salários)", input_filter="float")
        self.ppr = TextInput(hint_text="PPR (em salários)", input_filter="float")
        self.bruto_jan = TextInput(hint_text="Bruto Janeiro (só Julho)", input_filter="float")
        self.ir_jan = TextInput(hint_text="IR Janeiro (só Julho)", input_filter="float")

        self.mes = Spinner(text="Janeiro", values=("Janeiro", "Julho"))

        self.resultado = Label(text="", halign="left", valign="top")
        self.resultado.bind(size=self.resultado.setter("text_size"))

        btn = Button(text="Calcular", size_hint_y=None, height=50)
        btn.bind(on_press=self.calcular)

        for w in [
            self.salario, self.pl, self.ppr,
            self.mes, self.bruto_jan, self.ir_jan,
            btn, self.resultado
        ]:
            self.add_widget(w)

    def calcular(self, _):
        try:
            salario = float(self.salario.text)
            ppr = float(self.ppr.text)

            if self.mes.text == "Janeiro":
                pl = float(self.pl.text)
                r = calcular_janeiro(salario, pl, ppr)
                self.resultado.text = (
                    f"JANEIRO\n"
                    f"PL: R$ {r['pl']:.2f}\n"
                    f"PPR: R$ {r['ppr']:.2f}\n"
                    f"IR: R$ {r['ir']:.2f}\n"
                    f"Líquido: R$ {r['liquido']:.2f}"
                )
            else:
                bruto_jan = float(self.bruto_jan.text)
                ir_jan = float(self.ir_jan.text)
                r = calcular_julho(salario, ppr, bruto_jan, ir_jan)
                self.resultado.text = (
                    f"JULHO\n"
                    f"PPR: R$ {r['bruto']:.2f}\n"
                    f"IR: R$ {r['ir']:.2f}\n"
                    f"Líquido: R$ {r['liquido']:.2f}"
                )
        except:
            self.resultado.text = "Preencha todos os campos corretamente."

class CalculadoraPPRApp(App):
    def build(self):
        return Tela()

CalculadoraPPRApp().run()
