# Accessanalyzer Classes

# Access

### actions
- **Type**: typing.Optional[typing.Sequence[str]]

### resources
- **Type**: typing.Optional[typing.Sequence[str]]


# AccessPreview

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AccessPreviewFinding

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AccessPreviewStatusReason

### code
- **Type**: typing.Literal['INTERNAL_ERROR', 'INVALID_CONFIGURATION']
- **Required**: Yes


# AccessPreviewSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AclGrantee

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnalysisRule

### exclusions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.accessanalyzer_classes.AnalysisRuleCriteria]]


# AnalysisRuleCriteria

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### resourceTags
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, str]]]


# AnalysisRuleCriteriaOutput

### accountIds
- **Type**: typing.Optional[typing.List[str]]

### resourceTags
- **Type**: typing.Optional[typing.List[typing.Dict[str, str]]]


# AnalysisRuleOutput

### exclusions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.AnalysisRuleCriteriaOutput]]


# AnalyzedResource

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


# AnalyzedResourceSummary

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceOwnerAccount
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: typing.Literal['AWS::DynamoDB::Stream', 'AWS::DynamoDB::Table', 'AWS::EC2::Snapshot', 'AWS::ECR::Repository', 'AWS::EFS::FileSystem', 'AWS::IAM::Role', 'AWS::IAM::User', 'AWS::KMS::Key', 'AWS::Lambda::Function', 'AWS::Lambda::LayerVersion', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBSnapshot', 'AWS::S3::Bucket', 'AWS::S3Express::DirectoryBucket', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SecretsManager::Secret']
- **Required**: Yes


# AnalyzerConfiguration

### unusedAccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.UnusedAccessConfiguration]


# AnalyzerConfigurationOutput

### unusedAccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.UnusedAccessConfigurationOutput]


# AnalyzerConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnalyzerSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ApplyArchiveRuleRequest

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### ruleName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# ArchiveRuleSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelPolicyGenerationRequest

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# CheckAccessNotGrantedRequest

### policyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### access
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.accessanalyzer_classes.Access]
- **Required**: Yes

### policyType
- **Type**: typing.Literal['IDENTITY_POLICY', 'RESOURCE_POLICY']
- **Required**: Yes


# CheckAccessNotGrantedResponse

### result
- **Type**: typing.Literal['FAIL', 'PASS']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### reasons
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.ReasonSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadata'>
- **Required**: Yes


# CheckNoNewAccessRequest

### newPolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### existingPolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### policyType
- **Type**: typing.Literal['IDENTITY_POLICY', 'RESOURCE_POLICY']
- **Required**: Yes


# CheckNoNewAccessResponse

### result
- **Type**: typing.Literal['FAIL', 'PASS']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### reasons
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.ReasonSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadata'>
- **Required**: Yes


# CheckNoPublicAccessRequest

### policyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: typing.Literal['AWS::DynamoDB::Stream', 'AWS::DynamoDB::Table', 'AWS::EFS::FileSystem', 'AWS::IAM::AssumeRolePolicyDocument', 'AWS::KMS::Key', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::Lambda::Function', 'AWS::OpenSearchService::Domain', 'AWS::S3::AccessPoint', 'AWS::S3::Bucket', 'AWS::S3::Glacier', 'AWS::S3Express::DirectoryBucket', 'AWS::S3Outposts::AccessPoint', 'AWS::S3Outposts::Bucket', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SecretsManager::Secret']
- **Required**: Yes


# CheckNoPublicAccessResponse

### result
- **Type**: typing.Literal['FAIL', 'PASS']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### reasons
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.ReasonSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadata'>
- **Required**: Yes


# CloudTrailDetails

### trails
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.accessanalyzer_classes.Trail]
- **Required**: Yes

### accessRole
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.Timestamp'>
- **Required**: Yes

### endTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.Timestamp]


# CloudTrailProperties

### trailProperties
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.TrailProperties]
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# Configuration

### ebsSnapshot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.EbsSnapshotConfigurationUnion]

### ecrRepository
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.EcrRepositoryConfiguration]

### iamRole
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.IamRoleConfiguration]

### efsFileSystem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.EfsFileSystemConfiguration]

### kmsKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.KmsKeyConfigurationUnion]

### rdsDbClusterSnapshot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.RdsDbClusterSnapshotConfigurationUnion]

### rdsDbSnapshot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.RdsDbSnapshotConfigurationUnion]

### secretsManagerSecret
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.SecretsManagerSecretConfiguration]

### s3Bucket
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.S3BucketConfigurationUnion]

### snsTopic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.SnsTopicConfiguration]

### sqsQueue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.SqsQueueConfiguration]

### s3ExpressDirectoryBucket
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.S3ExpressDirectoryBucketConfiguration]

### dynamodbStream
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.DynamodbStreamConfiguration]

### dynamodbTable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.DynamodbTableConfiguration]


# ConfigurationOutput

### ebsSnapshot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.EbsSnapshotConfigurationOutput]

### ecrRepository
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.EcrRepositoryConfiguration]

### iamRole
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.IamRoleConfiguration]

### efsFileSystem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.EfsFileSystemConfiguration]

### kmsKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.KmsKeyConfigurationOutput]

### rdsDbClusterSnapshot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.RdsDbClusterSnapshotConfigurationOutput]

### rdsDbSnapshot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.RdsDbSnapshotConfigurationOutput]

### secretsManagerSecret
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.SecretsManagerSecretConfiguration]

### s3Bucket
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.S3BucketConfigurationOutput]

### snsTopic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.SnsTopicConfiguration]

### sqsQueue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.SqsQueueConfiguration]

### s3ExpressDirectoryBucket
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.S3ExpressDirectoryBucketConfiguration]

### dynamodbStream
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.DynamodbStreamConfiguration]

### dynamodbTable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.DynamodbTableConfiguration]


# ConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAccessPreviewRequest

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### configurations
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.accessanalyzer_classes.ConfigurationUnion]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreateAnalyzerResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadata'>
- **Required**: Yes


# Criterion

### eq
- **Type**: typing.Optional[typing.Sequence[str]]

### neq
- **Type**: typing.Optional[typing.Sequence[str]]

### contains
- **Type**: typing.Optional[typing.Sequence[str]]

### exists
- **Type**: typing.Optional[bool]


# CriterionOutput

### eq
- **Type**: typing.Optional[typing.List[str]]

### neq
- **Type**: typing.Optional[typing.List[str]]

### contains
- **Type**: typing.Optional[typing.List[str]]

### exists
- **Type**: typing.Optional[bool]


# DeleteAnalyzerRequest

### analyzerName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteArchiveRuleRequest

### analyzerName
- **Type**: <class 'str'>
- **Required**: Yes

### ruleName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DynamodbStreamConfiguration

### streamPolicy
- **Type**: typing.Optional[str]


# DynamodbTableConfiguration

### tablePolicy
- **Type**: typing.Optional[str]


# EbsSnapshotConfiguration

### userIds
- **Type**: typing.Optional[typing.Sequence[str]]

### groups
- **Type**: typing.Optional[typing.Sequence[str]]

### kmsKeyId
- **Type**: typing.Optional[str]


# EbsSnapshotConfigurationOutput

### userIds
- **Type**: typing.Optional[typing.List[str]]

### groups
- **Type**: typing.Optional[typing.List[str]]

### kmsKeyId
- **Type**: typing.Optional[str]


# EbsSnapshotConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EcrRepositoryConfiguration

### repositoryPolicy
- **Type**: typing.Optional[str]


# EfsFileSystemConfiguration

### fileSystemPolicy
- **Type**: typing.Optional[str]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadata'>
- **Required**: Yes


# ExternalAccessDetails

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.FindingSource]]

### resourceControlPolicyRestriction
- **Type**: typing.Optional[typing.Literal['APPLICABLE', 'FAILED_TO_EVALUATE_RCP', 'NOT_APPLICABLE']]


# ExternalAccessFindingsStatistics

