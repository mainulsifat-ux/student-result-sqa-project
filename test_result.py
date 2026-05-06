import pytest
from result_system import StudentResult


def test_grade_A_plus():
    student = StudentResult("Rahim", 85)
    assert student.calculate_grade() == "A+"


def test_grade_A():
    student = StudentResult("Karim", 72)
    assert student.calculate_grade() == "A"


def test_grade_B():
    student = StudentResult("Sifat", 55)
    assert student.calculate_grade() == "B"


def test_grade_F():
    student = StudentResult("Nayeem", 30)
    assert student.calculate_grade() == "F"


def test_invalid_marks():
    with pytest.raises(ValueError):
        student = StudentResult("Test", 150)
        student.calculate_grade()
