# S3Control Classes

# AbortIncompleteMultipartUpload

### DaysAfterInitiation
- **Type**: typing.Optional[int]


# AccessControlTranslation

### Owner
- **Type**: typing.Literal['Destination']
- **Required**: Yes


# AccessGrantsLocationConfiguration

### S3SubPrefix
- **Type**: typing.Optional[str]


# AccessPoint

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkOrigin
- **Type**: typing.Literal['Internet', 'VPC']
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### VpcConfiguration
- **Type**: <class 'NoneType'>

### AccessPointArn
- **Type**: typing.Optional[str]

### Alias
- **Type**: typing.Optional[str]

### BucketAccountId
- **Type**: typing.Optional[str]


# AccountLevel

### BucketLevel
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.BucketLevel'>
- **Required**: Yes

### ActivityMetrics
- **Type**: <class 'NoneType'>

### AdvancedCostOptimizationMetrics
- **Type**: <class 'NoneType'>

### AdvancedDataProtectionMetrics
- **Type**: <class 'NoneType'>

### DetailedStatusCodesMetrics
- **Type**: <class 'NoneType'>

### StorageLensGroupLevel
- **Type**: <class 'NoneType'>


# AccountLevelOutput

### BucketLevel
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.BucketLevel'>
- **Required**: Yes

### ActivityMetrics
- **Type**: <class 'NoneType'>

### AdvancedCostOptimizationMetrics
- **Type**: <class 'NoneType'>

### AdvancedDataProtectionMetrics
- **Type**: <class 'NoneType'>

### DetailedStatusCodesMetrics
- **Type**: <class 'NoneType'>

### StorageLensGroupLevel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.StorageLensGroupLevelOutput]


# ActivityMetrics

### IsEnabled
- **Type**: typing.Optional[bool]


# AdvancedCostOptimizationMetrics

### IsEnabled
- **Type**: typing.Optional[bool]


# AdvancedDataProtectionMetrics

### IsEnabled
- **Type**: typing.Optional[bool]


# AssociateAccessGrantsIdentityCenterRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityCenterArn
- **Type**: <class 'str'>
- **Required**: Yes


# AsyncErrorDetails

### Code
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### Resource
- **Type**: typing.Optional[str]

### RequestId
- **Type**: typing.Optional[str]


# AsyncOperation

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### Operation
- **Type**: typing.Optional[typing.Literal['CreateMultiRegionAccessPoint', 'DeleteMultiRegionAccessPoint', 'PutMultiRegionAccessPointPolicy']]

### RequestTokenARN
- **Type**: typing.Optional[str]

### RequestParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.AsyncRequestParameters]

### RequestStatus
- **Type**: typing.Optional[str]

### ResponseDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.AsyncResponseDetails]


# AsyncRequestParameters

### CreateMultiRegionAccessPointRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.CreateMultiRegionAccessPointInputOutput]

### DeleteMultiRegionAccessPointRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.DeleteMultiRegionAccessPointInput]

### PutMultiRegionAccessPointPolicyRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.PutMultiRegionAccessPointPolicyInput]


# AsyncResponseDetails

### MultiRegionAccessPointDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.MultiRegionAccessPointsAsyncResponse]

### ErrorDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.AsyncErrorDetails]


# AwsLambdaTransformation

### FunctionArn
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionPayload
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BucketLevel

### ActivityMetrics
- **Type**: <class 'NoneType'>

### PrefixLevel
- **Type**: <class 'NoneType'>

### AdvancedCostOptimizationMetrics
- **Type**: <class 'NoneType'>

### AdvancedDataProtectionMetrics
- **Type**: <class 'NoneType'>

### DetailedStatusCodesMetrics
- **Type**: <class 'NoneType'>


# CloudWatchMetrics

### IsEnabled
- **Type**: <class 'bool'>
- **Required**: Yes


# CreateAccessGrantRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantsLocationId
- **Type**: <class 'str'>
- **Required**: Yes

### Grantee
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.Grantee'>
- **Required**: Yes

### Permission
- **Type**: typing.Literal['READ', 'READWRITE', 'WRITE']
- **Required**: Yes

### AccessGrantsLocationConfiguration
- **Type**: <class 'NoneType'>

### ApplicationArn
- **Type**: typing.Optional[str]

### S3PrefixType
- **Type**: typing.Optional[typing.Literal['Object']]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.Tag]]


# CreateAccessGrantResult

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AccessGrantId
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantArn
- **Type**: <class 'str'>
- **Required**: Yes

### Grantee
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.Grantee'>
- **Required**: Yes

### AccessGrantsLocationId
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantsLocationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.AccessGrantsLocationConfiguration'>
- **Required**: Yes

### Permission
- **Type**: typing.Literal['READ', 'READWRITE', 'WRITE']
- **Required**: Yes

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### GrantScope
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAccessGrantsInstanceRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityCenterArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.Tag]]


# CreateAccessGrantsInstanceResult

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AccessGrantsInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantsInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityCenterArn
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityCenterInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityCenterApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAccessGrantsLocationRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### LocationScope
- **Type**: <class 'str'>
- **Required**: Yes

### IAMRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.Tag]]


# CreateAccessGrantsLocationResult

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AccessGrantsLocationId
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantsLocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### LocationScope
- **Type**: <class 'str'>
- **Required**: Yes

### IAMRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAccessPointForObjectLambdaRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ObjectLambdaConfigurationUnion'>
- **Required**: Yes


# CreateAccessPointForObjectLambdaResult

### ObjectLambdaAccessPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### Alias
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ObjectLambdaAccessPointAlias'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAccessPointRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### VpcConfiguration
- **Type**: <class 'NoneType'>

### PublicAccessBlockConfiguration
- **Type**: <class 'NoneType'>

### BucketAccountId
- **Type**: typing.Optional[str]


# CreateAccessPointResult

### AccessPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### Alias
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# CreateBucketConfiguration

### LocationConstraint
- **Type**: typing.Optional[typing.Literal['EU', 'ap-northeast-1', 'ap-south-1', 'ap-southeast-1', 'ap-southeast-2', 'cn-north-1', 'eu-central-1', 'eu-west-1', 'sa-east-1', 'us-west-1', 'us-west-2']]


# CreateBucketRequest

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### ACL
- **Type**: typing.Optional[typing.Literal['authenticated-read', 'private', 'public-read', 'public-read-write']]

### CreateBucketConfiguration
- **Type**: <class 'NoneType'>

### GrantFullControl
- **Type**: typing.Optional[str]

### GrantRead
- **Type**: typing.Optional[str]

### GrantReadACP
- **Type**: typing.Optional[str]

### GrantWrite
- **Type**: typing.Optional[str]

### GrantWriteACP
- **Type**: typing.Optional[str]

### ObjectLockEnabledForBucket
- **Type**: typing.Optional[bool]

### OutpostId
- **Type**: typing.Optional[str]


# CreateBucketResult

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### BucketArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# CreateJobRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Operation
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.JobOperationUnion'>
- **Required**: Yes

### Report
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.JobReport'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConfirmationRequired
- **Type**: typing.Optional[bool]

### Manifest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.JobManifestUnion]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.S3Tag]]

### ManifestGenerator
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.JobManifestGeneratorUnion]


