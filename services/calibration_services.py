from config.logger import logger


class CalibrationService:
    def __init__(self, logger):
        self.logger = logger

        self.calibration_value = 0

    def recalibrate(self, document: str, with_letters: bool):
        self._reset_calibration_value()
        logger.info(
            f"starts with: {document} "
            f"and calibration_value {self.calibration_value} "
            f"and with_letters? {with_letters}"
        )

        with open(document, "r") as file:
            for line in file:
                line = line.strip()
                logger.debug(f"line is: {line}")
                extract_value = self._get_extract_value(line)
                logger.debug(f"extract value is: {extract_value}")
                self.calibration_value += extract_value
        return self.calibration_value

    def _get_extract_value(self, value: str):
        digits = [ch for ch in value if ch.isdigit()]

        return (
            int(digits[0] + digits[-1])
            if len(digits) > 1
            else int(digits[0] * 2)
        )

    def _reset_calibration_value(self):
        self.calibration_value = 0
