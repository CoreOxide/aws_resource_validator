from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.healthlake.healthlake_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class IdentityProviderConfiguration(BaseValidatorModel):
    AuthorizationStrategy: AuthorizationStrategyType
    FineGrainedAuthorizationEnabled: Optional[bool] = None
    Metadata: Optional[str] = None
    IdpLambdaArn: Optional[str] = None


class PreloadDataConfig(BaseValidatorModel):
    PreloadDataType: Literal['SYNTHEA']


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

Timestamp = Union[datetime, str]


class ErrorCause(BaseValidatorModel):
    ErrorMessage: Optional[str] = None
    ErrorCategory: Optional[ErrorCategoryType] = None


# This class is the input for the 'delete_fhir_datastore' function.
class DeleteFHIRDatastoreRequest(BaseValidatorModel):
    DatastoreId: str


# This class is the input for the 'describe_fhir_datastore' function.
class DescribeFHIRDatastoreRequest(BaseValidatorModel):
    DatastoreId: str


# This class is the input for the 'describe_fhir_export_job' function.
class DescribeFHIRExportJobRequest(BaseValidatorModel):
    DatastoreId: str
    JobId: str


# This class is the input for the 'describe_fhir_import_job' function.
class DescribeFHIRImportJobRequest(BaseValidatorModel):
    DatastoreId: str
    JobId: str


class InputDataConfig(BaseValidatorModel):
    S3Uri: Optional[str] = None


class JobProgressReport(BaseValidatorModel):
    TotalNumberOfScannedFiles: Optional[int] = None
    TotalSizeOfScannedFilesInMB: Optional[float] = None
    TotalNumberOfImportedFiles: Optional[int] = None
    TotalNumberOfResourcesScanned: Optional[int] = None
    TotalNumberOfResourcesImported: Optional[int] = None
    TotalNumberOfResourcesWithCustomerError: Optional[int] = None
    TotalNumberOfFilesReadWithCustomerError: Optional[int] = None
    Throughput: Optional[float] = None


class KmsEncryptionConfig(BaseValidatorModel):
    CmkType: CmkTypeType
    KmsKeyId: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


class S3Configuration(BaseValidatorModel):
    S3Uri: str
    KmsKeyId: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: List[str]


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: List[Tag]


# This class is the output for the 'create_fhir_datastore' function.
class CreateFHIRDatastoreResponse(BaseValidatorModel):
    DatastoreId: str
    DatastoreArn: str
    DatastoreStatus: DatastoreStatusType
    DatastoreEndpoint: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_fhir_datastore' function.
class DeleteFHIRDatastoreResponse(BaseValidatorModel):
    DatastoreId: str
    DatastoreArn: str
    DatastoreStatus: DatastoreStatusType
    DatastoreEndpoint: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_fhir_export_job' function.
class StartFHIRExportJobResponse(BaseValidatorModel):
    JobId: str
    JobStatus: JobStatusType
    DatastoreId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_fhir_import_job' function.
class StartFHIRImportJobResponse(BaseValidatorModel):
    JobId: str
    JobStatus: JobStatusType
    DatastoreId: str
    ResponseMetadata: ResponseMetadata


class DatastoreFilter(BaseValidatorModel):
    DatastoreName: Optional[str] = None
    DatastoreStatus: Optional[DatastoreStatusType] = None
    CreatedBefore: Optional[Timestamp] = None
    CreatedAfter: Optional[Timestamp] = None


# This class is the input for the 'list_fhir_export_jobs' function.
class ListFHIRExportJobsRequest(BaseValidatorModel):
    DatastoreId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmittedBefore: Optional[Timestamp] = None
    SubmittedAfter: Optional[Timestamp] = None


# This class is the input for the 'list_fhir_import_jobs' function.
class ListFHIRImportJobsRequest(BaseValidatorModel):
    DatastoreId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmittedBefore: Optional[Timestamp] = None
    SubmittedAfter: Optional[Timestamp] = None


