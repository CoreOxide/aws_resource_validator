# Mturk Classes

# AcceptQualificationRequestRequestTypeDef

### QualificationRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegerValue
- **Type**: typing.Optional[int]


# ApproveAssignmentRequestTypeDef

### AssignmentId
- **Type**: <class 'str'>
- **Required**: Yes

### RequesterFeedback
- **Type**: typing.Optional[str]

### OverrideRejection
- **Type**: typing.Optional[bool]


# AssignmentTypeDef

### AssignmentId
- **Type**: typing.Optional[str]

### WorkerId
- **Type**: typing.Optional[str]

### HITId
- **Type**: typing.Optional[str]

### AssignmentStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'Rejected', 'Submitted']]

### AutoApprovalTime
- **Type**: typing.Optional[datetime.datetime]

### AcceptTime
- **Type**: typing.Optional[datetime.datetime]

### SubmitTime
- **Type**: typing.Optional[datetime.datetime]

### ApprovalTime
- **Type**: typing.Optional[datetime.datetime]

### RejectionTime
- **Type**: typing.Optional[datetime.datetime]

### Deadline
- **Type**: typing.Optional[datetime.datetime]

### Answer
- **Type**: typing.Optional[str]

### RequesterFeedback
- **Type**: typing.Optional[str]


# AssociateQualificationWithWorkerRequestTypeDef

### QualificationTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkerId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegerValue
- **Type**: typing.Optional[int]

### SendNotification
- **Type**: typing.Optional[bool]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BonusPaymentTypeDef

### WorkerId
- **Type**: typing.Optional[str]

### BonusAmount
- **Type**: typing.Optional[str]

### AssignmentId
- **Type**: typing.Optional[str]

### Reason
- **Type**: typing.Optional[str]

### GrantTime
- **Type**: typing.Optional[datetime.datetime]


# CreateAdditionalAssignmentsForHITRequestTypeDef

### HITId
- **Type**: <class 'str'>
- **Required**: Yes

### NumberOfAdditionalAssignments
- **Type**: <class 'int'>
- **Required**: Yes

### UniqueRequestToken
- **Type**: typing.Optional[str]


# CreateHITRequestTypeDef

### LifetimeInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### AssignmentDurationInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### Reward
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### MaxAssignments
- **Type**: typing.Optional[int]

### AutoApprovalDelayInSeconds
- **Type**: typing.Optional[int]

### Keywords
- **Type**: typing.Optional[str]

### Question
- **Type**: typing.Optional[str]

### RequesterAnnotation
- **Type**: typing.Optional[str]

### QualificationRequirements
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mturk_classes.QualificationRequirementUnionTypeDef]]

### UniqueRequestToken
- **Type**: typing.Optional[str]

### AssignmentReviewPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mturk_classes.ReviewPolicyUnionTypeDef]

### HITReviewPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mturk_classes.ReviewPolicyUnionTypeDef]

### HITLayoutId
- **Type**: typing.Optional[str]

### HITLayoutParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mturk_classes.HITLayoutParameterTypeDef]]


# CreateHITResponseTypeDef

### HIT
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.HITTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateHITTypeRequestTypeDef

### AssignmentDurationInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### Reward
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### AutoApprovalDelayInSeconds
- **Type**: typing.Optional[int]

### Keywords
- **Type**: typing.Optional[str]

### QualificationRequirements
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mturk_classes.QualificationRequirementUnionTypeDef]]


# CreateHITTypeResponseTypeDef

### HITTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateHITWithHITTypeRequestTypeDef

### HITTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### LifetimeInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### MaxAssignments
- **Type**: typing.Optional[int]

### Question
- **Type**: typing.Optional[str]

### RequesterAnnotation
- **Type**: typing.Optional[str]

### UniqueRequestToken
- **Type**: typing.Optional[str]

### AssignmentReviewPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mturk_classes.ReviewPolicyUnionTypeDef]

### HITReviewPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mturk_classes.ReviewPolicyUnionTypeDef]

### HITLayoutId
- **Type**: typing.Optional[str]

### HITLayoutParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mturk_classes.HITLayoutParameterTypeDef]]


# CreateHITWithHITTypeResponseTypeDef

### HIT
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.HITTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateQualificationTypeRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### QualificationTypeStatus
- **Type**: typing.Literal['Active', 'Inactive']
- **Required**: Yes

