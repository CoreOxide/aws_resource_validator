# Omics Classes

# AbortMultipartReadSetUploadRequestTypeDef

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes


# AcceptShareRequestTypeDef

### shareId
- **Type**: <class 'str'>
- **Required**: Yes


# AcceptShareResponseTypeDef

### status
- **Type**: typing.Literal['ACTIVATING', 'ACTIVE', 'DELETED', 'DELETING', 'FAILED', 'PENDING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ActivateReadSetFilterTypeDef

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### createdAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.TimestampTypeDef]

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.TimestampTypeDef]


# ActivateReadSetJobItemTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActivateReadSetSourceItemTypeDef

### readSetId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'FINISHED', 'IN_PROGRESS', 'NOT_STARTED']
- **Required**: Yes

### statusMessage
- **Type**: typing.Optional[str]


# AnnotationImportItemDetailTypeDef

### source
- **Type**: <class 'str'>
- **Required**: Yes

### jobStatus
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']
- **Required**: Yes


# AnnotationImportItemSourceTypeDef

### source
- **Type**: <class 'str'>
- **Required**: Yes


# AnnotationImportJobItemTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnnotationStoreItemTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnnotationStoreVersionItemTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDeleteReadSetRequestTypeDef

### ids
- **Type**: typing.Sequence[str]
- **Required**: Yes

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes


# BatchDeleteReadSetResponseTypeDef

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.ReadSetBatchErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelAnnotationImportRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelVariantImportRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# CompleteMultipartReadSetUploadRequestTypeDef

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes

### parts
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.omics_classes.CompleteReadSetUploadPartListItemTypeDef]
- **Required**: Yes


# CompleteMultipartReadSetUploadResponseTypeDef

### readSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CompleteReadSetUploadPartListItemTypeDef

### partNumber
- **Type**: <class 'int'>
- **Required**: Yes

### partSource
- **Type**: typing.Literal['SOURCE1', 'SOURCE2']
- **Required**: Yes

### checksum
- **Type**: <class 'str'>
- **Required**: Yes


# CreateAnnotationStoreRequestTypeDef

### storeFormat
- **Type**: typing.Literal['GFF', 'TSV', 'VCF']
- **Required**: Yes

### reference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.ReferenceItemTypeDef]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### versionName
- **Type**: typing.Optional[str]

### sseConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.SseConfigTypeDef]

### storeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.StoreOptionsUnionTypeDef]


# CreateAnnotationStoreVersionRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### versionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.VersionOptionsUnionTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateMultipartReadSetUploadRequestTypeDef

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


# CreateMultipartReadSetUploadResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateReferenceStoreRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### sseConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.SseConfigTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### clientToken
- **Type**: typing.Optional[str]


# CreateRunCacheRequestTypeDef

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


# CreateRunGroupRequestTypeDef

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


# CreateSequenceStoreRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### sseConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.SseConfigTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.S3AccessConfigTypeDef]


# CreateShareRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### principalSubscriber
- **Type**: <class 'str'>
- **Required**: Yes

### shareName
- **Type**: typing.Optional[str]


# CreateShareResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVariantStoreRequestTypeDef

### reference
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ReferenceItemTypeDef'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### sseConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.SseConfigTypeDef]


# CreateWorkflowRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.BlobTypeDef]

### definitionUri
- **Type**: typing.Optional[str]

### main
- **Type**: typing.Optional[str]

### parameterTemplate
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.omics_classes.WorkflowParameterTypeDef]]

### storageCapacity
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### accelerators
- **Type**: typing.Optional[typing.Literal['GPU']]


# DeleteAnnotationStoreRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### force
- **Type**: typing.Optional[bool]


# DeleteAnnotationStoreResponseTypeDef

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAnnotationStoreVersionsRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### versions
- **Type**: typing.Sequence[str]
- **Required**: Yes

### force
- **Type**: typing.Optional[bool]


