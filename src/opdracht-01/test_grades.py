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
    grade = 4.0
    result = is_sufficient(grade)
    assert result is False


def test_is_sufficient_geeft_true_bij_precies_55():
    grade = 5.5
    result = is_sufficient(grade)
    assert result is True


def test_calculate_average_berekent_gemiddelde():
    grades = [6.0, 8.0]
    result = calculate_average(grades)
    assert result == 7.0


def test_calculate_average_geeft_nul_bij_lege_lijst():
    grades = []
    result = calculate_average(grades)
    assert result == 0.0


def test_highest_grade_vindt_hoogste_cijfer():
    grades = [5.0, 9.0, 7.0]
    result = highest_grade(grades)
    assert result == 9.0


def test_highest_grade_geeft_none_bij_lege_lijst():
    grades = []
    result = highest_grade(grades)
 
    assert result is None


def test_count_sufficient_telt_voldoendes():
    grades = [4.0, 6.0, 8.0, 5.0]
    result = count_sufficient(grades)
    assert result == 2