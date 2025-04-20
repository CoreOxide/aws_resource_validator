# Omics Omics Classes

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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# ActivateReadSetFilter

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### createdAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# ActivateReadSetJobItem

### id
- **Type**: <class 'str'>
- **Required**: Yes

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### completionTime
- **Type**: typing.Optional[datetime.datetime]


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

### id
- **Type**: <class 'str'>
- **Required**: Yes

### destinationName
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### completionTime
- **Type**: typing.Optional[datetime.datetime]

### runLeftNormalization
- **Type**: typing.Optional[bool]

### annotationFields
- **Type**: typing.Optional[typing.Dict[str, str]]


# AnnotationStoreItem

### id
- **Type**: <class 'str'>
- **Required**: Yes

### reference
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ReferenceItem'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### storeArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### storeFormat
- **Type**: typing.Literal['GFF', 'TSV', 'VCF']
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### sseConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.SseConfig'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### storeSizeBytes
- **Type**: <class 'int'>
- **Required**: Yes


# AnnotationStoreVersionItem

### storeId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### versionArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### versionSizeBytes
- **Type**: <class 'int'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDeleteReadSetRequest

### ids
- **Type**: typing.List[str]
- **Required**: Yes

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes


# BatchDeleteReadSetResponse

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.ReadSetBatchError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# CancelAnnotationImportRequest

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelRunRequest

### id
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.CompleteReadSetUploadPartListItem]
- **Required**: Yes


# CompleteMultipartReadSetUploadResponse

### readSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.ReferenceItem]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### versionName
- **Type**: typing.Optional[str]

### sseConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.SseConfig]

### storeOptions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.omics.omics_classes.StoreOptions, aws_resource_validator.pydantic_models.omics.omics_classes.StoreOptionsOutput, NoneType]


# CreateAnnotationStoreResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### reference
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ReferenceItem'>
- **Required**: Yes

### storeFormat
- **Type**: typing.Literal['GFF', 'TSV', 'VCF']
- **Required**: Yes

### storeOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.StoreOptionsOutput'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.omics.omics_classes.VersionOptions, aws_resource_validator.pydantic_models.omics.omics_classes.VersionOptionsOutput, NoneType]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateAnnotationStoreVersionResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### storeId
- **Type**: <class 'str'>
- **Required**: Yes

### versionOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.VersionOptionsOutput'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


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
- **Type**: typing.Optional[typing.Dict[str, str]]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# CreateReferenceStoreRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### sseConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.SseConfig]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### clientToken
- **Type**: typing.Optional[str]


# CreateReferenceStoreResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### sseConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.SseConfig'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


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
- **Type**: typing.Optional[typing.Dict[str, str]]

### cacheBucketOwnerId
- **Type**: typing.Optional[str]


# CreateRunCacheResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'FAILED']
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


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
- **Type**: typing.Optional[typing.Dict[str, str]]

### maxGpus
- **Type**: typing.Optional[int]


# CreateRunGroupResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSequenceStoreRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### sseConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.SseConfig]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### clientToken
- **Type**: typing.Optional[str]

### fallbackLocation
- **Type**: typing.Optional[str]

### eTagAlgorithmFamily
- **Type**: typing.Optional[typing.Literal['MD5up', 'SHA256up', 'SHA512up']]

### propagatedSetLevelTags
- **Type**: typing.Optional[typing.List[str]]

### s3AccessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.S3AccessConfig]


# CreateSequenceStoreResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### sseConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.SseConfig'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### fallbackLocation
- **Type**: <class 'str'>
- **Required**: Yes

### eTagAlgorithmFamily
- **Type**: typing.Literal['MD5up', 'SHA256up', 'SHA512up']
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### propagatedSetLevelTags
- **Type**: typing.List[str]
- **Required**: Yes

### s3Access
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.SequenceStoreS3Access'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVariantStoreRequest

### reference
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ReferenceItem'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### sseConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.SseConfig]


# CreateVariantStoreResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### reference
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ReferenceItem'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


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
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]

### definitionUri
- **Type**: typing.Optional[str]

### main
- **Type**: typing.Optional[str]

### parameterTemplate
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.omics.omics_classes.WorkflowParameter]]

### storageCapacity
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### accelerators
- **Type**: typing.Optional[typing.Literal['GPU']]


# CreateWorkflowResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETED', 'FAILED', 'INACTIVE', 'UPDATING']
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAnnotationStoreVersionsRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### versions
- **Type**: typing.List[str]
- **Required**: Yes