# DeleteAnnotationStoreVersionsResponseTypeDef

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.VersionDeleteErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteS3AccessPolicyRequestTypeDef

### s3AccessPointArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteShareRequestTypeDef

### shareId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteShareResponseTypeDef

### status
- **Type**: typing.Literal['ACTIVATING', 'ACTIVE', 'DELETED', 'DELETING', 'FAILED', 'PENDING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteVariantStoreRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### force
- **Type**: typing.Optional[bool]


# DeleteVariantStoreResponseTypeDef

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ETagTypeDef

### algorithm
- **Type**: typing.Optional[typing.Literal['BAM_MD5up', 'BAM_SHA256up', 'BAM_SHA512up', 'CRAM_MD5up', 'CRAM_SHA256up', 'CRAM_SHA512up', 'FASTQ_MD5up', 'FASTQ_SHA256up', 'FASTQ_SHA512up']]

### source1
- **Type**: typing.Optional[str]

### source2
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExportReadSetFilterTypeDef

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### createdAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.TimestampTypeDef]

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.TimestampTypeDef]


# ExportReadSetJobDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ExportReadSetTypeDef

### readSetId
- **Type**: <class 'str'>
- **Required**: Yes


# FileInformationTypeDef

### totalParts
- **Type**: typing.Optional[int]

### partSize
- **Type**: typing.Optional[int]

### contentLength
- **Type**: typing.Optional[int]

### s3Access
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.ReadSetS3AccessTypeDef]


# FormatOptionsTypeDef

### tsvOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.TsvOptionsTypeDef]

### vcfOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.VcfOptionsTypeDef]


# GetAnnotationImportRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAnnotationImportRequestWaitTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.WaiterConfigTypeDef]


# GetAnnotationStoreRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetAnnotationStoreRequestWaitExtraTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.WaiterConfigTypeDef]


# GetAnnotationStoreRequestWaitTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.WaiterConfigTypeDef]


# GetAnnotationStoreVersionRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes


# GetAnnotationStoreVersionRequestWaitExtraTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.WaiterConfigTypeDef]


# GetAnnotationStoreVersionRequestWaitTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.WaiterConfigTypeDef]


# GetReadSetResponseTypeDef

### payload
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetReferenceResponseTypeDef

### payload
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRunTaskResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetS3AccessPolicyRequestTypeDef

### s3AccessPointArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetS3AccessPolicyResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetShareRequestTypeDef

### shareId
- **Type**: <class 'str'>
- **Required**: Yes


# GetShareResponseTypeDef

### share
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ShareDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVariantImportRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVariantImportRequestWaitTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.WaiterConfigTypeDef]


# GetVariantStoreRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetVariantStoreRequestWaitExtraTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.WaiterConfigTypeDef]


# GetVariantStoreRequestWaitTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.WaiterConfigTypeDef]


# ImportReadSetFilterTypeDef

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### createdAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.TimestampTypeDef]

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.TimestampTypeDef]


# ImportReadSetJobItemTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImportReadSetSourceItemTypeDef

### sourceFiles
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.SourceFilesTypeDef'>
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


# ImportReferenceFilterTypeDef

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### createdAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.TimestampTypeDef]

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.TimestampTypeDef]


# ImportReferenceJobItemTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImportReferenceSourceItemTypeDef

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


# ListAnnotationImportJobsFilterTypeDef

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### storeName
- **Type**: typing.Optional[str]


# ListAnnotationImportJobsResponseTypeDef

### annotationImportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.AnnotationImportJobItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAnnotationStoreVersionsFilterTypeDef

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]


# ListAnnotationStoreVersionsResponseTypeDef

### annotationStoreVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.AnnotationStoreVersionItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAnnotationStoresFilterTypeDef

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]


# ListAnnotationStoresResponseTypeDef