# CreateJobResult

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMultiRegionAccessPointInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Regions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.Region]
- **Required**: Yes

### PublicAccessBlock
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.PublicAccessBlockConfiguration]


# CreateMultiRegionAccessPointInputOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Regions
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.Region]
- **Required**: Yes

### PublicAccessBlock
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.PublicAccessBlockConfiguration]


# CreateMultiRegionAccessPointInputUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateMultiRegionAccessPointRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### Details
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.CreateMultiRegionAccessPointInputUnion'>
- **Required**: Yes


# CreateMultiRegionAccessPointResult

### RequestTokenARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# CreateStorageLensGroupRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### StorageLensGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.StorageLensGroupUnion'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.Tag]]


# Credentials

### AccessKeyId
- **Type**: typing.Optional[str]

### SecretAccessKey
- **Type**: typing.Optional[str]

### SessionToken
- **Type**: typing.Optional[str]

### Expiration
- **Type**: typing.Optional[datetime.datetime]


# DeleteAccessGrantRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAccessGrantsInstanceRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAccessGrantsInstanceResourcePolicyRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAccessGrantsLocationRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantsLocationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAccessPointForObjectLambdaRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAccessPointPolicyForObjectLambdaRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAccessPointPolicyRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAccessPointRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBucketLifecycleConfigurationRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBucketPolicyRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBucketReplicationRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBucketRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBucketTaggingRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteJobTaggingRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMarkerReplication

### Status
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes


# DeleteMultiRegionAccessPointInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMultiRegionAccessPointRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### Details
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.DeleteMultiRegionAccessPointInput'>
- **Required**: Yes


# DeleteMultiRegionAccessPointResult

### RequestTokenARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# DeletePublicAccessBlockRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStorageLensConfigurationRequest

### ConfigId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStorageLensConfigurationTaggingRequest

### ConfigId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStorageLensGroupRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeJobRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeJobResult

### Job
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.JobDescriptor'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeMultiRegionAccessPointOperationRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### RequestTokenARN
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMultiRegionAccessPointOperationResult

### AsyncOperation
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.AsyncOperation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# Destination

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Account
- **Type**: typing.Optional[str]

### ReplicationTime
- **Type**: <class 'NoneType'>

### AccessControlTranslation
- **Type**: <class 'NoneType'>

### EncryptionConfiguration
- **Type**: <class 'NoneType'>

### Metrics
- **Type**: <class 'NoneType'>

### StorageClass
- **Type**: typing.Optional[typing.Literal['DEEP_ARCHIVE', 'GLACIER', 'GLACIER_IR', 'INTELLIGENT_TIERING', 'ONEZONE_IA', 'OUTPOSTS', 'REDUCED_REDUNDANCY', 'STANDARD', 'STANDARD_IA']]


# DetailedStatusCodesMetrics

### IsEnabled
- **Type**: typing.Optional[bool]


# DissociateAccessGrantsIdentityCenterRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# EncryptionConfiguration

### ReplicaKmsKeyID
- **Type**: typing.Optional[str]


# EstablishedMultiRegionAccessPointPolicy

### Policy
- **Type**: typing.Optional[str]


# Exclude

### Buckets
- **Type**: typing.Optional[typing.Sequence[str]]

### Regions
- **Type**: typing.Optional[typing.Sequence[str]]


# ExcludeOutput

### Buckets
- **Type**: typing.Optional[typing.List[str]]

### Regions
- **Type**: typing.Optional[typing.List[str]]


# ExistingObjectReplication

### Status
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes


# GeneratedManifestEncryption

### SSES3
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### SSEKMS
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.SSEKMSEncryption]


# GeneratedManifestEncryptionOutput

### SSES3
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### SSEKMS
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.SSEKMSEncryption]


# GetAccessGrantRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessGrantResult

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AccessGrantId
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantArn
- **Type**: <class 'str'>
- **Required**: Yes

### Grantee
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.Grantee'>
- **Required**: Yes

### Permission
- **Type**: typing.Literal['READ', 'READWRITE', 'WRITE']
- **Required**: Yes

### AccessGrantsLocationId
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantsLocationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.AccessGrantsLocationConfiguration'>
- **Required**: Yes

### GrantScope
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# GetAccessGrantsInstanceForPrefixRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### S3Prefix
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessGrantsInstanceForPrefixResult

### AccessGrantsInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantsInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# GetAccessGrantsInstanceRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessGrantsInstanceResourcePolicyRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessGrantsInstanceResourcePolicyResult

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### Organization
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# GetAccessGrantsInstanceResult

### AccessGrantsInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantsInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityCenterArn
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityCenterInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityCenterApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# GetAccessGrantsLocationRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantsLocationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessGrantsLocationResult

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AccessGrantsLocationId
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantsLocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### LocationScope
- **Type**: <class 'str'>
- **Required**: Yes

### IAMRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# GetAccessPointConfigurationForObjectLambdaRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessPointConfigurationForObjectLambdaResult

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ObjectLambdaConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# GetAccessPointForObjectLambdaRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessPointForObjectLambdaResult

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PublicAccessBlockConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.PublicAccessBlockConfiguration'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Alias
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ObjectLambdaAccessPointAlias'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# GetAccessPointPolicyForObjectLambdaRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessPointPolicyForObjectLambdaResult

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# GetAccessPointPolicyRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessPointPolicyResult

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# GetAccessPointPolicyStatusForObjectLambdaRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessPointPolicyStatusForObjectLambdaResult

### PolicyStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.PolicyStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# GetAccessPointPolicyStatusRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessPointPolicyStatusResult

### PolicyStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.PolicyStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# GetAccessPointRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessPointResult

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkOrigin
- **Type**: typing.Literal['Internet', 'VPC']
- **Required**: Yes

### VpcConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.VpcConfiguration'>
- **Required**: Yes

### PublicAccessBlockConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.PublicAccessBlockConfiguration'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Alias
- **Type**: <class 'str'>
- **Required**: Yes

### AccessPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### Endpoints
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### BucketAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# GetBucketLifecycleConfigurationRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes


# GetBucketLifecycleConfigurationResult

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.LifecycleRuleOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# GetBucketPolicyRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes


# GetBucketPolicyResult

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# GetBucketReplicationRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes


# GetBucketReplicationResult

### ReplicationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ReplicationConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# GetBucketRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes


# GetBucketResult

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### PublicAccessBlockEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# GetBucketTaggingRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes


# GetBucketTaggingResult

### TagSet
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.S3Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# GetBucketVersioningRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes


# GetBucketVersioningResult

### Status
- **Type**: typing.Literal['Enabled', 'Suspended']
- **Required**: Yes

### MFADelete
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataAccessRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Target
- **Type**: <class 'str'>
- **Required**: Yes

### Permission
- **Type**: typing.Literal['READ', 'READWRITE', 'WRITE']
- **Required**: Yes

### DurationSeconds
- **Type**: typing.Optional[int]

### Privilege
- **Type**: typing.Optional[typing.Literal['Default', 'Minimal']]

### TargetType
- **Type**: typing.Optional[typing.Literal['Object']]


# GetDataAccessResult

### Credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.Credentials'>
- **Required**: Yes

### MatchedGrantTarget
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# GetJobTaggingRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetJobTaggingResult

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.S3Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# GetMultiRegionAccessPointPolicyRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetMultiRegionAccessPointPolicyResult

### Policy
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.MultiRegionAccessPointPolicyDocument'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# GetMultiRegionAccessPointPolicyStatusRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetMultiRegionAccessPointPolicyStatusResult

### Established
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.PolicyStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# GetMultiRegionAccessPointRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetMultiRegionAccessPointResult

### AccessPoint
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.MultiRegionAccessPointReport'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# GetMultiRegionAccessPointRoutesRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Mrap
- **Type**: <class 'str'>
- **Required**: Yes


# GetMultiRegionAccessPointRoutesResult

### Mrap
- **Type**: <class 'str'>
- **Required**: Yes

### Routes
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.MultiRegionAccessPointRoute]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# GetPublicAccessBlockOutput

### PublicAccessBlockConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.PublicAccessBlockConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# GetPublicAccessBlockRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# GetStorageLensConfigurationRequest

### ConfigId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# GetStorageLensConfigurationResult

### StorageLensConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.StorageLensConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# GetStorageLensConfigurationTaggingRequest

### ConfigId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# GetStorageLensConfigurationTaggingResult

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.StorageLensTag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# GetStorageLensGroupRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# GetStorageLensGroupResult

### StorageLensGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.StorageLensGroupOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# Grantee

### GranteeType
- **Type**: typing.Optional[typing.Literal['DIRECTORY_GROUP', 'DIRECTORY_USER', 'IAM']]

### GranteeIdentifier
- **Type**: typing.Optional[str]


# Include

### Buckets
- **Type**: typing.Optional[typing.Sequence[str]]

### Regions
- **Type**: typing.Optional[typing.Sequence[str]]


# IncludeOutput

### Buckets
- **Type**: typing.Optional[typing.List[str]]

### Regions
- **Type**: typing.Optional[typing.List[str]]


# JobDescriptor

### JobId
- **Type**: typing.Optional[str]

### ConfirmationRequired
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]

### JobArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Active', 'Cancelled', 'Cancelling', 'Complete', 'Completing', 'Failed', 'Failing', 'New', 'Paused', 'Pausing', 'Preparing', 'Ready', 'Suspended']]

### Manifest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.JobManifestOutput]

### Operation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.JobOperationOutput]

### Priority
- **Type**: typing.Optional[int]

### ProgressSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.JobProgressSummary]

### StatusUpdateReason
- **Type**: typing.Optional[str]

### FailureReasons
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.s3control_classes.JobFailure]]

### Report
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.JobReport]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### TerminationDate
- **Type**: typing.Optional[datetime.datetime]

### RoleArn
- **Type**: typing.Optional[str]

### SuspendedDate
- **Type**: typing.Optional[datetime.datetime]

### SuspendedCause
- **Type**: typing.Optional[str]

### ManifestGenerator
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.JobManifestGeneratorOutput]

### GeneratedManifestDescriptor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3GeneratedManifestDescriptor]


# JobFailure

### FailureCode
- **Type**: typing.Optional[str]

### FailureReason
- **Type**: typing.Optional[str]


# JobListDescriptor

### JobId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Operation
- **Type**: typing.Optional[typing.Literal['LambdaInvoke', 'S3DeleteObjectTagging', 'S3InitiateRestoreObject', 'S3PutObjectAcl', 'S3PutObjectCopy', 'S3PutObjectLegalHold', 'S3PutObjectRetention', 'S3PutObjectTagging', 'S3ReplicateObject']]

### Priority
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['Active', 'Cancelled', 'Cancelling', 'Complete', 'Completing', 'Failed', 'Failing', 'New', 'Paused', 'Pausing', 'Preparing', 'Ready', 'Suspended']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### TerminationDate
- **Type**: typing.Optional[datetime.datetime]

### ProgressSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.JobProgressSummary]


# JobManifest

### Spec
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.JobManifestSpec'>
- **Required**: Yes

### Location
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.JobManifestLocation'>
- **Required**: Yes


# JobManifestGenerator

### S3JobManifestGenerator
- **Type**: <class 'NoneType'>


# JobManifestGeneratorFilter

### EligibleForReplication
- **Type**: typing.Optional[bool]

### CreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.Timestamp]

### CreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.Timestamp]

### ObjectReplicationStatuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['COMPLETED', 'FAILED', 'NONE', 'REPLICA']]]

### KeyNameConstraint
- **Type**: <class 'NoneType'>

### ObjectSizeGreaterThanBytes
- **Type**: typing.Optional[int]

### ObjectSizeLessThanBytes
- **Type**: typing.Optional[int]

### MatchAnyStorageClass
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DEEP_ARCHIVE', 'GLACIER', 'GLACIER_IR', 'INTELLIGENT_TIERING', 'ONEZONE_IA', 'STANDARD', 'STANDARD_IA']]]


# JobManifestGeneratorFilterOutput

### EligibleForReplication
- **Type**: typing.Optional[bool]

### CreatedAfter
- **Type**: typing.Optional[datetime.datetime]

### CreatedBefore
- **Type**: typing.Optional[datetime.datetime]

### ObjectReplicationStatuses
- **Type**: typing.Optional[typing.List[typing.Literal['COMPLETED', 'FAILED', 'NONE', 'REPLICA']]]

### KeyNameConstraint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.KeyNameConstraintOutput]

### ObjectSizeGreaterThanBytes
- **Type**: typing.Optional[int]

### ObjectSizeLessThanBytes
- **Type**: typing.Optional[int]

### MatchAnyStorageClass
- **Type**: typing.Optional[typing.List[typing.Literal['DEEP_ARCHIVE', 'GLACIER', 'GLACIER_IR', 'INTELLIGENT_TIERING', 'ONEZONE_IA', 'STANDARD', 'STANDARD_IA']]]


# JobManifestGeneratorOutput

### S3JobManifestGenerator
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3JobManifestGeneratorOutput]


# JobManifestGeneratorUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobManifestLocation

### ObjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectVersionId
- **Type**: typing.Optional[str]


# JobManifestOutput

### Spec
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.JobManifestSpecOutput'>
- **Required**: Yes

### Location
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.JobManifestLocation'>
- **Required**: Yes


# JobManifestSpec

### Format
- **Type**: typing.Literal['S3BatchOperations_CSV_20180820', 'S3InventoryReport_CSV_20161130']
- **Required**: Yes

### Fields
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Bucket', 'Ignore', 'Key', 'VersionId']]]


# JobManifestSpecOutput

### Format
- **Type**: typing.Literal['S3BatchOperations_CSV_20180820', 'S3InventoryReport_CSV_20161130']
- **Required**: Yes

### Fields
- **Type**: typing.Optional[typing.List[typing.Literal['Bucket', 'Ignore', 'Key', 'VersionId']]]


# JobManifestUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobOperation

### LambdaInvoke
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.LambdaInvokeOperation]

### S3PutObjectCopy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3CopyObjectOperation]

### S3PutObjectAcl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3SetObjectAclOperation]

### S3PutObjectTagging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3SetObjectTaggingOperation]

### S3DeleteObjectTagging
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### S3InitiateRestoreObject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3InitiateRestoreObjectOperation]

### S3PutObjectLegalHold
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3SetObjectLegalHoldOperation]

### S3PutObjectRetention
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3SetObjectRetentionOperation]

