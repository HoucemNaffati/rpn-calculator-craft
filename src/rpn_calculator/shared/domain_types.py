from enum import Enum


class CommandType(str, Enum):
    add = "+"
    subtract = "-"
    multiply = "*"
    divide = "/"
    clear = "C"
