from grades import is_sufficient, calculate_average, highest_grade, count_sufficient


# VOORBEELD - Deze test is al ingevuld om te laten zien hoe het werkt
def test_voorbeeld_is_sufficient_geeft_true_bij_zeven():
    # Arrange: zet je testdata klaar
    grade = 7.0
    # Act: roep de functie aan
    result = is_sufficient(grade)
    # Assert: controleer het resultaat
    assert result is True


def test_is_sufficient_geeft_false_bij_vier():
    # TODO: Test of het cijfer 4.0 onvoldoende is
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_is_sufficient_geeft_true_bij_precies_55():
    # TODO: Test of 5.5 voldoende is (let op: dit is een grensgeval!)
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_calculate_average_berekent_gemiddelde():
    # TODO: Test of [6.0, 8.0] gemiddeld 7.0 is
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_calculate_average_geeft_nul_bij_lege_lijst():
    # TODO: Test of een lege lijst 0.0 teruggeeft
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_highest_grade_vindt_hoogste_cijfer():
    # TODO: Test of [5.0, 9.0, 7.0] het cijfer 9.0 teruggeeft
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_highest_grade_geeft_none_bij_lege_lijst():
    # TODO: Test of een lege lijst None teruggeeft
    # Hint: gebruik 'is None' in plaats van '== None'
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_count_sufficient_telt_voldoendes():
    # TODO: Test of [4.0, 6.0, 8.0, 5.0] er 2 voldoendes heeft
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"
