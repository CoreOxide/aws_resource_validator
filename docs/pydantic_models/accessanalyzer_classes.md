# Accessanalyzer Classes

# AccessPreviewFindingTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: typing.Literal['AWS::DynamoDB::Stream', 'AWS::DynamoDB::Table', 'AWS::EC2::Snapshot', 'AWS::ECR::Repository', 'AWS::EFS::FileSystem', 'AWS::IAM::Role', 'AWS::KMS::Key', 'AWS::Lambda::Function', 'AWS::Lambda::LayerVersion', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBSnapshot', 'AWS::S3::Bucket', 'AWS::S3Express::DirectoryBucket', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SecretsManager::Secret']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### changeType
- **Type**: typing.Literal['CHANGED', 'NEW', 'UNCHANGED']
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'ARCHIVED', 'RESOLVED']
- **Required**: Yes

### resourceOwnerAccount
- **Type**: <class 'str'>
- **Required**: Yes

### existingFindingId
- **Type**: typing.Optional[str]

### existingFindingStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ARCHIVED', 'RESOLVED']]

### principal
- **Type**: typing.Optional[typing.Dict[str, str]]

### action
- **Type**: typing.Optional[typing.List[str]]

### condition
- **Type**: typing.Optional[typing.Dict[str, str]]

### resource
- **Type**: typing.Optional[str]

### isPublic
- **Type**: typing.Optional[bool]

### error
- **Type**: typing.Optional[str]

### sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.FindingSourceTypeDef]]


# AccessPreviewStatusReasonTypeDef

### code
- **Type**: typing.Literal['INTERNAL_ERROR', 'INVALID_CONFIGURATION']
- **Required**: Yes


# AccessPreviewSummaryTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['COMPLETED', 'CREATING', 'FAILED']
- **Required**: Yes

### statusReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.AccessPreviewStatusReasonTypeDef]


# AccessPreviewTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### configurations
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.accessanalyzer_classes.ConfigurationOutputTypeDef]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['COMPLETED', 'CREATING', 'FAILED']
- **Required**: Yes

### statusReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.AccessPreviewStatusReasonTypeDef]


# AccessTypeDef

### actions
- **Type**: typing.Optional[typing.Sequence[str]]

### resources
- **Type**: typing.Optional[typing.Sequence[str]]


# AclGranteeTypeDef

### id
- **Type**: typing.Optional[str]

### uri
- **Type**: typing.Optional[str]


# AnalyzedResourceSummaryTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceOwnerAccount
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: typing.Literal['AWS::DynamoDB::Stream', 'AWS::DynamoDB::Table', 'AWS::EC2::Snapshot', 'AWS::ECR::Repository', 'AWS::EFS::FileSystem', 'AWS::IAM::Role', 'AWS::KMS::Key', 'AWS::Lambda::Function', 'AWS::Lambda::LayerVersion', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBSnapshot', 'AWS::S3::Bucket', 'AWS::S3Express::DirectoryBucket', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SecretsManager::Secret']
- **Required**: Yes


# AnalyzedResourceTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: typing.Literal['AWS::DynamoDB::Stream', 'AWS::DynamoDB::Table', 'AWS::EC2::Snapshot', 'AWS::ECR::Repository', 'AWS::EFS::FileSystem', 'AWS::IAM::Role', 'AWS::KMS::Key', 'AWS::Lambda::Function', 'AWS::Lambda::LayerVersion', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBSnapshot', 'AWS::S3::Bucket', 'AWS::S3Express::DirectoryBucket', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SecretsManager::Secret']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### analyzedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### isPublic
- **Type**: <class 'bool'>
- **Required**: Yes

### resourceOwnerAccount
- **Type**: <class 'str'>
- **Required**: Yes

### actions
- **Type**: typing.Optional[typing.List[str]]

### sharedVia
- **Type**: typing.Optional[typing.List[str]]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ARCHIVED', 'RESOLVED']]

### error
- **Type**: typing.Optional[str]


# AnalyzerConfigurationTypeDef

### unusedAccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.UnusedAccessConfigurationTypeDef]


# AnalyzerSummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['ACCOUNT', 'ACCOUNT_UNUSED_ACCESS', 'ORGANIZATION', 'ORGANIZATION_UNUSED_ACCESS']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DISABLED', 'FAILED']
- **Required**: Yes

### lastResourceAnalyzed
- **Type**: typing.Optional[str]

### lastResourceAnalyzedAt
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### statusReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.StatusReasonTypeDef]

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.AnalyzerConfigurationTypeDef]


# ApplyArchiveRuleRequestRequestTypeDef

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### ruleName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# ArchiveRuleSummaryTypeDef

### ruleName
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.accessanalyzer_classes.CriterionOutputTypeDef]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelPolicyGenerationRequestRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# CheckAccessNotGrantedRequestRequestTypeDef

### policyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### access
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.accessanalyzer_classes.AccessTypeDef]
- **Required**: Yes

