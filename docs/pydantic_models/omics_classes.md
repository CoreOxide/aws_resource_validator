# omics_classes

# AbortMultipartReadSetUploadRequestRequestTypeDef

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes


# AcceptShareRequestRequestTypeDef

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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# ActivateReadSetJobItemTypeDef

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


# AnnotationStoreItemTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### reference
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ReferenceItemTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.SseConfigTypeDef'>
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


# AnnotationStoreVersionItemTypeDef

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

# BatchDeleteReadSetRequestRequestTypeDef

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


# CancelAnnotationImportRequestRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelRunRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# CancelVariantImportRequestRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# CompleteMultipartReadSetUploadRequestRequestTypeDef

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


# CreateAnnotationStoreRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.StoreOptionsTypeDef]


# CreateAnnotationStoreResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### reference
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ReferenceItemTypeDef'>
- **Required**: Yes

### storeFormat
- **Type**: typing.Literal['GFF', 'TSV', 'VCF']
- **Required**: Yes

### storeOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.StoreOptionsOutputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAnnotationStoreVersionRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### versionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.VersionOptionsTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateAnnotationStoreVersionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.VersionOptionsOutputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMultipartReadSetUploadRequestRequestTypeDef

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


# CreateReferenceStoreRequestRequestTypeDef

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


# CreateReferenceStoreResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.SseConfigTypeDef'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRunGroupRequestRequestTypeDef

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


# CreateRunGroupResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSequenceStoreRequestRequestTypeDef

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


# CreateSequenceStoreResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.SseConfigTypeDef'>
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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateShareRequestRequestTypeDef

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


# CreateVariantStoreRequestRequestTypeDef

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


# CreateVariantStoreResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### reference
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ReferenceItemTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWorkflowRequestRequestTypeDef

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
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]

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


# CreateWorkflowResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAnnotationStoreRequestRequestTypeDef

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


# DeleteAnnotationStoreVersionsRequestRequestTypeDef

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


# DeleteReferenceRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### referenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReferenceStoreRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRunGroupRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRunRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSequenceStoreRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteShareRequestRequestTypeDef

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


# DeleteVariantStoreRequestRequestTypeDef

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


# DeleteWorkflowRequestRequestTypeDef

### id
- **Type**: <class 'str'>
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


# ExportReadSetDetailTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'FINISHED', 'IN_PROGRESS', 'NOT_STARTED']
- **Required**: Yes

### statusMessage
- **Type**: typing.Optional[str]


# ExportReadSetFilterTypeDef

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### createdAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# ExportReadSetJobDetailTypeDef

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


# FilterTypeDef

### resourceArns
- **Type**: typing.Optional[typing.Sequence[str]]

### status
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ACTIVATING', 'ACTIVE', 'DELETED', 'DELETING', 'FAILED', 'PENDING']]]

### type
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ANNOTATION_STORE', 'VARIANT_STORE', 'WORKFLOW']]]


# FormatOptionsTypeDef

### tsvOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.TsvOptionsTypeDef]

### vcfOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.VcfOptionsTypeDef]


# GetAnnotationImportRequestAnnotationImportJobCreatedWaitTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.WaiterConfigTypeDef]


# GetAnnotationImportRequestRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAnnotationImportResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.AnnotationImportItemDetailTypeDef]
- **Required**: Yes

### runLeftNormalization
- **Type**: <class 'bool'>
- **Required**: Yes

### formatOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.FormatOptionsTypeDef'>
- **Required**: Yes

### annotationFields
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAnnotationStoreRequestAnnotationStoreCreatedWaitTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.WaiterConfigTypeDef]


# GetAnnotationStoreRequestAnnotationStoreDeletedWaitTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.WaiterConfigTypeDef]


# GetAnnotationStoreRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetAnnotationStoreResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### reference
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ReferenceItemTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.SseConfigTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.StoreOptionsOutputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAnnotationStoreVersionRequestAnnotationStoreVersionCreatedWaitTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.WaiterConfigTypeDef]


# GetAnnotationStoreVersionRequestAnnotationStoreVersionDeletedWaitTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.WaiterConfigTypeDef]


# GetAnnotationStoreVersionRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes


# GetAnnotationStoreVersionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.VersionOptionsOutputTypeDef'>
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### versionSizeBytes
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetReadSetActivationJobRequestReadSetActivationJobCompletedWaitTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.WaiterConfigTypeDef]


# GetReadSetActivationJobRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes


# GetReadSetActivationJobResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.ActivateReadSetSourceItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetReadSetExportJobRequestReadSetExportJobCompletedWaitTypeDef

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.WaiterConfigTypeDef]


