class Calculator:
    number = 0
    operator = ""

    def print_screen(
        self,
    ) -> str:
        return f"{self.number}{self.operator}"

    def add_number(self, number: int) -> None:
        self.number = int(f"{self.number}{number}")

    def erase(self) -> None:
        str_number = f"{self.number}"

        if len(str_number) <= 1:
            self.number = 0
            return

        self.number = int(str_number[:len(str_number)-1])

    def clear(self) -> None:
        self.number = 0

    def add_operator(self, operator: str) -> None:
        if self.operator == "":
            self.operator = operator
