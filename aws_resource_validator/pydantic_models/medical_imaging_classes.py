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
from aws_resource_validator.pydantic_models.medical_imaging_constants import *

class CopyDestinationImageSetPropertiesTypeDef(BaseModel):
    imageSetId: str
    latestVersionId: str
    imageSetState: Optional[ImageSetStateType] = None
    imageSetWorkflowStatus: Optional[ImageSetWorkflowStatusType] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    imageSetArn: Optional[str] = None

class CopyDestinationImageSetTypeDef(BaseModel):
    imageSetId: str
    latestVersionId: str

class CopySourceImageSetInformationTypeDef(BaseModel):
    latestVersionId: str

class CopySourceImageSetPropertiesTypeDef(BaseModel):
    imageSetId: str
    latestVersionId: str
    imageSetState: Optional[ImageSetStateType] = None
    imageSetWorkflowStatus: Optional[ImageSetWorkflowStatusType] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    imageSetArn: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CreateDatastoreRequestRequestTypeDef(BaseModel):
    clientToken: str
    datastoreName: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    kmsKeyArn: Optional[str] = None

class DICOMImportJobPropertiesTypeDef(BaseModel):
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

class DICOMImportJobSummaryTypeDef(BaseModel):
    jobId: str
    jobName: str
    jobStatus: JobStatusType
    datastoreId: str
    dataAccessRoleArn: Optional[str] = None
    endedAt: Optional[datetime] = None
    submittedAt: Optional[datetime] = None
    message: Optional[str] = None

class DICOMStudyDateAndTimeTypeDef(BaseModel):
    DICOMStudyDate: str
    DICOMStudyTime: Optional[str] = None

class DICOMTagsTypeDef(BaseModel):
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

class DatastorePropertiesTypeDef(BaseModel):
    datastoreId: str
    datastoreName: str
    datastoreStatus: DatastoreStatusType
    kmsKeyArn: Optional[str] = None
    datastoreArn: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None

class DatastoreSummaryTypeDef(BaseModel):
    datastoreId: str
    datastoreName: str
    datastoreStatus: DatastoreStatusType
    datastoreArn: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None

class DeleteDatastoreRequestRequestTypeDef(BaseModel):
    datastoreId: str

class DeleteImageSetRequestRequestTypeDef(BaseModel):
    datastoreId: str
    imageSetId: str

class GetDICOMImportJobRequestRequestTypeDef(BaseModel):
    datastoreId: str
    jobId: str

class GetDatastoreRequestRequestTypeDef(BaseModel):
    datastoreId: str

class ImageFrameInformationTypeDef(BaseModel):
    imageFrameId: str

class GetImageSetMetadataRequestRequestTypeDef(BaseModel):
    datastoreId: str
    imageSetId: str
    versionId: Optional[str] = None

class GetImageSetRequestRequestTypeDef(BaseModel):
    datastoreId: str
    imageSetId: str
    versionId: Optional[str] = None

