# Omics Classes

# AbortMultipartReadSetUploadRequest

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes


# AcceptShareRequest

### shareId
- **Type**: <class 'str'>
- **Required**: Yes


# AcceptShareResponse

### status
- **Type**: typing.Literal['ACTIVATING', 'ACTIVE', 'DELETED', 'DELETING', 'FAILED', 'PENDING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes


# ActivateReadSetFilter

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### createdAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.Timestamp]

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.Timestamp]


# ActivateReadSetJobItem

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActivateReadSetSourceItem

### readSetId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'FINISHED', 'IN_PROGRESS', 'NOT_STARTED']
- **Required**: Yes

### statusMessage
- **Type**: typing.Optional[str]


# AnnotationImportItemDetail

### source
- **Type**: <class 'str'>
- **Required**: Yes

### jobStatus
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']
- **Required**: Yes


# AnnotationImportItemSource

### source
- **Type**: <class 'str'>
- **Required**: Yes


# AnnotationImportJobItem

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnnotationStoreItem

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnnotationStoreVersionItem

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDeleteReadSetRequest

### ids
- **Type**: typing.Sequence[str]
- **Required**: Yes

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes


# BatchDeleteReadSetResponse

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.ReadSetBatchError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes


# Blob

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelAnnotationImportRequest

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelVariantImportRequest

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# CompleteMultipartReadSetUploadRequest

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes

### parts
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.omics_classes.CompleteReadSetUploadPartListItem]
- **Required**: Yes


# CompleteMultipartReadSetUploadResponse

### readSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes


# CompleteReadSetUploadPartListItem

### partNumber
- **Type**: <class 'int'>
- **Required**: Yes

### partSource
- **Type**: typing.Literal['SOURCE1', 'SOURCE2']
- **Required**: Yes

### checksum
- **Type**: <class 'str'>
- **Required**: Yes


# CreateAnnotationStoreRequest

### storeFormat
- **Type**: typing.Literal['GFF', 'TSV', 'VCF']
- **Required**: Yes

### reference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.ReferenceItem]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### versionName
- **Type**: typing.Optional[str]

### sseConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.SseConfig]

### storeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.StoreOptionsUnion]


# CreateAnnotationStoreVersionRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### versionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.VersionOptionsUnion]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateMultipartReadSetUploadRequest

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### sourceFileType
- **Type**: typing.Literal['BAM', 'CRAM', 'FASTQ', 'UBAM']
- **Required**: Yes

### subjectId
- **Type**: <class 'str'>
- **Required**: Yes

### sampleId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### generatedFrom
- **Type**: typing.Optional[str]

### referenceArn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateMultipartReadSetUploadResponse

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes

### sourceFileType
- **Type**: typing.Literal['BAM', 'CRAM', 'FASTQ', 'UBAM']
- **Required**: Yes

### subjectId
- **Type**: <class 'str'>
- **Required**: Yes

### sampleId
- **Type**: <class 'str'>
- **Required**: Yes

### generatedFrom
- **Type**: <class 'str'>
- **Required**: Yes

### referenceArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes


# CreateReferenceStoreRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### sseConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.SseConfig]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### clientToken
- **Type**: typing.Optional[str]


# CreateRunCacheRequest

### cacheS3Location
- **Type**: <class 'str'>
- **Required**: Yes

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### cacheBehavior
- **Type**: typing.Optional[typing.Literal['CACHE_ALWAYS', 'CACHE_ON_FAILURE']]

### description
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### cacheBucketOwnerId
- **Type**: typing.Optional[str]


# CreateRunGroupRequest

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### maxCpus
- **Type**: typing.Optional[int]

### maxRuns
- **Type**: typing.Optional[int]

### maxDuration
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### maxGpus
- **Type**: typing.Optional[int]


# CreateSequenceStoreRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### sseConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.SseConfig]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### clientToken
- **Type**: typing.Optional[str]

### fallbackLocation
- **Type**: typing.Optional[str]

### eTagAlgorithmFamily
- **Type**: typing.Optional[typing.Literal['MD5up', 'SHA256up', 'SHA512up']]

### propagatedSetLevelTags
- **Type**: typing.Optional[typing.Sequence[str]]

### s3AccessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.S3AccessConfig]


# CreateShareRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### principalSubscriber
- **Type**: <class 'str'>
- **Required**: Yes

### shareName
- **Type**: typing.Optional[str]


# CreateShareResponse

### shareId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVATING', 'ACTIVE', 'DELETED', 'DELETING', 'FAILED', 'PENDING']
- **Required**: Yes

### shareName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVariantStoreRequest

### reference
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ReferenceItem'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### sseConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.SseConfig]


# CreateWorkflowRequest

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### engine
- **Type**: typing.Optional[typing.Literal['CWL', 'NEXTFLOW', 'WDL']]

### definitionZip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.Blob]

### definitionUri
- **Type**: typing.Optional[str]

### main
- **Type**: typing.Optional[str]

### parameterTemplate
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.omics_classes.WorkflowParameter]]

### storageCapacity
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### accelerators
- **Type**: typing.Optional[typing.Literal['GPU']]


# DeleteAnnotationStoreRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### force
- **Type**: typing.Optional[bool]


# DeleteAnnotationStoreResponse

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAnnotationStoreVersionsRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### versions
- **Type**: typing.Sequence[str]
- **Required**: Yes

### force
- **Type**: typing.Optional[bool]


# DeleteAnnotationStoreVersionsResponse

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.VersionDeleteError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteS3AccessPolicyRequest

### s3AccessPointArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteShareRequest

### shareId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteShareResponse

### status
- **Type**: typing.Literal['ACTIVATING', 'ACTIVE', 'DELETED', 'DELETING', 'FAILED', 'PENDING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteVariantStoreRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### force
- **Type**: typing.Optional[bool]


# DeleteVariantStoreResponse

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes


# ETag

### algorithm
- **Type**: typing.Optional[typing.Literal['BAM_MD5up', 'BAM_SHA256up', 'BAM_SHA512up', 'CRAM_MD5up', 'CRAM_SHA256up', 'CRAM_SHA512up', 'FASTQ_MD5up', 'FASTQ_SHA256up', 'FASTQ_SHA512up']]

### source1
- **Type**: typing.Optional[str]

### source2
- **Type**: typing.Optional[str]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes


# ExportReadSet

### readSetId
- **Type**: <class 'str'>
- **Required**: Yes


# ExportReadSetFilter

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### createdAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.Timestamp]

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.Timestamp]


# ExportReadSetJobDetail

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FileInformation

### totalParts
- **Type**: typing.Optional[int]

### partSize
- **Type**: typing.Optional[int]

### contentLength
- **Type**: typing.Optional[int]

### s3Access
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.ReadSetS3Access]


# FormatOptions

### tsvOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.TsvOptions]

### vcfOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.VcfOptions]


# GetAnnotationImportRequest

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAnnotationImportRequestWait

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetAnnotationStoreRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetAnnotationStoreRequestWait

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetAnnotationStoreRequestWaitExtra

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetAnnotationStoreVersionRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes


# GetAnnotationStoreVersionRequestWait

### name
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetAnnotationStoreVersionRequestWaitExtra

### name
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetReadSetResponse

### payload
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes


# GetReferenceResponse

### payload
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes


# GetRunTaskResponse

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'PENDING', 'RUNNING', 'STARTING', 'STOPPING']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### cpus
- **Type**: <class 'int'>
- **Required**: Yes

### cacheHit
- **Type**: <class 'bool'>
- **Required**: Yes

### cacheS3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### memory
- **Type**: <class 'int'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### stopTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### logStream
- **Type**: <class 'str'>
- **Required**: Yes

### gpus
- **Type**: <class 'int'>
- **Required**: Yes

### instanceType
- **Type**: <class 'str'>
- **Required**: Yes

### failureReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes


# GetS3AccessPolicyRequest

### s3AccessPointArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetS3AccessPolicyResponse

### s3AccessPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### storeId
- **Type**: <class 'str'>
- **Required**: Yes

### storeType
- **Type**: typing.Literal['REFERENCE_STORE', 'SEQUENCE_STORE']
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### s3AccessPolicy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes


# GetShareRequest

### shareId
- **Type**: <class 'str'>
- **Required**: Yes


# GetShareResponse

### share
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ShareDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes


# GetVariantImportRequest

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVariantImportRequestWait

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetVariantStoreRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetVariantStoreRequestWait

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetVariantStoreRequestWaitExtra

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# ImportReadSetFilter

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### createdAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.Timestamp]

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.Timestamp]


# ImportReadSetJobItem

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImportReadSetSourceItem

### sourceFiles
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.SourceFiles'>
- **Required**: Yes

### sourceFileType
- **Type**: typing.Literal['BAM', 'CRAM', 'FASTQ', 'UBAM']
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'FINISHED', 'IN_PROGRESS', 'NOT_STARTED']
- **Required**: Yes

### subjectId
- **Type**: <class 'str'>
- **Required**: Yes

### sampleId
- **Type**: <class 'str'>
- **Required**: Yes

### statusMessage
- **Type**: typing.Optional[str]

### generatedFrom
- **Type**: typing.Optional[str]

### referenceArn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### readSetId
- **Type**: typing.Optional[str]


# ImportReferenceFilter

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### createdAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.Timestamp]

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.Timestamp]


# ImportReferenceJobItem

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImportReferenceSourceItem

### status
- **Type**: typing.Literal['FAILED', 'FINISHED', 'IN_PROGRESS', 'NOT_STARTED']
- **Required**: Yes

### sourceFile
- **Type**: typing.Optional[str]

### statusMessage
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### referenceId
- **Type**: typing.Optional[str]


# ListAnnotationImportJobsFilter

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### storeName
- **Type**: typing.Optional[str]


# ListAnnotationImportJobsResponse

### annotationImportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.AnnotationImportJobItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAnnotationStoreVersionsFilter

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]


# ListAnnotationStoreVersionsResponse

### annotationStoreVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.AnnotationStoreVersionItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAnnotationStoresFilter

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]


# ListAnnotationStoresResponse

### annotationStores
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.AnnotationStoreItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMultipartReadSetUploadsRequest

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListMultipartReadSetUploadsRequestPaginate

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.PaginatorConfig]


# ListMultipartReadSetUploadsResponse

### uploads
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.MultipartReadSetUploadListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReadSetActivationJobsResponse

### activationJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.ActivateReadSetJobItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReadSetExportJobsResponse

### exportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.ExportReadSetJobDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReadSetImportJobsResponse

### importJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.ImportReadSetJobItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReadSetUploadPartsResponse

### parts
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.ReadSetUploadPartListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReadSetsResponse

### readSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.ReadSetListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReferenceImportJobsResponse

### importJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.ImportReferenceJobItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReferenceStoresResponse

### referenceStores
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.ReferenceStoreDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReferencesResponse

### references
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.ReferenceListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRunCachesRequest

### maxResults
- **Type**: typing.Optional[int]

### startingToken
- **Type**: typing.Optional[str]


# ListRunCachesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.PaginatorConfig]


# ListRunCachesResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.RunCacheListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRunGroupsRequest

### name
- **Type**: typing.Optional[str]

### startingToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListRunGroupsRequestPaginate

### name
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.PaginatorConfig]


# ListRunGroupsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.RunGroupListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRunTasksResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.TaskListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRunsRequest

### name
- **Type**: typing.Optional[str]

### runGroupId
- **Type**: typing.Optional[str]

### startingToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'DELETED', 'FAILED', 'PENDING', 'RUNNING', 'STARTING', 'STOPPING']]


# ListRunsRequestPaginate

### name
- **Type**: typing.Optional[str]

### runGroupId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'DELETED', 'FAILED', 'PENDING', 'RUNNING', 'STARTING', 'STOPPING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.PaginatorConfig]


# ListRunsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.RunListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSequenceStoresResponse

### sequenceStores
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.SequenceStoreDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSharesResponse

### shares
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.ShareDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes


# ListVariantImportJobsFilter

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### storeName
- **Type**: typing.Optional[str]


# ListVariantImportJobsResponse

### variantImportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.VariantImportJobItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListVariantStoresFilter

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]


# ListVariantStoresResponse

### variantStores
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.VariantStoreItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkflowsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.WorkflowListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# MultipartReadSetUploadListItem

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes

### sourceFileType
- **Type**: typing.Literal['BAM', 'CRAM', 'FASTQ', 'UBAM']
- **Required**: Yes

### subjectId
- **Type**: <class 'str'>
- **Required**: Yes

### sampleId
- **Type**: <class 'str'>
- **Required**: Yes

### generatedFrom
- **Type**: <class 'str'>
- **Required**: Yes

### referenceArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutS3AccessPolicyRequest

### s3AccessPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### s3AccessPolicy
- **Type**: <class 'str'>
- **Required**: Yes


# PutS3AccessPolicyResponse

### s3AccessPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### storeId
- **Type**: <class 'str'>
- **Required**: Yes

### storeType
- **Type**: typing.Literal['REFERENCE_STORE', 'SEQUENCE_STORE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes


# ReadOptions

### sep
- **Type**: typing.Optional[str]

### encoding
- **Type**: typing.Optional[str]

### quote
- **Type**: typing.Optional[str]

### quoteAll
- **Type**: typing.Optional[bool]

### escape
- **Type**: typing.Optional[str]

### escapeQuotes
- **Type**: typing.Optional[bool]

### comment
- **Type**: typing.Optional[str]

### header
- **Type**: typing.Optional[bool]

### lineSep
- **Type**: typing.Optional[str]


# ReadSetBatchError

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ReadSetFiles

### source1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.FileInformation]

### source2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.FileInformation]

### index
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.FileInformation]


# ReadSetFilter

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVATING', 'ACTIVE', 'ARCHIVED', 'DELETED', 'DELETING', 'PROCESSING_UPLOAD', 'UPLOAD_FAILED']]

### referenceArn
- **Type**: typing.Optional[str]

### createdAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.Timestamp]

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.Timestamp]

### sampleId
- **Type**: typing.Optional[str]

### subjectId
- **Type**: typing.Optional[str]

### generatedFrom
- **Type**: typing.Optional[str]

### creationType
- **Type**: typing.Optional[typing.Literal['IMPORT', 'UPLOAD']]


# ReadSetListItem

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ReadSetS3Access

### s3Uri
- **Type**: typing.Optional[str]


# ReadSetUploadPartListFilter

### createdAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.Timestamp]

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.Timestamp]


# ReadSetUploadPartListItem

### partNumber
- **Type**: <class 'int'>
- **Required**: Yes

### partSize
- **Type**: <class 'int'>
- **Required**: Yes

### partSource
- **Type**: typing.Literal['SOURCE1', 'SOURCE2']
- **Required**: Yes

### checksum
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]


# ReferenceFiles

### source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.FileInformation]

### index
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.FileInformation]


# ReferenceFilter

### name
- **Type**: typing.Optional[str]

### md5
- **Type**: typing.Optional[str]

### createdAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.Timestamp]

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.Timestamp]


# ReferenceItem

### referenceArn
- **Type**: typing.Optional[str]


# ReferenceListItem

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ReferenceStoreDetail

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ReferenceStoreFilter

### name
- **Type**: typing.Optional[str]

### createdAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.Timestamp]

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.Timestamp]


# ResponseMetadata

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HTTPStatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### HTTPHeaders
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RetryAttempts
- **Type**: <class 'int'>
- **Required**: Yes

### HostId
- **Type**: typing.Optional[str]


# RunCacheListItem

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RunGroupListItem

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RunListItem

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RunLogLocation

### engineLogStream
- **Type**: typing.Optional[str]

### runLogStream
- **Type**: typing.Optional[str]


# S3AccessConfig

### accessLogLocation
- **Type**: typing.Optional[str]


# SequenceInformation

### totalReadCount
- **Type**: typing.Optional[int]

### totalBaseCount
- **Type**: typing.Optional[int]

### generatedFrom
- **Type**: typing.Optional[str]

### alignment
- **Type**: typing.Optional[str]


# SequenceStoreDetail

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SequenceStoreFilter

### name
- **Type**: typing.Optional[str]

### createdAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.Timestamp]

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.Timestamp]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]

### updatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.Timestamp]

### updatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.Timestamp]


# SequenceStoreS3Access

### s3Uri
- **Type**: typing.Optional[str]

### s3AccessPointArn
- **Type**: typing.Optional[str]

