import sys
import random

from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import (
    QLabel,
    QWidget,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QApplication,
)

# Import snake_case and true_property after PySide6 imports.
from __feature__ import snake_case, true_property


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Since QMainWindow does not have a fixedSize property,
        # we use the setFixedSize() method but call it in the
        # snake-case style.
        self.set_fixed_size(300, 100)

        # However, QMainWindow does have a windowTitle property
        # for which we assign a value directly but must write
        # the property's name in snake-case style.
        self.window_title = "PySide6 Translator"

        # And this is our non-Qt Python property to which
        # we must assign a value just like above anyway,
        # so assigning values to properties uniformly
        # throughout our code could be intriguing.
        self.multilingual_greetings = (
            "Привет мир!",    # Russian ("Privet mir!" in Cyrillic)
            "Hallo Welt!",    # German
            "¡Hola Mundo!",   # Spanish
            "Hei maailma!",   # Finnish
            "Helló Világ!",   # Hungarian
            "Hallo Wereld!",  # Dutch
        )

        # We create a label with an English greeting by default.
        self.greeting = QLabel("Hello world!")

        # Instead of self.message.setAlignment(Qt.AlignCenter),
        # we set a value to the alignment property directly...
        self.greeting.alignment = Qt.AlignCenter

        # We now also create a button to translate our
        # English greeting and then connect it with
        # our translate_greeting() slot.
        self.translate_button = QPushButton("Translate")
        self.translate_button.clicked.connect(self.translate_greeting)

        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.add_widget(self.greeting)
        self.vertical_layout.add_widget(self.translate_button)

        self.widget_container = QWidget()
        self.widget_container.set_layout(self.vertical_layout)

        # Instead of calling .setCentralWidget(),
        # we call it by its snake-case name...
        self.set_central_widget(self.widget_container)

    @Slot()
    def translate_greeting(self):
        # Here, instead of using the .setText() method,
        # we set a value to the text property directly...
        self.greeting.text = random.choice(self.multilingual_greetings)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec()
