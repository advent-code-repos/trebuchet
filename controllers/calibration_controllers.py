from config.logger import logger
from managers.calibration_manager import CalibrationManager


class CalibrationController:
    def __init__(self, calibration_manager: CalibrationManager, logger):
        self.calibration_manager = calibration_manager
        self.logger = logger

    def run_calibration_by(self, document: str, part):
        logger.info(f"uses document: {document} and part: {part}")

        match part:
            case 1:
                return self.calibration_manager.start_calibration(
                    document, False
                )
            case 2:
                return self.calibration_manager.start_calibration(
                    document, True
                )
            case _:
                raise Exception(f"Choice not valid!: {part}")
