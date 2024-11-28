from config.logger import logger
from models.day_model import DayModel
from services.calibration_services import CalibrationService


class DayService:
    def __init__(self, day: DayModel):
        self.day = day

    def start(self, document: str):
        calibration_service = CalibrationService(document)
        logger.info("CalibrationService initiated")

        calibration_value = calibration_service.recalibrate()
        logger.info(
            "Recalibration is terminate with this "
            f"calibration value: {calibration_value}"
        )