### S3ReplicateObject
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# JobOperationOutput

### LambdaInvoke
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.LambdaInvokeOperationOutput]

### S3PutObjectCopy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3CopyObjectOperationOutput]

### S3PutObjectAcl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3SetObjectAclOperationOutput]

### S3PutObjectTagging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3SetObjectTaggingOperationOutput]

### S3DeleteObjectTagging
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### S3InitiateRestoreObject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3InitiateRestoreObjectOperation]

### S3PutObjectLegalHold
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3SetObjectLegalHoldOperation]

### S3PutObjectRetention
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3SetObjectRetentionOperationOutput]

### S3ReplicateObject
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# JobOperationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobProgressSummary

### TotalNumberOfTasks
- **Type**: typing.Optional[int]

### NumberOfTasksSucceeded
- **Type**: typing.Optional[int]

### NumberOfTasksFailed
- **Type**: typing.Optional[int]

### Timers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.JobTimers]


# JobReport

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Bucket
- **Type**: typing.Optional[str]

### Format
- **Type**: typing.Optional[typing.Literal['Report_CSV_20180820']]

### Prefix
- **Type**: typing.Optional[str]

### ReportScope
- **Type**: typing.Optional[typing.Literal['AllTasks', 'FailedTasksOnly']]


# JobTimers

### ElapsedTimeInActiveSeconds
- **Type**: typing.Optional[int]


# KeyNameConstraint

### MatchAnyPrefix
- **Type**: typing.Optional[typing.Sequence[str]]

### MatchAnySuffix
- **Type**: typing.Optional[typing.Sequence[str]]

### MatchAnySubstring
- **Type**: typing.Optional[typing.Sequence[str]]


# KeyNameConstraintOutput

### MatchAnyPrefix
- **Type**: typing.Optional[typing.List[str]]

### MatchAnySuffix
- **Type**: typing.Optional[typing.List[str]]

### MatchAnySubstring
- **Type**: typing.Optional[typing.List[str]]


# LambdaInvokeOperation

### FunctionArn
- **Type**: typing.Optional[str]

### InvocationSchemaVersion
- **Type**: typing.Optional[str]

### UserArguments
- **Type**: typing.Optional[typing.Mapping[str, str]]


# LambdaInvokeOperationOutput

### FunctionArn
- **Type**: typing.Optional[str]

### InvocationSchemaVersion
- **Type**: typing.Optional[str]

### UserArguments
- **Type**: typing.Optional[typing.Dict[str, str]]


# LifecycleConfiguration

### Rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.LifecycleRuleUnion]]


# LifecycleExpiration

### Date
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.Timestamp]

### Days
- **Type**: typing.Optional[int]

### ExpiredObjectDeleteMarker
- **Type**: typing.Optional[bool]


# LifecycleExpirationOutput

### Date
- **Type**: typing.Optional[datetime.datetime]

### Days
- **Type**: typing.Optional[int]

### ExpiredObjectDeleteMarker
- **Type**: typing.Optional[bool]


# LifecycleExpirationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LifecycleRule

### Status
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### Expiration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.LifecycleExpirationUnion]

### ID
- **Type**: typing.Optional[str]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.LifecycleRuleFilterUnion]

### Transitions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.TransitionUnion]]

### NoncurrentVersionTransitions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.NoncurrentVersionTransition]]

### NoncurrentVersionExpiration
- **Type**: <class 'NoneType'>

### AbortIncompleteMultipartUpload
- **Type**: <class 'NoneType'>


# LifecycleRuleAndOperator

### Prefix
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.S3Tag]]

### ObjectSizeGreaterThan
- **Type**: typing.Optional[int]

### ObjectSizeLessThan
- **Type**: typing.Optional[int]


# LifecycleRuleAndOperatorOutput

### Prefix
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.s3control_classes.S3Tag]]

### ObjectSizeGreaterThan
- **Type**: typing.Optional[int]

### ObjectSizeLessThan
- **Type**: typing.Optional[int]


# LifecycleRuleAndOperatorUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LifecycleRuleFilter

### Prefix
- **Type**: typing.Optional[str]

### Tag
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3Tag]

### And
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.LifecycleRuleAndOperatorUnion]

### ObjectSizeGreaterThan
- **Type**: typing.Optional[int]

### ObjectSizeLessThan
- **Type**: typing.Optional[int]


# LifecycleRuleFilterOutput

### Prefix
- **Type**: typing.Optional[str]

### Tag
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3Tag]

### And
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.LifecycleRuleAndOperatorOutput]

### ObjectSizeGreaterThan
- **Type**: typing.Optional[int]

### ObjectSizeLessThan
- **Type**: typing.Optional[int]


# LifecycleRuleFilterUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LifecycleRuleOutput

### Status
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### Expiration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.LifecycleExpirationOutput]

### ID
- **Type**: typing.Optional[str]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.LifecycleRuleFilterOutput]

### Transitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.s3control_classes.TransitionOutput]]

### NoncurrentVersionTransitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.s3control_classes.NoncurrentVersionTransition]]

### NoncurrentVersionExpiration
- **Type**: <class 'NoneType'>

### AbortIncompleteMultipartUpload
- **Type**: <class 'NoneType'>


# LifecycleRuleUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListAccessGrantEntry

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### AccessGrantId
- **Type**: typing.Optional[str]

### AccessGrantArn
- **Type**: typing.Optional[str]

### Grantee
- **Type**: <class 'NoneType'>

### Permission
- **Type**: typing.Optional[typing.Literal['READ', 'READWRITE', 'WRITE']]

### AccessGrantsLocationId
- **Type**: typing.Optional[str]

### AccessGrantsLocationConfiguration
- **Type**: <class 'NoneType'>

### GrantScope
- **Type**: typing.Optional[str]

### ApplicationArn
- **Type**: typing.Optional[str]


# ListAccessGrantsInstanceEntry

### AccessGrantsInstanceId
- **Type**: typing.Optional[str]

### AccessGrantsInstanceArn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### IdentityCenterArn
- **Type**: typing.Optional[str]

### IdentityCenterInstanceArn
- **Type**: typing.Optional[str]

### IdentityCenterApplicationArn
- **Type**: typing.Optional[str]


# ListAccessGrantsInstancesRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAccessGrantsInstancesResult

### AccessGrantsInstancesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.ListAccessGrantsInstanceEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAccessGrantsLocationsEntry

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### AccessGrantsLocationId
- **Type**: typing.Optional[str]

### AccessGrantsLocationArn
- **Type**: typing.Optional[str]

### LocationScope
- **Type**: typing.Optional[str]

### IAMRoleArn
- **Type**: typing.Optional[str]


# ListAccessGrantsLocationsRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### LocationScope
- **Type**: typing.Optional[str]


# ListAccessGrantsLocationsResult

### AccessGrantsLocationsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.ListAccessGrantsLocationsEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAccessGrantsRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### GranteeType
- **Type**: typing.Optional[typing.Literal['DIRECTORY_GROUP', 'DIRECTORY_USER', 'IAM']]

### GranteeIdentifier
- **Type**: typing.Optional[str]

### Permission
- **Type**: typing.Optional[typing.Literal['READ', 'READWRITE', 'WRITE']]

### GrantScope
- **Type**: typing.Optional[str]

### ApplicationArn
- **Type**: typing.Optional[str]


