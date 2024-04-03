import dataclasses


@dataclasses.dataclass(kw_only=True)
class RpnStack:
    values: tuple[int, ...]

    def append(self, value) -> None:
        self.values = tuple(self.values + (value,))

    def clone(self):
        return RpnStack(values=self.values[:])
