from AidsPrediction.config.configuration import ConfigurationManager
from AidsPrediction.components.data_validation import DataValidation
from AidsPrediction.logging import logger


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self) -> None:
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.validate_all_files_exist()
        logger.info("DataValidationTrainingPipeline completed successfully")
