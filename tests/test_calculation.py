import pytest
from employee import Employee


class TestEmployee:

    def test_calculation_is_correct(self):
        new_employee = Employee("fake_name",
                                [{'Day': 'MO', 'Start': '10:00', 'End': '12:00'},
                                 {'Day': 'TU', 'Start': '10:00', 'End': '12:00'},
                                 {'Day': 'TH', 'Start': '01:00', 'End': '03:00'},
                                 {'Day': 'SA', 'Start': '14:00', 'End': '18:00'},
                                 {'Day': 'SU', 'Start': '20:00', 'End': '21:00'}])
        assert new_employee.payment == 215

    def test_validation_is_correct(self):
        with pytest.raises(Exception) as exc:
            new_employee = Employee("fake_name", "")
            assert "Invalid hours" in str(exc)
