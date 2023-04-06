from src.calculator import Calculator


class TestCalculator:

    def test_print(
        self,
    ):
        # Given
        calculator = Calculator()
        # When

        # Then
        assert calculator.print_screen() == 0
