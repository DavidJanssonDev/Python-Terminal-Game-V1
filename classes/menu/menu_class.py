from typing import Callable
from rich.console import Console
from tabulate import tabulate


class Menu:
    def __init__(self) -> None:

        self.printing_console = Console()
        self.tuppel_data: list[tuple[str, list[str]]] = []

        self.header_data: list[str] = []
        self.body_data: list[list[str]] = []

    def set_header_data(self, input_headers_data: list[str]) -> None:
        self.header_data = input_headers_data

    def set_body_data(self, intput_body_data: list[list[str]]) -> None:
        self.body_data = intput_body_data

    def combind_data_to_tubulate_data(self) -> dict[str, list[str]]:
        return {
            header_element: self.body_data[index]
            for index, header_element in enumerate(self.header_data)
        }

    def printing_menu(self) -> None:

        tabulate_data: dict[str, list[str]] = self.combind_data_to_tubulate_data()
        self.printing_console.print(
            tabulate(tabulate_data, headers="keys", tablefmt="heavy_grid")
        )


if __name__ == "__main__":
    menuPrinter = Menu()
    menuPrinter.set_body_data(
        [
            [
                "QUESTION 1",
                "QUESTION 2",
                "QUESTION 3",
                "QUESTION 4",
            ],
            [
                "KOMAND 1",
                "KOMAND 2",
                "KOMAND 3",
                "KOMAND 4",
            ],
        ]
    )
    menuPrinter.set_header_data(["QUESTIONS", "COMAND"])

    menuPrinter.printing_menu()

    # menuPrinter.printing_menu()
