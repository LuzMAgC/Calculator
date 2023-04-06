class Calculator:
    number = 0

    def print_screen(
        self,
    ) -> int:
        return self.number

    def add_number(self, number: int) -> None:
        self.number = number
