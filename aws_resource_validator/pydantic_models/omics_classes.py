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
from aws_resource_validator.pydantic_models.omics_constants import *

class AbortMultipartReadSetUploadRequestRequestTypeDef(BaseModel):
    sequenceStoreId: str
    uploadId: str

class AcceptShareRequestRequestTypeDef(BaseModel):
    shareId: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ActivateReadSetJobItemTypeDef(BaseModel):
    id: str
    sequenceStoreId: str
    status: ReadSetActivationJobStatusType
    creationTime: datetime
    completionTime: Optional[datetime] = None

class ActivateReadSetSourceItemTypeDef(BaseModel):
    readSetId: str
    status: ReadSetActivationJobItemStatusType
    statusMessage: Optional[str] = None

class AnnotationImportItemDetailTypeDef(BaseModel):
    source: str
    jobStatus: JobStatusType

class AnnotationImportItemSourceTypeDef(BaseModel):
    source: str

class AnnotationImportJobItemTypeDef(BaseModel):
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

class ReferenceItemTypeDef(BaseModel):
    referenceArn: Optional[str] = None

class SseConfigTypeDef(BaseModel):
    type: Literal["KMS"]
    keyArn: Optional[str] = None

class AnnotationStoreVersionItemTypeDef(BaseModel):
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

class BatchDeleteReadSetRequestRequestTypeDef(BaseModel):
    ids: Sequence[str]
    sequenceStoreId: str

class ReadSetBatchErrorTypeDef(BaseModel):
    id: str
    code: str
    message: str

class CancelAnnotationImportRequestRequestTypeDef(BaseModel):
    jobId: str

class CancelRunRequestRequestTypeDef(BaseModel):
    id: str

class CancelVariantImportRequestRequestTypeDef(BaseModel):
    jobId: str

class CompleteReadSetUploadPartListItemTypeDef(BaseModel):
    partNumber: int
    partSource: ReadSetPartSourceType
    checksum: str

class CreateMultipartReadSetUploadRequestRequestTypeDef(BaseModel):
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

class CreateRunGroupRequestRequestTypeDef(BaseModel):
    requestId: str
    name: Optional[str] = None
    maxCpus: Optional[int] = None
    maxRuns: Optional[int] = None
    maxDuration: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None
    maxGpus: Optional[int] = None

class CreateShareRequestRequestTypeDef(BaseModel):
    resourceArn: str
    principalSubscriber: str
    shareName: Optional[str] = None

class WorkflowParameterTypeDef(BaseModel):
    description: Optional[str] = None
    optional: Optional[bool] = None

class DeleteAnnotationStoreRequestRequestTypeDef(BaseModel):
    name: str
    force: Optional[bool] = None

class DeleteAnnotationStoreVersionsRequestRequestTypeDef(BaseModel):
    name: str
    versions: Sequence[str]
    force: Optional[bool] = None

class VersionDeleteErrorTypeDef(BaseModel):
    versionName: str
    message: str

class DeleteReferenceRequestRequestTypeDef(BaseModel):
    id: str
    referenceStoreId: str

class DeleteReferenceStoreRequestRequestTypeDef(BaseModel):
    id: str

class DeleteRunGroupRequestRequestTypeDef(BaseModel):
    id: str

class DeleteRunRequestRequestTypeDef(BaseModel):
    id: str

class DeleteSequenceStoreRequestRequestTypeDef(BaseModel):
    id: str

class DeleteShareRequestRequestTypeDef(BaseModel):
    shareId: str

class DeleteVariantStoreRequestRequestTypeDef(BaseModel):
    name: str
    force: Optional[bool] = None

class DeleteWorkflowRequestRequestTypeDef(BaseModel):
    id: str

class ETagTypeDef(BaseModel):
    algorithm: Optional[ETagAlgorithmType] = None
    source1: Optional[str] = None
    source2: Optional[str] = None

class ExportReadSetDetailTypeDef(BaseModel):
    id: str
    status: ReadSetExportJobItemStatusType
    statusMessage: Optional[str] = None

class ExportReadSetJobDetailTypeDef(BaseModel):
    id: str
    sequenceStoreId: str
    destination: str
    status: ReadSetExportJobStatusType
    creationTime: datetime
    completionTime: Optional[datetime] = None

class ExportReadSetTypeDef(BaseModel):
    readSetId: str

class ReadSetS3AccessTypeDef(BaseModel):
    s3Uri: Optional[str] = None

class FilterTypeDef(BaseModel):
    resourceArns: Optional[Sequence[str]] = None
    status: Optional[Sequence[ShareStatusType]] = None
    type: Optional[Sequence[ShareResourceTypeType]] = None

class VcfOptionsTypeDef(BaseModel):
    ignoreQualField: Optional[bool] = None
    ignoreFilterField: Optional[bool] = None

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class GetAnnotationImportRequestRequestTypeDef(BaseModel):
    jobId: str

class GetAnnotationStoreRequestRequestTypeDef(BaseModel):
    name: str

class GetAnnotationStoreVersionRequestRequestTypeDef(BaseModel):
    name: str
    versionName: str

class GetReadSetActivationJobRequestRequestTypeDef(BaseModel):
    id: str
    sequenceStoreId: str

class GetReadSetExportJobRequestRequestTypeDef(BaseModel):
    sequenceStoreId: str
    id: str

