"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

TIMER_MIN = 1
TIMER_MAX = 19


class Repro1277(toga.App):

    def startup(self):
        main_box = toga.Box()

        self.value_label = toga.Label(text="Val: ")
        self.value_label.style.width = 80
        self.value_label.style.padding = 5

        self.timer_label = toga.Label(text="Tick: ")
        self.timer_label.style.width = 80
        self.timer_label.style.padding = 5

        self.timer_slide = toga.Slider(range=(TIMER_MIN, TIMER_MAX), tick_count=(TIMER_MAX - TIMER_MIN + 1),
                                       on_change=(self.timer_change),
                                       on_release=(self.timer_set))
        self.timer_slide.style.padding = 5
        self.timer_slide.style.padding_top = 5
        self.timer_slide.style.width = 200
        self.timer_slide.value = 10.0

        main_box.add(self.timer_slide)
        main_box.add(self.timer_label)
        main_box.add(self.value_label)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def timer_change(self, widget):
        self.timer_label.text = "Counter: " + str(self.timer_slide.tick_value)
        self.value_label.text = "Value: " + str(self.timer_slide.value)

    def timer_set(self, widget):
        pass


def main():
    return Repro1277()