### force
- **Type**: typing.Optional[bool]


# DeleteAnnotationStoreVersionsResponse

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.VersionDeleteError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteReferenceRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### referenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReferenceStoreRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRunCacheRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRunGroupRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRunRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteS3AccessPolicyRequest

### s3AccessPointArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSequenceStoreRequest

### id
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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteWorkflowRequest

### id
- **Type**: <class 'str'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# ExportReadSet

### readSetId
- **Type**: <class 'str'>
- **Required**: Yes


# ExportReadSetDetail

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'FINISHED', 'IN_PROGRESS', 'NOT_STARTED']
- **Required**: Yes

### statusMessage
- **Type**: typing.Optional[str]


# ExportReadSetFilter

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### createdAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# ExportReadSetJobDetail

### id
- **Type**: <class 'str'>
- **Required**: Yes

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### destination
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### completionTime
- **Type**: typing.Optional[datetime.datetime]


# FileInformation

### totalParts
- **Type**: typing.Optional[int]

### partSize
- **Type**: typing.Optional[int]

### contentLength
- **Type**: typing.Optional[int]

### s3Access
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.ReadSetS3Access]


# Filter

### resourceArns
- **Type**: typing.Optional[typing.List[str]]

### status
- **Type**: typing.Optional[typing.List[typing.Literal['ACTIVATING', 'ACTIVE', 'DELETED', 'DELETING', 'FAILED', 'PENDING']]]

### type
- **Type**: typing.Optional[typing.List[typing.Literal['ANNOTATION_STORE', 'VARIANT_STORE', 'WORKFLOW']]]


# FormatOptions

### tsvOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.TsvOptions]

### vcfOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.VcfOptions]


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


# GetAnnotationImportResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### destinationName
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### completionTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.AnnotationImportItemDetail]
- **Required**: Yes

### runLeftNormalization
- **Type**: <class 'bool'>
- **Required**: Yes

### formatOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.FormatOptions'>
- **Required**: Yes

### annotationFields
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


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


# GetAnnotationStoreResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### reference
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ReferenceItem'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### storeArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### sseConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.SseConfig'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### storeOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.StoreOptionsOutput'>
- **Required**: Yes

### storeFormat
- **Type**: typing.Literal['GFF', 'TSV', 'VCF']
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### storeSizeBytes
- **Type**: <class 'int'>
- **Required**: Yes

### numVersions
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


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


# GetAnnotationStoreVersionResponse

### storeId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### versionArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### versionOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.VersionOptionsOutput'>
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### versionSizeBytes
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# GetReadSetActivationJobRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes


# GetReadSetActivationJobRequestWait

### id
- **Type**: <class 'str'>
- **Required**: Yes

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetReadSetActivationJobResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### completionTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.ActivateReadSetSourceItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# GetReadSetExportJobRequest

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetReadSetExportJobRequestWait

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetReadSetExportJobResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### destination
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### completionTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### readSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.ExportReadSetDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# GetReadSetImportJobRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes


# GetReadSetImportJobRequestWait

### id
- **Type**: <class 'str'>
- **Required**: Yes

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetReadSetImportJobResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### completionTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.ImportReadSetSourceItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# GetReadSetMetadataRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes


# GetReadSetMetadataResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### subjectId
- **Type**: <class 'str'>
- **Required**: Yes

### sampleId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVATING', 'ACTIVE', 'ARCHIVED', 'DELETED', 'DELETING', 'PROCESSING_UPLOAD', 'UPLOAD_FAILED']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### fileType
- **Type**: typing.Literal['BAM', 'CRAM', 'FASTQ', 'UBAM']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### sequenceInformation
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.SequenceInformation'>
- **Required**: Yes

### referenceArn
- **Type**: <class 'str'>
- **Required**: Yes

### files
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ReadSetFiles'>
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### creationType
- **Type**: typing.Literal['IMPORT', 'UPLOAD']
- **Required**: Yes

### etag
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ETag'>
- **Required**: Yes

### creationJobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# GetReadSetRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### partNumber
- **Type**: <class 'int'>
- **Required**: Yes

### file
- **Type**: typing.Optional[typing.Literal['INDEX', 'SOURCE1', 'SOURCE2']]


# GetReadSetResponse

### payload
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# GetReferenceImportJobRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### referenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes


# GetReferenceImportJobRequestWait

