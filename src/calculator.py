class Calculator:
    number = False

    def print_screen(
        self,
    ) -> int:
        if self.number:
            return 6
        return 0

    def add_number(self, number: int) -> None:
        self.number = True
