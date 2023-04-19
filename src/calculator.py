class Calculator:
    number = 0
    operator = ""
    number2 = ""

    def print_screen(
        self,
    ) -> str:
        return f"{self.number}{self.operator}{self.number2}"

    def add_number(self, number: int) -> None:
        if self.operator == "":
            self.number = int(f"{self.number}{number}")
        else:
            self.number2 = int(f"{self.number2}{number}")

    def erase(self) -> None:

        if self.number2 == "" and self.operator != "":
            self.operator = ""
            return

        elif self.operator == "":
            str_number = f"{self.number}"

            if len(str_number) <= 1:
                self.number = 0
                return

            self.number = int(str_number[:len(str_number) - 1])
            return

        str_number2 = f"{self.number2}"

        if len(str_number2) <= 1:
            self.number2 = ""
            return

        self.number2 = int(str_number2[:len(str_number2)-1])
        return

    def clear(self) -> None:
        self.number = 0

    def add_operator(self, operator: str) -> None:
        self.operator = operator
