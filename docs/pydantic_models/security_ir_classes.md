# Security Ir Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetMemberAccountDetailsRequest

### membershipId
- **Type**: <class 'str'>
- **Required**: Yes

### accountIds
- **Type**: typing.List[str]
- **Required**: Yes


# BatchGetMemberAccountDetailsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.security_ir.security_ir_classes.GetMembershipAccountDetailItem]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.security_ir.security_ir_classes.GetMembershipAccountDetailError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.security_ir.security_ir_classes.ResponseMetadata'>
- **Required**: Yes


# CancelMembershipRequest

### membershipId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelMembershipResponse

### membershipId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.security_ir.security_ir_classes.ResponseMetadata'>
- **Required**: Yes


# CaseAttachmentAttributes

### attachmentId
- **Type**: <class 'str'>
- **Required**: Yes

### fileName
- **Type**: <class 'str'>
- **Required**: Yes

### attachmentStatus
- **Type**: typing.Literal['Failed', 'Pending', 'Verified']
- **Required**: Yes

### creator
- **Type**: <class 'str'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# CaseEditItem

### eventTimestamp
- **Type**: typing.Optional[datetime.datetime]

### principal
- **Type**: typing.Optional[str]

### action
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]


# CloseCaseRequest

### caseId
- **Type**: <class 'str'>
- **Required**: Yes


# CloseCaseResponse

### caseStatus
- **Type**: typing.Literal['Acknowledged', 'Closed', 'Containment, Eradication and Recovery', 'Detection and Analysis', 'Post-incident Activities', 'Ready to Close', 'Submitted']
- **Required**: Yes

### closedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.security_ir.security_ir_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCaseCommentRequest

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### body
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreateCaseCommentResponse

### commentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.security_ir.security_ir_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCaseRequest

### resolverType
- **Type**: typing.Literal['AWS', 'Self']
- **Required**: Yes

### title
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### engagementType
- **Type**: typing.Literal['Investigation', 'Security Incident']
- **Required**: Yes

### reportedIncidentStartDate
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### impactedAccounts
- **Type**: typing.List[str]
- **Required**: Yes

### watchers
- **Type**: typing.List[aws_resource_validator.pydantic_models.security_ir.security_ir_classes.Watcher]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### threatActorIpAddresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.security_ir.security_ir_classes.ThreatActorIp]]

### impactedServices
- **Type**: typing.Optional[typing.List[str]]

### impactedAwsRegions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.security_ir.security_ir_classes.ImpactedAwsRegion]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateCaseResponse

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.security_ir.security_ir_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMembershipRequest

### membershipName
- **Type**: <class 'str'>
- **Required**: Yes

### incidentResponseTeam
- **Type**: typing.List[aws_resource_validator.pydantic_models.security_ir.security_ir_classes.IncidentResponder]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### optInFeatures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.security_ir.security_ir_classes.OptInFeature]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateMembershipResponse

### membershipId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.security_ir.security_ir_classes.ResponseMetadata'>
- **Required**: Yes


# GetCaseAttachmentDownloadUrlRequest

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### attachmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCaseAttachmentDownloadUrlResponse

### attachmentPresignedUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.security_ir.security_ir_classes.ResponseMetadata'>
- **Required**: Yes


# GetCaseAttachmentUploadUrlRequest

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### fileName
- **Type**: <class 'str'>
- **Required**: Yes

### contentLength
- **Type**: <class 'int'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# GetCaseAttachmentUploadUrlResponse

### attachmentPresignedUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.security_ir.security_ir_classes.ResponseMetadata'>
- **Required**: Yes


# GetCaseRequest

### caseId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCaseResponse

### title
- **Type**: <class 'str'>
- **Required**: Yes

### caseArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### caseStatus
- **Type**: typing.Literal['Acknowledged', 'Closed', 'Containment, Eradication and Recovery', 'Detection and Analysis', 'Post-incident Activities', 'Ready to Close', 'Submitted']
- **Required**: Yes

### engagementType
- **Type**: typing.Literal['Investigation', 'Security Incident']
- **Required**: Yes

### reportedIncidentStartDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### actualIncidentStartDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### impactedAwsRegions
- **Type**: typing.List[aws_resource_validator.pydantic_models.security_ir.security_ir_classes.ImpactedAwsRegion]
- **Required**: Yes

### threatActorIpAddresses
- **Type**: typing.List[aws_resource_validator.pydantic_models.security_ir.security_ir_classes.ThreatActorIp]
- **Required**: Yes

### pendingAction
- **Type**: typing.Literal['Customer', 'None']
- **Required**: Yes

### impactedAccounts
- **Type**: typing.List[str]
- **Required**: Yes