### annotationStores
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.AnnotationStoreItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMultipartReadSetUploadsRequestPaginateTypeDef

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.PaginatorConfigTypeDef]


# ListMultipartReadSetUploadsRequestTypeDef

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListMultipartReadSetUploadsResponseTypeDef

### uploads
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.MultipartReadSetUploadListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReadSetActivationJobsResponseTypeDef

### activationJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.ActivateReadSetJobItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReadSetExportJobsResponseTypeDef

### exportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.ExportReadSetJobDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReadSetImportJobsResponseTypeDef

### importJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.ImportReadSetJobItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReadSetUploadPartsResponseTypeDef

### parts
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.ReadSetUploadPartListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReadSetsResponseTypeDef

### readSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.ReadSetListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReferenceImportJobsResponseTypeDef

### importJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.ImportReferenceJobItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReferenceStoresResponseTypeDef

### referenceStores
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.ReferenceStoreDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReferencesResponseTypeDef

### references
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.ReferenceListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRunCachesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.PaginatorConfigTypeDef]


# ListRunCachesRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### startingToken
- **Type**: typing.Optional[str]


# ListRunCachesResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.RunCacheListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRunGroupsRequestPaginateTypeDef

### name
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.PaginatorConfigTypeDef]


# ListRunGroupsRequestTypeDef

### name
- **Type**: typing.Optional[str]

### startingToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListRunGroupsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.RunGroupListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRunTasksResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.TaskListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRunsRequestPaginateTypeDef

### name
- **Type**: typing.Optional[str]

### runGroupId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'DELETED', 'FAILED', 'PENDING', 'RUNNING', 'STARTING', 'STOPPING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.PaginatorConfigTypeDef]


# ListRunsRequestTypeDef

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


# ListRunsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.RunListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSequenceStoresResponseTypeDef

### sequenceStores
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.SequenceStoreDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSharesResponseTypeDef

### shares
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.ShareDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVariantImportJobsFilterTypeDef

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### storeName
- **Type**: typing.Optional[str]


# ListVariantImportJobsResponseTypeDef

### variantImportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.VariantImportJobItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListVariantStoresFilterTypeDef

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]


# ListVariantStoresResponseTypeDef

### variantStores
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.VariantStoreItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkflowsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.WorkflowListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# MultipartReadSetUploadListItemTypeDef

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


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutS3AccessPolicyRequestTypeDef

### s3AccessPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### s3AccessPolicy
- **Type**: <class 'str'>
- **Required**: Yes


# PutS3AccessPolicyResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReadOptionsTypeDef

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


# ReadSetBatchErrorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ReadSetFilesTypeDef

### source1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.FileInformationTypeDef]

### source2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.FileInformationTypeDef]

### index
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.FileInformationTypeDef]


# ReadSetFilterTypeDef

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVATING', 'ACTIVE', 'ARCHIVED', 'DELETED', 'DELETING', 'PROCESSING_UPLOAD', 'UPLOAD_FAILED']]

### referenceArn
- **Type**: typing.Optional[str]

### createdAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.TimestampTypeDef]

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.TimestampTypeDef]

### sampleId
- **Type**: typing.Optional[str]

### subjectId
- **Type**: typing.Optional[str]

### generatedFrom
- **Type**: typing.Optional[str]

### creationType
- **Type**: typing.Optional[typing.Literal['IMPORT', 'UPLOAD']]


# ReadSetListItemTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ReadSetS3AccessTypeDef

### s3Uri
- **Type**: typing.Optional[str]


# ReadSetUploadPartListFilterTypeDef

### createdAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.TimestampTypeDef]

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.TimestampTypeDef]


# ReadSetUploadPartListItemTypeDef

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


# ReferenceFilesTypeDef

### source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.FileInformationTypeDef]

### index
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.FileInformationTypeDef]


# ReferenceFilterTypeDef

### name
- **Type**: typing.Optional[str]

