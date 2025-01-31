# auditmanager_classes

# AWSAccountTypeDef

### id
- **Type**: typing.Optional[str]

### emailAddress
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# AWSServiceTypeDef

### serviceName
- **Type**: typing.Optional[str]


# AssessmentControlSetTypeDef

### id
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'REVIEWED', 'UNDER_REVIEW']]

### roles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.RoleTypeDef]]

### controls
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentControlTypeDef]]

### delegations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.DelegationTypeDef]]

### systemEvidenceCount
- **Type**: typing.Optional[int]

### manualEvidenceCount
- **Type**: typing.Optional[int]


# AssessmentControlTypeDef

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['INACTIVE', 'REVIEWED', 'UNDER_REVIEW']]

### response
- **Type**: typing.Optional[typing.Literal['AUTOMATE', 'DEFER', 'IGNORE', 'MANUAL']]

### comments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.ControlCommentTypeDef]]

### evidenceSources
- **Type**: typing.Optional[typing.List[str]]

### evidenceCount
- **Type**: typing.Optional[int]

### assessmentReportEvidenceCount
- **Type**: typing.Optional[int]


# AssessmentEvidenceFolderTypeDef

### name
- **Type**: typing.Optional[str]

### date
- **Type**: typing.Optional[datetime.datetime]

### assessmentId
- **Type**: typing.Optional[str]

### controlSetId
- **Type**: typing.Optional[str]

### controlId
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### dataSource
- **Type**: typing.Optional[str]

### author
- **Type**: typing.Optional[str]

### totalEvidence
- **Type**: typing.Optional[int]

### assessmentReportSelectionCount
- **Type**: typing.Optional[int]

### controlName
- **Type**: typing.Optional[str]

### evidenceResourcesIncludedCount
- **Type**: typing.Optional[int]

### evidenceByTypeConfigurationDataCount
- **Type**: typing.Optional[int]

### evidenceByTypeManualCount
- **Type**: typing.Optional[int]

### evidenceByTypeComplianceCheckCount
- **Type**: typing.Optional[int]

### evidenceByTypeComplianceCheckIssuesCount
- **Type**: typing.Optional[int]

### evidenceByTypeUserActivityCount
- **Type**: typing.Optional[int]

### evidenceAwsServiceSourceCount
- **Type**: typing.Optional[int]


# AssessmentFrameworkMetadataTypeDef

### arn
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['Custom', 'Standard']]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### logo
- **Type**: typing.Optional[str]

### complianceType
- **Type**: typing.Optional[str]

### controlsCount
- **Type**: typing.Optional[int]

### controlSetsCount
- **Type**: typing.Optional[int]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# AssessmentFrameworkShareRequestTypeDef

### id
- **Type**: typing.Optional[str]

### frameworkId
- **Type**: typing.Optional[str]

### frameworkName
- **Type**: typing.Optional[str]

### frameworkDescription
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DECLINED', 'EXPIRED', 'EXPIRING', 'FAILED', 'REPLICATING', 'REVOKED', 'SHARED']]

### sourceAccount
- **Type**: typing.Optional[str]

### destinationAccount
- **Type**: typing.Optional[str]

### destinationRegion
- **Type**: typing.Optional[str]

### expirationTime
- **Type**: typing.Optional[datetime.datetime]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdated
- **Type**: typing.Optional[datetime.datetime]

### comment
- **Type**: typing.Optional[str]

### standardControlsCount
- **Type**: typing.Optional[int]

### customControlsCount
- **Type**: typing.Optional[int]

### complianceType
- **Type**: typing.Optional[str]


# AssessmentFrameworkTypeDef

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.FrameworkMetadataTypeDef]

### controlSets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentControlSetTypeDef]]


# AssessmentMetadataItemTypeDef

### name
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### complianceType
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### roles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.RoleTypeDef]]

### delegations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.DelegationTypeDef]]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdated
- **Type**: typing.Optional[datetime.datetime]


