from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.medical_imaging_constants import *

class CopyDestinationImageSetPropertiesTypeDef(BaseValidatorModel):
    imageSetId: str
    latestVersionId: str
    imageSetState: Optional[ImageSetStateType] = None
    imageSetWorkflowStatus: Optional[ImageSetWorkflowStatusType] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    imageSetArn: Optional[str] = None

class CopyDestinationImageSetTypeDef(BaseValidatorModel):
    imageSetId: str
    latestVersionId: str

class CopySourceImageSetInformationTypeDef(BaseValidatorModel):
    latestVersionId: str

class CopySourceImageSetPropertiesTypeDef(BaseValidatorModel):
    imageSetId: str
    latestVersionId: str
    imageSetState: Optional[ImageSetStateType] = None
    imageSetWorkflowStatus: Optional[ImageSetWorkflowStatusType] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    imageSetArn: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CreateDatastoreRequestRequestTypeDef(BaseValidatorModel):
    clientToken: str
    datastoreName: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    kmsKeyArn: Optional[str] = None

class DICOMImportJobPropertiesTypeDef(BaseValidatorModel):
    jobId: str
    jobName: str
    jobStatus: JobStatusType
    datastoreId: str
    dataAccessRoleArn: str
    inputS3Uri: str
    outputS3Uri: str
    endedAt: Optional[datetime] = None
    submittedAt: Optional[datetime] = None
    message: Optional[str] = None

class DICOMImportJobSummaryTypeDef(BaseValidatorModel):
    jobId: str
    jobName: str
    jobStatus: JobStatusType
    datastoreId: str
    dataAccessRoleArn: Optional[str] = None
    endedAt: Optional[datetime] = None
    submittedAt: Optional[datetime] = None
    message: Optional[str] = None

class DICOMStudyDateAndTimeTypeDef(BaseValidatorModel):
    DICOMStudyDate: str
    DICOMStudyTime: Optional[str] = None

class DICOMTagsTypeDef(BaseValidatorModel):
    DICOMPatientId: Optional[str] = None
    DICOMPatientName: Optional[str] = None
    DICOMPatientBirthDate: Optional[str] = None
    DICOMPatientSex: Optional[str] = None
    DICOMStudyInstanceUID: Optional[str] = None
    DICOMStudyId: Optional[str] = None
    DICOMStudyDescription: Optional[str] = None
    DICOMNumberOfStudyRelatedSeries: Optional[int] = None
    DICOMNumberOfStudyRelatedInstances: Optional[int] = None
    DICOMAccessionNumber: Optional[str] = None
    DICOMSeriesInstanceUID: Optional[str] = None
    DICOMSeriesModality: Optional[str] = None
    DICOMSeriesBodyPart: Optional[str] = None
    DICOMSeriesNumber: Optional[int] = None
    DICOMStudyDate: Optional[str] = None
    DICOMStudyTime: Optional[str] = None

class DatastorePropertiesTypeDef(BaseValidatorModel):
    datastoreId: str
    datastoreName: str
    datastoreStatus: DatastoreStatusType
    kmsKeyArn: Optional[str] = None
    datastoreArn: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None

class DatastoreSummaryTypeDef(BaseValidatorModel):
    datastoreId: str
    datastoreName: str
    datastoreStatus: DatastoreStatusType
    datastoreArn: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None

class DeleteDatastoreRequestRequestTypeDef(BaseValidatorModel):
    datastoreId: str

class DeleteImageSetRequestRequestTypeDef(BaseValidatorModel):
    datastoreId: str
    imageSetId: str

class GetDICOMImportJobRequestRequestTypeDef(BaseValidatorModel):
    datastoreId: str
    jobId: str

class GetDatastoreRequestRequestTypeDef(BaseValidatorModel):
    datastoreId: str

class ImageFrameInformationTypeDef(BaseValidatorModel):
    imageFrameId: str

class GetImageSetMetadataRequestRequestTypeDef(BaseValidatorModel):
    datastoreId: str
    imageSetId: str
    versionId: Optional[str] = None

class GetImageSetRequestRequestTypeDef(BaseValidatorModel):
    datastoreId: str
    imageSetId: str
    versionId: Optional[str] = None

