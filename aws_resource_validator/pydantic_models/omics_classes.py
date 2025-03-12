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

class AbortMultipartReadSetUploadRequestTypeDef(BaseValidatorModel):
    sequenceStoreId: str
    uploadId: str


class AcceptShareRequestTypeDef(BaseValidatorModel):
    shareId: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ActivateReadSetSourceItemTypeDef(BaseValidatorModel):
    readSetId: str
    status: ReadSetActivationJobItemStatusType
    statusMessage: Optional[str] = None


class AnnotationImportItemDetailTypeDef(BaseValidatorModel):
    source: str
    jobStatus: JobStatusType


class AnnotationImportItemSourceTypeDef(BaseValidatorModel):
    source: str


class ReferenceItemTypeDef(BaseValidatorModel):
    referenceArn: Optional[str] = None


class BatchDeleteReadSetRequestTypeDef(BaseValidatorModel):
    ids: Sequence[str]
    sequenceStoreId: str


class CancelAnnotationImportRequestTypeDef(BaseValidatorModel):
    jobId: str


class CancelVariantImportRequestTypeDef(BaseValidatorModel):
    jobId: str


class CompleteReadSetUploadPartListItemTypeDef(BaseValidatorModel):
    partNumber: int
    partSource: ReadSetPartSourceType
    checksum: str


class CreateMultipartReadSetUploadRequestTypeDef(BaseValidatorModel):
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


class CreateRunCacheRequestTypeDef(BaseValidatorModel):
    cacheS3Location: str
    requestId: str
    cacheBehavior: Optional[CacheBehaviorType] = None
    description: Optional[str] = None
    name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    cacheBucketOwnerId: Optional[str] = None


class CreateRunGroupRequestTypeDef(BaseValidatorModel):
    requestId: str
    name: Optional[str] = None
    maxCpus: Optional[int] = None
    maxRuns: Optional[int] = None
    maxDuration: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None
    maxGpus: Optional[int] = None


class S3AccessConfigTypeDef(BaseValidatorModel):
    accessLogLocation: Optional[str] = None


class SequenceStoreS3AccessTypeDef(BaseValidatorModel):
    s3Uri: Optional[str] = None
    s3AccessPointArn: Optional[str] = None
    accessLogLocation: Optional[str] = None


class CreateShareRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    principalSubscriber: str
    shareName: Optional[str] = None


class WorkflowParameterTypeDef(BaseValidatorModel):
    description: Optional[str] = None
    optional: Optional[bool] = None


class DeleteAnnotationStoreRequestTypeDef(BaseValidatorModel):
    name: str
    force: Optional[bool] = None


class DeleteAnnotationStoreVersionsRequestTypeDef(BaseValidatorModel):
    name: str
    versions: Sequence[str]
    force: Optional[bool] = None


class VersionDeleteErrorTypeDef(BaseValidatorModel):
    versionName: str
    message: str


class DeleteS3AccessPolicyRequestTypeDef(BaseValidatorModel):
    s3AccessPointArn: str


class DeleteShareRequestTypeDef(BaseValidatorModel):
    shareId: str


class DeleteVariantStoreRequestTypeDef(BaseValidatorModel):
    name: str
    force: Optional[bool] = None


class ETagTypeDef(BaseValidatorModel):
    algorithm: Optional[ETagAlgorithmType] = None
    source1: Optional[str] = None
    source2: Optional[str] = None


class ExportReadSetTypeDef(BaseValidatorModel):
    readSetId: str


class ReadSetS3AccessTypeDef(BaseValidatorModel):
    s3Uri: Optional[str] = None


class VcfOptionsTypeDef(BaseValidatorModel):
    ignoreQualField: Optional[bool] = None
    ignoreFilterField: Optional[bool] = None


class GetAnnotationImportRequestTypeDef(BaseValidatorModel):
    jobId: str


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class GetAnnotationStoreRequestTypeDef(BaseValidatorModel):
    name: str