# GetReadSetExportJobRequestRequestTypeDef

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetReadSetExportJobResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.ExportReadSetDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetReadSetImportJobRequestReadSetImportJobCompletedWaitTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.WaiterConfigTypeDef]


# GetReadSetImportJobRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes


# GetReadSetImportJobResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.ImportReadSetSourceItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetReadSetMetadataRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes


# GetReadSetMetadataResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.SequenceInformationTypeDef'>
- **Required**: Yes

### referenceArn
- **Type**: <class 'str'>
- **Required**: Yes

### files
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ReadSetFilesTypeDef'>
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### creationType
- **Type**: typing.Literal['IMPORT', 'UPLOAD']
- **Required**: Yes

### etag
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ETagTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetReadSetRequestRequestTypeDef

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


# GetReadSetResponseTypeDef

### payload
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetReferenceImportJobRequestReferenceImportJobCompletedWaitTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### referenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.WaiterConfigTypeDef]


# GetReferenceImportJobRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### referenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes


# GetReferenceImportJobResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.ImportReferenceSourceItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetReferenceMetadataRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### referenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes


# GetReferenceMetadataResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ReferenceFilesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetReferenceRequestRequestTypeDef

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


# GetReferenceResponseTypeDef

### payload
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetReferenceStoreRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetReferenceStoreResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.SseConfigTypeDef'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRunGroupRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetRunGroupResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRunRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### export
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DEFINITION']]]


# GetRunRequestRunCompletedWaitTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### export
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DEFINITION']]]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.WaiterConfigTypeDef]


# GetRunRequestRunRunningWaitTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### export
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DEFINITION']]]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.WaiterConfigTypeDef]


# GetRunResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.RunLogLocationTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRunTaskRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRunTaskRequestTaskCompletedWaitTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.WaiterConfigTypeDef]


# GetRunTaskRequestTaskRunningWaitTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.WaiterConfigTypeDef]


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


# GetSequenceStoreRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetSequenceStoreResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.SseConfigTypeDef'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### fallbackLocation
- **Type**: <class 'str'>
- **Required**: Yes

### s3Access
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.SequenceStoreS3AccessTypeDef'>
- **Required**: Yes

### eTagAlgorithmFamily
- **Type**: typing.Literal['MD5up', 'SHA256up', 'SHA512up']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetShareRequestRequestTypeDef

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


# GetVariantImportRequestRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVariantImportRequestVariantImportJobCreatedWaitTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.WaiterConfigTypeDef]


# GetVariantImportResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.VariantImportItemDetailTypeDef]
- **Required**: Yes

### runLeftNormalization
- **Type**: <class 'bool'>
- **Required**: Yes

### annotationFields
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVariantStoreRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetVariantStoreRequestVariantStoreCreatedWaitTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.WaiterConfigTypeDef]


# GetVariantStoreRequestVariantStoreDeletedWaitTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.WaiterConfigTypeDef]


# GetVariantStoreResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### reference
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ReferenceItemTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.SseConfigTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWorkflowRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'READY2RUN']]

### export
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DEFINITION']]]

### workflowOwnerId
- **Type**: typing.Optional[str]


# GetWorkflowRequestWorkflowActiveWaitTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'READY2RUN']]

### export
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DEFINITION']]]

### workflowOwnerId
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.WaiterConfigTypeDef]


# GetWorkflowResponseTypeDef

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.omics_classes.WorkflowParameterTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImportReadSetFilterTypeDef

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### createdAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# ImportReadSetJobItemTypeDef

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


# ImportReferenceFilterTypeDef

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### createdAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# ImportReferenceJobItemTypeDef

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


# ListAnnotationImportJobsFilterTypeDef

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### storeName
- **Type**: typing.Optional[str]


# ListAnnotationImportJobsRequestListAnnotationImportJobsPaginateTypeDef

### ids
- **Type**: typing.Optional[typing.Sequence[str]]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.ListAnnotationImportJobsFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.PaginatorConfigTypeDef]


# ListAnnotationImportJobsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### ids
- **Type**: typing.Optional[typing.Sequence[str]]

### nextToken
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.ListAnnotationImportJobsFilterTypeDef]


# ListAnnotationImportJobsResponseTypeDef

### annotationImportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.AnnotationImportJobItemTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAnnotationStoreVersionsFilterTypeDef

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]


# ListAnnotationStoreVersionsRequestListAnnotationStoreVersionsPaginateTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.ListAnnotationStoreVersionsFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.PaginatorConfigTypeDef]


# ListAnnotationStoreVersionsRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.ListAnnotationStoreVersionsFilterTypeDef]


# ListAnnotationStoreVersionsResponseTypeDef

### annotationStoreVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.AnnotationStoreVersionItemTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAnnotationStoresFilterTypeDef

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]


# ListAnnotationStoresRequestListAnnotationStoresPaginateTypeDef