### watchers
- **Type**: typing.List[aws_resource_validator.pydantic_models.security_ir.security_ir_classes.Watcher]
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### closureCode
- **Type**: typing.Literal['Duplicate', 'False Positive', 'Investigation Completed', 'Not Resolved']
- **Required**: Yes

### resolverType
- **Type**: typing.Literal['AWS', 'Self']
- **Required**: Yes

### impactedServices
- **Type**: typing.List[str]
- **Required**: Yes

### caseAttachments
- **Type**: typing.List[aws_resource_validator.pydantic_models.security_ir.security_ir_classes.CaseAttachmentAttributes]
- **Required**: Yes

### closedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.security_ir.security_ir_classes.ResponseMetadata'>
- **Required**: Yes


# GetMembershipAccountDetailError

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### error
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# GetMembershipAccountDetailItem

### accountId
- **Type**: typing.Optional[str]

### relationshipStatus
- **Type**: typing.Optional[typing.Literal['Associated', 'Disassociated']]

### relationshipType
- **Type**: typing.Optional[typing.Literal['Organization']]


# GetMembershipRequest

### membershipId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMembershipResponse

### membershipId
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### region
- **Type**: typing.Literal['af-south-1', 'ap-east-1', 'ap-northeast-1', 'ap-northeast-2', 'ap-northeast-3', 'ap-south-1', 'ap-south-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-southeast-3', 'ap-southeast-4', 'ap-southeast-5', 'ca-central-1', 'ca-west-1', 'cn-north-1', 'cn-northwest-1', 'eu-central-1', 'eu-central-2', 'eu-north-1', 'eu-south-1', 'eu-south-2', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'il-central-1', 'me-central-1', 'me-south-1', 'sa-east-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
- **Required**: Yes

### membershipName
- **Type**: <class 'str'>
- **Required**: Yes

### membershipArn
- **Type**: <class 'str'>
- **Required**: Yes

### membershipStatus
- **Type**: typing.Literal['Active', 'Cancelled', 'Terminated']
- **Required**: Yes

### membershipActivationTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### membershipDeactivationTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### customerType
- **Type**: typing.Literal['Organization', 'Standalone']
- **Required**: Yes

### numberOfAccountsCovered
- **Type**: <class 'int'>
- **Required**: Yes

### incidentResponseTeam
- **Type**: typing.List[aws_resource_validator.pydantic_models.security_ir.security_ir_classes.IncidentResponder]
- **Required**: Yes

### optInFeatures
- **Type**: typing.List[aws_resource_validator.pydantic_models.security_ir.security_ir_classes.OptInFeature]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.security_ir.security_ir_classes.ResponseMetadata'>
- **Required**: Yes


# ImpactedAwsRegion

### region
- **Type**: typing.Literal['af-south-1', 'ap-east-1', 'ap-northeast-1', 'ap-northeast-2', 'ap-northeast-3', 'ap-south-1', 'ap-south-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-southeast-3', 'ap-southeast-4', 'ap-southeast-5', 'ca-central-1', 'ca-west-1', 'cn-north-1', 'cn-northwest-1', 'eu-central-1', 'eu-central-2', 'eu-north-1', 'eu-south-1', 'eu-south-2', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'il-central-1', 'me-central-1', 'me-south-1', 'sa-east-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
- **Required**: Yes


# IncidentResponder

### name
- **Type**: <class 'str'>
- **Required**: Yes

### jobTitle
- **Type**: <class 'str'>
- **Required**: Yes

### email
- **Type**: <class 'str'>
- **Required**: Yes


# ListCaseEditsRequest

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCaseEditsRequestPaginate

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.security_ir.security_ir_classes.PaginatorConfig]


# ListCaseEditsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.security_ir.security_ir_classes.CaseEditItem]
- **Required**: Yes

### total
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.security_ir.security_ir_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCasesItem

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: typing.Optional[datetime.datetime]

### title
- **Type**: typing.Optional[str]

### caseArn
- **Type**: typing.Optional[str]

### engagementType
- **Type**: typing.Optional[typing.Literal['Investigation', 'Security Incident']]

### caseStatus
- **Type**: typing.Optional[typing.Literal['Acknowledged', 'Closed', 'Containment, Eradication and Recovery', 'Detection and Analysis', 'Post-incident Activities', 'Ready to Close', 'Submitted']]

### createdDate
- **Type**: typing.Optional[datetime.datetime]

### closedDate
- **Type**: typing.Optional[datetime.datetime]

### resolverType
- **Type**: typing.Optional[typing.Literal['AWS', 'Self']]

### pendingAction
- **Type**: typing.Optional[typing.Literal['Customer', 'None']]


# ListCasesRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCasesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.security_ir.security_ir_classes.PaginatorConfig]


# ListCasesResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.security_ir.security_ir_classes.ListCasesItem]
- **Required**: Yes

### total
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.security_ir.security_ir_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCommentsItem

### commentId
- **Type**: <class 'str'>
- **Required**: Yes

### createdDate
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDate
- **Type**: typing.Optional[datetime.datetime]

### creator
- **Type**: typing.Optional[str]

### lastUpdatedBy
- **Type**: typing.Optional[str]

### body
- **Type**: typing.Optional[str]


# ListCommentsRequest

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCommentsRequestPaginate

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.security_ir.security_ir_classes.PaginatorConfig]


# ListCommentsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.security_ir.security_ir_classes.ListCommentsItem]
- **Required**: Yes

### total
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.security_ir.security_ir_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMembershipItem

### membershipId
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[typing.Literal['af-south-1', 'ap-east-1', 'ap-northeast-1', 'ap-northeast-2', 'ap-northeast-3', 'ap-south-1', 'ap-south-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-southeast-3', 'ap-southeast-4', 'ap-southeast-5', 'ca-central-1', 'ca-west-1', 'cn-north-1', 'cn-northwest-1', 'eu-central-1', 'eu-central-2', 'eu-north-1', 'eu-south-1', 'eu-south-2', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'il-central-1', 'me-central-1', 'me-south-1', 'sa-east-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']]

### membershipArn
- **Type**: typing.Optional[str]

### membershipStatus
- **Type**: typing.Optional[typing.Literal['Active', 'Cancelled', 'Terminated']]


# ListMembershipsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListMembershipsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.security_ir.security_ir_classes.PaginatorConfig]


# ListMembershipsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.security_ir.security_ir_classes.ListMembershipItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.security_ir.security_ir_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutput

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.security_ir.security_ir_classes.ResponseMetadata'>
- **Required**: Yes


# OptInFeature

### featureName
- **Type**: typing.Literal['Triage']
- **Required**: Yes

### isEnabled
- **Type**: <class 'bool'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
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


# TagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# ThreatActorIp

### ipAddress
- **Type**: <class 'str'>
- **Required**: Yes

### userAgent
- **Type**: typing.Optional[str]


# UntagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateCaseCommentRequest

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### commentId
- **Type**: <class 'str'>
- **Required**: Yes

### body
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateCaseCommentResponse

### commentId
- **Type**: <class 'str'>
- **Required**: Yes

### body
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.security_ir.security_ir_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateCaseRequest

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### title
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### reportedIncidentStartDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### actualIncidentStartDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### engagementType
- **Type**: typing.Optional[typing.Literal['Investigation', 'Security Incident']]

### watchersToAdd
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.security_ir.security_ir_classes.Watcher]]

### watchersToDelete
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.security_ir.security_ir_classes.Watcher]]

### threatActorIpAddressesToAdd
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.security_ir.security_ir_classes.ThreatActorIp]]

### threatActorIpAddressesToDelete
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.security_ir.security_ir_classes.ThreatActorIp]]

### impactedServicesToAdd
- **Type**: typing.Optional[typing.List[str]]

### impactedServicesToDelete
- **Type**: typing.Optional[typing.List[str]]

### impactedAwsRegionsToAdd
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.security_ir.security_ir_classes.ImpactedAwsRegion]]

### impactedAwsRegionsToDelete
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.security_ir.security_ir_classes.ImpactedAwsRegion]]

### impactedAccountsToAdd
- **Type**: typing.Optional[typing.List[str]]

### impactedAccountsToDelete
- **Type**: typing.Optional[typing.List[str]]


# UpdateCaseStatusRequest

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### caseStatus
- **Type**: typing.Literal['Containment, Eradication and Recovery', 'Detection and Analysis', 'Post-incident Activities', 'Submitted']
- **Required**: Yes


# UpdateCaseStatusResponse

### caseStatus
- **Type**: typing.Literal['Containment, Eradication and Recovery', 'Detection and Analysis', 'Post-incident Activities', 'Submitted']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.security_ir.security_ir_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateMembershipRequest

### membershipId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipName
- **Type**: typing.Optional[str]

### incidentResponseTeam
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.security_ir.security_ir_classes.IncidentResponder]]

### optInFeatures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.security_ir.security_ir_classes.OptInFeature]]


# UpdateResolverTypeRequest

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### resolverType
- **Type**: typing.Literal['AWS', 'Self']
- **Required**: Yes


# UpdateResolverTypeResponse

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### caseStatus
- **Type**: typing.Literal['Acknowledged', 'Closed', 'Containment, Eradication and Recovery', 'Detection and Analysis', 'Post-incident Activities', 'Ready to Close', 'Submitted']
- **Required**: Yes

### resolverType
- **Type**: typing.Literal['AWS', 'Self']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.security_ir.security_ir_classes.ResponseMetadata'>
- **Required**: Yes


# Watcher

### email
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### jobTitle
- **Type**: typing.Optional[str]


