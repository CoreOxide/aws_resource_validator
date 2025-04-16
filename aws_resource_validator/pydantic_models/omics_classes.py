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
from aws_resource_validator.pydantic_models.omics_constants import *

class AbortMultipartReadSetUploadRequest(BaseValidatorModel):
    sequenceStoreId: str
    uploadId: str


class AcceptShareRequest(BaseValidatorModel):
    shareId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ActivateReadSetSourceItem(BaseValidatorModel):
    readSetId: str
    status: ReadSetActivationJobItemStatusType
    statusMessage: Optional[str] = None


class AnnotationImportItemDetail(BaseValidatorModel):
    source: str
    jobStatus: JobStatusType


class AnnotationImportItemSource(BaseValidatorModel):
    source: str


class ReferenceItem(BaseValidatorModel):
    referenceArn: Optional[str] = None


class BatchDeleteReadSetRequest(BaseValidatorModel):
    ids: Sequence[str]
    sequenceStoreId: str


class CancelAnnotationImportRequest(BaseValidatorModel):
    jobId: str


class CancelVariantImportRequest(BaseValidatorModel):
    jobId: str


class CompleteReadSetUploadPartListItem(BaseValidatorModel):
    partNumber: int
    partSource: ReadSetPartSourceType
    checksum: str


class CreateMultipartReadSetUploadRequest(BaseValidatorModel):
    sequenceStoreId: str
    sourceFileType: FileTypeType
    subjectId: str
    sampleId: str
    name: str
    clientToken: Optional[str] = None
    generatedFrom: Optional[str] = None
    referenceArn: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class CreateRunCacheRequest(BaseValidatorModel):
    cacheS3Location: str
    requestId: str
    cacheBehavior: Optional[CacheBehaviorType] = None
    description: Optional[str] = None
    name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    cacheBucketOwnerId: Optional[str] = None


class CreateRunGroupRequest(BaseValidatorModel):
    requestId: str
    name: Optional[str] = None
    maxCpus: Optional[int] = None
    maxRuns: Optional[int] = None
    maxDuration: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None
    maxGpus: Optional[int] = None


class S3AccessConfig(BaseValidatorModel):
    accessLogLocation: Optional[str] = None


class SequenceStoreS3Access(BaseValidatorModel):
    s3Uri: Optional[str] = None
    s3AccessPointArn: Optional[str] = None
    accessLogLocation: Optional[str] = None


class CreateShareRequest(BaseValidatorModel):
    resourceArn: str
    principalSubscriber: str
    shareName: Optional[str] = None


class WorkflowParameter(BaseValidatorModel):
    description: Optional[str] = None
    optional: Optional[bool] = None


class DeleteAnnotationStoreRequest(BaseValidatorModel):
    name: str
    force: Optional[bool] = None


class DeleteAnnotationStoreVersionsRequest(BaseValidatorModel):
    name: str
    versions: Sequence[str]
    force: Optional[bool] = None


class VersionDeleteError(BaseValidatorModel):
    versionName: str
    message: str


class DeleteS3AccessPolicyRequest(BaseValidatorModel):
    s3AccessPointArn: str


class DeleteShareRequest(BaseValidatorModel):
    shareId: str


class DeleteVariantStoreRequest(BaseValidatorModel):
    name: str
    force: Optional[bool] = None


class ETag(BaseValidatorModel):
    algorithm: Optional[ETagAlgorithmType] = None
    source1: Optional[str] = None
    source2: Optional[str] = None


class ExportReadSet(BaseValidatorModel):
    readSetId: str


class ReadSetS3Access(BaseValidatorModel):
    s3Uri: Optional[str] = None


class VcfOptions(BaseValidatorModel):
    ignoreQualField: Optional[bool] = None
    ignoreFilterField: Optional[bool] = None


class GetAnnotationImportRequest(BaseValidatorModel):
    jobId: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class GetAnnotationStoreRequest(BaseValidatorModel):
    name: str


class GetAnnotationStoreVersionRequest(BaseValidatorModel):
    name: str
    versionName: str


class SequenceInformation(BaseValidatorModel):
    totalReadCount: Optional[int] = None
    totalBaseCount: Optional[int] = None
    generatedFrom: Optional[str] = None
    alignment: Optional[str] = None


class ImportReferenceSourceItem(BaseValidatorModel):
    status: ReferenceImportJobItemStatusType
    sourceFile: Optional[str] = None
    statusMessage: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    referenceId: Optional[str] = None