class ImageSetPropertiesTypeDef(BaseValidatorModel):
    imageSetId: str
    versionId: str
    imageSetState: ImageSetStateType
    ImageSetWorkflowStatus: Optional[ImageSetWorkflowStatusType] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    deletedAt: Optional[datetime] = None
    message: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListDICOMImportJobsRequestRequestTypeDef(BaseValidatorModel):
    datastoreId: str
    jobStatus: Optional[JobStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDatastoresRequestRequestTypeDef(BaseValidatorModel):
    datastoreStatus: Optional[DatastoreStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListImageSetVersionsRequestRequestTypeDef(BaseValidatorModel):
    datastoreId: str
    imageSetId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class SortTypeDef(BaseValidatorModel):
    sortOrder: SortOrderType
    sortField: SortFieldType

class StartDICOMImportJobRequestRequestTypeDef(BaseValidatorModel):
    dataAccessRoleArn: str
    clientToken: str
    datastoreId: str
    inputS3Uri: str
    outputS3Uri: str
    jobName: Optional[str] = None
    inputOwnerAccountId: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class DICOMUpdatesTypeDef(BaseValidatorModel):
    removableAttributes: Optional[BlobTypeDef] = None
    updatableAttributes: Optional[BlobTypeDef] = None

class CopyImageSetInformationTypeDef(BaseValidatorModel):
    sourceImageSet: CopySourceImageSetInformationTypeDef
    destinationImageSet: Optional[CopyDestinationImageSetTypeDef] = None

class CopyImageSetResponseTypeDef(BaseValidatorModel):
    datastoreId: str
    sourceImageSetProperties: CopySourceImageSetPropertiesTypeDef
    destinationImageSetProperties: CopyDestinationImageSetPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatastoreResponseTypeDef(BaseValidatorModel):
    datastoreId: str
    datastoreStatus: DatastoreStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDatastoreResponseTypeDef(BaseValidatorModel):
    datastoreId: str
    datastoreStatus: DatastoreStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteImageSetResponseTypeDef(BaseValidatorModel):
    datastoreId: str
    imageSetId: str
    imageSetState: ImageSetStateType
    imageSetWorkflowStatus: ImageSetWorkflowStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetImageFrameResponseTypeDef(BaseValidatorModel):
    imageFrameBlob: StreamingBody
    contentType: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetImageSetMetadataResponseTypeDef(BaseValidatorModel):
    imageSetMetadataBlob: StreamingBody
    contentType: str
    contentEncoding: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetImageSetResponseTypeDef(BaseValidatorModel):
    datastoreId: str
    imageSetId: str
    versionId: str
    imageSetState: ImageSetStateType
    imageSetWorkflowStatus: ImageSetWorkflowStatusType
    createdAt: datetime
    updatedAt: datetime
    deletedAt: datetime
    message: str
    imageSetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartDICOMImportJobResponseTypeDef(BaseValidatorModel):
    datastoreId: str
    jobId: str
    jobStatus: JobStatusType
    submittedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateImageSetMetadataResponseTypeDef(BaseValidatorModel):
    datastoreId: str
    imageSetId: str
    latestVersionId: str
    imageSetState: ImageSetStateType
    imageSetWorkflowStatus: ImageSetWorkflowStatusType
    createdAt: datetime
    updatedAt: datetime
    message: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDICOMImportJobResponseTypeDef(BaseValidatorModel):
    jobProperties: DICOMImportJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDICOMImportJobsResponseTypeDef(BaseValidatorModel):
    jobSummaries: List[DICOMImportJobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImageSetsMetadataSummaryTypeDef(BaseValidatorModel):
    imageSetId: str
    version: Optional[int] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    DICOMTags: Optional[DICOMTagsTypeDef] = None

class GetDatastoreResponseTypeDef(BaseValidatorModel):
    datastoreProperties: DatastorePropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatastoresResponseTypeDef(BaseValidatorModel):
    datastoreSummaries: List[DatastoreSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetImageFrameRequestRequestTypeDef(BaseValidatorModel):
    datastoreId: str
    imageSetId: str
    imageFrameInformation: ImageFrameInformationTypeDef

class ListImageSetVersionsResponseTypeDef(BaseValidatorModel):
    imageSetPropertiesList: List[ImageSetPropertiesTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDICOMImportJobsRequestListDICOMImportJobsPaginateTypeDef(BaseValidatorModel):
    datastoreId: str
    jobStatus: Optional[JobStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDatastoresRequestListDatastoresPaginateTypeDef(BaseValidatorModel):
    datastoreStatus: Optional[DatastoreStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListImageSetVersionsRequestListImageSetVersionsPaginateTypeDef(BaseValidatorModel):
    datastoreId: str
    imageSetId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchByAttributeValueTypeDef(BaseValidatorModel):
    DICOMPatientId: Optional[str] = None
    DICOMAccessionNumber: Optional[str] = None
    DICOMStudyId: Optional[str] = None
    DICOMStudyInstanceUID: Optional[str] = None
    DICOMSeriesInstanceUID: Optional[str] = None
    createdAt: Optional[TimestampTypeDef] = None
    updatedAt: Optional[TimestampTypeDef] = None
    DICOMStudyDateAndTime: Optional[DICOMStudyDateAndTimeTypeDef] = None

class MetadataUpdatesTypeDef(BaseValidatorModel):
    DICOMUpdates: Optional[DICOMUpdatesTypeDef] = None

class CopyImageSetRequestRequestTypeDef(BaseValidatorModel):
    datastoreId: str
    sourceImageSetId: str
    copyImageSetInformation: CopyImageSetInformationTypeDef

class SearchImageSetsResponseTypeDef(BaseValidatorModel):
    imageSetsMetadataSummaries: List[ImageSetsMetadataSummaryTypeDef]
    sort: SortTypeDef
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchFilterTypeDef(BaseValidatorModel):
    values: Sequence[SearchByAttributeValueTypeDef]
    operator: OperatorType

class UpdateImageSetMetadataRequestRequestTypeDef(BaseValidatorModel):
    datastoreId: str
    imageSetId: str
    latestVersionId: str
    updateImageSetMetadataUpdates: MetadataUpdatesTypeDef

class SearchCriteriaTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[SearchFilterTypeDef]] = None
    sort: Optional[SortTypeDef] = None

class SearchImageSetsRequestRequestTypeDef(BaseValidatorModel):
    datastoreId: str
    searchCriteria: Optional[SearchCriteriaTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SearchImageSetsRequestSearchImageSetsPaginateTypeDef(BaseValidatorModel):
    datastoreId: str
    searchCriteria: Optional[SearchCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