### md5
- **Type**: typing.Optional[str]

### createdAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.TimestampTypeDef]

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.TimestampTypeDef]


# ReferenceItemTypeDef

### referenceArn
- **Type**: typing.Optional[str]


# ReferenceListItemTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ReferenceStoreDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ReferenceStoreFilterTypeDef

### name
- **Type**: typing.Optional[str]

### createdAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.TimestampTypeDef]

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.TimestampTypeDef]


# ResponseMetadataTypeDef

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


# RunCacheListItemTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RunGroupListItemTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RunListItemTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RunLogLocationTypeDef

### engineLogStream
- **Type**: typing.Optional[str]

### runLogStream
- **Type**: typing.Optional[str]


# S3AccessConfigTypeDef

### accessLogLocation
- **Type**: typing.Optional[str]


# SequenceInformationTypeDef

### totalReadCount
- **Type**: typing.Optional[int]

### totalBaseCount
- **Type**: typing.Optional[int]

### generatedFrom
- **Type**: typing.Optional[str]

### alignment
- **Type**: typing.Optional[str]


# SequenceStoreDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SequenceStoreFilterTypeDef

### name
- **Type**: typing.Optional[str]

### createdAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.TimestampTypeDef]

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.TimestampTypeDef]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]

### updatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.TimestampTypeDef]

### updatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.TimestampTypeDef]


# SequenceStoreS3AccessTypeDef

### s3Uri
- **Type**: typing.Optional[str]

### s3AccessPointArn
- **Type**: typing.Optional[str]

### accessLogLocation
- **Type**: typing.Optional[str]


# ShareDetailsTypeDef

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


# SourceFilesTypeDef

### source1
- **Type**: <class 'str'>
- **Required**: Yes

### source2
- **Type**: typing.Optional[str]


# SseConfigTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StartAnnotationImportRequestTypeDef

### destinationName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.omics_classes.AnnotationImportItemSourceTypeDef]
- **Required**: Yes

### versionName
- **Type**: typing.Optional[str]

### formatOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.FormatOptionsTypeDef]

### runLeftNormalization
- **Type**: typing.Optional[bool]

### annotationFields
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartAnnotationImportResponseTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartReadSetActivationJobRequestTypeDef

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.omics_classes.StartReadSetActivationJobSourceItemTypeDef]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# StartReadSetActivationJobSourceItemTypeDef

### readSetId
- **Type**: <class 'str'>
- **Required**: Yes


# StartReadSetExportJobRequestTypeDef

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.omics_classes.ExportReadSetTypeDef]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# StartReadSetImportJobRequestTypeDef

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.omics_classes.StartReadSetImportJobSourceItemTypeDef]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# StartReadSetImportJobSourceItemTypeDef

### sourceFiles
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.SourceFilesTypeDef'>
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


# StartReferenceImportJobRequestTypeDef

### referenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.omics_classes.StartReferenceImportJobSourceItemTypeDef]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# StartReferenceImportJobSourceItemTypeDef

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


# StartRunRequestTypeDef

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


# StartVariantImportRequestTypeDef

### destinationName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.omics_classes.VariantImportItemSourceTypeDef]
- **Required**: Yes

### runLeftNormalization
- **Type**: typing.Optional[bool]

### annotationFields
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartVariantImportResponseTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StoreOptionsOutputTypeDef

### tsvStoreOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.TsvStoreOptionsOutputTypeDef]


# StoreOptionsTypeDef

### tsvStoreOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.TsvStoreOptionsTypeDef]


# StoreOptionsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TaskListItemTypeDef

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


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TsvOptionsTypeDef

### readOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.ReadOptionsTypeDef]


# TsvStoreOptionsOutputTypeDef

### annotationType
- **Type**: typing.Optional[typing.Literal['CHR_POS', 'CHR_POS_REF_ALT', 'CHR_START_END_ONE_BASE', 'CHR_START_END_REF_ALT_ONE_BASE', 'CHR_START_END_REF_ALT_ZERO_BASE', 'CHR_START_END_ZERO_BASE', 'GENERIC']]