class RunLogLocation(BaseValidatorModel):
    engineLogStream: Optional[str] = None
    runLogStream: Optional[str] = None


class GetS3AccessPolicyRequest(BaseValidatorModel):
    s3AccessPointArn: str


class GetShareRequest(BaseValidatorModel):
    shareId: str


class ShareDetails(BaseValidatorModel):
    shareId: Optional[str] = None
    resourceArn: Optional[str] = None
    resourceId: Optional[str] = None
    principalSubscriber: Optional[str] = None
    ownerId: Optional[str] = None
    status: Optional[ShareStatusType] = None
    statusMessage: Optional[str] = None
    shareName: Optional[str] = None
    creationTime: Optional[datetime] = None
    updateTime: Optional[datetime] = None


class GetVariantImportRequest(BaseValidatorModel):
    jobId: str


class VariantImportItemDetail(BaseValidatorModel):
    source: str
    jobStatus: JobStatusType
    statusMessage: Optional[str] = None


class GetVariantStoreRequest(BaseValidatorModel):
    name: str


class SourceFiles(BaseValidatorModel):
    source1: str
    source2: Optional[str] = None


class ListAnnotationImportJobsFilter(BaseValidatorModel):
    status: Optional[JobStatusType] = None
    storeName: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAnnotationStoreVersionsFilter(BaseValidatorModel):
    status: Optional[VersionStatusType] = None


class ListAnnotationStoresFilter(BaseValidatorModel):
    status: Optional[StoreStatusType] = None


class ListMultipartReadSetUploadsRequest(BaseValidatorModel):
    sequenceStoreId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class MultipartReadSetUploadListItem(BaseValidatorModel):
    sequenceStoreId: str
    uploadId: str
    sourceFileType: FileTypeType
    subjectId: str
    sampleId: str
    generatedFrom: str
    referenceArn: str
    creationTime: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class ReadSetUploadPartListItem(BaseValidatorModel):
    partNumber: int
    partSize: int
    partSource: ReadSetPartSourceType
    checksum: str
    creationTime: Optional[datetime] = None
    lastUpdatedTime: Optional[datetime] = None


class ListRunCachesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    startingToken: Optional[str] = None


class ListRunGroupsRequest(BaseValidatorModel):
    name: Optional[str] = None
    startingToken: Optional[str] = None
    maxResults: Optional[int] = None


class TaskListItem(BaseValidatorModel):
    taskId: Optional[str] = None
    status: Optional[TaskStatusType] = None
    name: Optional[str] = None
    cpus: Optional[int] = None
    cacheHit: Optional[bool] = None
    cacheS3Uri: Optional[str] = None
    memory: Optional[int] = None
    creationTime: Optional[datetime] = None
    startTime: Optional[datetime] = None
    stopTime: Optional[datetime] = None
    gpus: Optional[int] = None
    instanceType: Optional[str] = None


class ListRunsRequest(BaseValidatorModel):
    name: Optional[str] = None
    runGroupId: Optional[str] = None
    startingToken: Optional[str] = None
    maxResults: Optional[int] = None
    status: Optional[RunStatusType] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class ListVariantImportJobsFilter(BaseValidatorModel):
    status: Optional[JobStatusType] = None
    storeName: Optional[str] = None


class ListVariantStoresFilter(BaseValidatorModel):
    status: Optional[StoreStatusType] = None


class PutS3AccessPolicyRequest(BaseValidatorModel):
    s3AccessPointArn: str
    s3AccessPolicy: str


class ReadOptions(BaseValidatorModel):
    sep: Optional[str] = None
    encoding: Optional[str] = None
    quote: Optional[str] = None
    quoteAll: Optional[bool] = None
    escape: Optional[str] = None
    escapeQuotes: Optional[bool] = None
    comment: Optional[str] = None
    header: Optional[bool] = None
    lineSep: Optional[str] = None


class StartReadSetActivationJobSourceItem(BaseValidatorModel):
    readSetId: str