# AssessmentMetadataTypeDef

### name
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### complianceType
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### assessmentReportsDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentReportsDestinationTypeDef]

### scope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.ScopeOutputTypeDef]

### roles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.RoleTypeDef]]

### delegations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.DelegationTypeDef]]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdated
- **Type**: typing.Optional[datetime.datetime]


# AssessmentReportEvidenceErrorTypeDef

### evidenceId
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]


# AssessmentReportMetadataTypeDef

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### assessmentId
- **Type**: typing.Optional[str]

### assessmentName
- **Type**: typing.Optional[str]

### author
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'FAILED', 'IN_PROGRESS']]

### creationTime
- **Type**: typing.Optional[datetime.datetime]


# AssessmentReportTypeDef

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### awsAccountId
- **Type**: typing.Optional[str]

### assessmentId
- **Type**: typing.Optional[str]

### assessmentName
- **Type**: typing.Optional[str]

### author
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'FAILED', 'IN_PROGRESS']]

### creationTime
- **Type**: typing.Optional[datetime.datetime]


# AssessmentReportsDestinationTypeDef

### destinationType
- **Type**: typing.Optional[typing.Literal['S3']]

### destination
- **Type**: typing.Optional[str]


# AssessmentTypeDef

### arn
- **Type**: typing.Optional[str]

### awsAccount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.AWSAccountTypeDef]

### metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentMetadataTypeDef]

### framework
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentFrameworkTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# AssociateAssessmentReportEvidenceFolderRequestRequestTypeDef

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes

### evidenceFolderId
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchAssociateAssessmentReportEvidenceRequestRequestTypeDef

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes

### evidenceFolderId
- **Type**: <class 'str'>
- **Required**: Yes

### evidenceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchAssociateAssessmentReportEvidenceResponseTypeDef

### evidenceIds
- **Type**: typing.List[str]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentReportEvidenceErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchCreateDelegationByAssessmentErrorTypeDef

### createDelegationRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.CreateDelegationRequestTypeDef]

### errorCode
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]


# BatchCreateDelegationByAssessmentRequestRequestTypeDef

### createDelegationRequests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.auditmanager_classes.CreateDelegationRequestTypeDef]
- **Required**: Yes

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes


# BatchCreateDelegationByAssessmentResponseTypeDef

### delegations
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.DelegationTypeDef]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.BatchCreateDelegationByAssessmentErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDeleteDelegationByAssessmentErrorTypeDef

### delegationId
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]


# BatchDeleteDelegationByAssessmentRequestRequestTypeDef

### delegationIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes


# BatchDeleteDelegationByAssessmentResponseTypeDef

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.BatchDeleteDelegationByAssessmentErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDisassociateAssessmentReportEvidenceRequestRequestTypeDef

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes

### evidenceFolderId
- **Type**: <class 'str'>
- **Required**: Yes

### evidenceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchDisassociateAssessmentReportEvidenceResponseTypeDef

### evidenceIds
- **Type**: typing.List[str]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentReportEvidenceErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchImportEvidenceToAssessmentControlErrorTypeDef

### manualEvidence
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.ManualEvidenceTypeDef]

### errorCode
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]


# BatchImportEvidenceToAssessmentControlRequestRequestTypeDef

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.auditmanager_classes.ManualEvidenceTypeDef]
- **Required**: Yes


# BatchImportEvidenceToAssessmentControlResponseTypeDef

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.BatchImportEvidenceToAssessmentControlErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ChangeLogTypeDef

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


# ControlCommentTypeDef

### authorName
- **Type**: typing.Optional[str]

### commentBody
- **Type**: typing.Optional[str]

### postedDate
- **Type**: typing.Optional[datetime.datetime]


# ControlDomainInsightsTypeDef

### name
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### controlsCountByNoncompliantEvidence
- **Type**: typing.Optional[int]

