import dataclasses


@dataclasses.dataclass
class StackDatabase:
    stack: tuple[float, ...] = ()


database = StackDatabase()
