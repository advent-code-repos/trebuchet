from config.logger import logger
from services.calibration_services import CalibrationService


class CalibrationManager:
    def __init__(self, calibration_service: CalibrationService, logger):
        self.calibration_service = calibration_service
        self.logger = logger

    def start_calibration(self, document: str, with_letters: bool):
        calibration_value = self.calibration_service.recalibrate(
            document, with_letters
        )
        logger.info(
            "Recalibration is terminate with this "
            f"calibration value: {calibration_value}"
        )

        return calibration_value