### id
- **Type**: <class 'str'>
- **Required**: Yes

### referenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetReferenceImportJobResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### referenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### completionTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.ImportReferenceSourceItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# GetReferenceMetadataRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### referenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes


# GetReferenceMetadataResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### referenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### md5
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'DELETING']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### files
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ReferenceFiles'>
- **Required**: Yes

### creationType
- **Type**: typing.Literal['IMPORT']
- **Required**: Yes

### creationJobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# GetReferenceRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### referenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### partNumber
- **Type**: <class 'int'>
- **Required**: Yes

### range
- **Type**: typing.Optional[str]

### file
- **Type**: typing.Optional[typing.Literal['INDEX', 'SOURCE']]


# GetReferenceResponse

### payload
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# GetReferenceStoreRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetReferenceStoreResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### sseConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.SseConfig'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# GetRunCacheRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetRunCacheResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### cacheBehavior
- **Type**: typing.Literal['CACHE_ALWAYS', 'CACHE_ON_FAILURE']
- **Required**: Yes

### cacheBucketOwnerId
- **Type**: <class 'str'>
- **Required**: Yes

### cacheS3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'FAILED']
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# GetRunGroupRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetRunGroupResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### maxCpus
- **Type**: <class 'int'>
- **Required**: Yes

### maxRuns
- **Type**: <class 'int'>
- **Required**: Yes

### maxDuration
- **Type**: <class 'int'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### maxGpus
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# GetRunRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### export
- **Type**: typing.Optional[typing.List[typing.Literal['DEFINITION']]]


# GetRunRequestWait

### id
- **Type**: <class 'str'>
- **Required**: Yes

### export
- **Type**: typing.Optional[typing.List[typing.Literal['DEFINITION']]]

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetRunRequestWaitExtra

### id
- **Type**: <class 'str'>
- **Required**: Yes

### export
- **Type**: typing.Optional[typing.List[typing.Literal['DEFINITION']]]

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetRunResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### cacheId
- **Type**: <class 'str'>
- **Required**: Yes

### cacheBehavior
- **Type**: typing.Literal['CACHE_ALWAYS', 'CACHE_ON_FAILURE']
- **Required**: Yes

### engineVersion
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'DELETED', 'FAILED', 'PENDING', 'RUNNING', 'STARTING', 'STOPPING']
- **Required**: Yes

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### workflowType
- **Type**: typing.Literal['PRIVATE', 'READY2RUN']
- **Required**: Yes

### runId
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### runGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### priority
- **Type**: <class 'int'>
- **Required**: Yes

### definition
- **Type**: <class 'str'>
- **Required**: Yes

### digest
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### storageCapacity
- **Type**: <class 'int'>
- **Required**: Yes

### outputUri
- **Type**: <class 'str'>
- **Required**: Yes

### logLevel
- **Type**: typing.Literal['ALL', 'ERROR', 'FATAL', 'OFF']
- **Required**: Yes

### resourceDigests
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### startedBy
- **Type**: <class 'str'>
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

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### accelerators
- **Type**: typing.Literal['GPU']
- **Required**: Yes

### retentionMode
- **Type**: typing.Literal['REMOVE', 'RETAIN']
- **Required**: Yes

### failureReason
- **Type**: <class 'str'>
- **Required**: Yes

### logLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.RunLogLocation'>
- **Required**: Yes

### uuid
- **Type**: <class 'str'>
- **Required**: Yes

### runOutputUri
- **Type**: <class 'str'>
- **Required**: Yes

### storageType
- **Type**: typing.Literal['DYNAMIC', 'STATIC']
- **Required**: Yes

### workflowOwnerId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# GetRunTaskRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRunTaskRequestWait

### id
- **Type**: <class 'str'>
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetRunTaskRequestWaitExtra

### id
- **Type**: <class 'str'>
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# GetSequenceStoreRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetSequenceStoreResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### sseConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.SseConfig'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### fallbackLocation
- **Type**: <class 'str'>
- **Required**: Yes

### s3Access
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.SequenceStoreS3Access'>
- **Required**: Yes

### eTagAlgorithmFamily
- **Type**: typing.Literal['MD5up', 'SHA256up', 'SHA512up']
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### propagatedSetLevelTags
- **Type**: typing.List[str]
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# GetShareRequest

### shareId
- **Type**: <class 'str'>
- **Required**: Yes


# GetShareResponse

### share
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ShareDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
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


# GetVariantImportResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### destinationName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### completionTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.VariantImportItemDetail]
- **Required**: Yes

### runLeftNormalization
- **Type**: <class 'bool'>
- **Required**: Yes

### annotationFields
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


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


# GetVariantStoreResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### reference
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ReferenceItem'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### storeArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### sseConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.SseConfig'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### storeSizeBytes
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# GetWorkflowRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'READY2RUN']]

### export
- **Type**: typing.Optional[typing.List[typing.Literal['DEFINITION']]]

### workflowOwnerId
- **Type**: typing.Optional[str]


# GetWorkflowRequestWait

### id
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'READY2RUN']]

### export
- **Type**: typing.Optional[typing.List[typing.Literal['DEFINITION']]]

### workflowOwnerId
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetWorkflowResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETED', 'FAILED', 'INACTIVE', 'UPDATING']
- **Required**: Yes

### type
- **Type**: typing.Literal['PRIVATE', 'READY2RUN']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### engine
- **Type**: typing.Literal['CWL', 'NEXTFLOW', 'WDL']
- **Required**: Yes

### definition
- **Type**: <class 'str'>
- **Required**: Yes

### main
- **Type**: <class 'str'>
- **Required**: Yes

### digest
- **Type**: <class 'str'>
- **Required**: Yes

### parameterTemplate
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.omics.omics_classes.WorkflowParameter]
- **Required**: Yes

### storageCapacity
- **Type**: <class 'int'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### metadata
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### accelerators
- **Type**: typing.Literal['GPU']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# ImportReadSetFilter

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### createdAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# ImportReadSetJobItem

### id
- **Type**: <class 'str'>
- **Required**: Yes

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### completionTime
- **Type**: typing.Optional[datetime.datetime]


# ImportReadSetSourceItem

### sourceFiles
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.SourceFiles'>
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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# ImportReferenceJobItem

### id
- **Type**: <class 'str'>
- **Required**: Yes

### referenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### completionTime
- **Type**: typing.Optional[datetime.datetime]


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


# ListAnnotationImportJobsRequest

### maxResults
- **Type**: typing.Optional[int]

### ids
- **Type**: typing.Optional[typing.List[str]]

### nextToken
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.ListAnnotationImportJobsFilter]


# ListAnnotationImportJobsRequestPaginate

### ids
- **Type**: typing.Optional[typing.List[str]]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.ListAnnotationImportJobsFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.PaginatorConfig]


# ListAnnotationImportJobsResponse

### annotationImportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.AnnotationImportJobItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAnnotationStoreVersionsFilter

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]


# ListAnnotationStoreVersionsRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.ListAnnotationStoreVersionsFilter]


# ListAnnotationStoreVersionsRequestPaginate

### name
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.ListAnnotationStoreVersionsFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.PaginatorConfig]


# ListAnnotationStoreVersionsResponse

### annotationStoreVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.AnnotationStoreVersionItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAnnotationStoresFilter

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]


# ListAnnotationStoresRequest

### ids
- **Type**: typing.Optional[typing.List[str]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.ListAnnotationStoresFilter]


# ListAnnotationStoresRequestPaginate

### ids
- **Type**: typing.Optional[typing.List[str]]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.ListAnnotationStoresFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.PaginatorConfig]


# ListAnnotationStoresResponse

### annotationStores
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.AnnotationStoreItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.PaginatorConfig]


# ListMultipartReadSetUploadsResponse

### uploads
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.MultipartReadSetUploadListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReadSetActivationJobsRequest

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.ActivateReadSetFilter]


# ListReadSetActivationJobsRequestPaginate

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.ActivateReadSetFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.PaginatorConfig]


# ListReadSetActivationJobsResponse

### activationJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.ActivateReadSetJobItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReadSetExportJobsRequest

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.ExportReadSetFilter]


# ListReadSetExportJobsRequestPaginate

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.ExportReadSetFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.PaginatorConfig]


# ListReadSetExportJobsResponse

### exportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.ExportReadSetJobDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReadSetImportJobsRequest

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.ImportReadSetFilter]


# ListReadSetImportJobsRequestPaginate

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.ImportReadSetFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.PaginatorConfig]


# ListReadSetImportJobsResponse

### importJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.ImportReadSetJobItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReadSetUploadPartsRequest

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes

### partSource
- **Type**: typing.Literal['SOURCE1', 'SOURCE2']
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.ReadSetUploadPartListFilter]


