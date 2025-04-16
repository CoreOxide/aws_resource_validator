# Inspector2 Classes

# Account

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResourceStatus'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DISABLED', 'DISABLING', 'ENABLED', 'ENABLING', 'SUSPENDED', 'SUSPENDING']
- **Required**: Yes


# AccountAggregation

### findingType
- **Type**: typing.Optional[typing.Literal['CODE_VULNERABILITY', 'NETWORK_REACHABILITY', 'PACKAGE_VULNERABILITY']]

### resourceType
- **Type**: typing.Optional[typing.Literal['AWS_EC2_INSTANCE', 'AWS_ECR_CONTAINER_IMAGE', 'AWS_LAMBDA_FUNCTION']]

### sortBy
- **Type**: typing.Optional[typing.Literal['ALL', 'CRITICAL', 'HIGH']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# AccountAggregationResponse

### accountId
- **Type**: typing.Optional[str]

### exploitAvailableCount
- **Type**: typing.Optional[int]

### fixAvailableCount
- **Type**: typing.Optional[int]

### severityCounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.SeverityCounts]


# AccountState

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceState
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResourceState'>
- **Required**: Yes

### state
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.State'>
- **Required**: Yes


# AggregationRequest

### accountAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.AccountAggregation]

### amiAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.AmiAggregation]

### awsEcrContainerAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.AwsEcrContainerAggregation]

### ec2InstanceAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.Ec2InstanceAggregation]

### findingTypeAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.FindingTypeAggregation]

### imageLayerAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.ImageLayerAggregation]

### lambdaFunctionAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.LambdaFunctionAggregation]

### lambdaLayerAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.LambdaLayerAggregation]

### packageAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PackageAggregation]

### repositoryAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.RepositoryAggregation]

### titleAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.TitleAggregation]


# AggregationResponse

### accountAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.AccountAggregationResponse]

### amiAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.AmiAggregationResponse]

### awsEcrContainerAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.AwsEcrContainerAggregationResponse]

### ec2InstanceAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.Ec2InstanceAggregationResponse]

### findingTypeAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.FindingTypeAggregationResponse]

### imageLayerAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.ImageLayerAggregationResponse]

### lambdaFunctionAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.LambdaFunctionAggregationResponse]

### lambdaLayerAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.LambdaLayerAggregationResponse]

### packageAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PackageAggregationResponse]

### repositoryAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.RepositoryAggregationResponse]

### titleAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.TitleAggregationResponse]


# AmiAggregation

### amis
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### sortBy
- **Type**: typing.Optional[typing.Literal['AFFECTED_INSTANCES', 'ALL', 'CRITICAL', 'HIGH']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# AmiAggregationResponse

### ami
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### affectedInstances
- **Type**: typing.Optional[int]

### severityCounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.SeverityCounts]


# AssociateMemberRequest

### accountId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateMemberResponse

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes


# AtigData

### firstSeen
- **Type**: typing.Optional[datetime.datetime]

### lastSeen
- **Type**: typing.Optional[datetime.datetime]

### targets
- **Type**: typing.Optional[typing.List[str]]

### ttps
- **Type**: typing.Optional[typing.List[str]]


# AutoEnable

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEc2InstanceDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsEcrContainerAggregation

### architectures
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### imageShas
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### imageTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### repositories
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### resourceIds
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### sortBy
- **Type**: typing.Optional[typing.Literal['ALL', 'CRITICAL', 'HIGH']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# AwsEcrContainerAggregationResponse

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### architecture
- **Type**: typing.Optional[str]

### imageSha
- **Type**: typing.Optional[str]

### imageTags
- **Type**: typing.Optional[typing.List[str]]

### repository
- **Type**: typing.Optional[str]

### severityCounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.SeverityCounts]


# AwsEcrContainerImageDetails

### imageHash
- **Type**: <class 'str'>
- **Required**: Yes

### registry
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### architecture
- **Type**: typing.Optional[str]

### author
- **Type**: typing.Optional[str]

### imageTags
- **Type**: typing.Optional[typing.List[str]]

### platform
- **Type**: typing.Optional[str]

### pushedAt
- **Type**: typing.Optional[datetime.datetime]


# AwsLambdaFunctionDetails

### codeSha256
- **Type**: <class 'str'>
- **Required**: Yes

### executionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### functionName
- **Type**: <class 'str'>
- **Required**: Yes

### runtime
- **Type**: typing.Literal['DOTNETCORE_3_1', 'DOTNET_6', 'DOTNET_7', 'GO_1_X', 'JAVA_11', 'JAVA_17', 'JAVA_8', 'JAVA_8_AL2', 'NODEJS', 'NODEJS_12_X', 'NODEJS_14_X', 'NODEJS_16_X', 'NODEJS_18_X', 'PYTHON_3_10', 'PYTHON_3_11', 'PYTHON_3_7', 'PYTHON_3_8', 'PYTHON_3_9', 'RUBY_2_7', 'RUBY_3_2', 'UNSUPPORTED']
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### architectures
- **Type**: typing.Optional[typing.List[typing.Literal['ARM64', 'X86_64']]]

### lastModifiedAt
- **Type**: typing.Optional[datetime.datetime]

### layers
- **Type**: typing.Optional[typing.List[str]]

### packageType
- **Type**: typing.Optional[typing.Literal['IMAGE', 'ZIP']]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.LambdaVpcConfig]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetAccountStatusRequest

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]


# BatchGetAccountStatusResponse

### accounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.AccountState]
- **Required**: Yes

### failedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.FailedAccount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetCodeSnippetRequest

### findingArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetCodeSnippetResponse

### codeSnippetResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.CodeSnippetResult]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.CodeSnippetError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetFindingDetailsRequest

### findingArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetFindingDetailsResponse

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.FindingDetailsError]
- **Required**: Yes

### findingDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.FindingDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetFreeTrialInfoRequest

### accountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetFreeTrialInfoResponse

### accounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.FreeTrialAccountInfo]
- **Required**: Yes

### failedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.FreeTrialInfoError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetMemberEc2DeepInspectionStatusRequest

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]


# BatchGetMemberEc2DeepInspectionStatusResponse

### accountIds
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.MemberAccountEc2DeepInspectionStatusState]
- **Required**: Yes

### failedAccountIds
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.FailedMemberAccountEc2DeepInspectionStatusState]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes


# BatchUpdateMemberEc2DeepInspectionStatusRequest

### accountIds
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.MemberAccountEc2DeepInspectionStatus]
- **Required**: Yes


# BatchUpdateMemberEc2DeepInspectionStatusResponse

### accountIds
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.MemberAccountEc2DeepInspectionStatusState]
- **Required**: Yes

### failedAccountIds
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.FailedMemberAccountEc2DeepInspectionStatusState]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes


# Blob

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelFindingsReportRequest

### reportId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelFindingsReportResponse

### reportId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes


# CancelSbomExportRequest

### reportId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelSbomExportResponse

### reportId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes


# CisCheckAggregation

### scanArn
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### checkDescription
- **Type**: typing.Optional[str]

### checkId
- **Type**: typing.Optional[str]

### level
- **Type**: typing.Optional[typing.Literal['LEVEL_1', 'LEVEL_2']]

### platform
- **Type**: typing.Optional[str]

### statusCounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.StatusCounts]

### title
- **Type**: typing.Optional[str]


# CisDateFilter

### earliestScanStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.Timestamp]

### latestScanStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.Timestamp]


# CisFindingStatusFilter

### comparison
- **Type**: typing.Literal['EQUALS']
- **Required**: Yes