### totalControlsCount
- **Type**: typing.Optional[int]

### evidenceInsights
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.EvidenceInsightsTypeDef]

### lastUpdated
- **Type**: typing.Optional[datetime.datetime]


# ControlInsightsMetadataByAssessmentItemTypeDef

### name
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### evidenceInsights
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.EvidenceInsightsTypeDef]

### controlSetName
- **Type**: typing.Optional[str]

### lastUpdated
- **Type**: typing.Optional[datetime.datetime]


# ControlInsightsMetadataItemTypeDef

### name
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### evidenceInsights
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.EvidenceInsightsTypeDef]

### lastUpdated
- **Type**: typing.Optional[datetime.datetime]


# ControlMappingSourceTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.SourceKeywordTypeDef]

### sourceFrequency
- **Type**: typing.Optional[typing.Literal['DAILY', 'MONTHLY', 'WEEKLY']]

### troubleshootingText
- **Type**: typing.Optional[str]


# ControlMetadataTypeDef

### arn
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### controlSources
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# ControlSetTypeDef

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### controls
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.ControlTypeDef]]


# ControlTypeDef

### arn
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['Core', 'Custom', 'Standard']]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### testingInformation
- **Type**: typing.Optional[str]

### actionPlanTitle
- **Type**: typing.Optional[str]

### actionPlanInstructions
- **Type**: typing.Optional[str]

### controlSources
- **Type**: typing.Optional[str]

### controlMappingSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.ControlMappingSourceTypeDef]]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### lastUpdatedBy
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### state
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'END_OF_SUPPORT']]


# CreateAssessmentFrameworkControlSetTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### controls
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.auditmanager_classes.CreateAssessmentFrameworkControlTypeDef]]


# CreateAssessmentFrameworkControlTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# CreateAssessmentFrameworkRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### controlSets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.auditmanager_classes.CreateAssessmentFrameworkControlSetTypeDef]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### complianceType
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateAssessmentFrameworkResponseTypeDef

### framework
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.FrameworkTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAssessmentReportRequestRequestTypeDef

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


# CreateAssessmentReportResponseTypeDef

### assessmentReport
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentReportTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAssessmentRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### assessmentReportsDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentReportsDestinationTypeDef'>
- **Required**: Yes

### scope
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ScopeTypeDef'>
- **Required**: Yes

### roles
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.auditmanager_classes.RoleTypeDef]
- **Required**: Yes

### frameworkId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateAssessmentResponseTypeDef

### assessment
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateControlMappingSourceTypeDef

### sourceName
- **Type**: typing.Optional[str]

### sourceDescription
- **Type**: typing.Optional[str]

### sourceSetUpOption
- **Type**: typing.Optional[typing.Literal['Procedural_Controls_Mapping', 'System_Controls_Mapping']]

### sourceType
- **Type**: typing.Optional[typing.Literal['AWS_API_Call', 'AWS_Cloudtrail', 'AWS_Config', 'AWS_Security_Hub', 'Common_Control', 'Core_Control', 'MANUAL']]

### sourceKeyword
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.SourceKeywordTypeDef]

### sourceFrequency
- **Type**: typing.Optional[typing.Literal['DAILY', 'MONTHLY', 'WEEKLY']]

### troubleshootingText
- **Type**: typing.Optional[str]


# CreateControlRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### controlMappingSources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.auditmanager_classes.CreateControlMappingSourceTypeDef]
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


# CreateControlResponseTypeDef

### control
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ControlTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDelegationRequestTypeDef

### comment
- **Type**: typing.Optional[str]

### controlSetId
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### roleType
- **Type**: typing.Optional[typing.Literal['PROCESS_OWNER', 'RESOURCE_OWNER']]


# DefaultExportDestinationTypeDef

### destinationType
- **Type**: typing.Optional[typing.Literal['S3']]

### destination
- **Type**: typing.Optional[str]


# DelegationMetadataTypeDef

