class CannotApplyRpnCommandException(Exception):
    def __init__(self):
        super().__init__(
            "Cannot apply rpn command. The stack should contain at least two elements"
        )
