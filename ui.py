import flet as ft
import random
import asyncio

from word import Word
from word_list import WordList


class UI:
    @staticmethod
    def read_file(file_name: str = "words.txt") -> str:
        with open(file_name, "r", encoding="utf-8") as file:
            return file.read()

    @staticmethod
    def parse_file_to_words_list(file_name: str = "words.txt") -> WordList:
        return WordList(WordList.parse_file_to_words(UI.read_file(file_name)))

    @staticmethod
    def clean_stress_index(word_obj: Word) -> int:
        """Индекс ударной буквы в строке word_no_highlight (без U+0301)."""
        idx = word_obj.stress_index
        if idx < 0:
            return -1
        clean_idx = 0
        for i, ch in enumerate(word_obj.word):
            if i == idx:
                return clean_idx
            if ch != "\u0301":
                clean_idx += 1
        return -1

    @staticmethod
    async def main(page: ft.Page):
        page.title = "Ударения"
        page.bgcolor = ft.Colors.BLUE_GREY_900
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER

        # --- состояние ---
        words_list = UI.parse_file_to_words_list()
        unshown_words: list[Word] = list(words_list.word_list)
        random.shuffle(unshown_words)

        score = 0
        possible_score = 0
        streak = 0
        current_word: Word | None = None
        correct_index = -1
        locked = False

        # --- UI-элементы ---
        letters_row = ft.Row(
            controls=[],
            alignment=ft.MainAxisAlignment.CENTER,
            wrap=True,
        )
        feedback_text = ft.Text("", size=18, color=ft.Colors.WHITE)
        score_text = ft.Text(
            "Score: 0/0    Streak: 0",
            size=16,
            color=ft.Colors.WHITE_70,
        )

        def render_word(word: str) -> None:
            letters_row.controls.clear()
            for i, letter in enumerate(word):
                tile = ft.Container(
                    content=ft.Text(
                        letter,
                        size=30,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE,
                    ),
                    width=56,
                    height=68,
                    bgcolor=ft.Colors.BLUE_GREY_700,
                    border_radius=12,
                    alignment=ft.Alignment.CENTER,
                    on_click=lambda e, idx=i: page.run_task(
                        on_letter_click, idx
                    ),
                )
                letters_row.controls.append(tile)

        async def on_letter_click(index: int) -> None:
            nonlocal score, possible_score, streak, locked
            if locked or current_word is None:
                return

            locked = True
            possible_score += 1

            clicked_tile = letters_row.controls[index]
            correct_tile = letters_row.controls[correct_index]

            if index == correct_index:
                score += 1
                streak += 1
                clicked_tile.bgcolor = ft.Colors.GREEN_600
                feedback_text.value = "Правильно! 🟢"
                feedback_text.color = ft.Colors.GREEN_300
            else:
                streak = 0
                clicked_tile.bgcolor = ft.Colors.RED_600
                correct_tile.bgcolor = ft.Colors.GREEN_600
                feedback_text.value = (
                    f"Неверно 🔴  Верно: {current_word.word}"
                )
                feedback_text.color = ft.Colors.RED_300

            score_text.value = (
                f"Score: {score}/{possible_score}    Streak: {streak}"
            )
            page.update()

            await asyncio.sleep(1.5)
            show_next_word()

        def show_next_word() -> None:
            nonlocal current_word, correct_index, locked
            if not unshown_words:
                letters_row.controls.clear()
                letters_row.controls.append(
                    ft.Text("Игра окончена!", size=32, color=ft.Colors.WHITE)
                )
                feedback_text.value = (
                    f"Итоговый счёт: {score}/{possible_score}"
                )
                feedback_text.color = ft.Colors.WHITE
                page.update()
                return

            current_word = unshown_words.pop()
            correct_index = UI.clean_stress_index(current_word)
            locked = False
            render_word(current_word.word_no_highlight)
            feedback_text.value = "Кликните на ударную гласную"
            feedback_text.color = ft.Colors.WHITE_70
            page.update()

        # --- карточка ---
        card = ft.Container(
            width=760,
            height=380,
            bgcolor=ft.Colors.BLUE_GREY_800,
            border_radius=24,
            padding=40,
            alignment=ft.Alignment.CENTER,
            content=ft.Column(
                controls=[
                    ft.Text(
                        "Выберите ударный слог",
                        size=20,
                        color=ft.Colors.WHITE_70,
                    ),
                    ft.Container(height=30),
                    letters_row,
                    ft.Container(height=30),
                    feedback_text,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        )

        # --- общий layout ---
        layout = ft.Column(
            controls=[
                ft.Container(expand=1),
                card,
                ft.Container(expand=1),
                score_text,
                ft.Container(height=24),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        )
        page.add(layout)

        show_next_word()

    @staticmethod
    def run():
        ft.run(UI.main, view=ft.AppView.WEB_BROWSER)