# ListAccessGrantsResult

### AccessGrantsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.ListAccessGrantEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAccessPointsForObjectLambdaRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAccessPointsForObjectLambdaRequestPaginate

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.PaginatorConfig]


# ListAccessPointsForObjectLambdaResult

### ObjectLambdaAccessPointList
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.ObjectLambdaAccessPoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAccessPointsRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAccessPointsResult

### AccessPointList
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.AccessPoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCallerAccessGrantsEntry

### Permission
- **Type**: typing.Optional[typing.Literal['READ', 'READWRITE', 'WRITE']]

### GrantScope
- **Type**: typing.Optional[str]

### ApplicationArn
- **Type**: typing.Optional[str]


# ListCallerAccessGrantsRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### GrantScope
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### AllowedByApplication
- **Type**: typing.Optional[bool]


# ListCallerAccessGrantsRequestPaginate

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### GrantScope
- **Type**: typing.Optional[str]

### AllowedByApplication
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.PaginatorConfig]


# ListCallerAccessGrantsResult

### CallerAccessGrantsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.ListCallerAccessGrantsEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListJobsRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Active', 'Cancelled', 'Cancelling', 'Complete', 'Completing', 'Failed', 'Failing', 'New', 'Paused', 'Pausing', 'Preparing', 'Ready', 'Suspended']]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListJobsResult

### Jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.JobListDescriptor]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMultiRegionAccessPointsRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMultiRegionAccessPointsResult

### AccessPoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.MultiRegionAccessPointReport]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRegionalBucketsRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### OutpostId
- **Type**: typing.Optional[str]


# ListRegionalBucketsResult

### RegionalBucketList
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.RegionalBucket]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStorageLensConfigurationEntry

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### StorageLensArn
- **Type**: <class 'str'>
- **Required**: Yes

### HomeRegion
- **Type**: <class 'str'>
- **Required**: Yes

### IsEnabled
- **Type**: typing.Optional[bool]


# ListStorageLensConfigurationsRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStorageLensConfigurationsResult

### StorageLensConfigurationList
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.ListStorageLensConfigurationEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStorageLensGroupEntry

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### StorageLensGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### HomeRegion
- **Type**: <class 'str'>
- **Required**: Yes


# ListStorageLensGroupsRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStorageLensGroupsResult

### StorageLensGroupList
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.ListStorageLensGroupEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResult

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# MatchObjectAge

### DaysGreaterThan
- **Type**: typing.Optional[int]

### DaysLessThan
- **Type**: typing.Optional[int]


# MatchObjectSize

### BytesGreaterThan
- **Type**: typing.Optional[int]

### BytesLessThan
- **Type**: typing.Optional[int]


# Metrics

### Status
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### EventThreshold
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.ReplicationTimeValue]


# MultiRegionAccessPointPolicyDocument

### Established
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.EstablishedMultiRegionAccessPointPolicy]

### Proposed
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.ProposedMultiRegionAccessPointPolicy]


# MultiRegionAccessPointRegionalResponse

### Name
- **Type**: typing.Optional[str]

### RequestStatus
- **Type**: typing.Optional[str]


# MultiRegionAccessPointReport

### Name
- **Type**: typing.Optional[str]

### Alias
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### PublicAccessBlock
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.PublicAccessBlockConfiguration]

### Status
- **Type**: typing.Optional[typing.Literal['CREATING', 'DELETING', 'INCONSISTENT_ACROSS_REGIONS', 'PARTIALLY_CREATED', 'PARTIALLY_DELETED', 'READY']]

### Regions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.s3control_classes.RegionReport]]


# MultiRegionAccessPointRoute

### TrafficDialPercentage
- **Type**: <class 'int'>
- **Required**: Yes

### Bucket
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]


# MultiRegionAccessPointsAsyncResponse

### Regions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.s3control_classes.MultiRegionAccessPointRegionalResponse]]


# NoncurrentVersionExpiration

### NoncurrentDays
- **Type**: typing.Optional[int]

### NewerNoncurrentVersions
- **Type**: typing.Optional[int]


# NoncurrentVersionTransition

### NoncurrentDays
- **Type**: typing.Optional[int]

### StorageClass
- **Type**: typing.Optional[typing.Literal['DEEP_ARCHIVE', 'GLACIER', 'INTELLIGENT_TIERING', 'ONEZONE_IA', 'STANDARD_IA']]


# ObjectLambdaAccessPoint

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectLambdaAccessPointArn
- **Type**: typing.Optional[str]

### Alias
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.ObjectLambdaAccessPointAlias]


# ObjectLambdaAccessPointAlias

### Value
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['PROVISIONING', 'READY']]


# ObjectLambdaConfiguration

### SupportingAccessPoint
- **Type**: <class 'str'>
- **Required**: Yes

### TransformationConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.ObjectLambdaTransformationConfiguration]
- **Required**: Yes

### CloudWatchMetricsEnabled
- **Type**: typing.Optional[bool]

### AllowedFeatures
- **Type**: typing.Optional[typing.Sequence[typing.Literal['GetObject-PartNumber', 'GetObject-Range', 'HeadObject-PartNumber', 'HeadObject-Range']]]


# ObjectLambdaConfigurationOutput

### SupportingAccessPoint
- **Type**: <class 'str'>
- **Required**: Yes

### TransformationConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.ObjectLambdaTransformationConfigurationOutput]
- **Required**: Yes

### CloudWatchMetricsEnabled
- **Type**: typing.Optional[bool]

### AllowedFeatures
- **Type**: typing.Optional[typing.List[typing.Literal['GetObject-PartNumber', 'GetObject-Range', 'HeadObject-PartNumber', 'HeadObject-Range']]]


# ObjectLambdaConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ObjectLambdaContentTransformation

### AwsLambda
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.AwsLambdaTransformation]


# ObjectLambdaTransformationConfiguration

### Actions
- **Type**: typing.Sequence[typing.Literal['GetObject', 'HeadObject', 'ListObjects', 'ListObjectsV2']]
- **Required**: Yes

### ContentTransformation
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ObjectLambdaContentTransformation'>
- **Required**: Yes


# ObjectLambdaTransformationConfigurationOutput

### Actions
- **Type**: typing.List[typing.Literal['GetObject', 'HeadObject', 'ListObjects', 'ListObjectsV2']]
- **Required**: Yes

### ContentTransformation
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ObjectLambdaContentTransformation'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PolicyStatus

### IsPublic
- **Type**: typing.Optional[bool]


# PrefixLevel

### StorageMetrics
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.PrefixLevelStorageMetrics'>
- **Required**: Yes


# PrefixLevelStorageMetrics

### IsEnabled
- **Type**: typing.Optional[bool]

### SelectionCriteria
- **Type**: <class 'NoneType'>


# ProposedMultiRegionAccessPointPolicy

### Policy
- **Type**: typing.Optional[str]


# PublicAccessBlockConfiguration

### BlockPublicAcls
- **Type**: typing.Optional[bool]

### IgnorePublicAcls
- **Type**: typing.Optional[bool]

### BlockPublicPolicy
- **Type**: typing.Optional[bool]

### RestrictPublicBuckets
- **Type**: typing.Optional[bool]


# PutAccessGrantsInstanceResourcePolicyRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### Organization
- **Type**: typing.Optional[str]


