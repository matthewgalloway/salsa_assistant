import unittest
from unittest.mock import Mock

# Assuming your function is in a file called my_module.py
from salsa_app.spaced_repition_algorithm import spaced_repetition


class TestSpacedRepetition(unittest.TestCase):
    
    def setUp(self):
        self.form = Mock()
        self.form.cleaned_data = {}

    def test_spaced_repetition_case1(self):
        # Set up mock form data
        self.form.cleaned_data['easiness_factor_remembering'] = 1
        self.form.cleaned_data['repetition'] = 1
        self.form.cleaned_data['interval'] = 1
        self.form.cleaned_data['difficulty_remembering'] = 2

        expected_result = (1, 1.3, 2)
        result = spaced_repetition(self.form)

        self.assertEqual(result, expected_result)

    def test_spaced_repetition_case2(self):
        # Set up mock form data
        self.form.cleaned_data['easiness_factor_remembering'] = 1
        self.form.cleaned_data['repetition'] = 1
        self.form.cleaned_data['interval'] = 1
        self.form.cleaned_data['difficulty_remembering'] = 4

        expected_result = (1, 1.3, 2)
        result = spaced_repetition(self.form)

        self.assertEqual(result, expected_result)

    def test_spaced_repetition_case3(self):
        # Set up mock form data
        self.form.cleaned_data['easiness_factor_remembering'] = 1
        self.form.cleaned_data['repetition'] = 1
        self.form.cleaned_data['interval'] = 1
        self.form.cleaned_data['difficulty_remembering'] = 1

        expected_result = (0.003472222222222222, 1.3, 0.003472222222222222)
        result = spaced_repetition(self.form)

        self.assertEqual(result, expected_result)

    # Add more test cases as needed...

if __name__ == '__main__':
    unittest.main()