### id
- **Type**: typing.Optional[str]

### assessmentName
- **Type**: typing.Optional[str]

### assessmentId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'IN_PROGRESS', 'UNDER_REVIEW']]

### roleArn
- **Type**: typing.Optional[str]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### controlSetName
- **Type**: typing.Optional[str]


# DelegationTypeDef

### id
- **Type**: typing.Optional[str]

### assessmentName
- **Type**: typing.Optional[str]

### assessmentId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'IN_PROGRESS', 'UNDER_REVIEW']]

### roleArn
- **Type**: typing.Optional[str]

### roleType
- **Type**: typing.Optional[typing.Literal['PROCESS_OWNER', 'RESOURCE_OWNER']]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdated
- **Type**: typing.Optional[datetime.datetime]

### controlSetId
- **Type**: typing.Optional[str]

### comment
- **Type**: typing.Optional[str]

### createdBy
- **Type**: typing.Optional[str]


# DeleteAssessmentFrameworkRequestRequestTypeDef

### frameworkId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAssessmentFrameworkShareRequestRequestTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### requestType
- **Type**: typing.Literal['RECEIVED', 'SENT']
- **Required**: Yes


# DeleteAssessmentReportRequestRequestTypeDef

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes

### assessmentReportId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAssessmentRequestRequestTypeDef

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteControlRequestRequestTypeDef

### controlId
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterAccountResponseTypeDef

### status
- **Type**: typing.Literal['ACTIVE', 'INACTIVE', 'PENDING_ACTIVATION']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeregisterOrganizationAdminAccountRequestRequestTypeDef

### adminAccountId
- **Type**: typing.Optional[str]


# DeregistrationPolicyTypeDef

### deleteResources
- **Type**: typing.Optional[typing.Literal['ALL', 'DEFAULT']]


# DisassociateAssessmentReportEvidenceFolderRequestRequestTypeDef

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes

### evidenceFolderId
- **Type**: <class 'str'>
- **Required**: Yes


# EvidenceFinderEnablementTypeDef

### eventDataStoreArn
- **Type**: typing.Optional[str]

### enablementStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'DISABLE_IN_PROGRESS', 'ENABLED', 'ENABLE_IN_PROGRESS']]

### backfillStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'IN_PROGRESS', 'NOT_STARTED']]

### error
- **Type**: typing.Optional[str]


# EvidenceInsightsTypeDef

### noncompliantEvidenceCount
- **Type**: typing.Optional[int]

### compliantEvidenceCount
- **Type**: typing.Optional[int]

### inconclusiveEvidenceCount
- **Type**: typing.Optional[int]


# EvidenceTypeDef

### dataSource
- **Type**: typing.Optional[str]

### evidenceAwsAccountId
- **Type**: typing.Optional[str]

### time
- **Type**: typing.Optional[datetime.datetime]

### eventSource
- **Type**: typing.Optional[str]

### eventName
- **Type**: typing.Optional[str]

### evidenceByType
- **Type**: typing.Optional[str]

### resourcesIncluded
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.ResourceTypeDef]]

### attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### iamId
- **Type**: typing.Optional[str]

### complianceCheck
- **Type**: typing.Optional[str]

### awsOrganization
- **Type**: typing.Optional[str]

### awsAccountId
- **Type**: typing.Optional[str]

### evidenceFolderId
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### assessmentReportSelection
- **Type**: typing.Optional[str]


# FrameworkMetadataTypeDef

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### logo
- **Type**: typing.Optional[str]

### complianceType
- **Type**: typing.Optional[str]


# FrameworkTypeDef

### arn
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['Custom', 'Standard']]

### complianceType
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### logo
- **Type**: typing.Optional[str]

### controlSources
- **Type**: typing.Optional[str]

### controlSets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.ControlSetTypeDef]]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### lastUpdatedBy
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# GetAccountStatusResponseTypeDef

