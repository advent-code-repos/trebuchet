from config.logger import logger

class CalibrationService:
  def __init__(self, document):
    self.calibration_value = 0
    self.document = document
  
  def recalibrate(self):
    logger.info(f"starts with: {self.document}")
    with open(self.document, 'r') as file:
      for line in file:
        self.calibration_value += 1
        line = line.strip()
        logger.debug(f'line is: {line}')
    return self.calibration_value