### resourceTypeStatistics
- **Type**: typing.Optional[typing.Dict[typing.Literal['AWS::DynamoDB::Stream', 'AWS::DynamoDB::Table', 'AWS::EC2::Snapshot', 'AWS::ECR::Repository', 'AWS::EFS::FileSystem', 'AWS::IAM::Role', 'AWS::IAM::User', 'AWS::KMS::Key', 'AWS::Lambda::Function', 'AWS::Lambda::LayerVersion', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBSnapshot', 'AWS::S3::Bucket', 'AWS::S3Express::DirectoryBucket', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SecretsManager::Secret'], aws_resource_validator.pydantic_models.accessanalyzer_classes.ResourceTypeDetails]]

### totalActiveFindings
- **Type**: typing.Optional[int]

### totalArchivedFindings
- **Type**: typing.Optional[int]

### totalResolvedFindings
- **Type**: typing.Optional[int]


# Finding

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FindingAggregationAccountDetails

### account
- **Type**: typing.Optional[str]

### numberOfActiveFindings
- **Type**: typing.Optional[int]

### details
- **Type**: typing.Optional[typing.Dict[str, int]]


# FindingDetails

### externalAccessDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.ExternalAccessDetails]

### unusedPermissionDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.UnusedPermissionDetails]

### unusedIamUserAccessKeyDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.UnusedIamUserAccessKeyDetails]

### unusedIamRoleDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.UnusedIamRoleDetails]

### unusedIamUserPasswordDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.UnusedIamUserPasswordDetails]


# FindingSource

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FindingSourceDetail

### accessPointArn
- **Type**: typing.Optional[str]

### accessPointAccount
- **Type**: typing.Optional[str]


# FindingSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FindingSummaryV2

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FindingsStatistics

### externalAccessFindingsStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.ExternalAccessFindingsStatistics]

### unusedAccessFindingsStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.UnusedAccessFindingsStatistics]


# GeneratedPolicy

### policy
- **Type**: <class 'str'>
- **Required**: Yes


# GeneratedPolicyProperties

### principalArn
- **Type**: <class 'str'>
- **Required**: Yes

### isComplete
- **Type**: typing.Optional[bool]

### cloudTrailProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.CloudTrailProperties]


# GeneratedPolicyResult

### properties
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.GeneratedPolicyProperties'>
- **Required**: Yes

### generatedPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.GeneratedPolicy]]


# GetAccessPreviewRequest

### accessPreviewId
- **Type**: <class 'str'>
- **Required**: Yes

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessPreviewResponse

### accessPreview
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.AccessPreview'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadata'>
- **Required**: Yes


# GetAnalyzedResourceRequest

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetAnalyzedResourceResponse

### resource
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.AnalyzedResource'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadata'>
- **Required**: Yes


# GetAnalyzerRequest

### analyzerName
- **Type**: <class 'str'>
- **Required**: Yes


# GetAnalyzerResponse

### analyzer
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.AnalyzerSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadata'>
- **Required**: Yes


# GetArchiveRuleRequest

### analyzerName
- **Type**: <class 'str'>
- **Required**: Yes

### ruleName
- **Type**: <class 'str'>
- **Required**: Yes


# GetArchiveRuleResponse

### archiveRule
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ArchiveRuleSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadata'>
- **Required**: Yes


# GetFindingRecommendationResponse

### startedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### completedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### error
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.RecommendationError'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### recommendedSteps
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.RecommendedStep]
- **Required**: Yes

### recommendationType
- **Type**: typing.Literal['UnusedPermissionRecommendation']
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetFindingResponse

### finding
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.Finding'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadata'>
- **Required**: Yes


# GetFindingsStatisticsRequest

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetFindingsStatisticsResponse

### findingsStatistics
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.FindingsStatistics]
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadata'>
- **Required**: Yes


# GetGeneratedPolicyRequest

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### includeResourcePlaceholders
- **Type**: typing.Optional[bool]

### includeServiceLevelTemplate
- **Type**: typing.Optional[bool]


# GetGeneratedPolicyResponse

### jobDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.JobDetails'>
- **Required**: Yes

### generatedPolicyResult
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.GeneratedPolicyResult'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadata'>
- **Required**: Yes


# IamRoleConfiguration

### trustPolicy
- **Type**: typing.Optional[str]


# JobDetails

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.JobError]


# JobError