class GetAnnotationStoreVersionRequestTypeDef(BaseValidatorModel):
    name: str
    versionName: str


class SequenceInformationTypeDef(BaseValidatorModel):
    totalReadCount: Optional[int] = None
    totalBaseCount: Optional[int] = None
    generatedFrom: Optional[str] = None
    alignment: Optional[str] = None


class ImportReferenceSourceItemTypeDef(BaseValidatorModel):
    status: ReferenceImportJobItemStatusType
    sourceFile: Optional[str] = None
    statusMessage: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    referenceId: Optional[str] = None


class RunLogLocationTypeDef(BaseValidatorModel):
    engineLogStream: Optional[str] = None
    runLogStream: Optional[str] = None


class GetS3AccessPolicyRequestTypeDef(BaseValidatorModel):
    s3AccessPointArn: str


class GetShareRequestTypeDef(BaseValidatorModel):
    shareId: str


class ShareDetailsTypeDef(BaseValidatorModel):
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


class GetVariantImportRequestTypeDef(BaseValidatorModel):
    jobId: str


class VariantImportItemDetailTypeDef(BaseValidatorModel):
    source: str
    jobStatus: JobStatusType
    statusMessage: Optional[str] = None


class GetVariantStoreRequestTypeDef(BaseValidatorModel):
    name: str


class SourceFilesTypeDef(BaseValidatorModel):
    source1: str
    source2: Optional[str] = None


class ListAnnotationImportJobsFilterTypeDef(BaseValidatorModel):
    status: Optional[JobStatusType] = None
    storeName: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAnnotationStoreVersionsFilterTypeDef(BaseValidatorModel):
    status: Optional[VersionStatusType] = None


class ListAnnotationStoresFilterTypeDef(BaseValidatorModel):
    status: Optional[StoreStatusType] = None


class ListMultipartReadSetUploadsRequestTypeDef(BaseValidatorModel):
    sequenceStoreId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class MultipartReadSetUploadListItemTypeDef(BaseValidatorModel):
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


class ReadSetUploadPartListItemTypeDef(BaseValidatorModel):
    partNumber: int
    partSize: int
    partSource: ReadSetPartSourceType
    checksum: str
    creationTime: Optional[datetime] = None
    lastUpdatedTime: Optional[datetime] = None


class ListRunCachesRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    startingToken: Optional[str] = None


class ListRunGroupsRequestTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    startingToken: Optional[str] = None
    maxResults: Optional[int] = None


class TaskListItemTypeDef(BaseValidatorModel):
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


class ListRunsRequestTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    runGroupId: Optional[str] = None
    startingToken: Optional[str] = None
    maxResults: Optional[int] = None
    status: Optional[RunStatusType] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class ListVariantImportJobsFilterTypeDef(BaseValidatorModel):
    status: Optional[JobStatusType] = None
    storeName: Optional[str] = None


class ListVariantStoresFilterTypeDef(BaseValidatorModel):
    status: Optional[StoreStatusType] = None


class PutS3AccessPolicyRequestTypeDef(BaseValidatorModel):
    s3AccessPointArn: str
    s3AccessPolicy: str


class ReadOptionsTypeDef(BaseValidatorModel):
    sep: Optional[str] = None
    encoding: Optional[str] = None
    quote: Optional[str] = None
    quoteAll: Optional[bool] = None
    escape: Optional[str] = None
    escapeQuotes: Optional[bool] = None
    comment: Optional[str] = None
    header: Optional[bool] = None
    lineSep: Optional[str] = None


class StartReadSetActivationJobSourceItemTypeDef(BaseValidatorModel):
    readSetId: str


class StartReferenceImportJobSourceItemTypeDef(BaseValidatorModel):
    sourceFile: str
    name: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class StartRunRequestTypeDef(BaseValidatorModel):
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


class VariantImportItemSourceTypeDef(BaseValidatorModel):
    source: str