# PutAccessGrantsInstanceResourcePolicyResult

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### Organization
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# PutAccessPointConfigurationForObjectLambdaRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ObjectLambdaConfigurationUnion'>
- **Required**: Yes


# PutAccessPointPolicyForObjectLambdaRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# PutAccessPointPolicyRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# PutBucketLifecycleConfigurationRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### LifecycleConfiguration
- **Type**: <class 'NoneType'>


# PutBucketPolicyRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ConfirmRemoveSelfBucketAccess
- **Type**: typing.Optional[bool]


# PutBucketReplicationRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ReplicationConfigurationUnion'>
- **Required**: Yes


# PutBucketTaggingRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Tagging
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.Tagging'>
- **Required**: Yes


# PutBucketVersioningRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### VersioningConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.VersioningConfiguration'>
- **Required**: Yes

### MFA
- **Type**: typing.Optional[str]


# PutJobTaggingRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.S3Tag]
- **Required**: Yes


# PutMultiRegionAccessPointPolicyInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# PutMultiRegionAccessPointPolicyRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### Details
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.PutMultiRegionAccessPointPolicyInput'>
- **Required**: Yes


# PutMultiRegionAccessPointPolicyResult

### RequestTokenARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# PutPublicAccessBlockRequest

### PublicAccessBlockConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.PublicAccessBlockConfiguration'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# PutStorageLensConfigurationRequest

### ConfigId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### StorageLensConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.StorageLensConfigurationUnion'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.StorageLensTag]]


# PutStorageLensConfigurationTaggingRequest

### ConfigId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.StorageLensTag]
- **Required**: Yes


# Region

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### BucketAccountId
- **Type**: typing.Optional[str]


# RegionReport

### Bucket
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### BucketAccountId
- **Type**: typing.Optional[str]


# RegionalBucket

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### PublicAccessBlockEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### BucketArn
- **Type**: typing.Optional[str]

### OutpostId
- **Type**: typing.Optional[str]


# ReplicaModifications

### Status
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes


# ReplicationConfiguration

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### Rules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.ReplicationRule]
- **Required**: Yes


# ReplicationConfigurationOutput

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.ReplicationRuleOutput]
- **Required**: Yes


# ReplicationConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ReplicationRule

### Status
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.Destination'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### ID
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[int]

### Prefix
- **Type**: typing.Optional[str]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.ReplicationRuleFilter]

### SourceSelectionCriteria
- **Type**: <class 'NoneType'>

### ExistingObjectReplication
- **Type**: <class 'NoneType'>

### DeleteMarkerReplication
- **Type**: <class 'NoneType'>


# ReplicationRuleAndOperator

### Prefix
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.S3Tag]]


# ReplicationRuleAndOperatorOutput

### Prefix
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.s3control_classes.S3Tag]]


# ReplicationRuleFilter

### Prefix
- **Type**: typing.Optional[str]

### Tag
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3Tag]

### And
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.ReplicationRuleAndOperator]


# ReplicationRuleFilterOutput

### Prefix
- **Type**: typing.Optional[str]

### Tag
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3Tag]

### And
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.ReplicationRuleAndOperatorOutput]


# ReplicationRuleOutput

### Status
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.Destination'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### ID
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[int]

### Prefix
- **Type**: typing.Optional[str]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.ReplicationRuleFilterOutput]

### SourceSelectionCriteria
- **Type**: <class 'NoneType'>

### ExistingObjectReplication
- **Type**: <class 'NoneType'>

### DeleteMarkerReplication
- **Type**: <class 'NoneType'>


# ReplicationTime

### Status
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### Time
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ReplicationTimeValue'>
- **Required**: Yes


# ReplicationTimeValue

### Minutes
- **Type**: typing.Optional[int]


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


# S3AccessControlList

### Owner
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.S3ObjectOwner'>
- **Required**: Yes

### Grants
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.S3Grant]]


# S3AccessControlListOutput

### Owner
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.S3ObjectOwner'>
- **Required**: Yes

### Grants
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.s3control_classes.S3Grant]]


# S3AccessControlPolicy

### AccessControlList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3AccessControlList]

### CannedAccessControlList
- **Type**: typing.Optional[typing.Literal['authenticated-read', 'aws-exec-read', 'bucket-owner-full-control', 'bucket-owner-read', 'private', 'public-read', 'public-read-write']]


# S3AccessControlPolicyOutput

### AccessControlList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3AccessControlListOutput]

### CannedAccessControlList
- **Type**: typing.Optional[typing.Literal['authenticated-read', 'aws-exec-read', 'bucket-owner-full-control', 'bucket-owner-read', 'private', 'public-read', 'public-read-write']]


# S3BucketDestination

### Format
- **Type**: typing.Literal['CSV', 'Parquet']
- **Required**: Yes

### OutputSchemaVersion
- **Type**: typing.Literal['V_1']
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Prefix
- **Type**: typing.Optional[str]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.StorageLensDataExportEncryption]


# S3BucketDestinationOutput

### Format
- **Type**: typing.Literal['CSV', 'Parquet']
- **Required**: Yes

### OutputSchemaVersion
- **Type**: typing.Literal['V_1']
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Prefix
- **Type**: typing.Optional[str]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.StorageLensDataExportEncryptionOutput]


# S3CopyObjectOperation

### TargetResource
- **Type**: typing.Optional[str]

### CannedAccessControlList
- **Type**: typing.Optional[typing.Literal['authenticated-read', 'aws-exec-read', 'bucket-owner-full-control', 'bucket-owner-read', 'private', 'public-read', 'public-read-write']]

### AccessControlGrants
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.S3Grant]]

### MetadataDirective
- **Type**: typing.Optional[typing.Literal['COPY', 'REPLACE']]

### ModifiedSinceConstraint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.Timestamp]

### NewObjectMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3ObjectMetadata]

### NewObjectTagging
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.S3Tag]]

### RedirectLocation
- **Type**: typing.Optional[str]

### RequesterPays
- **Type**: typing.Optional[bool]

### StorageClass
- **Type**: typing.Optional[typing.Literal['DEEP_ARCHIVE', 'GLACIER', 'GLACIER_IR', 'INTELLIGENT_TIERING', 'ONEZONE_IA', 'STANDARD', 'STANDARD_IA']]

### UnModifiedSinceConstraint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.Timestamp]

### SSEAwsKmsKeyId
- **Type**: typing.Optional[str]

### TargetKeyPrefix
- **Type**: typing.Optional[str]

### ObjectLockLegalHoldStatus
- **Type**: typing.Optional[typing.Literal['OFF', 'ON']]

### ObjectLockMode
- **Type**: typing.Optional[typing.Literal['COMPLIANCE', 'GOVERNANCE']]

### ObjectLockRetainUntilDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.Timestamp]

### BucketKeyEnabled
- **Type**: typing.Optional[bool]

### ChecksumAlgorithm
- **Type**: typing.Optional[typing.Literal['CRC32', 'CRC32C', 'CRC64NVME', 'SHA1', 'SHA256']]


# S3CopyObjectOperationOutput

### TargetResource
- **Type**: typing.Optional[str]

### CannedAccessControlList
- **Type**: typing.Optional[typing.Literal['authenticated-read', 'aws-exec-read', 'bucket-owner-full-control', 'bucket-owner-read', 'private', 'public-read', 'public-read-write']]

