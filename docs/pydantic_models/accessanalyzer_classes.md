# Accessanalyzer Classes

# AccessPreviewFindingTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AccessPreviewStatusReasonTypeDef

### code
- **Type**: typing.Literal['INTERNAL_ERROR', 'INVALID_CONFIGURATION']
- **Required**: Yes


# AccessPreviewSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AccessPreviewTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AccessTypeDef

### actions
- **Type**: typing.Optional[typing.Sequence[str]]

### resources
- **Type**: typing.Optional[typing.Sequence[str]]


# AclGranteeTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnalysisRuleCriteriaOutputTypeDef

### accountIds
- **Type**: typing.Optional[typing.List[str]]

### resourceTags
- **Type**: typing.Optional[typing.List[typing.Dict[str, str]]]


# AnalysisRuleCriteriaTypeDef

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### resourceTags
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, str]]]


# AnalysisRuleOutputTypeDef

### exclusions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.AnalysisRuleCriteriaOutputTypeDef]]


# AnalysisRuleTypeDef

### exclusions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.accessanalyzer_classes.AnalysisRuleCriteriaTypeDef]]


# AnalyzedResourceSummaryTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceOwnerAccount
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: typing.Literal['AWS::DynamoDB::Stream', 'AWS::DynamoDB::Table', 'AWS::EC2::Snapshot', 'AWS::ECR::Repository', 'AWS::EFS::FileSystem', 'AWS::IAM::Role', 'AWS::IAM::User', 'AWS::KMS::Key', 'AWS::Lambda::Function', 'AWS::Lambda::LayerVersion', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBSnapshot', 'AWS::S3::Bucket', 'AWS::S3Express::DirectoryBucket', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SecretsManager::Secret']
- **Required**: Yes


# AnalyzedResourceTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: typing.Literal['AWS::DynamoDB::Stream', 'AWS::DynamoDB::Table', 'AWS::EC2::Snapshot', 'AWS::ECR::Repository', 'AWS::EFS::FileSystem', 'AWS::IAM::Role', 'AWS::IAM::User', 'AWS::KMS::Key', 'AWS::Lambda::Function', 'AWS::Lambda::LayerVersion', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBSnapshot', 'AWS::S3::Bucket', 'AWS::S3Express::DirectoryBucket', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SecretsManager::Secret']
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


# AnalyzerConfigurationOutputTypeDef

### unusedAccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.UnusedAccessConfigurationOutputTypeDef]


# AnalyzerConfigurationTypeDef

### unusedAccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.UnusedAccessConfigurationTypeDef]


# AnalyzerConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnalyzerSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ApplyArchiveRuleRequestTypeDef

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### ruleName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# ArchiveRuleSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelPolicyGenerationRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# CheckAccessNotGrantedRequestTypeDef

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


# CheckNoNewAccessRequestTypeDef

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


# CheckNoPublicAccessRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.TimestampTypeDef'>
- **Required**: Yes

### endTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.TimestampTypeDef]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.EbsSnapshotConfigurationUnionTypeDef]

### ecrRepository
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.EcrRepositoryConfigurationTypeDef]

### iamRole
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.IamRoleConfigurationTypeDef]

### efsFileSystem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.EfsFileSystemConfigurationTypeDef]

### kmsKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.KmsKeyConfigurationUnionTypeDef]

### rdsDbClusterSnapshot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.RdsDbClusterSnapshotConfigurationUnionTypeDef]

### rdsDbSnapshot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.RdsDbSnapshotConfigurationUnionTypeDef]

### secretsManagerSecret
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.SecretsManagerSecretConfigurationTypeDef]

### s3Bucket
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.S3BucketConfigurationUnionTypeDef]

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


# ConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAccessPreviewRequestTypeDef

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### configurations
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.accessanalyzer_classes.ConfigurationUnionTypeDef]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreateAnalyzerResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# DeleteAnalyzerRequestTypeDef

### analyzerName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteArchiveRuleRequestTypeDef

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


# EbsSnapshotConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

### resourceControlPolicyRestriction
- **Type**: typing.Optional[typing.Literal['APPLICABLE', 'FAILED_TO_EVALUATE_RCP', 'NOT_APPLICABLE']]


# ExternalAccessFindingsStatisticsTypeDef