### policyType
- **Type**: typing.Literal['IDENTITY_POLICY', 'RESOURCE_POLICY']
- **Required**: Yes


# CheckAccessNotGrantedResponseTypeDef

### result
- **Type**: typing.Literal['FAIL', 'PASS']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### reasons
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.ReasonSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CheckNoNewAccessRequestRequestTypeDef

### newPolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### existingPolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### policyType
- **Type**: typing.Literal['IDENTITY_POLICY', 'RESOURCE_POLICY']
- **Required**: Yes


# CheckNoNewAccessResponseTypeDef

### result
- **Type**: typing.Literal['FAIL', 'PASS']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### reasons
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.ReasonSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CheckNoPublicAccessRequestRequestTypeDef

### policyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: typing.Literal['AWS::DynamoDB::Stream', 'AWS::DynamoDB::Table', 'AWS::EFS::FileSystem', 'AWS::IAM::AssumeRolePolicyDocument', 'AWS::KMS::Key', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::Lambda::Function', 'AWS::OpenSearchService::Domain', 'AWS::S3::AccessPoint', 'AWS::S3::Bucket', 'AWS::S3::Glacier', 'AWS::S3Express::DirectoryBucket', 'AWS::S3Outposts::AccessPoint', 'AWS::S3Outposts::Bucket', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SecretsManager::Secret']
- **Required**: Yes


# CheckNoPublicAccessResponseTypeDef

### result
- **Type**: typing.Literal['FAIL', 'PASS']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### reasons
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.ReasonSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CloudTrailDetailsTypeDef

### trails
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.accessanalyzer_classes.TrailTypeDef]
- **Required**: Yes

### accessRole
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# CloudTrailPropertiesTypeDef

### trailProperties
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.TrailPropertiesTypeDef]
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ConfigurationOutputTypeDef

### ebsSnapshot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.EbsSnapshotConfigurationOutputTypeDef]

### ecrRepository
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.EcrRepositoryConfigurationTypeDef]

### iamRole
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.IamRoleConfigurationTypeDef]

### efsFileSystem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.EfsFileSystemConfigurationTypeDef]

### kmsKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.KmsKeyConfigurationOutputTypeDef]

### rdsDbClusterSnapshot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.RdsDbClusterSnapshotConfigurationOutputTypeDef]

### rdsDbSnapshot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.RdsDbSnapshotConfigurationOutputTypeDef]

### secretsManagerSecret
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.SecretsManagerSecretConfigurationTypeDef]

### s3Bucket
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.S3BucketConfigurationOutputTypeDef]

### snsTopic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.SnsTopicConfigurationTypeDef]

### sqsQueue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.SqsQueueConfigurationTypeDef]

### s3ExpressDirectoryBucket
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.S3ExpressDirectoryBucketConfigurationTypeDef]

### dynamodbStream
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.DynamodbStreamConfigurationTypeDef]

### dynamodbTable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.DynamodbTableConfigurationTypeDef]


# ConfigurationTypeDef

### ebsSnapshot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.EbsSnapshotConfigurationTypeDef]

### ecrRepository
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.EcrRepositoryConfigurationTypeDef]

### iamRole
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.IamRoleConfigurationTypeDef]

### efsFileSystem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.EfsFileSystemConfigurationTypeDef]

### kmsKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.KmsKeyConfigurationTypeDef]

### rdsDbClusterSnapshot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.RdsDbClusterSnapshotConfigurationTypeDef]

### rdsDbSnapshot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.RdsDbSnapshotConfigurationTypeDef]

### secretsManagerSecret
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.SecretsManagerSecretConfigurationTypeDef]

### s3Bucket
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.S3BucketConfigurationTypeDef]

### snsTopic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.SnsTopicConfigurationTypeDef]

### sqsQueue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.SqsQueueConfigurationTypeDef]

### s3ExpressDirectoryBucket
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.S3ExpressDirectoryBucketConfigurationTypeDef]

### dynamodbStream
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.DynamodbStreamConfigurationTypeDef]

### dynamodbTable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.DynamodbTableConfigurationTypeDef]


# CreateAccessPreviewRequestRequestTypeDef

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### configurations
- **Type**: typing.Mapping[str, typing.Union[aws_resource_validator.pydantic_models.accessanalyzer_classes.ConfigurationTypeDef, aws_resource_validator.pydantic_models.accessanalyzer_classes.ConfigurationOutputTypeDef]]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreateAccessPreviewResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAnalyzerRequestRequestTypeDef

### analyzerName
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['ACCOUNT', 'ACCOUNT_UNUSED_ACCESS', 'ORGANIZATION', 'ORGANIZATION_UNUSED_ACCESS']
- **Required**: Yes

### archiveRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.accessanalyzer_classes.InlineArchiveRuleTypeDef]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### clientToken
- **Type**: typing.Optional[str]

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.AnalyzerConfigurationTypeDef]


# CreateAnalyzerResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateArchiveRuleRequestRequestTypeDef

### analyzerName
- **Type**: <class 'str'>
- **Required**: Yes

### ruleName
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Mapping[str, typing.Union[aws_resource_validator.pydantic_models.accessanalyzer_classes.CriterionTypeDef, aws_resource_validator.pydantic_models.accessanalyzer_classes.CriterionExtraOutputTypeDef]]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CriterionExtraOutputTypeDef

### eq
- **Type**: typing.Optional[typing.List[str]]

### neq
- **Type**: typing.Optional[typing.List[str]]

### contains
- **Type**: typing.Optional[typing.List[str]]

### exists
- **Type**: typing.Optional[bool]


# CriterionOutputTypeDef

### eq
- **Type**: typing.Optional[typing.List[str]]

### neq
- **Type**: typing.Optional[typing.List[str]]

### contains
- **Type**: typing.Optional[typing.List[str]]

### exists
- **Type**: typing.Optional[bool]


# CriterionTypeDef

### eq
- **Type**: typing.Optional[typing.Sequence[str]]

### neq
- **Type**: typing.Optional[typing.Sequence[str]]

### contains
- **Type**: typing.Optional[typing.Sequence[str]]

### exists
- **Type**: typing.Optional[bool]


# DeleteAnalyzerRequestRequestTypeDef

### analyzerName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteArchiveRuleRequestRequestTypeDef

### analyzerName
- **Type**: <class 'str'>
- **Required**: Yes

### ruleName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DynamodbStreamConfigurationTypeDef

### streamPolicy
- **Type**: typing.Optional[str]


# DynamodbTableConfigurationTypeDef

### tablePolicy
- **Type**: typing.Optional[str]


# EbsSnapshotConfigurationOutputTypeDef

### userIds
- **Type**: typing.Optional[typing.List[str]]

### groups
- **Type**: typing.Optional[typing.List[str]]

### kmsKeyId
- **Type**: typing.Optional[str]


# EbsSnapshotConfigurationTypeDef

### userIds
- **Type**: typing.Optional[typing.Sequence[str]]

### groups
- **Type**: typing.Optional[typing.Sequence[str]]

### kmsKeyId
- **Type**: typing.Optional[str]


# EcrRepositoryConfigurationTypeDef

### repositoryPolicy
- **Type**: typing.Optional[str]


# EfsFileSystemConfigurationTypeDef

### fileSystemPolicy
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExternalAccessDetailsTypeDef

### condition
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### action
- **Type**: typing.Optional[typing.List[str]]

### isPublic
- **Type**: typing.Optional[bool]

### principal
- **Type**: typing.Optional[typing.Dict[str, str]]

### sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.FindingSourceTypeDef]]


# FindingDetailsTypeDef

### externalAccessDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.ExternalAccessDetailsTypeDef]

### unusedPermissionDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.UnusedPermissionDetailsTypeDef]

### unusedIamUserAccessKeyDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.UnusedIamUserAccessKeyDetailsTypeDef]

### unusedIamRoleDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.UnusedIamRoleDetailsTypeDef]

### unusedIamUserPasswordDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.UnusedIamUserPasswordDetailsTypeDef]


# FindingSourceDetailTypeDef

### accessPointArn
- **Type**: typing.Optional[str]

### accessPointAccount
- **Type**: typing.Optional[str]


# FindingSourceTypeDef

### type
- **Type**: typing.Literal['BUCKET_ACL', 'POLICY', 'S3_ACCESS_POINT', 'S3_ACCESS_POINT_ACCOUNT']
- **Required**: Yes

### detail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.FindingSourceDetailTypeDef]


# FindingSummaryTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: typing.Literal['AWS::DynamoDB::Stream', 'AWS::DynamoDB::Table', 'AWS::EC2::Snapshot', 'AWS::ECR::Repository', 'AWS::EFS::FileSystem', 'AWS::IAM::Role', 'AWS::KMS::Key', 'AWS::Lambda::Function', 'AWS::Lambda::LayerVersion', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBSnapshot', 'AWS::S3::Bucket', 'AWS::S3Express::DirectoryBucket', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SecretsManager::Secret']
- **Required**: Yes

### condition
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### analyzedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'ARCHIVED', 'RESOLVED']
- **Required**: Yes

### resourceOwnerAccount
- **Type**: <class 'str'>
- **Required**: Yes

### principal
- **Type**: typing.Optional[typing.Dict[str, str]]

### action
- **Type**: typing.Optional[typing.List[str]]

### resource
- **Type**: typing.Optional[str]

### isPublic
- **Type**: typing.Optional[bool]

### error
- **Type**: typing.Optional[str]

### sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.FindingSourceTypeDef]]


# FindingSummaryV2TypeDef

### analyzedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: typing.Literal['AWS::DynamoDB::Stream', 'AWS::DynamoDB::Table', 'AWS::EC2::Snapshot', 'AWS::ECR::Repository', 'AWS::EFS::FileSystem', 'AWS::IAM::Role', 'AWS::KMS::Key', 'AWS::Lambda::Function', 'AWS::Lambda::LayerVersion', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBSnapshot', 'AWS::S3::Bucket', 'AWS::S3Express::DirectoryBucket', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SecretsManager::Secret']
- **Required**: Yes

