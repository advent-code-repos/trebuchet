from config.logger import logger
from services.calibration_services import CalibrationService


def main():
    logger.info("Advent Calendar 2023 starts")

    document = "calibration-document"

    calibration_service = CalibrationService(document)
    logger.info("CalibrationService initiated")

    calibration_value = calibration_service.recalibrate()
    logger.info(
        "Recalibration is terminate with this "
        f"calibration value: {calibration_value}"
    )


if __name__ == "__main__":
    main()