### AccessControlGrants
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.s3control_classes.S3Grant]]

### MetadataDirective
- **Type**: typing.Optional[typing.Literal['COPY', 'REPLACE']]

### ModifiedSinceConstraint
- **Type**: typing.Optional[datetime.datetime]

### NewObjectMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3ObjectMetadataOutput]

### NewObjectTagging
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.s3control_classes.S3Tag]]

### RedirectLocation
- **Type**: typing.Optional[str]

### RequesterPays
- **Type**: typing.Optional[bool]

### StorageClass
- **Type**: typing.Optional[typing.Literal['DEEP_ARCHIVE', 'GLACIER', 'GLACIER_IR', 'INTELLIGENT_TIERING', 'ONEZONE_IA', 'STANDARD', 'STANDARD_IA']]

### UnModifiedSinceConstraint
- **Type**: typing.Optional[datetime.datetime]

### SSEAwsKmsKeyId
- **Type**: typing.Optional[str]

### TargetKeyPrefix
- **Type**: typing.Optional[str]

### ObjectLockLegalHoldStatus
- **Type**: typing.Optional[typing.Literal['OFF', 'ON']]

### ObjectLockMode
- **Type**: typing.Optional[typing.Literal['COMPLIANCE', 'GOVERNANCE']]

### ObjectLockRetainUntilDate
- **Type**: typing.Optional[datetime.datetime]

### BucketKeyEnabled
- **Type**: typing.Optional[bool]

### ChecksumAlgorithm
- **Type**: typing.Optional[typing.Literal['CRC32', 'CRC32C', 'CRC64NVME', 'SHA1', 'SHA256']]


# S3GeneratedManifestDescriptor

### Format
- **Type**: typing.Optional[typing.Literal['S3InventoryReport_CSV_20211130']]

### Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.JobManifestLocation]


# S3Grant

### Grantee
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3Grantee]

### Permission
- **Type**: typing.Optional[typing.Literal['FULL_CONTROL', 'READ', 'READ_ACP', 'WRITE', 'WRITE_ACP']]


# S3Grantee

### TypeIdentifier
- **Type**: typing.Optional[typing.Literal['emailAddress', 'id', 'uri']]

### Identifier
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]


# S3InitiateRestoreObjectOperation

### ExpirationInDays
- **Type**: typing.Optional[int]

### GlacierJobTier
- **Type**: typing.Optional[typing.Literal['BULK', 'STANDARD']]


# S3JobManifestGenerator

### SourceBucket
- **Type**: <class 'str'>
- **Required**: Yes

### EnableManifestOutput
- **Type**: <class 'bool'>
- **Required**: Yes

### ExpectedBucketOwner
- **Type**: typing.Optional[str]

### ManifestOutputLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3ManifestOutputLocation]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.JobManifestGeneratorFilter]


# S3JobManifestGeneratorOutput

### SourceBucket
- **Type**: <class 'str'>
- **Required**: Yes

### EnableManifestOutput
- **Type**: <class 'bool'>
- **Required**: Yes

### ExpectedBucketOwner
- **Type**: typing.Optional[str]

### ManifestOutputLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3ManifestOutputLocationOutput]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.JobManifestGeneratorFilterOutput]


# S3ManifestOutputLocation

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### ManifestFormat
- **Type**: typing.Literal['S3InventoryReport_CSV_20211130']
- **Required**: Yes

### ExpectedManifestBucketOwner
- **Type**: typing.Optional[str]

### ManifestPrefix
- **Type**: typing.Optional[str]

### ManifestEncryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.GeneratedManifestEncryption]


# S3ManifestOutputLocationOutput

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### ManifestFormat
- **Type**: typing.Literal['S3InventoryReport_CSV_20211130']
- **Required**: Yes

### ExpectedManifestBucketOwner
- **Type**: typing.Optional[str]

### ManifestPrefix
- **Type**: typing.Optional[str]

### ManifestEncryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.GeneratedManifestEncryptionOutput]


# S3ObjectLockLegalHold

### Status
- **Type**: typing.Literal['OFF', 'ON']
- **Required**: Yes


# S3ObjectMetadata

### CacheControl
- **Type**: typing.Optional[str]

### ContentDisposition
- **Type**: typing.Optional[str]

### ContentEncoding
- **Type**: typing.Optional[str]

### ContentLanguage
- **Type**: typing.Optional[str]

### UserMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ContentLength
- **Type**: typing.Optional[int]

### ContentMD5
- **Type**: typing.Optional[str]

### ContentType
- **Type**: typing.Optional[str]

### HttpExpiresDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.Timestamp]

### RequesterCharged
- **Type**: typing.Optional[bool]

### SSEAlgorithm
- **Type**: typing.Optional[typing.Literal['AES256', 'KMS']]


# S3ObjectMetadataOutput

### CacheControl
- **Type**: typing.Optional[str]

### ContentDisposition
- **Type**: typing.Optional[str]

### ContentEncoding
- **Type**: typing.Optional[str]

### ContentLanguage
- **Type**: typing.Optional[str]

### UserMetadata
- **Type**: typing.Optional[typing.Dict[str, str]]

### ContentLength
- **Type**: typing.Optional[int]

### ContentMD5
- **Type**: typing.Optional[str]

### ContentType
- **Type**: typing.Optional[str]

### HttpExpiresDate
- **Type**: typing.Optional[datetime.datetime]

### RequesterCharged
- **Type**: typing.Optional[bool]

### SSEAlgorithm
- **Type**: typing.Optional[typing.Literal['AES256', 'KMS']]


# S3ObjectOwner

### ID
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]


# S3Retention

### RetainUntilDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.Timestamp]

### Mode
- **Type**: typing.Optional[typing.Literal['COMPLIANCE', 'GOVERNANCE']]


# S3RetentionOutput

### RetainUntilDate
- **Type**: typing.Optional[datetime.datetime]

### Mode
- **Type**: typing.Optional[typing.Literal['COMPLIANCE', 'GOVERNANCE']]


# S3SetObjectAclOperation

### AccessControlPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3AccessControlPolicy]


# S3SetObjectAclOperationOutput

### AccessControlPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3AccessControlPolicyOutput]


# S3SetObjectLegalHoldOperation

### LegalHold
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.S3ObjectLockLegalHold'>
- **Required**: Yes


# S3SetObjectRetentionOperation

### Retention
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.S3Retention'>
- **Required**: Yes

### BypassGovernanceRetention
- **Type**: typing.Optional[bool]


# S3SetObjectRetentionOperationOutput

### Retention
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.S3RetentionOutput'>
- **Required**: Yes

### BypassGovernanceRetention
- **Type**: typing.Optional[bool]


# S3SetObjectTaggingOperation

### TagSet
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.S3Tag]]


# S3SetObjectTaggingOperationOutput

### TagSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.s3control_classes.S3Tag]]


# S3Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# SSEKMS

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes


# SSEKMSEncryption

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes


# SelectionCriteria

### Delimiter
- **Type**: typing.Optional[str]

### MaxDepth
- **Type**: typing.Optional[int]

### MinStorageBytesPercentage
- **Type**: typing.Optional[float]


# SourceSelectionCriteria

### SseKmsEncryptedObjects
- **Type**: <class 'NoneType'>

### ReplicaModifications
- **Type**: <class 'NoneType'>


