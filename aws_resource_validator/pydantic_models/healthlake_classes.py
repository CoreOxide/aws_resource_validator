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
from aws_resource_validator.pydantic_models.healthlake_constants import *

class IdentityProviderConfigurationTypeDef(BaseModel):
    AuthorizationStrategy: AuthorizationStrategyType
    FineGrainedAuthorizationEnabled: Optional[bool] = None
    Metadata: Optional[str] = None
    IdpLambdaArn: Optional[str] = None

class PreloadDataConfigTypeDef(BaseModel):
    PreloadDataType: Literal["SYNTHEA"]

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ErrorCauseTypeDef(BaseModel):
    ErrorMessage: Optional[str] = None
    ErrorCategory: Optional[ErrorCategoryType] = None

class DeleteFHIRDatastoreRequestRequestTypeDef(BaseModel):
    DatastoreId: str

class DescribeFHIRDatastoreRequestRequestTypeDef(BaseModel):
    DatastoreId: str

class DescribeFHIRExportJobRequestRequestTypeDef(BaseModel):
    DatastoreId: str
    JobId: str

class DescribeFHIRImportJobRequestRequestTypeDef(BaseModel):
    DatastoreId: str
    JobId: str

class InputDataConfigTypeDef(BaseModel):
    S3Uri: Optional[str] = None

class JobProgressReportTypeDef(BaseModel):
    TotalNumberOfScannedFiles: Optional[int] = None
    TotalSizeOfScannedFilesInMB: Optional[float] = None
    TotalNumberOfImportedFiles: Optional[int] = None
    TotalNumberOfResourcesScanned: Optional[int] = None
    TotalNumberOfResourcesImported: Optional[int] = None
    TotalNumberOfResourcesWithCustomerError: Optional[int] = None
    TotalNumberOfFilesReadWithCustomerError: Optional[int] = None
    Throughput: Optional[float] = None

class KmsEncryptionConfigTypeDef(BaseModel):
    CmkType: CmkTypeType
    KmsKeyId: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str

class S3ConfigurationTypeDef(BaseModel):
    S3Uri: str
    KmsKeyId: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateFHIRDatastoreResponseTypeDef(BaseModel):
    DatastoreId: str
    DatastoreArn: str
    DatastoreStatus: DatastoreStatusType
    DatastoreEndpoint: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFHIRDatastoreResponseTypeDef(BaseModel):
    DatastoreId: str
    DatastoreArn: str
    DatastoreStatus: DatastoreStatusType
    DatastoreEndpoint: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartFHIRExportJobResponseTypeDef(BaseModel):
    JobId: str
    JobStatus: JobStatusType
    DatastoreId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartFHIRImportJobResponseTypeDef(BaseModel):
    JobId: str
    JobStatus: JobStatusType
    DatastoreId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DatastoreFilterTypeDef(BaseModel):
    DatastoreName: Optional[str] = None
    DatastoreStatus: Optional[DatastoreStatusType] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    CreatedAfter: Optional[TimestampTypeDef] = None

class ListFHIRExportJobsRequestRequestTypeDef(BaseModel):
    DatastoreId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmittedBefore: Optional[TimestampTypeDef] = None
    SubmittedAfter: Optional[TimestampTypeDef] = None

class ListFHIRImportJobsRequestRequestTypeDef(BaseModel):
    DatastoreId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmittedBefore: Optional[TimestampTypeDef] = None
    SubmittedAfter: Optional[TimestampTypeDef] = None

class SseConfigurationTypeDef(BaseModel):
    KmsEncryptionConfig: KmsEncryptionConfigTypeDef

class OutputDataConfigTypeDef(BaseModel):
    S3Configuration: Optional[S3ConfigurationTypeDef] = None

class ListFHIRDatastoresRequestRequestTypeDef(BaseModel):
    Filter: Optional[DatastoreFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class CreateFHIRDatastoreRequestRequestTypeDef(BaseModel):
    DatastoreTypeVersion: Literal["R4"]
    DatastoreName: Optional[str] = None
    SseConfiguration: Optional[SseConfigurationTypeDef] = None
    PreloadDataConfig: Optional[PreloadDataConfigTypeDef] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    IdentityProviderConfiguration: Optional[IdentityProviderConfigurationTypeDef] = None

class DatastorePropertiesTypeDef(BaseModel):
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

class ExportJobPropertiesTypeDef(BaseModel):
    JobId: str
    JobStatus: JobStatusType
    SubmitTime: datetime
    DatastoreId: str
    OutputDataConfig: OutputDataConfigTypeDef
    JobName: Optional[str] = None
    EndTime: Optional[datetime] = None
    DataAccessRoleArn: Optional[str] = None
    Message: Optional[str] = None

class ImportJobPropertiesTypeDef(BaseModel):
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

class StartFHIRExportJobRequestRequestTypeDef(BaseModel):
    OutputDataConfig: OutputDataConfigTypeDef
    DatastoreId: str
    DataAccessRoleArn: str
    ClientToken: str
    JobName: Optional[str] = None

class StartFHIRImportJobRequestRequestTypeDef(BaseModel):
    InputDataConfig: InputDataConfigTypeDef
    JobOutputDataConfig: OutputDataConfigTypeDef
    DatastoreId: str
    DataAccessRoleArn: str
    ClientToken: str
    JobName: Optional[str] = None

class DescribeFHIRDatastoreResponseTypeDef(BaseModel):
    DatastoreProperties: DatastorePropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListFHIRDatastoresResponseTypeDef(BaseModel):
    DatastorePropertiesList: List[DatastorePropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFHIRExportJobResponseTypeDef(BaseModel):
    ExportJobProperties: ExportJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListFHIRExportJobsResponseTypeDef(BaseModel):
    ExportJobPropertiesList: List[ExportJobPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFHIRImportJobResponseTypeDef(BaseModel):
    ImportJobProperties: ImportJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListFHIRImportJobsResponseTypeDef(BaseModel):
    ImportJobPropertiesList: List[ImportJobPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

