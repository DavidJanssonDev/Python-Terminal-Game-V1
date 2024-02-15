from typing import Callable
from rich.console import Console

from tabulate import tabulate


class Menu:
    def __init__(self) -> None:
        self.terminal_console = Console()
        self.menu_headers: list[str] = []
        self.menu_data: list[list[str]] = []

        
    def printing_menu(self) -> None:

        menu_dict_data = self.format_data(self.menu_data, self.menu_headers)

        self.terminal_console.print(
            tabulate(tabular_data=menu_dict_data, tablefmt="keys")
        )

    def format_data(self, data: list[list[str]], headers: list[str]) -> dict[str, str]:
        raise NotImplementedError

    def set_menu_headers(self, headers: list[str]) -> None:
        self.menu_headers = headers

    def set_menu_data(self, data: list[list[str]]) -> None:
        self.menu_data = data

    def get_menu_options() -> Callable[[]]:
        raise NotImplementedError


""" 
________________________
| QUESTIONS  | COMAND  |
|____________|_________|
| QUESTION 1 | KOMAND 1|
| QUESTION 2 | KOMAND 2|
| QUESTION 3 | KOMAND 3|
| QUESTION 4 | KOMAND 4|
|____________|_________|

data = {
    QUESTIONS: [
        "QUESTION 1", 
        "QUESTION 2", 
        "QUESTION 3", 
        "QUESTION 4", 
    ],
    COMAND: [
        "KOMAND 1",
        "KOMAND 2",
        "KOMAND 3",
        "KOMAND 4",
    ]
    
}

headers = ["QUESTIONS", "COMAND"]
data = [
    [
        "QUESTION 1", 
        "QUESTION 2", 
        "QUESTION 3", 
        "QUESTION 4", 
    ],
    [
        "COMAND 1",
        "COMAND 2",
        "COMAND 3",
        "COMAND 4",
    ]
    ]


"""
