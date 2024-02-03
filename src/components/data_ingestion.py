import os
import sys #because we are using custom exception
from src.exception import CustomException # inside src folder we have exception file
from src.logger import logging # inside src folder we have logging file
import pandas as pd # we have to work with dataframe
from sklearn.model_selection import train_test_split
from dataclasses import dataclass # this is in python 3.9, this is used to create class variables
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig


#from src.components.model_trainer import ModelTrainerConfig
#from src.components.model_trainer import ModelTrainer

# When ever we are performing data ingestion component there should be some input that may be required by data ingestion component , the input can be 
# like where we want to save the training data , test data , raw data and we keep it in new class. In data ingestion component any input we would be requiring 
# we would keep them provide through this component. The decorator dataclass is amazing because inside a class to define the class variables we use init
# but if we use dataclass we will be able to define the class variables. we can ise dataclass when we define variables only 
# if we have functions too then go for def __init__(self) way
@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")
    
    
class DataIngestion:
    def __init__(self):
        # when we call DataIngestionConfig the 3 path would get saved
        self.ingestion_config = DataIngestionConfig()
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # here we can read data from any where
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info('Train Test split initiated')
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Ingesion of data is completed")
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        
        
if __name__ == "__main__":
    obj=DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
    
    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data, test_data)                    