### resourceTypeStatistics
- **Type**: typing.Optional[typing.Dict[typing.Literal['AWS::DynamoDB::Stream', 'AWS::DynamoDB::Table', 'AWS::EC2::Snapshot', 'AWS::ECR::Repository', 'AWS::EFS::FileSystem', 'AWS::IAM::Role', 'AWS::IAM::User', 'AWS::KMS::Key', 'AWS::Lambda::Function', 'AWS::Lambda::LayerVersion', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBSnapshot', 'AWS::S3::Bucket', 'AWS::S3Express::DirectoryBucket', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SecretsManager::Secret'], aws_resource_validator.pydantic_models.accessanalyzer_classes.ResourceTypeDetailsTypeDef]]

### totalActiveFindings
- **Type**: typing.Optional[int]

### totalArchivedFindings
- **Type**: typing.Optional[int]

### totalResolvedFindings
- **Type**: typing.Optional[int]


# FindingAggregationAccountDetailsTypeDef

### account
- **Type**: typing.Optional[str]

### numberOfActiveFindings
- **Type**: typing.Optional[int]

### details
- **Type**: typing.Optional[typing.Dict[str, int]]


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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FindingSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FindingSummaryV2TypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FindingTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FindingsStatisticsTypeDef

### externalAccessFindingsStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.ExternalAccessFindingsStatisticsTypeDef]

### unusedAccessFindingsStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.UnusedAccessFindingsStatisticsTypeDef]


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


# GetAccessPreviewRequestTypeDef

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


# GetAnalyzedResourceRequestTypeDef

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


# GetAnalyzerRequestTypeDef

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


# GetArchiveRuleRequestTypeDef

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


# GetFindingRecommendationResponseTypeDef

### startedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### completedAt
- **Type**: <class 'datetime.datetime'>
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

### nextToken
- **Type**: typing.Optional[str]


# GetFindingResponseTypeDef

### finding
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.FindingTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFindingsStatisticsRequestTypeDef

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetFindingsStatisticsResponseTypeDef

### findingsStatistics
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.FindingsStatisticsTypeDef]
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGeneratedPolicyRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.KmsGrantConstraintsUnionTypeDef]


# KmsGrantConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# KmsGrantConstraintsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KmsKeyConfigurationOutputTypeDef

### keyPolicies
- **Type**: typing.Optional[typing.Dict[str, str]]

### grants
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.KmsGrantConfigurationOutputTypeDef]]


# KmsKeyConfigurationTypeDef

### keyPolicies
- **Type**: typing.Optional[typing.Mapping[str, str]]

### grants
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.accessanalyzer_classes.KmsGrantConfigurationUnionTypeDef]]


# KmsKeyConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListAccessPreviewFindingsResponseTypeDef

### findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.AccessPreviewFindingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAccessPreviewsRequestPaginateTypeDef

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.PaginatorConfigTypeDef]


# ListAccessPreviewsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAnalyzedResourcesRequestPaginateTypeDef

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: typing.Optional[typing.Literal['AWS::DynamoDB::Stream', 'AWS::DynamoDB::Table', 'AWS::EC2::Snapshot', 'AWS::ECR::Repository', 'AWS::EFS::FileSystem', 'AWS::IAM::Role', 'AWS::IAM::User', 'AWS::KMS::Key', 'AWS::Lambda::Function', 'AWS::Lambda::LayerVersion', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBSnapshot', 'AWS::S3::Bucket', 'AWS::S3Express::DirectoryBucket', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SecretsManager::Secret']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.PaginatorConfigTypeDef]


# ListAnalyzedResourcesRequestTypeDef

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: typing.Optional[typing.Literal['AWS::DynamoDB::Stream', 'AWS::DynamoDB::Table', 'AWS::EC2::Snapshot', 'AWS::ECR::Repository', 'AWS::EFS::FileSystem', 'AWS::IAM::Role', 'AWS::IAM::User', 'AWS::KMS::Key', 'AWS::Lambda::Function', 'AWS::Lambda::LayerVersion', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBSnapshot', 'AWS::S3::Bucket', 'AWS::S3Express::DirectoryBucket', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SecretsManager::Secret']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAnalyzedResourcesResponseTypeDef

### analyzedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.AnalyzedResourceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAnalyzersResponseTypeDef

### analyzers
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.AnalyzerSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListArchiveRulesRequestPaginateTypeDef

### analyzerName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.PaginatorConfigTypeDef]


# ListArchiveRulesRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFindingsResponseTypeDef

### findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.FindingSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFindingsV2ResponseTypeDef

### findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.FindingSummaryV2TypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPolicyGenerationsRequestPaginateTypeDef

### principalArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.PaginatorConfigTypeDef]


# ListPolicyGenerationsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
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


# NetworkOriginConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# RdsDbClusterSnapshotAttributeValueUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RdsDbClusterSnapshotConfigurationOutputTypeDef

### attributes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.accessanalyzer_classes.RdsDbClusterSnapshotAttributeValueOutputTypeDef]]

### kmsKeyId
- **Type**: typing.Optional[str]


# RdsDbClusterSnapshotConfigurationTypeDef

### attributes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.accessanalyzer_classes.RdsDbClusterSnapshotAttributeValueUnionTypeDef]]

### kmsKeyId
- **Type**: typing.Optional[str]


# RdsDbClusterSnapshotConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RdsDbSnapshotAttributeValueOutputTypeDef

### accountIds
- **Type**: typing.Optional[typing.List[str]]


# RdsDbSnapshotAttributeValueTypeDef

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]


# RdsDbSnapshotAttributeValueUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RdsDbSnapshotConfigurationOutputTypeDef

### attributes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.accessanalyzer_classes.RdsDbSnapshotAttributeValueOutputTypeDef]]

### kmsKeyId
- **Type**: typing.Optional[str]


# RdsDbSnapshotConfigurationTypeDef

### attributes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.accessanalyzer_classes.RdsDbSnapshotAttributeValueUnionTypeDef]]

### kmsKeyId
- **Type**: typing.Optional[str]


# RdsDbSnapshotConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# ResourceTypeDetailsTypeDef

### totalActivePublic
- **Type**: typing.Optional[int]

### totalActiveCrossAccount
- **Type**: typing.Optional[int]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.NetworkOriginConfigurationUnionTypeDef]


# S3AccessPointConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.accessanalyzer_classes.S3AccessPointConfigurationUnionTypeDef]]


# S3BucketConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# StartPolicyGenerationRequestTypeDef

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


# StartResourceScanRequestTypeDef

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


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UnusedAccessConfigurationOutputTypeDef

### unusedAccessAge
- **Type**: typing.Optional[int]

### analysisRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.AnalysisRuleOutputTypeDef]


# UnusedAccessConfigurationTypeDef

### unusedAccessAge
- **Type**: typing.Optional[int]

### analysisRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.AnalysisRuleTypeDef]


# UnusedAccessFindingsStatisticsTypeDef

### unusedAccessTypeStatistics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.UnusedAccessTypeStatisticsTypeDef]]

### topAccounts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.FindingAggregationAccountDetailsTypeDef]]

### totalActiveFindings
- **Type**: typing.Optional[int]

### totalArchivedFindings
- **Type**: typing.Optional[int]

### totalResolvedFindings
- **Type**: typing.Optional[int]


# UnusedAccessTypeStatisticsTypeDef

### unusedAccessType
- **Type**: typing.Optional[str]

### total
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


# UpdateAnalyzerRequestTypeDef

### analyzerName
- **Type**: <class 'str'>
- **Required**: Yes

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.AnalyzerConfigurationUnionTypeDef]


# UpdateAnalyzerResponseTypeDef

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.AnalyzerConfigurationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFindingsRequestTypeDef

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


# ValidatePolicyRequestPaginateTypeDef

### policyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### policyType
- **Type**: typing.Literal['IDENTITY_POLICY', 'RESOURCE_CONTROL_POLICY', 'RESOURCE_POLICY', 'SERVICE_CONTROL_POLICY']
- **Required**: Yes

### locale
- **Type**: typing.Optional[typing.Literal['DE', 'EN', 'ES', 'FR', 'IT', 'JA', 'KO', 'PT_BR', 'ZH_CN', 'ZH_TW']]

### validatePolicyResourceType
- **Type**: typing.Optional[typing.Literal['AWS::DynamoDB::Table', 'AWS::IAM::AssumeRolePolicyDocument', 'AWS::S3::AccessPoint', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3ObjectLambda::AccessPoint']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.PaginatorConfigTypeDef]


# ValidatePolicyRequestTypeDef

### policyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### policyType
- **Type**: typing.Literal['IDENTITY_POLICY', 'RESOURCE_CONTROL_POLICY', 'RESOURCE_POLICY', 'SERVICE_CONTROL_POLICY']
- **Required**: Yes

### locale
- **Type**: typing.Optional[typing.Literal['DE', 'EN', 'ES', 'FR', 'IT', 'JA', 'KO', 'PT_BR', 'ZH_CN', 'ZH_TW']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### validatePolicyResourceType
- **Type**: typing.Optional[typing.Literal['AWS::DynamoDB::Table', 'AWS::IAM::AssumeRolePolicyDocument', 'AWS::S3::AccessPoint', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3ObjectLambda::AccessPoint']]


# ValidatePolicyResponseTypeDef

### findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.ValidatePolicyFindingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# VpcConfigurationTypeDef

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes


