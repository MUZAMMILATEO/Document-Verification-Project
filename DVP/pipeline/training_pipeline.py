import sys
from DVP.exception import USvisaException
from DVP.logger import logging
from DVP.components.data_ingestion import DataIngestion
from DVP.components.data_validation import DataValidation
# from DVP.components.data_transformation import DataTransformation
# from DVP.components.model_trainer import ModelTrainer
# from DVP.components.model_evaluation import ModelEvaluation
# from DVP.components.model_pusher import ModelPusher


from DVP.entity.config_entity import (DataIngestionConfig,
                                          DataValidationConfig,)
#                                          DataTransformationConfig,
#                                          ModelTrainerConfig,
#                                          ModelEvaluationConfig,
#                                          ModelPusherConfig)
# 
from DVP.entity.artifact_entity import (DataIngestionArtifact,
                                             DataValidationArtifact,)
#                                             DataTransformationArtifact,
#                                             ModelTrainerArtifact,
#                                             ModelEvaluationArtifact,
#                                             ModelPusherArtifact)


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()
        # self.data_transformation_config = DataTransformationConfig()
        # self.model_trainer_config = ModelTrainerConfig()
        # self.model_evaluation_config = ModelEvaluationConfig()
        # self.model_pusher_config = ModelPusherConfig()


    
    def start_data_ingestion(self) -> DataIngestionArtifact:
        """
        This method of TrainPipeline class is responsible for starting data ingestion component
        """
        try:
            logging.info("Entered the start_data_ingestion method of TrainPipeline class")
            logging.info("Getting the data from mongodb")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the train_set and test_set from mongodb")
            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )
            return data_ingestion_artifact
        except Exception as e:
            raise USvisaException(e, sys) from e

    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        """
        This method of TrainPipeline class is responsible for starting data validation component
        """
        logging.info("Entered the start_data_validation method of TrainPipeline class")

        try:
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,
                                             data_validation_config=self.data_validation_config
                                             )

            data_validation_artifact = data_validation.initiate_data_validation()

            logging.info("Performed the data validation operation")

            logging.info(
                "Exited the start_data_validation method of TrainPipeline class"
            )

            return data_validation_artifact

        except Exception as e:
            raise USvisaException(e, sys) from e



    def run_pipeline(self, ) -> None:
        """
        This method of TrainPipeline class is responsible for running complete pipeline
        """
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)

        except Exception as e:
            raise USvisaException(e, sys)
        