### formatToHeader
- **Type**: typing.Optional[typing.Dict[typing.Literal['ALT', 'CHR', 'END', 'POS', 'REF', 'START'], str]]

### schema
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Literal['BOOLEAN', 'DOUBLE', 'FLOAT', 'INT', 'LONG', 'STRING']]]]


# TsvStoreOptionsTypeDef

### annotationType
- **Type**: typing.Optional[typing.Literal['CHR_POS', 'CHR_POS_REF_ALT', 'CHR_START_END_ONE_BASE', 'CHR_START_END_REF_ALT_ONE_BASE', 'CHR_START_END_REF_ALT_ZERO_BASE', 'CHR_START_END_ZERO_BASE', 'GENERIC']]

### formatToHeader
- **Type**: typing.Optional[typing.Mapping[typing.Literal['ALT', 'CHR', 'END', 'POS', 'REF', 'START'], str]]

### schema
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Literal['BOOLEAN', 'DOUBLE', 'FLOAT', 'INT', 'LONG', 'STRING']]]]


# TsvVersionOptionsOutputTypeDef

### annotationType
- **Type**: typing.Optional[typing.Literal['CHR_POS', 'CHR_POS_REF_ALT', 'CHR_START_END_ONE_BASE', 'CHR_START_END_REF_ALT_ONE_BASE', 'CHR_START_END_REF_ALT_ZERO_BASE', 'CHR_START_END_ZERO_BASE', 'GENERIC']]

### formatToHeader
- **Type**: typing.Optional[typing.Dict[typing.Literal['ALT', 'CHR', 'END', 'POS', 'REF', 'START'], str]]

### schema
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Literal['BOOLEAN', 'DOUBLE', 'FLOAT', 'INT', 'LONG', 'STRING']]]]


# TsvVersionOptionsTypeDef

### annotationType
- **Type**: typing.Optional[typing.Literal['CHR_POS', 'CHR_POS_REF_ALT', 'CHR_START_END_ONE_BASE', 'CHR_START_END_REF_ALT_ONE_BASE', 'CHR_START_END_REF_ALT_ZERO_BASE', 'CHR_START_END_ZERO_BASE', 'GENERIC']]

### formatToHeader
- **Type**: typing.Optional[typing.Mapping[typing.Literal['ALT', 'CHR', 'END', 'POS', 'REF', 'START'], str]]

### schema
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Literal['BOOLEAN', 'DOUBLE', 'FLOAT', 'INT', 'LONG', 'STRING']]]]


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAnnotationStoreRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateAnnotationStoreVersionRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateVariantStoreRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UploadReadSetPartRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.BlobTypeDef'>
- **Required**: Yes


# UploadReadSetPartResponseTypeDef

### checksum
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VariantImportItemDetailTypeDef

### source
- **Type**: <class 'str'>
- **Required**: Yes

### jobStatus
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']
- **Required**: Yes

### statusMessage
- **Type**: typing.Optional[str]


# VariantImportItemSourceTypeDef

### source
- **Type**: <class 'str'>
- **Required**: Yes


# VariantImportJobItemTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VariantStoreItemTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VcfOptionsTypeDef

### ignoreQualField
- **Type**: typing.Optional[bool]

### ignoreFilterField
- **Type**: typing.Optional[bool]


# VersionDeleteErrorTypeDef

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# VersionOptionsOutputTypeDef

### tsvVersionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.TsvVersionOptionsOutputTypeDef]


# VersionOptionsTypeDef

### tsvVersionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.TsvVersionOptionsTypeDef]


# VersionOptionsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


# WorkflowListItemTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WorkflowParameterTypeDef

### description
- **Type**: typing.Optional[str]

### optional
- **Type**: typing.Optional[bool]


