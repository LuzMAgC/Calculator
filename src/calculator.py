class Calculator:
    number = 0

    def print_screen(
        self,
    ) -> int:
        return self.number

    def add_number(self, number: int) -> None:
        self.number = int(f"{self.number}{number}")

    def erase(self) -> None:
        str_number = f"{self.number}"

        if len(str_number) <= 1:
            self.number = 0
            return

        self.number = int(str_number[:len(str_number)-1])
