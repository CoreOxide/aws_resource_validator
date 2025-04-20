# Codeguru Reviewer Codeguru Reviewer Classes

# AssociateRepositoryRequest

### Repository
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.Repository'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### KMSKeyDetails
- **Type**: <class 'NoneType'>


# AssociateRepositoryResponse

### RepositoryAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.RepositoryAssociation'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.ResponseMetadata'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BranchDiffSourceCodeType

### SourceBranchName
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationBranchName
- **Type**: <class 'str'>
- **Required**: Yes


# CodeArtifacts

### SourceCodeArtifactsObjectKey
- **Type**: <class 'str'>
- **Required**: Yes

### BuildArtifactsObjectKey
- **Type**: typing.Optional[str]


# CodeCommitRepository

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# CodeReview

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
- **Type**: <class 'NoneType'>

### AssociationArn
- **Type**: typing.Optional[str]

### Metrics
- **Type**: <class 'NoneType'>

### AnalysisTypes
- **Type**: typing.Optional[typing.List[typing.Literal['CodeQuality', 'Security']]]

### ConfigFileState
- **Type**: typing.Optional[typing.Literal['Absent', 'Present', 'PresentWithErrors']]


# CodeReviewSummary

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
- **Type**: <class 'NoneType'>

### SourceCodeType
- **Type**: <class 'NoneType'>


# CodeReviewType

### RepositoryAnalysis
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.RepositoryAnalysis'>
- **Required**: Yes

### AnalysisTypes
- **Type**: typing.Optional[typing.List[typing.Literal['CodeQuality', 'Security']]]


# CommitDiffSourceCodeType

### SourceCommit
- **Type**: typing.Optional[str]

### DestinationCommit
- **Type**: typing.Optional[str]

### MergeBaseCommit
- **Type**: typing.Optional[str]


# CreateCodeReviewRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RepositoryAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.CodeReviewType'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# CreateCodeReviewResponse

### CodeReview
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.CodeReview'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCodeReviewRequest

### CodeReviewArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCodeReviewRequestWait

### CodeReviewArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeCodeReviewResponse

### CodeReview
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.CodeReview'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRecommendationFeedbackRequest

### CodeReviewArn
- **Type**: <class 'str'>
- **Required**: Yes

### RecommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: typing.Optional[str]


# DescribeRecommendationFeedbackResponse

### RecommendationFeedback
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.RecommendationFeedback'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRepositoryAssociationRequest

### AssociationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRepositoryAssociationRequestWait

### AssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeRepositoryAssociationResponse

### RepositoryAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.RepositoryAssociation'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateRepositoryRequest

### AssociationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateRepositoryResponse

### RepositoryAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.RepositoryAssociation'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.ResponseMetadata'>
- **Required**: Yes


# EventInfo

### Name
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]


# KMSKeyDetails

### KMSKeyId
- **Type**: typing.Optional[str]

### EncryptionOption
- **Type**: typing.Optional[typing.Literal['AWS_OWNED_CMK', 'CUSTOMER_MANAGED_CMK']]


# ListCodeReviewsRequest

### Type
- **Type**: typing.Literal['PullRequest', 'RepositoryAnalysis']
- **Required**: Yes

### ProviderTypes
- **Type**: typing.Optional[typing.List[typing.Literal['Bitbucket', 'CodeCommit', 'GitHub', 'GitHubEnterpriseServer', 'S3Bucket']]]

### States
- **Type**: typing.Optional[typing.List[typing.Literal['Completed', 'Deleting', 'Failed', 'Pending']]]

