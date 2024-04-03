class CannotApplyRpnCommandException(Exception):
    def __init__(self):
        super().__init__(
            "Cannot apply rpn command. The stack should contain at least two elements"
        )


class DivisionByZeroException(Exception):
    def __init__(self):
        super().__init__(
            "Cannot apply division command. The last stack's elements should not be zero"
        )