### code
- **Type**: typing.Literal['AUTHORIZATION_ERROR', 'RESOURCE_NOT_FOUND_ERROR', 'SERVICE_ERROR', 'SERVICE_QUOTA_EXCEEDED_ERROR']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# KmsGrantConfiguration

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.KmsGrantConstraintsUnion]


# KmsGrantConfigurationOutput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.KmsGrantConstraintsOutput]


# KmsGrantConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KmsGrantConstraints

### encryptionContextEquals
- **Type**: typing.Optional[typing.Mapping[str, str]]

### encryptionContextSubset
- **Type**: typing.Optional[typing.Mapping[str, str]]


# KmsGrantConstraintsOutput

### encryptionContextEquals
- **Type**: typing.Optional[typing.Dict[str, str]]

### encryptionContextSubset
- **Type**: typing.Optional[typing.Dict[str, str]]


# KmsGrantConstraintsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KmsKeyConfiguration

### keyPolicies
- **Type**: typing.Optional[typing.Mapping[str, str]]

### grants
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.accessanalyzer_classes.KmsGrantConfigurationUnion]]


# KmsKeyConfigurationOutput

### keyPolicies
- **Type**: typing.Optional[typing.Dict[str, str]]

### grants
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.KmsGrantConfigurationOutput]]


# KmsKeyConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListAccessPreviewFindingsResponse

### findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.AccessPreviewFinding]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAccessPreviewsRequest

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAccessPreviewsRequestPaginate

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.PaginatorConfig]


# ListAccessPreviewsResponse

### accessPreviews
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.AccessPreviewSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAnalyzedResourcesRequest

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: typing.Optional[typing.Literal['AWS::DynamoDB::Stream', 'AWS::DynamoDB::Table', 'AWS::EC2::Snapshot', 'AWS::ECR::Repository', 'AWS::EFS::FileSystem', 'AWS::IAM::Role', 'AWS::IAM::User', 'AWS::KMS::Key', 'AWS::Lambda::Function', 'AWS::Lambda::LayerVersion', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBSnapshot', 'AWS::S3::Bucket', 'AWS::S3Express::DirectoryBucket', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SecretsManager::Secret']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAnalyzedResourcesRequestPaginate

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: typing.Optional[typing.Literal['AWS::DynamoDB::Stream', 'AWS::DynamoDB::Table', 'AWS::EC2::Snapshot', 'AWS::ECR::Repository', 'AWS::EFS::FileSystem', 'AWS::IAM::Role', 'AWS::IAM::User', 'AWS::KMS::Key', 'AWS::Lambda::Function', 'AWS::Lambda::LayerVersion', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBSnapshot', 'AWS::S3::Bucket', 'AWS::S3Express::DirectoryBucket', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SecretsManager::Secret']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.PaginatorConfig]


# ListAnalyzedResourcesResponse

### analyzedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.AnalyzedResourceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAnalyzersResponse

### analyzers
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.AnalyzerSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListArchiveRulesRequest

### analyzerName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListArchiveRulesRequestPaginate

### analyzerName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.PaginatorConfig]


# ListArchiveRulesResponse

### archiveRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.ArchiveRuleSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFindingsResponse

### findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.FindingSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFindingsV2Response

### findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.FindingSummaryV2]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPolicyGenerationsRequest

### principalArn
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListPolicyGenerationsRequestPaginate

### principalArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.PaginatorConfig]


# ListPolicyGenerationsResponse

### policyGenerations
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.PolicyGeneration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadata'>
- **Required**: Yes


# Location

### path
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.PathElement]
- **Required**: Yes

### span
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.Span'>
- **Required**: Yes


# NetworkOriginConfiguration

### vpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.VpcConfiguration]

### internetConfiguration
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# NetworkOriginConfigurationOutput

### vpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.VpcConfiguration]

### internetConfiguration
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# NetworkOriginConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PathElement

### index
- **Type**: typing.Optional[int]

### key
- **Type**: typing.Optional[str]

### substring
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.Substring]

### value
- **Type**: typing.Optional[str]


# PolicyGeneration

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


# PolicyGenerationDetails

### principalArn
- **Type**: <class 'str'>
- **Required**: Yes


# Position

### line
- **Type**: <class 'int'>
- **Required**: Yes

