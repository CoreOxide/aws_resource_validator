from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.marketplacecommerceanalytics_constants import *

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class GenerateDataSetRequestRequestTypeDef(BaseValidatorModel):
    dataSetType: DataSetTypeType
    dataSetPublicationDate: TimestampTypeDef
    roleNameArn: str
    destinationS3BucketName: str
    snsTopicArn: str
    destinationS3Prefix: Optional[str] = None
    customerDefinedValues: Optional[Mapping[str, str]] = None

class StartSupportDataExportRequestRequestTypeDef(BaseValidatorModel):
    dataSetType: SupportDataSetTypeType
    fromDate: TimestampTypeDef
    roleNameArn: str
    destinationS3BucketName: str
    snsTopicArn: str
    destinationS3Prefix: Optional[str] = None
    customerDefinedValues: Optional[Mapping[str, str]] = None

class GenerateDataSetResultTypeDef(BaseValidatorModel):
    dataSetRequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartSupportDataExportResultTypeDef(BaseValidatorModel):
    dataSetRequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

