from datetime import datetime

from botocore.response import StreamingBody

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
from aws_resource_validator.pydantic_models.omics_constants import *

class AbortMultipartReadSetUploadRequestRequestTypeDef(BaseValidatorModel):
    sequenceStoreId: str
    uploadId: str

class AcceptShareRequestRequestTypeDef(BaseValidatorModel):
    shareId: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ActivateReadSetJobItemTypeDef(BaseValidatorModel):
    id: str
    sequenceStoreId: str
    status: ReadSetActivationJobStatusType
    creationTime: datetime
    completionTime: Optional[datetime] = None

class ActivateReadSetSourceItemTypeDef(BaseValidatorModel):
    readSetId: str
    status: ReadSetActivationJobItemStatusType
    statusMessage: Optional[str] = None

class AnnotationImportItemDetailTypeDef(BaseValidatorModel):
    source: str
    jobStatus: JobStatusType

class AnnotationImportItemSourceTypeDef(BaseValidatorModel):
    source: str

class AnnotationImportJobItemTypeDef(BaseValidatorModel):
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

class ReferenceItemTypeDef(BaseValidatorModel):
    referenceArn: Optional[str] = None

class SseConfigTypeDef(BaseValidatorModel):
    type: Literal["KMS"]
    keyArn: Optional[str] = None

class AnnotationStoreVersionItemTypeDef(BaseValidatorModel):
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

class BatchDeleteReadSetRequestRequestTypeDef(BaseValidatorModel):
    ids: Sequence[str]
    sequenceStoreId: str

class ReadSetBatchErrorTypeDef(BaseValidatorModel):
    id: str
    code: str
    message: str

class CancelAnnotationImportRequestRequestTypeDef(BaseValidatorModel):
    jobId: str

class CancelRunRequestRequestTypeDef(BaseValidatorModel):
    id: str

class CancelVariantImportRequestRequestTypeDef(BaseValidatorModel):
    jobId: str

class CompleteReadSetUploadPartListItemTypeDef(BaseValidatorModel):
    partNumber: int
    partSource: ReadSetPartSourceType
    checksum: str

class CreateMultipartReadSetUploadRequestRequestTypeDef(BaseValidatorModel):
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

class CreateRunGroupRequestRequestTypeDef(BaseValidatorModel):
    requestId: str
    name: Optional[str] = None
    maxCpus: Optional[int] = None
    maxRuns: Optional[int] = None
    maxDuration: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None
    maxGpus: Optional[int] = None

class CreateShareRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    principalSubscriber: str
    shareName: Optional[str] = None

class WorkflowParameterTypeDef(BaseValidatorModel):
    description: Optional[str] = None
    optional: Optional[bool] = None

class DeleteAnnotationStoreRequestRequestTypeDef(BaseValidatorModel):
    name: str
    force: Optional[bool] = None

class DeleteAnnotationStoreVersionsRequestRequestTypeDef(BaseValidatorModel):
    name: str
    versions: Sequence[str]
    force: Optional[bool] = None

class VersionDeleteErrorTypeDef(BaseValidatorModel):
    versionName: str
    message: str

class DeleteReferenceRequestRequestTypeDef(BaseValidatorModel):
    id: str
    referenceStoreId: str

class DeleteReferenceStoreRequestRequestTypeDef(BaseValidatorModel):
    id: str

class DeleteRunGroupRequestRequestTypeDef(BaseValidatorModel):
    id: str

class DeleteRunRequestRequestTypeDef(BaseValidatorModel):
    id: str

class DeleteSequenceStoreRequestRequestTypeDef(BaseValidatorModel):
    id: str

class DeleteShareRequestRequestTypeDef(BaseValidatorModel):
    shareId: str

class DeleteVariantStoreRequestRequestTypeDef(BaseValidatorModel):
    name: str
    force: Optional[bool] = None

class DeleteWorkflowRequestRequestTypeDef(BaseValidatorModel):
    id: str

class ETagTypeDef(BaseValidatorModel):
    algorithm: Optional[ETagAlgorithmType] = None
    source1: Optional[str] = None
    source2: Optional[str] = None

class ExportReadSetDetailTypeDef(BaseValidatorModel):
    id: str
    status: ReadSetExportJobItemStatusType
    statusMessage: Optional[str] = None

class ExportReadSetJobDetailTypeDef(BaseValidatorModel):
    id: str
    sequenceStoreId: str
    destination: str
    status: ReadSetExportJobStatusType
    creationTime: datetime
    completionTime: Optional[datetime] = None

class ExportReadSetTypeDef(BaseValidatorModel):
    readSetId: str

class ReadSetS3AccessTypeDef(BaseValidatorModel):
    s3Uri: Optional[str] = None

class FilterTypeDef(BaseValidatorModel):
    resourceArns: Optional[Sequence[str]] = None
    status: Optional[Sequence[ShareStatusType]] = None
    type: Optional[Sequence[ShareResourceTypeType]] = None

class VcfOptionsTypeDef(BaseValidatorModel):
    ignoreQualField: Optional[bool] = None
    ignoreFilterField: Optional[bool] = None

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class GetAnnotationImportRequestRequestTypeDef(BaseValidatorModel):
    jobId: str

class GetAnnotationStoreRequestRequestTypeDef(BaseValidatorModel):
    name: str

class GetAnnotationStoreVersionRequestRequestTypeDef(BaseValidatorModel):
    name: str
    versionName: str

class GetReadSetActivationJobRequestRequestTypeDef(BaseValidatorModel):
    id: str
    sequenceStoreId: str

class GetReadSetExportJobRequestRequestTypeDef(BaseValidatorModel):
    sequenceStoreId: str
    id: str

class GetReadSetImportJobRequestRequestTypeDef(BaseValidatorModel):
    id: str
    sequenceStoreId: str

class GetReadSetMetadataRequestRequestTypeDef(BaseValidatorModel):
    id: str
    sequenceStoreId: str

class SequenceInformationTypeDef(BaseValidatorModel):
    totalReadCount: Optional[int] = None
    totalBaseCount: Optional[int] = None
    generatedFrom: Optional[str] = None
    alignment: Optional[str] = None

class GetReadSetRequestRequestTypeDef(BaseValidatorModel):
    id: str
    sequenceStoreId: str
    partNumber: int
    file: Optional[ReadSetFileType] = None

class GetReferenceImportJobRequestRequestTypeDef(BaseValidatorModel):
    id: str
    referenceStoreId: str

class ImportReferenceSourceItemTypeDef(BaseValidatorModel):
    status: ReferenceImportJobItemStatusType
    sourceFile: Optional[str] = None
    statusMessage: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class GetReferenceMetadataRequestRequestTypeDef(BaseValidatorModel):
    id: str
    referenceStoreId: str

class GetReferenceRequestRequestTypeDef(BaseValidatorModel):
    id: str
    referenceStoreId: str
    partNumber: int
    range: Optional[str] = None
    file: Optional[ReferenceFileType] = None

class GetReferenceStoreRequestRequestTypeDef(BaseValidatorModel):
    id: str

class GetRunGroupRequestRequestTypeDef(BaseValidatorModel):
    id: str

class GetRunRequestRequestTypeDef(BaseValidatorModel):
    id: str
    export: Optional[Sequence[Literal["DEFINITION"]]] = None

class RunLogLocationTypeDef(BaseValidatorModel):
    engineLogStream: Optional[str] = None
    runLogStream: Optional[str] = None

class GetRunTaskRequestRequestTypeDef(BaseValidatorModel):
    id: str
    taskId: str

class GetSequenceStoreRequestRequestTypeDef(BaseValidatorModel):
    id: str

class SequenceStoreS3AccessTypeDef(BaseValidatorModel):
    s3Uri: Optional[str] = None
    s3AccessPointArn: Optional[str] = None

class GetShareRequestRequestTypeDef(BaseValidatorModel):
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

class GetVariantImportRequestRequestTypeDef(BaseValidatorModel):
    jobId: str

class VariantImportItemDetailTypeDef(BaseValidatorModel):
    source: str
    jobStatus: JobStatusType
    statusMessage: Optional[str] = None

