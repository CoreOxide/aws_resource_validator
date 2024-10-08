# Pydantic Models in codeguru_reviewer_classes

# AssociateRepositoryRequestRequestTypeDef

### Repository
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer_classes.RepositoryTypeDef'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### KMSKeyDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer_classes.KMSKeyDetailsTypeDef]


# AssociateRepositoryResponseTypeDef

### RepositoryAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer_classes.RepositoryAssociationTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BranchDiffSourceCodeTypeTypeDef

### SourceBranchName
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationBranchName
- **Type**: <class 'str'>
- **Required**: Yes


# CodeArtifactsTypeDef

### SourceCodeArtifactsObjectKey
- **Type**: <class 'str'>
- **Required**: Yes

### BuildArtifactsObjectKey
- **Type**: typing.Optional[str]


# CodeCommitRepositoryTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# CodeReviewSummaryTypeDef

### Name
- **Type**: typing.Optional[str]

### CodeReviewArn
- **Type**: typing.Optional[str]

### RepositoryName
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[str]

### ProviderType
- **Type**: typing.Optional[typing.Literal['Bitbucket', 'CodeCommit', 'GitHub', 'GitHubEnterpriseServer', 'S3Bucket']]

### State
- **Type**: typing.Optional[typing.Literal['Completed', 'Deleting', 'Failed', 'Pending']]

### CreatedTimeStamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTimeStamp
- **Type**: typing.Optional[datetime.datetime]

### Type
- **Type**: typing.Optional[typing.Literal['PullRequest', 'RepositoryAnalysis']]

### PullRequestId
- **Type**: typing.Optional[str]

### MetricsSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer_classes.MetricsSummaryTypeDef]

### SourceCodeType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer_classes.SourceCodeTypeTypeDef]


# CodeReviewTypeDef

### Name
- **Type**: typing.Optional[str]

### CodeReviewArn
- **Type**: typing.Optional[str]

### RepositoryName
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[str]

### ProviderType
- **Type**: typing.Optional[typing.Literal['Bitbucket', 'CodeCommit', 'GitHub', 'GitHubEnterpriseServer', 'S3Bucket']]

### State
- **Type**: typing.Optional[typing.Literal['Completed', 'Deleting', 'Failed', 'Pending']]

### StateReason
- **Type**: typing.Optional[str]

### CreatedTimeStamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTimeStamp
- **Type**: typing.Optional[datetime.datetime]

### Type
- **Type**: typing.Optional[typing.Literal['PullRequest', 'RepositoryAnalysis']]

### PullRequestId
- **Type**: typing.Optional[str]

### SourceCodeType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer_classes.SourceCodeTypeTypeDef]

### AssociationArn
- **Type**: typing.Optional[str]

### Metrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer_classes.MetricsTypeDef]

### AnalysisTypes
- **Type**: typing.Optional[typing.List[typing.Literal['CodeQuality', 'Security']]]

### ConfigFileState
- **Type**: typing.Optional[typing.Literal['Absent', 'Present', 'PresentWithErrors']]


# CodeReviewTypeTypeDef

### RepositoryAnalysis
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer_classes.RepositoryAnalysisTypeDef'>
- **Required**: Yes

### AnalysisTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CodeQuality', 'Security']]]


# CommitDiffSourceCodeTypeTypeDef

### SourceCommit
- **Type**: typing.Optional[str]

### DestinationCommit
- **Type**: typing.Optional[str]

### MergeBaseCommit
- **Type**: typing.Optional[str]


# CreateCodeReviewRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RepositoryAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer_classes.CodeReviewTypeTypeDef'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# CreateCodeReviewResponseTypeDef

### CodeReview
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer_classes.CodeReviewTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCodeReviewRequestCodeReviewCompletedWaitTypeDef

### CodeReviewArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer_classes.WaiterConfigTypeDef]


# DescribeCodeReviewRequestRequestTypeDef

### CodeReviewArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCodeReviewResponseTypeDef

### CodeReview
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer_classes.CodeReviewTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRecommendationFeedbackRequestRequestTypeDef

### CodeReviewArn
- **Type**: <class 'str'>
- **Required**: Yes

### RecommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: typing.Optional[str]


# DescribeRecommendationFeedbackResponseTypeDef

### RecommendationFeedback
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer_classes.RecommendationFeedbackTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRepositoryAssociationRequestRepositoryAssociationSucceededWaitTypeDef

### AssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer_classes.WaiterConfigTypeDef]


# DescribeRepositoryAssociationRequestRequestTypeDef

### AssociationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRepositoryAssociationResponseTypeDef

### RepositoryAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer_classes.RepositoryAssociationTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateRepositoryRequestRequestTypeDef

### AssociationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateRepositoryResponseTypeDef

### RepositoryAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer_classes.RepositoryAssociationTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EventInfoTypeDef

### Name
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]


# KMSKeyDetailsTypeDef

### KMSKeyId
- **Type**: typing.Optional[str]

### EncryptionOption
- **Type**: typing.Optional[typing.Literal['AWS_OWNED_CMK', 'CUSTOMER_MANAGED_CMK']]


# ListCodeReviewsRequestRequestTypeDef

### Type
- **Type**: typing.Literal['PullRequest', 'RepositoryAnalysis']
- **Required**: Yes

### ProviderTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Bitbucket', 'CodeCommit', 'GitHub', 'GitHubEnterpriseServer', 'S3Bucket']]]

### States
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Completed', 'Deleting', 'Failed', 'Pending']]]

### RepositoryNames
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCodeReviewsResponseTypeDef

### CodeReviewSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguru_reviewer_classes.CodeReviewSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRecommendationFeedbackRequestRequestTypeDef

### CodeReviewArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### UserIds
- **Type**: typing.Optional[typing.Sequence[str]]

### RecommendationIds
- **Type**: typing.Optional[typing.Sequence[str]]


# ListRecommendationFeedbackResponseTypeDef

### RecommendationFeedbackSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguru_reviewer_classes.RecommendationFeedbackSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRecommendationsRequestRequestTypeDef

### CodeReviewArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListRecommendationsResponseTypeDef

### RecommendationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguru_reviewer_classes.RecommendationSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRepositoryAssociationsRequestListRepositoryAssociationsPaginateTypeDef

### ProviderTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Bitbucket', 'CodeCommit', 'GitHub', 'GitHubEnterpriseServer', 'S3Bucket']]]

### States
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Associated', 'Associating', 'Disassociated', 'Disassociating', 'Failed']]]

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### Owners
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer_classes.PaginatorConfigTypeDef]


# ListRepositoryAssociationsRequestRequestTypeDef

### ProviderTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Bitbucket', 'CodeCommit', 'GitHub', 'GitHubEnterpriseServer', 'S3Bucket']]]

### States
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Associated', 'Associating', 'Disassociated', 'Disassociating', 'Failed']]]

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### Owners
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRepositoryAssociationsResponseTypeDef

### RepositoryAssociationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguru_reviewer_classes.RepositoryAssociationSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MetricsSummaryTypeDef

### MeteredLinesOfCodeCount
- **Type**: typing.Optional[int]

### SuppressedLinesOfCodeCount
- **Type**: typing.Optional[int]

### FindingsCount
- **Type**: typing.Optional[int]


# MetricsTypeDef

### MeteredLinesOfCodeCount
- **Type**: typing.Optional[int]

### SuppressedLinesOfCodeCount
- **Type**: typing.Optional[int]

### FindingsCount
- **Type**: typing.Optional[int]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutRecommendationFeedbackRequestRequestTypeDef

### CodeReviewArn
- **Type**: <class 'str'>
- **Required**: Yes

### RecommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### Reactions
- **Type**: typing.Sequence[typing.Literal['ThumbsDown', 'ThumbsUp']]
- **Required**: Yes


# RecommendationFeedbackSummaryTypeDef

### RecommendationId
- **Type**: typing.Optional[str]

### Reactions
- **Type**: typing.Optional[typing.List[typing.Literal['ThumbsDown', 'ThumbsUp']]]

### UserId
- **Type**: typing.Optional[str]


# RecommendationFeedbackTypeDef

### CodeReviewArn
- **Type**: typing.Optional[str]

### RecommendationId
- **Type**: typing.Optional[str]

### Reactions
- **Type**: typing.Optional[typing.List[typing.Literal['ThumbsDown', 'ThumbsUp']]]

### UserId
- **Type**: typing.Optional[str]

### CreatedTimeStamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTimeStamp
- **Type**: typing.Optional[datetime.datetime]


# RecommendationSummaryTypeDef

### FilePath
- **Type**: typing.Optional[str]

### RecommendationId
- **Type**: typing.Optional[str]

### StartLine
- **Type**: typing.Optional[int]

### EndLine
- **Type**: typing.Optional[int]