### Keywords
- **Type**: typing.Optional[str]

### RetryDelayInSeconds
- **Type**: typing.Optional[int]

### Test
- **Type**: typing.Optional[str]

### AnswerKey
- **Type**: typing.Optional[str]

### TestDurationInSeconds
- **Type**: typing.Optional[int]

### AutoGranted
- **Type**: typing.Optional[bool]

### AutoGrantedValue
- **Type**: typing.Optional[int]


# CreateQualificationTypeResponseTypeDef

### QualificationType
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.QualificationTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWorkerBlockRequestTypeDef

### WorkerId
- **Type**: <class 'str'>
- **Required**: Yes

### Reason
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHITRequestTypeDef

### HITId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQualificationTypeRequestTypeDef

### QualificationTypeId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkerBlockRequestTypeDef

### WorkerId
- **Type**: <class 'str'>
- **Required**: Yes

### Reason
- **Type**: typing.Optional[str]


# DisassociateQualificationFromWorkerRequestTypeDef

### WorkerId
- **Type**: <class 'str'>
- **Required**: Yes

### QualificationTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### Reason
- **Type**: typing.Optional[str]


# GetAccountBalanceResponseTypeDef

### AvailableBalance
- **Type**: <class 'str'>
- **Required**: Yes

### OnHoldBalance
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAssignmentRequestTypeDef

### AssignmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAssignmentResponseTypeDef

### Assignment
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.AssignmentTypeDef'>
- **Required**: Yes

### HIT
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.HITTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFileUploadURLRequestTypeDef

### AssignmentId
- **Type**: <class 'str'>
- **Required**: Yes

### QuestionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetFileUploadURLResponseTypeDef

### FileUploadURL
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetHITRequestTypeDef

### HITId
- **Type**: <class 'str'>
- **Required**: Yes


# GetHITResponseTypeDef

### HIT
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.HITTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetQualificationScoreRequestTypeDef

### QualificationTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkerId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQualificationScoreResponseTypeDef

### Qualification
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.QualificationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetQualificationTypeRequestTypeDef

### QualificationTypeId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQualificationTypeResponseTypeDef

### QualificationType
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.QualificationTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HITLayoutParameterTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# HITTypeDef

### HITId
- **Type**: typing.Optional[str]

### HITTypeId
- **Type**: typing.Optional[str]

### HITGroupId
- **Type**: typing.Optional[str]

### HITLayoutId
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### Title
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Question
- **Type**: typing.Optional[str]

### Keywords
- **Type**: typing.Optional[str]

### HITStatus
- **Type**: typing.Optional[typing.Literal['Assignable', 'Disposed', 'Reviewable', 'Reviewing', 'Unassignable']]

### MaxAssignments
- **Type**: typing.Optional[int]

### Reward
- **Type**: typing.Optional[str]

### AutoApprovalDelayInSeconds
- **Type**: typing.Optional[int]

### Expiration
- **Type**: typing.Optional[datetime.datetime]

### AssignmentDurationInSeconds
- **Type**: typing.Optional[int]

### RequesterAnnotation
- **Type**: typing.Optional[str]

### QualificationRequirements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mturk_classes.QualificationRequirementOutputTypeDef]]

### HITReviewStatus
- **Type**: typing.Optional[typing.Literal['MarkedForReview', 'NotReviewed', 'ReviewedAppropriate', 'ReviewedInappropriate']]

### NumberOfAssignmentsPending
- **Type**: typing.Optional[int]

### NumberOfAssignmentsAvailable
- **Type**: typing.Optional[int]

### NumberOfAssignmentsCompleted
- **Type**: typing.Optional[int]


# ListAssignmentsForHITRequestPaginateTypeDef

### HITId
- **Type**: <class 'str'>
- **Required**: Yes

### AssignmentStatuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Approved', 'Rejected', 'Submitted']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mturk_classes.PaginatorConfigTypeDef]


# ListAssignmentsForHITRequestTypeDef

### HITId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### AssignmentStatuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Approved', 'Rejected', 'Submitted']]]


# ListAssignmentsForHITResponseTypeDef

### NumResults
- **Type**: <class 'int'>
- **Required**: Yes

### Assignments
- **Type**: typing.List[aws_resource_validator.pydantic_models.mturk_classes.AssignmentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListBonusPaymentsRequestPaginateTypeDef

### HITId
- **Type**: typing.Optional[str]

### AssignmentId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mturk_classes.PaginatorConfigTypeDef]


# ListBonusPaymentsRequestTypeDef

### HITId
- **Type**: typing.Optional[str]

### AssignmentId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListBonusPaymentsResponseTypeDef

### NumResults
- **Type**: <class 'int'>
- **Required**: Yes

### BonusPayments
- **Type**: typing.List[aws_resource_validator.pydantic_models.mturk_classes.BonusPaymentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHITsForQualificationTypeRequestPaginateTypeDef

### QualificationTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mturk_classes.PaginatorConfigTypeDef]


# ListHITsForQualificationTypeRequestTypeDef

### QualificationTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListHITsForQualificationTypeResponseTypeDef

### NumResults
- **Type**: <class 'int'>
- **Required**: Yes

### HITs
- **Type**: typing.List[aws_resource_validator.pydantic_models.mturk_classes.HITTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHITsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mturk_classes.PaginatorConfigTypeDef]


# ListHITsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListHITsResponseTypeDef

### NumResults
- **Type**: <class 'int'>
- **Required**: Yes

### HITs
- **Type**: typing.List[aws_resource_validator.pydantic_models.mturk_classes.HITTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListQualificationRequestsRequestPaginateTypeDef

### QualificationTypeId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mturk_classes.PaginatorConfigTypeDef]


# ListQualificationRequestsRequestTypeDef

### QualificationTypeId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListQualificationRequestsResponseTypeDef

### NumResults
- **Type**: <class 'int'>
- **Required**: Yes

### QualificationRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.mturk_classes.QualificationRequestTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListQualificationTypesRequestPaginateTypeDef

### MustBeRequestable
- **Type**: <class 'bool'>
- **Required**: Yes

### Query
- **Type**: typing.Optional[str]

### MustBeOwnedByCaller
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mturk_classes.PaginatorConfigTypeDef]


# ListQualificationTypesRequestTypeDef

### MustBeRequestable
- **Type**: <class 'bool'>
- **Required**: Yes

### Query
- **Type**: typing.Optional[str]

### MustBeOwnedByCaller
- **Type**: typing.Optional[bool]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListQualificationTypesResponseTypeDef

### NumResults
- **Type**: <class 'int'>
- **Required**: Yes

### QualificationTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.mturk_classes.QualificationTypeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListReviewPolicyResultsForHITRequestTypeDef

### HITId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyLevels
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Assignment', 'HIT']]]

### RetrieveActions
- **Type**: typing.Optional[bool]

### RetrieveResults
- **Type**: typing.Optional[bool]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListReviewPolicyResultsForHITResponseTypeDef

### HITId
- **Type**: <class 'str'>
- **Required**: Yes

### AssignmentReviewPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.ReviewPolicyOutputTypeDef'>
- **Required**: Yes

### HITReviewPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.ReviewPolicyOutputTypeDef'>
- **Required**: Yes

### AssignmentReviewReport
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.ReviewReportTypeDef'>
- **Required**: Yes

### HITReviewReport
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.ReviewReportTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListReviewableHITsRequestPaginateTypeDef

### HITTypeId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Reviewable', 'Reviewing']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mturk_classes.PaginatorConfigTypeDef]


# ListReviewableHITsRequestTypeDef

### HITTypeId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Reviewable', 'Reviewing']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListReviewableHITsResponseTypeDef

### NumResults
- **Type**: <class 'int'>
- **Required**: Yes

### HITs
- **Type**: typing.List[aws_resource_validator.pydantic_models.mturk_classes.HITTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListWorkerBlocksRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mturk_classes.PaginatorConfigTypeDef]


# ListWorkerBlocksRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListWorkerBlocksResponseTypeDef

### NumResults
- **Type**: <class 'int'>
- **Required**: Yes

### WorkerBlocks
- **Type**: typing.List[aws_resource_validator.pydantic_models.mturk_classes.WorkerBlockTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListWorkersWithQualificationTypeRequestPaginateTypeDef

### QualificationTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['Granted', 'Revoked']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mturk_classes.PaginatorConfigTypeDef]


# ListWorkersWithQualificationTypeRequestTypeDef

### QualificationTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['Granted', 'Revoked']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListWorkersWithQualificationTypeResponseTypeDef

### NumResults
- **Type**: <class 'int'>
- **Required**: Yes

### Qualifications
- **Type**: typing.List[aws_resource_validator.pydantic_models.mturk_classes.QualificationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LocaleTypeDef

### Country
- **Type**: <class 'str'>
- **Required**: Yes

### Subdivision
- **Type**: typing.Optional[str]


# NotificationSpecificationTypeDef

### Destination
- **Type**: <class 'str'>
- **Required**: Yes

### Transport
- **Type**: typing.Literal['Email', 'SNS', 'SQS']
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### EventTypes
- **Type**: typing.Sequence[typing.Literal['AssignmentAbandoned', 'AssignmentAccepted', 'AssignmentApproved', 'AssignmentRejected', 'AssignmentReturned', 'AssignmentSubmitted', 'HITCreated', 'HITDisposed', 'HITExpired', 'HITExtended', 'HITReviewable', 'Ping']]
- **Required**: Yes


# NotifyWorkersFailureStatusTypeDef

### NotifyWorkersFailureCode
- **Type**: typing.Optional[typing.Literal['HardFailure', 'SoftFailure']]

### NotifyWorkersFailureMessage
- **Type**: typing.Optional[str]

### WorkerId
- **Type**: typing.Optional[str]


# NotifyWorkersRequestTypeDef

### Subject
- **Type**: <class 'str'>
- **Required**: Yes

### MessageText
- **Type**: <class 'str'>
- **Required**: Yes

### WorkerIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# NotifyWorkersResponseTypeDef

### NotifyWorkersFailureStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.mturk_classes.NotifyWorkersFailureStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParameterMapEntryOutputTypeDef

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]


# ParameterMapEntryTypeDef

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# PolicyParameterOutputTypeDef

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]

### MapEntries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mturk_classes.ParameterMapEntryOutputTypeDef]]


# PolicyParameterTypeDef

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]

### MapEntries
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mturk_classes.ParameterMapEntryTypeDef]]


