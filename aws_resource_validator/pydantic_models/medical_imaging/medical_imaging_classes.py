from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream



Blob = Union[str, bytes, IO[Any], StreamingBody]


class CopyDestinationImageSetProperties(BaseValidatorModel):
    imageSetId: str
    latestVersionId: str
    imageSetState: Optional[ImageSetStateType] = None
    imageSetWorkflowStatus: Optional[ImageSetWorkflowStatusType] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    imageSetArn: Optional[str] = None


class CopyDestinationImageSet(BaseValidatorModel):
    imageSetId: str
    latestVersionId: str


class CopySourceImageSetProperties(BaseValidatorModel):
    imageSetId: str
    latestVersionId: str
    imageSetState: Optional[ImageSetStateType] = None
    imageSetWorkflowStatus: Optional[ImageSetWorkflowStatusType] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    imageSetArn: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class MetadataCopies(BaseValidatorModel):
    copiableAttributes: str


# This class is the input for the 'create_datastore' function.
class CreateDatastoreRequest(BaseValidatorModel):
    clientToken: str
    datastoreName: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    kmsKeyArn: Optional[str] = None


class DICOMImportJobProperties(BaseValidatorModel):
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


class DICOMImportJobSummary(BaseValidatorModel):
    jobId: str
    jobName: str
    jobStatus: JobStatusType
    datastoreId: str
    dataAccessRoleArn: Optional[str] = None
    endedAt: Optional[datetime] = None
    submittedAt: Optional[datetime] = None
    message: Optional[str] = None


class DICOMStudyDateAndTime(BaseValidatorModel):
    DICOMStudyDate: str
    DICOMStudyTime: Optional[str] = None


class DICOMTags(BaseValidatorModel):
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


class DatastoreProperties(BaseValidatorModel):
    datastoreId: str
    datastoreName: str
    datastoreStatus: DatastoreStatusType
    kmsKeyArn: Optional[str] = None
    datastoreArn: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None


class DatastoreSummary(BaseValidatorModel):
    datastoreId: str
    datastoreName: str
    datastoreStatus: DatastoreStatusType
    datastoreArn: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None


# This class is the input for the 'delete_datastore' function.
class DeleteDatastoreRequest(BaseValidatorModel):
    datastoreId: str


# This class is the input for the 'delete_image_set' function.
class DeleteImageSetRequest(BaseValidatorModel):
    datastoreId: str
    imageSetId: str


# This class is the input for the 'get_dicom_import_job' function.
class GetDICOMImportJobRequest(BaseValidatorModel):
    datastoreId: str
    jobId: str


# This class is the input for the 'get_datastore' function.
class GetDatastoreRequest(BaseValidatorModel):
    datastoreId: str


class ImageFrameInformation(BaseValidatorModel):
    imageFrameId: str


# This class is the input for the 'get_image_set_metadata' function.
class GetImageSetMetadataRequest(BaseValidatorModel):
    datastoreId: str
    imageSetId: str
    versionId: Optional[str] = None


# This class is the input for the 'get_image_set' function.
class GetImageSetRequest(BaseValidatorModel):
    datastoreId: str
    imageSetId: str
    versionId: Optional[str] = None


class Overrides(BaseValidatorModel):
    forced: Optional[bool] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_dicom_import_jobs' function.