### Description
- **Type**: typing.Optional[str]

### RecommendationCategory
- **Type**: typing.Optional[typing.Literal['AWSBestPractices', 'AWSCloudFormationIssues', 'CodeInconsistencies', 'CodeMaintenanceIssues', 'ConcurrencyIssues', 'DuplicateCode', 'InputValidations', 'JavaBestPractices', 'PythonBestPractices', 'ResourceLeaks', 'SecurityIssues']]

### RuleMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer_classes.RuleMetadataTypeDef]

### Severity
- **Type**: typing.Optional[typing.Literal['Critical', 'High', 'Info', 'Low', 'Medium']]


# RepositoryAnalysisTypeDef

### RepositoryHead
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer_classes.RepositoryHeadSourceCodeTypeTypeDef]

### SourceCodeType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer_classes.SourceCodeTypeTypeDef]


# RepositoryAssociationSummaryTypeDef

### AssociationArn
- **Type**: typing.Optional[str]

### ConnectionArn
- **Type**: typing.Optional[str]

### LastUpdatedTimeStamp
- **Type**: typing.Optional[datetime.datetime]

### AssociationId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[str]

### ProviderType
- **Type**: typing.Optional[typing.Literal['Bitbucket', 'CodeCommit', 'GitHub', 'GitHubEnterpriseServer', 'S3Bucket']]

### State
- **Type**: typing.Optional[typing.Literal['Associated', 'Associating', 'Disassociated', 'Disassociating', 'Failed']]


# RepositoryAssociationTypeDef

### AssociationId
- **Type**: typing.Optional[str]

### AssociationArn
- **Type**: typing.Optional[str]

### ConnectionArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[str]

### ProviderType
- **Type**: typing.Optional[typing.Literal['Bitbucket', 'CodeCommit', 'GitHub', 'GitHubEnterpriseServer', 'S3Bucket']]

### State
- **Type**: typing.Optional[typing.Literal['Associated', 'Associating', 'Disassociated', 'Disassociating', 'Failed']]

### StateReason
- **Type**: typing.Optional[str]

### LastUpdatedTimeStamp
- **Type**: typing.Optional[datetime.datetime]

### CreatedTimeStamp
- **Type**: typing.Optional[datetime.datetime]

### KMSKeyDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer_classes.KMSKeyDetailsTypeDef]

### S3RepositoryDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer_classes.S3RepositoryDetailsTypeDef]


# RepositoryHeadSourceCodeTypeTypeDef

### BranchName
- **Type**: <class 'str'>
- **Required**: Yes


# RepositoryTypeDef

### CodeCommit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer_classes.CodeCommitRepositoryTypeDef]

### Bitbucket
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer_classes.ThirdPartySourceRepositoryTypeDef]

### GitHubEnterpriseServer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer_classes.ThirdPartySourceRepositoryTypeDef]

### S3Bucket
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer_classes.S3RepositoryTypeDef]


# RequestMetadataTypeDef

### RequestId
- **Type**: typing.Optional[str]

### Requester
- **Type**: typing.Optional[str]

### EventInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer_classes.EventInfoTypeDef]

### VendorName
- **Type**: typing.Optional[typing.Literal['GitHub', 'GitLab', 'NativeS3']]


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HostId
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


# RuleMetadataTypeDef

### RuleId
- **Type**: typing.Optional[str]

### RuleName
- **Type**: typing.Optional[str]

### ShortDescription
- **Type**: typing.Optional[str]

### LongDescription
- **Type**: typing.Optional[str]

### RuleTags
- **Type**: typing.Optional[typing.List[str]]


# S3BucketRepositoryTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Details
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer_classes.S3RepositoryDetailsTypeDef]


# S3RepositoryDetailsTypeDef

### BucketName
- **Type**: typing.Optional[str]

### CodeArtifacts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer_classes.CodeArtifactsTypeDef]


# S3RepositoryTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes


# SourceCodeTypeTypeDef

### CommitDiff
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer_classes.CommitDiffSourceCodeTypeTypeDef]

### RepositoryHead
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer_classes.RepositoryHeadSourceCodeTypeTypeDef]

### BranchDiff
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer_classes.BranchDiffSourceCodeTypeTypeDef]

### S3BucketRepository
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer_classes.S3BucketRepositoryTypeDef]

### RequestMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer_classes.RequestMetadataTypeDef]


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# ThirdPartySourceRepositoryTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Owner
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


