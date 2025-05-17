from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.importexport.importexport_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class Artifact(BaseValidatorModel):
    Description: Optional[str] = None
    URL: Optional[str] = None


# This class is the input for the 'cancel_job' function.
class CancelJobInput(BaseValidatorModel):
    JobId: str
    APIVersion: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'create_job' function.
class CreateJobInput(BaseValidatorModel):
    JobType: JobTypeType
    Manifest: str
    ValidateOnly: bool
    ManifestAddendum: Optional[str] = None
    APIVersion: Optional[str] = None


# This class is the input for the 'get_shipping_label' function.
class GetShippingLabelInput(BaseValidatorModel):
    jobIds: List[str]
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


# This class is the input for the 'get_status' function.
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


# This class is the input for the 'list_jobs' function.
class ListJobsInput(BaseValidatorModel):
    MaxJobs: Optional[int] = None
    Marker: Optional[str] = None
    APIVersion: Optional[str] = None


# This class is the input for the 'update_job' function.
class UpdateJobInput(BaseValidatorModel):
    JobId: str
    Manifest: str
    JobType: JobTypeType
    ValidateOnly: bool
    APIVersion: Optional[str] = None


# This class is the output for the 'cancel_job' function.
class CancelJobOutput(BaseValidatorModel):
    Success: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_job' function.
class CreateJobOutput(BaseValidatorModel):
    JobId: str
    JobType: JobTypeType
    Signature: str
    SignatureFileContents: str
    WarningMessage: str
    ArtifactList: List[Artifact]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_shipping_label' function.
class GetShippingLabelOutput(BaseValidatorModel):
    ShippingLabelURL: str
    Warning: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_status' function.
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


# This class is the output for the 'update_job' function.
class UpdateJobOutput(BaseValidatorModel):
    Success: bool
    WarningMessage: str
    ArtifactList: List[Artifact]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_jobs' function.
class ListJobsOutput(BaseValidatorModel):
    Jobs: List[Job]
    IsTruncated: bool
    ResponseMetadata: ResponseMetadata


class ListJobsInputPaginate(BaseValidatorModel):
    APIVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None