### value
- **Type**: typing.Literal['FAILED', 'PASSED', 'SKIPPED']
- **Required**: Yes


# CisNumberFilter

### lowerInclusive
- **Type**: typing.Optional[int]

### upperInclusive
- **Type**: typing.Optional[int]


# CisResultStatusFilter

### comparison
- **Type**: typing.Literal['EQUALS']
- **Required**: Yes

### value
- **Type**: typing.Literal['FAILED', 'PASSED', 'SKIPPED']
- **Required**: Yes


# CisScan

### scanArn
- **Type**: <class 'str'>
- **Required**: Yes

### scanConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### failedChecks
- **Type**: typing.Optional[int]

### scanDate
- **Type**: typing.Optional[datetime.datetime]

### scanName
- **Type**: typing.Optional[str]

### scheduledBy
- **Type**: typing.Optional[str]

### securityLevel
- **Type**: typing.Optional[typing.Literal['LEVEL_1', 'LEVEL_2']]

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'IN_PROGRESS']]

### targets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.CisTargets]

### totalChecks
- **Type**: typing.Optional[int]


# CisScanConfiguration

### scanConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ownerId
- **Type**: typing.Optional[str]

### scanName
- **Type**: typing.Optional[str]

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.ScheduleOutput]

### securityLevel
- **Type**: typing.Optional[typing.Literal['LEVEL_1', 'LEVEL_2']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### targets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.CisTargets]


# CisScanResultDetails

### scanArn
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### checkDescription
- **Type**: typing.Optional[str]

### checkId
- **Type**: typing.Optional[str]

### findingArn
- **Type**: typing.Optional[str]

### level
- **Type**: typing.Optional[typing.Literal['LEVEL_1', 'LEVEL_2']]

### platform
- **Type**: typing.Optional[str]

### remediation
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'PASSED', 'SKIPPED']]

### statusReason
- **Type**: typing.Optional[str]

### targetResourceId
- **Type**: typing.Optional[str]

### title
- **Type**: typing.Optional[str]


# CisScanResultDetailsFilterCriteria

### checkIdFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilter]]

### findingArnFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilter]]

### findingStatusFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisFindingStatusFilter]]

### securityLevelFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisSecurityLevelFilter]]

### titleFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilter]]


# CisScanResultsAggregatedByChecksFilterCriteria

### accountIdFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilter]]

### checkIdFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilter]]

### failedResourcesFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisNumberFilter]]

### platformFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilter]]

### securityLevelFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisSecurityLevelFilter]]

### titleFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilter]]


# CisScanResultsAggregatedByTargetResourceFilterCriteria

### accountIdFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilter]]

### checkIdFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilter]]

### failedChecksFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisNumberFilter]]

### platformFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilter]]

### statusFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisResultStatusFilter]]

### targetResourceIdFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilter]]

### targetResourceTagFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.TagFilter]]

### targetStatusFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisTargetStatusFilter]]

### targetStatusReasonFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisTargetStatusReasonFilter]]


# CisScanStatusFilter

### comparison
- **Type**: typing.Literal['EQUALS']
- **Required**: Yes

### value
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'IN_PROGRESS']
- **Required**: Yes


# CisSecurityLevelFilter

### comparison
- **Type**: typing.Literal['EQUALS']
- **Required**: Yes

### value
- **Type**: typing.Literal['LEVEL_1', 'LEVEL_2']
- **Required**: Yes


# CisSessionMessage

### cisRuleDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.Blob'>
- **Required**: Yes

### ruleId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ERROR', 'FAILED', 'INFORMATIONAL', 'NOT_APPLICABLE', 'NOT_EVALUATED', 'PASSED', 'UNKNOWN']
- **Required**: Yes


# CisStringFilter

### comparison
- **Type**: typing.Literal['EQUALS', 'NOT_EQUALS', 'PREFIX']
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# CisTargetResourceAggregation

### scanArn
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### platform
- **Type**: typing.Optional[str]

### statusCounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.StatusCounts]

### targetResourceId
- **Type**: typing.Optional[str]

### targetResourceTags
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### targetStatus
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'TIMED_OUT']]

### targetStatusReason
- **Type**: typing.Optional[typing.Literal['SCAN_IN_PROGRESS', 'SSM_UNMANAGED', 'UNSUPPORTED_OS']]


# CisTargetStatusFilter

### comparison
- **Type**: typing.Literal['EQUALS']
- **Required**: Yes

### value
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'TIMED_OUT']
- **Required**: Yes


# CisTargetStatusReasonFilter

### comparison
- **Type**: typing.Literal['EQUALS']
- **Required**: Yes

### value
- **Type**: typing.Literal['SCAN_IN_PROGRESS', 'SSM_UNMANAGED', 'UNSUPPORTED_OS']
- **Required**: Yes


# CisTargets

### accountIds
- **Type**: typing.Optional[typing.List[str]]

### targetResourceTags
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


# CisaData

### action
- **Type**: typing.Optional[str]

### dateAdded
- **Type**: typing.Optional[datetime.datetime]

### dateDue
- **Type**: typing.Optional[datetime.datetime]


# CodeFilePath

### endLine
- **Type**: <class 'int'>
- **Required**: Yes

### fileName
- **Type**: <class 'str'>
- **Required**: Yes

### filePath
- **Type**: <class 'str'>
- **Required**: Yes

### startLine
- **Type**: <class 'int'>
- **Required**: Yes


# CodeLine

### content
- **Type**: <class 'str'>
- **Required**: Yes

### lineNumber
- **Type**: <class 'int'>
- **Required**: Yes


# CodeSnippetError

### errorCode
- **Type**: typing.Literal['ACCESS_DENIED', 'CODE_SNIPPET_NOT_FOUND', 'INTERNAL_ERROR', 'INVALID_INPUT']
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### findingArn
- **Type**: <class 'str'>
- **Required**: Yes


# CodeSnippetResult

### codeSnippet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.CodeLine]]

### endLine
- **Type**: typing.Optional[int]

### findingArn
- **Type**: typing.Optional[str]

### startLine
- **Type**: typing.Optional[int]

### suggestedFixes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.SuggestedFix]]


# CodeVulnerabilityDetails

### cwes
- **Type**: typing.List[str]
- **Required**: Yes

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes

### detectorName
- **Type**: <class 'str'>
- **Required**: Yes

### filePath
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.CodeFilePath'>
- **Required**: Yes

### detectorTags
- **Type**: typing.Optional[typing.List[str]]

### referenceUrls
- **Type**: typing.Optional[typing.List[str]]

### ruleId
- **Type**: typing.Optional[str]

### sourceLambdaLayerArn
- **Type**: typing.Optional[str]


# ComputePlatform

### product
- **Type**: typing.Optional[str]

### vendor
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]


# Counts

### count
- **Type**: typing.Optional[int]

### groupKey
- **Type**: typing.Optional[typing.Literal['ACCOUNT_ID', 'ECR_REPOSITORY_NAME', 'RESOURCE_TYPE', 'SCAN_STATUS_CODE', 'SCAN_STATUS_REASON']]


# CoverageDateFilter

### endInclusive
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.Timestamp]

### startInclusive
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.Timestamp]


# CoverageFilterCriteria

### accountId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CoverageStringFilter]]

### ec2InstanceTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CoverageMapFilter]]

### ecrImageTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CoverageStringFilter]]

### ecrRepositoryName
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CoverageStringFilter]]

### imagePulledAt
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CoverageDateFilter]]

### lambdaFunctionName
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CoverageStringFilter]]

