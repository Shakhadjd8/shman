import os
import sys
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.graphics import RoundedRectangle, Color
from kivy.uix.image import Image
from kivy.clock import Clock

def resource_path(relative_path):
    """ Получение абсолютного пути к ресурсу. """
    try:
        # PyInstaller создает временную папку и помещает приложения в нее
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class CustomButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(*self.background_color)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, instance, value):
        self.rect.size = self.size
        self.rect.pos = self.pos

class ManualApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # словарь с контентом для каждого мануала в зависимости от подраздела
        self.manual_content = {
            1: {
                'мануал1': "Контент для мануала 1 в подразделе 1",
                'мануал2': "Контент для мануала 2 в подразделе 1",
                'мануал3': "Контент для мануала 3 в подразделе 1",
                # добавьте остальные мануалы...
            },
            2: {
                'мануал1': "Контент для мануала 1 в подразделе 2",
                'мануал2': "Контент для мануала 2 в подразделе 2",
                'мануал3': "Контент для мануала 3 в подразделе 2",
                # добавьте остальные мануалы...
            },
            3: {
                'мануал1': "Контент для мануала 1 в подразделе 2",
                'мануал2': "Контент для мануала 2 в подразделе 2",
                'мануал3': "Контент для мануала 3 в подразделе 2",
            },
            4: {
                'мануал1': "Контент для мануала 1 в подразделе 2",
                'мануал2': "Контент для мануала 2 в подразделе 2",
                'мануал3': "Контент для мануала 3 в подразделе 2",
            },
            5: {
                'мануал1': "Контент для мануала 1 в подразделе 2",
                'мануал2': "Контент для мануала 2 в подразделе 2",
                'мануал3': "Контент для мануала 3 в подразделе 2",
            }
            # добавьте остальные подразделы...
        }

        # Текст для названий подразделов
        self.subsection_texts = {
            1: "подр1",
            2: "подр2",
            3: "подр3",
            4: "подр4",
            5: "подр5",
            # добавьте остальные подразделы...
        }

        # Текст для названий мануалов
        self.manual_texts = {
            1: "мануал 1 (описание)",
            2: "мануал 2 (описание)",
            3: "мануал 3 (описание)",
            4: "мануал 4 (описание)",
            # добавьте остальные мануалы...
        }

        # цвета кнопок полупрозрачные
        self.button_colors = [
            (1, 0, 0, 0.5),
            (0, 1, 0, 0.5),
            (0, 0, 1, 0.5),
            (1, 1, 0, 0.5),
            (1, 0, 1, 0.5),
            (0, 1, 1, 0.5),
            (0.5, 0, 0.5, 0.5),
            (0.5, 0.5, 0, 0.5),
            (0, 0.5, 0, 0.5),
            (0.5, 0, 0, 0.5)
        ]

    def build(self):
        # Создаем заставку
        self.splash_layout = BoxLayout(orientation='vertical')

        # Добавляем изображение заставки
        self.splash_image = Image(source='log.jpg', allow_stretch=True, keep_ratio=False)  # Замена на ваше изображение
        self.splash_layout.add_widget(self.splash_image)

        Window.size = (1280, 720)
        return self.splash_layout  # Возвращаем сначала заставку

    def on_start(self):
        # Запланируем переход на основной интерфейс через 1 секунду
        Clock.schedule_once(self.show_main_interface, 1)

    def show_main_interface(self, dt):
        self.main_layout = BoxLayout(orientation='vertical', padding=25, spacing=20)

        # Добавляем изображение фона
        self.background_image = Image(source='haker.jpg', allow_stretch=True, keep_ratio=False)
        self.main_layout.add_widget(self.background_image)

        self.content_area = BoxLayout(orientation='vertical', size_hint=(1, None), spacing=10)
        self.content_area.bind(size=self.update_content_area)

        self.main_menu_widgets = [
            Label(text="", height=30),
            CustomButton(text="Раздел мануалов", on_press=self.show_manuals, size_hint_y=None, height=40),
            CustomButton(text="Создатель", on_press=self.show_creator, size_hint_y=None, height=40),
            Label(text="", height=20)
        ]

        self.back_button = CustomButton(text="Назад", on_press=self.go_back, size_hint_y=None, height=40)
        self.back_button.opacity = 0

        self.reset_main_menu()

        # Добавляем контент и кнопку "Назад"
        self.main_layout.add_widget(self.content_area)
        self.main_layout.add_widget(self.back_button)

        # Добавляем Label для нижней части экрана
        self.footer_label = Label(text="пенис секс пенис секс.", size_hint_y=None, height=50)

        self.main_layout.add_widget(self.footer_label)

        # Убираем заставку и показываем основное приложение
        self.root_window.remove_widget(self.splash_layout)  # Удаляем заставку
        self.root_window.add_widget(self.main_layout)  # Добавляем основной интерфейс

    def update_content_area(self, instance, value):
        self.content_area.height = self.content_area.minimum_height

    def reset_main_menu(self):
        self.content_area.clear_widgets()
        for i, widget in enumerate(self.main_menu_widgets):
            widget.background_color = self.button_colors[i % len(self.button_colors)]
            self.content_area.add_widget(widget)

    def show_manuals(self, instance):
        self.show_subscreen(self.create_manual_grid())

    def show_creator(self, instance):
        self.show_subscreen(Label(text="shakhasoft @govno5554", size_hint_y=None, height=140))

    def create_manual_grid(self):
        manual_grid = GridLayout(cols=1, size_hint_y=None)
        manual_grid.bind(minimum_height=manual_grid.setter('height'))

        for i in range(1, 6):  # Измените на 11, если у вас есть 10 подразделов.
            button_text = self.subsection_texts.get(i, f"Подраздел {i} (название)")
            button = CustomButton(text=button_text, background_color=self.button_colors[i % len(self.button_colors)],
                                  size_hint_y=None, height=40)
            button.bind(on_press=lambda x, i=i: self.show_sub_manuals(i))
            manual_grid.add_widget(button)

        scroll_view = ScrollView(size_hint=(1, None), size=(400, 300))
        scroll_view.add_widget(manual_grid)

        return scroll_view

    def show_sub_manuals(self, manual_section):
        self.back_button.opacity = 1
        self.content_area.clear_widgets()
        manual_grid = GridLayout(cols=1, size_hint_y=None)
        manual_grid.bind(minimum_height=manual_grid.setter('height'))

        for i in range(1, 4):  # Измените на 11, если у вас есть 10 мануалов в каждом подразделе.
            manual_name = f'мануал{i}'
            manual_button_text = self.manual_texts.get(i, manual_name)  # Изменяем название кнопки
            button = CustomButton(text=manual_button_text, size_hint_y=None, height=40,
                                  background_color=(1, 1, 1, 0.5))
            button.bind(on_press=lambda x, manual=manual_name, section=manual_section: self.show_manual_content(manual, section))
            manual_grid.add_widget(button)

        scroll_view = ScrollView(size_hint=(1, None), size=(400, 300))
        scroll_view.add_widget(manual_grid)

        self.content_area.add_widget(scroll_view)

    def show_manual_content(self, manual_name, manual_section):
        self.back_button.opacity = 1
        self.content_area.clear_widgets()

        manual_content = self.manual_content[manual_section][manual_name]

        scroll_view = ScrollView(size_hint=(1, None), size=(400, 300))

        label = Label(text=manual_content, size_hint_y=None)
        label.bind(texture_size=label.setter('size'))  # Динамическая высота метки
        scroll_view.add_widget(label)

        back_button = CustomButton(text="Назад", on_press=lambda x: self.show_sub_manuals(manual_section), size_hint_y=None, height=40)

        self.content_area.add_widget(scroll_view)
        self.content_area.add_widget(back_button)

    def show_subscreen(self, content):
        self.back_button.opacity = 1
        self.content_area.clear_widgets()
        self.content_area.add_widget(content)

    def go_back(self, instance):
        self.back_button.opacity = 0
        self.reset_main_menu()  # гл меню

if __name__ == '__main__':
    ManualApp().run()