class ListDICOMImportJobsRequest(BaseValidatorModel):
    datastoreId: str
    jobStatus: Optional[JobStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_datastores' function.
class ListDatastoresRequest(BaseValidatorModel):
    datastoreStatus: Optional[DatastoreStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_image_set_versions' function.
class ListImageSetVersionsRequest(BaseValidatorModel):
    datastoreId: str
    imageSetId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str

Timestamp = Union[datetime, str]


class Sort(BaseValidatorModel):
    sortOrder: SortOrderType
    sortField: SortFieldType


# This class is the input for the 'start_dicom_import_job' function.
class StartDICOMImportJobRequest(BaseValidatorModel):
    dataAccessRoleArn: str
    clientToken: str
    datastoreId: str
    inputS3Uri: str
    outputS3Uri: str
    jobName: Optional[str] = None
    inputOwnerAccountId: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class DICOMUpdates(BaseValidatorModel):
    removableAttributes: Optional[Blob] = None
    updatableAttributes: Optional[Blob] = None


# This class is the output for the 'copy_image_set' function.
class CopyImageSetResponse(BaseValidatorModel):
    datastoreId: str
    sourceImageSetProperties: CopySourceImageSetProperties
    destinationImageSetProperties: CopyDestinationImageSetProperties
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_datastore' function.
class CreateDatastoreResponse(BaseValidatorModel):
    datastoreId: str
    datastoreStatus: DatastoreStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_datastore' function.
class DeleteDatastoreResponse(BaseValidatorModel):
    datastoreId: str
    datastoreStatus: DatastoreStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_image_set' function.
class DeleteImageSetResponse(BaseValidatorModel):
    datastoreId: str
    imageSetId: str
    imageSetState: ImageSetStateType
    imageSetWorkflowStatus: ImageSetWorkflowStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_image_frame' function.
class GetImageFrameResponse(BaseValidatorModel):
    imageFrameBlob: StreamingBody
    contentType: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_image_set_metadata' function.
class GetImageSetMetadataResponse(BaseValidatorModel):
    imageSetMetadataBlob: StreamingBody
    contentType: str
    contentEncoding: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_dicom_import_job' function.
class StartDICOMImportJobResponse(BaseValidatorModel):
    datastoreId: str
    jobId: str
    jobStatus: JobStatusType
    submittedAt: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_image_set_metadata' function.
class UpdateImageSetMetadataResponse(BaseValidatorModel):
    datastoreId: str
    imageSetId: str
    latestVersionId: str
    imageSetState: ImageSetStateType
    imageSetWorkflowStatus: ImageSetWorkflowStatusType
    createdAt: datetime
    updatedAt: datetime
    message: str
    ResponseMetadata: ResponseMetadata


class CopySourceImageSetInformation(BaseValidatorModel):
    latestVersionId: str
    DICOMCopies: Optional[MetadataCopies] = None


# This class is the output for the 'get_dicom_import_job' function.
class GetDICOMImportJobResponse(BaseValidatorModel):
    jobProperties: DICOMImportJobProperties
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_dicom_import_jobs' function.
class ListDICOMImportJobsResponse(BaseValidatorModel):
    jobSummaries: List[DICOMImportJobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ImageSetsMetadataSummary(BaseValidatorModel):
    imageSetId: str
    version: Optional[int] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    DICOMTags: Optional[DICOMTags] = None


# This class is the output for the 'get_datastore' function.
class GetDatastoreResponse(BaseValidatorModel):
    datastoreProperties: DatastoreProperties
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_datastores' function.
class ListDatastoresResponse(BaseValidatorModel):
    datastoreSummaries: List[DatastoreSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'get_image_frame' function.
class GetImageFrameRequest(BaseValidatorModel):
    datastoreId: str
    imageSetId: str
    imageFrameInformation: ImageFrameInformation


# This class is the output for the 'get_image_set' function.
class GetImageSetResponse(BaseValidatorModel):
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
    overrides: Overrides
    ResponseMetadata: ResponseMetadata


class ImageSetProperties(BaseValidatorModel):
    imageSetId: str
    versionId: str
    imageSetState: ImageSetStateType
    ImageSetWorkflowStatus: Optional[ImageSetWorkflowStatusType] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    deletedAt: Optional[datetime] = None
    message: Optional[str] = None
    overrides: Optional[Overrides] = None


class ListDICOMImportJobsRequestPaginate(BaseValidatorModel):
    datastoreId: str
    jobStatus: Optional[JobStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDatastoresRequestPaginate(BaseValidatorModel):
    datastoreStatus: Optional[DatastoreStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListImageSetVersionsRequestPaginate(BaseValidatorModel):
    datastoreId: str
    imageSetId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchByAttributeValue(BaseValidatorModel):
    DICOMPatientId: Optional[str] = None
    DICOMAccessionNumber: Optional[str] = None
    DICOMStudyId: Optional[str] = None
    DICOMStudyInstanceUID: Optional[str] = None
    DICOMSeriesInstanceUID: Optional[str] = None
    createdAt: Optional[Timestamp] = None
    updatedAt: Optional[Timestamp] = None
    DICOMStudyDateAndTime: Optional[DICOMStudyDateAndTime] = None


class MetadataUpdates(BaseValidatorModel):
    DICOMUpdates: Optional[DICOMUpdates] = None
    revertToVersionId: Optional[str] = None


class CopyImageSetInformation(BaseValidatorModel):
    sourceImageSet: CopySourceImageSetInformation
    destinationImageSet: Optional[CopyDestinationImageSet] = None


# This class is the output for the 'search_image_sets' function.
class SearchImageSetsResponse(BaseValidatorModel):
    imageSetsMetadataSummaries: List[ImageSetsMetadataSummary]
    sort: Sort
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_image_set_versions' function.
class ListImageSetVersionsResponse(BaseValidatorModel):
    imageSetPropertiesList: List[ImageSetProperties]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SearchFilter(BaseValidatorModel):
    values: List[SearchByAttributeValue]
    operator: OperatorType


# This class is the input for the 'update_image_set_metadata' function.
class UpdateImageSetMetadataRequest(BaseValidatorModel):
    datastoreId: str
    imageSetId: str
    latestVersionId: str
    updateImageSetMetadataUpdates: MetadataUpdates
    force: Optional[bool] = None


# This class is the input for the 'copy_image_set' function.
class CopyImageSetRequest(BaseValidatorModel):
    datastoreId: str
    sourceImageSetId: str
    copyImageSetInformation: CopyImageSetInformation
    force: Optional[bool] = None


class SearchCriteria(BaseValidatorModel):
    filters: Optional[List[SearchFilter]] = None
    sort: Optional[Sort] = None


class SearchImageSetsRequestPaginate(BaseValidatorModel):
    datastoreId: str
    searchCriteria: Optional[SearchCriteria] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'search_image_sets' function.
class SearchImageSetsRequest(BaseValidatorModel):
    datastoreId: str
    searchCriteria: Optional[SearchCriteria] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None