class GetReadSetImportJobRequestRequestTypeDef(BaseModel):
    id: str
    sequenceStoreId: str

class GetReadSetMetadataRequestRequestTypeDef(BaseModel):
    id: str
    sequenceStoreId: str

class SequenceInformationTypeDef(BaseModel):
    totalReadCount: Optional[int] = None
    totalBaseCount: Optional[int] = None
    generatedFrom: Optional[str] = None
    alignment: Optional[str] = None

class GetReadSetRequestRequestTypeDef(BaseModel):
    id: str
    sequenceStoreId: str
    partNumber: int
    file: Optional[ReadSetFileType] = None

class GetReferenceImportJobRequestRequestTypeDef(BaseModel):
    id: str
    referenceStoreId: str

class ImportReferenceSourceItemTypeDef(BaseModel):
    status: ReferenceImportJobItemStatusType
    sourceFile: Optional[str] = None
    statusMessage: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class GetReferenceMetadataRequestRequestTypeDef(BaseModel):
    id: str
    referenceStoreId: str

class GetReferenceRequestRequestTypeDef(BaseModel):
    id: str
    referenceStoreId: str
    partNumber: int
    range: Optional[str] = None
    file: Optional[ReferenceFileType] = None

class GetReferenceStoreRequestRequestTypeDef(BaseModel):
    id: str

class GetRunGroupRequestRequestTypeDef(BaseModel):
    id: str

class GetRunRequestRequestTypeDef(BaseModel):
    id: str
    export: Optional[Sequence[Literal["DEFINITION"]]] = None

class RunLogLocationTypeDef(BaseModel):
    engineLogStream: Optional[str] = None
    runLogStream: Optional[str] = None

class GetRunTaskRequestRequestTypeDef(BaseModel):
    id: str
    taskId: str

class GetSequenceStoreRequestRequestTypeDef(BaseModel):
    id: str

class SequenceStoreS3AccessTypeDef(BaseModel):
    s3Uri: Optional[str] = None
    s3AccessPointArn: Optional[str] = None

class GetShareRequestRequestTypeDef(BaseModel):
    shareId: str

class ShareDetailsTypeDef(BaseModel):
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

class GetVariantImportRequestRequestTypeDef(BaseModel):
    jobId: str

class VariantImportItemDetailTypeDef(BaseModel):
    source: str
    jobStatus: JobStatusType
    statusMessage: Optional[str] = None

class GetVariantStoreRequestRequestTypeDef(BaseModel):
    name: str

class GetWorkflowRequestRequestTypeDef(BaseModel):
    id: str
    type: Optional[WorkflowTypeType] = None
    export: Optional[Sequence[Literal["DEFINITION"]]] = None
    workflowOwnerId: Optional[str] = None

class ImportReadSetJobItemTypeDef(BaseModel):
    id: str
    sequenceStoreId: str
    roleArn: str
    status: ReadSetImportJobStatusType
    creationTime: datetime
    completionTime: Optional[datetime] = None

class SourceFilesTypeDef(BaseModel):
    source1: str
    source2: Optional[str] = None

class ImportReferenceJobItemTypeDef(BaseModel):
    id: str
    referenceStoreId: str
    roleArn: str
    status: ReferenceImportJobStatusType
    creationTime: datetime
    completionTime: Optional[datetime] = None

class ListAnnotationImportJobsFilterTypeDef(BaseModel):
    status: Optional[JobStatusType] = None
    storeName: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAnnotationStoreVersionsFilterTypeDef(BaseModel):
    status: Optional[VersionStatusType] = None

class ListAnnotationStoresFilterTypeDef(BaseModel):
    status: Optional[StoreStatusType] = None

class ListMultipartReadSetUploadsRequestRequestTypeDef(BaseModel):
    sequenceStoreId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class MultipartReadSetUploadListItemTypeDef(BaseModel):
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

class ReadSetUploadPartListItemTypeDef(BaseModel):
    partNumber: int
    partSize: int
    partSource: ReadSetPartSourceType
    checksum: str
    creationTime: Optional[datetime] = None
    lastUpdatedTime: Optional[datetime] = None

class ReferenceListItemTypeDef(BaseModel):
    id: str
    arn: str
    referenceStoreId: str
    md5: str
    creationTime: datetime
    updateTime: datetime
    status: Optional[ReferenceStatusType] = None
    name: Optional[str] = None
    description: Optional[str] = None

class ListRunGroupsRequestRequestTypeDef(BaseModel):
    name: Optional[str] = None
    startingToken: Optional[str] = None
    maxResults: Optional[int] = None

class RunGroupListItemTypeDef(BaseModel):
    arn: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    maxCpus: Optional[int] = None
    maxRuns: Optional[int] = None
    maxDuration: Optional[int] = None
    creationTime: Optional[datetime] = None
    maxGpus: Optional[int] = None

class ListRunTasksRequestRequestTypeDef(BaseModel):
    id: str
    status: Optional[TaskStatusType] = None
    startingToken: Optional[str] = None
    maxResults: Optional[int] = None