class TsvStoreOptionsOutputTypeDef(BaseValidatorModel):
    annotationType: Optional[AnnotationTypeType] = None
    formatToHeader: Optional[Dict[FormatToHeaderKeyType, str]] = None
    schema: Optional[List[Dict[str, SchemaValueTypeType]]] = None


class TsvStoreOptionsTypeDef(BaseValidatorModel):
    annotationType: Optional[AnnotationTypeType] = None
    formatToHeader: Optional[Mapping[FormatToHeaderKeyType, str]] = None
    schema: Optional[Sequence[Mapping[str, SchemaValueTypeType]]] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class TsvVersionOptionsOutputTypeDef(BaseValidatorModel):
    annotationType: Optional[AnnotationTypeType] = None
    formatToHeader: Optional[Dict[FormatToHeaderKeyType, str]] = None
    schema: Optional[List[Dict[str, SchemaValueTypeType]]] = None


class TsvVersionOptionsTypeDef(BaseValidatorModel):
    annotationType: Optional[AnnotationTypeType] = None
    formatToHeader: Optional[Mapping[FormatToHeaderKeyType, str]] = None
    schema: Optional[Sequence[Mapping[str, SchemaValueTypeType]]] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateAnnotationStoreRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None


class UpdateAnnotationStoreVersionRequestTypeDef(BaseValidatorModel):
    name: str
    versionName: str
    description: Optional[str] = None


class UpdateVariantStoreRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None


class AcceptShareResponseTypeDef(BaseValidatorModel):
    status: ShareStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class CompleteMultipartReadSetUploadResponseTypeDef(BaseValidatorModel):
    readSetId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateMultipartReadSetUploadResponseTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef


class CreateShareResponseTypeDef(BaseValidatorModel):
    shareId: str
    status: ShareStatusType
    shareName: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteAnnotationStoreResponseTypeDef(BaseValidatorModel):
    status: StoreStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteShareResponseTypeDef(BaseValidatorModel):
    status: ShareStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteVariantStoreResponseTypeDef(BaseValidatorModel):
    status: StoreStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetReadSetResponseTypeDef(BaseValidatorModel):
    payload: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef


class GetReferenceResponseTypeDef(BaseValidatorModel):
    payload: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef


class GetRunTaskResponseTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef


class GetS3AccessPolicyResponseTypeDef(BaseValidatorModel):
    s3AccessPointArn: str
    storeId: str
    storeType: StoreTypeType
    updateTime: datetime
    s3AccessPolicy: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class PutS3AccessPolicyResponseTypeDef(BaseValidatorModel):
    s3AccessPointArn: str
    storeId: str
    storeType: StoreTypeType
    ResponseMetadata: ResponseMetadataTypeDef


class StartAnnotationImportResponseTypeDef(BaseValidatorModel):
    jobId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartVariantImportResponseTypeDef(BaseValidatorModel):
    jobId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UploadReadSetPartResponseTypeDef(BaseValidatorModel):
    checksum: str
    ResponseMetadata: ResponseMetadataTypeDef


class TimestampTypeDef(BaseValidatorModel):
    pass


class ActivateReadSetFilterTypeDef(BaseValidatorModel):
    status: Optional[ReadSetActivationJobStatusType] = None
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None


class ExportReadSetFilterTypeDef(BaseValidatorModel):
    status: Optional[ReadSetExportJobStatusType] = None
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None


class ImportReadSetFilterTypeDef(BaseValidatorModel):
    status: Optional[ReadSetImportJobStatusType] = None
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None


class ImportReferenceFilterTypeDef(BaseValidatorModel):
    status: Optional[ReferenceImportJobStatusType] = None
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None


class ReadSetFilterTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    status: Optional[ReadSetStatusType] = None
    referenceArn: Optional[str] = None
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None
    sampleId: Optional[str] = None
    subjectId: Optional[str] = None
    generatedFrom: Optional[str] = None
    creationType: Optional[CreationTypeType] = None