# QualificationRequestTypeDef

### QualificationRequestId
- **Type**: typing.Optional[str]

### QualificationTypeId
- **Type**: typing.Optional[str]

### WorkerId
- **Type**: typing.Optional[str]

### Test
- **Type**: typing.Optional[str]

### Answer
- **Type**: typing.Optional[str]

### SubmitTime
- **Type**: typing.Optional[datetime.datetime]


# QualificationRequirementOutputTypeDef

### QualificationTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### Comparator
- **Type**: typing.Literal['DoesNotExist', 'EqualTo', 'Exists', 'GreaterThan', 'GreaterThanOrEqualTo', 'In', 'LessThan', 'LessThanOrEqualTo', 'NotEqualTo', 'NotIn']
- **Required**: Yes

### IntegerValues
- **Type**: typing.Optional[typing.List[int]]

### LocaleValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mturk_classes.LocaleTypeDef]]

### RequiredToPreview
- **Type**: typing.Optional[bool]

### ActionsGuarded
- **Type**: typing.Optional[typing.Literal['Accept', 'DiscoverPreviewAndAccept', 'PreviewAndAccept']]


# QualificationRequirementTypeDef

### QualificationTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### Comparator
- **Type**: typing.Literal['DoesNotExist', 'EqualTo', 'Exists', 'GreaterThan', 'GreaterThanOrEqualTo', 'In', 'LessThan', 'LessThanOrEqualTo', 'NotEqualTo', 'NotIn']
- **Required**: Yes

### IntegerValues
- **Type**: typing.Optional[typing.Sequence[int]]

### LocaleValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mturk_classes.LocaleTypeDef]]

### RequiredToPreview
- **Type**: typing.Optional[bool]

### ActionsGuarded
- **Type**: typing.Optional[typing.Literal['Accept', 'DiscoverPreviewAndAccept', 'PreviewAndAccept']]


# QualificationRequirementUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# QualificationTypeDef

### QualificationTypeId
- **Type**: typing.Optional[str]

### WorkerId
- **Type**: typing.Optional[str]

### GrantTime
- **Type**: typing.Optional[datetime.datetime]

### IntegerValue
- **Type**: typing.Optional[int]

### LocaleValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mturk_classes.LocaleTypeDef]

### Status
- **Type**: typing.Optional[typing.Literal['Granted', 'Revoked']]


# QualificationTypeTypeDef

