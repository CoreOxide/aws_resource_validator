from datetime import datetime
from pydantic import BaseModel
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

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class GenerateDataSetRequestRequestTypeDef(BaseModel):
    dataSetType: DataSetTypeType
    dataSetPublicationDate: TimestampTypeDef
    roleNameArn: str
    destinationS3BucketName: str
    snsTopicArn: str
    destinationS3Prefix: Optional[str] = None
    customerDefinedValues: Optional[Mapping[str, str]] = None

class StartSupportDataExportRequestRequestTypeDef(BaseModel):
    dataSetType: SupportDataSetTypeType
    fromDate: TimestampTypeDef
    roleNameArn: str
    destinationS3BucketName: str
    snsTopicArn: str
    destinationS3Prefix: Optional[str] = None
    customerDefinedValues: Optional[Mapping[str, str]] = None

class GenerateDataSetResultTypeDef(BaseModel):
    dataSetRequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartSupportDataExportResultTypeDef(BaseModel):
    dataSetRequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