class StartReferenceImportJobSourceItem(BaseValidatorModel):
    sourceFile: str
    name: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class StartRunRequest(BaseValidatorModel):
    roleArn: str
    requestId: str
    workflowId: Optional[str] = None
    workflowType: Optional[WorkflowTypeType] = None
    runId: Optional[str] = None
    name: Optional[str] = None
    cacheId: Optional[str] = None
    cacheBehavior: Optional[CacheBehaviorType] = None
    runGroupId: Optional[str] = None
    priority: Optional[int] = None
    parameters: Optional[Mapping[str, Any]] = None
    storageCapacity: Optional[int] = None
    outputUri: Optional[str] = None
    logLevel: Optional[RunLogLevelType] = None
    tags: Optional[Mapping[str, str]] = None
    retentionMode: Optional[RunRetentionModeType] = None
    storageType: Optional[StorageTypeType] = None
    workflowOwnerId: Optional[str] = None


class VariantImportItemSource(BaseValidatorModel):
    source: str


class TsvStoreOptionsOutput(BaseValidatorModel):
    annotationType: Optional[AnnotationTypeType] = None
    formatToHeader: Optional[Dict[FormatToHeaderKeyType, str]] = None
    schema: Optional[List[Dict[str, SchemaValueTypeType]]] = None


class TsvStoreOptions(BaseValidatorModel):
    annotationType: Optional[AnnotationTypeType] = None
    formatToHeader: Optional[Mapping[FormatToHeaderKeyType, str]] = None
    schema: Optional[Sequence[Mapping[str, SchemaValueTypeType]]] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class TsvVersionOptionsOutput(BaseValidatorModel):
    annotationType: Optional[AnnotationTypeType] = None
    formatToHeader: Optional[Dict[FormatToHeaderKeyType, str]] = None
    schema: Optional[List[Dict[str, SchemaValueTypeType]]] = None


class TsvVersionOptions(BaseValidatorModel):
    annotationType: Optional[AnnotationTypeType] = None
    formatToHeader: Optional[Mapping[FormatToHeaderKeyType, str]] = None
    schema: Optional[Sequence[Mapping[str, SchemaValueTypeType]]] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateAnnotationStoreRequest(BaseValidatorModel):
    name: str
    description: Optional[str] = None


class UpdateAnnotationStoreVersionRequest(BaseValidatorModel):
    name: str
    versionName: str
    description: Optional[str] = None


class UpdateVariantStoreRequest(BaseValidatorModel):
    name: str
    description: Optional[str] = None


class AcceptShareResponse(BaseValidatorModel):
    status: ShareStatusType
    ResponseMetadata: ResponseMetadata


class CompleteMultipartReadSetUploadResponse(BaseValidatorModel):
    readSetId: str
    ResponseMetadata: ResponseMetadata


class CreateMultipartReadSetUploadResponse(BaseValidatorModel):
    sequenceStoreId: str
    uploadId: str
    sourceFileType: FileTypeType
    subjectId: str
    sampleId: str
    generatedFrom: str
    referenceArn: str
    name: str
    description: str
    tags: Dict[str, str]
    creationTime: datetime
    ResponseMetadata: ResponseMetadata


class CreateShareResponse(BaseValidatorModel):
    shareId: str
    status: ShareStatusType
    shareName: str
    ResponseMetadata: ResponseMetadata


class DeleteAnnotationStoreResponse(BaseValidatorModel):
    status: StoreStatusType
    ResponseMetadata: ResponseMetadata


class DeleteShareResponse(BaseValidatorModel):
    status: ShareStatusType
    ResponseMetadata: ResponseMetadata


class DeleteVariantStoreResponse(BaseValidatorModel):
    status: StoreStatusType
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetReadSetResponse(BaseValidatorModel):
    payload: StreamingBody
    ResponseMetadata: ResponseMetadata


class GetReferenceResponse(BaseValidatorModel):
    payload: StreamingBody
    ResponseMetadata: ResponseMetadata


class GetRunTaskResponse(BaseValidatorModel):
    taskId: str
    status: TaskStatusType
    name: str
    cpus: int
    cacheHit: bool
    cacheS3Uri: str
    memory: int
    creationTime: datetime
    startTime: datetime
    stopTime: datetime
    statusMessage: str
    logStream: str
    gpus: int
    instanceType: str
    failureReason: str
    ResponseMetadata: ResponseMetadata


class GetS3AccessPolicyResponse(BaseValidatorModel):
    s3AccessPointArn: str
    storeId: str
    storeType: StoreTypeType
    updateTime: datetime
    s3AccessPolicy: str
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class PutS3AccessPolicyResponse(BaseValidatorModel):
    s3AccessPointArn: str
    storeId: str
    storeType: StoreTypeType
    ResponseMetadata: ResponseMetadata


