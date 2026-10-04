import flet as ft
from random import randint
class UI:
    def __init__(self):
        pass

    @staticmethod
    def main(page: ft.Page):
        page.title = "Ударения"
        page.bgcolor = ft.Colors.WHITE_54

        text = ft.Text("Выбери правильное ударение", size=24)
        container = ft.Container(
            content=text,
            alignment=ft.Alignment.CENTER,
            expand=True,
        )
        stack = ft.Stack(expand=True,
                         controls=[container])
        #page.add(stack)
        page.add(ft.Container(
            expand=True,                        # на весь экран
            alignment=ft.Alignment.CENTER,      # центрируем содержимое
            content=ft.Container(
                width=700,
                height=600,
                bgcolor=ft.Colors.RED_500,
            ),
))



    @staticmethod
    def run():
        ft.run(UI.main, view=ft.AppView.WEB_BROWSER)