from src.calculator import Calculator


class TestCalculator:

    def test_print_0_when_no_value_is_given(
        self,
    ):
        # Given
        calculator = Calculator()
        # When

        # Then
        assert calculator.print_screen() == 0