class StartAnnotationImportResponse(BaseValidatorModel):
    jobId: str
    ResponseMetadata: ResponseMetadata


class StartVariantImportResponse(BaseValidatorModel):
    jobId: str
    ResponseMetadata: ResponseMetadata


class UploadReadSetPartResponse(BaseValidatorModel):
    checksum: str
    ResponseMetadata: ResponseMetadata


class Timestamp(BaseValidatorModel):
    pass


class ActivateReadSetFilter(BaseValidatorModel):
    status: Optional[ReadSetActivationJobStatusType] = None
    createdAfter: Optional[Timestamp] = None
    createdBefore: Optional[Timestamp] = None


class ExportReadSetFilter(BaseValidatorModel):
    status: Optional[ReadSetExportJobStatusType] = None
    createdAfter: Optional[Timestamp] = None
    createdBefore: Optional[Timestamp] = None


class ImportReadSetFilter(BaseValidatorModel):
    status: Optional[ReadSetImportJobStatusType] = None
    createdAfter: Optional[Timestamp] = None
    createdBefore: Optional[Timestamp] = None


class ImportReferenceFilter(BaseValidatorModel):
    status: Optional[ReferenceImportJobStatusType] = None
    createdAfter: Optional[Timestamp] = None
    createdBefore: Optional[Timestamp] = None


class ReadSetFilter(BaseValidatorModel):
    name: Optional[str] = None
    status: Optional[ReadSetStatusType] = None
    referenceArn: Optional[str] = None
    createdAfter: Optional[Timestamp] = None
    createdBefore: Optional[Timestamp] = None
    sampleId: Optional[str] = None
    subjectId: Optional[str] = None
    generatedFrom: Optional[str] = None
    creationType: Optional[CreationTypeType] = None


class ReadSetUploadPartListFilter(BaseValidatorModel):
    createdAfter: Optional[Timestamp] = None
    createdBefore: Optional[Timestamp] = None


class ReferenceFilter(BaseValidatorModel):
    name: Optional[str] = None
    md5: Optional[str] = None
    createdAfter: Optional[Timestamp] = None
    createdBefore: Optional[Timestamp] = None


class ReferenceStoreFilter(BaseValidatorModel):
    name: Optional[str] = None
    createdAfter: Optional[Timestamp] = None
    createdBefore: Optional[Timestamp] = None


class SequenceStoreFilter(BaseValidatorModel):
    name: Optional[str] = None
    createdAfter: Optional[Timestamp] = None
    createdBefore: Optional[Timestamp] = None
    status: Optional[SequenceStoreStatusType] = None
    updatedAfter: Optional[Timestamp] = None
    updatedBefore: Optional[Timestamp] = None


class ActivateReadSetJobItem(BaseValidatorModel):
    pass