### ids
- **Type**: typing.Optional[typing.Sequence[str]]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.ListAnnotationStoresFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.PaginatorConfigTypeDef]


# ListAnnotationStoresRequestRequestTypeDef

### ids
- **Type**: typing.Optional[typing.Sequence[str]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.ListAnnotationStoresFilterTypeDef]


# ListAnnotationStoresResponseTypeDef

### annotationStores
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.AnnotationStoreItemTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMultipartReadSetUploadsRequestListMultipartReadSetUploadsPaginateTypeDef

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.PaginatorConfigTypeDef]


# ListMultipartReadSetUploadsRequestRequestTypeDef

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListMultipartReadSetUploadsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### uploads
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.MultipartReadSetUploadListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListReadSetActivationJobsRequestListReadSetActivationJobsPaginateTypeDef

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.ActivateReadSetFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.PaginatorConfigTypeDef]


# ListReadSetActivationJobsRequestRequestTypeDef

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.ActivateReadSetFilterTypeDef]


# ListReadSetActivationJobsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### activationJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.ActivateReadSetJobItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListReadSetExportJobsRequestListReadSetExportJobsPaginateTypeDef

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.ExportReadSetFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.PaginatorConfigTypeDef]


# ListReadSetExportJobsRequestRequestTypeDef

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.ExportReadSetFilterTypeDef]


# ListReadSetExportJobsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### exportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.ExportReadSetJobDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListReadSetImportJobsRequestListReadSetImportJobsPaginateTypeDef

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.ImportReadSetFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.PaginatorConfigTypeDef]


# ListReadSetImportJobsRequestRequestTypeDef

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.ImportReadSetFilterTypeDef]


# ListReadSetImportJobsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### importJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.ImportReadSetJobItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListReadSetUploadPartsRequestListReadSetUploadPartsPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.ReadSetUploadPartListFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.PaginatorConfigTypeDef]


# ListReadSetUploadPartsRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.ReadSetUploadPartListFilterTypeDef]


# ListReadSetUploadPartsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### parts
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.ReadSetUploadPartListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListReadSetsRequestListReadSetsPaginateTypeDef

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.ReadSetFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.PaginatorConfigTypeDef]


# ListReadSetsRequestRequestTypeDef

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.ReadSetFilterTypeDef]


# ListReadSetsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### readSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.ReadSetListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListReferenceImportJobsRequestListReferenceImportJobsPaginateTypeDef

### referenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.ImportReferenceFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.PaginatorConfigTypeDef]


# ListReferenceImportJobsRequestRequestTypeDef

### referenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.ImportReferenceFilterTypeDef]


# ListReferenceImportJobsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### importJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.ImportReferenceJobItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListReferenceStoresRequestListReferenceStoresPaginateTypeDef

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.ReferenceStoreFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.PaginatorConfigTypeDef]


# ListReferenceStoresRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.ReferenceStoreFilterTypeDef]


# ListReferenceStoresResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### referenceStores
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.ReferenceStoreDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListReferencesRequestListReferencesPaginateTypeDef

### referenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.ReferenceFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.PaginatorConfigTypeDef]


# ListReferencesRequestRequestTypeDef

### referenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.ReferenceFilterTypeDef]


# ListReferencesResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### references
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.ReferenceListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRunGroupsRequestListRunGroupsPaginateTypeDef

### name
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.PaginatorConfigTypeDef]


# ListRunGroupsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRunTasksRequestListRunTasksPaginateTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'PENDING', 'RUNNING', 'STARTING', 'STOPPING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.PaginatorConfigTypeDef]


# ListRunTasksRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'PENDING', 'RUNNING', 'STARTING', 'STOPPING']]

### startingToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListRunTasksResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.TaskListItemTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRunsRequestListRunsPaginateTypeDef

### name
- **Type**: typing.Optional[str]

### runGroupId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'DELETED', 'FAILED', 'PENDING', 'RUNNING', 'STARTING', 'STOPPING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.PaginatorConfigTypeDef]


# ListRunsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSequenceStoresRequestListSequenceStoresPaginateTypeDef

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.SequenceStoreFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.PaginatorConfigTypeDef]


# ListSequenceStoresRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.SequenceStoreFilterTypeDef]


# ListSequenceStoresResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### sequenceStores
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.SequenceStoreDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSharesRequestListSharesPaginateTypeDef

### resourceOwner
- **Type**: typing.Literal['OTHER', 'SELF']
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.FilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.PaginatorConfigTypeDef]


# ListSharesRequestRequestTypeDef

### resourceOwner
- **Type**: typing.Literal['OTHER', 'SELF']
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.FilterTypeDef]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListSharesResponseTypeDef

### shares
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.ShareDetailsTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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


# ListVariantImportJobsRequestListVariantImportJobsPaginateTypeDef

### ids
- **Type**: typing.Optional[typing.Sequence[str]]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.ListVariantImportJobsFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.PaginatorConfigTypeDef]


# ListVariantImportJobsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### ids
- **Type**: typing.Optional[typing.Sequence[str]]

### nextToken
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.ListVariantImportJobsFilterTypeDef]


# ListVariantImportJobsResponseTypeDef

### variantImportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.VariantImportJobItemTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVariantStoresFilterTypeDef

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]


# ListVariantStoresRequestListVariantStoresPaginateTypeDef

### ids
- **Type**: typing.Optional[typing.Sequence[str]]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.ListVariantStoresFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.PaginatorConfigTypeDef]


# ListVariantStoresRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### ids
- **Type**: typing.Optional[typing.Sequence[str]]

### nextToken
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.ListVariantStoresFilterTypeDef]


# ListVariantStoresResponseTypeDef

### variantStores
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.VariantStoreItemTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWorkflowsRequestListWorkflowsPaginateTypeDef

### type
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'READY2RUN']]

### name
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.PaginatorConfigTypeDef]


# ListWorkflowsRequestRequestTypeDef

### type
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'READY2RUN']]

### name
- **Type**: typing.Optional[str]

### startingToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListWorkflowsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.omics_classes.WorkflowListItemTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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

### id
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


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


# ReadSetListItemTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.SequenceInformationTypeDef]

### statusMessage
- **Type**: typing.Optional[str]

### creationType
- **Type**: typing.Optional[typing.Literal['IMPORT', 'UPLOAD']]

### etag
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.ETagTypeDef]


# ReadSetS3AccessTypeDef

### s3Uri
- **Type**: typing.Optional[str]


# ReadSetUploadPartListFilterTypeDef

### createdAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]


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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# ReferenceItemTypeDef

### referenceArn
- **Type**: typing.Optional[str]


# ReferenceListItemTypeDef

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


# ReferenceStoreDetailTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.SseConfigTypeDef]


# ReferenceStoreFilterTypeDef

### name
- **Type**: typing.Optional[str]

### createdAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]


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


# RunGroupListItemTypeDef

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


# RunListItemTypeDef

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


# RunLogLocationTypeDef

### engineLogStream
- **Type**: typing.Optional[str]

### runLogStream
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.omics_classes.SseConfigTypeDef]

### fallbackLocation
- **Type**: typing.Optional[str]

### eTagAlgorithmFamily
- **Type**: typing.Optional[typing.Literal['MD5up', 'SHA256up', 'SHA512up']]


# SequenceStoreFilterTypeDef

### name
- **Type**: typing.Optional[str]

### createdAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# SequenceStoreS3AccessTypeDef

### s3Uri
- **Type**: typing.Optional[str]

### s3AccessPointArn
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

### type
- **Type**: typing.Literal['KMS']
- **Required**: Yes

### keyArn
- **Type**: typing.Optional[str]


# StartAnnotationImportRequestRequestTypeDef

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


# StartReadSetActivationJobRequestRequestTypeDef

### sequenceStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.omics_classes.StartReadSetActivationJobSourceItemTypeDef]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# StartReadSetActivationJobResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartReadSetActivationJobSourceItemTypeDef

### readSetId
- **Type**: <class 'str'>
- **Required**: Yes


# StartReadSetExportJobRequestRequestTypeDef

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


# StartReadSetExportJobResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartReadSetImportJobRequestRequestTypeDef

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


# StartReadSetImportJobResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# StartReferenceImportJobRequestRequestTypeDef

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


# StartReferenceImportJobResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# StartRunRequestRequestTypeDef

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


# StartRunResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartVariantImportRequestRequestTypeDef

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


# TagResourceRequestRequestTypeDef

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


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAnnotationStoreRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateAnnotationStoreResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### reference
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ReferenceItemTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.StoreOptionsOutputTypeDef'>
- **Required**: Yes

### storeFormat
- **Type**: typing.Literal['GFF', 'TSV', 'VCF']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAnnotationStoreVersionRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### versionName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateAnnotationStoreVersionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRunGroupRequestRequestTypeDef

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


# UpdateVariantStoreRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateVariantStoreResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### reference
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ReferenceItemTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateWorkflowRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# UploadReadSetPartRequestRequestTypeDef

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
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
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


# VariantStoreItemTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### reference
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.ReferenceItemTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.omics_classes.SseConfigTypeDef'>
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


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


# WorkflowListItemTypeDef

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


# WorkflowParameterTypeDef

### description
- **Type**: typing.Optional[str]

### optional
- **Type**: typing.Optional[bool]