### resourceOwnerAccount
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'ARCHIVED', 'RESOLVED']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### error
- **Type**: typing.Optional[str]

### resource
- **Type**: typing.Optional[str]

### findingType
- **Type**: typing.Optional[typing.Literal['ExternalAccess', 'UnusedIAMRole', 'UnusedIAMUserAccessKey', 'UnusedIAMUserPassword', 'UnusedPermission']]


# FindingTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: typing.Literal['AWS::DynamoDB::Stream', 'AWS::DynamoDB::Table', 'AWS::EC2::Snapshot', 'AWS::ECR::Repository', 'AWS::EFS::FileSystem', 'AWS::IAM::Role', 'AWS::KMS::Key', 'AWS::Lambda::Function', 'AWS::Lambda::LayerVersion', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBSnapshot', 'AWS::S3::Bucket', 'AWS::S3Express::DirectoryBucket', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SecretsManager::Secret']
- **Required**: Yes

### condition
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### analyzedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'ARCHIVED', 'RESOLVED']
- **Required**: Yes

### resourceOwnerAccount
- **Type**: <class 'str'>
- **Required**: Yes

### principal
- **Type**: typing.Optional[typing.Dict[str, str]]

### action
- **Type**: typing.Optional[typing.List[str]]

### resource
- **Type**: typing.Optional[str]

### isPublic
- **Type**: typing.Optional[bool]

### error
- **Type**: typing.Optional[str]

### sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.FindingSourceTypeDef]]


# GenerateFindingRecommendationRequestRequestTypeDef

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GeneratedPolicyPropertiesTypeDef

### principalArn
- **Type**: <class 'str'>
- **Required**: Yes

### isComplete
- **Type**: typing.Optional[bool]

### cloudTrailProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.CloudTrailPropertiesTypeDef]


# GeneratedPolicyResultTypeDef

### properties
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.GeneratedPolicyPropertiesTypeDef'>
- **Required**: Yes

### generatedPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.GeneratedPolicyTypeDef]]


# GeneratedPolicyTypeDef

### policy
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessPreviewRequestRequestTypeDef

### accessPreviewId
- **Type**: <class 'str'>
- **Required**: Yes

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessPreviewResponseTypeDef

### accessPreview
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.AccessPreviewTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAnalyzedResourceRequestRequestTypeDef

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetAnalyzedResourceResponseTypeDef

### resource
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.AnalyzedResourceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAnalyzerRequestRequestTypeDef

### analyzerName
- **Type**: <class 'str'>
- **Required**: Yes


# GetAnalyzerResponseTypeDef

### analyzer
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.AnalyzerSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetArchiveRuleRequestRequestTypeDef

### analyzerName
- **Type**: <class 'str'>
- **Required**: Yes

### ruleName
- **Type**: <class 'str'>
- **Required**: Yes


# GetArchiveRuleResponseTypeDef

### archiveRule
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ArchiveRuleSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFindingRecommendationRequestGetFindingRecommendationPaginateTypeDef

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.PaginatorConfigTypeDef]


# GetFindingRecommendationRequestRequestTypeDef

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# GetFindingRecommendationResponseTypeDef

### startedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### completedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### error
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.RecommendationErrorTypeDef'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### recommendedSteps
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.RecommendedStepTypeDef]
- **Required**: Yes

### recommendationType
- **Type**: typing.Literal['UnusedPermissionRecommendation']
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFindingRequestRequestTypeDef

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetFindingResponseTypeDef

### finding
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.FindingTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFindingV2RequestGetFindingV2PaginateTypeDef

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.PaginatorConfigTypeDef]


# GetFindingV2RequestRequestTypeDef

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# GetFindingV2ResponseTypeDef

### analyzedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### error
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### resource
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: typing.Literal['AWS::DynamoDB::Stream', 'AWS::DynamoDB::Table', 'AWS::EC2::Snapshot', 'AWS::ECR::Repository', 'AWS::EFS::FileSystem', 'AWS::IAM::Role', 'AWS::KMS::Key', 'AWS::Lambda::Function', 'AWS::Lambda::LayerVersion', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBSnapshot', 'AWS::S3::Bucket', 'AWS::S3Express::DirectoryBucket', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SecretsManager::Secret']
- **Required**: Yes

### resourceOwnerAccount
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'ARCHIVED', 'RESOLVED']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### findingDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.FindingDetailsTypeDef]
- **Required**: Yes

### findingType
- **Type**: typing.Literal['ExternalAccess', 'UnusedIAMRole', 'UnusedIAMUserAccessKey', 'UnusedIAMUserPassword', 'UnusedPermission']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGeneratedPolicyRequestRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### includeResourcePlaceholders
- **Type**: typing.Optional[bool]

