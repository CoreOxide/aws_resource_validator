# Signer Signer Classes

# AddProfilePermissionRequest

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


# AddProfilePermissionResponse

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.signer.signer_classes.ResponseMetadata'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelSigningProfileRequest

### profileName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSigningJobRequest

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSigningJobRequestWait

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeSigningJobResponse

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.signer.signer_classes.Source'>
- **Required**: Yes

### signingMaterial
- **Type**: <class 'aws_resource_validator.pydantic_models.signer.signer_classes.SigningMaterial'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.signer.signer_classes.SigningPlatformOverrides'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.signer.signer_classes.SigningJobRevocationRecord'>
- **Required**: Yes

### signedObject
- **Type**: <class 'aws_resource_validator.pydantic_models.signer.signer_classes.SignedObject'>
- **Required**: Yes

### jobOwner
- **Type**: <class 'str'>
- **Required**: Yes

### jobInvoker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.signer.signer_classes.ResponseMetadata'>
- **Required**: Yes


# Destination

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer.signer_classes.S3Destination]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.signer.signer_classes.ResponseMetadata'>
- **Required**: Yes


# EncryptionAlgorithmOptions

### allowedValues
- **Type**: typing.List[typing.Literal['ECDSA', 'RSA']]
- **Required**: Yes

### defaultValue
- **Type**: typing.Literal['ECDSA', 'RSA']
- **Required**: Yes


# GetRevocationStatusRequest

### signatureTimestamp
- **Type**: typing.Union[datetime.datetime, str]
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
- **Type**: typing.List[str]
- **Required**: Yes


# GetRevocationStatusResponse

### revokedEntities
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.signer.signer_classes.ResponseMetadata'>
- **Required**: Yes


# GetSigningPlatformRequest

### platformId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSigningPlatformResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.signer.signer_classes.SigningConfiguration'>
- **Required**: Yes

### signingImageFormat
- **Type**: <class 'aws_resource_validator.pydantic_models.signer.signer_classes.SigningImageFormat'>
- **Required**: Yes

### maxSizeInMB
- **Type**: <class 'int'>
- **Required**: Yes

### revocationSupported
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.signer.signer_classes.ResponseMetadata'>
- **Required**: Yes


# GetSigningProfileRequest

### profileName
- **Type**: <class 'str'>
- **Required**: Yes

### profileOwner
- **Type**: typing.Optional[str]


# GetSigningProfileResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.signer.signer_classes.SigningProfileRevocationRecord'>
- **Required**: Yes

### signingMaterial
- **Type**: <class 'aws_resource_validator.pydantic_models.signer.signer_classes.SigningMaterial'>
- **Required**: Yes

### platformId
- **Type**: <class 'str'>
- **Required**: Yes

### platformDisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### signatureValidityPeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.signer.signer_classes.SignatureValidityPeriod'>
- **Required**: Yes

### overrides
- **Type**: <class 'aws_resource_validator.pydantic_models.signer.signer_classes.SigningPlatformOverrides'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.signer.signer_classes.ResponseMetadata'>
- **Required**: Yes


# HashAlgorithmOptions

### allowedValues
- **Type**: typing.List[typing.Literal['SHA1', 'SHA256']]
- **Required**: Yes

### defaultValue
- **Type**: typing.Literal['SHA1', 'SHA256']
- **Required**: Yes


# ListProfilePermissionsRequest

### profileName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProfilePermissionsResponse

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### policySizeBytes
- **Type**: <class 'int'>
- **Required**: Yes

### permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.signer.signer_classes.Permission]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.signer.signer_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSigningJobsRequest

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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### signatureExpiresAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### jobInvoker
- **Type**: typing.Optional[str]


# ListSigningJobsRequestPaginate

### status
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'Succeeded']]

### platformId
- **Type**: typing.Optional[str]

### requestedBy
- **Type**: typing.Optional[str]

### isRevoked
- **Type**: typing.Optional[bool]

### signatureExpiresBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### signatureExpiresAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### jobInvoker
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer.signer_classes.PaginatorConfig]


# ListSigningJobsResponse

### jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.signer.signer_classes.SigningJob]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.signer.signer_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSigningPlatformsRequest

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


# ListSigningPlatformsRequestPaginate

### category
- **Type**: typing.Optional[str]

### partner
- **Type**: typing.Optional[str]

### target
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer.signer_classes.PaginatorConfig]


# ListSigningPlatformsResponse

### platforms
- **Type**: typing.List[aws_resource_validator.pydantic_models.signer.signer_classes.SigningPlatform]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.signer.signer_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSigningProfilesRequest

### includeCanceled
- **Type**: typing.Optional[bool]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### platformId
- **Type**: typing.Optional[str]

### statuses
- **Type**: typing.Optional[typing.List[typing.Literal['Active', 'Canceled', 'Revoked']]]


# ListSigningProfilesRequestPaginate

### includeCanceled
- **Type**: typing.Optional[bool]

### platformId
- **Type**: typing.Optional[str]

### statuses
- **Type**: typing.Optional[typing.List[typing.Literal['Active', 'Canceled', 'Revoked']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer.signer_classes.PaginatorConfig]


# ListSigningProfilesResponse

### profiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.signer.signer_classes.SigningProfile]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.signer.signer_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.signer.signer_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Permission

### action
- **Type**: typing.Optional[str]

### principal
- **Type**: typing.Optional[str]

### statementId
- **Type**: typing.Optional[str]

### profileVersion
- **Type**: typing.Optional[str]


# PutSigningProfileRequest

### profileName
- **Type**: <class 'str'>
- **Required**: Yes

### platformId
- **Type**: <class 'str'>
- **Required**: Yes

### signingMaterial
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer.signer_classes.SigningMaterial]

### signatureValidityPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer.signer_classes.SignatureValidityPeriod]

### overrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer.signer_classes.SigningPlatformOverrides]

### signingParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# PutSigningProfileResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.signer.signer_classes.ResponseMetadata'>
- **Required**: Yes


# RemoveProfilePermissionRequest

### profileName
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### statementId
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveProfilePermissionResponse

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.signer.signer_classes.ResponseMetadata'>
- **Required**: Yes


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


# RevokeSignatureRequest

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### reason
- **Type**: <class 'str'>
- **Required**: Yes

### jobOwner
- **Type**: typing.Optional[str]


# RevokeSigningProfileRequest

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
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# S3Destination

### bucketName
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]


# S3SignedObject

### bucketName
- **Type**: typing.Optional[str]

### key
- **Type**: typing.Optional[str]


# S3Source

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes


# SignPayloadRequest

### profileName
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### payloadFormat
- **Type**: <class 'str'>
- **Required**: Yes

### profileOwner
- **Type**: typing.Optional[str]


# SignPayloadResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.signer.signer_classes.ResponseMetadata'>
- **Required**: Yes


# SignatureValidityPeriod

### value
- **Type**: typing.Optional[int]

### type
- **Type**: typing.Optional[typing.Literal['DAYS', 'MONTHS', 'YEARS']]


# SignedObject

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer.signer_classes.S3SignedObject]


# SigningConfiguration

### encryptionAlgorithmOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.signer.signer_classes.EncryptionAlgorithmOptions'>
- **Required**: Yes

### hashAlgorithmOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.signer.signer_classes.HashAlgorithmOptions'>
- **Required**: Yes


# SigningConfigurationOverrides

### encryptionAlgorithm
- **Type**: typing.Optional[typing.Literal['ECDSA', 'RSA']]

### hashAlgorithm
- **Type**: typing.Optional[typing.Literal['SHA1', 'SHA256']]


# SigningImageFormat

### supportedFormats
- **Type**: typing.List[typing.Literal['JSON', 'JSONDetached', 'JSONEmbedded']]
- **Required**: Yes

### defaultFormat
- **Type**: typing.Literal['JSON', 'JSONDetached', 'JSONEmbedded']
- **Required**: Yes


# SigningJob

### jobId
- **Type**: typing.Optional[str]

### source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer.signer_classes.Source]

### signedObject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer.signer_classes.SignedObject]

### signingMaterial
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer.signer_classes.SigningMaterial]

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


# SigningJobRevocationRecord

### reason
- **Type**: typing.Optional[str]

### revokedAt
- **Type**: typing.Optional[datetime.datetime]

### revokedBy
- **Type**: typing.Optional[str]


# SigningMaterial

### certificateArn
- **Type**: <class 'str'>
- **Required**: Yes


# SigningPlatform

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer.signer_classes.SigningConfiguration]

### signingImageFormat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer.signer_classes.SigningImageFormat]

### maxSizeInMB
- **Type**: typing.Optional[int]

### revocationSupported
- **Type**: typing.Optional[bool]


# SigningPlatformOverrides

### signingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer.signer_classes.SigningConfigurationOverrides]

### signingImageFormat
- **Type**: typing.Optional[typing.Literal['JSON', 'JSONDetached', 'JSONEmbedded']]


# SigningProfile

### profileName
- **Type**: typing.Optional[str]

### profileVersion
- **Type**: typing.Optional[str]

### profileVersionArn
- **Type**: typing.Optional[str]

### signingMaterial
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer.signer_classes.SigningMaterial]

### signatureValidityPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer.signer_classes.SignatureValidityPeriod]

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


# SigningProfileRevocationRecord

### revocationEffectiveFrom
- **Type**: typing.Optional[datetime.datetime]

### revokedAt
- **Type**: typing.Optional[datetime.datetime]

### revokedBy
- **Type**: typing.Optional[str]


# Source

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.signer.signer_classes.S3Source]


# StartSigningJobRequest

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.signer.signer_classes.Source'>
- **Required**: Yes

### destination
- **Type**: <class 'aws_resource_validator.pydantic_models.signer.signer_classes.Destination'>
- **Required**: Yes

### profileName
- **Type**: <class 'str'>
- **Required**: Yes

### clientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### profileOwner
- **Type**: typing.Optional[str]


# StartSigningJobResponse

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### jobOwner
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.signer.signer_classes.ResponseMetadata'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