### status
- **Type**: typing.Literal['ACTIVE', 'INACTIVE', 'PENDING_ACTIVATION']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAssessmentFrameworkRequestRequestTypeDef

### frameworkId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAssessmentFrameworkResponseTypeDef

### framework
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.FrameworkTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAssessmentReportUrlRequestRequestTypeDef

### assessmentReportId
- **Type**: <class 'str'>
- **Required**: Yes

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAssessmentReportUrlResponseTypeDef

### preSignedUrl
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.URLTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAssessmentRequestRequestTypeDef

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAssessmentResponseTypeDef

### assessment
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentTypeDef'>
- **Required**: Yes

### userRole
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.RoleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetChangeLogsRequestRequestTypeDef

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


# GetChangeLogsResponseTypeDef

### changeLogs
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.ChangeLogTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetControlRequestRequestTypeDef

### controlId
- **Type**: <class 'str'>
- **Required**: Yes


# GetControlResponseTypeDef

### control
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ControlTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDelegationsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetDelegationsResponseTypeDef

### delegations
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.DelegationMetadataTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEvidenceByEvidenceFolderRequestRequestTypeDef

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


# GetEvidenceByEvidenceFolderResponseTypeDef

### evidence
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.EvidenceTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEvidenceFileUploadUrlRequestRequestTypeDef

### fileName
- **Type**: <class 'str'>
- **Required**: Yes


# GetEvidenceFileUploadUrlResponseTypeDef

### evidenceFileName
- **Type**: <class 'str'>
- **Required**: Yes

### uploadUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEvidenceFolderRequestRequestTypeDef

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes

### controlSetId
- **Type**: <class 'str'>
- **Required**: Yes

### evidenceFolderId
- **Type**: <class 'str'>
- **Required**: Yes


# GetEvidenceFolderResponseTypeDef

### evidenceFolder
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentEvidenceFolderTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEvidenceFoldersByAssessmentControlRequestRequestTypeDef

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


# GetEvidenceFoldersByAssessmentControlResponseTypeDef

### evidenceFolders
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentEvidenceFolderTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEvidenceFoldersByAssessmentRequestRequestTypeDef

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetEvidenceFoldersByAssessmentResponseTypeDef

### evidenceFolders
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentEvidenceFolderTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEvidenceRequestRequestTypeDef

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


# GetEvidenceResponseTypeDef

### evidence
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.EvidenceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInsightsByAssessmentRequestRequestTypeDef

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetInsightsByAssessmentResponseTypeDef

### insights
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.InsightsByAssessmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInsightsResponseTypeDef

### insights
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.InsightsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetOrganizationAdminAccountResponseTypeDef

### adminAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### organizationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetServicesInScopeResponseTypeDef

### serviceMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.ServiceMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSettingsRequestRequestTypeDef

### attribute
- **Type**: typing.Literal['ALL', 'DEFAULT_ASSESSMENT_REPORTS_DESTINATION', 'DEFAULT_EXPORT_DESTINATION', 'DEFAULT_PROCESS_OWNERS', 'DEREGISTRATION_POLICY', 'EVIDENCE_FINDER_ENABLEMENT', 'IS_AWS_ORG_ENABLED', 'SNS_TOPIC']
- **Required**: Yes


# GetSettingsResponseTypeDef

### settings
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.SettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InsightsByAssessmentTypeDef

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


# InsightsTypeDef

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


# ListAssessmentControlInsightsByControlDomainRequestRequestTypeDef

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


# ListAssessmentControlInsightsByControlDomainResponseTypeDef

### controlInsightsByAssessment
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.ControlInsightsMetadataByAssessmentItemTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAssessmentFrameworkShareRequestsRequestRequestTypeDef

### requestType
- **Type**: typing.Literal['RECEIVED', 'SENT']
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAssessmentFrameworkShareRequestsResponseTypeDef

### assessmentFrameworkShareRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentFrameworkShareRequestTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAssessmentFrameworksRequestRequestTypeDef

### frameworkType
- **Type**: typing.Literal['Custom', 'Standard']
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAssessmentFrameworksResponseTypeDef

### frameworkMetadataList
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentFrameworkMetadataTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAssessmentReportsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAssessmentReportsResponseTypeDef

### assessmentReports
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentReportMetadataTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAssessmentsRequestRequestTypeDef

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAssessmentsResponseTypeDef

### assessmentMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentMetadataItemTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListControlDomainInsightsByAssessmentRequestRequestTypeDef

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListControlDomainInsightsByAssessmentResponseTypeDef

### controlDomainInsights
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.ControlDomainInsightsTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListControlDomainInsightsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListControlDomainInsightsResponseTypeDef

### controlDomainInsights
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.ControlDomainInsightsTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListControlInsightsByControlDomainRequestRequestTypeDef

### controlDomainId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListControlInsightsByControlDomainResponseTypeDef

### controlInsightsMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.ControlInsightsMetadataItemTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListControlsRequestRequestTypeDef

### controlType
- **Type**: typing.Literal['Core', 'Custom', 'Standard']
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### controlCatalogId
- **Type**: typing.Optional[str]


# ListControlsResponseTypeDef

### controlMetadataList
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.ControlMetadataTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListKeywordsForDataSourceRequestRequestTypeDef

### source
- **Type**: typing.Literal['AWS_API_Call', 'AWS_Cloudtrail', 'AWS_Config', 'AWS_Security_Hub', 'MANUAL']
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListKeywordsForDataSourceResponseTypeDef

### keywords
- **Type**: typing.List[str]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListNotificationsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListNotificationsResponseTypeDef

### notifications
- **Type**: typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.NotificationTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ManualEvidenceTypeDef

### s3ResourcePath
- **Type**: typing.Optional[str]

### textResponse
- **Type**: typing.Optional[str]

### evidenceFileName
- **Type**: typing.Optional[str]


# NotificationTypeDef

### id
- **Type**: typing.Optional[str]

### assessmentId
- **Type**: typing.Optional[str]

### assessmentName
- **Type**: typing.Optional[str]

### controlSetId
- **Type**: typing.Optional[str]

### controlSetName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### eventTime
- **Type**: typing.Optional[datetime.datetime]

### source
- **Type**: typing.Optional[str]


# RegisterAccountRequestRequestTypeDef

### kmsKey
- **Type**: typing.Optional[str]

### delegatedAdminAccount
- **Type**: typing.Optional[str]


# RegisterAccountResponseTypeDef

### status
- **Type**: typing.Literal['ACTIVE', 'INACTIVE', 'PENDING_ACTIVATION']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegisterOrganizationAdminAccountRequestRequestTypeDef

### adminAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterOrganizationAdminAccountResponseTypeDef

### adminAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### organizationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResourceTypeDef

### arn
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]

### complianceCheck
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


# RoleTypeDef

### roleType
- **Type**: typing.Literal['PROCESS_OWNER', 'RESOURCE_OWNER']
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# ScopeOutputTypeDef

### awsAccounts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.AWSAccountTypeDef]]

### awsServices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.AWSServiceTypeDef]]


# ScopeTypeDef

### awsAccounts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.auditmanager_classes.AWSAccountTypeDef]]

### awsServices
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.auditmanager_classes.AWSServiceTypeDef]]


# ServiceMetadataTypeDef

### name
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### category
- **Type**: typing.Optional[str]


# SettingsTypeDef

### isAwsOrgEnabled
- **Type**: typing.Optional[bool]

### snsTopic
- **Type**: typing.Optional[str]

### defaultAssessmentReportsDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentReportsDestinationTypeDef]

### defaultProcessOwners
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.auditmanager_classes.RoleTypeDef]]

### kmsKey
- **Type**: typing.Optional[str]

