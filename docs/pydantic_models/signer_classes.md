# Signer Classes

# AddProfilePermissionRequestTypeDef

### profileName
- **Type**: <class 'str'>
- **Required**: Yes

### action
- **Type**: <class 'str'>
- **Required**: Yes

### principal
- **Type**: <class 'str'>
- **Required**: Yes

### statementId
- **Type**: <class 'str'>
- **Required**: Yes

### profileVersion
- **Type**: typing.Optional[str]

### revisionId
- **Type**: typing.Optional[str]


# AddProfilePermissionResponseTypeDef

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.signer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelSigningProfileRequestTypeDef

### profileName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSigningJobRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSigningJobRequestWaitTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer_classes.WaiterConfigTypeDef]


# DescribeSigningJobResponseTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.signer_classes.SourceTypeDef'>
- **Required**: Yes

### signingMaterial
- **Type**: <class 'aws_resource_validator.pydantic_models.signer_classes.SigningMaterialTypeDef'>
- **Required**: Yes

### platformId
- **Type**: <class 'str'>
- **Required**: Yes

### platformDisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### profileName
- **Type**: <class 'str'>
- **Required**: Yes

### profileVersion
- **Type**: <class 'str'>
- **Required**: Yes

### overrides
- **Type**: <class 'aws_resource_validator.pydantic_models.signer_classes.SigningPlatformOverridesTypeDef'>
- **Required**: Yes

### signingParameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### completedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### signatureExpiresAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### requestedBy
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Failed', 'InProgress', 'Succeeded']
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### revocationRecord
- **Type**: <class 'aws_resource_validator.pydantic_models.signer_classes.SigningJobRevocationRecordTypeDef'>
- **Required**: Yes

### signedObject
- **Type**: <class 'aws_resource_validator.pydantic_models.signer_classes.SignedObjectTypeDef'>
- **Required**: Yes

### jobOwner
- **Type**: <class 'str'>
- **Required**: Yes

### jobInvoker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.signer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DestinationTypeDef

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer_classes.S3DestinationTypeDef]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.signer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EncryptionAlgorithmOptionsTypeDef

### allowedValues
- **Type**: typing.List[typing.Literal['ECDSA', 'RSA']]
- **Required**: Yes

### defaultValue
- **Type**: typing.Literal['ECDSA', 'RSA']
- **Required**: Yes


# GetRevocationStatusRequestTypeDef

### signatureTimestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.signer_classes.TimestampTypeDef'>
- **Required**: Yes

### platformId
- **Type**: <class 'str'>
- **Required**: Yes

### profileVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### certificateHashes
- **Type**: typing.Sequence[str]
- **Required**: Yes


# GetRevocationStatusResponseTypeDef

### revokedEntities
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.signer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSigningPlatformRequestTypeDef

### platformId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSigningPlatformResponseTypeDef

### platformId
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### partner
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: <class 'str'>
- **Required**: Yes

### category
- **Type**: typing.Literal['AWSIoT']
- **Required**: Yes

### signingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.signer_classes.SigningConfigurationTypeDef'>
- **Required**: Yes

### signingImageFormat
- **Type**: <class 'aws_resource_validator.pydantic_models.signer_classes.SigningImageFormatTypeDef'>
- **Required**: Yes

### maxSizeInMB
- **Type**: <class 'int'>
- **Required**: Yes

### revocationSupported
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.signer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSigningProfileRequestTypeDef

### profileName
- **Type**: <class 'str'>
- **Required**: Yes

### profileOwner
- **Type**: typing.Optional[str]


# GetSigningProfileResponseTypeDef

### profileName
- **Type**: <class 'str'>
- **Required**: Yes

### profileVersion
- **Type**: <class 'str'>
- **Required**: Yes

### profileVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### revocationRecord
- **Type**: <class 'aws_resource_validator.pydantic_models.signer_classes.SigningProfileRevocationRecordTypeDef'>
- **Required**: Yes

### signingMaterial
- **Type**: <class 'aws_resource_validator.pydantic_models.signer_classes.SigningMaterialTypeDef'>
- **Required**: Yes

### platformId
- **Type**: <class 'str'>
- **Required**: Yes

### platformDisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### signatureValidityPeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.signer_classes.SignatureValidityPeriodTypeDef'>
- **Required**: Yes

### overrides
- **Type**: <class 'aws_resource_validator.pydantic_models.signer_classes.SigningPlatformOverridesTypeDef'>
- **Required**: Yes

### signingParameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### status
- **Type**: typing.Literal['Active', 'Canceled', 'Revoked']
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.signer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HashAlgorithmOptionsTypeDef

