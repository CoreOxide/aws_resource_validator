# Auditmanager Classes

# AWSAccount

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AWSService

### serviceName
- **Type**: typing.Optional[str]


# Assessment

### arn
- **Type**: typing.Optional[str]

### awsAccount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.AWSAccount]

### metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentMetadata]

### framework
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentFramework]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# AssessmentControl

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssessmentControlSet

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssessmentEvidenceFolder

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssessmentFramework

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssessmentFrameworkMetadata

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssessmentFrameworkShareRequest

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssessmentMetadata

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssessmentMetadataItem

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssessmentReport

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssessmentReportEvidenceError

### evidenceId
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]


# AssessmentReportMetadata

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssessmentReportsDestination

### destinationType
- **Type**: typing.Optional[typing.Literal['S3']]

### destination
- **Type**: typing.Optional[str]


# AssociateAssessmentReportEvidenceFolderRequest

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes

### evidenceFolderId
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchAssociateAssessmentReportEvidenceRequest

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes

### evidenceFolderId
- **Type**: <class 'str'>
- **Required**: Yes

### evidenceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchAssociateAssessmentReportEvidenceResponse

### evidenceIds
- **Type**: typing.List[str]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentReportEvidenceError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# BatchCreateDelegationByAssessmentError

### createDelegationRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.CreateDelegationRequest]

### errorCode
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]


# BatchCreateDelegationByAssessmentRequest

### createDelegationRequests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.auditmanager_classes.CreateDelegationRequest]
- **Required**: Yes

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes


# BatchCreateDelegationByAssessmentResponse

### delegations
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.Delegation]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.BatchCreateDelegationByAssessmentError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDeleteDelegationByAssessmentError

### delegationId
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]


# BatchDeleteDelegationByAssessmentRequest

### delegationIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes


# BatchDeleteDelegationByAssessmentResponse

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.BatchDeleteDelegationByAssessmentError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDisassociateAssessmentReportEvidenceRequest

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes

### evidenceFolderId
- **Type**: <class 'str'>
- **Required**: Yes

### evidenceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchDisassociateAssessmentReportEvidenceResponse

### evidenceIds
- **Type**: typing.List[str]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentReportEvidenceError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# BatchImportEvidenceToAssessmentControlError

### manualEvidence
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.ManualEvidence]

### errorCode
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]


# BatchImportEvidenceToAssessmentControlRequest

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes

### controlSetId
- **Type**: <class 'str'>
- **Required**: Yes

### controlId
- **Type**: <class 'str'>
- **Required**: Yes

### manualEvidence
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.auditmanager_classes.ManualEvidence]
- **Required**: Yes


# BatchImportEvidenceToAssessmentControlResponse

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.BatchImportEvidenceToAssessmentControlError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# ChangeLog

### objectType
- **Type**: typing.Optional[typing.Literal['ASSESSMENT', 'ASSESSMENT_REPORT', 'CONTROL', 'CONTROL_SET', 'DELEGATION']]

### objectName
- **Type**: typing.Optional[str]

### action
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE', 'DELETE', 'IMPORT_EVIDENCE', 'INACTIVE', 'REVIEWED', 'UNDER_REVIEW', 'UPDATE_METADATA']]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]


# Control

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ControlComment

### authorName
- **Type**: typing.Optional[str]

### commentBody
- **Type**: typing.Optional[str]

### postedDate
- **Type**: typing.Optional[datetime.datetime]


# ControlDomainInsights

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ControlInsightsMetadataByAssessmentItem

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ControlInsightsMetadataItem

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ControlMappingSource

### sourceId
- **Type**: typing.Optional[str]

### sourceName
- **Type**: typing.Optional[str]

### sourceDescription
- **Type**: typing.Optional[str]

### sourceSetUpOption
- **Type**: typing.Optional[typing.Literal['Procedural_Controls_Mapping', 'System_Controls_Mapping']]

### sourceType
- **Type**: typing.Optional[typing.Literal['AWS_API_Call', 'AWS_Cloudtrail', 'AWS_Config', 'AWS_Security_Hub', 'Common_Control', 'Core_Control', 'MANUAL']]

