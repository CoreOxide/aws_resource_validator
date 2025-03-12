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
from aws_resource_validator.pydantic_models.healthlake_constants import *

class IdentityProviderConfigurationTypeDef(BaseValidatorModel):
    AuthorizationStrategy: AuthorizationStrategyType
    FineGrainedAuthorizationEnabled: Optional[bool] = None
    Metadata: Optional[str] = None
    IdpLambdaArn: Optional[str] = None


class PreloadDataConfigTypeDef(BaseValidatorModel):
    PreloadDataType: Literal["SYNTHEA"]


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ErrorCauseTypeDef(BaseValidatorModel):
    ErrorMessage: Optional[str] = None
    ErrorCategory: Optional[ErrorCategoryType] = None


class DeleteFHIRDatastoreRequestTypeDef(BaseValidatorModel):
    DatastoreId: str


class DescribeFHIRDatastoreRequestTypeDef(BaseValidatorModel):
    DatastoreId: str


class DescribeFHIRExportJobRequestTypeDef(BaseValidatorModel):
    DatastoreId: str
    JobId: str


class DescribeFHIRImportJobRequestTypeDef(BaseValidatorModel):
    DatastoreId: str
    JobId: str


class InputDataConfigTypeDef(BaseValidatorModel):
    S3Uri: Optional[str] = None


class JobProgressReportTypeDef(BaseValidatorModel):
    TotalNumberOfScannedFiles: Optional[int] = None
    TotalSizeOfScannedFilesInMB: Optional[float] = None
    TotalNumberOfImportedFiles: Optional[int] = None
    TotalNumberOfResourcesScanned: Optional[int] = None
    TotalNumberOfResourcesImported: Optional[int] = None
    TotalNumberOfResourcesWithCustomerError: Optional[int] = None
    TotalNumberOfFilesReadWithCustomerError: Optional[int] = None
    Throughput: Optional[float] = None


class KmsEncryptionConfigTypeDef(BaseValidatorModel):
    CmkType: CmkTypeType
    KmsKeyId: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str


class S3ConfigurationTypeDef(BaseValidatorModel):
    S3Uri: str
    KmsKeyId: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]


class CreateFHIRDatastoreResponseTypeDef(BaseValidatorModel):
    DatastoreId: str
    DatastoreArn: str
    DatastoreStatus: DatastoreStatusType
    DatastoreEndpoint: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteFHIRDatastoreResponseTypeDef(BaseValidatorModel):
    DatastoreId: str
    DatastoreArn: str
    DatastoreStatus: DatastoreStatusType
    DatastoreEndpoint: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class StartFHIRExportJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    JobStatus: JobStatusType
    DatastoreId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartFHIRImportJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    JobStatus: JobStatusType
    DatastoreId: str
    ResponseMetadata: ResponseMetadataTypeDef


class TimestampTypeDef(BaseValidatorModel):
    pass


class DatastoreFilterTypeDef(BaseValidatorModel):
    DatastoreName: Optional[str] = None
    DatastoreStatus: Optional[DatastoreStatusType] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    CreatedAfter: Optional[TimestampTypeDef] = None


class ListFHIRExportJobsRequestTypeDef(BaseValidatorModel):
    DatastoreId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmittedBefore: Optional[TimestampTypeDef] = None
    SubmittedAfter: Optional[TimestampTypeDef] = None


class ListFHIRImportJobsRequestTypeDef(BaseValidatorModel):
    DatastoreId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmittedBefore: Optional[TimestampTypeDef] = None
    SubmittedAfter: Optional[TimestampTypeDef] = None


class SseConfigurationTypeDef(BaseValidatorModel):
    KmsEncryptionConfig: KmsEncryptionConfigTypeDef


class OutputDataConfigTypeDef(BaseValidatorModel):
    S3Configuration: Optional[S3ConfigurationTypeDef] = None


class ListFHIRDatastoresRequestTypeDef(BaseValidatorModel):
    Filter: Optional[DatastoreFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class CreateFHIRDatastoreRequestTypeDef(BaseValidatorModel):
    DatastoreTypeVersion: Literal["R4"]
    DatastoreName: Optional[str] = None
    SseConfiguration: Optional[SseConfigurationTypeDef] = None
    PreloadDataConfig: Optional[PreloadDataConfigTypeDef] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    IdentityProviderConfiguration: Optional[IdentityProviderConfigurationTypeDef] = None


class DatastorePropertiesTypeDef(BaseValidatorModel):
    DatastoreId: str
    DatastoreArn: str
    DatastoreStatus: DatastoreStatusType
    DatastoreTypeVersion: Literal["R4"]
    DatastoreEndpoint: str
    DatastoreName: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    SseConfiguration: Optional[SseConfigurationTypeDef] = None
    PreloadDataConfig: Optional[PreloadDataConfigTypeDef] = None
    IdentityProviderConfiguration: Optional[IdentityProviderConfigurationTypeDef] = None
    ErrorCause: Optional[ErrorCauseTypeDef] = None


class ExportJobPropertiesTypeDef(BaseValidatorModel):
    JobId: str
    JobStatus: JobStatusType
    SubmitTime: datetime
    DatastoreId: str
    OutputDataConfig: OutputDataConfigTypeDef
    JobName: Optional[str] = None
    EndTime: Optional[datetime] = None
    DataAccessRoleArn: Optional[str] = None
    Message: Optional[str] = None


class ImportJobPropertiesTypeDef(BaseValidatorModel):
    JobId: str
    JobStatus: JobStatusType
    SubmitTime: datetime
    DatastoreId: str
    InputDataConfig: InputDataConfigTypeDef
    JobName: Optional[str] = None
    EndTime: Optional[datetime] = None
    JobOutputDataConfig: Optional[OutputDataConfigTypeDef] = None
    JobProgressReport: Optional[JobProgressReportTypeDef] = None
    DataAccessRoleArn: Optional[str] = None
    Message: Optional[str] = None


class StartFHIRExportJobRequestTypeDef(BaseValidatorModel):
    OutputDataConfig: OutputDataConfigTypeDef
    DatastoreId: str
    DataAccessRoleArn: str
    JobName: Optional[str] = None
    ClientToken: Optional[str] = None


class StartFHIRImportJobRequestTypeDef(BaseValidatorModel):
    InputDataConfig: InputDataConfigTypeDef
    JobOutputDataConfig: OutputDataConfigTypeDef
    DatastoreId: str
    DataAccessRoleArn: str
    JobName: Optional[str] = None
    ClientToken: Optional[str] = None


class DescribeFHIRDatastoreResponseTypeDef(BaseValidatorModel):
    DatastoreProperties: DatastorePropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListFHIRDatastoresResponseTypeDef(BaseValidatorModel):
    DatastorePropertiesList: List[DatastorePropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeFHIRExportJobResponseTypeDef(BaseValidatorModel):
    ExportJobProperties: ExportJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListFHIRExportJobsResponseTypeDef(BaseValidatorModel):
    ExportJobPropertiesList: List[ExportJobPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeFHIRImportJobResponseTypeDef(BaseValidatorModel):
    ImportJobProperties: ImportJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListFHIRImportJobsResponseTypeDef(BaseValidatorModel):
    ImportJobPropertiesList: List[ImportJobPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