### RepositoryNames
- **Type**: typing.Optional[typing.List[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCodeReviewsResponse

### CodeReviewSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.CodeReviewSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRecommendationFeedbackRequest

### CodeReviewArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### UserIds
- **Type**: typing.Optional[typing.List[str]]

### RecommendationIds
- **Type**: typing.Optional[typing.List[str]]


# ListRecommendationFeedbackResponse

### RecommendationFeedbackSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.RecommendationFeedbackSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRecommendationsRequest

### CodeReviewArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListRecommendationsResponse

### RecommendationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.RecommendationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRepositoryAssociationsRequest

### ProviderTypes
- **Type**: typing.Optional[typing.List[typing.Literal['Bitbucket', 'CodeCommit', 'GitHub', 'GitHubEnterpriseServer', 'S3Bucket']]]

### States
- **Type**: typing.Optional[typing.List[typing.Literal['Associated', 'Associating', 'Disassociated', 'Disassociating', 'Failed']]]

### Names
- **Type**: typing.Optional[typing.List[str]]

### Owners
- **Type**: typing.Optional[typing.List[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRepositoryAssociationsRequestPaginate

### ProviderTypes
- **Type**: typing.Optional[typing.List[typing.Literal['Bitbucket', 'CodeCommit', 'GitHub', 'GitHubEnterpriseServer', 'S3Bucket']]]

### States
- **Type**: typing.Optional[typing.List[typing.Literal['Associated', 'Associating', 'Disassociated', 'Disassociating', 'Failed']]]

### Names
- **Type**: typing.Optional[typing.List[str]]

### Owners
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.PaginatorConfig]


# ListRepositoryAssociationsResponse

### RepositoryAssociationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.RepositoryAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.ResponseMetadata'>
- **Required**: Yes


# Metrics

### MeteredLinesOfCodeCount
- **Type**: typing.Optional[int]

### SuppressedLinesOfCodeCount
- **Type**: typing.Optional[int]

### FindingsCount
- **Type**: typing.Optional[int]


# MetricsSummary

### MeteredLinesOfCodeCount
- **Type**: typing.Optional[int]

### SuppressedLinesOfCodeCount
- **Type**: typing.Optional[int]

### FindingsCount
- **Type**: typing.Optional[int]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutRecommendationFeedbackRequest

### CodeReviewArn
- **Type**: <class 'str'>
- **Required**: Yes

### RecommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### Reactions
- **Type**: typing.List[typing.Literal['ThumbsDown', 'ThumbsUp']]
- **Required**: Yes


# RecommendationFeedback

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


# RecommendationFeedbackSummary

### RecommendationId
- **Type**: typing.Optional[str]

### Reactions
- **Type**: typing.Optional[typing.List[typing.Literal['ThumbsDown', 'ThumbsUp']]]

### UserId
- **Type**: typing.Optional[str]


# RecommendationSummary

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
- **Type**: <class 'NoneType'>

### Severity
- **Type**: typing.Optional[typing.Literal['Critical', 'High', 'Info', 'Low', 'Medium']]


# Repository

### CodeCommit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.CodeCommitRepository]

### Bitbucket
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.ThirdPartySourceRepository]

### GitHubEnterpriseServer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.ThirdPartySourceRepository]

### S3Bucket
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.S3Repository]


# RepositoryAnalysis

### RepositoryHead
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.RepositoryHeadSourceCodeType]

### SourceCodeType
- **Type**: <class 'NoneType'>


# RepositoryAssociation

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
- **Type**: <class 'NoneType'>

### S3RepositoryDetails
- **Type**: <class 'NoneType'>


# RepositoryAssociationSummary

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


# RepositoryHeadSourceCodeType

### BranchName
- **Type**: <class 'str'>
- **Required**: Yes


# RequestMetadata

### RequestId
- **Type**: typing.Optional[str]

### Requester
- **Type**: typing.Optional[str]

### EventInfo
- **Type**: <class 'NoneType'>

### VendorName
- **Type**: typing.Optional[typing.Literal['GitHub', 'GitLab', 'NativeS3']]


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


# RuleMetadata

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


# S3BucketRepository

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Details
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.S3RepositoryDetails]


# S3Repository

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes


# S3RepositoryDetails

### BucketName
- **Type**: typing.Optional[str]

### CodeArtifacts
- **Type**: <class 'NoneType'>


# SourceCodeType

### CommitDiff
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.CommitDiffSourceCodeType]

### RepositoryHead
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.RepositoryHeadSourceCodeType]

### BranchDiff
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_classes.BranchDiffSourceCodeType]

### S3BucketRepository
- **Type**: <class 'NoneType'>

### RequestMetadata
- **Type**: <class 'NoneType'>


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# ThirdPartySourceRepository

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Owner
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