### sourceKeyword
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.SourceKeyword]

### sourceFrequency
- **Type**: typing.Optional[typing.Literal['DAILY', 'MONTHLY', 'WEEKLY']]

### troubleshootingText
- **Type**: typing.Optional[str]


# ControlMetadata

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAssessmentFrameworkControl

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAssessmentFrameworkControlSet

### name
- **Type**: <class 'str'>
- **Required**: Yes

### controls
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.auditmanager_classes.CreateAssessmentFrameworkControl]]


# CreateAssessmentFrameworkRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### controlSets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.auditmanager_classes.CreateAssessmentFrameworkControlSet]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### complianceType
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateAssessmentFrameworkResponse

### framework
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.Framework'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAssessmentReportRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### queryStatement
- **Type**: typing.Optional[str]


# CreateAssessmentReportResponse

### assessmentReport
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentReport'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAssessmentRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### assessmentReportsDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentReportsDestination'>
- **Required**: Yes

### scope
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ScopeUnion'>
- **Required**: Yes

### roles
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.auditmanager_classes.Role]
- **Required**: Yes

### frameworkId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateAssessmentResponse

### assessment
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.Assessment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# CreateControlMappingSource

### sourceName
- **Type**: typing.Optional[str]

### sourceDescription
- **Type**: typing.Optional[str]

### sourceSetUpOption
- **Type**: typing.Optional[typing.Literal['Procedural_Controls_Mapping', 'System_Controls_Mapping']]

### sourceType
- **Type**: typing.Optional[typing.Literal['AWS_API_Call', 'AWS_Cloudtrail', 'AWS_Config', 'AWS_Security_Hub', 'Common_Control', 'Core_Control', 'MANUAL']]

### sourceKeyword
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.SourceKeyword]

### sourceFrequency
- **Type**: typing.Optional[typing.Literal['DAILY', 'MONTHLY', 'WEEKLY']]

### troubleshootingText
- **Type**: typing.Optional[str]


# CreateControlRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### controlMappingSources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.auditmanager_classes.CreateControlMappingSource]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### testingInformation
- **Type**: typing.Optional[str]

### actionPlanTitle
- **Type**: typing.Optional[str]

### actionPlanInstructions
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateControlResponse

### control
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.Control'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDelegationRequest

### comment
- **Type**: typing.Optional[str]

### controlSetId
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### roleType
- **Type**: typing.Optional[typing.Literal['PROCESS_OWNER', 'RESOURCE_OWNER']]


# DefaultExportDestination

### destinationType
- **Type**: typing.Optional[typing.Literal['S3']]

### destination
- **Type**: typing.Optional[str]


# Delegation

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DelegationMetadata

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteAssessmentFrameworkRequest

### frameworkId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAssessmentFrameworkShareRequest

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### requestType
- **Type**: typing.Literal['RECEIVED', 'SENT']
- **Required**: Yes


# DeleteAssessmentReportRequest

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes

### assessmentReportId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAssessmentRequest

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteControlRequest

### controlId
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterAccountResponse

### status
- **Type**: typing.Literal['ACTIVE', 'INACTIVE', 'PENDING_ACTIVATION']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# DeregisterOrganizationAdminAccountRequest

### adminAccountId
- **Type**: typing.Optional[str]


# DeregistrationPolicy

### deleteResources
- **Type**: typing.Optional[typing.Literal['ALL', 'DEFAULT']]


# DisassociateAssessmentReportEvidenceFolderRequest

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes

### evidenceFolderId
- **Type**: <class 'str'>
- **Required**: Yes


# Evidence

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EvidenceFinderEnablement

### eventDataStoreArn
- **Type**: typing.Optional[str]

### enablementStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'DISABLE_IN_PROGRESS', 'ENABLED', 'ENABLE_IN_PROGRESS']]

### backfillStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'IN_PROGRESS', 'NOT_STARTED']]

### error
- **Type**: typing.Optional[str]


# EvidenceInsights

### noncompliantEvidenceCount
- **Type**: typing.Optional[int]

### compliantEvidenceCount
- **Type**: typing.Optional[int]