### lambdaFunctionRuntime
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CoverageStringFilter]]

### lambdaFunctionTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CoverageMapFilter]]

### lastScannedAt
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CoverageDateFilter]]

### resourceId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CoverageStringFilter]]

### resourceType
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CoverageStringFilter]]

### scanMode
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CoverageStringFilter]]

### scanStatusCode
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CoverageStringFilter]]

### scanStatusReason
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CoverageStringFilter]]

### scanType
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CoverageStringFilter]]


# CoverageMapFilter

### comparison
- **Type**: typing.Literal['EQUALS']
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[str]


# CoverageStringFilter

### comparison
- **Type**: typing.Literal['EQUALS', 'NOT_EQUALS']
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# CoveredResource

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: typing.Literal['AWS_EC2_INSTANCE', 'AWS_ECR_CONTAINER_IMAGE', 'AWS_ECR_REPOSITORY', 'AWS_LAMBDA_FUNCTION']
- **Required**: Yes

### scanType
- **Type**: typing.Literal['CODE', 'NETWORK', 'PACKAGE']
- **Required**: Yes

### lastScannedAt
- **Type**: typing.Optional[datetime.datetime]

### resourceMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.ResourceScanMetadata]

### scanMode
- **Type**: typing.Optional[typing.Literal['EC2_AGENTLESS', 'EC2_SSM_AGENT_BASED']]

### scanStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.ScanStatus]


# CreateCisScanConfigurationRequest

### scanName
- **Type**: <class 'str'>
- **Required**: Yes

### schedule
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ScheduleUnion'>
- **Required**: Yes

### securityLevel
- **Type**: typing.Literal['LEVEL_1', 'LEVEL_2']
- **Required**: Yes

### targets
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.CreateCisTargets'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateCisScanConfigurationResponse

### scanConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCisTargets

### accountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### targetResourceTags
- **Type**: typing.Mapping[str, typing.Sequence[str]]
- **Required**: Yes


# CreateFilterRequest

### action
- **Type**: typing.Literal['NONE', 'SUPPRESS']
- **Required**: Yes

### filterCriteria
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.FilterCriteriaUnion'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### reason
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateFilterResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFindingsReportRequest

### reportFormat
- **Type**: typing.Literal['CSV', 'JSON']
- **Required**: Yes

### s3Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.Destination'>
- **Required**: Yes

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.FilterCriteriaUnion]


# CreateFindingsReportResponse

### reportId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSbomExportRequest

### reportFormat
- **Type**: typing.Literal['CYCLONEDX_1_4', 'SPDX_2_3']
- **Required**: Yes

### s3Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.Destination'>
- **Required**: Yes

### resourceFilterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.ResourceFilterCriteriaUnion]


# CreateSbomExportResponse

### reportId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes


# Cvss2

### baseScore
- **Type**: typing.Optional[float]

### scoringVector
- **Type**: typing.Optional[str]


# Cvss3

### baseScore
- **Type**: typing.Optional[float]

### scoringVector
- **Type**: typing.Optional[str]


# CvssScore

### baseScore
- **Type**: <class 'float'>
- **Required**: Yes

### scoringVector
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes


# CvssScoreAdjustment

### metric
- **Type**: <class 'str'>
- **Required**: Yes

### reason
- **Type**: <class 'str'>
- **Required**: Yes


# CvssScoreDetails

### score
- **Type**: <class 'float'>
- **Required**: Yes

### scoreSource
- **Type**: <class 'str'>
- **Required**: Yes

### scoringVector
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### adjustments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.CvssScoreAdjustment]]

### cvssSource
- **Type**: typing.Optional[str]


# DailySchedule

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.Time'>
- **Required**: Yes


# DateFilter

### endInclusive
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.Timestamp]

### startInclusive
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.Timestamp]


# DateFilterOutput

### endInclusive
- **Type**: typing.Optional[datetime.datetime]

### startInclusive
- **Type**: typing.Optional[datetime.datetime]


# DelegatedAdmin

### accountId
- **Type**: typing.Optional[str]

### relationshipStatus
- **Type**: typing.Optional[typing.Literal['ACCOUNT_SUSPENDED', 'CANNOT_CREATE_DETECTOR_IN_ORG_MASTER', 'CREATED', 'DELETED', 'DISABLED', 'EMAIL_VERIFICATION_FAILED', 'EMAIL_VERIFICATION_IN_PROGRESS', 'ENABLED', 'INVITED', 'REGION_DISABLED', 'REMOVED', 'RESIGNED']]


# DelegatedAdminAccount

### accountId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DISABLE_IN_PROGRESS', 'ENABLED']]


# DeleteCisScanConfigurationRequest

### scanConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCisScanConfigurationResponse

### scanConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteFilterRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFilterResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeOrganizationConfigurationResponse

### autoEnable
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.AutoEnable'>
- **Required**: Yes

### maxAccountLimitReached
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes


# Destination

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### keyPrefix
- **Type**: typing.Optional[str]


# DisableDelegatedAdminAccountRequest

### delegatedAdminAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DisableDelegatedAdminAccountResponse

### delegatedAdminAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes


# DisableRequest

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### resourceTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['EC2', 'ECR', 'LAMBDA', 'LAMBDA_CODE']]]


# DisableResponse

### accounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.Account]
- **Required**: Yes

### failedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.FailedAccount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateMemberRequest

### accountId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateMemberResponse

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes


# Ec2Configuration

### scanMode
- **Type**: typing.Literal['EC2_HYBRID', 'EC2_SSM_AGENT_BASED']
- **Required**: Yes


# Ec2ConfigurationState

### scanModeState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.Ec2ScanModeState]


# Ec2InstanceAggregation

### amis
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### instanceIds
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### instanceTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.MapFilter]]

### operatingSystems
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### sortBy
- **Type**: typing.Optional[typing.Literal['ALL', 'CRITICAL', 'HIGH', 'NETWORK_FINDINGS']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# Ec2InstanceAggregationResponse

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### ami
- **Type**: typing.Optional[str]

### instanceTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### networkFindings
- **Type**: typing.Optional[int]

### operatingSystem
- **Type**: typing.Optional[str]

### severityCounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.SeverityCounts]


# Ec2Metadata

### amiId
- **Type**: typing.Optional[str]

### platform
- **Type**: typing.Optional[typing.Literal['LINUX', 'MACOS', 'UNKNOWN', 'WINDOWS']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# Ec2ScanModeState

### scanMode
- **Type**: typing.Optional[typing.Literal['EC2_HYBRID', 'EC2_SSM_AGENT_BASED']]

### scanModeStatus
- **Type**: typing.Optional[typing.Literal['PENDING', 'SUCCESS']]


# EcrConfiguration

### rescanDuration
- **Type**: typing.Literal['DAYS_14', 'DAYS_180', 'DAYS_30', 'DAYS_60', 'DAYS_90', 'LIFETIME']
- **Required**: Yes

### pullDateRescanDuration
- **Type**: typing.Optional[typing.Literal['DAYS_14', 'DAYS_180', 'DAYS_30', 'DAYS_60', 'DAYS_90']]


# EcrConfigurationState

### rescanDurationState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.EcrRescanDurationState]


# EcrContainerImageMetadata

### imagePulledAt
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.List[str]]


# EcrRepositoryMetadata

### name
- **Type**: typing.Optional[str]

### scanFrequency
- **Type**: typing.Optional[typing.Literal['CONTINUOUS_SCAN', 'MANUAL', 'SCAN_ON_PUSH']]


# EcrRescanDurationState

### pullDateRescanDuration
- **Type**: typing.Optional[typing.Literal['DAYS_14', 'DAYS_180', 'DAYS_30', 'DAYS_60', 'DAYS_90']]

### rescanDuration
- **Type**: typing.Optional[typing.Literal['DAYS_14', 'DAYS_180', 'DAYS_30', 'DAYS_60', 'DAYS_90', 'LIFETIME']]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'SUCCESS']]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# EnableDelegatedAdminAccountRequest

### delegatedAdminAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# EnableDelegatedAdminAccountResponse

### delegatedAdminAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes


# EnableRequest

### resourceTypes
- **Type**: typing.Sequence[typing.Literal['EC2', 'ECR', 'LAMBDA', 'LAMBDA_CODE']]
- **Required**: Yes

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### clientToken
- **Type**: typing.Optional[str]


# EnableResponse

### accounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.Account]
- **Required**: Yes

### failedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.FailedAccount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes


# Epss

### score
- **Type**: typing.Optional[float]


# EpssDetails

### score
- **Type**: typing.Optional[float]


# Evidence

### evidenceDetail
- **Type**: typing.Optional[str]

### evidenceRule
- **Type**: typing.Optional[str]

### severity
- **Type**: typing.Optional[str]


# ExploitObserved

### firstSeen
- **Type**: typing.Optional[datetime.datetime]

### lastSeen
- **Type**: typing.Optional[datetime.datetime]


# ExploitabilityDetails

### lastKnownExploitAt
- **Type**: typing.Optional[datetime.datetime]


# FailedAccount

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### errorCode
- **Type**: typing.Literal['ACCESS_DENIED', 'ACCOUNT_IS_ISOLATED', 'ALREADY_ENABLED', 'DISABLE_IN_PROGRESS', 'DISASSOCIATE_ALL_MEMBERS', 'EC2_SSM_ASSOCIATION_VERSION_LIMIT_EXCEEDED', 'EC2_SSM_RESOURCE_DATA_SYNC_LIMIT_EXCEEDED', 'ENABLE_IN_PROGRESS', 'EVENTBRIDGE_THROTTLED', 'EVENTBRIDGE_UNAVAILABLE', 'INTERNAL_ERROR', 'RESOURCE_NOT_FOUND', 'RESOURCE_SCAN_NOT_DISABLED', 'SSM_THROTTLED', 'SSM_UNAVAILABLE', 'SUSPEND_IN_PROGRESS']
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### resourceStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.ResourceStatus]

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'DISABLING', 'ENABLED', 'ENABLING', 'SUSPENDED', 'SUSPENDING']]


# FailedMemberAccountEc2DeepInspectionStatusState

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### ec2ScanStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'DISABLING', 'ENABLED', 'ENABLING', 'SUSPENDED', 'SUSPENDING']]

### errorMessage
- **Type**: typing.Optional[str]


# Filter

### action
- **Type**: typing.Literal['NONE', 'SUPPRESS']
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### criteria
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.FilterCriteriaOutput'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ownerId
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### reason
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# FilterCriteria

### awsAccountId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### codeVulnerabilityDetectorName
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### codeVulnerabilityDetectorTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### codeVulnerabilityFilePath
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### componentId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### componentType
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### ec2InstanceImageId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### ec2InstanceSubnetId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### ec2InstanceVpcId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### ecrImageArchitecture
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### ecrImageHash
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### ecrImagePushedAt
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.DateFilter]]

### ecrImageRegistry
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### ecrImageRepositoryName
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### ecrImageTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### epssScore
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.NumberFilter]]

### exploitAvailable
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### findingArn
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### findingStatus
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### findingType
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### firstObservedAt
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.DateFilter]]

### fixAvailable
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### inspectorScore
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.NumberFilter]]

### lambdaFunctionExecutionRoleArn
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### lambdaFunctionLastModifiedAt
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.DateFilter]]

### lambdaFunctionLayers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### lambdaFunctionName
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### lambdaFunctionRuntime
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### lastObservedAt
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.DateFilter]]

### networkProtocol
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### portRange
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.PortRangeFilter]]

### relatedVulnerabilities
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### resourceId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### resourceTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.MapFilter]]

### resourceType
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### severity
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### title
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### updatedAt
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.DateFilter]]

### vendorSeverity
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### vulnerabilityId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### vulnerabilitySource
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### vulnerablePackages
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.PackageFilter]]


# FilterCriteriaOutput

### awsAccountId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### codeVulnerabilityDetectorName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### codeVulnerabilityDetectorTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### codeVulnerabilityFilePath
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### componentId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### componentType
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### ec2InstanceImageId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### ec2InstanceSubnetId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### ec2InstanceVpcId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### ecrImageArchitecture
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### ecrImageHash
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### ecrImagePushedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.DateFilterOutput]]

### ecrImageRegistry
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### ecrImageRepositoryName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### ecrImageTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### epssScore
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.NumberFilter]]

### exploitAvailable
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### findingArn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### findingStatus
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### findingType
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### firstObservedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.DateFilterOutput]]

### fixAvailable
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### inspectorScore
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.NumberFilter]]

### lambdaFunctionExecutionRoleArn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### lambdaFunctionLastModifiedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.DateFilterOutput]]

### lambdaFunctionLayers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### lambdaFunctionName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### lambdaFunctionRuntime
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### lastObservedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.DateFilterOutput]]

### networkProtocol
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### portRange
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.PortRangeFilter]]

### relatedVulnerabilities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### resourceId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### resourceTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.MapFilter]]

### resourceType
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### severity
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### title
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### updatedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.DateFilterOutput]]

### vendorSeverity
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### vulnerabilityId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### vulnerabilitySource
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### vulnerablePackages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.PackageFilter]]


# FilterCriteriaUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Finding

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FindingDetail

### cisaData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.CisaData]

### cwes
- **Type**: typing.Optional[typing.List[str]]

### epssScore
- **Type**: typing.Optional[float]

### evidences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.Evidence]]

### exploitObserved
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.ExploitObserved]

### findingArn
- **Type**: typing.Optional[str]

### referenceUrls
- **Type**: typing.Optional[typing.List[str]]

### riskScore
- **Type**: typing.Optional[int]

### tools
- **Type**: typing.Optional[typing.List[str]]

### ttps
- **Type**: typing.Optional[typing.List[str]]


# FindingDetailsError

### errorCode
- **Type**: typing.Literal['ACCESS_DENIED', 'FINDING_DETAILS_NOT_FOUND', 'INTERNAL_ERROR', 'INVALID_INPUT']
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### findingArn
- **Type**: <class 'str'>
- **Required**: Yes


# FindingTypeAggregation

### findingType
- **Type**: typing.Optional[typing.Literal['CODE_VULNERABILITY', 'NETWORK_REACHABILITY', 'PACKAGE_VULNERABILITY']]

### resourceType
- **Type**: typing.Optional[typing.Literal['AWS_EC2_INSTANCE', 'AWS_ECR_CONTAINER_IMAGE', 'AWS_LAMBDA_FUNCTION']]

