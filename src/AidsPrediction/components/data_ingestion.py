import os
from AidsPrediction.logging import logger
from AidsPrediction.utils.common import get_size
from AidsPrediction.entity import DataIngestionConfig
from pathlib import Path
import shutil


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            data_path = os.path.join("research", "data", "data.csv")
            filename = self.config.local_data_file
            shutil.copy(data_path, filename)
            logger.info(f"Downloaded file {filename}")
        else:
            logger.info(
                f"file already exists of size: {get_size(Path(self.config.local_data_file))} KB"
            )
