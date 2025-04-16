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
from aws_resource_validator.pydantic_models.importexport_constants import *

class Artifact(BaseValidatorModel):
    Description: Optional[str] = None
    URL: Optional[str] = None


class CancelJobInput(BaseValidatorModel):
    JobId: str
    APIVersion: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateJobInput(BaseValidatorModel):
    JobType: JobTypeType
    Manifest: str
    ValidateOnly: bool
    ManifestAddendum: Optional[str] = None
    APIVersion: Optional[str] = None


class GetShippingLabelInput(BaseValidatorModel):
    jobIds: Sequence[str]
    name: Optional[str] = None
    company: Optional[str] = None
    phoneNumber: Optional[str] = None
    country: Optional[str] = None
    stateOrProvince: Optional[str] = None
    city: Optional[str] = None
    postalCode: Optional[str] = None
    street1: Optional[str] = None
    street2: Optional[str] = None
    street3: Optional[str] = None
    APIVersion: Optional[str] = None


class GetStatusInput(BaseValidatorModel):
    JobId: str
    APIVersion: Optional[str] = None


class Job(BaseValidatorModel):
    JobId: Optional[str] = None
    CreationDate: Optional[datetime] = None
    IsCanceled: Optional[bool] = None
    JobType: Optional[JobTypeType] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListJobsInput(BaseValidatorModel):
    MaxJobs: Optional[int] = None
    Marker: Optional[str] = None
    APIVersion: Optional[str] = None


class UpdateJobInput(BaseValidatorModel):
    JobId: str
    Manifest: str
    JobType: JobTypeType
    ValidateOnly: bool
    APIVersion: Optional[str] = None


class CancelJobOutput(BaseValidatorModel):
    Success: bool
    ResponseMetadata: ResponseMetadata


class CreateJobOutput(BaseValidatorModel):
    JobId: str
    JobType: JobTypeType
    Signature: str
    SignatureFileContents: str
    WarningMessage: str
    ArtifactList: List[Artifact]
    ResponseMetadata: ResponseMetadata


class GetStatusOutput(BaseValidatorModel):
    JobId: str
    JobType: JobTypeType
    LocationCode: str
    LocationMessage: str
    ProgressCode: str
    ProgressMessage: str
    Carrier: str
    TrackingNumber: str
    LogBucket: str
    LogKey: str
    ErrorCount: int
    Signature: str
    SignatureFileContents: str
    CurrentManifest: str
    CreationDate: datetime
    ArtifactList: List[Artifact]
    ResponseMetadata: ResponseMetadata


class UpdateJobOutput(BaseValidatorModel):
    Success: bool
    WarningMessage: str
    ArtifactList: List[Artifact]
    ResponseMetadata: ResponseMetadata


class ListJobsOutput(BaseValidatorModel):
    Jobs: List[Job]
    IsTruncated: bool
    ResponseMetadata: ResponseMetadata


class ListJobsInputPaginate(BaseValidatorModel):
    APIVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


