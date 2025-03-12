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
from aws_resource_validator.pydantic_models.iot_jobs_data_constants import *

class DescribeJobExecutionRequestTypeDef(BaseValidatorModel):
    jobId: str
    thingName: str
    includeJobDocument: Optional[bool] = None
    executionNumber: Optional[int] = None


class JobExecutionTypeDef(BaseValidatorModel):
    jobId: Optional[str] = None
    thingName: Optional[str] = None
    status: Optional[JobExecutionStatusType] = None
    statusDetails: Optional[Dict[str, str]] = None
    queuedAt: Optional[int] = None
    startedAt: Optional[int] = None
    lastUpdatedAt: Optional[int] = None
    approximateSecondsBeforeTimedOut: Optional[int] = None
    versionNumber: Optional[int] = None
    executionNumber: Optional[int] = None
    jobDocument: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class GetPendingJobExecutionsRequestTypeDef(BaseValidatorModel):
    thingName: str


class JobExecutionSummaryTypeDef(BaseValidatorModel):
    jobId: Optional[str] = None
    queuedAt: Optional[int] = None
    startedAt: Optional[int] = None
    lastUpdatedAt: Optional[int] = None
    versionNumber: Optional[int] = None
    executionNumber: Optional[int] = None


class JobExecutionStateTypeDef(BaseValidatorModel):
    status: Optional[JobExecutionStatusType] = None
    statusDetails: Optional[Dict[str, str]] = None
    versionNumber: Optional[int] = None


class StartNextPendingJobExecutionRequestTypeDef(BaseValidatorModel):
    thingName: str
    statusDetails: Optional[Mapping[str, str]] = None
    stepTimeoutInMinutes: Optional[int] = None


class UpdateJobExecutionRequestTypeDef(BaseValidatorModel):
    jobId: str
    thingName: str
    status: JobExecutionStatusType
    statusDetails: Optional[Mapping[str, str]] = None
    stepTimeoutInMinutes: Optional[int] = None
    expectedVersion: Optional[int] = None
    includeJobExecutionState: Optional[bool] = None
    includeJobDocument: Optional[bool] = None
    executionNumber: Optional[int] = None


class BlobTypeDef(BaseValidatorModel):
    pass


class CommandParameterValueTypeDef(BaseValidatorModel):
    S: Optional[str] = None
    B: Optional[bool] = None
    I: Optional[int] = None
    L: Optional[int] = None
    D: Optional[float] = None
    BIN: Optional[BlobTypeDef] = None
    UL: Optional[str] = None


class DescribeJobExecutionResponseTypeDef(BaseValidatorModel):
    execution: JobExecutionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StartCommandExecutionResponseTypeDef(BaseValidatorModel):
    executionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartNextPendingJobExecutionResponseTypeDef(BaseValidatorModel):
    execution: JobExecutionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetPendingJobExecutionsResponseTypeDef(BaseValidatorModel):
    inProgressJobs: List[JobExecutionSummaryTypeDef]
    queuedJobs: List[JobExecutionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateJobExecutionResponseTypeDef(BaseValidatorModel):
    executionState: JobExecutionStateTypeDef
    jobDocument: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartCommandExecutionRequestTypeDef(BaseValidatorModel):
    targetArn: str
    commandArn: str
    parameters: Optional[Mapping[str, CommandParameterValueTypeDef]] = None
    executionTimeoutSeconds: Optional[int] = None
    clientToken: Optional[str] = None


