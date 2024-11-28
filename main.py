from config.logger import logger
from controllers.calibration_controllers import CalibrationController
from managers.calibration_manager import CalibrationManager
from services.calibration_services import CalibrationService


def main():
    logger.info("Advent Calendar 2023 starts")

    document = "calibration-document.example"

    service = CalibrationService(logger)
    manager = CalibrationManager(service, logger)
    controller = CalibrationController(manager, logger)

    controller.run_calibration_by(document, 1)


if __name__ == "__main__":
    main()