### includeServiceLevelTemplate
- **Type**: typing.Optional[bool]


# GetGeneratedPolicyResponseTypeDef

### jobDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.JobDetailsTypeDef'>
- **Required**: Yes

### generatedPolicyResult
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.GeneratedPolicyResultTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IamRoleConfigurationTypeDef

### trustPolicy
- **Type**: typing.Optional[str]


# InlineArchiveRuleTypeDef

### ruleName
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.accessanalyzer_classes.CriterionTypeDef]
- **Required**: Yes


# JobDetailsTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELED', 'FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### startedOn
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### completedOn
- **Type**: typing.Optional[datetime.datetime]

### jobError
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.JobErrorTypeDef]


# JobErrorTypeDef

### code
- **Type**: typing.Literal['AUTHORIZATION_ERROR', 'RESOURCE_NOT_FOUND_ERROR', 'SERVICE_ERROR', 'SERVICE_QUOTA_EXCEEDED_ERROR']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# KmsGrantConfigurationOutputTypeDef

### operations
- **Type**: typing.List[typing.Literal['CreateGrant', 'Decrypt', 'DescribeKey', 'Encrypt', 'GenerateDataKey', 'GenerateDataKeyPair', 'GenerateDataKeyPairWithoutPlaintext', 'GenerateDataKeyWithoutPlaintext', 'GetPublicKey', 'ReEncryptFrom', 'ReEncryptTo', 'RetireGrant', 'Sign', 'Verify']]
- **Required**: Yes

### granteePrincipal
- **Type**: <class 'str'>
- **Required**: Yes

### issuingAccount
- **Type**: <class 'str'>
- **Required**: Yes

### retiringPrincipal
- **Type**: typing.Optional[str]

### constraints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.KmsGrantConstraintsOutputTypeDef]


# KmsGrantConfigurationTypeDef

### operations
- **Type**: typing.Sequence[typing.Literal['CreateGrant', 'Decrypt', 'DescribeKey', 'Encrypt', 'GenerateDataKey', 'GenerateDataKeyPair', 'GenerateDataKeyPairWithoutPlaintext', 'GenerateDataKeyWithoutPlaintext', 'GetPublicKey', 'ReEncryptFrom', 'ReEncryptTo', 'RetireGrant', 'Sign', 'Verify']]
- **Required**: Yes

### granteePrincipal
- **Type**: <class 'str'>
- **Required**: Yes

### issuingAccount
- **Type**: <class 'str'>
- **Required**: Yes

### retiringPrincipal
- **Type**: typing.Optional[str]

### constraints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.KmsGrantConstraintsTypeDef]


# KmsGrantConstraintsOutputTypeDef

### encryptionContextEquals
- **Type**: typing.Optional[typing.Dict[str, str]]

### encryptionContextSubset
- **Type**: typing.Optional[typing.Dict[str, str]]


# KmsGrantConstraintsTypeDef

### encryptionContextEquals
- **Type**: typing.Optional[typing.Mapping[str, str]]

### encryptionContextSubset
- **Type**: typing.Optional[typing.Mapping[str, str]]


# KmsKeyConfigurationOutputTypeDef

### keyPolicies
- **Type**: typing.Optional[typing.Dict[str, str]]

### grants
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.KmsGrantConfigurationOutputTypeDef]]


# KmsKeyConfigurationTypeDef

### keyPolicies
- **Type**: typing.Optional[typing.Mapping[str, str]]

### grants
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.accessanalyzer_classes.KmsGrantConfigurationTypeDef]]


# ListAccessPreviewFindingsRequestListAccessPreviewFindingsPaginateTypeDef

### accessPreviewId
- **Type**: <class 'str'>
- **Required**: Yes

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[typing.Mapping[str, typing.Union[aws_resource_validator.pydantic_models.accessanalyzer_classes.CriterionTypeDef, aws_resource_validator.pydantic_models.accessanalyzer_classes.CriterionExtraOutputTypeDef]]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.PaginatorConfigTypeDef]


# ListAccessPreviewFindingsRequestRequestTypeDef

### accessPreviewId
- **Type**: <class 'str'>
- **Required**: Yes

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[typing.Mapping[str, typing.Union[aws_resource_validator.pydantic_models.accessanalyzer_classes.CriterionTypeDef, aws_resource_validator.pydantic_models.accessanalyzer_classes.CriterionExtraOutputTypeDef]]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAccessPreviewFindingsResponseTypeDef

### findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.AccessPreviewFindingTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAccessPreviewsRequestListAccessPreviewsPaginateTypeDef

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.PaginatorConfigTypeDef]


# ListAccessPreviewsRequestRequestTypeDef

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAccessPreviewsResponseTypeDef

### accessPreviews
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.AccessPreviewSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAnalyzedResourcesRequestListAnalyzedResourcesPaginateTypeDef

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: typing.Optional[typing.Literal['AWS::DynamoDB::Stream', 'AWS::DynamoDB::Table', 'AWS::EC2::Snapshot', 'AWS::ECR::Repository', 'AWS::EFS::FileSystem', 'AWS::IAM::Role', 'AWS::KMS::Key', 'AWS::Lambda::Function', 'AWS::Lambda::LayerVersion', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBSnapshot', 'AWS::S3::Bucket', 'AWS::S3Express::DirectoryBucket', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SecretsManager::Secret']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.PaginatorConfigTypeDef]


# ListAnalyzedResourcesRequestRequestTypeDef

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: typing.Optional[typing.Literal['AWS::DynamoDB::Stream', 'AWS::DynamoDB::Table', 'AWS::EC2::Snapshot', 'AWS::ECR::Repository', 'AWS::EFS::FileSystem', 'AWS::IAM::Role', 'AWS::KMS::Key', 'AWS::Lambda::Function', 'AWS::Lambda::LayerVersion', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBSnapshot', 'AWS::S3::Bucket', 'AWS::S3Express::DirectoryBucket', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SecretsManager::Secret']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAnalyzedResourcesResponseTypeDef

### analyzedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.AnalyzedResourceSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAnalyzersRequestListAnalyzersPaginateTypeDef

### type
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'ACCOUNT_UNUSED_ACCESS', 'ORGANIZATION', 'ORGANIZATION_UNUSED_ACCESS']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.PaginatorConfigTypeDef]


# ListAnalyzersRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### type
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'ACCOUNT_UNUSED_ACCESS', 'ORGANIZATION', 'ORGANIZATION_UNUSED_ACCESS']]


# ListAnalyzersResponseTypeDef

### analyzers
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.AnalyzerSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListArchiveRulesRequestListArchiveRulesPaginateTypeDef

### analyzerName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.PaginatorConfigTypeDef]


# ListArchiveRulesRequestRequestTypeDef

### analyzerName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListArchiveRulesResponseTypeDef

### archiveRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.ArchiveRuleSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFindingsRequestListFindingsPaginateTypeDef

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[typing.Mapping[str, typing.Union[aws_resource_validator.pydantic_models.accessanalyzer_classes.CriterionTypeDef, aws_resource_validator.pydantic_models.accessanalyzer_classes.CriterionExtraOutputTypeDef]]]

### sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.SortCriteriaTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.PaginatorConfigTypeDef]


# ListFindingsRequestRequestTypeDef

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[typing.Mapping[str, typing.Union[aws_resource_validator.pydantic_models.accessanalyzer_classes.CriterionTypeDef, aws_resource_validator.pydantic_models.accessanalyzer_classes.CriterionExtraOutputTypeDef]]]

### sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.SortCriteriaTypeDef]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListFindingsResponseTypeDef

### findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.FindingSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFindingsV2RequestListFindingsV2PaginateTypeDef

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[typing.Mapping[str, typing.Union[aws_resource_validator.pydantic_models.accessanalyzer_classes.CriterionTypeDef, aws_resource_validator.pydantic_models.accessanalyzer_classes.CriterionExtraOutputTypeDef]]]

### sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.SortCriteriaTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.PaginatorConfigTypeDef]


# ListFindingsV2RequestRequestTypeDef

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[typing.Mapping[str, typing.Union[aws_resource_validator.pydantic_models.accessanalyzer_classes.CriterionTypeDef, aws_resource_validator.pydantic_models.accessanalyzer_classes.CriterionExtraOutputTypeDef]]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.SortCriteriaTypeDef]


# ListFindingsV2ResponseTypeDef

### findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.FindingSummaryV2TypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPolicyGenerationsRequestListPolicyGenerationsPaginateTypeDef

### principalArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.PaginatorConfigTypeDef]


# ListPolicyGenerationsRequestRequestTypeDef

### principalArn
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListPolicyGenerationsResponseTypeDef

### policyGenerations
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.PolicyGenerationTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LocationTypeDef

### path
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.PathElementTypeDef]
- **Required**: Yes

### span
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.SpanTypeDef'>
- **Required**: Yes


# NetworkOriginConfigurationOutputTypeDef

### vpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.VpcConfigurationTypeDef]

### internetConfiguration
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# NetworkOriginConfigurationTypeDef

### vpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.VpcConfigurationTypeDef]

### internetConfiguration
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PathElementTypeDef

### index
- **Type**: typing.Optional[int]

### key
- **Type**: typing.Optional[str]

### substring
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.SubstringTypeDef]

### value
- **Type**: typing.Optional[str]


# PolicyGenerationDetailsTypeDef

### principalArn
- **Type**: <class 'str'>
- **Required**: Yes


# PolicyGenerationTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### principalArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELED', 'FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### startedOn
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### completedOn
- **Type**: typing.Optional[datetime.datetime]


# PositionTypeDef

### line
- **Type**: <class 'int'>
- **Required**: Yes

### column
- **Type**: <class 'int'>
- **Required**: Yes

### offset
- **Type**: <class 'int'>
- **Required**: Yes