### sortBy
- **Type**: typing.Optional[typing.Literal['ALL', 'CRITICAL', 'HIGH']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# FindingTypeAggregationResponse

### accountId
- **Type**: typing.Optional[str]

### exploitAvailableCount
- **Type**: typing.Optional[int]

### fixAvailableCount
- **Type**: typing.Optional[int]

### severityCounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.SeverityCounts]


# FreeTrialAccountInfo

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### freeTrialInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.FreeTrialInfo]
- **Required**: Yes


# FreeTrialInfo

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FreeTrialInfoError

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: typing.Literal['ACCESS_DENIED', 'INTERNAL_ERROR']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# GetCisScanReportRequest

### scanArn
- **Type**: <class 'str'>
- **Required**: Yes

### reportFormat
- **Type**: typing.Optional[typing.Literal['CSV', 'PDF']]

### targetAccounts
- **Type**: typing.Optional[typing.Sequence[str]]


# GetCisScanReportResponse

### status
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### url
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes


# GetCisScanResultDetailsRequest

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### scanArn
- **Type**: <class 'str'>
- **Required**: Yes

### targetResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.CisScanResultDetailsFilterCriteria]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['CHECK_ID', 'STATUS']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# GetCisScanResultDetailsRequestPaginate

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### scanArn
- **Type**: <class 'str'>
- **Required**: Yes

### targetResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.CisScanResultDetailsFilterCriteria]

### sortBy
- **Type**: typing.Optional[typing.Literal['CHECK_ID', 'STATUS']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PaginatorConfig]


# GetCisScanResultDetailsResponse

### scanResultDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.CisScanResultDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetConfigurationResponse

### ec2Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.Ec2ConfigurationState'>
- **Required**: Yes

### ecrConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.EcrConfigurationState'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes


# GetDelegatedAdminAccountResponse

### delegatedAdmin
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.DelegatedAdmin'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes


# GetEc2DeepInspectionConfigurationResponse

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### orgPackagePaths
- **Type**: typing.List[str]
- **Required**: Yes

### packagePaths
- **Type**: typing.List[str]
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVATED', 'DEACTIVATED', 'FAILED', 'PENDING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes


# GetEncryptionKeyRequest

### resourceType
- **Type**: typing.Literal['AWS_EC2_INSTANCE', 'AWS_ECR_CONTAINER_IMAGE', 'AWS_ECR_REPOSITORY', 'AWS_LAMBDA_FUNCTION']
- **Required**: Yes

### scanType
- **Type**: typing.Literal['CODE', 'NETWORK', 'PACKAGE']
- **Required**: Yes


# GetEncryptionKeyResponse

### kmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes


# GetFindingsReportStatusRequest

### reportId
- **Type**: typing.Optional[str]


# GetFindingsReportStatusResponse

### destination
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.Destination'>
- **Required**: Yes

### errorCode
- **Type**: typing.Literal['BUCKET_NOT_FOUND', 'INCOMPATIBLE_BUCKET_REGION', 'INTERNAL_ERROR', 'INVALID_PERMISSIONS', 'MALFORMED_KMS_KEY', 'NO_FINDINGS_FOUND']
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### filterCriteria
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.FilterCriteriaOutput'>
- **Required**: Yes

### reportId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes


# GetMemberRequest

### accountId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMemberResponse

### member
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.Member'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes


# GetSbomExportRequest

### reportId
- **Type**: <class 'str'>
- **Required**: Yes


# ImageLayerAggregation

### layerHashes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### repositories
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### resourceIds
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### sortBy
- **Type**: typing.Optional[typing.Literal['ALL', 'CRITICAL', 'HIGH']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# ImageLayerAggregationResponse

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### layerHash
- **Type**: <class 'str'>
- **Required**: Yes

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### severityCounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.SeverityCounts]


# InspectorScoreDetails

### adjustedCvss
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.CvssScoreDetails]


# LambdaFunctionAggregation

### functionNames
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### functionTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.MapFilter]]

### resourceIds
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### runtimes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### sortBy
- **Type**: typing.Optional[typing.Literal['ALL', 'CRITICAL', 'HIGH']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# LambdaFunctionAggregationResponse

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### functionName
- **Type**: typing.Optional[str]

### lambdaTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### lastModifiedAt
- **Type**: typing.Optional[datetime.datetime]

### runtime
- **Type**: typing.Optional[str]

### severityCounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.SeverityCounts]


# LambdaFunctionMetadata

### functionName
- **Type**: typing.Optional[str]

### functionTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### layers
- **Type**: typing.Optional[typing.List[str]]

### runtime
- **Type**: typing.Optional[typing.Literal['DOTNETCORE_3_1', 'DOTNET_6', 'DOTNET_7', 'GO_1_X', 'JAVA_11', 'JAVA_17', 'JAVA_8', 'JAVA_8_AL2', 'NODEJS', 'NODEJS_12_X', 'NODEJS_14_X', 'NODEJS_16_X', 'NODEJS_18_X', 'PYTHON_3_10', 'PYTHON_3_11', 'PYTHON_3_7', 'PYTHON_3_8', 'PYTHON_3_9', 'RUBY_2_7', 'RUBY_3_2', 'UNSUPPORTED']]


# LambdaLayerAggregation

### functionNames
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### layerArns
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### resourceIds
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### sortBy
- **Type**: typing.Optional[typing.Literal['ALL', 'CRITICAL', 'HIGH']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# LambdaLayerAggregationResponse

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### functionName
- **Type**: <class 'str'>
- **Required**: Yes

### layerArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### severityCounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.SeverityCounts]


# LambdaVpcConfig

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### subnetIds
- **Type**: typing.Optional[typing.List[str]]

### vpcId
- **Type**: typing.Optional[str]


# ListAccountPermissionsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### service
- **Type**: typing.Optional[typing.Literal['EC2', 'ECR', 'LAMBDA']]


# ListAccountPermissionsRequestPaginate

### service
- **Type**: typing.Optional[typing.Literal['EC2', 'ECR', 'LAMBDA']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PaginatorConfig]


# ListAccountPermissionsResponse

### permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.Permission]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCisScanConfigurationsFilterCriteria

### scanConfigurationArnFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilter]]

### scanNameFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilter]]

### targetResourceTagFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.TagFilter]]


# ListCisScanConfigurationsRequest

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.ListCisScanConfigurationsFilterCriteria]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['SCAN_CONFIGURATION_ARN', 'SCAN_NAME']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# ListCisScanConfigurationsRequestPaginate

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.ListCisScanConfigurationsFilterCriteria]

### sortBy
- **Type**: typing.Optional[typing.Literal['SCAN_CONFIGURATION_ARN', 'SCAN_NAME']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PaginatorConfig]


# ListCisScanConfigurationsResponse

### scanConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.CisScanConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCisScanResultsAggregatedByChecksRequest

### scanArn
- **Type**: <class 'str'>
- **Required**: Yes

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.CisScanResultsAggregatedByChecksFilterCriteria]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['CHECK_ID', 'FAILED_COUNTS', 'PLATFORM', 'SECURITY_LEVEL', 'TITLE']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# ListCisScanResultsAggregatedByChecksRequestPaginate

### scanArn
- **Type**: <class 'str'>
- **Required**: Yes

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.CisScanResultsAggregatedByChecksFilterCriteria]

### sortBy
- **Type**: typing.Optional[typing.Literal['CHECK_ID', 'FAILED_COUNTS', 'PLATFORM', 'SECURITY_LEVEL', 'TITLE']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PaginatorConfig]


# ListCisScanResultsAggregatedByChecksResponse

### checkAggregations
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.CisCheckAggregation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCisScanResultsAggregatedByTargetResourceRequest

### scanArn
- **Type**: <class 'str'>
- **Required**: Yes

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.CisScanResultsAggregatedByTargetResourceFilterCriteria]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['ACCOUNT_ID', 'FAILED_COUNTS', 'PLATFORM', 'RESOURCE_ID', 'TARGET_STATUS', 'TARGET_STATUS_REASON']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# ListCisScanResultsAggregatedByTargetResourceRequestPaginate