### allowedValues
- **Type**: typing.List[typing.Literal['SHA1', 'SHA256']]
- **Required**: Yes

### defaultValue
- **Type**: typing.Literal['SHA1', 'SHA256']
- **Required**: Yes


# ListProfilePermissionsRequestTypeDef

### profileName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProfilePermissionsResponseTypeDef

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### policySizeBytes
- **Type**: <class 'int'>
- **Required**: Yes

### permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.signer_classes.PermissionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.signer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSigningJobsRequestPaginateTypeDef

### status
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'Succeeded']]

### platformId
- **Type**: typing.Optional[str]

### requestedBy
- **Type**: typing.Optional[str]

### isRevoked
- **Type**: typing.Optional[bool]

### signatureExpiresBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer_classes.TimestampTypeDef]

### signatureExpiresAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer_classes.TimestampTypeDef]

### jobInvoker
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer_classes.PaginatorConfigTypeDef]


# ListSigningJobsRequestTypeDef

### status
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'Succeeded']]

### platformId
- **Type**: typing.Optional[str]

### requestedBy
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### isRevoked
- **Type**: typing.Optional[bool]

### signatureExpiresBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer_classes.TimestampTypeDef]

### signatureExpiresAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer_classes.TimestampTypeDef]

### jobInvoker
- **Type**: typing.Optional[str]


# ListSigningJobsResponseTypeDef

### jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.signer_classes.SigningJobTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.signer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSigningPlatformsRequestPaginateTypeDef

### category
- **Type**: typing.Optional[str]

### partner
- **Type**: typing.Optional[str]

### target
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer_classes.PaginatorConfigTypeDef]


# ListSigningPlatformsRequestTypeDef

### category
- **Type**: typing.Optional[str]

### partner
- **Type**: typing.Optional[str]

### target
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSigningPlatformsResponseTypeDef

### platforms
- **Type**: typing.List[aws_resource_validator.pydantic_models.signer_classes.SigningPlatformTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.signer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSigningProfilesRequestPaginateTypeDef

### includeCanceled
- **Type**: typing.Optional[bool]

### platformId
- **Type**: typing.Optional[str]

### statuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Active', 'Canceled', 'Revoked']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer_classes.PaginatorConfigTypeDef]


# ListSigningProfilesRequestTypeDef

### includeCanceled
- **Type**: typing.Optional[bool]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### platformId
- **Type**: typing.Optional[str]

### statuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Active', 'Canceled', 'Revoked']]]


# ListSigningProfilesResponseTypeDef

### profiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.signer_classes.SigningProfileTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.signer_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.signer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PermissionTypeDef

### action
- **Type**: typing.Optional[str]

### principal
- **Type**: typing.Optional[str]

### statementId
- **Type**: typing.Optional[str]

### profileVersion
- **Type**: typing.Optional[str]


# PutSigningProfileRequestTypeDef

### profileName
- **Type**: <class 'str'>
- **Required**: Yes

### platformId
- **Type**: <class 'str'>
- **Required**: Yes

### signingMaterial
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer_classes.SigningMaterialTypeDef]

### signatureValidityPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer_classes.SignatureValidityPeriodTypeDef]

### overrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer_classes.SigningPlatformOverridesTypeDef]

### signingParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# PutSigningProfileResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### profileVersion
- **Type**: <class 'str'>
- **Required**: Yes

### profileVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.signer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RemoveProfilePermissionRequestTypeDef

### profileName
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### statementId
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveProfilePermissionResponseTypeDef

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.signer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# RevokeSignatureRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### reason
- **Type**: <class 'str'>
- **Required**: Yes

### jobOwner
- **Type**: typing.Optional[str]


# RevokeSigningProfileRequestTypeDef

### profileName
- **Type**: <class 'str'>
- **Required**: Yes

### profileVersion
- **Type**: <class 'str'>
- **Required**: Yes

### reason
- **Type**: <class 'str'>
- **Required**: Yes

### effectiveTime
- **Type**: <class 'aws_resource_validator.pydantic_models.signer_classes.TimestampTypeDef'>
- **Required**: Yes


# S3DestinationTypeDef

### bucketName
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]


# S3SignedObjectTypeDef

### bucketName
- **Type**: typing.Optional[str]

### key
- **Type**: typing.Optional[str]


# S3SourceTypeDef

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes


# SignPayloadRequestTypeDef

### profileName
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: <class 'aws_resource_validator.pydantic_models.signer_classes.BlobTypeDef'>
- **Required**: Yes