# ListReadSetUploadPartsRequestPaginate

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes

### partSource
- **Type**: typing.Literal['SOURCE1', 'SOURCE2']
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.ReadSetUploadPartListFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.PaginatorConfig]


# ListReadSetUploadPartsResponse

### parts
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.ReadSetUploadPartListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReadSetsRequest

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.ReadSetFilter]


# ListReadSetsRequestPaginate

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.ReadSetFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.PaginatorConfig]


# ListReadSetsResponse

### readSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.ReadSetListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReferenceImportJobsRequest

### referenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.ImportReferenceFilter]


# ListReferenceImportJobsRequestPaginate

### referenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.ImportReferenceFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.PaginatorConfig]


# ListReferenceImportJobsResponse

### importJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.ImportReferenceJobItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReferenceStoresRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.ReferenceStoreFilter]


# ListReferenceStoresRequestPaginate

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.ReferenceStoreFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.PaginatorConfig]


# ListReferenceStoresResponse

### referenceStores
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.ReferenceStoreDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReferencesRequest

### referenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.ReferenceFilter]


# ListReferencesRequestPaginate

### referenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.ReferenceFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.PaginatorConfig]


# ListReferencesResponse

### references
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.ReferenceListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.PaginatorConfig]


# ListRunCachesResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.RunCacheListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.PaginatorConfig]


# ListRunGroupsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.RunGroupListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRunTasksRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'PENDING', 'RUNNING', 'STARTING', 'STOPPING']]

### startingToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListRunTasksRequestPaginate

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'PENDING', 'RUNNING', 'STARTING', 'STOPPING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.PaginatorConfig]


# ListRunTasksResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.TaskListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.PaginatorConfig]


# ListRunsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.RunListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSequenceStoresRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.SequenceStoreFilter]


# ListSequenceStoresRequestPaginate

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.SequenceStoreFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.PaginatorConfig]


# ListSequenceStoresResponse

### sequenceStores
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.SequenceStoreDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSharesRequest

### resourceOwner
- **Type**: typing.Literal['OTHER', 'SELF']
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.Filter]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListSharesRequestPaginate

### resourceOwner
- **Type**: typing.Literal['OTHER', 'SELF']
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.Filter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.PaginatorConfig]


# ListSharesResponse

### shares
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.ShareDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# ListVariantImportJobsFilter

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### storeName
- **Type**: typing.Optional[str]


# ListVariantImportJobsRequest

### maxResults
- **Type**: typing.Optional[int]

### ids
- **Type**: typing.Optional[typing.List[str]]

### nextToken
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.ListVariantImportJobsFilter]


# ListVariantImportJobsRequestPaginate

### ids
- **Type**: typing.Optional[typing.List[str]]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.ListVariantImportJobsFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.PaginatorConfig]


# ListVariantImportJobsResponse

### variantImportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.VariantImportJobItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListVariantStoresFilter

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]


# ListVariantStoresRequest

### maxResults
- **Type**: typing.Optional[int]

### ids
- **Type**: typing.Optional[typing.List[str]]

### nextToken
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.ListVariantStoresFilter]


# ListVariantStoresRequestPaginate

### ids
- **Type**: typing.Optional[typing.List[str]]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.ListVariantStoresFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.PaginatorConfig]


# ListVariantStoresResponse

### variantStores
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.VariantStoreItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkflowsRequest

### type
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'READY2RUN']]

### name
- **Type**: typing.Optional[str]

### startingToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListWorkflowsRequestPaginate

### type
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'READY2RUN']]

### name
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.PaginatorConfig]


# ListWorkflowsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.WorkflowListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
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

### id
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# ReadSetFiles

### source1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.FileInformation]

### source2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.FileInformation]

### index
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.FileInformation]


# ReadSetFilter

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVATING', 'ACTIVE', 'ARCHIVED', 'DELETED', 'DELETING', 'PROCESSING_UPLOAD', 'UPLOAD_FAILED']]

### referenceArn
- **Type**: typing.Optional[str]

### createdAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### sampleId
- **Type**: typing.Optional[str]

### subjectId
- **Type**: typing.Optional[str]

### generatedFrom
- **Type**: typing.Optional[str]

### creationType
- **Type**: typing.Optional[typing.Literal['IMPORT', 'UPLOAD']]


# ReadSetListItem

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVATING', 'ACTIVE', 'ARCHIVED', 'DELETED', 'DELETING', 'PROCESSING_UPLOAD', 'UPLOAD_FAILED']
- **Required**: Yes