### inconclusiveEvidenceCount
- **Type**: typing.Optional[int]


# Framework

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FrameworkMetadata

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### logo
- **Type**: typing.Optional[str]

### complianceType
- **Type**: typing.Optional[str]


# GetAccountStatusResponse

### status
- **Type**: typing.Literal['ACTIVE', 'INACTIVE', 'PENDING_ACTIVATION']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetAssessmentFrameworkRequest

### frameworkId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAssessmentFrameworkResponse

### framework
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.Framework'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetAssessmentReportUrlRequest

### assessmentReportId
- **Type**: <class 'str'>
- **Required**: Yes

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAssessmentReportUrlResponse

### preSignedUrl
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.URL'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetAssessmentRequest

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAssessmentResponse

### assessment
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.Assessment'>
- **Required**: Yes

### userRole
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.Role'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetChangeLogsRequest

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes

### controlSetId
- **Type**: typing.Optional[str]

### controlId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetChangeLogsResponse

### changeLogs
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.ChangeLog]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetControlRequest

### controlId
- **Type**: <class 'str'>
- **Required**: Yes


# GetControlResponse

### control
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.Control'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetDelegationsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetDelegationsResponse

### delegations
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.DelegationMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetEvidenceByEvidenceFolderRequest

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes

### controlSetId
- **Type**: <class 'str'>
- **Required**: Yes

### evidenceFolderId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetEvidenceByEvidenceFolderResponse

### evidence
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.Evidence]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetEvidenceFileUploadUrlRequest

### fileName
- **Type**: <class 'str'>
- **Required**: Yes


# GetEvidenceFileUploadUrlResponse

### evidenceFileName
- **Type**: <class 'str'>
- **Required**: Yes

### uploadUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetEvidenceFolderRequest

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes

### controlSetId
- **Type**: <class 'str'>
- **Required**: Yes

### evidenceFolderId
- **Type**: <class 'str'>
- **Required**: Yes


# GetEvidenceFolderResponse

### evidenceFolder
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentEvidenceFolder'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetEvidenceFoldersByAssessmentControlRequest

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes

### controlSetId
- **Type**: <class 'str'>
- **Required**: Yes

### controlId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetEvidenceFoldersByAssessmentControlResponse

### evidenceFolders
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentEvidenceFolder]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetEvidenceFoldersByAssessmentRequest

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetEvidenceFoldersByAssessmentResponse

### evidenceFolders
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentEvidenceFolder]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetEvidenceRequest

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes

### controlSetId
- **Type**: <class 'str'>
- **Required**: Yes

### evidenceFolderId
- **Type**: <class 'str'>
- **Required**: Yes

### evidenceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetEvidenceResponse

### evidence
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.Evidence'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetInsightsByAssessmentRequest

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetInsightsByAssessmentResponse

### insights
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.InsightsByAssessment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetInsightsResponse

### insights
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.Insights'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetOrganizationAdminAccountResponse

### adminAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### organizationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetServicesInScopeResponse

### serviceMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.ServiceMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetSettingsRequest

### attribute
- **Type**: typing.Literal['ALL', 'DEFAULT_ASSESSMENT_REPORTS_DESTINATION', 'DEFAULT_EXPORT_DESTINATION', 'DEFAULT_PROCESS_OWNERS', 'DEREGISTRATION_POLICY', 'EVIDENCE_FINDER_ENABLEMENT', 'IS_AWS_ORG_ENABLED', 'SNS_TOPIC']
- **Required**: Yes


# GetSettingsResponse

### settings
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.Settings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# Insights

### activeAssessmentsCount
- **Type**: typing.Optional[int]

### noncompliantEvidenceCount
- **Type**: typing.Optional[int]

### compliantEvidenceCount
- **Type**: typing.Optional[int]

### inconclusiveEvidenceCount
- **Type**: typing.Optional[int]

### assessmentControlsCountByNoncompliantEvidence
- **Type**: typing.Optional[int]

### totalAssessmentControlsCount
- **Type**: typing.Optional[int]

### lastUpdated
- **Type**: typing.Optional[datetime.datetime]


# InsightsByAssessment