### column
- **Type**: <class 'int'>
- **Required**: Yes

### offset
- **Type**: <class 'int'>
- **Required**: Yes


# RdsDbClusterSnapshotAttributeValue

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]


# RdsDbClusterSnapshotAttributeValueOutput

### accountIds
- **Type**: typing.Optional[typing.List[str]]


# RdsDbClusterSnapshotAttributeValueUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RdsDbClusterSnapshotConfiguration

### attributes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.accessanalyzer_classes.RdsDbClusterSnapshotAttributeValueUnion]]

### kmsKeyId
- **Type**: typing.Optional[str]


# RdsDbClusterSnapshotConfigurationOutput

### attributes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.accessanalyzer_classes.RdsDbClusterSnapshotAttributeValueOutput]]

### kmsKeyId
- **Type**: typing.Optional[str]


# RdsDbClusterSnapshotConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RdsDbSnapshotAttributeValue

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]


# RdsDbSnapshotAttributeValueOutput

### accountIds
- **Type**: typing.Optional[typing.List[str]]


# RdsDbSnapshotAttributeValueUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RdsDbSnapshotConfiguration

### attributes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.accessanalyzer_classes.RdsDbSnapshotAttributeValueUnion]]

### kmsKeyId
- **Type**: typing.Optional[str]


# RdsDbSnapshotConfigurationOutput

### attributes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.accessanalyzer_classes.RdsDbSnapshotAttributeValueOutput]]

### kmsKeyId
- **Type**: typing.Optional[str]


# RdsDbSnapshotConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ReasonSummary

### description
- **Type**: typing.Optional[str]

### statementIndex
- **Type**: typing.Optional[int]

### statementId
- **Type**: typing.Optional[str]


# RecommendationError

### code
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# RecommendedStep

### unusedPermissionsRecommendedStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.UnusedPermissionsRecommendedStep]


# ResourceTypeDetails

### totalActivePublic
- **Type**: typing.Optional[int]

### totalActiveCrossAccount
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


# S3AccessPointConfiguration

### accessPointPolicy
- **Type**: typing.Optional[str]

### publicAccessBlock
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.S3PublicAccessBlockConfiguration]

### networkOrigin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.NetworkOriginConfigurationUnion]


# S3AccessPointConfigurationOutput

### accessPointPolicy
- **Type**: typing.Optional[str]

### publicAccessBlock
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.S3PublicAccessBlockConfiguration]

### networkOrigin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.NetworkOriginConfigurationOutput]


# S3AccessPointConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# S3BucketAclGrantConfiguration

### permission
- **Type**: typing.Literal['FULL_CONTROL', 'READ', 'READ_ACP', 'WRITE', 'WRITE_ACP']
- **Required**: Yes

### grantee
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.AclGrantee'>
- **Required**: Yes


# S3BucketConfiguration

### bucketPolicy
- **Type**: typing.Optional[str]

### bucketAclGrants
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.accessanalyzer_classes.S3BucketAclGrantConfiguration]]

### bucketPublicAccessBlock
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.S3PublicAccessBlockConfiguration]

### accessPoints
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.accessanalyzer_classes.S3AccessPointConfigurationUnion]]


# S3BucketConfigurationOutput

### bucketPolicy
- **Type**: typing.Optional[str]

### bucketAclGrants
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.S3BucketAclGrantConfiguration]]

### bucketPublicAccessBlock
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.S3PublicAccessBlockConfiguration]

### accessPoints
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.accessanalyzer_classes.S3AccessPointConfigurationOutput]]


# S3BucketConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# S3ExpressDirectoryBucketConfiguration

### bucketPolicy
- **Type**: typing.Optional[str]


# S3PublicAccessBlockConfiguration

### ignorePublicAcls
- **Type**: <class 'bool'>
- **Required**: Yes

### restrictPublicBuckets
- **Type**: <class 'bool'>
- **Required**: Yes


# SecretsManagerSecretConfiguration

### kmsKeyId
- **Type**: typing.Optional[str]

### secretPolicy
- **Type**: typing.Optional[str]


# SnsTopicConfiguration

### topicPolicy
- **Type**: typing.Optional[str]


