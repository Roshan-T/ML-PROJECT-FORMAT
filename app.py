from src.mlproject.logger import logging
from src.mlproject.expection import CustomException
import sys
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig
from src.mlproject.components.data_transformation import DataTransformation
from src.mlproject.components.data_ingestion import DataIngestionConfig

if __name__ == "__main__":
    logging.info("The excution has started")
    
    try:
        # data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        train_data_path , test_data_path =  data_ingestion.initiate_data_ingestion()
        data_tranformation =DataTransformation()
        data_tranformation.initiate_data_transformation(train_data_path , test_data_path)
        
        
    except Exception as e:
            raise CustomException(e, sys)