### noncompliantEvidenceCount
- **Type**: typing.Optional[int]

### compliantEvidenceCount
- **Type**: typing.Optional[int]

### inconclusiveEvidenceCount
- **Type**: typing.Optional[int]

### assessmentControlsCountByNoncompliantEvidence
- **Type**: typing.Optional[int]

### totalAssessmentControlsCount
- **Type**: typing.Optional[int]

### lastUpdated
- **Type**: typing.Optional[datetime.datetime]


# ListAssessmentControlInsightsByControlDomainRequest

### controlDomainId
- **Type**: <class 'str'>
- **Required**: Yes

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAssessmentControlInsightsByControlDomainResponse

### controlInsightsByAssessment
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.ControlInsightsMetadataByAssessmentItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAssessmentFrameworkShareRequestsRequest

### requestType
- **Type**: typing.Literal['RECEIVED', 'SENT']
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAssessmentFrameworkShareRequestsResponse

### assessmentFrameworkShareRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentFrameworkShareRequest]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAssessmentFrameworksRequest

### frameworkType
- **Type**: typing.Literal['Custom', 'Standard']
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAssessmentFrameworksResponse

### frameworkMetadataList
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentFrameworkMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAssessmentReportsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAssessmentReportsResponse

### assessmentReports
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentReportMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAssessmentsRequest

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAssessmentsResponse

### assessmentMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentMetadataItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListControlDomainInsightsByAssessmentRequest

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListControlDomainInsightsByAssessmentResponse

### controlDomainInsights
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.ControlDomainInsights]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListControlDomainInsightsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListControlDomainInsightsResponse

### controlDomainInsights
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.ControlDomainInsights]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListControlInsightsByControlDomainRequest

### controlDomainId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListControlInsightsByControlDomainResponse

### controlInsightsMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.ControlInsightsMetadataItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListControlsRequest

### controlType
- **Type**: typing.Literal['Core', 'Custom', 'Standard']
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### controlCatalogId
- **Type**: typing.Optional[str]


# ListControlsResponse

### controlMetadataList
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.ControlMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListKeywordsForDataSourceRequest

### source
- **Type**: typing.Literal['AWS_API_Call', 'AWS_Cloudtrail', 'AWS_Config', 'AWS_Security_Hub', 'MANUAL']
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListKeywordsForDataSourceResponse

### keywords
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListNotificationsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListNotificationsResponse

### notifications
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.Notification]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# ManualEvidence

### s3ResourcePath
- **Type**: typing.Optional[str]

### textResponse
- **Type**: typing.Optional[str]

### evidenceFileName
- **Type**: typing.Optional[str]


# Notification

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RegisterAccountRequest

### kmsKey
- **Type**: typing.Optional[str]

### delegatedAdminAccount
- **Type**: typing.Optional[str]


# RegisterAccountResponse

### status
- **Type**: typing.Literal['ACTIVE', 'INACTIVE', 'PENDING_ACTIVATION']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# RegisterOrganizationAdminAccountRequest

### adminAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterOrganizationAdminAccountResponse

### adminAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### organizationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# Resource

### arn
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]

### complianceCheck
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


# Role

### roleType
- **Type**: typing.Literal['PROCESS_OWNER', 'RESOURCE_OWNER']
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# Scope

### awsAccounts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.auditmanager_classes.AWSAccount]]

### awsServices
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.auditmanager_classes.AWSService]]


# ScopeOutput

### awsAccounts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.AWSAccount]]

### awsServices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.AWSService]]


# ScopeUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServiceMetadata

### name
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### category
- **Type**: typing.Optional[str]


# Settings

### isAwsOrgEnabled
- **Type**: typing.Optional[bool]

### snsTopic
- **Type**: typing.Optional[str]

### defaultAssessmentReportsDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentReportsDestination]

### defaultProcessOwners
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.Role]]

### kmsKey
- **Type**: typing.Optional[str]

### evidenceFinderEnablement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.EvidenceFinderEnablement]

### deregistrationPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.DeregistrationPolicy]

### defaultExportDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.DefaultExportDestination]


# SourceKeyword