# SseKmsEncryptedObjects

### Status
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes


# StorageLensAwsOrg

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# StorageLensConfiguration

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AccountLevel
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.AccountLevel'>
- **Required**: Yes

### IsEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Include
- **Type**: <class 'NoneType'>

### Exclude
- **Type**: <class 'NoneType'>

### DataExport
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.StorageLensDataExport]

### AwsOrg
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.StorageLensAwsOrg]

### StorageLensArn
- **Type**: typing.Optional[str]


# StorageLensConfigurationOutput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AccountLevel
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.AccountLevelOutput'>
- **Required**: Yes

### IsEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Include
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.IncludeOutput]

### Exclude
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.ExcludeOutput]

### DataExport
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.StorageLensDataExportOutput]

### AwsOrg
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.StorageLensAwsOrg]

### StorageLensArn
- **Type**: typing.Optional[str]


# StorageLensConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StorageLensDataExport

### S3BucketDestination
- **Type**: <class 'NoneType'>

### CloudWatchMetrics
- **Type**: <class 'NoneType'>


# StorageLensDataExportEncryption

### SSES3
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### SSEKMS
- **Type**: <class 'NoneType'>


# StorageLensDataExportEncryptionOutput

### SSES3
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### SSEKMS
- **Type**: <class 'NoneType'>


# StorageLensDataExportOutput

### S3BucketDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3BucketDestinationOutput]

### CloudWatchMetrics
- **Type**: <class 'NoneType'>


# StorageLensGroup

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.StorageLensGroupFilter'>
- **Required**: Yes

### StorageLensGroupArn
- **Type**: typing.Optional[str]


# StorageLensGroupAndOperator

### MatchAnyPrefix
- **Type**: typing.Optional[typing.Sequence[str]]

### MatchAnySuffix
- **Type**: typing.Optional[typing.Sequence[str]]

### MatchAnyTag
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.S3Tag]]

### MatchObjectAge
- **Type**: <class 'NoneType'>

### MatchObjectSize
- **Type**: <class 'NoneType'>


# StorageLensGroupAndOperatorOutput

### MatchAnyPrefix
- **Type**: typing.Optional[typing.List[str]]

### MatchAnySuffix
- **Type**: typing.Optional[typing.List[str]]

### MatchAnyTag
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.s3control_classes.S3Tag]]

### MatchObjectAge
- **Type**: <class 'NoneType'>

### MatchObjectSize
- **Type**: <class 'NoneType'>


# StorageLensGroupFilter

### MatchAnyPrefix
- **Type**: typing.Optional[typing.Sequence[str]]

### MatchAnySuffix
- **Type**: typing.Optional[typing.Sequence[str]]

### MatchAnyTag
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.S3Tag]]

### MatchObjectAge
- **Type**: <class 'NoneType'>

### MatchObjectSize
- **Type**: <class 'NoneType'>

### And
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.StorageLensGroupAndOperator]

### Or
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.StorageLensGroupOrOperator]


# StorageLensGroupFilterOutput

### MatchAnyPrefix
- **Type**: typing.Optional[typing.List[str]]

### MatchAnySuffix
- **Type**: typing.Optional[typing.List[str]]

### MatchAnyTag
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.s3control_classes.S3Tag]]

### MatchObjectAge
- **Type**: <class 'NoneType'>

### MatchObjectSize
- **Type**: <class 'NoneType'>

### And
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.StorageLensGroupAndOperatorOutput]

### Or
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.StorageLensGroupOrOperatorOutput]


# StorageLensGroupLevel

### SelectionCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.StorageLensGroupLevelSelectionCriteria]


# StorageLensGroupLevelOutput

### SelectionCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.StorageLensGroupLevelSelectionCriteriaOutput]


# StorageLensGroupLevelSelectionCriteria

### Include
- **Type**: typing.Optional[typing.Sequence[str]]

### Exclude
- **Type**: typing.Optional[typing.Sequence[str]]


# StorageLensGroupLevelSelectionCriteriaOutput

### Include
- **Type**: typing.Optional[typing.List[str]]

### Exclude
- **Type**: typing.Optional[typing.List[str]]


# StorageLensGroupOrOperator

### MatchAnyPrefix
- **Type**: typing.Optional[typing.Sequence[str]]

### MatchAnySuffix
- **Type**: typing.Optional[typing.Sequence[str]]

### MatchAnyTag
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.S3Tag]]

### MatchObjectAge
- **Type**: <class 'NoneType'>

### MatchObjectSize
- **Type**: <class 'NoneType'>


# StorageLensGroupOrOperatorOutput

### MatchAnyPrefix
- **Type**: typing.Optional[typing.List[str]]

### MatchAnySuffix
- **Type**: typing.Optional[typing.List[str]]

### MatchAnyTag
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.s3control_classes.S3Tag]]

### MatchObjectAge
- **Type**: <class 'NoneType'>

### MatchObjectSize
- **Type**: <class 'NoneType'>


# StorageLensGroupOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.StorageLensGroupFilterOutput'>
- **Required**: Yes

### StorageLensGroupArn
- **Type**: typing.Optional[str]


# StorageLensGroupUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StorageLensTag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# SubmitMultiRegionAccessPointRoutesRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Mrap
- **Type**: <class 'str'>
- **Required**: Yes

### RouteUpdates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.MultiRegionAccessPointRoute]
- **Required**: Yes


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.Tag]
- **Required**: Yes


# Tagging

### TagSet
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.S3Tag]
- **Required**: Yes


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Transition

### Date
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.Timestamp]

### Days
- **Type**: typing.Optional[int]

### StorageClass
- **Type**: typing.Optional[typing.Literal['DEEP_ARCHIVE', 'GLACIER', 'INTELLIGENT_TIERING', 'ONEZONE_IA', 'STANDARD_IA']]


# TransitionOutput

### Date
- **Type**: typing.Optional[datetime.datetime]

### Days
- **Type**: typing.Optional[int]

### StorageClass
- **Type**: typing.Optional[typing.Literal['DEEP_ARCHIVE', 'GLACIER', 'INTELLIGENT_TIERING', 'ONEZONE_IA', 'STANDARD_IA']]


# TransitionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAccessGrantsLocationRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantsLocationId
- **Type**: <class 'str'>
- **Required**: Yes

### IAMRoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateAccessGrantsLocationResult

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AccessGrantsLocationId
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantsLocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### LocationScope
- **Type**: <class 'str'>
- **Required**: Yes

### IAMRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateJobPriorityRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes


# UpdateJobPriorityResult

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateJobStatusRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### RequestedJobStatus
- **Type**: typing.Literal['Cancelled', 'Ready']
- **Required**: Yes

### StatusUpdateReason
- **Type**: typing.Optional[str]


# UpdateJobStatusResult

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Active', 'Cancelled', 'Cancelling', 'Complete', 'Completing', 'Failed', 'Failing', 'New', 'Paused', 'Pausing', 'Preparing', 'Ready', 'Suspended']
- **Required**: Yes

### StatusUpdateReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateStorageLensGroupRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### StorageLensGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.StorageLensGroupUnion'>
- **Required**: Yes


# VersioningConfiguration

### MFADelete
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### Status
- **Type**: typing.Optional[typing.Literal['Enabled', 'Suspended']]


# VpcConfiguration

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes


