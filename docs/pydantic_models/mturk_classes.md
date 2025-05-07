# Mturk Classes

# AcceptQualificationRequestRequest

### QualificationRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegerValue
- **Type**: typing.Optional[int]


# ApproveAssignmentRequest

### AssignmentId
- **Type**: <class 'str'>
- **Required**: Yes

### RequesterFeedback
- **Type**: typing.Optional[str]

### OverrideRejection
- **Type**: typing.Optional[bool]


# Assignment

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


# AssociateQualificationWithWorkerRequest

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

# BonusPayment

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


# CreateAdditionalAssignmentsForHITRequest

### HITId
- **Type**: <class 'str'>
- **Required**: Yes

### NumberOfAdditionalAssignments
- **Type**: <class 'int'>
- **Required**: Yes

### UniqueRequestToken
- **Type**: typing.Optional[str]


# CreateHITRequest

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
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.mturk.mturk_classes.QualificationRequirement, aws_resource_validator.pydantic_models.mturk.mturk_classes.QualificationRequirementOutput]]]

### UniqueRequestToken
- **Type**: typing.Optional[str]

### AssignmentReviewPolicy
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mturk.mturk_classes.ReviewPolicy, aws_resource_validator.pydantic_models.mturk.mturk_classes.ReviewPolicyOutput, NoneType]

### HITReviewPolicy
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mturk.mturk_classes.ReviewPolicy, aws_resource_validator.pydantic_models.mturk.mturk_classes.ReviewPolicyOutput, NoneType]

### HITLayoutId
- **Type**: typing.Optional[str]

### HITLayoutParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mturk.mturk_classes.HITLayoutParameter]]


# CreateHITResponse

### HIT
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.HIT'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.ResponseMetadata'>
- **Required**: Yes


# CreateHITTypeRequest

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
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.mturk.mturk_classes.QualificationRequirement, aws_resource_validator.pydantic_models.mturk.mturk_classes.QualificationRequirementOutput]]]


# CreateHITTypeResponse

### HITTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.ResponseMetadata'>
- **Required**: Yes


# CreateHITWithHITTypeRequest

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mturk.mturk_classes.ReviewPolicy, aws_resource_validator.pydantic_models.mturk.mturk_classes.ReviewPolicyOutput, NoneType]

### HITReviewPolicy
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mturk.mturk_classes.ReviewPolicy, aws_resource_validator.pydantic_models.mturk.mturk_classes.ReviewPolicyOutput, NoneType]

### HITLayoutId
- **Type**: typing.Optional[str]

### HITLayoutParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mturk.mturk_classes.HITLayoutParameter]]


# CreateHITWithHITTypeResponse

### HIT
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.HIT'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.ResponseMetadata'>
- **Required**: Yes


# CreateQualificationTypeRequest

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


# CreateQualificationTypeResponse

### QualificationType
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.QualificationType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWorkerBlockRequest

### WorkerId
- **Type**: <class 'str'>
- **Required**: Yes

### Reason
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHITRequest

### HITId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQualificationTypeRequest

### QualificationTypeId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkerBlockRequest

### WorkerId
- **Type**: <class 'str'>
- **Required**: Yes

### Reason
- **Type**: typing.Optional[str]


# DisassociateQualificationFromWorkerRequest

### WorkerId
- **Type**: <class 'str'>
- **Required**: Yes

### QualificationTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### Reason
- **Type**: typing.Optional[str]


# GetAccountBalanceResponse

### AvailableBalance
- **Type**: <class 'str'>
- **Required**: Yes

### OnHoldBalance
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.ResponseMetadata'>
- **Required**: Yes


# GetAssignmentRequest

### AssignmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAssignmentResponse

### Assignment
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.Assignment'>
- **Required**: Yes

### HIT
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.HIT'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.ResponseMetadata'>
- **Required**: Yes


# GetFileUploadURLRequest

### AssignmentId
- **Type**: <class 'str'>
- **Required**: Yes

### QuestionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetFileUploadURLResponse

### FileUploadURL
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.ResponseMetadata'>
- **Required**: Yes


# GetHITRequest

### HITId
- **Type**: <class 'str'>
- **Required**: Yes


# GetHITResponse

### HIT
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.HIT'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.ResponseMetadata'>
- **Required**: Yes


# GetQualificationScoreRequest

### QualificationTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkerId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQualificationScoreResponse

### Qualification
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.Qualification'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.ResponseMetadata'>
- **Required**: Yes


# GetQualificationTypeRequest

### QualificationTypeId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQualificationTypeResponse

### QualificationType
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.QualificationType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.ResponseMetadata'>
- **Required**: Yes


# HIT

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mturk.mturk_classes.QualificationRequirementOutput]]

### HITReviewStatus
- **Type**: typing.Optional[typing.Literal['MarkedForReview', 'NotReviewed', 'ReviewedAppropriate', 'ReviewedInappropriate']]

### NumberOfAssignmentsPending
- **Type**: typing.Optional[int]

### NumberOfAssignmentsAvailable
- **Type**: typing.Optional[int]

### NumberOfAssignmentsCompleted
- **Type**: typing.Optional[int]


# HITLayoutParameter

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ListAssignmentsForHITRequest

### HITId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### AssignmentStatuses
- **Type**: typing.Optional[typing.List[typing.Literal['Approved', 'Rejected', 'Submitted']]]


# ListAssignmentsForHITRequestPaginate

### HITId
- **Type**: <class 'str'>
- **Required**: Yes

### AssignmentStatuses
- **Type**: typing.Optional[typing.List[typing.Literal['Approved', 'Rejected', 'Submitted']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mturk.mturk_classes.PaginatorConfig]


# ListAssignmentsForHITResponse

### NumResults
- **Type**: <class 'int'>
- **Required**: Yes

### Assignments
- **Type**: typing.List[aws_resource_validator.pydantic_models.mturk.mturk_classes.Assignment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListBonusPaymentsRequest

### HITId
- **Type**: typing.Optional[str]

### AssignmentId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListBonusPaymentsRequestPaginate

### HITId
- **Type**: typing.Optional[str]

### AssignmentId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mturk.mturk_classes.PaginatorConfig]


# ListBonusPaymentsResponse

### NumResults
- **Type**: <class 'int'>
- **Required**: Yes

### BonusPayments
- **Type**: typing.List[aws_resource_validator.pydantic_models.mturk.mturk_classes.BonusPayment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHITsForQualificationTypeRequest

### QualificationTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListHITsForQualificationTypeRequestPaginate

### QualificationTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mturk.mturk_classes.PaginatorConfig]


# ListHITsForQualificationTypeResponse

### NumResults
- **Type**: <class 'int'>
- **Required**: Yes

### HITs
- **Type**: typing.List[aws_resource_validator.pydantic_models.mturk.mturk_classes.HIT]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHITsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListHITsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mturk.mturk_classes.PaginatorConfig]


# ListHITsResponse

### NumResults
- **Type**: <class 'int'>
- **Required**: Yes

### HITs
- **Type**: typing.List[aws_resource_validator.pydantic_models.mturk.mturk_classes.HIT]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListQualificationRequestsRequest

### QualificationTypeId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListQualificationRequestsRequestPaginate

### QualificationTypeId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mturk.mturk_classes.PaginatorConfig]


# ListQualificationRequestsResponse

### NumResults
- **Type**: <class 'int'>
- **Required**: Yes

### QualificationRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.mturk.mturk_classes.QualificationRequest]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListQualificationTypesRequest

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


# ListQualificationTypesRequestPaginate

### MustBeRequestable
- **Type**: <class 'bool'>
- **Required**: Yes

### Query
- **Type**: typing.Optional[str]

### MustBeOwnedByCaller
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mturk.mturk_classes.PaginatorConfig]


# ListQualificationTypesResponse

### NumResults
- **Type**: <class 'int'>
- **Required**: Yes

### QualificationTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.mturk.mturk_classes.QualificationType]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListReviewPolicyResultsForHITRequest

### HITId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyLevels
- **Type**: typing.Optional[typing.List[typing.Literal['Assignment', 'HIT']]]

### RetrieveActions
- **Type**: typing.Optional[bool]

### RetrieveResults
- **Type**: typing.Optional[bool]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListReviewPolicyResultsForHITResponse

### HITId
- **Type**: <class 'str'>
- **Required**: Yes

### AssignmentReviewPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.ReviewPolicyOutput'>
- **Required**: Yes

### HITReviewPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.ReviewPolicyOutput'>
- **Required**: Yes

### AssignmentReviewReport
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.ReviewReport'>
- **Required**: Yes

### HITReviewReport
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.ReviewReport'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListReviewableHITsRequest

### HITTypeId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Reviewable', 'Reviewing']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListReviewableHITsRequestPaginate

### HITTypeId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Reviewable', 'Reviewing']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mturk.mturk_classes.PaginatorConfig]


# ListReviewableHITsResponse

### NumResults
- **Type**: <class 'int'>
- **Required**: Yes

### HITs
- **Type**: typing.List[aws_resource_validator.pydantic_models.mturk.mturk_classes.HIT]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListWorkerBlocksRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListWorkerBlocksRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mturk.mturk_classes.PaginatorConfig]


