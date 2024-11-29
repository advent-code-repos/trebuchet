import re

from config.logger import logger

token_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


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
                if not with_letters:
                    extract_value = self._get_extract_value(line)
                else:
                    extract_value = self._get_extract_token_number(line)
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

    def _get_extract_token_number(self, line):
        logger.debug(f"line input: {line}")
        return self._substitute_letter_with_numbers(line)

    def _substitute_letter_with_numbers(self, line):
        words_map = {}
        for token in token_map:
            if token in line:
                indexes = self._find_occurrences(line, token)
                logger.debug(f"indexes: {indexes}")
                words_map = words_map | (
                    self._assign_indexes(indexes, token_map[token])
                )
        logger.debug(f"words_map: {words_map}")

        digits_map = {line.find(ch): int(ch) for ch in line if ch.isdigit()}
        logger.debug(f"digits_map: {digits_map}")

        numbers_map = digits_map | words_map

        if len(numbers_map) < 1:
            return 0

        numbers_map = dict(sorted(numbers_map.items()))

        min_index = min(numbers_map.keys())
        max_index = max(numbers_map.keys())

        if len(numbers_map) == 1:
            return int(
                str(numbers_map[min_index]) + str(numbers_map[min_index])
            )
        result = str(numbers_map[min_index]) + str(numbers_map[max_index])
        logger.info(f"line: {line}")
        logger.info(f"numbers_map: {numbers_map}")
        logger.info(f"result: {result}")

        return int(result)

    def _find_occurrences(self, line, token):
        return [match.start() for match in re.finditer(re.escape(token), line)]

    def _assign_indexes(self, indexes, value):
        return {i: value for i in indexes}