### scanArn
- **Type**: <class 'str'>
- **Required**: Yes

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.CisScanResultsAggregatedByTargetResourceFilterCriteria]

### sortBy
- **Type**: typing.Optional[typing.Literal['ACCOUNT_ID', 'FAILED_COUNTS', 'PLATFORM', 'RESOURCE_ID', 'TARGET_STATUS', 'TARGET_STATUS_REASON']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PaginatorConfig]


# ListCisScanResultsAggregatedByTargetResourceResponse

### targetResourceAggregations
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.CisTargetResourceAggregation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCisScansFilterCriteria

### failedChecksFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisNumberFilter]]

### scanArnFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilter]]

### scanAtFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisDateFilter]]

### scanConfigurationArnFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilter]]

### scanNameFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilter]]

### scanStatusFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisScanStatusFilter]]

### scheduledByFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilter]]

### targetAccountIdFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilter]]

### targetResourceIdFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilter]]

### targetResourceTagFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.TagFilter]]


# ListCisScansRequest

### detailLevel
- **Type**: typing.Optional[typing.Literal['MEMBER', 'ORGANIZATION']]

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.ListCisScansFilterCriteria]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['FAILED_CHECKS', 'SCAN_START_DATE', 'SCHEDULED_BY', 'STATUS']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# ListCisScansRequestPaginate

### detailLevel
- **Type**: typing.Optional[typing.Literal['MEMBER', 'ORGANIZATION']]

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.ListCisScansFilterCriteria]

### sortBy
- **Type**: typing.Optional[typing.Literal['FAILED_CHECKS', 'SCAN_START_DATE', 'SCHEDULED_BY', 'STATUS']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PaginatorConfig]


# ListCisScansResponse

### scans
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.CisScan]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCoverageRequest

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.CoverageFilterCriteria]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListCoverageRequestPaginate

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.CoverageFilterCriteria]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PaginatorConfig]


# ListCoverageResponse

### coveredResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.CoveredResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCoverageStatisticsRequest

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.CoverageFilterCriteria]

### groupBy
- **Type**: typing.Optional[typing.Literal['ACCOUNT_ID', 'ECR_REPOSITORY_NAME', 'RESOURCE_TYPE', 'SCAN_STATUS_CODE', 'SCAN_STATUS_REASON']]

### nextToken
- **Type**: typing.Optional[str]


# ListCoverageStatisticsRequestPaginate

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.CoverageFilterCriteria]

### groupBy
- **Type**: typing.Optional[typing.Literal['ACCOUNT_ID', 'ECR_REPOSITORY_NAME', 'RESOURCE_TYPE', 'SCAN_STATUS_CODE', 'SCAN_STATUS_REASON']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PaginatorConfig]


# ListCoverageStatisticsResponse

### countsByGroup
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.Counts]
- **Required**: Yes

### totalCounts
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDelegatedAdminAccountsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDelegatedAdminAccountsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PaginatorConfig]


# ListDelegatedAdminAccountsResponse

### delegatedAdminAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.DelegatedAdminAccount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFiltersRequest

### action
- **Type**: typing.Optional[typing.Literal['NONE', 'SUPPRESS']]

### arns
- **Type**: typing.Optional[typing.Sequence[str]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListFiltersRequestPaginate

### action
- **Type**: typing.Optional[typing.Literal['NONE', 'SUPPRESS']]

### arns
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PaginatorConfig]


# ListFiltersResponse

### filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.Filter]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFindingAggregationsRequest

### aggregationType
- **Type**: typing.Literal['ACCOUNT', 'AMI', 'AWS_EC2_INSTANCE', 'AWS_ECR_CONTAINER', 'AWS_LAMBDA_FUNCTION', 'FINDING_TYPE', 'IMAGE_LAYER', 'LAMBDA_LAYER', 'PACKAGE', 'REPOSITORY', 'TITLE']
- **Required**: Yes

### accountIds
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### aggregationRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.AggregationRequest]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListFindingAggregationsRequestPaginate

### aggregationType
- **Type**: typing.Literal['ACCOUNT', 'AMI', 'AWS_EC2_INSTANCE', 'AWS_ECR_CONTAINER', 'AWS_LAMBDA_FUNCTION', 'FINDING_TYPE', 'IMAGE_LAYER', 'LAMBDA_LAYER', 'PACKAGE', 'REPOSITORY', 'TITLE']
- **Required**: Yes

### accountIds
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### aggregationRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.AggregationRequest]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PaginatorConfig]


# ListFindingAggregationsResponse

### aggregationType
- **Type**: typing.Literal['ACCOUNT', 'AMI', 'AWS_EC2_INSTANCE', 'AWS_ECR_CONTAINER', 'AWS_LAMBDA_FUNCTION', 'FINDING_TYPE', 'IMAGE_LAYER', 'LAMBDA_LAYER', 'PACKAGE', 'REPOSITORY', 'TITLE']
- **Required**: Yes

### responses
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.AggregationResponse]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFindingsRequest

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.FilterCriteriaUnion]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.SortCriteria]


# ListFindingsRequestPaginate

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.FilterCriteriaUnion]

### sortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.SortCriteria]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PaginatorConfig]


# ListFindingsResponse

### findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.Finding]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMembersRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### onlyAssociated
- **Type**: typing.Optional[bool]


# ListMembersRequestPaginate

### onlyAssociated
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PaginatorConfig]


# ListMembersResponse

### members
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.Member]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes


# ListUsageTotalsRequest

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListUsageTotalsRequestPaginate

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PaginatorConfig]


# ListUsageTotalsResponse

### totals
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.UsageTotal]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# MapFilter

### comparison
- **Type**: typing.Literal['EQUALS']
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[str]


# Member

### accountId
- **Type**: typing.Optional[str]

### delegatedAdminAccountId
- **Type**: typing.Optional[str]

### relationshipStatus
- **Type**: typing.Optional[typing.Literal['ACCOUNT_SUSPENDED', 'CANNOT_CREATE_DETECTOR_IN_ORG_MASTER', 'CREATED', 'DELETED', 'DISABLED', 'EMAIL_VERIFICATION_FAILED', 'EMAIL_VERIFICATION_IN_PROGRESS', 'ENABLED', 'INVITED', 'REGION_DISABLED', 'REMOVED', 'RESIGNED']]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# MemberAccountEc2DeepInspectionStatus

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### activateDeepInspection
- **Type**: <class 'bool'>
- **Required**: Yes


# MemberAccountEc2DeepInspectionStatusState

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVATED', 'DEACTIVATED', 'FAILED', 'PENDING']]


# MonthlySchedule

### day
- **Type**: typing.Literal['FRI', 'MON', 'SAT', 'SUN', 'THU', 'TUE', 'WED']
- **Required**: Yes

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.Time'>
- **Required**: Yes


# NetworkPath

### steps
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.Step]]


# NetworkReachabilityDetails

### networkPath
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.NetworkPath'>
- **Required**: Yes

### openPortRange
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.PortRange'>
- **Required**: Yes

### protocol
- **Type**: typing.Literal['TCP', 'UDP']
- **Required**: Yes


# NumberFilter

### lowerInclusive
- **Type**: typing.Optional[float]

### upperInclusive
- **Type**: typing.Optional[float]


# PackageAggregation

### packageNames
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### sortBy
- **Type**: typing.Optional[typing.Literal['ALL', 'CRITICAL', 'HIGH']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# PackageAggregationResponse

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### severityCounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.SeverityCounts]


# PackageFilter

### architecture
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]

### epoch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.NumberFilter]

### filePath
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]

### name
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]

### release
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]

