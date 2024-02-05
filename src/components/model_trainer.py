import os #
import sys #
from dataclasses import dataclass #

from catboost import CatBoostRegressor #      
from sklearn.ensemble import( #
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)

from sklearn.linear_model import LinearRegression #
from sklearn.metrics import r2_score #
from sklearn.neighbors import KNeighborsRegressor #
from sklearn.tree import DecisionTreeRegressor #
# xgboost wont work as Python 3.8 I have is 32 bit
# from xgboost import XGBRegressor

from src.exception import CustomException #
from src.logger import logging #

from src.utils import save_object, evaluate_models

# For every component we need to create config file, there we would be giving path of pickle file etc

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts","model.pkl") # after creating the model we want to create that into a pickle file
    
class ModelTrainer:#responsible for training our model
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()#inside the model_trainer_config we will get the path name coming from object in ModelTrainerConfig
            
    def initiate_model_trainer(self, train_array, test_array):# the inputs are the output from the data transformation, the last feature is target feature as mention in the data transformation
        try:
            logging.info("Split training and test input data")
            X_train, y_train, X_test, y_test = (
                train_array[:,:-1],#X_train
                train_array[:,-1],#y_train
                test_array[:,:-1],#X_test
                test_array[:,-1],#y_test
            )
            
            # Creating dictionary of models
            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "K-Neighbors Regressor": KNeighborsRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }
            
            # evaluate model is coming from utils, model_report is a dictionary
            model_report:dict = evaluate_models(X_train=X_train, y_train=y_train, X_test = X_test, y_test=y_test, models=models)
            
            # To get the best model score from dict
            best_model_score = max(sorted(model_report.values()))
            
            # To get best model name from the dict, the key is the model name
            best_model_name = list(model_report.keys())[  #model_report.keys() is a list
                list(model_report.values()).index(best_model_score) # we are creating a nested list
            ]
            best_model = models[best_model_name]
            if best_model_score < 0.6:
                raise CustomException("No best model found")
            
            logging.info(f"Best found model on both training and testing dataset")
            
            # dumping the best model in the specific path
            save_object(
                file_path = self.model_trainer_config.trained_model_file_path,
                obj = best_model
            )
            
            predicted = best_model.predict(X_test)
            
            r2_square = r2_score(y_test, predicted)
            return r2_square
        
        except Exception as e:
            raise CustomException(e,sys)