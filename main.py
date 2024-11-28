from services.calibration_services import CalibrationService
from config.logger import logger

def main():
  logger.info("Advent Calendar 2023 starts")

  document = "calibration-document"
  calibration_service = CalibrationService(document) 
  logger.info("CalibrationService initiated")

  calibration_value = calibration_service.recalibrate()
  logger.info(f"Recalibration is terminate with this calibration value: {calibration_value}")

if __name__ == "__main__":
    main()