# ListWorkerBlocksResponse

### NumResults
- **Type**: <class 'int'>
- **Required**: Yes

### WorkerBlocks
- **Type**: typing.List[aws_resource_validator.pydantic_models.mturk.mturk_classes.WorkerBlock]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListWorkersWithQualificationTypeRequest

### QualificationTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['Granted', 'Revoked']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListWorkersWithQualificationTypeRequestPaginate

### QualificationTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['Granted', 'Revoked']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mturk.mturk_classes.PaginatorConfig]


# ListWorkersWithQualificationTypeResponse

### NumResults
- **Type**: <class 'int'>
- **Required**: Yes

### Qualifications
- **Type**: typing.List[aws_resource_validator.pydantic_models.mturk.mturk_classes.Qualification]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# Locale

### Country
- **Type**: <class 'str'>
- **Required**: Yes

### Subdivision
- **Type**: typing.Optional[str]


# NotificationSpecification

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
- **Type**: typing.List[typing.Literal['AssignmentAbandoned', 'AssignmentAccepted', 'AssignmentApproved', 'AssignmentRejected', 'AssignmentReturned', 'AssignmentSubmitted', 'HITCreated', 'HITDisposed', 'HITExpired', 'HITExtended', 'HITReviewable', 'Ping']]
- **Required**: Yes


# NotifyWorkersFailureStatus

### NotifyWorkersFailureCode
- **Type**: typing.Optional[typing.Literal['HardFailure', 'SoftFailure']]

### NotifyWorkersFailureMessage
- **Type**: typing.Optional[str]

### WorkerId
- **Type**: typing.Optional[str]


# NotifyWorkersRequest

### Subject
- **Type**: <class 'str'>
- **Required**: Yes

### MessageText
- **Type**: <class 'str'>
- **Required**: Yes

### WorkerIds
- **Type**: typing.List[str]
- **Required**: Yes


# NotifyWorkersResponse

### NotifyWorkersFailureStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.mturk.mturk_classes.NotifyWorkersFailureStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParameterMapEntry

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]


# ParameterMapEntryOutput

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]


# PolicyParameter

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]

### MapEntries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mturk.mturk_classes.ParameterMapEntry]]


# PolicyParameterOutput

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]

### MapEntries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mturk.mturk_classes.ParameterMapEntryOutput]]


# Qualification

### QualificationTypeId
- **Type**: typing.Optional[str]

### WorkerId
- **Type**: typing.Optional[str]

### GrantTime
- **Type**: typing.Optional[datetime.datetime]

### IntegerValue
- **Type**: typing.Optional[int]

### LocaleValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mturk.mturk_classes.Locale]

### Status
- **Type**: typing.Optional[typing.Literal['Granted', 'Revoked']]


# QualificationRequest

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


# QualificationRequirement

### QualificationTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### Comparator
- **Type**: typing.Literal['DoesNotExist', 'EqualTo', 'Exists', 'GreaterThan', 'GreaterThanOrEqualTo', 'In', 'LessThan', 'LessThanOrEqualTo', 'NotEqualTo', 'NotIn']
- **Required**: Yes

### IntegerValues
- **Type**: typing.Optional[typing.List[int]]

### LocaleValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mturk.mturk_classes.Locale]]

### RequiredToPreview
- **Type**: typing.Optional[bool]

### ActionsGuarded
- **Type**: typing.Optional[typing.Literal['Accept', 'DiscoverPreviewAndAccept', 'PreviewAndAccept']]


# QualificationRequirementOutput

### QualificationTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### Comparator
- **Type**: typing.Literal['DoesNotExist', 'EqualTo', 'Exists', 'GreaterThan', 'GreaterThanOrEqualTo', 'In', 'LessThan', 'LessThanOrEqualTo', 'NotEqualTo', 'NotIn']
- **Required**: Yes

### IntegerValues
- **Type**: typing.Optional[typing.List[int]]

### LocaleValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mturk.mturk_classes.Locale]]

### RequiredToPreview
- **Type**: typing.Optional[bool]

### ActionsGuarded
- **Type**: typing.Optional[typing.Literal['Accept', 'DiscoverPreviewAndAccept', 'PreviewAndAccept']]


# QualificationType

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


# RejectAssignmentRequest

### AssignmentId
- **Type**: <class 'str'>
- **Required**: Yes

### RequesterFeedback
- **Type**: <class 'str'>
- **Required**: Yes


# RejectQualificationRequestRequest

### QualificationRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Reason
- **Type**: typing.Optional[str]


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


# ReviewActionDetail

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


# ReviewPolicy

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mturk.mturk_classes.PolicyParameter]]


# ReviewPolicyOutput

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mturk.mturk_classes.PolicyParameterOutput]]


# ReviewReport

### ReviewResults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mturk.mturk_classes.ReviewResultDetail]]

### ReviewActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mturk.mturk_classes.ReviewActionDetail]]


# ReviewResultDetail

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


# SendBonusRequest

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


# SendTestEventNotificationRequest

### Notification
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.NotificationSpecification'>
- **Required**: Yes

### TestEventType
- **Type**: typing.Literal['AssignmentAbandoned', 'AssignmentAccepted', 'AssignmentApproved', 'AssignmentRejected', 'AssignmentReturned', 'AssignmentSubmitted', 'HITCreated', 'HITDisposed', 'HITExpired', 'HITExtended', 'HITReviewable', 'Ping']
- **Required**: Yes


# UpdateExpirationForHITRequest

### HITId
- **Type**: <class 'str'>
- **Required**: Yes

### ExpireAt
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# UpdateHITReviewStatusRequest

### HITId
- **Type**: <class 'str'>
- **Required**: Yes

### Revert
- **Type**: typing.Optional[bool]


# UpdateHITTypeOfHITRequest

### HITId
- **Type**: <class 'str'>
- **Required**: Yes

### HITTypeId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateNotificationSettingsRequest

### HITTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### Notification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mturk.mturk_classes.NotificationSpecification]

### Active
- **Type**: typing.Optional[bool]


# UpdateQualificationTypeRequest

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


# UpdateQualificationTypeResponse

### QualificationType
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.QualificationType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mturk.mturk_classes.ResponseMetadata'>
- **Required**: Yes


# WorkerBlock

### WorkerId
- **Type**: typing.Optional[str]

### Reason
- **Type**: typing.Optional[str]