### payloadFormat
- **Type**: <class 'str'>
- **Required**: Yes

### profileOwner
- **Type**: typing.Optional[str]


# SignPayloadResponseTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### jobOwner
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### signature
- **Type**: <class 'bytes'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.signer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SignatureValidityPeriodTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SignedObjectTypeDef

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer_classes.S3SignedObjectTypeDef]


# SigningConfigurationOverridesTypeDef

### encryptionAlgorithm
- **Type**: typing.Optional[typing.Literal['ECDSA', 'RSA']]

### hashAlgorithm
- **Type**: typing.Optional[typing.Literal['SHA1', 'SHA256']]


# SigningConfigurationTypeDef

### encryptionAlgorithmOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.signer_classes.EncryptionAlgorithmOptionsTypeDef'>
- **Required**: Yes

### hashAlgorithmOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.signer_classes.HashAlgorithmOptionsTypeDef'>
- **Required**: Yes


# SigningImageFormatTypeDef

### supportedFormats
- **Type**: typing.List[typing.Literal['JSON', 'JSONDetached', 'JSONEmbedded']]
- **Required**: Yes

### defaultFormat
- **Type**: typing.Literal['JSON', 'JSONDetached', 'JSONEmbedded']
- **Required**: Yes


# SigningJobRevocationRecordTypeDef

### reason
- **Type**: typing.Optional[str]

### revokedAt
- **Type**: typing.Optional[datetime.datetime]

### revokedBy
- **Type**: typing.Optional[str]


# SigningJobTypeDef

### jobId
- **Type**: typing.Optional[str]

### source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer_classes.SourceTypeDef]

### signedObject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer_classes.SignedObjectTypeDef]

### signingMaterial
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer_classes.SigningMaterialTypeDef]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'Succeeded']]

### isRevoked
- **Type**: typing.Optional[bool]

### profileName
- **Type**: typing.Optional[str]

### profileVersion
- **Type**: typing.Optional[str]

### platformId
- **Type**: typing.Optional[str]

### platformDisplayName
- **Type**: typing.Optional[str]

### signatureExpiresAt
- **Type**: typing.Optional[datetime.datetime]

### jobOwner
- **Type**: typing.Optional[str]

### jobInvoker
- **Type**: typing.Optional[str]


# SigningMaterialTypeDef

### certificateArn
- **Type**: <class 'str'>
- **Required**: Yes


# SigningPlatformOverridesTypeDef

### signingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer_classes.SigningConfigurationOverridesTypeDef]

### signingImageFormat
- **Type**: typing.Optional[typing.Literal['JSON', 'JSONDetached', 'JSONEmbedded']]


# SigningPlatformTypeDef

### platformId
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### partner
- **Type**: typing.Optional[str]

### target
- **Type**: typing.Optional[str]

### category
- **Type**: typing.Optional[typing.Literal['AWSIoT']]

### signingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer_classes.SigningConfigurationTypeDef]

### signingImageFormat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer_classes.SigningImageFormatTypeDef]

### maxSizeInMB
- **Type**: typing.Optional[int]

### revocationSupported
- **Type**: typing.Optional[bool]


# SigningProfileRevocationRecordTypeDef

### revocationEffectiveFrom
- **Type**: typing.Optional[datetime.datetime]

### revokedAt
- **Type**: typing.Optional[datetime.datetime]

### revokedBy
- **Type**: typing.Optional[str]


# SigningProfileTypeDef

### profileName
- **Type**: typing.Optional[str]

### profileVersion
- **Type**: typing.Optional[str]

### profileVersionArn
- **Type**: typing.Optional[str]

### signingMaterial
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer_classes.SigningMaterialTypeDef]

### signatureValidityPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer_classes.SignatureValidityPeriodTypeDef]

### platformId
- **Type**: typing.Optional[str]

### platformDisplayName
- **Type**: typing.Optional[str]

### signingParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### status
- **Type**: typing.Optional[typing.Literal['Active', 'Canceled', 'Revoked']]

### arn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# SourceTypeDef

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer_classes.S3SourceTypeDef]


# StartSigningJobRequestTypeDef

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.signer_classes.SourceTypeDef'>
- **Required**: Yes

### destination
- **Type**: <class 'aws_resource_validator.pydantic_models.signer_classes.DestinationTypeDef'>
- **Required**: Yes

### profileName
- **Type**: <class 'str'>
- **Required**: Yes

### clientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### profileOwner
- **Type**: typing.Optional[str]


# StartSigningJobResponseTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### jobOwner
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.signer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


