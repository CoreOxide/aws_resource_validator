from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.marketplacecommerceanalytics.marketplacecommerceanalytics_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream



Timestamp = Union[datetime, str]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class GenerateDataSetRequest(BaseValidatorModel):
    dataSetType: DataSetTypeType
    dataSetPublicationDate: Timestamp
    roleNameArn: str
    destinationS3BucketName: str
    snsTopicArn: str
    destinationS3Prefix: Optional[str] = None
    customerDefinedValues: Optional[Dict[str, str]] = None


class StartSupportDataExportRequest(BaseValidatorModel):
    dataSetType: SupportDataSetTypeType
    fromDate: Timestamp
    roleNameArn: str
    destinationS3BucketName: str
    snsTopicArn: str
    destinationS3Prefix: Optional[str] = None
    customerDefinedValues: Optional[Dict[str, str]] = None


class GenerateDataSetResult(BaseValidatorModel):
    dataSetRequestId: str
    ResponseMetadata: ResponseMetadata


class StartSupportDataExportResult(BaseValidatorModel):
    dataSetRequestId: str
    ResponseMetadata: ResponseMetadata