class GetVariantStoreRequestRequestTypeDef(BaseValidatorModel):
    name: str

class GetWorkflowRequestRequestTypeDef(BaseValidatorModel):
    id: str
    type: Optional[WorkflowTypeType] = None
    export: Optional[Sequence[Literal["DEFINITION"]]] = None
    workflowOwnerId: Optional[str] = None

class ImportReadSetJobItemTypeDef(BaseValidatorModel):
    id: str
    sequenceStoreId: str
    roleArn: str
    status: ReadSetImportJobStatusType
    creationTime: datetime
    completionTime: Optional[datetime] = None

class SourceFilesTypeDef(BaseValidatorModel):
    source1: str
    source2: Optional[str] = None

class ImportReferenceJobItemTypeDef(BaseValidatorModel):
    id: str
    referenceStoreId: str
    roleArn: str
    status: ReferenceImportJobStatusType
    creationTime: datetime
    completionTime: Optional[datetime] = None

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

class ListMultipartReadSetUploadsRequestRequestTypeDef(BaseValidatorModel):
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

class ReferenceListItemTypeDef(BaseValidatorModel):
    id: str
    arn: str
    referenceStoreId: str
    md5: str
    creationTime: datetime
    updateTime: datetime
    status: Optional[ReferenceStatusType] = None
    name: Optional[str] = None
    description: Optional[str] = None

class ListRunGroupsRequestRequestTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    startingToken: Optional[str] = None
    maxResults: Optional[int] = None

class RunGroupListItemTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    maxCpus: Optional[int] = None
    maxRuns: Optional[int] = None
    maxDuration: Optional[int] = None
    creationTime: Optional[datetime] = None
    maxGpus: Optional[int] = None

class ListRunTasksRequestRequestTypeDef(BaseValidatorModel):
    id: str
    status: Optional[TaskStatusType] = None
    startingToken: Optional[str] = None
    maxResults: Optional[int] = None

class TaskListItemTypeDef(BaseValidatorModel):
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

class ListRunsRequestRequestTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    runGroupId: Optional[str] = None
    startingToken: Optional[str] = None
    maxResults: Optional[int] = None
    status: Optional[RunStatusType] = None

class RunListItemTypeDef(BaseValidatorModel):
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

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class ListVariantImportJobsFilterTypeDef(BaseValidatorModel):
    status: Optional[JobStatusType] = None
    storeName: Optional[str] = None

class VariantImportJobItemTypeDef(BaseValidatorModel):
    id: str
    destinationName: str
    roleArn: str
    status: JobStatusType
    creationTime: datetime
    updateTime: datetime
    completionTime: Optional[datetime] = None
    runLeftNormalization: Optional[bool] = None
    annotationFields: Optional[Dict[str, str]] = None

class ListVariantStoresFilterTypeDef(BaseValidatorModel):
    status: Optional[StoreStatusType] = None

class ListWorkflowsRequestRequestTypeDef(BaseValidatorModel):
    type: Optional[WorkflowTypeType] = None
    name: Optional[str] = None
    startingToken: Optional[str] = None
    maxResults: Optional[int] = None

class WorkflowListItemTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    status: Optional[WorkflowStatusType] = None
    type: Optional[WorkflowTypeType] = None
    digest: Optional[str] = None
    creationTime: Optional[datetime] = None
    metadata: Optional[Dict[str, str]] = None

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

class StartRunRequestRequestTypeDef(BaseValidatorModel):
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

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
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

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAnnotationStoreRequestRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None

class UpdateAnnotationStoreVersionRequestRequestTypeDef(BaseValidatorModel):
    name: str
    versionName: str
    description: Optional[str] = None

class UpdateRunGroupRequestRequestTypeDef(BaseValidatorModel):
    id: str
    name: Optional[str] = None
    maxCpus: Optional[int] = None
    maxRuns: Optional[int] = None
    maxDuration: Optional[int] = None
    maxGpus: Optional[int] = None

class UpdateVariantStoreRequestRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None

