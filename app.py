from src.mlproject.logger import logging
from src.mlproject.expection import CustomException
import sys
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig
from src.mlproject.components.data_transformation import DataTransformation
from src.mlproject.components.data_ingestion import DataIngestionConfig
from src.mlproject.components.model_trainer import ModelTrainer, ModelTrainerConfig
if __name__ == "__main__":
    logging.info("The excution has started")
    
    try:
        # data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        train_data_path , test_data_path =  data_ingestion.initiate_data_ingestion()
        
        data_tranformation =DataTransformation()
        train_arr , test_arr, _  = data_tranformation.initiate_data_transformation(train_data_path , test_data_path)
        
        model_trainer =  ModelTrainer()
        r2square = model_trainer.initiate_model_trainer(train_arr , test_arr)
        print(r2square)
        
    except Exception as e:
            raise CustomException(e, sys)