class TaskListItemTypeDef(BaseModel):
    taskId: Optional[str] = None
    status: Optional[TaskStatusType] = None
    name: Optional[str] = None
    cpus: Optional[int] = None
    memory: Optional[int] = None
    creationTime: Optional[datetime] = None
    startTime: Optional[datetime] = None
    stopTime: Optional[datetime] = None
    gpus: Optional[int] = None
    instanceType: Optional[str] = None

class ListRunsRequestRequestTypeDef(BaseModel):
    name: Optional[str] = None
    runGroupId: Optional[str] = None
    startingToken: Optional[str] = None
    maxResults: Optional[int] = None
    status: Optional[RunStatusType] = None

class RunListItemTypeDef(BaseModel):
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

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class ListVariantImportJobsFilterTypeDef(BaseModel):
    status: Optional[JobStatusType] = None
    storeName: Optional[str] = None

class VariantImportJobItemTypeDef(BaseModel):
    id: str
    destinationName: str
    roleArn: str
    status: JobStatusType
    creationTime: datetime
    updateTime: datetime
    completionTime: Optional[datetime] = None
    runLeftNormalization: Optional[bool] = None
    annotationFields: Optional[Dict[str, str]] = None

class ListVariantStoresFilterTypeDef(BaseModel):
    status: Optional[StoreStatusType] = None

class ListWorkflowsRequestRequestTypeDef(BaseModel):
    type: Optional[WorkflowTypeType] = None
    name: Optional[str] = None
    startingToken: Optional[str] = None
    maxResults: Optional[int] = None

class WorkflowListItemTypeDef(BaseModel):
    arn: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    status: Optional[WorkflowStatusType] = None
    type: Optional[WorkflowTypeType] = None
    digest: Optional[str] = None
    creationTime: Optional[datetime] = None
    metadata: Optional[Dict[str, str]] = None

class ReadOptionsTypeDef(BaseModel):
    sep: Optional[str] = None
    encoding: Optional[str] = None
    quote: Optional[str] = None
    quoteAll: Optional[bool] = None
    escape: Optional[str] = None
    escapeQuotes: Optional[bool] = None
    comment: Optional[str] = None
    header: Optional[bool] = None
    lineSep: Optional[str] = None

class StartReadSetActivationJobSourceItemTypeDef(BaseModel):
    readSetId: str

class StartReferenceImportJobSourceItemTypeDef(BaseModel):
    sourceFile: str
    name: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class StartRunRequestRequestTypeDef(BaseModel):
    roleArn: str
    requestId: str
    workflowId: Optional[str] = None
    workflowType: Optional[WorkflowTypeType] = None
    runId: Optional[str] = None
    name: Optional[str] = None
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

class VariantImportItemSourceTypeDef(BaseModel):
    source: str

class TsvStoreOptionsOutputTypeDef(BaseModel):
    annotationType: Optional[AnnotationTypeType] = None
    formatToHeader: Optional[Dict[FormatToHeaderKeyType, str]] = None
    schema: Optional[List[Dict[str, SchemaValueTypeType]]] = None