class ReadSetUploadPartListFilterTypeDef(BaseValidatorModel):
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None


class ReferenceFilterTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    md5: Optional[str] = None
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None


class ReferenceStoreFilterTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None


class SequenceStoreFilterTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None
    status: Optional[SequenceStoreStatusType] = None
    updatedAfter: Optional[TimestampTypeDef] = None
    updatedBefore: Optional[TimestampTypeDef] = None


class ActivateReadSetJobItemTypeDef(BaseValidatorModel):
    pass


class ListReadSetActivationJobsResponseTypeDef(BaseValidatorModel):
    activationJobs: List[ActivateReadSetJobItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AnnotationImportJobItemTypeDef(BaseValidatorModel):
    pass


class ListAnnotationImportJobsResponseTypeDef(BaseValidatorModel):
    annotationImportJobs: List[AnnotationImportJobItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SseConfigTypeDef(BaseValidatorModel):
    pass


class CreateReferenceStoreRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    sseConfig: Optional[SseConfigTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None


class CreateVariantStoreRequestTypeDef(BaseValidatorModel):
    reference: ReferenceItemTypeDef
    name: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    sseConfig: Optional[SseConfigTypeDef] = None


class AnnotationStoreVersionItemTypeDef(BaseValidatorModel):
    pass


class ListAnnotationStoreVersionsResponseTypeDef(BaseValidatorModel):
    annotationStoreVersions: List[AnnotationStoreVersionItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ReadSetBatchErrorTypeDef(BaseValidatorModel):
    pass


class BatchDeleteReadSetResponseTypeDef(BaseValidatorModel):
    errors: List[ReadSetBatchErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BlobTypeDef(BaseValidatorModel):
    pass


class UploadReadSetPartRequestTypeDef(BaseValidatorModel):
    sequenceStoreId: str
    uploadId: str
    partSource: ReadSetPartSourceType
    partNumber: int
    payload: BlobTypeDef


class CompleteMultipartReadSetUploadRequestTypeDef(BaseValidatorModel):
    sequenceStoreId: str
    uploadId: str
    parts: Sequence[CompleteReadSetUploadPartListItemTypeDef]


class CreateSequenceStoreRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    sseConfig: Optional[SseConfigTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None
    fallbackLocation: Optional[str] = None
    eTagAlgorithmFamily: Optional[ETagAlgorithmFamilyType] = None
    propagatedSetLevelTags: Optional[Sequence[str]] = None
    s3AccessConfig: Optional[S3AccessConfigTypeDef] = None


class CreateWorkflowRequestTypeDef(BaseValidatorModel):
    requestId: str
    name: Optional[str] = None
    description: Optional[str] = None
    engine: Optional[WorkflowEngineType] = None
    definitionZip: Optional[BlobTypeDef] = None
    definitionUri: Optional[str] = None
    main: Optional[str] = None
    parameterTemplate: Optional[Mapping[str, WorkflowParameterTypeDef]] = None
    storageCapacity: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None
    accelerators: Optional[Literal["GPU"]] = None


class DeleteAnnotationStoreVersionsResponseTypeDef(BaseValidatorModel):
    errors: List[VersionDeleteErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ExportReadSetJobDetailTypeDef(BaseValidatorModel):
    pass


class ListReadSetExportJobsResponseTypeDef(BaseValidatorModel):
    exportJobs: List[ExportReadSetJobDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class StartReadSetExportJobRequestTypeDef(BaseValidatorModel):
    sequenceStoreId: str
    destination: str
    roleArn: str
    sources: Sequence[ExportReadSetTypeDef]
    clientToken: Optional[str] = None


class FileInformationTypeDef(BaseValidatorModel):
    totalParts: Optional[int] = None
    partSize: Optional[int] = None
    contentLength: Optional[int] = None
    s3Access: Optional[ReadSetS3AccessTypeDef] = None


class GetAnnotationImportRequestWaitTypeDef(BaseValidatorModel):
    jobId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetAnnotationStoreRequestWaitExtraTypeDef(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetAnnotationStoreRequestWaitTypeDef(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetAnnotationStoreVersionRequestWaitExtraTypeDef(BaseValidatorModel):
    name: str
    versionName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetAnnotationStoreVersionRequestWaitTypeDef(BaseValidatorModel):
    name: str
    versionName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetVariantImportRequestWaitTypeDef(BaseValidatorModel):
    jobId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetVariantStoreRequestWaitExtraTypeDef(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetVariantStoreRequestWaitTypeDef(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetShareResponseTypeDef(BaseValidatorModel):
    share: ShareDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListSharesResponseTypeDef(BaseValidatorModel):
    shares: List[ShareDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ImportReadSetJobItemTypeDef(BaseValidatorModel):
    pass


class ListReadSetImportJobsResponseTypeDef(BaseValidatorModel):
    importJobs: List[ImportReadSetJobItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ImportReadSetSourceItemTypeDef(BaseValidatorModel):
    sourceFiles: SourceFilesTypeDef
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


class StartReadSetImportJobSourceItemTypeDef(BaseValidatorModel):
    sourceFiles: SourceFilesTypeDef
    sourceFileType: FileTypeType
    subjectId: str
    sampleId: str
    generatedFrom: Optional[str] = None
    referenceArn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class ImportReferenceJobItemTypeDef(BaseValidatorModel):
    pass


class ListReferenceImportJobsResponseTypeDef(BaseValidatorModel):
    importJobs: List[ImportReferenceJobItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListMultipartReadSetUploadsRequestPaginateTypeDef(BaseValidatorModel):
    sequenceStoreId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRunCachesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRunGroupsRequestPaginateTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRunsRequestPaginateTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    runGroupId: Optional[str] = None
    status: Optional[RunStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMultipartReadSetUploadsResponseTypeDef(BaseValidatorModel):
    uploads: List[MultipartReadSetUploadListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListReadSetUploadPartsResponseTypeDef(BaseValidatorModel):
    parts: List[ReadSetUploadPartListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ReferenceListItemTypeDef(BaseValidatorModel):
    pass


class ListReferencesResponseTypeDef(BaseValidatorModel):
    references: List[ReferenceListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RunCacheListItemTypeDef(BaseValidatorModel):
    pass


class ListRunCachesResponseTypeDef(BaseValidatorModel):
    items: List[RunCacheListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RunGroupListItemTypeDef(BaseValidatorModel):
    pass


class ListRunGroupsResponseTypeDef(BaseValidatorModel):
    items: List[RunGroupListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListRunTasksResponseTypeDef(BaseValidatorModel):
    items: List[TaskListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RunListItemTypeDef(BaseValidatorModel):
    pass


class ListRunsResponseTypeDef(BaseValidatorModel):
    items: List[RunListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class VariantImportJobItemTypeDef(BaseValidatorModel):
    pass


class ListVariantImportJobsResponseTypeDef(BaseValidatorModel):
    variantImportJobs: List[VariantImportJobItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class WorkflowListItemTypeDef(BaseValidatorModel):
    pass


class ListWorkflowsResponseTypeDef(BaseValidatorModel):
    items: List[WorkflowListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class TsvOptionsTypeDef(BaseValidatorModel):
    readOptions: Optional[ReadOptionsTypeDef] = None


class StartReadSetActivationJobRequestTypeDef(BaseValidatorModel):
    sequenceStoreId: str
    sources: Sequence[StartReadSetActivationJobSourceItemTypeDef]
    clientToken: Optional[str] = None


class StartReferenceImportJobRequestTypeDef(BaseValidatorModel):
    referenceStoreId: str
    roleArn: str
    sources: Sequence[StartReferenceImportJobSourceItemTypeDef]
    clientToken: Optional[str] = None


class StartVariantImportRequestTypeDef(BaseValidatorModel):
    destinationName: str
    roleArn: str
    items: Sequence[VariantImportItemSourceTypeDef]
    runLeftNormalization: Optional[bool] = None
    annotationFields: Optional[Mapping[str, str]] = None


class StoreOptionsOutputTypeDef(BaseValidatorModel):
    tsvStoreOptions: Optional[TsvStoreOptionsOutputTypeDef] = None


class StoreOptionsTypeDef(BaseValidatorModel):
    tsvStoreOptions: Optional[TsvStoreOptionsTypeDef] = None


class VersionOptionsOutputTypeDef(BaseValidatorModel):
    tsvVersionOptions: Optional[TsvVersionOptionsOutputTypeDef] = None


class VersionOptionsTypeDef(BaseValidatorModel):
    tsvVersionOptions: Optional[TsvVersionOptionsTypeDef] = None


class AnnotationStoreItemTypeDef(BaseValidatorModel):
    pass


class ListAnnotationStoresResponseTypeDef(BaseValidatorModel):
    annotationStores: List[AnnotationStoreItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ReferenceStoreDetailTypeDef(BaseValidatorModel):
    pass


class ListReferenceStoresResponseTypeDef(BaseValidatorModel):
    referenceStores: List[ReferenceStoreDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SequenceStoreDetailTypeDef(BaseValidatorModel):
    pass


class ListSequenceStoresResponseTypeDef(BaseValidatorModel):
    sequenceStores: List[SequenceStoreDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class VariantStoreItemTypeDef(BaseValidatorModel):
    pass


class ListVariantStoresResponseTypeDef(BaseValidatorModel):
    variantStores: List[VariantStoreItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ReadSetFilesTypeDef(BaseValidatorModel):
    source1: Optional[FileInformationTypeDef] = None
    source2: Optional[FileInformationTypeDef] = None
    index: Optional[FileInformationTypeDef] = None


class ReferenceFilesTypeDef(BaseValidatorModel):
    source: Optional[FileInformationTypeDef] = None
    index: Optional[FileInformationTypeDef] = None


class ReadSetListItemTypeDef(BaseValidatorModel):
    pass


class ListReadSetsResponseTypeDef(BaseValidatorModel):
    readSets: List[ReadSetListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class StartReadSetImportJobRequestTypeDef(BaseValidatorModel):
    sequenceStoreId: str
    roleArn: str
    sources: Sequence[StartReadSetImportJobSourceItemTypeDef]
    clientToken: Optional[str] = None


class FormatOptionsTypeDef(BaseValidatorModel):
    tsvOptions: Optional[TsvOptionsTypeDef] = None
    vcfOptions: Optional[VcfOptionsTypeDef] = None


class StartAnnotationImportRequestTypeDef(BaseValidatorModel):
    destinationName: str
    roleArn: str
    items: Sequence[AnnotationImportItemSourceTypeDef]
    versionName: Optional[str] = None
    formatOptions: Optional[FormatOptionsTypeDef] = None
    runLeftNormalization: Optional[bool] = None
    annotationFields: Optional[Mapping[str, str]] = None


class StoreOptionsUnionTypeDef(BaseValidatorModel):
    pass


class CreateAnnotationStoreRequestTypeDef(BaseValidatorModel):
    storeFormat: StoreFormatType
    reference: Optional[ReferenceItemTypeDef] = None
    name: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    versionName: Optional[str] = None
    sseConfig: Optional[SseConfigTypeDef] = None
    storeOptions: Optional[StoreOptionsUnionTypeDef] = None


class VersionOptionsUnionTypeDef(BaseValidatorModel):
    pass


class CreateAnnotationStoreVersionRequestTypeDef(BaseValidatorModel):
    name: str
    versionName: str
    description: Optional[str] = None
    versionOptions: Optional[VersionOptionsUnionTypeDef] = None
    tags: Optional[Mapping[str, str]] = None