class SseConfiguration(BaseValidatorModel):
    KmsEncryptionConfig: KmsEncryptionConfig


class OutputDataConfig(BaseValidatorModel):
    S3Configuration: Optional[S3Configuration] = None


# This class is the input for the 'list_fhir_datastores' function.
class ListFHIRDatastoresRequest(BaseValidatorModel):
    Filter: Optional[DatastoreFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'create_fhir_datastore' function.
class CreateFHIRDatastoreRequest(BaseValidatorModel):
    DatastoreTypeVersion: Literal['R4']
    DatastoreName: Optional[str] = None
    SseConfiguration: Optional[SseConfiguration] = None
    PreloadDataConfig: Optional[PreloadDataConfig] = None
    ClientToken: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    IdentityProviderConfiguration: Optional[IdentityProviderConfiguration] = None


class DatastoreProperties(BaseValidatorModel):
    DatastoreId: str
    DatastoreArn: str
    DatastoreStatus: DatastoreStatusType
    DatastoreTypeVersion: Literal['R4']
    DatastoreEndpoint: str
    DatastoreName: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    SseConfiguration: Optional[SseConfiguration] = None
    PreloadDataConfig: Optional[PreloadDataConfig] = None
    IdentityProviderConfiguration: Optional[IdentityProviderConfiguration] = None
    ErrorCause: Optional[ErrorCause] = None


class ExportJobProperties(BaseValidatorModel):
    JobId: str
    JobStatus: JobStatusType
    SubmitTime: datetime
    DatastoreId: str
    OutputDataConfig: OutputDataConfig
    JobName: Optional[str] = None
    EndTime: Optional[datetime] = None
    DataAccessRoleArn: Optional[str] = None
    Message: Optional[str] = None


class ImportJobProperties(BaseValidatorModel):
    JobId: str
    JobStatus: JobStatusType
    SubmitTime: datetime
    DatastoreId: str
    InputDataConfig: InputDataConfig
    JobName: Optional[str] = None
    EndTime: Optional[datetime] = None
    JobOutputDataConfig: Optional[OutputDataConfig] = None
    JobProgressReport: Optional[JobProgressReport] = None
    DataAccessRoleArn: Optional[str] = None
    Message: Optional[str] = None


# This class is the input for the 'start_fhir_export_job' function.
class StartFHIRExportJobRequest(BaseValidatorModel):
    OutputDataConfig: OutputDataConfig
    DatastoreId: str
    DataAccessRoleArn: str
    JobName: Optional[str] = None
    ClientToken: Optional[str] = None


# This class is the input for the 'start_fhir_import_job' function.
class StartFHIRImportJobRequest(BaseValidatorModel):
    InputDataConfig: InputDataConfig
    JobOutputDataConfig: OutputDataConfig
    DatastoreId: str
    DataAccessRoleArn: str
    JobName: Optional[str] = None
    ClientToken: Optional[str] = None


# This class is the output for the 'describe_fhir_datastore' function.
class DescribeFHIRDatastoreResponse(BaseValidatorModel):
    DatastoreProperties: DatastoreProperties
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_fhir_datastores' function.
class ListFHIRDatastoresResponse(BaseValidatorModel):
    DatastorePropertiesList: List[DatastoreProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_fhir_export_job' function.
class DescribeFHIRExportJobResponse(BaseValidatorModel):
    ExportJobProperties: ExportJobProperties
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_fhir_export_jobs' function.
class ListFHIRExportJobsResponse(BaseValidatorModel):
    ExportJobPropertiesList: List[ExportJobProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_fhir_import_job' function.
class DescribeFHIRImportJobResponse(BaseValidatorModel):
    ImportJobProperties: ImportJobProperties
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_fhir_import_jobs' function.
class ListFHIRImportJobsResponse(BaseValidatorModel):
    ImportJobPropertiesList: List[ImportJobProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None