class UpdateWorkflowRequestRequestTypeDef(BaseValidatorModel):
    id: str
    name: Optional[str] = None
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

class CreateRunGroupResponseTypeDef(BaseValidatorModel):
    arn: str
    id: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateShareResponseTypeDef(BaseValidatorModel):
    shareId: str
    status: ShareStatusType
    shareName: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkflowResponseTypeDef(BaseValidatorModel):
    arn: str
    id: str
    status: WorkflowStatusType
    tags: Dict[str, str]
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

class GetRunGroupResponseTypeDef(BaseValidatorModel):
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

class GetRunTaskResponseTypeDef(BaseValidatorModel):
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

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartAnnotationImportResponseTypeDef(BaseValidatorModel):
    jobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartReadSetActivationJobResponseTypeDef(BaseValidatorModel):
    id: str
    sequenceStoreId: str
    status: ReadSetActivationJobStatusType
    creationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StartReadSetExportJobResponseTypeDef(BaseValidatorModel):
    id: str
    sequenceStoreId: str
    destination: str
    status: ReadSetExportJobStatusType
    creationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StartReadSetImportJobResponseTypeDef(BaseValidatorModel):
    id: str
    sequenceStoreId: str
    roleArn: str
    status: ReadSetImportJobStatusType
    creationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StartReferenceImportJobResponseTypeDef(BaseValidatorModel):
    id: str
    referenceStoreId: str
    roleArn: str
    status: ReferenceImportJobStatusType
    creationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StartRunResponseTypeDef(BaseValidatorModel):
    arn: str
    id: str
    status: RunStatusType
    tags: Dict[str, str]
    uuid: str
    runOutputUri: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartVariantImportResponseTypeDef(BaseValidatorModel):
    jobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAnnotationStoreVersionResponseTypeDef(BaseValidatorModel):
    storeId: str
    id: str
    status: VersionStatusType
    name: str
    versionName: str
    description: str
    creationTime: datetime
    updateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UploadReadSetPartResponseTypeDef(BaseValidatorModel):
    checksum: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class ListReadSetActivationJobsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    activationJobs: List[ActivateReadSetJobItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetReadSetActivationJobResponseTypeDef(BaseValidatorModel):
    id: str
    sequenceStoreId: str
    status: ReadSetActivationJobStatusType
    statusMessage: str
    creationTime: datetime
    completionTime: datetime
    sources: List[ActivateReadSetSourceItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAnnotationImportJobsResponseTypeDef(BaseValidatorModel):
    annotationImportJobs: List[AnnotationImportJobItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVariantStoreResponseTypeDef(BaseValidatorModel):
    id: str
    reference: ReferenceItemTypeDef
    status: StoreStatusType
    name: str
    creationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVariantStoreResponseTypeDef(BaseValidatorModel):
    id: str
    reference: ReferenceItemTypeDef
    status: StoreStatusType
    name: str
    description: str
    creationTime: datetime
    updateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class AnnotationStoreItemTypeDef(BaseValidatorModel):
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

class CreateReferenceStoreRequestRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    sseConfig: Optional[SseConfigTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None

class CreateReferenceStoreResponseTypeDef(BaseValidatorModel):
    id: str
    arn: str
    name: str
    description: str
    sseConfig: SseConfigTypeDef
    creationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSequenceStoreRequestRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    sseConfig: Optional[SseConfigTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None
    fallbackLocation: Optional[str] = None
    eTagAlgorithmFamily: Optional[ETagAlgorithmFamilyType] = None

class CreateSequenceStoreResponseTypeDef(BaseValidatorModel):
    id: str
    arn: str
    name: str
    description: str
    sseConfig: SseConfigTypeDef
    creationTime: datetime
    fallbackLocation: str
    eTagAlgorithmFamily: ETagAlgorithmFamilyType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVariantStoreRequestRequestTypeDef(BaseValidatorModel):
    reference: ReferenceItemTypeDef
    name: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    sseConfig: Optional[SseConfigTypeDef] = None

class GetReferenceStoreResponseTypeDef(BaseValidatorModel):
    id: str
    arn: str
    name: str
    description: str
    sseConfig: SseConfigTypeDef
    creationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetVariantStoreResponseTypeDef(BaseValidatorModel):
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

class ReferenceStoreDetailTypeDef(BaseValidatorModel):
    arn: str
    id: str
    creationTime: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    sseConfig: Optional[SseConfigTypeDef] = None

class SequenceStoreDetailTypeDef(BaseValidatorModel):
    arn: str
    id: str
    creationTime: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    sseConfig: Optional[SseConfigTypeDef] = None
    fallbackLocation: Optional[str] = None
    eTagAlgorithmFamily: Optional[ETagAlgorithmFamilyType] = None

class VariantStoreItemTypeDef(BaseValidatorModel):
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

class ListAnnotationStoreVersionsResponseTypeDef(BaseValidatorModel):
    annotationStoreVersions: List[AnnotationStoreVersionItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteReadSetResponseTypeDef(BaseValidatorModel):
    errors: List[ReadSetBatchErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UploadReadSetPartRequestRequestTypeDef(BaseValidatorModel):
    sequenceStoreId: str
    uploadId: str
    partSource: ReadSetPartSourceType
    partNumber: int
    payload: BlobTypeDef

class CompleteMultipartReadSetUploadRequestRequestTypeDef(BaseValidatorModel):
    sequenceStoreId: str
    uploadId: str
    parts: Sequence[CompleteReadSetUploadPartListItemTypeDef]

class CreateWorkflowRequestRequestTypeDef(BaseValidatorModel):
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

class GetWorkflowResponseTypeDef(BaseValidatorModel):
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

class DeleteAnnotationStoreVersionsResponseTypeDef(BaseValidatorModel):
    errors: List[VersionDeleteErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetReadSetExportJobResponseTypeDef(BaseValidatorModel):
    id: str
    sequenceStoreId: str
    destination: str
    status: ReadSetExportJobStatusType
    statusMessage: str
    creationTime: datetime
    completionTime: datetime
    readSets: List[ExportReadSetDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListReadSetExportJobsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    exportJobs: List[ExportReadSetJobDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartReadSetExportJobRequestRequestTypeDef(BaseValidatorModel):
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

class ListSharesRequestRequestTypeDef(BaseValidatorModel):
    resourceOwner: ResourceOwnerType
    filter: Optional[FilterTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetAnnotationImportRequestAnnotationImportJobCreatedWaitTypeDef(BaseValidatorModel):
    jobId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetAnnotationStoreRequestAnnotationStoreCreatedWaitTypeDef(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetAnnotationStoreRequestAnnotationStoreDeletedWaitTypeDef(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetAnnotationStoreVersionRequestAnnotationStoreVersionCreatedWaitTypeDef(BaseValidatorModel):
    name: str
    versionName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetAnnotationStoreVersionRequestAnnotationStoreVersionDeletedWaitTypeDef(BaseValidatorModel):
    name: str
    versionName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetReadSetActivationJobRequestReadSetActivationJobCompletedWaitTypeDef(BaseValidatorModel):
    id: str
    sequenceStoreId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetReadSetExportJobRequestReadSetExportJobCompletedWaitTypeDef(BaseValidatorModel):
    sequenceStoreId: str
    id: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetReadSetImportJobRequestReadSetImportJobCompletedWaitTypeDef(BaseValidatorModel):
    id: str
    sequenceStoreId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetReferenceImportJobRequestReferenceImportJobCompletedWaitTypeDef(BaseValidatorModel):
    id: str
    referenceStoreId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetRunRequestRunCompletedWaitTypeDef(BaseValidatorModel):
    id: str
    export: Optional[Sequence[Literal["DEFINITION"]]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetRunRequestRunRunningWaitTypeDef(BaseValidatorModel):
    id: str
    export: Optional[Sequence[Literal["DEFINITION"]]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetRunTaskRequestTaskCompletedWaitTypeDef(BaseValidatorModel):
    id: str
    taskId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetRunTaskRequestTaskRunningWaitTypeDef(BaseValidatorModel):
    id: str
    taskId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetVariantImportRequestVariantImportJobCreatedWaitTypeDef(BaseValidatorModel):
    jobId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetVariantStoreRequestVariantStoreCreatedWaitTypeDef(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetVariantStoreRequestVariantStoreDeletedWaitTypeDef(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetWorkflowRequestWorkflowActiveWaitTypeDef(BaseValidatorModel):
    id: str
    type: Optional[WorkflowTypeType] = None
    export: Optional[Sequence[Literal["DEFINITION"]]] = None
    workflowOwnerId: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class ReadSetListItemTypeDef(BaseValidatorModel):
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

class GetReferenceImportJobResponseTypeDef(BaseValidatorModel):
    id: str
    referenceStoreId: str
    roleArn: str
    status: ReferenceImportJobStatusType
    statusMessage: str
    creationTime: datetime
    completionTime: datetime
    sources: List[ImportReferenceSourceItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetRunResponseTypeDef(BaseValidatorModel):
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

class GetSequenceStoreResponseTypeDef(BaseValidatorModel):
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

class GetShareResponseTypeDef(BaseValidatorModel):
    share: ShareDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSharesResponseTypeDef(BaseValidatorModel):
    shares: List[ShareDetailsTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetVariantImportResponseTypeDef(BaseValidatorModel):
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

class ListReadSetImportJobsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    importJobs: List[ImportReadSetJobItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

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

class ListReferenceImportJobsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    importJobs: List[ImportReferenceJobItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAnnotationImportJobsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    ids: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    filter: Optional[ListAnnotationImportJobsFilterTypeDef] = None

class ListAnnotationImportJobsRequestListAnnotationImportJobsPaginateTypeDef(BaseValidatorModel):
    ids: Optional[Sequence[str]] = None
    filter: Optional[ListAnnotationImportJobsFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMultipartReadSetUploadsRequestListMultipartReadSetUploadsPaginateTypeDef(BaseValidatorModel):
    sequenceStoreId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRunGroupsRequestListRunGroupsPaginateTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRunTasksRequestListRunTasksPaginateTypeDef(BaseValidatorModel):
    id: str
    status: Optional[TaskStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRunsRequestListRunsPaginateTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    runGroupId: Optional[str] = None
    status: Optional[RunStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSharesRequestListSharesPaginateTypeDef(BaseValidatorModel):
    resourceOwner: ResourceOwnerType
    filter: Optional[FilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkflowsRequestListWorkflowsPaginateTypeDef(BaseValidatorModel):
    type: Optional[WorkflowTypeType] = None
    name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAnnotationStoreVersionsRequestListAnnotationStoreVersionsPaginateTypeDef(BaseValidatorModel):
    name: str
    filter: Optional[ListAnnotationStoreVersionsFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAnnotationStoreVersionsRequestRequestTypeDef(BaseValidatorModel):
    name: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filter: Optional[ListAnnotationStoreVersionsFilterTypeDef] = None

class ListAnnotationStoresRequestListAnnotationStoresPaginateTypeDef(BaseValidatorModel):
    ids: Optional[Sequence[str]] = None
    filter: Optional[ListAnnotationStoresFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAnnotationStoresRequestRequestTypeDef(BaseValidatorModel):
    ids: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filter: Optional[ListAnnotationStoresFilterTypeDef] = None

class ListMultipartReadSetUploadsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    uploads: List[MultipartReadSetUploadListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListReadSetUploadPartsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    parts: List[ReadSetUploadPartListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListReferencesResponseTypeDef(BaseValidatorModel):
    nextToken: str
    references: List[ReferenceListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRunGroupsResponseTypeDef(BaseValidatorModel):
    items: List[RunGroupListItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRunTasksResponseTypeDef(BaseValidatorModel):
    items: List[TaskListItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRunsResponseTypeDef(BaseValidatorModel):
    items: List[RunListItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListVariantImportJobsRequestListVariantImportJobsPaginateTypeDef(BaseValidatorModel):
    ids: Optional[Sequence[str]] = None
    filter: Optional[ListVariantImportJobsFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVariantImportJobsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    ids: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    filter: Optional[ListVariantImportJobsFilterTypeDef] = None

class ListVariantImportJobsResponseTypeDef(BaseValidatorModel):
    variantImportJobs: List[VariantImportJobItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListVariantStoresRequestListVariantStoresPaginateTypeDef(BaseValidatorModel):
    ids: Optional[Sequence[str]] = None
    filter: Optional[ListVariantStoresFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVariantStoresRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    ids: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    filter: Optional[ListVariantStoresFilterTypeDef] = None

class ListWorkflowsResponseTypeDef(BaseValidatorModel):
    items: List[WorkflowListItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TsvOptionsTypeDef(BaseValidatorModel):
    readOptions: Optional[ReadOptionsTypeDef] = None

class StartReadSetActivationJobRequestRequestTypeDef(BaseValidatorModel):
    sequenceStoreId: str
    sources: Sequence[StartReadSetActivationJobSourceItemTypeDef]
    clientToken: Optional[str] = None

class StartReferenceImportJobRequestRequestTypeDef(BaseValidatorModel):
    referenceStoreId: str
    roleArn: str
    sources: Sequence[StartReferenceImportJobSourceItemTypeDef]
    clientToken: Optional[str] = None

class StartVariantImportRequestRequestTypeDef(BaseValidatorModel):
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

class ListReadSetActivationJobsRequestListReadSetActivationJobsPaginateTypeDef(BaseValidatorModel):
    sequenceStoreId: str
    filter: Optional[ActivateReadSetFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReadSetActivationJobsRequestRequestTypeDef(BaseValidatorModel):
    sequenceStoreId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filter: Optional[ActivateReadSetFilterTypeDef] = None

class ListReadSetExportJobsRequestListReadSetExportJobsPaginateTypeDef(BaseValidatorModel):
    sequenceStoreId: str
    filter: Optional[ExportReadSetFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReadSetExportJobsRequestRequestTypeDef(BaseValidatorModel):
    sequenceStoreId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filter: Optional[ExportReadSetFilterTypeDef] = None

class ListReadSetImportJobsRequestListReadSetImportJobsPaginateTypeDef(BaseValidatorModel):
    sequenceStoreId: str
    filter: Optional[ImportReadSetFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReadSetImportJobsRequestRequestTypeDef(BaseValidatorModel):
    sequenceStoreId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filter: Optional[ImportReadSetFilterTypeDef] = None

class ListReferenceImportJobsRequestListReferenceImportJobsPaginateTypeDef(BaseValidatorModel):
    referenceStoreId: str
    filter: Optional[ImportReferenceFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReferenceImportJobsRequestRequestTypeDef(BaseValidatorModel):
    referenceStoreId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filter: Optional[ImportReferenceFilterTypeDef] = None

class ListReadSetsRequestListReadSetsPaginateTypeDef(BaseValidatorModel):
    sequenceStoreId: str
    filter: Optional[ReadSetFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReadSetsRequestRequestTypeDef(BaseValidatorModel):
    sequenceStoreId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filter: Optional[ReadSetFilterTypeDef] = None

class ListReadSetUploadPartsRequestListReadSetUploadPartsPaginateTypeDef(BaseValidatorModel):
    sequenceStoreId: str
    uploadId: str
    partSource: ReadSetPartSourceType
    filter: Optional[ReadSetUploadPartListFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReadSetUploadPartsRequestRequestTypeDef(BaseValidatorModel):
    sequenceStoreId: str
    uploadId: str
    partSource: ReadSetPartSourceType
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filter: Optional[ReadSetUploadPartListFilterTypeDef] = None

class ListReferencesRequestListReferencesPaginateTypeDef(BaseValidatorModel):
    referenceStoreId: str
    filter: Optional[ReferenceFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReferencesRequestRequestTypeDef(BaseValidatorModel):
    referenceStoreId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filter: Optional[ReferenceFilterTypeDef] = None

class ListReferenceStoresRequestListReferenceStoresPaginateTypeDef(BaseValidatorModel):
    filter: Optional[ReferenceStoreFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReferenceStoresRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filter: Optional[ReferenceStoreFilterTypeDef] = None

class ListSequenceStoresRequestListSequenceStoresPaginateTypeDef(BaseValidatorModel):
    filter: Optional[SequenceStoreFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSequenceStoresRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filter: Optional[SequenceStoreFilterTypeDef] = None

class ListAnnotationStoresResponseTypeDef(BaseValidatorModel):
    annotationStores: List[AnnotationStoreItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListReferenceStoresResponseTypeDef(BaseValidatorModel):
    nextToken: str
    referenceStores: List[ReferenceStoreDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSequenceStoresResponseTypeDef(BaseValidatorModel):
    nextToken: str
    sequenceStores: List[SequenceStoreDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListVariantStoresResponseTypeDef(BaseValidatorModel):
    variantStores: List[VariantStoreItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReadSetFilesTypeDef(BaseValidatorModel):
    source1: Optional[FileInformationTypeDef] = None
    source2: Optional[FileInformationTypeDef] = None
    index: Optional[FileInformationTypeDef] = None

class ReferenceFilesTypeDef(BaseValidatorModel):
    source: Optional[FileInformationTypeDef] = None
    index: Optional[FileInformationTypeDef] = None

class ListReadSetsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    readSets: List[ReadSetListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetReadSetImportJobResponseTypeDef(BaseValidatorModel):
    id: str
    sequenceStoreId: str
    roleArn: str
    status: ReadSetImportJobStatusType
    statusMessage: str
    creationTime: datetime
    completionTime: datetime
    sources: List[ImportReadSetSourceItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartReadSetImportJobRequestRequestTypeDef(BaseValidatorModel):
    sequenceStoreId: str
    roleArn: str
    sources: Sequence[StartReadSetImportJobSourceItemTypeDef]
    clientToken: Optional[str] = None

class FormatOptionsTypeDef(BaseValidatorModel):
    tsvOptions: Optional[TsvOptionsTypeDef] = None
    vcfOptions: Optional[VcfOptionsTypeDef] = None

class CreateAnnotationStoreResponseTypeDef(BaseValidatorModel):
    id: str
    reference: ReferenceItemTypeDef
    storeFormat: StoreFormatType
    storeOptions: StoreOptionsOutputTypeDef
    status: StoreStatusType
    name: str
    versionName: str
    creationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetAnnotationStoreResponseTypeDef(BaseValidatorModel):
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

class UpdateAnnotationStoreResponseTypeDef(BaseValidatorModel):
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

class CreateAnnotationStoreRequestRequestTypeDef(BaseValidatorModel):
    storeFormat: StoreFormatType
    reference: Optional[ReferenceItemTypeDef] = None
    name: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    versionName: Optional[str] = None
    sseConfig: Optional[SseConfigTypeDef] = None
    storeOptions: Optional[StoreOptionsTypeDef] = None

class CreateAnnotationStoreVersionResponseTypeDef(BaseValidatorModel):
    id: str
    versionName: str
    storeId: str
    versionOptions: VersionOptionsOutputTypeDef
    name: str
    status: VersionStatusType
    creationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetAnnotationStoreVersionResponseTypeDef(BaseValidatorModel):
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

class CreateAnnotationStoreVersionRequestRequestTypeDef(BaseValidatorModel):
    name: str
    versionName: str
    description: Optional[str] = None
    versionOptions: Optional[VersionOptionsTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class GetReadSetMetadataResponseTypeDef(BaseValidatorModel):
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

class GetReferenceMetadataResponseTypeDef(BaseValidatorModel):
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

class GetAnnotationImportResponseTypeDef(BaseValidatorModel):
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

class StartAnnotationImportRequestRequestTypeDef(BaseValidatorModel):
    destinationName: str
    roleArn: str
    items: Sequence[AnnotationImportItemSourceTypeDef]
    versionName: Optional[str] = None
    formatOptions: Optional[FormatOptionsTypeDef] = None
    runLeftNormalization: Optional[bool] = None
    annotationFields: Optional[Mapping[str, str]] = None

