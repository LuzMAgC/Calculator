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

    def test_print_6_when_6_is_given(
        self,
    ):
        # Given
        calculator = Calculator()
        # When
        calculator.add_number(6)
        # Then
        assert calculator.print_screen() == 6

    def test_print_9_when_9_is_given(
        self,
    ):
        # Given
        calculator = Calculator()
        # When
        calculator.add_number(9)
        # Then
        assert calculator.print_screen() == 9

    def test_print_12_when_1_and_2_are_given(
        self,
    ):
        # Given
        calculator = Calculator()
        # When
        calculator.add_number(1)
        calculator.add_number(2)
        # Then
        assert calculator.print_screen() == 12

    def test_print_983_when_0_9_8_and_3_are_given(
        self,
    ):
        # Given
        calculator = Calculator()
        # When
        calculator.add_number(0)
        calculator.add_number(9)
        calculator.add_number(8)
        calculator.add_number(3)
        # Then
        assert calculator.print_screen() == 983

    def test_erase_last_number(
        self,
    ):
        # Given
        calculator = Calculator()
        # When
        calculator.add_number(8)
        calculator.add_number(3)
        calculator.erase()
        # Then
        assert calculator.print_screen() == 8

    def test_erase_last_2_numbers(
        self,
    ):
        # Given
        calculator = Calculator()
        # When
        calculator.add_number(8)
        calculator.add_number(3)
        calculator.add_number(3)
        calculator.erase()
        calculator.erase()
        # Then
        assert calculator.print_screen() == 8
