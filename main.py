from config.enums import AdventCalendar, AdventPart
from config.logger import logger
from models.day_model import DayModel
from services.day_services import DayService


def main():
    logger.info("Advent Calendar 2023 starts")

    document = "calibration-document.example"

    day = DayModel(AdventCalendar.TREBUCHET, AdventPart.FIRST)
    DayService(day).start(document)


#  document = "calibration-document-spelled-out-letters.example"
#
#  calibration_service = CalibrationService(document)
#  logger.info("CalibrationService initiated")

#  calibration_value = calibration_service.recalibrate(False)
#  logger.info(
#      "Recalibration is terminate with this "
#      f"calibration value: {calibration_value}"
#  )


if __name__ == "__main__":
    main()