# RdsDbClusterSnapshotAttributeValueOutputTypeDef

### accountIds
- **Type**: typing.Optional[typing.List[str]]


# RdsDbClusterSnapshotAttributeValueTypeDef

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]


# RdsDbClusterSnapshotConfigurationOutputTypeDef

### attributes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.accessanalyzer_classes.RdsDbClusterSnapshotAttributeValueOutputTypeDef]]

### kmsKeyId
- **Type**: typing.Optional[str]


# RdsDbClusterSnapshotConfigurationTypeDef

### attributes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.accessanalyzer_classes.RdsDbClusterSnapshotAttributeValueTypeDef]]

### kmsKeyId
- **Type**: typing.Optional[str]


# RdsDbSnapshotAttributeValueOutputTypeDef

### accountIds
- **Type**: typing.Optional[typing.List[str]]


# RdsDbSnapshotAttributeValueTypeDef

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]


# RdsDbSnapshotConfigurationOutputTypeDef

### attributes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.accessanalyzer_classes.RdsDbSnapshotAttributeValueOutputTypeDef]]

### kmsKeyId
- **Type**: typing.Optional[str]


# RdsDbSnapshotConfigurationTypeDef

### attributes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.accessanalyzer_classes.RdsDbSnapshotAttributeValueTypeDef]]

### kmsKeyId
- **Type**: typing.Optional[str]


# ReasonSummaryTypeDef

### description
- **Type**: typing.Optional[str]

### statementIndex
- **Type**: typing.Optional[int]

### statementId
- **Type**: typing.Optional[str]


# RecommendationErrorTypeDef

### code
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# RecommendedStepTypeDef

### unusedPermissionsRecommendedStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.UnusedPermissionsRecommendedStepTypeDef]


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


# S3AccessPointConfigurationOutputTypeDef

### accessPointPolicy
- **Type**: typing.Optional[str]

### publicAccessBlock
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.S3PublicAccessBlockConfigurationTypeDef]

### networkOrigin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.NetworkOriginConfigurationOutputTypeDef]


# S3AccessPointConfigurationTypeDef

### accessPointPolicy
- **Type**: typing.Optional[str]

### publicAccessBlock
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.S3PublicAccessBlockConfigurationTypeDef]

### networkOrigin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.NetworkOriginConfigurationTypeDef]


# S3BucketAclGrantConfigurationTypeDef

### permission
- **Type**: typing.Literal['FULL_CONTROL', 'READ', 'READ_ACP', 'WRITE', 'WRITE_ACP']
- **Required**: Yes

### grantee
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.AclGranteeTypeDef'>
- **Required**: Yes


# S3BucketConfigurationOutputTypeDef

### bucketPolicy
- **Type**: typing.Optional[str]

### bucketAclGrants
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.S3BucketAclGrantConfigurationTypeDef]]

### bucketPublicAccessBlock
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.S3PublicAccessBlockConfigurationTypeDef]

### accessPoints
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.accessanalyzer_classes.S3AccessPointConfigurationOutputTypeDef]]


# S3BucketConfigurationTypeDef

### bucketPolicy
- **Type**: typing.Optional[str]

### bucketAclGrants
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.accessanalyzer_classes.S3BucketAclGrantConfigurationTypeDef]]

### bucketPublicAccessBlock
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.S3PublicAccessBlockConfigurationTypeDef]

### accessPoints
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.accessanalyzer_classes.S3AccessPointConfigurationTypeDef]]


# S3ExpressDirectoryBucketConfigurationTypeDef

### bucketPolicy
- **Type**: typing.Optional[str]


# S3PublicAccessBlockConfigurationTypeDef

### ignorePublicAcls
- **Type**: <class 'bool'>
- **Required**: Yes

### restrictPublicBuckets
- **Type**: <class 'bool'>
- **Required**: Yes


# SecretsManagerSecretConfigurationTypeDef

### kmsKeyId
- **Type**: typing.Optional[str]

### secretPolicy
- **Type**: typing.Optional[str]


# SnsTopicConfigurationTypeDef

### topicPolicy
- **Type**: typing.Optional[str]


# SortCriteriaTypeDef

### attributeName
- **Type**: typing.Optional[str]

### orderBy
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# SpanTypeDef

### start
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.PositionTypeDef'>
- **Required**: Yes

### end
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.PositionTypeDef'>
- **Required**: Yes


# SqsQueueConfigurationTypeDef

### queuePolicy
- **Type**: typing.Optional[str]


# StartPolicyGenerationRequestRequestTypeDef

### policyGenerationDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.PolicyGenerationDetailsTypeDef'>
- **Required**: Yes

### cloudTrailDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.CloudTrailDetailsTypeDef]

### clientToken
- **Type**: typing.Optional[str]


# StartPolicyGenerationResponseTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartResourceScanRequestRequestTypeDef

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceOwnerAccount
- **Type**: typing.Optional[str]


# StatusReasonTypeDef