### QualificationTypeId
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Keywords
- **Type**: typing.Optional[str]

### QualificationTypeStatus
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]

### Test
- **Type**: typing.Optional[str]

### TestDurationInSeconds
- **Type**: typing.Optional[int]

### AnswerKey
- **Type**: typing.Optional[str]

### RetryDelayInSeconds
- **Type**: typing.Optional[int]

### IsRequestable
- **Type**: typing.Optional[bool]

### AutoGranted
- **Type**: typing.Optional[bool]

### AutoGrantedValue
- **Type**: typing.Optional[int]


# RejectAssignmentRequestTypeDef

### AssignmentId
- **Type**: <class 'str'>
- **Required**: Yes

### RequesterFeedback
- **Type**: <class 'str'>
- **Required**: Yes


# RejectQualificationRequestRequestTypeDef

### QualificationRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Reason
- **Type**: typing.Optional[str]


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


# ReviewActionDetailTypeDef

### ActionId
- **Type**: typing.Optional[str]

### ActionName
- **Type**: typing.Optional[str]

### TargetId
- **Type**: typing.Optional[str]

### TargetType
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Cancelled', 'Failed', 'Intended', 'Succeeded']]

### CompleteTime
- **Type**: typing.Optional[datetime.datetime]

### Result
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]


# ReviewPolicyOutputTypeDef

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mturk_classes.PolicyParameterOutputTypeDef]]


# ReviewPolicyTypeDef

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mturk_classes.PolicyParameterTypeDef]]


# ReviewPolicyUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ReviewReportTypeDef

### ReviewResults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mturk_classes.ReviewResultDetailTypeDef]]

### ReviewActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mturk_classes.ReviewActionDetailTypeDef]]


# ReviewResultDetailTypeDef

### ActionId
- **Type**: typing.Optional[str]

### SubjectId
- **Type**: typing.Optional[str]

### SubjectType
- **Type**: typing.Optional[str]

### QuestionId
- **Type**: typing.Optional[str]

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# SendBonusRequestTypeDef

### WorkerId
- **Type**: <class 'str'>
- **Required**: Yes

### BonusAmount
- **Type**: <class 'str'>
- **Required**: Yes

### AssignmentId
- **Type**: <class 'str'>
- **Required**: Yes

### Reason
- **Type**: <class 'str'>
- **Required**: Yes

### UniqueRequestToken
- **Type**: typing.Optional[str]


# SendTestEventNotificationRequestTypeDef

### Notification
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.NotificationSpecificationTypeDef'>
- **Required**: Yes

### TestEventType
- **Type**: typing.Literal['AssignmentAbandoned', 'AssignmentAccepted', 'AssignmentApproved', 'AssignmentRejected', 'AssignmentReturned', 'AssignmentSubmitted', 'HITCreated', 'HITDisposed', 'HITExpired', 'HITExtended', 'HITReviewable', 'Ping']
- **Required**: Yes


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UpdateExpirationForHITRequestTypeDef

### HITId
- **Type**: <class 'str'>
- **Required**: Yes

### ExpireAt
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.TimestampTypeDef'>
- **Required**: Yes


# UpdateHITReviewStatusRequestTypeDef

### HITId
- **Type**: <class 'str'>
- **Required**: Yes

### Revert
- **Type**: typing.Optional[bool]


# UpdateHITTypeOfHITRequestTypeDef

### HITId
- **Type**: <class 'str'>
- **Required**: Yes

### HITTypeId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateNotificationSettingsRequestTypeDef

### HITTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### Notification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mturk_classes.NotificationSpecificationTypeDef]

### Active
- **Type**: typing.Optional[bool]


# UpdateQualificationTypeRequestTypeDef

### QualificationTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### QualificationTypeStatus
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]

### Test
- **Type**: typing.Optional[str]

### AnswerKey
- **Type**: typing.Optional[str]

### TestDurationInSeconds
- **Type**: typing.Optional[int]

### RetryDelayInSeconds
- **Type**: typing.Optional[int]

### AutoGranted
- **Type**: typing.Optional[bool]

### AutoGrantedValue
- **Type**: typing.Optional[int]


# UpdateQualificationTypeResponseTypeDef

### QualificationType
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.QualificationTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WorkerBlockTypeDef

### WorkerId
- **Type**: typing.Optional[str]

### Reason
- **Type**: typing.Optional[str]