### fileType
- **Type**: typing.Literal['BAM', 'CRAM', 'FASTQ', 'UBAM']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### subjectId
- **Type**: typing.Optional[str]

### sampleId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### referenceArn
- **Type**: typing.Optional[str]

### sequenceInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.SequenceInformation]

### statusMessage
- **Type**: typing.Optional[str]

### creationType
- **Type**: typing.Optional[typing.Literal['IMPORT', 'UPLOAD']]

### etag
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.ETag]


# ReadSetS3Access

### s3Uri
- **Type**: typing.Optional[str]


# ReadSetUploadPartListFilter

### createdAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.FileInformation]

### index
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.FileInformation]


# ReferenceFilter

### name
- **Type**: typing.Optional[str]

### md5
- **Type**: typing.Optional[str]

### createdAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# ReferenceItem

### referenceArn
- **Type**: typing.Optional[str]


# ReferenceListItem

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### referenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### md5
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED', 'DELETING']]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# ReferenceStoreDetail

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### sseConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.SseConfig]


# ReferenceStoreFilter

### name
- **Type**: typing.Optional[str]

### createdAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]


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

### arn
- **Type**: typing.Optional[str]

### cacheBehavior
- **Type**: typing.Optional[typing.Literal['CACHE_ALWAYS', 'CACHE_ON_FAILURE']]

### cacheS3Uri
- **Type**: typing.Optional[str]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED', 'FAILED']]


# RunGroupListItem

### arn
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### maxCpus
- **Type**: typing.Optional[int]

### maxRuns
- **Type**: typing.Optional[int]

### maxDuration
- **Type**: typing.Optional[int]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### maxGpus
- **Type**: typing.Optional[int]


# RunListItem

### arn
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'DELETED', 'FAILED', 'PENDING', 'RUNNING', 'STARTING', 'STOPPING']]

### workflowId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### priority
- **Type**: typing.Optional[int]

### storageCapacity
- **Type**: typing.Optional[int]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### stopTime
- **Type**: typing.Optional[datetime.datetime]

### storageType
- **Type**: typing.Optional[typing.Literal['DYNAMIC', 'STATIC']]


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

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### sseConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.SseConfig]

### fallbackLocation
- **Type**: typing.Optional[str]

### eTagAlgorithmFamily
- **Type**: typing.Optional[typing.Literal['MD5up', 'SHA256up', 'SHA512up']]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]

### statusMessage
- **Type**: typing.Optional[str]

### updateTime
- **Type**: typing.Optional[datetime.datetime]


# SequenceStoreFilter

### name
- **Type**: typing.Optional[str]

### createdAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]

### updatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### updatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]


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

### type
- **Type**: typing.Literal['KMS']
- **Required**: Yes

### keyArn
- **Type**: typing.Optional[str]


# StartAnnotationImportRequest

### destinationName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.AnnotationImportItemSource]
- **Required**: Yes

### versionName
- **Type**: typing.Optional[str]

### formatOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.FormatOptions]

### runLeftNormalization
- **Type**: typing.Optional[bool]

### annotationFields
- **Type**: typing.Optional[typing.Dict[str, str]]


# StartAnnotationImportResponse

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# StartReadSetActivationJobRequest

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.StartReadSetActivationJobSourceItem]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# StartReadSetActivationJobResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


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
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.ExportReadSet]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# StartReadSetExportJobResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### destination
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# StartReadSetImportJobRequest

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.StartReadSetImportJobSourceItem]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# StartReadSetImportJobResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# StartReadSetImportJobSourceItem

### sourceFiles
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.SourceFiles'>
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
- **Type**: typing.Optional[typing.Dict[str, str]]


# StartReferenceImportJobRequest

### referenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.StartReferenceImportJobSourceItem]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# StartReferenceImportJobResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### referenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


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
- **Type**: typing.Optional[typing.Dict[str, str]]


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
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### storageCapacity
- **Type**: typing.Optional[int]

### outputUri
- **Type**: typing.Optional[str]