class ImageSetPropertiesTypeDef(BaseModel):
    imageSetId: str
    versionId: str
    imageSetState: ImageSetStateType
    ImageSetWorkflowStatus: Optional[ImageSetWorkflowStatusType] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    deletedAt: Optional[datetime] = None
    message: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListDICOMImportJobsRequestRequestTypeDef(BaseModel):
    datastoreId: str
    jobStatus: Optional[JobStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDatastoresRequestRequestTypeDef(BaseModel):
    datastoreStatus: Optional[DatastoreStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListImageSetVersionsRequestRequestTypeDef(BaseModel):
    datastoreId: str
    imageSetId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class SortTypeDef(BaseModel):
    sortOrder: SortOrderType
    sortField: SortFieldType

class StartDICOMImportJobRequestRequestTypeDef(BaseModel):
    dataAccessRoleArn: str
    clientToken: str
    datastoreId: str
    inputS3Uri: str
    outputS3Uri: str
    jobName: Optional[str] = None
    inputOwnerAccountId: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class DICOMUpdatesTypeDef(BaseModel):
    removableAttributes: Optional[BlobTypeDef] = None
    updatableAttributes: Optional[BlobTypeDef] = None

class CopyImageSetInformationTypeDef(BaseModel):
    sourceImageSet: CopySourceImageSetInformationTypeDef
    destinationImageSet: Optional[CopyDestinationImageSetTypeDef] = None

class CopyImageSetResponseTypeDef(BaseModel):
    datastoreId: str
    sourceImageSetProperties: CopySourceImageSetPropertiesTypeDef
    destinationImageSetProperties: CopyDestinationImageSetPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatastoreResponseTypeDef(BaseModel):
    datastoreId: str
    datastoreStatus: DatastoreStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDatastoreResponseTypeDef(BaseModel):
    datastoreId: str
    datastoreStatus: DatastoreStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteImageSetResponseTypeDef(BaseModel):
    datastoreId: str
    imageSetId: str
    imageSetState: ImageSetStateType
    imageSetWorkflowStatus: ImageSetWorkflowStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetImageFrameResponseTypeDef(BaseModel):
    imageFrameBlob: StreamingBody
    contentType: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetImageSetMetadataResponseTypeDef(BaseModel):
    imageSetMetadataBlob: StreamingBody
    contentType: str
    contentEncoding: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetImageSetResponseTypeDef(BaseModel):
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

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartDICOMImportJobResponseTypeDef(BaseModel):
    datastoreId: str
    jobId: str
    jobStatus: JobStatusType
    submittedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateImageSetMetadataResponseTypeDef(BaseModel):
    datastoreId: str
    imageSetId: str
    latestVersionId: str
    imageSetState: ImageSetStateType
    imageSetWorkflowStatus: ImageSetWorkflowStatusType
    createdAt: datetime
    updatedAt: datetime
    message: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDICOMImportJobResponseTypeDef(BaseModel):
    jobProperties: DICOMImportJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDICOMImportJobsResponseTypeDef(BaseModel):
    jobSummaries: List[DICOMImportJobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImageSetsMetadataSummaryTypeDef(BaseModel):
    imageSetId: str
    version: Optional[int] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    DICOMTags: Optional[DICOMTagsTypeDef] = None

class GetDatastoreResponseTypeDef(BaseModel):
    datastoreProperties: DatastorePropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatastoresResponseTypeDef(BaseModel):
    datastoreSummaries: List[DatastoreSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetImageFrameRequestRequestTypeDef(BaseModel):
    datastoreId: str
    imageSetId: str
    imageFrameInformation: ImageFrameInformationTypeDef

class ListImageSetVersionsResponseTypeDef(BaseModel):
    imageSetPropertiesList: List[ImageSetPropertiesTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDICOMImportJobsRequestListDICOMImportJobsPaginateTypeDef(BaseModel):
    datastoreId: str
    jobStatus: Optional[JobStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDatastoresRequestListDatastoresPaginateTypeDef(BaseModel):
    datastoreStatus: Optional[DatastoreStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListImageSetVersionsRequestListImageSetVersionsPaginateTypeDef(BaseModel):
    datastoreId: str
    imageSetId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchByAttributeValueTypeDef(BaseModel):
    DICOMPatientId: Optional[str] = None
    DICOMAccessionNumber: Optional[str] = None
    DICOMStudyId: Optional[str] = None
    DICOMStudyInstanceUID: Optional[str] = None
    DICOMSeriesInstanceUID: Optional[str] = None
    createdAt: Optional[TimestampTypeDef] = None
    updatedAt: Optional[TimestampTypeDef] = None
    DICOMStudyDateAndTime: Optional[DICOMStudyDateAndTimeTypeDef] = None

class MetadataUpdatesTypeDef(BaseModel):
    DICOMUpdates: Optional[DICOMUpdatesTypeDef] = None

class CopyImageSetRequestRequestTypeDef(BaseModel):
    datastoreId: str
    sourceImageSetId: str
    copyImageSetInformation: CopyImageSetInformationTypeDef

class SearchImageSetsResponseTypeDef(BaseModel):
    imageSetsMetadataSummaries: List[ImageSetsMetadataSummaryTypeDef]
    sort: SortTypeDef
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchFilterTypeDef(BaseModel):
    values: Sequence[SearchByAttributeValueTypeDef]
    operator: OperatorType

class UpdateImageSetMetadataRequestRequestTypeDef(BaseModel):
    datastoreId: str
    imageSetId: str
    latestVersionId: str
    updateImageSetMetadataUpdates: MetadataUpdatesTypeDef

class SearchCriteriaTypeDef(BaseModel):
    filters: Optional[Sequence[SearchFilterTypeDef]] = None
    sort: Optional[SortTypeDef] = None

class SearchImageSetsRequestRequestTypeDef(BaseModel):
    datastoreId: str
    searchCriteria: Optional[SearchCriteriaTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SearchImageSetsRequestSearchImageSetsPaginateTypeDef(BaseModel):
    datastoreId: str
    searchCriteria: Optional[SearchCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

