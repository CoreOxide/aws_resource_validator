from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from botocore.response import StreamingBody
from datetime import datetime
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
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class GenerateDataSetRequestTypeDef(BaseValidatorModel):
    dataSetType: DataSetTypeType
    dataSetPublicationDate: TimestampTypeDef
    roleNameArn: str
    destinationS3BucketName: str
    snsTopicArn: str
    destinationS3Prefix: Optional[str] = None
    customerDefinedValues: Optional[Mapping[str, str]] = None


class StartSupportDataExportRequestTypeDef(BaseValidatorModel):
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