### logLevel
- **Type**: typing.Optional[typing.Literal['ALL', 'ERROR', 'FATAL', 'OFF']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### retentionMode
- **Type**: typing.Optional[typing.Literal['REMOVE', 'RETAIN']]

### storageType
- **Type**: typing.Optional[typing.Literal['DYNAMIC', 'STATIC']]

### workflowOwnerId
- **Type**: typing.Optional[str]


# StartRunResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'DELETED', 'FAILED', 'PENDING', 'RUNNING', 'STARTING', 'STOPPING']
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### uuid
- **Type**: <class 'str'>
- **Required**: Yes

### runOutputUri
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# StartVariantImportRequest

### destinationName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics.omics_classes.VariantImportItemSource]
- **Required**: Yes

### runLeftNormalization
- **Type**: typing.Optional[bool]

### annotationFields
- **Type**: typing.Optional[typing.Dict[str, str]]


# StartVariantImportResponse

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# StoreOptions

### tsvStoreOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.TsvStoreOptions]


# StoreOptionsOutput

### tsvStoreOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.TsvStoreOptionsOutput]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
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


# TsvOptions

### readOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.ReadOptions]


# TsvStoreOptions

### annotationType
- **Type**: typing.Optional[typing.Literal['CHR_POS', 'CHR_POS_REF_ALT', 'CHR_START_END_ONE_BASE', 'CHR_START_END_REF_ALT_ONE_BASE', 'CHR_START_END_REF_ALT_ZERO_BASE', 'CHR_START_END_ZERO_BASE', 'GENERIC']]

### formatToHeader
- **Type**: typing.Optional[typing.Dict[typing.Literal['ALT', 'CHR', 'END', 'POS', 'REF', 'START'], str]]

### schema
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Literal['BOOLEAN', 'DOUBLE', 'FLOAT', 'INT', 'LONG', 'STRING']]]]


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
- **Type**: typing.Optional[typing.Dict[typing.Literal['ALT', 'CHR', 'END', 'POS', 'REF', 'START'], str]]

### schema
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Literal['BOOLEAN', 'DOUBLE', 'FLOAT', 'INT', 'LONG', 'STRING']]]]


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
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAnnotationStoreRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateAnnotationStoreResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### reference
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ReferenceItem'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### storeOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.StoreOptionsOutput'>
- **Required**: Yes

### storeFormat
- **Type**: typing.Literal['GFF', 'TSV', 'VCF']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAnnotationStoreVersionRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateAnnotationStoreVersionResponse

### storeId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRunCacheRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### cacheBehavior
- **Type**: typing.Optional[typing.Literal['CACHE_ALWAYS', 'CACHE_ON_FAILURE']]

### description
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# UpdateRunGroupRequest

### id
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

### maxGpus
- **Type**: typing.Optional[int]


# UpdateSequenceStoreRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### fallbackLocation
- **Type**: typing.Optional[str]

### propagatedSetLevelTags
- **Type**: typing.Optional[typing.List[str]]

### s3AccessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.S3AccessConfig]


# UpdateSequenceStoreResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### sseConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.SseConfig'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### propagatedSetLevelTags
- **Type**: typing.List[str]
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### fallbackLocation
- **Type**: <class 'str'>
- **Required**: Yes

### s3Access
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.SequenceStoreS3Access'>
- **Required**: Yes

### eTagAlgorithmFamily
- **Type**: typing.Literal['MD5up', 'SHA256up', 'SHA512up']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateVariantStoreRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateVariantStoreResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### reference
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ReferenceItem'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateWorkflowRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

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
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes


# UploadReadSetPartResponse

### checksum
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ResponseMetadata'>
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

### id
- **Type**: <class 'str'>
- **Required**: Yes

### destinationName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### completionTime
- **Type**: typing.Optional[datetime.datetime]

### runLeftNormalization
- **Type**: typing.Optional[bool]

### annotationFields
- **Type**: typing.Optional[typing.Dict[str, str]]


# VariantStoreItem

### id
- **Type**: <class 'str'>
- **Required**: Yes

### reference
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.ReferenceItem'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### storeArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### sseConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.omics.omics_classes.SseConfig'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### storeSizeBytes
- **Type**: <class 'int'>
- **Required**: Yes


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.TsvVersionOptions]


# VersionOptionsOutput

### tsvVersionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics.omics_classes.TsvVersionOptionsOutput]


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


# WorkflowListItem

### arn
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETED', 'FAILED', 'INACTIVE', 'UPDATING']]

### type
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'READY2RUN']]

### digest
- **Type**: typing.Optional[str]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### metadata
- **Type**: typing.Optional[typing.Dict[str, str]]


# WorkflowParameter

### description
- **Type**: typing.Optional[str]

### optional
- **Type**: typing.Optional[bool]