class TsvStoreOptionsTypeDef(BaseModel):
    annotationType: Optional[AnnotationTypeType] = None
    formatToHeader: Optional[Mapping[FormatToHeaderKeyType, str]] = None
    schema: Optional[Sequence[Mapping[str, SchemaValueTypeType]]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class TsvVersionOptionsOutputTypeDef(BaseModel):
    annotationType: Optional[AnnotationTypeType] = None
    formatToHeader: Optional[Dict[FormatToHeaderKeyType, str]] = None
    schema: Optional[List[Dict[str, SchemaValueTypeType]]] = None

class TsvVersionOptionsTypeDef(BaseModel):
    annotationType: Optional[AnnotationTypeType] = None
    formatToHeader: Optional[Mapping[FormatToHeaderKeyType, str]] = None
    schema: Optional[Sequence[Mapping[str, SchemaValueTypeType]]] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAnnotationStoreRequestRequestTypeDef(BaseModel):
    name: str
    description: Optional[str] = None

class UpdateAnnotationStoreVersionRequestRequestTypeDef(BaseModel):
    name: str
    versionName: str
    description: Optional[str] = None

class UpdateRunGroupRequestRequestTypeDef(BaseModel):
    id: str
    name: Optional[str] = None
    maxCpus: Optional[int] = None
    maxRuns: Optional[int] = None
    maxDuration: Optional[int] = None
    maxGpus: Optional[int] = None

class UpdateVariantStoreRequestRequestTypeDef(BaseModel):
    name: str
    description: Optional[str] = None

class UpdateWorkflowRequestRequestTypeDef(BaseModel):
    id: str
    name: Optional[str] = None
    description: Optional[str] = None

class AcceptShareResponseTypeDef(BaseModel):
    status: ShareStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CompleteMultipartReadSetUploadResponseTypeDef(BaseModel):
    readSetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMultipartReadSetUploadResponseTypeDef(BaseModel):
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

class CreateRunGroupResponseTypeDef(BaseModel):
    arn: str
    id: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateShareResponseTypeDef(BaseModel):
    shareId: str
    status: ShareStatusType
    shareName: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkflowResponseTypeDef(BaseModel):
    arn: str
    id: str
    status: WorkflowStatusType
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAnnotationStoreResponseTypeDef(BaseModel):
    status: StoreStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteShareResponseTypeDef(BaseModel):
    status: ShareStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVariantStoreResponseTypeDef(BaseModel):
    status: StoreStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetReadSetResponseTypeDef(BaseModel):
    payload: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class GetReferenceResponseTypeDef(BaseModel):
    payload: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class GetRunGroupResponseTypeDef(BaseModel):
    arn: str
    id: str
    name: str
    maxCpus: int
    maxRuns: int
    maxDuration: int
    creationTime: datetime
    tags: Dict[str, str]
    maxGpus: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetRunTaskResponseTypeDef(BaseModel):
    taskId: str
    status: TaskStatusType
    name: str
    cpus: int
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

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartAnnotationImportResponseTypeDef(BaseModel):
    jobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartReadSetActivationJobResponseTypeDef(BaseModel):
    id: str
    sequenceStoreId: str
    status: ReadSetActivationJobStatusType
    creationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StartReadSetExportJobResponseTypeDef(BaseModel):
    id: str
    sequenceStoreId: str
    destination: str
    status: ReadSetExportJobStatusType
    creationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StartReadSetImportJobResponseTypeDef(BaseModel):
    id: str
    sequenceStoreId: str
    roleArn: str
    status: ReadSetImportJobStatusType
    creationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StartReferenceImportJobResponseTypeDef(BaseModel):
    id: str
    referenceStoreId: str
    roleArn: str
    status: ReferenceImportJobStatusType
    creationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StartRunResponseTypeDef(BaseModel):
    arn: str
    id: str
    status: RunStatusType
    tags: Dict[str, str]
    uuid: str
    runOutputUri: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartVariantImportResponseTypeDef(BaseModel):
    jobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAnnotationStoreVersionResponseTypeDef(BaseModel):
    storeId: str
    id: str
    status: VersionStatusType
    name: str
    versionName: str
    description: str
    creationTime: datetime
    updateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UploadReadSetPartResponseTypeDef(BaseModel):
    checksum: str
    ResponseMetadata: ResponseMetadataTypeDef

class ActivateReadSetFilterTypeDef(BaseModel):
    status: Optional[ReadSetActivationJobStatusType] = None
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None

class ExportReadSetFilterTypeDef(BaseModel):
    status: Optional[ReadSetExportJobStatusType] = None
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None

class ImportReadSetFilterTypeDef(BaseModel):
    status: Optional[ReadSetImportJobStatusType] = None
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None

class ImportReferenceFilterTypeDef(BaseModel):
    status: Optional[ReferenceImportJobStatusType] = None
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None

class ReadSetFilterTypeDef(BaseModel):
    name: Optional[str] = None
    status: Optional[ReadSetStatusType] = None
    referenceArn: Optional[str] = None
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None
    sampleId: Optional[str] = None
    subjectId: Optional[str] = None
    generatedFrom: Optional[str] = None
    creationType: Optional[CreationTypeType] = None

class ReadSetUploadPartListFilterTypeDef(BaseModel):
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None

class ReferenceFilterTypeDef(BaseModel):
    name: Optional[str] = None
    md5: Optional[str] = None
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None

class ReferenceStoreFilterTypeDef(BaseModel):
    name: Optional[str] = None
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None

class SequenceStoreFilterTypeDef(BaseModel):
    name: Optional[str] = None
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None

class ListReadSetActivationJobsResponseTypeDef(BaseModel):
    nextToken: str
    activationJobs: List[ActivateReadSetJobItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetReadSetActivationJobResponseTypeDef(BaseModel):
    id: str
    sequenceStoreId: str
    status: ReadSetActivationJobStatusType
    statusMessage: str
    creationTime: datetime
    completionTime: datetime
    sources: List[ActivateReadSetSourceItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAnnotationImportJobsResponseTypeDef(BaseModel):
    annotationImportJobs: List[AnnotationImportJobItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVariantStoreResponseTypeDef(BaseModel):
    id: str
    reference: ReferenceItemTypeDef
    status: StoreStatusType
    name: str
    creationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVariantStoreResponseTypeDef(BaseModel):
    id: str
    reference: ReferenceItemTypeDef
    status: StoreStatusType
    name: str
    description: str
    creationTime: datetime
    updateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class AnnotationStoreItemTypeDef(BaseModel):
    id: str
    reference: ReferenceItemTypeDef
    status: StoreStatusType
    storeArn: str
    name: str
    storeFormat: StoreFormatType
    description: str
    sseConfig: SseConfigTypeDef
    creationTime: datetime
    updateTime: datetime
    statusMessage: str
    storeSizeBytes: int

class CreateReferenceStoreRequestRequestTypeDef(BaseModel):
    name: str
    description: Optional[str] = None
    sseConfig: Optional[SseConfigTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None

class CreateReferenceStoreResponseTypeDef(BaseModel):
    id: str
    arn: str
    name: str
    description: str
    sseConfig: SseConfigTypeDef
    creationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSequenceStoreRequestRequestTypeDef(BaseModel):
    name: str
    description: Optional[str] = None
    sseConfig: Optional[SseConfigTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None
    fallbackLocation: Optional[str] = None
    eTagAlgorithmFamily: Optional[ETagAlgorithmFamilyType] = None

class CreateSequenceStoreResponseTypeDef(BaseModel):
    id: str
    arn: str
    name: str
    description: str
    sseConfig: SseConfigTypeDef
    creationTime: datetime
    fallbackLocation: str
    eTagAlgorithmFamily: ETagAlgorithmFamilyType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVariantStoreRequestRequestTypeDef(BaseModel):
    reference: ReferenceItemTypeDef
    name: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    sseConfig: Optional[SseConfigTypeDef] = None

class GetReferenceStoreResponseTypeDef(BaseModel):
    id: str
    arn: str
    name: str
    description: str
    sseConfig: SseConfigTypeDef
    creationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetVariantStoreResponseTypeDef(BaseModel):
    id: str
    reference: ReferenceItemTypeDef
    status: StoreStatusType
    storeArn: str
    name: str
    description: str
    sseConfig: SseConfigTypeDef
    creationTime: datetime
    updateTime: datetime
    tags: Dict[str, str]
    statusMessage: str
    storeSizeBytes: int
    ResponseMetadata: ResponseMetadataTypeDef

class ReferenceStoreDetailTypeDef(BaseModel):
    arn: str
    id: str
    creationTime: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    sseConfig: Optional[SseConfigTypeDef] = None

class SequenceStoreDetailTypeDef(BaseModel):
    arn: str
    id: str
    creationTime: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    sseConfig: Optional[SseConfigTypeDef] = None
    fallbackLocation: Optional[str] = None
    eTagAlgorithmFamily: Optional[ETagAlgorithmFamilyType] = None

class VariantStoreItemTypeDef(BaseModel):
    id: str
    reference: ReferenceItemTypeDef
    status: StoreStatusType
    storeArn: str
    name: str
    description: str
    sseConfig: SseConfigTypeDef
    creationTime: datetime
    updateTime: datetime
    statusMessage: str
    storeSizeBytes: int

class ListAnnotationStoreVersionsResponseTypeDef(BaseModel):
    annotationStoreVersions: List[AnnotationStoreVersionItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteReadSetResponseTypeDef(BaseModel):
    errors: List[ReadSetBatchErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UploadReadSetPartRequestRequestTypeDef(BaseModel):
    sequenceStoreId: str
    uploadId: str
    partSource: ReadSetPartSourceType
    partNumber: int
    payload: BlobTypeDef

class CompleteMultipartReadSetUploadRequestRequestTypeDef(BaseModel):
    sequenceStoreId: str
    uploadId: str
    parts: Sequence[CompleteReadSetUploadPartListItemTypeDef]

class CreateWorkflowRequestRequestTypeDef(BaseModel):
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

class GetWorkflowResponseTypeDef(BaseModel):
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
    parameterTemplate: Dict[str, WorkflowParameterTypeDef]
    storageCapacity: int
    creationTime: datetime
    statusMessage: str
    tags: Dict[str, str]
    metadata: Dict[str, str]
    accelerators: Literal["GPU"]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAnnotationStoreVersionsResponseTypeDef(BaseModel):
    errors: List[VersionDeleteErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetReadSetExportJobResponseTypeDef(BaseModel):
    id: str
    sequenceStoreId: str
    destination: str
    status: ReadSetExportJobStatusType
    statusMessage: str
    creationTime: datetime
    completionTime: datetime
    readSets: List[ExportReadSetDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListReadSetExportJobsResponseTypeDef(BaseModel):
    nextToken: str
    exportJobs: List[ExportReadSetJobDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartReadSetExportJobRequestRequestTypeDef(BaseModel):
    sequenceStoreId: str
    destination: str
    roleArn: str
    sources: Sequence[ExportReadSetTypeDef]
    clientToken: Optional[str] = None

class FileInformationTypeDef(BaseModel):
    totalParts: Optional[int] = None
    partSize: Optional[int] = None
    contentLength: Optional[int] = None
    s3Access: Optional[ReadSetS3AccessTypeDef] = None

class ListSharesRequestRequestTypeDef(BaseModel):
    resourceOwner: ResourceOwnerType
    filter: Optional[FilterTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetAnnotationImportRequestAnnotationImportJobCreatedWaitTypeDef(BaseModel):
    jobId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetAnnotationStoreRequestAnnotationStoreCreatedWaitTypeDef(BaseModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetAnnotationStoreRequestAnnotationStoreDeletedWaitTypeDef(BaseModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetAnnotationStoreVersionRequestAnnotationStoreVersionCreatedWaitTypeDef(BaseModel):
    name: str
    versionName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetAnnotationStoreVersionRequestAnnotationStoreVersionDeletedWaitTypeDef(BaseModel):
    name: str
    versionName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetReadSetActivationJobRequestReadSetActivationJobCompletedWaitTypeDef(BaseModel):
    id: str
    sequenceStoreId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetReadSetExportJobRequestReadSetExportJobCompletedWaitTypeDef(BaseModel):
    sequenceStoreId: str
    id: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetReadSetImportJobRequestReadSetImportJobCompletedWaitTypeDef(BaseModel):
    id: str
    sequenceStoreId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetReferenceImportJobRequestReferenceImportJobCompletedWaitTypeDef(BaseModel):
    id: str
    referenceStoreId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetRunRequestRunCompletedWaitTypeDef(BaseModel):
    id: str
    export: Optional[Sequence[Literal["DEFINITION"]]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetRunRequestRunRunningWaitTypeDef(BaseModel):
    id: str
    export: Optional[Sequence[Literal["DEFINITION"]]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetRunTaskRequestTaskCompletedWaitTypeDef(BaseModel):
    id: str
    taskId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetRunTaskRequestTaskRunningWaitTypeDef(BaseModel):
    id: str
    taskId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetVariantImportRequestVariantImportJobCreatedWaitTypeDef(BaseModel):
    jobId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetVariantStoreRequestVariantStoreCreatedWaitTypeDef(BaseModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetVariantStoreRequestVariantStoreDeletedWaitTypeDef(BaseModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetWorkflowRequestWorkflowActiveWaitTypeDef(BaseModel):
    id: str
    type: Optional[WorkflowTypeType] = None
    export: Optional[Sequence[Literal["DEFINITION"]]] = None
    workflowOwnerId: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class ReadSetListItemTypeDef(BaseModel):
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
    sequenceInformation: Optional[SequenceInformationTypeDef] = None
    statusMessage: Optional[str] = None
    creationType: Optional[CreationTypeType] = None
    etag: Optional[ETagTypeDef] = None

class GetReferenceImportJobResponseTypeDef(BaseModel):
    id: str
    referenceStoreId: str
    roleArn: str
    status: ReferenceImportJobStatusType
    statusMessage: str
    creationTime: datetime
    completionTime: datetime
    sources: List[ImportReferenceSourceItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetRunResponseTypeDef(BaseModel):
    arn: str
    id: str
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
    accelerators: Literal["GPU"]
    retentionMode: RunRetentionModeType
    failureReason: str
    logLocation: RunLogLocationTypeDef
    uuid: str
    runOutputUri: str
    storageType: StorageTypeType
    workflowOwnerId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSequenceStoreResponseTypeDef(BaseModel):
    id: str
    arn: str
    name: str
    description: str
    sseConfig: SseConfigTypeDef
    creationTime: datetime
    fallbackLocation: str
    s3Access: SequenceStoreS3AccessTypeDef
    eTagAlgorithmFamily: ETagAlgorithmFamilyType
    ResponseMetadata: ResponseMetadataTypeDef

class GetShareResponseTypeDef(BaseModel):
    share: ShareDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSharesResponseTypeDef(BaseModel):
    shares: List[ShareDetailsTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetVariantImportResponseTypeDef(BaseModel):
    id: str
    destinationName: str
    roleArn: str
    status: JobStatusType
    statusMessage: str
    creationTime: datetime
    updateTime: datetime
    completionTime: datetime
    items: List[VariantImportItemDetailTypeDef]
    runLeftNormalization: bool
    annotationFields: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListReadSetImportJobsResponseTypeDef(BaseModel):
    nextToken: str
    importJobs: List[ImportReadSetJobItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ImportReadSetSourceItemTypeDef(BaseModel):
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

class StartReadSetImportJobSourceItemTypeDef(BaseModel):
    sourceFiles: SourceFilesTypeDef
    sourceFileType: FileTypeType
    subjectId: str
    sampleId: str
    generatedFrom: Optional[str] = None
    referenceArn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class ListReferenceImportJobsResponseTypeDef(BaseModel):
    nextToken: str
    importJobs: List[ImportReferenceJobItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAnnotationImportJobsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    ids: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    filter: Optional[ListAnnotationImportJobsFilterTypeDef] = None

class ListAnnotationImportJobsRequestListAnnotationImportJobsPaginateTypeDef(BaseModel):
    ids: Optional[Sequence[str]] = None
    filter: Optional[ListAnnotationImportJobsFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMultipartReadSetUploadsRequestListMultipartReadSetUploadsPaginateTypeDef(BaseModel):
    sequenceStoreId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRunGroupsRequestListRunGroupsPaginateTypeDef(BaseModel):
    name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRunTasksRequestListRunTasksPaginateTypeDef(BaseModel):
    id: str
    status: Optional[TaskStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRunsRequestListRunsPaginateTypeDef(BaseModel):
    name: Optional[str] = None
    runGroupId: Optional[str] = None
    status: Optional[RunStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSharesRequestListSharesPaginateTypeDef(BaseModel):
    resourceOwner: ResourceOwnerType
    filter: Optional[FilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkflowsRequestListWorkflowsPaginateTypeDef(BaseModel):
    type: Optional[WorkflowTypeType] = None
    name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAnnotationStoreVersionsRequestListAnnotationStoreVersionsPaginateTypeDef(BaseModel):
    name: str
    filter: Optional[ListAnnotationStoreVersionsFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAnnotationStoreVersionsRequestRequestTypeDef(BaseModel):
    name: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filter: Optional[ListAnnotationStoreVersionsFilterTypeDef] = None

class ListAnnotationStoresRequestListAnnotationStoresPaginateTypeDef(BaseModel):
    ids: Optional[Sequence[str]] = None
    filter: Optional[ListAnnotationStoresFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAnnotationStoresRequestRequestTypeDef(BaseModel):
    ids: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filter: Optional[ListAnnotationStoresFilterTypeDef] = None

class ListMultipartReadSetUploadsResponseTypeDef(BaseModel):
    nextToken: str
    uploads: List[MultipartReadSetUploadListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListReadSetUploadPartsResponseTypeDef(BaseModel):
    nextToken: str
    parts: List[ReadSetUploadPartListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListReferencesResponseTypeDef(BaseModel):
    nextToken: str
    references: List[ReferenceListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRunGroupsResponseTypeDef(BaseModel):
    items: List[RunGroupListItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRunTasksResponseTypeDef(BaseModel):
    items: List[TaskListItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRunsResponseTypeDef(BaseModel):
    items: List[RunListItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListVariantImportJobsRequestListVariantImportJobsPaginateTypeDef(BaseModel):
    ids: Optional[Sequence[str]] = None
    filter: Optional[ListVariantImportJobsFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVariantImportJobsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    ids: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    filter: Optional[ListVariantImportJobsFilterTypeDef] = None

class ListVariantImportJobsResponseTypeDef(BaseModel):
    variantImportJobs: List[VariantImportJobItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListVariantStoresRequestListVariantStoresPaginateTypeDef(BaseModel):
    ids: Optional[Sequence[str]] = None
    filter: Optional[ListVariantStoresFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVariantStoresRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    ids: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    filter: Optional[ListVariantStoresFilterTypeDef] = None

class ListWorkflowsResponseTypeDef(BaseModel):
    items: List[WorkflowListItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TsvOptionsTypeDef(BaseModel):
    readOptions: Optional[ReadOptionsTypeDef] = None

class StartReadSetActivationJobRequestRequestTypeDef(BaseModel):
    sequenceStoreId: str
    sources: Sequence[StartReadSetActivationJobSourceItemTypeDef]
    clientToken: Optional[str] = None

class StartReferenceImportJobRequestRequestTypeDef(BaseModel):
    referenceStoreId: str
    roleArn: str
    sources: Sequence[StartReferenceImportJobSourceItemTypeDef]
    clientToken: Optional[str] = None

class StartVariantImportRequestRequestTypeDef(BaseModel):
    destinationName: str
    roleArn: str
    items: Sequence[VariantImportItemSourceTypeDef]
    runLeftNormalization: Optional[bool] = None
    annotationFields: Optional[Mapping[str, str]] = None

class StoreOptionsOutputTypeDef(BaseModel):
    tsvStoreOptions: Optional[TsvStoreOptionsOutputTypeDef] = None

class StoreOptionsTypeDef(BaseModel):
    tsvStoreOptions: Optional[TsvStoreOptionsTypeDef] = None

class VersionOptionsOutputTypeDef(BaseModel):
    tsvVersionOptions: Optional[TsvVersionOptionsOutputTypeDef] = None

class VersionOptionsTypeDef(BaseModel):
    tsvVersionOptions: Optional[TsvVersionOptionsTypeDef] = None

class ListReadSetActivationJobsRequestListReadSetActivationJobsPaginateTypeDef(BaseModel):
    sequenceStoreId: str
    filter: Optional[ActivateReadSetFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReadSetActivationJobsRequestRequestTypeDef(BaseModel):
    sequenceStoreId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filter: Optional[ActivateReadSetFilterTypeDef] = None

class ListReadSetExportJobsRequestListReadSetExportJobsPaginateTypeDef(BaseModel):
    sequenceStoreId: str
    filter: Optional[ExportReadSetFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReadSetExportJobsRequestRequestTypeDef(BaseModel):
    sequenceStoreId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filter: Optional[ExportReadSetFilterTypeDef] = None

class ListReadSetImportJobsRequestListReadSetImportJobsPaginateTypeDef(BaseModel):
    sequenceStoreId: str
    filter: Optional[ImportReadSetFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReadSetImportJobsRequestRequestTypeDef(BaseModel):
    sequenceStoreId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filter: Optional[ImportReadSetFilterTypeDef] = None

class ListReferenceImportJobsRequestListReferenceImportJobsPaginateTypeDef(BaseModel):
    referenceStoreId: str
    filter: Optional[ImportReferenceFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReferenceImportJobsRequestRequestTypeDef(BaseModel):
    referenceStoreId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filter: Optional[ImportReferenceFilterTypeDef] = None

class ListReadSetsRequestListReadSetsPaginateTypeDef(BaseModel):
    sequenceStoreId: str
    filter: Optional[ReadSetFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReadSetsRequestRequestTypeDef(BaseModel):
    sequenceStoreId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filter: Optional[ReadSetFilterTypeDef] = None

class ListReadSetUploadPartsRequestListReadSetUploadPartsPaginateTypeDef(BaseModel):
    sequenceStoreId: str
    uploadId: str
    partSource: ReadSetPartSourceType
    filter: Optional[ReadSetUploadPartListFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReadSetUploadPartsRequestRequestTypeDef(BaseModel):
    sequenceStoreId: str
    uploadId: str
    partSource: ReadSetPartSourceType
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filter: Optional[ReadSetUploadPartListFilterTypeDef] = None

class ListReferencesRequestListReferencesPaginateTypeDef(BaseModel):
    referenceStoreId: str
    filter: Optional[ReferenceFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReferencesRequestRequestTypeDef(BaseModel):
    referenceStoreId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filter: Optional[ReferenceFilterTypeDef] = None

class ListReferenceStoresRequestListReferenceStoresPaginateTypeDef(BaseModel):
    filter: Optional[ReferenceStoreFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReferenceStoresRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filter: Optional[ReferenceStoreFilterTypeDef] = None

class ListSequenceStoresRequestListSequenceStoresPaginateTypeDef(BaseModel):
    filter: Optional[SequenceStoreFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSequenceStoresRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filter: Optional[SequenceStoreFilterTypeDef] = None

class ListAnnotationStoresResponseTypeDef(BaseModel):
    annotationStores: List[AnnotationStoreItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListReferenceStoresResponseTypeDef(BaseModel):
    nextToken: str
    referenceStores: List[ReferenceStoreDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSequenceStoresResponseTypeDef(BaseModel):
    nextToken: str
    sequenceStores: List[SequenceStoreDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListVariantStoresResponseTypeDef(BaseModel):
    variantStores: List[VariantStoreItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReadSetFilesTypeDef(BaseModel):
    source1: Optional[FileInformationTypeDef] = None
    source2: Optional[FileInformationTypeDef] = None
    index: Optional[FileInformationTypeDef] = None

class ReferenceFilesTypeDef(BaseModel):
    source: Optional[FileInformationTypeDef] = None
    index: Optional[FileInformationTypeDef] = None

class ListReadSetsResponseTypeDef(BaseModel):
    nextToken: str
    readSets: List[ReadSetListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetReadSetImportJobResponseTypeDef(BaseModel):
    id: str
    sequenceStoreId: str
    roleArn: str
    status: ReadSetImportJobStatusType
    statusMessage: str
    creationTime: datetime
    completionTime: datetime
    sources: List[ImportReadSetSourceItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartReadSetImportJobRequestRequestTypeDef(BaseModel):
    sequenceStoreId: str
    roleArn: str
    sources: Sequence[StartReadSetImportJobSourceItemTypeDef]
    clientToken: Optional[str] = None

class FormatOptionsTypeDef(BaseModel):
    tsvOptions: Optional[TsvOptionsTypeDef] = None
    vcfOptions: Optional[VcfOptionsTypeDef] = None

class CreateAnnotationStoreResponseTypeDef(BaseModel):
    id: str
    reference: ReferenceItemTypeDef
    storeFormat: StoreFormatType
    storeOptions: StoreOptionsOutputTypeDef
    status: StoreStatusType
    name: str
    versionName: str
    creationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetAnnotationStoreResponseTypeDef(BaseModel):
    id: str
    reference: ReferenceItemTypeDef
    status: StoreStatusType
    storeArn: str
    name: str
    description: str
    sseConfig: SseConfigTypeDef
    creationTime: datetime
    updateTime: datetime
    tags: Dict[str, str]
    storeOptions: StoreOptionsOutputTypeDef
    storeFormat: StoreFormatType
    statusMessage: str
    storeSizeBytes: int
    numVersions: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAnnotationStoreResponseTypeDef(BaseModel):
    id: str
    reference: ReferenceItemTypeDef
    status: StoreStatusType
    name: str
    description: str
    creationTime: datetime
    updateTime: datetime
    storeOptions: StoreOptionsOutputTypeDef
    storeFormat: StoreFormatType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAnnotationStoreRequestRequestTypeDef(BaseModel):
    storeFormat: StoreFormatType
    reference: Optional[ReferenceItemTypeDef] = None
    name: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    versionName: Optional[str] = None
    sseConfig: Optional[SseConfigTypeDef] = None
    storeOptions: Optional[StoreOptionsTypeDef] = None

class CreateAnnotationStoreVersionResponseTypeDef(BaseModel):
    id: str
    versionName: str
    storeId: str
    versionOptions: VersionOptionsOutputTypeDef
    name: str
    status: VersionStatusType
    creationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetAnnotationStoreVersionResponseTypeDef(BaseModel):
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
    versionOptions: VersionOptionsOutputTypeDef
    statusMessage: str
    versionSizeBytes: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAnnotationStoreVersionRequestRequestTypeDef(BaseModel):
    name: str
    versionName: str
    description: Optional[str] = None
    versionOptions: Optional[VersionOptionsTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class GetReadSetMetadataResponseTypeDef(BaseModel):
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
    sequenceInformation: SequenceInformationTypeDef
    referenceArn: str
    files: ReadSetFilesTypeDef
    statusMessage: str
    creationType: CreationTypeType
    etag: ETagTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetReferenceMetadataResponseTypeDef(BaseModel):
    id: str
    arn: str
    referenceStoreId: str
    md5: str
    status: ReferenceStatusType
    name: str
    description: str
    creationTime: datetime
    updateTime: datetime
    files: ReferenceFilesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAnnotationImportResponseTypeDef(BaseModel):
    id: str
    destinationName: str
    versionName: str
    roleArn: str
    status: JobStatusType
    statusMessage: str
    creationTime: datetime
    updateTime: datetime
    completionTime: datetime
    items: List[AnnotationImportItemDetailTypeDef]
    runLeftNormalization: bool
    formatOptions: FormatOptionsTypeDef
    annotationFields: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartAnnotationImportRequestRequestTypeDef(BaseModel):
    destinationName: str
    roleArn: str
    items: Sequence[AnnotationImportItemSourceTypeDef]
    versionName: Optional[str] = None
    formatOptions: Optional[FormatOptionsTypeDef] = None
    runLeftNormalization: Optional[bool] = None
    annotationFields: Optional[Mapping[str, str]] = None