### sourceLambdaLayerArn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]

### sourceLayerHash
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]

### version
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]


# PackageVulnerabilityDetails

### source
- **Type**: <class 'str'>
- **Required**: Yes

### vulnerabilityId
- **Type**: <class 'str'>
- **Required**: Yes

### cvss
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.CvssScore]]

### referenceUrls
- **Type**: typing.Optional[typing.List[str]]

### relatedVulnerabilities
- **Type**: typing.Optional[typing.List[str]]

### sourceUrl
- **Type**: typing.Optional[str]

### vendorCreatedAt
- **Type**: typing.Optional[datetime.datetime]

### vendorSeverity
- **Type**: typing.Optional[str]

### vendorUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### vulnerablePackages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.VulnerablePackage]]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Permission

### operation
- **Type**: typing.Literal['DISABLE_REPOSITORY', 'DISABLE_SCANNING', 'ENABLE_REPOSITORY', 'ENABLE_SCANNING']
- **Required**: Yes

### service
- **Type**: typing.Literal['EC2', 'ECR', 'LAMBDA']
- **Required**: Yes


# PortRange

### begin
- **Type**: <class 'int'>
- **Required**: Yes

### end
- **Type**: <class 'int'>
- **Required**: Yes


# PortRangeFilter

### beginInclusive
- **Type**: typing.Optional[int]

### endInclusive
- **Type**: typing.Optional[int]


# Recommendation

### Url
- **Type**: typing.Optional[str]

### text
- **Type**: typing.Optional[str]


# Remediation

### recommendation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.Recommendation]


# RepositoryAggregation

### repositories
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### sortBy
- **Type**: typing.Optional[typing.Literal['AFFECTED_IMAGES', 'ALL', 'CRITICAL', 'HIGH']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# RepositoryAggregationResponse

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### affectedImages
- **Type**: typing.Optional[int]

### severityCounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.SeverityCounts]


# ResetEncryptionKeyRequest

### resourceType
- **Type**: typing.Literal['AWS_EC2_INSTANCE', 'AWS_ECR_CONTAINER_IMAGE', 'AWS_ECR_REPOSITORY', 'AWS_LAMBDA_FUNCTION']
- **Required**: Yes

### scanType
- **Type**: typing.Literal['CODE', 'NETWORK', 'PACKAGE']
- **Required**: Yes


# ResourceDetails

### awsEc2Instance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.AwsEc2InstanceDetails]

### awsEcrContainerImage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.AwsEcrContainerImageDetails]

### awsLambdaFunction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.AwsLambdaFunctionDetails]


# ResourceFilterCriteria

### accountId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.ResourceStringFilter]]

### ec2InstanceTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.ResourceMapFilter]]

### ecrImageTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.ResourceStringFilter]]

### ecrRepositoryName
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.ResourceStringFilter]]

### lambdaFunctionName
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.ResourceStringFilter]]

### lambdaFunctionTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.ResourceMapFilter]]

### resourceId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.ResourceStringFilter]]

### resourceType
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.ResourceStringFilter]]


# ResourceFilterCriteriaOutput

### accountId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.ResourceStringFilter]]

### ec2InstanceTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.ResourceMapFilter]]

### ecrImageTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.ResourceStringFilter]]

### ecrRepositoryName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.ResourceStringFilter]]

### lambdaFunctionName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.ResourceStringFilter]]

### lambdaFunctionTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.ResourceMapFilter]]

### resourceId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.ResourceStringFilter]]

### resourceType
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.ResourceStringFilter]]


# ResourceFilterCriteriaUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResourceMapFilter

### comparison
- **Type**: typing.Literal['EQUALS']
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[str]


# ResourceScanMetadata

### ec2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.Ec2Metadata]

### ecrImage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.EcrContainerImageMetadata]

### ecrRepository
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.EcrRepositoryMetadata]

### lambdaFunction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.LambdaFunctionMetadata]


# ResourceState

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResourceStatus

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResourceStringFilter

### comparison
- **Type**: typing.Literal['EQUALS', 'NOT_EQUALS']
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


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


# ScanStatus

### reason
- **Type**: typing.Literal['ACCESS_DENIED', 'AGENTLESS_INSTANCE_COLLECTION_TIME_LIMIT_EXCEEDED', 'AGENTLESS_INSTANCE_STORAGE_LIMIT_EXCEEDED', 'DEEP_INSPECTION_COLLECTION_TIME_LIMIT_EXCEEDED', 'DEEP_INSPECTION_DAILY_SSM_INVENTORY_LIMIT_EXCEEDED', 'DEEP_INSPECTION_NO_INVENTORY', 'DEEP_INSPECTION_PACKAGE_COLLECTION_LIMIT_EXCEEDED', 'EC2_INSTANCE_STOPPED', 'EXCLUDED_BY_TAG', 'IMAGE_SIZE_EXCEEDED', 'INTERNAL_ERROR', 'NO_INVENTORY', 'NO_RESOURCES_FOUND', 'PENDING_DISABLE', 'PENDING_INITIAL_SCAN', 'RESOURCE_TERMINATED', 'SCAN_ELIGIBILITY_EXPIRED', 'SCAN_FREQUENCY_MANUAL', 'SCAN_FREQUENCY_SCAN_ON_PUSH', 'STALE_INVENTORY', 'SUCCESSFUL', 'UNMANAGED_EC2_INSTANCE', 'UNSUPPORTED_CONFIG_FILE', 'UNSUPPORTED_MEDIA_TYPE', 'UNSUPPORTED_OS', 'UNSUPPORTED_RUNTIME']
- **Required**: Yes

### statusCode
- **Type**: typing.Literal['ACTIVE', 'INACTIVE']
- **Required**: Yes


# Schedule

### daily
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.DailySchedule]

### monthly
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.MonthlySchedule]

### oneTime
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### weekly
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.WeeklySchedule]


# ScheduleOutput

### daily
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.DailySchedule]

### monthly
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.MonthlySchedule]

### oneTime
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### weekly
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.WeeklyScheduleOutput]


# ScheduleUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SearchVulnerabilitiesFilterCriteria

### vulnerabilityIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# SearchVulnerabilitiesRequest

### filterCriteria
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.SearchVulnerabilitiesFilterCriteria'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchVulnerabilitiesRequestPaginate

### filterCriteria
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.SearchVulnerabilitiesFilterCriteria'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PaginatorConfig]


# SearchVulnerabilitiesResponse

### vulnerabilities
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.Vulnerability]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SendCisSessionHealthRequest

### scanJobId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionToken
- **Type**: <class 'str'>
- **Required**: Yes


# SendCisSessionTelemetryRequest

### messages
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisSessionMessage]
- **Required**: Yes

### scanJobId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionToken
- **Type**: <class 'str'>
- **Required**: Yes


# SeverityCounts

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SortCriteria

### field
- **Type**: typing.Literal['AWS_ACCOUNT_ID', 'COMPONENT_TYPE', 'ECR_IMAGE_PUSHED_AT', 'ECR_IMAGE_REGISTRY', 'ECR_IMAGE_REPOSITORY_NAME', 'EPSS_SCORE', 'FINDING_STATUS', 'FINDING_TYPE', 'FIRST_OBSERVED_AT', 'INSPECTOR_SCORE', 'LAST_OBSERVED_AT', 'NETWORK_PROTOCOL', 'RESOURCE_TYPE', 'SEVERITY', 'VENDOR_SEVERITY', 'VULNERABILITY_ID', 'VULNERABILITY_SOURCE']
- **Required**: Yes

