from config.logger import logger


class CalibrationService:
    def __init__(self, document):
        self.calibration_value = 0
        self.document = document

    def recalibrate(self):
        logger.info(f"starts with: {self.document}")
        with open(self.document, "r") as file:
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
