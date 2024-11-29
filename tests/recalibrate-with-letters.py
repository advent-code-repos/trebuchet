import unittest

from config.logger import logger
from services.calibration_services import CalibrationService


class TestProcessInput(unittest.TestCase):
    def test_success(self):
        input_string = "eighttkbtzjz6nineeight"
        calibration_service = CalibrationService(logger)
        result = calibration_service._get_extract_token_number(input_string)
        self.assertEqual(result, 88)


if __name__ == "__main__":
    unittest.main()
