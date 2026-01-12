from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


try:
    logger.info(f">>>>>>>  stage {}