# SortCriteria

### attributeName
- **Type**: typing.Optional[str]

### orderBy
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# Span

### start
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.Position'>
- **Required**: Yes

### end
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.Position'>
- **Required**: Yes


# SqsQueueConfiguration

### queuePolicy
- **Type**: typing.Optional[str]


# StartPolicyGenerationRequest

### policyGenerationDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.PolicyGenerationDetails'>
- **Required**: Yes

### cloudTrailDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.CloudTrailDetails]

### clientToken
- **Type**: typing.Optional[str]


# StartPolicyGenerationResponse

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadata'>
- **Required**: Yes


# StartResourceScanRequest

### analyzerArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceOwnerAccount
- **Type**: typing.Optional[str]


# StatusReason

### code
- **Type**: typing.Literal['AWS_SERVICE_ACCESS_DISABLED', 'DELEGATED_ADMINISTRATOR_DEREGISTERED', 'ORGANIZATION_DELETED', 'SERVICE_LINKED_ROLE_CREATION_FAILED']
- **Required**: Yes


# Substring

### start
- **Type**: <class 'int'>
- **Required**: Yes

### length
- **Type**: <class 'int'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Trail

### cloudTrailArn
- **Type**: <class 'str'>
- **Required**: Yes

### regions
- **Type**: typing.Optional[typing.Sequence[str]]

### allRegions
- **Type**: typing.Optional[bool]


# TrailProperties

### cloudTrailArn
- **Type**: <class 'str'>
- **Required**: Yes

### regions
- **Type**: typing.Optional[typing.List[str]]

### allRegions
- **Type**: typing.Optional[bool]


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UnusedAccessConfiguration

### unusedAccessAge
- **Type**: typing.Optional[int]

### analysisRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.AnalysisRule]


# UnusedAccessConfigurationOutput

### unusedAccessAge
- **Type**: typing.Optional[int]

### analysisRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.AnalysisRuleOutput]


# UnusedAccessFindingsStatistics

### unusedAccessTypeStatistics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.UnusedAccessTypeStatistics]]

### topAccounts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.FindingAggregationAccountDetails]]

### totalActiveFindings
- **Type**: typing.Optional[int]

### totalArchivedFindings
- **Type**: typing.Optional[int]

### totalResolvedFindings
- **Type**: typing.Optional[int]


# UnusedAccessTypeStatistics

### unusedAccessType
- **Type**: typing.Optional[str]

### total
- **Type**: typing.Optional[int]


# UnusedAction

### action
- **Type**: <class 'str'>
- **Required**: Yes

### lastAccessed
- **Type**: typing.Optional[datetime.datetime]


# UnusedIamRoleDetails

### lastAccessed
- **Type**: typing.Optional[datetime.datetime]


# UnusedIamUserAccessKeyDetails

### accessKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### lastAccessed
- **Type**: typing.Optional[datetime.datetime]


# UnusedIamUserPasswordDetails

### lastAccessed
- **Type**: typing.Optional[datetime.datetime]


# UnusedPermissionDetails

### serviceNamespace
- **Type**: <class 'str'>
- **Required**: Yes

### actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.UnusedAction]]

### lastAccessed
- **Type**: typing.Optional[datetime.datetime]


# UnusedPermissionsRecommendedStep

### recommendedAction
- **Type**: typing.Literal['CREATE_POLICY', 'DETACH_POLICY']
- **Required**: Yes

### policyUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### recommendedPolicy
- **Type**: typing.Optional[str]

### existingPolicyId
- **Type**: typing.Optional[str]


# UpdateAnalyzerRequest

### analyzerName
- **Type**: <class 'str'>
- **Required**: Yes

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.AnalyzerConfigurationUnion]


# UpdateAnalyzerResponse

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.AnalyzerConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFindingsRequest

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


# ValidatePolicyFinding

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.Location]
- **Required**: Yes


# ValidatePolicyRequest

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


# ValidatePolicyRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.accessanalyzer_classes.PaginatorConfig]


# ValidatePolicyResponse

### findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.accessanalyzer_classes.ValidatePolicyFinding]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.accessanalyzer_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# VpcConfiguration

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes


