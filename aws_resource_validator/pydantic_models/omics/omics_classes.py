from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.omics.omics_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




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

Timestamp = Union[datetime, str]


class ActivateReadSetJobItem(BaseValidatorModel):
    id: str
    sequenceStoreId: str
    status: ReadSetActivationJobStatusType
    creationTime: datetime
    completionTime: Optional[datetime] = None


class ActivateReadSetSourceItem(BaseValidatorModel):
    readSetId: str
    status: ReadSetActivationJobItemStatusType
    statusMessage: Optional[str] = None


class AnnotationImportItemDetail(BaseValidatorModel):
    source: str
    jobStatus: JobStatusType


class AnnotationImportItemSource(BaseValidatorModel):
    source: str


class AnnotationImportJobItem(BaseValidatorModel):
    id: str
    destinationName: str
    versionName: str
    roleArn: str
    status: JobStatusType
    creationTime: datetime
    updateTime: datetime
    completionTime: Optional[datetime] = None
    runLeftNormalization: Optional[bool] = None
    annotationFields: Optional[Dict[str, str]] = None


class ReferenceItem(BaseValidatorModel):
    referenceArn: Optional[str] = None


class SseConfig(BaseValidatorModel):
    type: Literal['KMS']
    keyArn: Optional[str] = None


class AnnotationStoreVersionItem(BaseValidatorModel):
    storeId: str
    id: str
    status: VersionStatusType
    versionArn: str
    name: str
    versionName: str
    description: str
    creationTime: datetime
    updateTime: datetime
    statusMessage: str
    versionSizeBytes: int


class BatchDeleteReadSetRequest(BaseValidatorModel):
    ids: List[str]
    sequenceStoreId: str


class ReadSetBatchError(BaseValidatorModel):
    id: str
    code: str
    message: str

Blob = Union[str, bytes, IO[Any], StreamingBody]


class CancelAnnotationImportRequest(BaseValidatorModel):
    jobId: str


class CancelRunRequest(BaseValidatorModel):
    id: str


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
    tags: Optional[Dict[str, str]] = None


class CreateRunCacheRequest(BaseValidatorModel):
    cacheS3Location: str
    requestId: str
    cacheBehavior: Optional[CacheBehaviorType] = None
    description: Optional[str] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    cacheBucketOwnerId: Optional[str] = None


class CreateRunGroupRequest(BaseValidatorModel):
    requestId: str
    name: Optional[str] = None
    maxCpus: Optional[int] = None
    maxRuns: Optional[int] = None
    maxDuration: Optional[int] = None
    tags: Optional[Dict[str, str]] = None
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
    versions: List[str]
    force: Optional[bool] = None


class VersionDeleteError(BaseValidatorModel):
    versionName: str
    message: str


class DeleteReferenceRequest(BaseValidatorModel):
    id: str
    referenceStoreId: str


class DeleteReferenceStoreRequest(BaseValidatorModel):
    id: str


class DeleteRunCacheRequest(BaseValidatorModel):
    id: str


class DeleteRunGroupRequest(BaseValidatorModel):
    id: str


class DeleteRunRequest(BaseValidatorModel):
    id: str


class DeleteS3AccessPolicyRequest(BaseValidatorModel):
    s3AccessPointArn: str


class DeleteSequenceStoreRequest(BaseValidatorModel):
    id: str


class DeleteShareRequest(BaseValidatorModel):
    shareId: str


class DeleteVariantStoreRequest(BaseValidatorModel):
    name: str
    force: Optional[bool] = None


class DeleteWorkflowRequest(BaseValidatorModel):
    id: str


class ETag(BaseValidatorModel):
    algorithm: Optional[ETagAlgorithmType] = None
    source1: Optional[str] = None
    source2: Optional[str] = None


class ExportReadSetDetail(BaseValidatorModel):
    id: str
    status: ReadSetExportJobItemStatusType
    statusMessage: Optional[str] = None


class ExportReadSetJobDetail(BaseValidatorModel):
    id: str
    sequenceStoreId: str
    destination: str
    status: ReadSetExportJobStatusType
    creationTime: datetime
    completionTime: Optional[datetime] = None


class ExportReadSet(BaseValidatorModel):
    readSetId: str


class ReadSetS3Access(BaseValidatorModel):
    s3Uri: Optional[str] = None


class Filter(BaseValidatorModel):
    resourceArns: Optional[List[str]] = None
    status: Optional[List[ShareStatusType]] = None
    type: Optional[List[ShareResourceTypeType]] = None


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


class GetReadSetActivationJobRequest(BaseValidatorModel):
    id: str
    sequenceStoreId: str


class GetReadSetExportJobRequest(BaseValidatorModel):
    sequenceStoreId: str
    id: str


class GetReadSetImportJobRequest(BaseValidatorModel):
    id: str
    sequenceStoreId: str


class GetReadSetMetadataRequest(BaseValidatorModel):
    id: str
    sequenceStoreId: str


class SequenceInformation(BaseValidatorModel):
    totalReadCount: Optional[int] = None
    totalBaseCount: Optional[int] = None
    generatedFrom: Optional[str] = None
    alignment: Optional[str] = None


class GetReadSetRequest(BaseValidatorModel):
    id: str
    sequenceStoreId: str
    partNumber: int
    file: Optional[ReadSetFileType] = None


class GetReferenceImportJobRequest(BaseValidatorModel):
    id: str
    referenceStoreId: str


class ImportReferenceSourceItem(BaseValidatorModel):
    status: ReferenceImportJobItemStatusType
    sourceFile: Optional[str] = None
    statusMessage: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    referenceId: Optional[str] = None


class GetReferenceMetadataRequest(BaseValidatorModel):
    id: str
    referenceStoreId: str


class GetReferenceRequest(BaseValidatorModel):
    id: str
    referenceStoreId: str
    partNumber: int
    range: Optional[str] = None
    file: Optional[ReferenceFileType] = None


class GetReferenceStoreRequest(BaseValidatorModel):
    id: str


class GetRunCacheRequest(BaseValidatorModel):
    id: str


class GetRunGroupRequest(BaseValidatorModel):
    id: str


class GetRunRequest(BaseValidatorModel):
    id: str
    export: Optional[List[Literal['DEFINITION']]] = None


class RunLogLocation(BaseValidatorModel):
    engineLogStream: Optional[str] = None
    runLogStream: Optional[str] = None


class GetRunTaskRequest(BaseValidatorModel):
    id: str
    taskId: str


class GetS3AccessPolicyRequest(BaseValidatorModel):
    s3AccessPointArn: str


class GetSequenceStoreRequest(BaseValidatorModel):
    id: str


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


class GetWorkflowRequest(BaseValidatorModel):
    id: str
    type: Optional[WorkflowTypeType] = None
    export: Optional[List[Literal['DEFINITION']]] = None
    workflowOwnerId: Optional[str] = None


class ImportReadSetJobItem(BaseValidatorModel):
    id: str
    sequenceStoreId: str
    roleArn: str
    status: ReadSetImportJobStatusType
    creationTime: datetime
    completionTime: Optional[datetime] = None


class SourceFiles(BaseValidatorModel):
    source1: str
    source2: Optional[str] = None


class ImportReferenceJobItem(BaseValidatorModel):
    id: str
    referenceStoreId: str
    roleArn: str
    status: ReferenceImportJobStatusType
    creationTime: datetime
    completionTime: Optional[datetime] = None


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


class ReferenceListItem(BaseValidatorModel):
    id: str
    arn: str
    referenceStoreId: str
    md5: str
    creationTime: datetime
    updateTime: datetime
    status: Optional[ReferenceStatusType] = None
    name: Optional[str] = None
    description: Optional[str] = None


class ListRunCachesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    startingToken: Optional[str] = None


class RunCacheListItem(BaseValidatorModel):
    arn: Optional[str] = None
    cacheBehavior: Optional[CacheBehaviorType] = None
    cacheS3Uri: Optional[str] = None
    creationTime: Optional[datetime] = None
    id: Optional[str] = None
    name: Optional[str] = None
    status: Optional[RunCacheStatusType] = None


class ListRunGroupsRequest(BaseValidatorModel):
    name: Optional[str] = None
    startingToken: Optional[str] = None
    maxResults: Optional[int] = None


class RunGroupListItem(BaseValidatorModel):
    arn: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    maxCpus: Optional[int] = None
    maxRuns: Optional[int] = None
    maxDuration: Optional[int] = None
    creationTime: Optional[datetime] = None
    maxGpus: Optional[int] = None


class ListRunTasksRequest(BaseValidatorModel):
    id: str
    status: Optional[TaskStatusType] = None
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


class RunListItem(BaseValidatorModel):
    arn: Optional[str] = None
    id: Optional[str] = None
    status: Optional[RunStatusType] = None
    workflowId: Optional[str] = None
    name: Optional[str] = None
    priority: Optional[int] = None
    storageCapacity: Optional[int] = None
    creationTime: Optional[datetime] = None
    startTime: Optional[datetime] = None
    stopTime: Optional[datetime] = None
    storageType: Optional[StorageTypeType] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class ListVariantImportJobsFilter(BaseValidatorModel):
    status: Optional[JobStatusType] = None
    storeName: Optional[str] = None


class VariantImportJobItem(BaseValidatorModel):
    id: str
    destinationName: str
    roleArn: str
    status: JobStatusType
    creationTime: datetime
    updateTime: datetime
    completionTime: Optional[datetime] = None
    runLeftNormalization: Optional[bool] = None
    annotationFields: Optional[Dict[str, str]] = None


class ListVariantStoresFilter(BaseValidatorModel):
    status: Optional[StoreStatusType] = None


class ListWorkflowsRequest(BaseValidatorModel):
    type: Optional[WorkflowTypeType] = None
    name: Optional[str] = None
    startingToken: Optional[str] = None
    maxResults: Optional[int] = None


class WorkflowListItem(BaseValidatorModel):
    arn: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    status: Optional[WorkflowStatusType] = None
    type: Optional[WorkflowTypeType] = None
    digest: Optional[str] = None
    creationTime: Optional[datetime] = None
    metadata: Optional[Dict[str, str]] = None


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
    tags: Optional[Dict[str, str]] = None


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
    parameters: Optional[Dict[str, Any]] = None
    storageCapacity: Optional[int] = None
    outputUri: Optional[str] = None
    logLevel: Optional[RunLogLevelType] = None
    tags: Optional[Dict[str, str]] = None
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
    formatToHeader: Optional[Dict[FormatToHeaderKeyType, str]] = None
    schema: Optional[List[Dict[str, SchemaValueTypeType]]] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class TsvVersionOptionsOutput(BaseValidatorModel):
    annotationType: Optional[AnnotationTypeType] = None
    formatToHeader: Optional[Dict[FormatToHeaderKeyType, str]] = None
    schema: Optional[List[Dict[str, SchemaValueTypeType]]] = None


class TsvVersionOptions(BaseValidatorModel):
    annotationType: Optional[AnnotationTypeType] = None
    formatToHeader: Optional[Dict[FormatToHeaderKeyType, str]] = None
    schema: Optional[List[Dict[str, SchemaValueTypeType]]] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class UpdateAnnotationStoreRequest(BaseValidatorModel):
    name: str
    description: Optional[str] = None


class UpdateAnnotationStoreVersionRequest(BaseValidatorModel):
    name: str
    versionName: str
    description: Optional[str] = None


class UpdateRunCacheRequest(BaseValidatorModel):
    id: str
    cacheBehavior: Optional[CacheBehaviorType] = None
    description: Optional[str] = None
    name: Optional[str] = None


class UpdateRunGroupRequest(BaseValidatorModel):
    id: str
    name: Optional[str] = None
    maxCpus: Optional[int] = None
    maxRuns: Optional[int] = None
    maxDuration: Optional[int] = None
    maxGpus: Optional[int] = None


class UpdateVariantStoreRequest(BaseValidatorModel):
    name: str
    description: Optional[str] = None


class UpdateWorkflowRequest(BaseValidatorModel):
    id: str
    name: Optional[str] = None
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


class CreateRunCacheResponse(BaseValidatorModel):
    arn: str
    id: str
    status: RunCacheStatusType
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateRunGroupResponse(BaseValidatorModel):
    arn: str
    id: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateShareResponse(BaseValidatorModel):
    shareId: str
    status: ShareStatusType
    shareName: str
    ResponseMetadata: ResponseMetadata


class CreateWorkflowResponse(BaseValidatorModel):
    arn: str
    id: str
    status: WorkflowStatusType
    tags: Dict[str, str]
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


class GetRunCacheResponse(BaseValidatorModel):
    arn: str
    cacheBehavior: CacheBehaviorType
    cacheBucketOwnerId: str
    cacheS3Uri: str
    creationTime: datetime
    description: str
    id: str
    name: str
    status: RunCacheStatusType
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetRunGroupResponse(BaseValidatorModel):
    arn: str
    id: str
    name: str
    maxCpus: int
    maxRuns: int
    maxDuration: int
    creationTime: datetime
    tags: Dict[str, str]
    maxGpus: int
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


class StartReadSetActivationJobResponse(BaseValidatorModel):
    id: str
    sequenceStoreId: str
    status: ReadSetActivationJobStatusType
    creationTime: datetime
    ResponseMetadata: ResponseMetadata


class StartReadSetExportJobResponse(BaseValidatorModel):
    id: str
    sequenceStoreId: str
    destination: str
    status: ReadSetExportJobStatusType
    creationTime: datetime
    ResponseMetadata: ResponseMetadata


class StartReadSetImportJobResponse(BaseValidatorModel):
    id: str
    sequenceStoreId: str
    roleArn: str
    status: ReadSetImportJobStatusType
    creationTime: datetime
    ResponseMetadata: ResponseMetadata


class StartReferenceImportJobResponse(BaseValidatorModel):
    id: str
    referenceStoreId: str
    roleArn: str
    status: ReferenceImportJobStatusType
    creationTime: datetime
    ResponseMetadata: ResponseMetadata


class StartRunResponse(BaseValidatorModel):
    arn: str
    id: str
    status: RunStatusType
    tags: Dict[str, str]
    uuid: str
    runOutputUri: str
    ResponseMetadata: ResponseMetadata


class StartVariantImportResponse(BaseValidatorModel):
    jobId: str
    ResponseMetadata: ResponseMetadata


class UpdateAnnotationStoreVersionResponse(BaseValidatorModel):
    storeId: str
    id: str
    status: VersionStatusType
    name: str
    versionName: str
    description: str
    creationTime: datetime
    updateTime: datetime
    ResponseMetadata: ResponseMetadata


class UploadReadSetPartResponse(BaseValidatorModel):
    checksum: str
    ResponseMetadata: ResponseMetadata


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


class ListReadSetActivationJobsResponse(BaseValidatorModel):
    activationJobs: List[ActivateReadSetJobItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetReadSetActivationJobResponse(BaseValidatorModel):
    id: str
    sequenceStoreId: str
    status: ReadSetActivationJobStatusType
    statusMessage: str
    creationTime: datetime
    completionTime: datetime
    sources: List[ActivateReadSetSourceItem]
    ResponseMetadata: ResponseMetadata


class ListAnnotationImportJobsResponse(BaseValidatorModel):
    annotationImportJobs: List[AnnotationImportJobItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreateVariantStoreResponse(BaseValidatorModel):
    id: str
    reference: ReferenceItem
    status: StoreStatusType
    name: str
    creationTime: datetime
    ResponseMetadata: ResponseMetadata


class UpdateVariantStoreResponse(BaseValidatorModel):
    id: str
    reference: ReferenceItem
    status: StoreStatusType
    name: str
    description: str
    creationTime: datetime
    updateTime: datetime
    ResponseMetadata: ResponseMetadata


class AnnotationStoreItem(BaseValidatorModel):
    id: str
    reference: ReferenceItem
    status: StoreStatusType
    storeArn: str
    name: str
    storeFormat: StoreFormatType
    description: str
    sseConfig: SseConfig
    creationTime: datetime
    updateTime: datetime
    statusMessage: str
    storeSizeBytes: int


class CreateReferenceStoreRequest(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    sseConfig: Optional[SseConfig] = None
    tags: Optional[Dict[str, str]] = None
    clientToken: Optional[str] = None


class CreateReferenceStoreResponse(BaseValidatorModel):
    id: str
    arn: str
    name: str
    description: str
    sseConfig: SseConfig
    creationTime: datetime
    ResponseMetadata: ResponseMetadata


class CreateVariantStoreRequest(BaseValidatorModel):
    reference: ReferenceItem
    name: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    sseConfig: Optional[SseConfig] = None


class GetReferenceStoreResponse(BaseValidatorModel):
    id: str
    arn: str
    name: str
    description: str
    sseConfig: SseConfig
    creationTime: datetime
    ResponseMetadata: ResponseMetadata


class GetVariantStoreResponse(BaseValidatorModel):
    id: str
    reference: ReferenceItem
    status: StoreStatusType
    storeArn: str
    name: str
    description: str
    sseConfig: SseConfig
    creationTime: datetime
    updateTime: datetime
    tags: Dict[str, str]
    statusMessage: str
    storeSizeBytes: int
    ResponseMetadata: ResponseMetadata


class ReferenceStoreDetail(BaseValidatorModel):
    arn: str
    id: str
    creationTime: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    sseConfig: Optional[SseConfig] = None


class SequenceStoreDetail(BaseValidatorModel):
    arn: str
    id: str
    creationTime: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    sseConfig: Optional[SseConfig] = None
    fallbackLocation: Optional[str] = None
    eTagAlgorithmFamily: Optional[ETagAlgorithmFamilyType] = None
    status: Optional[SequenceStoreStatusType] = None
    statusMessage: Optional[str] = None
    updateTime: Optional[datetime] = None


class VariantStoreItem(BaseValidatorModel):
    id: str
    reference: ReferenceItem
    status: StoreStatusType
    storeArn: str
    name: str
    description: str
    sseConfig: SseConfig
    creationTime: datetime
    updateTime: datetime
    statusMessage: str
    storeSizeBytes: int


class ListAnnotationStoreVersionsResponse(BaseValidatorModel):
    annotationStoreVersions: List[AnnotationStoreVersionItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class BatchDeleteReadSetResponse(BaseValidatorModel):
    errors: List[ReadSetBatchError]
    ResponseMetadata: ResponseMetadata


class UploadReadSetPartRequest(BaseValidatorModel):
    sequenceStoreId: str
    uploadId: str
    partSource: ReadSetPartSourceType
    partNumber: int
    payload: Blob


class CompleteMultipartReadSetUploadRequest(BaseValidatorModel):
    sequenceStoreId: str
    uploadId: str
    parts: List[CompleteReadSetUploadPartListItem]


class CreateSequenceStoreRequest(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    sseConfig: Optional[SseConfig] = None
    tags: Optional[Dict[str, str]] = None
    clientToken: Optional[str] = None
    fallbackLocation: Optional[str] = None
    eTagAlgorithmFamily: Optional[ETagAlgorithmFamilyType] = None
    propagatedSetLevelTags: Optional[List[str]] = None
    s3AccessConfig: Optional[S3AccessConfig] = None


class UpdateSequenceStoreRequest(BaseValidatorModel):
    id: str
    name: Optional[str] = None
    description: Optional[str] = None
    clientToken: Optional[str] = None
    fallbackLocation: Optional[str] = None
    propagatedSetLevelTags: Optional[List[str]] = None
    s3AccessConfig: Optional[S3AccessConfig] = None


class CreateSequenceStoreResponse(BaseValidatorModel):
    id: str
    arn: str
    name: str
    description: str
    sseConfig: SseConfig
    creationTime: datetime
    fallbackLocation: str
    eTagAlgorithmFamily: ETagAlgorithmFamilyType
    status: SequenceStoreStatusType
    statusMessage: str
    propagatedSetLevelTags: List[str]
    s3Access: SequenceStoreS3Access
    ResponseMetadata: ResponseMetadata


class GetSequenceStoreResponse(BaseValidatorModel):
    id: str
    arn: str
    name: str
    description: str
    sseConfig: SseConfig
    creationTime: datetime
    fallbackLocation: str
    s3Access: SequenceStoreS3Access
    eTagAlgorithmFamily: ETagAlgorithmFamilyType
    status: SequenceStoreStatusType
    statusMessage: str
    propagatedSetLevelTags: List[str]
    updateTime: datetime
    ResponseMetadata: ResponseMetadata


class UpdateSequenceStoreResponse(BaseValidatorModel):
    id: str
    arn: str
    name: str
    description: str
    sseConfig: SseConfig
    creationTime: datetime
    updateTime: datetime
    propagatedSetLevelTags: List[str]
    status: SequenceStoreStatusType
    statusMessage: str
    fallbackLocation: str
    s3Access: SequenceStoreS3Access
    eTagAlgorithmFamily: ETagAlgorithmFamilyType
    ResponseMetadata: ResponseMetadata


class CreateWorkflowRequest(BaseValidatorModel):
    requestId: str
    name: Optional[str] = None
    description: Optional[str] = None
    engine: Optional[WorkflowEngineType] = None
    definitionZip: Optional[Blob] = None
    definitionUri: Optional[str] = None
    main: Optional[str] = None
    parameterTemplate: Optional[Dict[str, WorkflowParameter]] = None
    storageCapacity: Optional[int] = None
    tags: Optional[Dict[str, str]] = None
    accelerators: Optional[Literal['GPU']] = None


class GetWorkflowResponse(BaseValidatorModel):
    arn: str
    id: str
    status: WorkflowStatusType
    type: WorkflowTypeType
    name: str
    description: str
    engine: WorkflowEngineType
    definition: str
    main: str
    digest: str
    parameterTemplate: Dict[str, WorkflowParameter]
    storageCapacity: int
    creationTime: datetime
    statusMessage: str
    tags: Dict[str, str]
    metadata: Dict[str, str]
    accelerators: Literal['GPU']
    ResponseMetadata: ResponseMetadata


class DeleteAnnotationStoreVersionsResponse(BaseValidatorModel):
    errors: List[VersionDeleteError]
    ResponseMetadata: ResponseMetadata


class GetReadSetExportJobResponse(BaseValidatorModel):
    id: str
    sequenceStoreId: str
    destination: str
    status: ReadSetExportJobStatusType
    statusMessage: str
    creationTime: datetime
    completionTime: datetime
    readSets: List[ExportReadSetDetail]
    ResponseMetadata: ResponseMetadata


class ListReadSetExportJobsResponse(BaseValidatorModel):
    exportJobs: List[ExportReadSetJobDetail]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class StartReadSetExportJobRequest(BaseValidatorModel):
    sequenceStoreId: str
    destination: str
    roleArn: str
    sources: List[ExportReadSet]
    clientToken: Optional[str] = None


class FileInformation(BaseValidatorModel):
    totalParts: Optional[int] = None
    partSize: Optional[int] = None
    contentLength: Optional[int] = None
    s3Access: Optional[ReadSetS3Access] = None


class ListSharesRequest(BaseValidatorModel):
    resourceOwner: ResourceOwnerType
    filter: Optional[Filter] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


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


class GetReadSetActivationJobRequestWait(BaseValidatorModel):
    id: str
    sequenceStoreId: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetReadSetExportJobRequestWait(BaseValidatorModel):
    sequenceStoreId: str
    id: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetReadSetImportJobRequestWait(BaseValidatorModel):
    id: str
    sequenceStoreId: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetReferenceImportJobRequestWait(BaseValidatorModel):
    id: str
    referenceStoreId: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetRunRequestWaitExtra(BaseValidatorModel):
    id: str
    export: Optional[List[Literal['DEFINITION']]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class GetRunRequestWait(BaseValidatorModel):
    id: str
    export: Optional[List[Literal['DEFINITION']]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class GetRunTaskRequestWaitExtra(BaseValidatorModel):
    id: str
    taskId: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetRunTaskRequestWait(BaseValidatorModel):
    id: str
    taskId: str
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


class GetWorkflowRequestWait(BaseValidatorModel):
    id: str
    type: Optional[WorkflowTypeType] = None
    export: Optional[List[Literal['DEFINITION']]] = None
    workflowOwnerId: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class ReadSetListItem(BaseValidatorModel):
    id: str
    arn: str
    sequenceStoreId: str
    status: ReadSetStatusType
    fileType: FileTypeType
    creationTime: datetime
    subjectId: Optional[str] = None
    sampleId: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    referenceArn: Optional[str] = None
    sequenceInformation: Optional[SequenceInformation] = None
    statusMessage: Optional[str] = None
    creationType: Optional[CreationTypeType] = None
    etag: Optional[ETag] = None


class GetReferenceImportJobResponse(BaseValidatorModel):
    id: str
    referenceStoreId: str
    roleArn: str
    status: ReferenceImportJobStatusType
    statusMessage: str
    creationTime: datetime
    completionTime: datetime
    sources: List[ImportReferenceSourceItem]
    ResponseMetadata: ResponseMetadata


class GetRunResponse(BaseValidatorModel):
    arn: str
    id: str
    cacheId: str
    cacheBehavior: CacheBehaviorType
    engineVersion: str
    status: RunStatusType
    workflowId: str
    workflowType: WorkflowTypeType
    runId: str
    roleArn: str
    name: str
    runGroupId: str
    priority: int
    definition: str
    digest: str
    parameters: Dict[str, Any]
    storageCapacity: int
    outputUri: str
    logLevel: RunLogLevelType
    resourceDigests: Dict[str, str]
    startedBy: str
    creationTime: datetime
    startTime: datetime
    stopTime: datetime
    statusMessage: str
    tags: Dict[str, str]
    accelerators: Literal['GPU']
    retentionMode: RunRetentionModeType
    failureReason: str
    logLocation: RunLogLocation
    uuid: str
    runOutputUri: str
    storageType: StorageTypeType
    workflowOwnerId: str
    ResponseMetadata: ResponseMetadata


class GetShareResponse(BaseValidatorModel):
    share: ShareDetails
    ResponseMetadata: ResponseMetadata


class ListSharesResponse(BaseValidatorModel):
    shares: List[ShareDetails]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetVariantImportResponse(BaseValidatorModel):
    id: str
    destinationName: str
    roleArn: str
    status: JobStatusType
    statusMessage: str
    creationTime: datetime
    updateTime: datetime
    completionTime: datetime
    items: List[VariantImportItemDetail]
    runLeftNormalization: bool
    annotationFields: Dict[str, str]
    ResponseMetadata: ResponseMetadata


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
    tags: Optional[Dict[str, str]] = None


class ListReferenceImportJobsResponse(BaseValidatorModel):
    importJobs: List[ImportReferenceJobItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListAnnotationImportJobsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    ids: Optional[List[str]] = None
    nextToken: Optional[str] = None
    filter: Optional[ListAnnotationImportJobsFilter] = None


class ListAnnotationImportJobsRequestPaginate(BaseValidatorModel):
    ids: Optional[List[str]] = None
    filter: Optional[ListAnnotationImportJobsFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMultipartReadSetUploadsRequestPaginate(BaseValidatorModel):
    sequenceStoreId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRunCachesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRunGroupsRequestPaginate(BaseValidatorModel):
    name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRunTasksRequestPaginate(BaseValidatorModel):
    id: str
    status: Optional[TaskStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRunsRequestPaginate(BaseValidatorModel):
    name: Optional[str] = None
    runGroupId: Optional[str] = None
    status: Optional[RunStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSharesRequestPaginate(BaseValidatorModel):
    resourceOwner: ResourceOwnerType
    filter: Optional[Filter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWorkflowsRequestPaginate(BaseValidatorModel):
    type: Optional[WorkflowTypeType] = None
    name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAnnotationStoreVersionsRequestPaginate(BaseValidatorModel):
    name: str
    filter: Optional[ListAnnotationStoreVersionsFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAnnotationStoreVersionsRequest(BaseValidatorModel):
    name: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filter: Optional[ListAnnotationStoreVersionsFilter] = None


class ListAnnotationStoresRequestPaginate(BaseValidatorModel):
    ids: Optional[List[str]] = None
    filter: Optional[ListAnnotationStoresFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAnnotationStoresRequest(BaseValidatorModel):
    ids: Optional[List[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filter: Optional[ListAnnotationStoresFilter] = None


class ListMultipartReadSetUploadsResponse(BaseValidatorModel):
    uploads: List[MultipartReadSetUploadListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListReadSetUploadPartsResponse(BaseValidatorModel):
    parts: List[ReadSetUploadPartListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListReferencesResponse(BaseValidatorModel):
    references: List[ReferenceListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListRunCachesResponse(BaseValidatorModel):
    items: List[RunCacheListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListRunGroupsResponse(BaseValidatorModel):
    items: List[RunGroupListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListRunTasksResponse(BaseValidatorModel):
    items: List[TaskListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListRunsResponse(BaseValidatorModel):
    items: List[RunListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListVariantImportJobsRequestPaginate(BaseValidatorModel):
    ids: Optional[List[str]] = None
    filter: Optional[ListVariantImportJobsFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListVariantImportJobsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    ids: Optional[List[str]] = None
    nextToken: Optional[str] = None
    filter: Optional[ListVariantImportJobsFilter] = None


class ListVariantImportJobsResponse(BaseValidatorModel):
    variantImportJobs: List[VariantImportJobItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListVariantStoresRequestPaginate(BaseValidatorModel):
    ids: Optional[List[str]] = None
    filter: Optional[ListVariantStoresFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListVariantStoresRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    ids: Optional[List[str]] = None
    nextToken: Optional[str] = None
    filter: Optional[ListVariantStoresFilter] = None


class ListWorkflowsResponse(BaseValidatorModel):
    items: List[WorkflowListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class TsvOptions(BaseValidatorModel):
    readOptions: Optional[ReadOptions] = None


class StartReadSetActivationJobRequest(BaseValidatorModel):
    sequenceStoreId: str
    sources: List[StartReadSetActivationJobSourceItem]
    clientToken: Optional[str] = None


class StartReferenceImportJobRequest(BaseValidatorModel):
    referenceStoreId: str
    roleArn: str
    sources: List[StartReferenceImportJobSourceItem]
    clientToken: Optional[str] = None


class StartVariantImportRequest(BaseValidatorModel):
    destinationName: str
    roleArn: str
    items: List[VariantImportItemSource]
    runLeftNormalization: Optional[bool] = None
    annotationFields: Optional[Dict[str, str]] = None


class StoreOptionsOutput(BaseValidatorModel):
    tsvStoreOptions: Optional[TsvStoreOptionsOutput] = None


class StoreOptions(BaseValidatorModel):
    tsvStoreOptions: Optional[TsvStoreOptions] = None


class VersionOptionsOutput(BaseValidatorModel):
    tsvVersionOptions: Optional[TsvVersionOptionsOutput] = None


class VersionOptions(BaseValidatorModel):
    tsvVersionOptions: Optional[TsvVersionOptions] = None


class ListReadSetActivationJobsRequestPaginate(BaseValidatorModel):
    sequenceStoreId: str
    filter: Optional[ActivateReadSetFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListReadSetActivationJobsRequest(BaseValidatorModel):
    sequenceStoreId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filter: Optional[ActivateReadSetFilter] = None


class ListReadSetExportJobsRequestPaginate(BaseValidatorModel):
    sequenceStoreId: str
    filter: Optional[ExportReadSetFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListReadSetExportJobsRequest(BaseValidatorModel):
    sequenceStoreId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filter: Optional[ExportReadSetFilter] = None


class ListReadSetImportJobsRequestPaginate(BaseValidatorModel):
    sequenceStoreId: str
    filter: Optional[ImportReadSetFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListReadSetImportJobsRequest(BaseValidatorModel):
    sequenceStoreId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filter: Optional[ImportReadSetFilter] = None


class ListReferenceImportJobsRequestPaginate(BaseValidatorModel):
    referenceStoreId: str
    filter: Optional[ImportReferenceFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListReferenceImportJobsRequest(BaseValidatorModel):
    referenceStoreId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filter: Optional[ImportReferenceFilter] = None


class ListReadSetsRequestPaginate(BaseValidatorModel):
    sequenceStoreId: str
    filter: Optional[ReadSetFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListReadSetsRequest(BaseValidatorModel):
    sequenceStoreId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filter: Optional[ReadSetFilter] = None


class ListReadSetUploadPartsRequestPaginate(BaseValidatorModel):
    sequenceStoreId: str
    uploadId: str
    partSource: ReadSetPartSourceType
    filter: Optional[ReadSetUploadPartListFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListReadSetUploadPartsRequest(BaseValidatorModel):
    sequenceStoreId: str
    uploadId: str
    partSource: ReadSetPartSourceType
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filter: Optional[ReadSetUploadPartListFilter] = None


class ListReferencesRequestPaginate(BaseValidatorModel):
    referenceStoreId: str
    filter: Optional[ReferenceFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListReferencesRequest(BaseValidatorModel):
    referenceStoreId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filter: Optional[ReferenceFilter] = None


class ListReferenceStoresRequestPaginate(BaseValidatorModel):
    filter: Optional[ReferenceStoreFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListReferenceStoresRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filter: Optional[ReferenceStoreFilter] = None


class ListSequenceStoresRequestPaginate(BaseValidatorModel):
    filter: Optional[SequenceStoreFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSequenceStoresRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filter: Optional[SequenceStoreFilter] = None


class ListAnnotationStoresResponse(BaseValidatorModel):
    annotationStores: List[AnnotationStoreItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListReferenceStoresResponse(BaseValidatorModel):
    referenceStores: List[ReferenceStoreDetail]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListSequenceStoresResponse(BaseValidatorModel):
    sequenceStores: List[SequenceStoreDetail]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


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


class ListReadSetsResponse(BaseValidatorModel):
    readSets: List[ReadSetListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetReadSetImportJobResponse(BaseValidatorModel):
    id: str
    sequenceStoreId: str
    roleArn: str
    status: ReadSetImportJobStatusType
    statusMessage: str
    creationTime: datetime
    completionTime: datetime
    sources: List[ImportReadSetSourceItem]
    ResponseMetadata: ResponseMetadata


class StartReadSetImportJobRequest(BaseValidatorModel):
    sequenceStoreId: str
    roleArn: str
    sources: List[StartReadSetImportJobSourceItem]
    clientToken: Optional[str] = None


class FormatOptions(BaseValidatorModel):
    tsvOptions: Optional[TsvOptions] = None
    vcfOptions: Optional[VcfOptions] = None


class CreateAnnotationStoreResponse(BaseValidatorModel):
    id: str
    reference: ReferenceItem
    storeFormat: StoreFormatType
    storeOptions: StoreOptionsOutput
    status: StoreStatusType
    name: str
    versionName: str
    creationTime: datetime
    ResponseMetadata: ResponseMetadata


class GetAnnotationStoreResponse(BaseValidatorModel):
    id: str
    reference: ReferenceItem
    status: StoreStatusType
    storeArn: str
    name: str
    description: str
    sseConfig: SseConfig
    creationTime: datetime
    updateTime: datetime
    tags: Dict[str, str]
    storeOptions: StoreOptionsOutput
    storeFormat: StoreFormatType
    statusMessage: str
    storeSizeBytes: int
    numVersions: int
    ResponseMetadata: ResponseMetadata


class UpdateAnnotationStoreResponse(BaseValidatorModel):
    id: str
    reference: ReferenceItem
    status: StoreStatusType
    name: str
    description: str
    creationTime: datetime
    updateTime: datetime
    storeOptions: StoreOptionsOutput
    storeFormat: StoreFormatType
    ResponseMetadata: ResponseMetadata

StoreOptionsUnion = Union[StoreOptions, StoreOptionsOutput]


class CreateAnnotationStoreVersionResponse(BaseValidatorModel):
    id: str
    versionName: str
    storeId: str
    versionOptions: VersionOptionsOutput
    name: str
    status: VersionStatusType
    creationTime: datetime
    ResponseMetadata: ResponseMetadata


class GetAnnotationStoreVersionResponse(BaseValidatorModel):
    storeId: str
    id: str
    status: VersionStatusType
    versionArn: str
    name: str
    versionName: str
    description: str
    creationTime: datetime
    updateTime: datetime
    tags: Dict[str, str]
    versionOptions: VersionOptionsOutput
    statusMessage: str
    versionSizeBytes: int
    ResponseMetadata: ResponseMetadata

VersionOptionsUnion = Union[VersionOptions, VersionOptionsOutput]


class GetReadSetMetadataResponse(BaseValidatorModel):
    id: str
    arn: str
    sequenceStoreId: str
    subjectId: str
    sampleId: str
    status: ReadSetStatusType
    name: str
    description: str
    fileType: FileTypeType
    creationTime: datetime
    sequenceInformation: SequenceInformation
    referenceArn: str
    files: ReadSetFiles
    statusMessage: str
    creationType: CreationTypeType
    etag: ETag
    creationJobId: str
    ResponseMetadata: ResponseMetadata


class GetReferenceMetadataResponse(BaseValidatorModel):
    id: str
    arn: str
    referenceStoreId: str
    md5: str
    status: ReferenceStatusType
    name: str
    description: str
    creationTime: datetime
    updateTime: datetime
    files: ReferenceFiles
    creationType: Literal['IMPORT']
    creationJobId: str
    ResponseMetadata: ResponseMetadata


class GetAnnotationImportResponse(BaseValidatorModel):
    id: str
    destinationName: str
    versionName: str
    roleArn: str
    status: JobStatusType
    statusMessage: str
    creationTime: datetime
    updateTime: datetime
    completionTime: datetime
    items: List[AnnotationImportItemDetail]
    runLeftNormalization: bool
    formatOptions: FormatOptions
    annotationFields: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class StartAnnotationImportRequest(BaseValidatorModel):
    destinationName: str
    roleArn: str
    items: List[AnnotationImportItemSource]
    versionName: Optional[str] = None
    formatOptions: Optional[FormatOptions] = None
    runLeftNormalization: Optional[bool] = None
    annotationFields: Optional[Dict[str, str]] = None


class CreateAnnotationStoreRequest(BaseValidatorModel):
    storeFormat: StoreFormatType
    reference: Optional[ReferenceItem] = None
    name: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    versionName: Optional[str] = None
    sseConfig: Optional[SseConfig] = None
    storeOptions: Optional[StoreOptionsUnion] = None


class CreateAnnotationStoreVersionRequest(BaseValidatorModel):
    name: str
    versionName: str
    description: Optional[str] = None
    versionOptions: Optional[VersionOptionsUnion] = None
    tags: Optional[Dict[str, str]] = None