### accessLogLocation
- **Type**: typing.Optional[str]


# ShareDetails

### shareId
- **Type**: typing.Optional[str]

### resourceArn
- **Type**: typing.Optional[str]

### resourceId
- **Type**: typing.Optional[str]

### principalSubscriber
- **Type**: typing.Optional[str]

### ownerId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVATING', 'ACTIVE', 'DELETED', 'DELETING', 'FAILED', 'PENDING']]

### statusMessage
- **Type**: typing.Optional[str]

### shareName
- **Type**: typing.Optional[str]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### updateTime
- **Type**: typing.Optional[datetime.datetime]


# SourceFiles

### source1
- **Type**: <class 'str'>
- **Required**: Yes

### source2
- **Type**: typing.Optional[str]


# SseConfig

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StartAnnotationImportRequest

### destinationName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.omics_classes.AnnotationImportItemSource]
- **Required**: Yes

### versionName
- **Type**: typing.Optional[str]

### formatOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.FormatOptions]

### runLeftNormalization
- **Type**: typing.Optional[bool]

### annotationFields
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartAnnotationImportResponse

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes


# StartReadSetActivationJobRequest

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.omics_classes.StartReadSetActivationJobSourceItem]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# StartReadSetActivationJobSourceItem

### readSetId
- **Type**: <class 'str'>
- **Required**: Yes


# StartReadSetExportJobRequest

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### destination
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.omics_classes.ExportReadSet]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# StartReadSetImportJobRequest

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.omics_classes.StartReadSetImportJobSourceItem]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# StartReadSetImportJobSourceItem

### sourceFiles
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.SourceFiles'>
- **Required**: Yes

### sourceFileType
- **Type**: typing.Literal['BAM', 'CRAM', 'FASTQ', 'UBAM']
- **Required**: Yes

### subjectId
- **Type**: <class 'str'>
- **Required**: Yes

### sampleId
- **Type**: <class 'str'>
- **Required**: Yes

### generatedFrom
- **Type**: typing.Optional[str]

### referenceArn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartReferenceImportJobRequest

### referenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.omics_classes.StartReferenceImportJobSourceItem]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# StartReferenceImportJobSourceItem

### sourceFile
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartRunRequest

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### workflowId
- **Type**: typing.Optional[str]

### workflowType
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'READY2RUN']]

### runId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### cacheId
- **Type**: typing.Optional[str]

### cacheBehavior
- **Type**: typing.Optional[typing.Literal['CACHE_ALWAYS', 'CACHE_ON_FAILURE']]

### runGroupId
- **Type**: typing.Optional[str]

### priority
- **Type**: typing.Optional[int]

### parameters
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### storageCapacity
- **Type**: typing.Optional[int]

### outputUri
- **Type**: typing.Optional[str]

### logLevel
- **Type**: typing.Optional[typing.Literal['ALL', 'ERROR', 'FATAL', 'OFF']]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### retentionMode
- **Type**: typing.Optional[typing.Literal['REMOVE', 'RETAIN']]

### storageType
- **Type**: typing.Optional[typing.Literal['DYNAMIC', 'STATIC']]

### workflowOwnerId
- **Type**: typing.Optional[str]


# StartVariantImportRequest

### destinationName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.omics_classes.VariantImportItemSource]
- **Required**: Yes

### runLeftNormalization
- **Type**: typing.Optional[bool]

### annotationFields
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartVariantImportResponse

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes


# StoreOptions

### tsvStoreOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.TsvStoreOptions]


# StoreOptionsOutput

### tsvStoreOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.TsvStoreOptionsOutput]


# StoreOptionsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TaskListItem

### taskId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'PENDING', 'RUNNING', 'STARTING', 'STOPPING']]

### name
- **Type**: typing.Optional[str]

### cpus
- **Type**: typing.Optional[int]

### cacheHit
- **Type**: typing.Optional[bool]

### cacheS3Uri
- **Type**: typing.Optional[str]

### memory
- **Type**: typing.Optional[int]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### stopTime
- **Type**: typing.Optional[datetime.datetime]

### gpus
- **Type**: typing.Optional[int]

### instanceType
- **Type**: typing.Optional[str]


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TsvOptions

### readOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.ReadOptions]


# TsvStoreOptions

### annotationType
- **Type**: typing.Optional[typing.Literal['CHR_POS', 'CHR_POS_REF_ALT', 'CHR_START_END_ONE_BASE', 'CHR_START_END_REF_ALT_ONE_BASE', 'CHR_START_END_REF_ALT_ZERO_BASE', 'CHR_START_END_ZERO_BASE', 'GENERIC']]

### formatToHeader
- **Type**: typing.Optional[typing.Mapping[typing.Literal['ALT', 'CHR', 'END', 'POS', 'REF', 'START'], str]]

### schema
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Literal['BOOLEAN', 'DOUBLE', 'FLOAT', 'INT', 'LONG', 'STRING']]]]


# TsvStoreOptionsOutput

### annotationType
- **Type**: typing.Optional[typing.Literal['CHR_POS', 'CHR_POS_REF_ALT', 'CHR_START_END_ONE_BASE', 'CHR_START_END_REF_ALT_ONE_BASE', 'CHR_START_END_REF_ALT_ZERO_BASE', 'CHR_START_END_ZERO_BASE', 'GENERIC']]

### formatToHeader
- **Type**: typing.Optional[typing.Dict[typing.Literal['ALT', 'CHR', 'END', 'POS', 'REF', 'START'], str]]

### schema
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Literal['BOOLEAN', 'DOUBLE', 'FLOAT', 'INT', 'LONG', 'STRING']]]]


# TsvVersionOptions

### annotationType
- **Type**: typing.Optional[typing.Literal['CHR_POS', 'CHR_POS_REF_ALT', 'CHR_START_END_ONE_BASE', 'CHR_START_END_REF_ALT_ONE_BASE', 'CHR_START_END_REF_ALT_ZERO_BASE', 'CHR_START_END_ZERO_BASE', 'GENERIC']]

### formatToHeader
- **Type**: typing.Optional[typing.Mapping[typing.Literal['ALT', 'CHR', 'END', 'POS', 'REF', 'START'], str]]

### schema
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Literal['BOOLEAN', 'DOUBLE', 'FLOAT', 'INT', 'LONG', 'STRING']]]]


# TsvVersionOptionsOutput

### annotationType
- **Type**: typing.Optional[typing.Literal['CHR_POS', 'CHR_POS_REF_ALT', 'CHR_START_END_ONE_BASE', 'CHR_START_END_REF_ALT_ONE_BASE', 'CHR_START_END_REF_ALT_ZERO_BASE', 'CHR_START_END_ZERO_BASE', 'GENERIC']]

### formatToHeader
- **Type**: typing.Optional[typing.Dict[typing.Literal['ALT', 'CHR', 'END', 'POS', 'REF', 'START'], str]]

### schema
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Literal['BOOLEAN', 'DOUBLE', 'FLOAT', 'INT', 'LONG', 'STRING']]]]


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAnnotationStoreRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateAnnotationStoreVersionRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateVariantStoreRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UploadReadSetPartRequest

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes

### partSource
- **Type**: typing.Literal['SOURCE1', 'SOURCE2']
- **Required**: Yes

### partNumber
- **Type**: <class 'int'>
- **Required**: Yes

### payload
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.Blob'>
- **Required**: Yes


# UploadReadSetPartResponse

### checksum
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadata'>
- **Required**: Yes


# VariantImportItemDetail

### source
- **Type**: <class 'str'>
- **Required**: Yes

### jobStatus
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']
- **Required**: Yes

### statusMessage
- **Type**: typing.Optional[str]


# VariantImportItemSource

### source
- **Type**: <class 'str'>
- **Required**: Yes


# VariantImportJobItem

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VariantStoreItem

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VcfOptions

### ignoreQualField
- **Type**: typing.Optional[bool]

### ignoreFilterField
- **Type**: typing.Optional[bool]


# VersionDeleteError

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# VersionOptions

### tsvVersionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.TsvVersionOptions]


# VersionOptionsOutput

### tsvVersionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.TsvVersionOptionsOutput]


# VersionOptionsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


# WorkflowListItem

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WorkflowParameter

### description
- **Type**: typing.Optional[str]

### optional
- **Type**: typing.Optional[bool]