### evidenceFinderEnablement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.EvidenceFinderEnablementTypeDef]

### deregistrationPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.DeregistrationPolicyTypeDef]

### defaultExportDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.DefaultExportDestinationTypeDef]


# SourceKeywordTypeDef

### keywordInputType
- **Type**: typing.Optional[typing.Literal['INPUT_TEXT', 'SELECT_FROM_LIST', 'UPLOAD_FILE']]

### keywordValue
- **Type**: typing.Optional[str]


# StartAssessmentFrameworkShareRequestRequestTypeDef

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


# StartAssessmentFrameworkShareResponseTypeDef

### assessmentFrameworkShareRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentFrameworkShareRequestTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# URLTypeDef

### hyperlinkName
- **Type**: typing.Optional[str]

### link
- **Type**: typing.Optional[str]


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAssessmentControlRequestRequestTypeDef

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


# UpdateAssessmentControlResponseTypeDef

### control
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentControlTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAssessmentControlSetStatusRequestRequestTypeDef

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


# UpdateAssessmentControlSetStatusResponseTypeDef

### controlSet
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentControlSetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAssessmentFrameworkControlSetTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### controls
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.auditmanager_classes.CreateAssessmentFrameworkControlTypeDef]
- **Required**: Yes

### id
- **Type**: typing.Optional[str]


# UpdateAssessmentFrameworkRequestRequestTypeDef

### frameworkId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### controlSets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.auditmanager_classes.UpdateAssessmentFrameworkControlSetTypeDef]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### complianceType
- **Type**: typing.Optional[str]


# UpdateAssessmentFrameworkResponseTypeDef

### framework
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.FrameworkTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAssessmentFrameworkShareRequestRequestTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### requestType
- **Type**: typing.Literal['RECEIVED', 'SENT']
- **Required**: Yes

### action
- **Type**: typing.Literal['ACCEPT', 'DECLINE', 'REVOKE']
- **Required**: Yes


# UpdateAssessmentFrameworkShareResponseTypeDef

### assessmentFrameworkShareRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentFrameworkShareRequestTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAssessmentRequestRequestTypeDef

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes

### scope
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ScopeTypeDef'>
- **Required**: Yes

### assessmentName
- **Type**: typing.Optional[str]

### assessmentDescription
- **Type**: typing.Optional[str]

### assessmentReportsDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentReportsDestinationTypeDef]

### roles
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.auditmanager_classes.RoleTypeDef]]


# UpdateAssessmentResponseTypeDef

### assessment
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAssessmentStatusRequestRequestTypeDef

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'INACTIVE']
- **Required**: Yes


# UpdateAssessmentStatusResponseTypeDef

### assessment
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateControlRequestRequestTypeDef

### controlId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### controlMappingSources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.auditmanager_classes.ControlMappingSourceTypeDef]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### testingInformation
- **Type**: typing.Optional[str]

### actionPlanTitle
- **Type**: typing.Optional[str]

### actionPlanInstructions
- **Type**: typing.Optional[str]


# UpdateControlResponseTypeDef

### control
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ControlTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSettingsRequestRequestTypeDef

### snsTopic
- **Type**: typing.Optional[str]

### defaultAssessmentReportsDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.AssessmentReportsDestinationTypeDef]

### defaultProcessOwners
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.auditmanager_classes.RoleTypeDef]]

### kmsKey
- **Type**: typing.Optional[str]

### evidenceFinderEnabled
- **Type**: typing.Optional[bool]

### deregistrationPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.DeregistrationPolicyTypeDef]

### defaultExportDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.auditmanager_classes.DefaultExportDestinationTypeDef]


# UpdateSettingsResponseTypeDef

### settings
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.SettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ValidateAssessmentReportIntegrityRequestRequestTypeDef

### s3RelativePath
- **Type**: <class 'str'>
- **Required**: Yes


# ValidateAssessmentReportIntegrityResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.auditmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


