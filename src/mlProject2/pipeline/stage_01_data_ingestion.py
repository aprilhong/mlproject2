from mlProject2.config.configuration import ConfigurationManager
from mlProject2.components.data_ingestion import DataIngestion
from mlProject2 import logger   


STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

# Initiate Pipeline
if __name__ == '__main__':
    try: 
        logger.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<')
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>> stage {STAGE_NAME} completed <<<<<<\n\n x============x')
    except Exception as e:
        logger.exception(e)
        raise e