### sortOrder
- **Type**: typing.Literal['ASC', 'DESC']
- **Required**: Yes


# StartCisSessionMessage

### sessionToken
- **Type**: <class 'str'>
- **Required**: Yes


# StartCisSessionRequest

### message
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.StartCisSessionMessage'>
- **Required**: Yes

### scanJobId
- **Type**: <class 'str'>
- **Required**: Yes


# State

### errorCode
- **Type**: typing.Literal['ACCESS_DENIED', 'ACCOUNT_IS_ISOLATED', 'ALREADY_ENABLED', 'DISABLE_IN_PROGRESS', 'DISASSOCIATE_ALL_MEMBERS', 'EC2_SSM_ASSOCIATION_VERSION_LIMIT_EXCEEDED', 'EC2_SSM_RESOURCE_DATA_SYNC_LIMIT_EXCEEDED', 'ENABLE_IN_PROGRESS', 'EVENTBRIDGE_THROTTLED', 'EVENTBRIDGE_UNAVAILABLE', 'INTERNAL_ERROR', 'RESOURCE_NOT_FOUND', 'RESOURCE_SCAN_NOT_DISABLED', 'SSM_THROTTLED', 'SSM_UNAVAILABLE', 'SUSPEND_IN_PROGRESS']
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DISABLED', 'DISABLING', 'ENABLED', 'ENABLING', 'SUSPENDED', 'SUSPENDING']
- **Required**: Yes


# StatusCounts

### failed
- **Type**: typing.Optional[int]

### passed
- **Type**: typing.Optional[int]

### skipped
- **Type**: typing.Optional[int]


# Step

### componentId
- **Type**: <class 'str'>
- **Required**: Yes

### componentType
- **Type**: <class 'str'>
- **Required**: Yes


# StopCisMessageProgress

### errorChecks
- **Type**: typing.Optional[int]

### failedChecks
- **Type**: typing.Optional[int]

### informationalChecks
- **Type**: typing.Optional[int]

### notApplicableChecks
- **Type**: typing.Optional[int]

### notEvaluatedChecks
- **Type**: typing.Optional[int]

### successfulChecks
- **Type**: typing.Optional[int]

### totalChecks
- **Type**: typing.Optional[int]

### unknownChecks
- **Type**: typing.Optional[int]


# StopCisSessionMessage

### progress
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.StopCisMessageProgress'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'INTERRUPTED', 'SUCCESS', 'UNSUPPORTED_OS']
- **Required**: Yes

### benchmarkProfile
- **Type**: typing.Optional[str]

### benchmarkVersion
- **Type**: typing.Optional[str]

### computePlatform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.ComputePlatform]

### reason
- **Type**: typing.Optional[str]


# StopCisSessionRequest

### message
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.StopCisSessionMessage'>
- **Required**: Yes

### scanJobId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionToken
- **Type**: <class 'str'>
- **Required**: Yes


# StringFilter

### comparison
- **Type**: typing.Literal['EQUALS', 'NOT_EQUALS', 'PREFIX']
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# SuggestedFix

### code
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# TagFilter

### comparison
- **Type**: typing.Literal['EQUALS']
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# Time

### timeOfDay
- **Type**: <class 'str'>
- **Required**: Yes

### timezone
- **Type**: <class 'str'>
- **Required**: Yes


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TitleAggregation

### findingType
- **Type**: typing.Optional[typing.Literal['CODE_VULNERABILITY', 'NETWORK_REACHABILITY', 'PACKAGE_VULNERABILITY']]

### resourceType
- **Type**: typing.Optional[typing.Literal['AWS_EC2_INSTANCE', 'AWS_ECR_CONTAINER_IMAGE', 'AWS_LAMBDA_FUNCTION']]

### sortBy
- **Type**: typing.Optional[typing.Literal['ALL', 'CRITICAL', 'HIGH']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]

### titles
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]

### vulnerabilityIds
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilter]]


# TitleAggregationResponse

### title
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### severityCounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.SeverityCounts]

### vulnerabilityId
- **Type**: typing.Optional[str]


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateCisScanConfigurationRequest

### scanConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### scanName
- **Type**: typing.Optional[str]

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.ScheduleUnion]

### securityLevel
- **Type**: typing.Optional[typing.Literal['LEVEL_1', 'LEVEL_2']]

### targets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.UpdateCisTargets]


# UpdateCisScanConfigurationResponse

### scanConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateCisTargets

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### targetResourceTags
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]


# UpdateConfigurationRequest

### ec2Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.Ec2Configuration]

### ecrConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.EcrConfiguration]


# UpdateEc2DeepInspectionConfigurationRequest

### activateDeepInspection
- **Type**: typing.Optional[bool]

### packagePaths
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateEc2DeepInspectionConfigurationResponse

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### orgPackagePaths
- **Type**: typing.List[str]
- **Required**: Yes

### packagePaths
- **Type**: typing.List[str]
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVATED', 'DEACTIVATED', 'FAILED', 'PENDING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEncryptionKeyRequest

### kmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: typing.Literal['AWS_EC2_INSTANCE', 'AWS_ECR_CONTAINER_IMAGE', 'AWS_ECR_REPOSITORY', 'AWS_LAMBDA_FUNCTION']
- **Required**: Yes

### scanType
- **Type**: typing.Literal['CODE', 'NETWORK', 'PACKAGE']
- **Required**: Yes


# UpdateFilterRequest

### filterArn
- **Type**: <class 'str'>
- **Required**: Yes

### action
- **Type**: typing.Optional[typing.Literal['NONE', 'SUPPRESS']]

### description
- **Type**: typing.Optional[str]

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.FilterCriteriaUnion]

### name
- **Type**: typing.Optional[str]

### reason
- **Type**: typing.Optional[str]


# UpdateFilterResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateOrgEc2DeepInspectionConfigurationRequest

### orgPackagePaths
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateOrganizationConfigurationRequest

### autoEnable
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.AutoEnable'>
- **Required**: Yes


# UpdateOrganizationConfigurationResponse

### autoEnable
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.AutoEnable'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadata'>
- **Required**: Yes


# Usage

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UsageTotal

### accountId
- **Type**: typing.Optional[str]

### usage
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.Usage]]


# Vulnerability

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VulnerablePackage

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### arch
- **Type**: typing.Optional[str]

### epoch
- **Type**: typing.Optional[int]

### filePath
- **Type**: typing.Optional[str]

### fixedInVersion
- **Type**: typing.Optional[str]

### packageManager
- **Type**: typing.Optional[typing.Literal['BUNDLER', 'CARGO', 'COMPOSER', 'DOTNET_CORE', 'GEMSPEC', 'GOBINARY', 'GOMOD', 'JAR', 'NODEPKG', 'NPM', 'NUGET', 'OS', 'PIP', 'PIPENV', 'POETRY', 'POM', 'PYTHONPKG', 'YARN']]

### release
- **Type**: typing.Optional[str]

### remediation
- **Type**: typing.Optional[str]

### sourceLambdaLayerArn
- **Type**: typing.Optional[str]

### sourceLayerHash
- **Type**: typing.Optional[str]


# WeeklySchedule

### days
- **Type**: typing.Sequence[typing.Literal['FRI', 'MON', 'SAT', 'SUN', 'THU', 'TUE', 'WED']]
- **Required**: Yes

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.Time'>
- **Required**: Yes


# WeeklyScheduleOutput

### days
- **Type**: typing.List[typing.Literal['FRI', 'MON', 'SAT', 'SUN', 'THU', 'TUE', 'WED']]
- **Required**: Yes

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.Time'>
- **Required**: Yes


