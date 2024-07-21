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
from aws_resource_validator.pydantic_models.importexport_constants import *

class ArtifactTypeDef(BaseModel):
    Description: Optional[str] = None
    URL: Optional[str] = None

class CancelJobInputRequestTypeDef(BaseModel):
    JobId: str
    APIVersion: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateJobInputRequestTypeDef(BaseModel):
    JobType: JobTypeType
    Manifest: str
    ValidateOnly: bool
    ManifestAddendum: Optional[str] = None
    APIVersion: Optional[str] = None

class GetShippingLabelInputRequestTypeDef(BaseModel):
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

class GetStatusInputRequestTypeDef(BaseModel):
    JobId: str
    APIVersion: Optional[str] = None

class JobTypeDef(BaseModel):
    JobId: Optional[str] = None
    CreationDate: Optional[datetime] = None
    IsCanceled: Optional[bool] = None
    JobType: Optional[JobTypeType] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListJobsInputRequestTypeDef(BaseModel):
    MaxJobs: Optional[int] = None
    Marker: Optional[str] = None
    APIVersion: Optional[str] = None

class UpdateJobInputRequestTypeDef(BaseModel):
    JobId: str
    Manifest: str
    JobType: JobTypeType
    ValidateOnly: bool
    APIVersion: Optional[str] = None

class CancelJobOutputTypeDef(BaseModel):
    Success: bool
    ResponseMetadata: ResponseMetadataTypeDef

class CreateJobOutputTypeDef(BaseModel):
    JobId: str
    JobType: JobTypeType
    Signature: str
    SignatureFileContents: str
    WarningMessage: str
    ArtifactList: List[ArtifactTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetShippingLabelOutputTypeDef(BaseModel):
    ShippingLabelURL: str
    Warning: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetStatusOutputTypeDef(BaseModel):
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
    ArtifactList: List[ArtifactTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateJobOutputTypeDef(BaseModel):
    Success: bool
    WarningMessage: str
    ArtifactList: List[ArtifactTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobsOutputTypeDef(BaseModel):
    Jobs: List[JobTypeDef]
    IsTruncated: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobsInputListJobsPaginateTypeDef(BaseModel):
    APIVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