### keywordInputType
- **Type**: typing.Optional[typing.Literal['INPUT_TEXT', 'SELECT_FROM_LIST', 'UPLOAD_FILE']]

### keywordValue
- **Type**: typing.Optional[str]


# StartAssessmentFrameworkShareRequest

### frameworkId
- **Type**: <class 'str'>
- **Required**: Yes

### destinationAccount
- **Type**: <class 'str'>
- **Required**: Yes

### destinationRegion
- **Type**: <class 'str'>
- **Required**: Yes

### comment
- **Type**: typing.Optional[str]


# StartAssessmentFrameworkShareResponse

### assessmentFrameworkShareRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentFrameworkShareRequest'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# URL

### hyperlinkName
- **Type**: typing.Optional[str]

### link
- **Type**: typing.Optional[str]


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAssessmentControlRequest

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes

### controlSetId
- **Type**: <class 'str'>
- **Required**: Yes

### controlId
- **Type**: <class 'str'>
- **Required**: Yes

### controlStatus
- **Type**: typing.Optional[typing.Literal['INACTIVE', 'REVIEWED', 'UNDER_REVIEW']]

### commentBody
- **Type**: typing.Optional[str]


# UpdateAssessmentControlResponse

### control
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentControl'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAssessmentControlSetStatusRequest

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes

### controlSetId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'REVIEWED', 'UNDER_REVIEW']
- **Required**: Yes

### comment
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateAssessmentControlSetStatusResponse

### controlSet
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentControlSet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAssessmentFrameworkControlSet

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UpdateAssessmentFrameworkRequest

### frameworkId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### controlSets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.auditmanager_classes.UpdateAssessmentFrameworkControlSet]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### complianceType
- **Type**: typing.Optional[str]


# UpdateAssessmentFrameworkResponse

### framework
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.Framework'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAssessmentFrameworkShareRequest

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### requestType
- **Type**: typing.Literal['RECEIVED', 'SENT']
- **Required**: Yes

### action
- **Type**: typing.Literal['ACCEPT', 'DECLINE', 'REVOKE']
- **Required**: Yes


# UpdateAssessmentFrameworkShareResponse

### assessmentFrameworkShareRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentFrameworkShareRequest'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAssessmentRequest

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes

### scope
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ScopeUnion'>
- **Required**: Yes

### assessmentName
- **Type**: typing.Optional[str]

### assessmentDescription
- **Type**: typing.Optional[str]

### assessmentReportsDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentReportsDestination]

### roles
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.auditmanager_classes.Role]]


# UpdateAssessmentResponse

### assessment
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.Assessment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAssessmentStatusRequest

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'INACTIVE']
- **Required**: Yes


# UpdateAssessmentStatusResponse

### assessment
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.Assessment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateControlRequest

### controlId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### controlMappingSources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.auditmanager_classes.ControlMappingSource]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### testingInformation
- **Type**: typing.Optional[str]

### actionPlanTitle
- **Type**: typing.Optional[str]

### actionPlanInstructions
- **Type**: typing.Optional[str]


# UpdateControlResponse

### control
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.Control'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSettingsRequest

### snsTopic
- **Type**: typing.Optional[str]

### defaultAssessmentReportsDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentReportsDestination]

### defaultProcessOwners
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.auditmanager_classes.Role]]

### kmsKey
- **Type**: typing.Optional[str]

### evidenceFinderEnabled
- **Type**: typing.Optional[bool]

### deregistrationPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.DeregistrationPolicy]

### defaultExportDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.DefaultExportDestination]


# UpdateSettingsResponse

### settings
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.Settings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


# ValidateAssessmentReportIntegrityRequest

### s3RelativePath
- **Type**: <class 'str'>
- **Required**: Yes


# ValidateAssessmentReportIntegrityResponse

### signatureValid
- **Type**: <class 'bool'>
- **Required**: Yes

### signatureAlgorithm
- **Type**: <class 'str'>
- **Required**: Yes

### signatureDateTime
- **Type**: <class 'str'>
- **Required**: Yes

### signatureKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### validationErrors
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadata'>
- **Required**: Yes