### code
- **Type**: typing.Literal['AWS_SERVICE_ACCESS_DISABLED', 'DELEGATED_ADMINISTRATOR_DEREGISTERED', 'ORGANIZATION_DELETED', 'SERVICE_LINKED_ROLE_CREATION_FAILED']
- **Required**: Yes


# SubstringTypeDef

### start
- **Type**: <class 'int'>
- **Required**: Yes

### length
- **Type**: <class 'int'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TrailPropertiesTypeDef

### cloudTrailArn
- **Type**: <class 'str'>
- **Required**: Yes

### regions
- **Type**: typing.Optional[typing.List[str]]

### allRegions
- **Type**: typing.Optional[bool]


# TrailTypeDef

### cloudTrailArn
- **Type**: <class 'str'>
- **Required**: Yes

### regions
- **Type**: typing.Optional[typing.Sequence[str]]

### allRegions
- **Type**: typing.Optional[bool]


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UnusedAccessConfigurationTypeDef

### unusedAccessAge
- **Type**: typing.Optional[int]


# UnusedActionTypeDef

### action
- **Type**: <class 'str'>
- **Required**: Yes

### lastAccessed
- **Type**: typing.Optional[datetime.datetime]


# UnusedIamRoleDetailsTypeDef

### lastAccessed
- **Type**: typing.Optional[datetime.datetime]


# UnusedIamUserAccessKeyDetailsTypeDef

### accessKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### lastAccessed
- **Type**: typing.Optional[datetime.datetime]


# UnusedIamUserPasswordDetailsTypeDef

### lastAccessed
- **Type**: typing.Optional[datetime.datetime]


# UnusedPermissionDetailsTypeDef

### serviceNamespace
- **Type**: <class 'str'>
- **Required**: Yes

### actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.UnusedActionTypeDef]]

### lastAccessed
- **Type**: typing.Optional[datetime.datetime]


# UnusedPermissionsRecommendedStepTypeDef

### recommendedAction
- **Type**: typing.Literal['CREATE_POLICY', 'DETACH_POLICY']
- **Required**: Yes

### policyUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### recommendedPolicy
- **Type**: typing.Optional[str]

### existingPolicyId
- **Type**: typing.Optional[str]


# UpdateArchiveRuleRequestRequestTypeDef

### analyzerName
- **Type**: <class 'str'>
- **Required**: Yes

### ruleName
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Mapping[str, typing.Union[aws_resource_validator.pydantic_models.accessanalyzer_classes.CriterionTypeDef, aws_resource_validator.pydantic_models.accessanalyzer_classes.CriterionExtraOutputTypeDef]]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# UpdateFindingsRequestRequestTypeDef

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'ARCHIVED']
- **Required**: Yes

### ids
- **Type**: typing.Optional[typing.Sequence[str]]

### resourceArn
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


# ValidatePolicyFindingTypeDef

### findingDetails
- **Type**: <class 'str'>
- **Required**: Yes

### findingType
- **Type**: typing.Literal['ERROR', 'SECURITY_WARNING', 'SUGGESTION', 'WARNING']
- **Required**: Yes

### issueCode
- **Type**: <class 'str'>
- **Required**: Yes

### learnMoreLink
- **Type**: <class 'str'>
- **Required**: Yes

### locations
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.LocationTypeDef]
- **Required**: Yes


# ValidatePolicyRequestRequestTypeDef

### policyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### policyType
- **Type**: typing.Literal['IDENTITY_POLICY', 'RESOURCE_POLICY', 'SERVICE_CONTROL_POLICY']
- **Required**: Yes

### locale
- **Type**: typing.Optional[typing.Literal['DE', 'EN', 'ES', 'FR', 'IT', 'JA', 'KO', 'PT_BR', 'ZH_CN', 'ZH_TW']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### validatePolicyResourceType
- **Type**: typing.Optional[typing.Literal['AWS::DynamoDB::Table', 'AWS::IAM::AssumeRolePolicyDocument', 'AWS::S3::AccessPoint', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3ObjectLambda::AccessPoint']]


# ValidatePolicyRequestValidatePolicyPaginateTypeDef

### policyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### policyType
- **Type**: typing.Literal['IDENTITY_POLICY', 'RESOURCE_POLICY', 'SERVICE_CONTROL_POLICY']
- **Required**: Yes

### locale
- **Type**: typing.Optional[typing.Literal['DE', 'EN', 'ES', 'FR', 'IT', 'JA', 'KO', 'PT_BR', 'ZH_CN', 'ZH_TW']]

### validatePolicyResourceType
- **Type**: typing.Optional[typing.Literal['AWS::DynamoDB::Table', 'AWS::IAM::AssumeRolePolicyDocument', 'AWS::S3::AccessPoint', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3ObjectLambda::AccessPoint']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.PaginatorConfigTypeDef]


# ValidatePolicyResponseTypeDef

### findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.ValidatePolicyFindingTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VpcConfigurationTypeDef

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes


