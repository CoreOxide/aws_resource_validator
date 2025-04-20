from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.iot_jobs_data.iot_jobs_data_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream



Blob = Union[str, bytes, IO[Any], StreamingBody]


class DescribeJobExecutionRequest(BaseValidatorModel):
    jobId: str
    thingName: str
    includeJobDocument: Optional[bool] = None
    executionNumber: Optional[int] = None


class JobExecution(BaseValidatorModel):
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


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class GetPendingJobExecutionsRequest(BaseValidatorModel):
    thingName: str


class JobExecutionSummary(BaseValidatorModel):
    jobId: Optional[str] = None
    queuedAt: Optional[int] = None
    startedAt: Optional[int] = None
    lastUpdatedAt: Optional[int] = None
    versionNumber: Optional[int] = None
    executionNumber: Optional[int] = None


class JobExecutionState(BaseValidatorModel):
    status: Optional[JobExecutionStatusType] = None
    statusDetails: Optional[Dict[str, str]] = None
    versionNumber: Optional[int] = None


class StartNextPendingJobExecutionRequest(BaseValidatorModel):
    thingName: str
    statusDetails: Optional[Dict[str, str]] = None
    stepTimeoutInMinutes: Optional[int] = None


class UpdateJobExecutionRequest(BaseValidatorModel):
    jobId: str
    thingName: str
    status: JobExecutionStatusType
    statusDetails: Optional[Dict[str, str]] = None
    stepTimeoutInMinutes: Optional[int] = None
    expectedVersion: Optional[int] = None
    includeJobExecutionState: Optional[bool] = None
    includeJobDocument: Optional[bool] = None
    executionNumber: Optional[int] = None


class CommandParameterValue(BaseValidatorModel):
    S: Optional[str] = None
    B: Optional[bool] = None
    I: Optional[int] = None
    L: Optional[int] = None
    D: Optional[float] = None
    BIN: Optional[Blob] = None
    UL: Optional[str] = None


class DescribeJobExecutionResponse(BaseValidatorModel):
    execution: JobExecution
    ResponseMetadata: ResponseMetadata


class StartCommandExecutionResponse(BaseValidatorModel):
    executionId: str
    ResponseMetadata: ResponseMetadata


class StartNextPendingJobExecutionResponse(BaseValidatorModel):
    execution: JobExecution
    ResponseMetadata: ResponseMetadata


class GetPendingJobExecutionsResponse(BaseValidatorModel):
    inProgressJobs: List[JobExecutionSummary]
    queuedJobs: List[JobExecutionSummary]
    ResponseMetadata: ResponseMetadata


class UpdateJobExecutionResponse(BaseValidatorModel):
    executionState: JobExecutionState
    jobDocument: str
    ResponseMetadata: ResponseMetadata


class StartCommandExecutionRequest(BaseValidatorModel):
    targetArn: str
    commandArn: str
    parameters: Optional[Dict[str, CommandParameterValue]] = None
    executionTimeoutSeconds: Optional[int] = None
    clientToken: Optional[str] = None