class ListReadSetActivationJobsResponse(BaseValidatorModel):
    activationJobs: List[ActivateReadSetJobItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class AnnotationImportJobItem(BaseValidatorModel):
    pass


class ListAnnotationImportJobsResponse(BaseValidatorModel):
    annotationImportJobs: List[AnnotationImportJobItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SseConfig(BaseValidatorModel):
    pass


class CreateReferenceStoreRequest(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    sseConfig: Optional[SseConfig] = None
    tags: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None


class CreateVariantStoreRequest(BaseValidatorModel):
    reference: ReferenceItem
    name: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    sseConfig: Optional[SseConfig] = None


class AnnotationStoreVersionItem(BaseValidatorModel):
    pass


class ListAnnotationStoreVersionsResponse(BaseValidatorModel):
    annotationStoreVersions: List[AnnotationStoreVersionItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ReadSetBatchError(BaseValidatorModel):
    pass


class BatchDeleteReadSetResponse(BaseValidatorModel):
    errors: List[ReadSetBatchError]
    ResponseMetadata: ResponseMetadata


class Blob(BaseValidatorModel):
    pass


class UploadReadSetPartRequest(BaseValidatorModel):
    sequenceStoreId: str
    uploadId: str
    partSource: ReadSetPartSourceType
    partNumber: int
    payload: Blob


class CompleteMultipartReadSetUploadRequest(BaseValidatorModel):
    sequenceStoreId: str
    uploadId: str
    parts: Sequence[CompleteReadSetUploadPartListItem]


class CreateSequenceStoreRequest(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    sseConfig: Optional[SseConfig] = None
    tags: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None
    fallbackLocation: Optional[str] = None
    eTagAlgorithmFamily: Optional[ETagAlgorithmFamilyType] = None
    propagatedSetLevelTags: Optional[Sequence[str]] = None
    s3AccessConfig: Optional[S3AccessConfig] = None


class CreateWorkflowRequest(BaseValidatorModel):
    requestId: str
    name: Optional[str] = None
    description: Optional[str] = None
    engine: Optional[WorkflowEngineType] = None
    definitionZip: Optional[Blob] = None
    definitionUri: Optional[str] = None
    main: Optional[str] = None
    parameterTemplate: Optional[Mapping[str, WorkflowParameter]] = None
    storageCapacity: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None
    accelerators: Optional[Literal["GPU"]] = None


class DeleteAnnotationStoreVersionsResponse(BaseValidatorModel):
    errors: List[VersionDeleteError]
    ResponseMetadata: ResponseMetadata


class ExportReadSetJobDetail(BaseValidatorModel):
    pass


class ListReadSetExportJobsResponse(BaseValidatorModel):
    exportJobs: List[ExportReadSetJobDetail]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class StartReadSetExportJobRequest(BaseValidatorModel):
    sequenceStoreId: str
    destination: str
    roleArn: str
    sources: Sequence[ExportReadSet]
    clientToken: Optional[str] = None


class FileInformation(BaseValidatorModel):
    totalParts: Optional[int] = None
    partSize: Optional[int] = None
    contentLength: Optional[int] = None
    s3Access: Optional[ReadSetS3Access] = None


class GetAnnotationImportRequestWait(BaseValidatorModel):
    jobId: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetAnnotationStoreRequestWaitExtra(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetAnnotationStoreRequestWait(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetAnnotationStoreVersionRequestWaitExtra(BaseValidatorModel):
    name: str
    versionName: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetAnnotationStoreVersionRequestWait(BaseValidatorModel):
    name: str
    versionName: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetVariantImportRequestWait(BaseValidatorModel):
    jobId: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetVariantStoreRequestWaitExtra(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetVariantStoreRequestWait(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetShareResponse(BaseValidatorModel):
    share: ShareDetails
    ResponseMetadata: ResponseMetadata


class ListSharesResponse(BaseValidatorModel):
    shares: List[ShareDetails]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ImportReadSetJobItem(BaseValidatorModel):
    pass


class ListReadSetImportJobsResponse(BaseValidatorModel):
    importJobs: List[ImportReadSetJobItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ImportReadSetSourceItem(BaseValidatorModel):
    sourceFiles: SourceFiles
    sourceFileType: FileTypeType
    status: ReadSetImportJobItemStatusType
    subjectId: str
    sampleId: str
    statusMessage: Optional[str] = None
    generatedFrom: Optional[str] = None
    referenceArn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    readSetId: Optional[str] = None


class StartReadSetImportJobSourceItem(BaseValidatorModel):
    sourceFiles: SourceFiles
    sourceFileType: FileTypeType
    subjectId: str
    sampleId: str
    generatedFrom: Optional[str] = None
    referenceArn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class ImportReferenceJobItem(BaseValidatorModel):
    pass


class ListReferenceImportJobsResponse(BaseValidatorModel):
    importJobs: List[ImportReferenceJobItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListMultipartReadSetUploadsRequestPaginate(BaseValidatorModel):
    sequenceStoreId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRunCachesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRunGroupsRequestPaginate(BaseValidatorModel):
    name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRunsRequestPaginate(BaseValidatorModel):
    name: Optional[str] = None
    runGroupId: Optional[str] = None
    status: Optional[RunStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMultipartReadSetUploadsResponse(BaseValidatorModel):
    uploads: List[MultipartReadSetUploadListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListReadSetUploadPartsResponse(BaseValidatorModel):
    parts: List[ReadSetUploadPartListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ReferenceListItem(BaseValidatorModel):
    pass


class ListReferencesResponse(BaseValidatorModel):
    references: List[ReferenceListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class RunCacheListItem(BaseValidatorModel):
    pass


class ListRunCachesResponse(BaseValidatorModel):
    items: List[RunCacheListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class RunGroupListItem(BaseValidatorModel):
    pass


class ListRunGroupsResponse(BaseValidatorModel):
    items: List[RunGroupListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListRunTasksResponse(BaseValidatorModel):
    items: List[TaskListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class RunListItem(BaseValidatorModel):
    pass


class ListRunsResponse(BaseValidatorModel):
    items: List[RunListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class VariantImportJobItem(BaseValidatorModel):
    pass


class ListVariantImportJobsResponse(BaseValidatorModel):
    variantImportJobs: List[VariantImportJobItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class WorkflowListItem(BaseValidatorModel):
    pass


class ListWorkflowsResponse(BaseValidatorModel):
    items: List[WorkflowListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class TsvOptions(BaseValidatorModel):
    readOptions: Optional[ReadOptions] = None


class StartReadSetActivationJobRequest(BaseValidatorModel):
    sequenceStoreId: str
    sources: Sequence[StartReadSetActivationJobSourceItem]
    clientToken: Optional[str] = None


class StartReferenceImportJobRequest(BaseValidatorModel):
    referenceStoreId: str
    roleArn: str
    sources: Sequence[StartReferenceImportJobSourceItem]
    clientToken: Optional[str] = None


class StartVariantImportRequest(BaseValidatorModel):
    destinationName: str
    roleArn: str
    items: Sequence[VariantImportItemSource]
    runLeftNormalization: Optional[bool] = None
    annotationFields: Optional[Mapping[str, str]] = None


class StoreOptionsOutput(BaseValidatorModel):
    tsvStoreOptions: Optional[TsvStoreOptionsOutput] = None


class StoreOptions(BaseValidatorModel):
    tsvStoreOptions: Optional[TsvStoreOptions] = None


class VersionOptionsOutput(BaseValidatorModel):
    tsvVersionOptions: Optional[TsvVersionOptionsOutput] = None


class VersionOptions(BaseValidatorModel):
    tsvVersionOptions: Optional[TsvVersionOptions] = None


class AnnotationStoreItem(BaseValidatorModel):
    pass


class ListAnnotationStoresResponse(BaseValidatorModel):
    annotationStores: List[AnnotationStoreItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ReferenceStoreDetail(BaseValidatorModel):
    pass


class ListReferenceStoresResponse(BaseValidatorModel):
    referenceStores: List[ReferenceStoreDetail]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SequenceStoreDetail(BaseValidatorModel):
    pass


class ListSequenceStoresResponse(BaseValidatorModel):
    sequenceStores: List[SequenceStoreDetail]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class VariantStoreItem(BaseValidatorModel):
    pass


class ListVariantStoresResponse(BaseValidatorModel):
    variantStores: List[VariantStoreItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ReadSetFiles(BaseValidatorModel):
    source1: Optional[FileInformation] = None
    source2: Optional[FileInformation] = None
    index: Optional[FileInformation] = None


class ReferenceFiles(BaseValidatorModel):
    source: Optional[FileInformation] = None
    index: Optional[FileInformation] = None


class ReadSetListItem(BaseValidatorModel):
    pass


class ListReadSetsResponse(BaseValidatorModel):
    readSets: List[ReadSetListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class StartReadSetImportJobRequest(BaseValidatorModel):
    sequenceStoreId: str
    roleArn: str
    sources: Sequence[StartReadSetImportJobSourceItem]
    clientToken: Optional[str] = None


class FormatOptions(BaseValidatorModel):
    tsvOptions: Optional[TsvOptions] = None
    vcfOptions: Optional[VcfOptions] = None


class StartAnnotationImportRequest(BaseValidatorModel):
    destinationName: str
    roleArn: str
    items: Sequence[AnnotationImportItemSource]
    versionName: Optional[str] = None
    formatOptions: Optional[FormatOptions] = None
    runLeftNormalization: Optional[bool] = None
    annotationFields: Optional[Mapping[str, str]] = None


class StoreOptionsUnion(BaseValidatorModel):
    pass


class CreateAnnotationStoreRequest(BaseValidatorModel):
    storeFormat: StoreFormatType
    reference: Optional[ReferenceItem] = None
    name: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    versionName: Optional[str] = None
    sseConfig: Optional[SseConfig] = None
    storeOptions: Optional[StoreOptionsUnion] = None


class VersionOptionsUnion(BaseValidatorModel):
    pass


class CreateAnnotationStoreVersionRequest(BaseValidatorModel):
    name: str
    versionName: str
    description: Optional[str] = None
    versionOptions: Optional[VersionOptionsUnion] = None
    tags: Optional[Mapping[str, str]] = None


