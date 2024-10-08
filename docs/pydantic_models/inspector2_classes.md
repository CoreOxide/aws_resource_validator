# Pydantic Models in inspector2_classes

# AccountAggregationResponseTypeDef

### accountId
- **Type**: typing.Optional[str]

### severityCounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.SeverityCountsTypeDef]


# AccountAggregationTypeDef

### findingType
- **Type**: typing.Optional[typing.Literal['CODE_VULNERABILITY', 'NETWORK_REACHABILITY', 'PACKAGE_VULNERABILITY']]

### resourceType
- **Type**: typing.Optional[typing.Literal['AWS_EC2_INSTANCE', 'AWS_ECR_CONTAINER_IMAGE', 'AWS_LAMBDA_FUNCTION']]

### sortBy
- **Type**: typing.Optional[typing.Literal['ALL', 'CRITICAL', 'HIGH']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# AccountStateTypeDef

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceState
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResourceStateTypeDef'>
- **Required**: Yes

### state
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.StateTypeDef'>
- **Required**: Yes


# AccountTypeDef

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResourceStatusTypeDef'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DISABLED', 'DISABLING', 'ENABLED', 'ENABLING', 'SUSPENDED', 'SUSPENDING']
- **Required**: Yes


# AggregationRequestTypeDef

### accountAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.AccountAggregationTypeDef]

### amiAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.AmiAggregationTypeDef]

### awsEcrContainerAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.AwsEcrContainerAggregationTypeDef]

### ec2InstanceAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.Ec2InstanceAggregationTypeDef]

### findingTypeAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.FindingTypeAggregationTypeDef]

### imageLayerAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.ImageLayerAggregationTypeDef]

### lambdaFunctionAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.LambdaFunctionAggregationTypeDef]

### lambdaLayerAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.LambdaLayerAggregationTypeDef]

### packageAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PackageAggregationTypeDef]

### repositoryAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.RepositoryAggregationTypeDef]

### titleAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.TitleAggregationTypeDef]


# AggregationResponseTypeDef

### accountAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.AccountAggregationResponseTypeDef]

### amiAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.AmiAggregationResponseTypeDef]

### awsEcrContainerAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.AwsEcrContainerAggregationResponseTypeDef]

### ec2InstanceAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.Ec2InstanceAggregationResponseTypeDef]

### findingTypeAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.FindingTypeAggregationResponseTypeDef]

### imageLayerAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.ImageLayerAggregationResponseTypeDef]

### lambdaFunctionAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.LambdaFunctionAggregationResponseTypeDef]

### lambdaLayerAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.LambdaLayerAggregationResponseTypeDef]

### packageAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PackageAggregationResponseTypeDef]

### repositoryAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.RepositoryAggregationResponseTypeDef]

### titleAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.TitleAggregationResponseTypeDef]


# AmiAggregationResponseTypeDef

### ami
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### affectedInstances
- **Type**: typing.Optional[int]

### severityCounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.SeverityCountsTypeDef]


# AmiAggregationTypeDef

### amis
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### sortBy
- **Type**: typing.Optional[typing.Literal['AFFECTED_INSTANCES', 'ALL', 'CRITICAL', 'HIGH']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# AssociateMemberRequestRequestTypeDef

### accountId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateMemberResponseTypeDef

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AtigDataTypeDef

### firstSeen
- **Type**: typing.Optional[datetime.datetime]

### lastSeen
- **Type**: typing.Optional[datetime.datetime]

### targets
- **Type**: typing.Optional[typing.List[str]]

### ttps
- **Type**: typing.Optional[typing.List[str]]


# AutoEnableTypeDef

### ec2
- **Type**: <class 'bool'>
- **Required**: Yes

### ecr
- **Type**: <class 'bool'>
- **Required**: Yes

### lambdaCode
- **Type**: typing.Optional[bool]


# AwsEc2InstanceDetailsTypeDef

### iamInstanceProfileArn
- **Type**: typing.Optional[str]

### imageId
- **Type**: typing.Optional[str]

### ipV4Addresses
- **Type**: typing.Optional[typing.List[str]]

### ipV6Addresses
- **Type**: typing.Optional[typing.List[str]]

### keyName
- **Type**: typing.Optional[str]

### launchedAt
- **Type**: typing.Optional[datetime.datetime]

### platform
- **Type**: typing.Optional[str]

### subnetId
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]

### vpcId
- **Type**: typing.Optional[str]


# AwsEcrContainerAggregationResponseTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.SeverityCountsTypeDef]


# AwsEcrContainerAggregationTypeDef

### architectures
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### imageShas
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### imageTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### repositories
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### resourceIds
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### sortBy
- **Type**: typing.Optional[typing.Literal['ALL', 'CRITICAL', 'HIGH']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# AwsEcrContainerImageDetailsTypeDef

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


# AwsLambdaFunctionDetailsTypeDef

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
- **Type**: typing.Literal['GO_1_X', 'JAVA_11', 'JAVA_17', 'JAVA_8', 'JAVA_8_AL2', 'NODEJS', 'NODEJS_12_X', 'NODEJS_14_X', 'NODEJS_16_X', 'NODEJS_18_X', 'PYTHON_3_10', 'PYTHON_3_7', 'PYTHON_3_8', 'PYTHON_3_9', 'UNSUPPORTED']
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.LambdaVpcConfigTypeDef]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetAccountStatusRequestRequestTypeDef

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]


# BatchGetAccountStatusResponseTypeDef

### accounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.AccountStateTypeDef]
- **Required**: Yes

### failedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.FailedAccountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetCodeSnippetRequestRequestTypeDef

### findingArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetCodeSnippetResponseTypeDef

### codeSnippetResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.CodeSnippetResultTypeDef]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.CodeSnippetErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetFindingDetailsRequestRequestTypeDef

### findingArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetFindingDetailsResponseTypeDef

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.FindingDetailsErrorTypeDef]
- **Required**: Yes

### findingDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.FindingDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetFreeTrialInfoRequestRequestTypeDef

### accountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetFreeTrialInfoResponseTypeDef

### accounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.FreeTrialAccountInfoTypeDef]
- **Required**: Yes

### failedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.FreeTrialInfoErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetMemberEc2DeepInspectionStatusRequestRequestTypeDef

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]


# BatchGetMemberEc2DeepInspectionStatusResponseTypeDef

### accountIds
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.MemberAccountEc2DeepInspectionStatusStateTypeDef]
- **Required**: Yes

### failedAccountIds
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.FailedMemberAccountEc2DeepInspectionStatusStateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchUpdateMemberEc2DeepInspectionStatusRequestRequestTypeDef

### accountIds
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.MemberAccountEc2DeepInspectionStatusTypeDef]
- **Required**: Yes


# BatchUpdateMemberEc2DeepInspectionStatusResponseTypeDef

### accountIds
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.MemberAccountEc2DeepInspectionStatusStateTypeDef]
- **Required**: Yes

### failedAccountIds
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.FailedMemberAccountEc2DeepInspectionStatusStateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CancelFindingsReportRequestRequestTypeDef

### reportId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelFindingsReportResponseTypeDef

### reportId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CancelSbomExportRequestRequestTypeDef

### reportId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelSbomExportResponseTypeDef

### reportId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CisCheckAggregationTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.StatusCountsTypeDef]

### title
- **Type**: typing.Optional[str]


# CisDateFilterTypeDef

### earliestScanStartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### latestScanStartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# CisFindingStatusFilterTypeDef

### comparison
- **Type**: typing.Literal['EQUALS']
- **Required**: Yes

### value
- **Type**: typing.Literal['FAILED', 'PASSED', 'SKIPPED']
- **Required**: Yes


# CisNumberFilterTypeDef

### lowerInclusive
- **Type**: typing.Optional[int]

### upperInclusive
- **Type**: typing.Optional[int]


# CisResultStatusFilterTypeDef

### comparison
- **Type**: typing.Literal['EQUALS']
- **Required**: Yes

### value
- **Type**: typing.Literal['FAILED', 'PASSED', 'SKIPPED']
- **Required**: Yes


# CisScanConfigurationTypeDef

### scanConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ownerId
- **Type**: typing.Optional[str]

### scanName
- **Type**: typing.Optional[str]

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.ScheduleOutputTypeDef]

### securityLevel
- **Type**: typing.Optional[typing.Literal['LEVEL_1', 'LEVEL_2']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### targets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.CisTargetsTypeDef]


# CisScanResultDetailsFilterCriteriaTypeDef

### checkIdFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilterTypeDef]]

### findingArnFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilterTypeDef]]

### findingStatusFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisFindingStatusFilterTypeDef]]

### securityLevelFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisSecurityLevelFilterTypeDef]]

### titleFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilterTypeDef]]


# CisScanResultDetailsTypeDef

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


# CisScanResultsAggregatedByChecksFilterCriteriaTypeDef

### accountIdFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilterTypeDef]]

### checkIdFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilterTypeDef]]

### failedResourcesFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisNumberFilterTypeDef]]

### platformFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilterTypeDef]]

### securityLevelFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisSecurityLevelFilterTypeDef]]

### titleFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilterTypeDef]]


# CisScanResultsAggregatedByTargetResourceFilterCriteriaTypeDef

### accountIdFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilterTypeDef]]

### checkIdFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilterTypeDef]]

### failedChecksFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisNumberFilterTypeDef]]

### platformFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilterTypeDef]]

### statusFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisResultStatusFilterTypeDef]]

### targetResourceIdFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilterTypeDef]]

### targetResourceTagFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.TagFilterTypeDef]]

### targetStatusFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisTargetStatusFilterTypeDef]]

### targetStatusReasonFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisTargetStatusReasonFilterTypeDef]]


# CisScanStatusFilterTypeDef

### comparison
- **Type**: typing.Literal['EQUALS']
- **Required**: Yes

### value
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'IN_PROGRESS']
- **Required**: Yes


# CisScanTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.CisTargetsTypeDef]

### totalChecks
- **Type**: typing.Optional[int]


# CisSecurityLevelFilterTypeDef

### comparison
- **Type**: typing.Literal['EQUALS']
- **Required**: Yes

### value
- **Type**: typing.Literal['LEVEL_1', 'LEVEL_2']
- **Required**: Yes


# CisSessionMessageTypeDef

### cisRuleDetails
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### ruleId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ERROR', 'FAILED', 'INFORMATIONAL', 'NOT_APPLICABLE', 'NOT_EVALUATED', 'PASSED', 'UNKNOWN']
- **Required**: Yes


# CisStringFilterTypeDef

### comparison
- **Type**: typing.Literal['EQUALS', 'NOT_EQUALS', 'PREFIX']
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# CisTargetResourceAggregationTypeDef

### scanArn
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### platform
- **Type**: typing.Optional[str]

### statusCounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.StatusCountsTypeDef]

### targetResourceId
- **Type**: typing.Optional[str]

### targetResourceTags
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### targetStatus
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'TIMED_OUT']]

### targetStatusReason
- **Type**: typing.Optional[typing.Literal['SCAN_IN_PROGRESS', 'SSM_UNMANAGED', 'UNSUPPORTED_OS']]


# CisTargetStatusFilterTypeDef

### comparison
- **Type**: typing.Literal['EQUALS']
- **Required**: Yes

### value
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'TIMED_OUT']
- **Required**: Yes


# CisTargetStatusReasonFilterTypeDef

### comparison
- **Type**: typing.Literal['EQUALS']
- **Required**: Yes

### value
- **Type**: typing.Literal['SCAN_IN_PROGRESS', 'SSM_UNMANAGED', 'UNSUPPORTED_OS']
- **Required**: Yes


# CisTargetsTypeDef

### accountIds
- **Type**: typing.Optional[typing.List[str]]

### targetResourceTags
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


# CisaDataTypeDef

### action
- **Type**: typing.Optional[str]

### dateAdded
- **Type**: typing.Optional[datetime.datetime]

### dateDue
- **Type**: typing.Optional[datetime.datetime]


# CodeFilePathTypeDef

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


# CodeLineTypeDef

### content
- **Type**: <class 'str'>
- **Required**: Yes

### lineNumber
- **Type**: <class 'int'>
- **Required**: Yes


# CodeSnippetErrorTypeDef

### errorCode
- **Type**: typing.Literal['ACCESS_DENIED', 'CODE_SNIPPET_NOT_FOUND', 'INTERNAL_ERROR', 'INVALID_INPUT']
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### findingArn
- **Type**: <class 'str'>
- **Required**: Yes


# CodeSnippetResultTypeDef

### codeSnippet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.CodeLineTypeDef]]

### endLine
- **Type**: typing.Optional[int]

### findingArn
- **Type**: typing.Optional[str]

### startLine
- **Type**: typing.Optional[int]

### suggestedFixes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.SuggestedFixTypeDef]]


# CodeVulnerabilityDetailsTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.CodeFilePathTypeDef'>
- **Required**: Yes

### detectorTags
- **Type**: typing.Optional[typing.List[str]]

### referenceUrls
- **Type**: typing.Optional[typing.List[str]]

### ruleId
- **Type**: typing.Optional[str]

### sourceLambdaLayerArn
- **Type**: typing.Optional[str]


# ComputePlatformTypeDef

### product
- **Type**: typing.Optional[str]

### vendor
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]


# CountsTypeDef

### count
- **Type**: typing.Optional[int]

### groupKey
- **Type**: typing.Optional[typing.Literal['ACCOUNT_ID', 'ECR_REPOSITORY_NAME', 'RESOURCE_TYPE', 'SCAN_STATUS_CODE', 'SCAN_STATUS_REASON']]


# CoverageDateFilterTypeDef

### endInclusive
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### startInclusive
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# CoverageFilterCriteriaTypeDef

### accountId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CoverageStringFilterTypeDef]]

### ec2InstanceTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CoverageMapFilterTypeDef]]

### ecrImageTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CoverageStringFilterTypeDef]]

### ecrRepositoryName
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CoverageStringFilterTypeDef]]

### imagePulledAt
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CoverageDateFilterTypeDef]]

### lambdaFunctionName
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CoverageStringFilterTypeDef]]

### lambdaFunctionRuntime
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CoverageStringFilterTypeDef]]

### lambdaFunctionTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CoverageMapFilterTypeDef]]

### lastScannedAt
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CoverageDateFilterTypeDef]]

### resourceId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CoverageStringFilterTypeDef]]

### resourceType
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CoverageStringFilterTypeDef]]

### scanMode
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CoverageStringFilterTypeDef]]

### scanStatusCode
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CoverageStringFilterTypeDef]]

### scanStatusReason
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CoverageStringFilterTypeDef]]

### scanType
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CoverageStringFilterTypeDef]]


# CoverageMapFilterTypeDef

### comparison
- **Type**: typing.Literal['EQUALS']
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[str]


# CoverageStringFilterTypeDef

### comparison
- **Type**: typing.Literal['EQUALS', 'NOT_EQUALS']
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# CoveredResourceTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.ResourceScanMetadataTypeDef]

### scanMode
- **Type**: typing.Optional[typing.Literal['EC2_AGENTLESS', 'EC2_SSM_AGENT_BASED']]

### scanStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.ScanStatusTypeDef]


# CreateCisScanConfigurationRequestRequestTypeDef

### scanName
- **Type**: <class 'str'>
- **Required**: Yes

### schedule
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ScheduleTypeDef'>
- **Required**: Yes

### securityLevel
- **Type**: typing.Literal['LEVEL_1', 'LEVEL_2']
- **Required**: Yes

### targets
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.CreateCisTargetsTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateCisScanConfigurationResponseTypeDef

### scanConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCisTargetsTypeDef

### accountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### targetResourceTags
- **Type**: typing.Mapping[str, typing.Sequence[str]]
- **Required**: Yes


# CreateFilterRequestRequestTypeDef

### action
- **Type**: typing.Literal['NONE', 'SUPPRESS']
- **Required**: Yes

### filterCriteria
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.FilterCriteriaTypeDef'>
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


# CreateFilterResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFindingsReportRequestRequestTypeDef

### reportFormat
- **Type**: typing.Literal['CSV', 'JSON']
- **Required**: Yes

### s3Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.DestinationTypeDef'>
- **Required**: Yes

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.FilterCriteriaTypeDef]


# CreateFindingsReportResponseTypeDef

### reportId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSbomExportRequestRequestTypeDef

### reportFormat
- **Type**: typing.Literal['CYCLONEDX_1_4', 'SPDX_2_3']
- **Required**: Yes

### s3Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.DestinationTypeDef'>
- **Required**: Yes

### resourceFilterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.ResourceFilterCriteriaTypeDef]


# CreateSbomExportResponseTypeDef

### reportId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# Cvss2TypeDef

### baseScore
- **Type**: typing.Optional[float]

### scoringVector
- **Type**: typing.Optional[str]


# Cvss3TypeDef

### baseScore
- **Type**: typing.Optional[float]

### scoringVector
- **Type**: typing.Optional[str]


# CvssScoreAdjustmentTypeDef

### metric
- **Type**: <class 'str'>
- **Required**: Yes

### reason
- **Type**: <class 'str'>
- **Required**: Yes


# CvssScoreDetailsTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.CvssScoreAdjustmentTypeDef]]

### cvssSource
- **Type**: typing.Optional[str]


# CvssScoreTypeDef

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


# DailyScheduleTypeDef

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.TimeTypeDef'>
- **Required**: Yes


# DateFilterExtraOutputTypeDef

### endInclusive
- **Type**: typing.Optional[datetime.datetime]

### startInclusive
- **Type**: typing.Optional[datetime.datetime]


# DateFilterOutputTypeDef

### endInclusive
- **Type**: typing.Optional[datetime.datetime]

### startInclusive
- **Type**: typing.Optional[datetime.datetime]


# DateFilterTypeDef

### endInclusive
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### startInclusive
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# DelegatedAdminAccountTypeDef

### accountId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DISABLE_IN_PROGRESS', 'ENABLED']]


# DelegatedAdminTypeDef

### accountId
- **Type**: typing.Optional[str]

### relationshipStatus
- **Type**: typing.Optional[typing.Literal['ACCOUNT_SUSPENDED', 'CANNOT_CREATE_DETECTOR_IN_ORG_MASTER', 'CREATED', 'DELETED', 'DISABLED', 'EMAIL_VERIFICATION_FAILED', 'EMAIL_VERIFICATION_IN_PROGRESS', 'ENABLED', 'INVITED', 'REGION_DISABLED', 'REMOVED', 'RESIGNED']]


# DeleteCisScanConfigurationRequestRequestTypeDef

### scanConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCisScanConfigurationResponseTypeDef

### scanConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteFilterRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFilterResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeOrganizationConfigurationResponseTypeDef

### autoEnable
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.AutoEnableTypeDef'>
- **Required**: Yes

### maxAccountLimitReached
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DestinationTypeDef

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### keyPrefix
- **Type**: typing.Optional[str]


# DisableDelegatedAdminAccountRequestRequestTypeDef

### delegatedAdminAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DisableDelegatedAdminAccountResponseTypeDef

### delegatedAdminAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisableRequestRequestTypeDef

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### resourceTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['EC2', 'ECR', 'LAMBDA', 'LAMBDA_CODE']]]


# DisableResponseTypeDef

### accounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.AccountTypeDef]
- **Required**: Yes

### failedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.FailedAccountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateMemberRequestRequestTypeDef

### accountId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateMemberResponseTypeDef

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# Ec2ConfigurationStateTypeDef

### scanModeState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.Ec2ScanModeStateTypeDef]


# Ec2ConfigurationTypeDef

### scanMode
- **Type**: typing.Literal['EC2_HYBRID', 'EC2_SSM_AGENT_BASED']
- **Required**: Yes


# Ec2InstanceAggregationResponseTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.SeverityCountsTypeDef]


# Ec2InstanceAggregationTypeDef

### amis
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### instanceIds
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### instanceTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.MapFilterTypeDef]]

### operatingSystems
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### sortBy
- **Type**: typing.Optional[typing.Literal['ALL', 'CRITICAL', 'HIGH', 'NETWORK_FINDINGS']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# Ec2MetadataTypeDef

### amiId
- **Type**: typing.Optional[str]

### platform
- **Type**: typing.Optional[typing.Literal['LINUX', 'MACOS', 'UNKNOWN', 'WINDOWS']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# Ec2ScanModeStateTypeDef

### scanMode
- **Type**: typing.Optional[typing.Literal['EC2_HYBRID', 'EC2_SSM_AGENT_BASED']]

### scanModeStatus
- **Type**: typing.Optional[typing.Literal['PENDING', 'SUCCESS']]


# EcrConfigurationStateTypeDef

### rescanDurationState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.EcrRescanDurationStateTypeDef]


# EcrConfigurationTypeDef

### rescanDuration
- **Type**: typing.Literal['DAYS_14', 'DAYS_180', 'DAYS_30', 'DAYS_60', 'DAYS_90', 'LIFETIME']
- **Required**: Yes

### pullDateRescanDuration
- **Type**: typing.Optional[typing.Literal['DAYS_14', 'DAYS_180', 'DAYS_30', 'DAYS_60', 'DAYS_90']]


# EcrContainerImageMetadataTypeDef

### imagePulledAt
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.List[str]]


# EcrRepositoryMetadataTypeDef

### name
- **Type**: typing.Optional[str]

### scanFrequency
- **Type**: typing.Optional[typing.Literal['CONTINUOUS_SCAN', 'MANUAL', 'SCAN_ON_PUSH']]


# EcrRescanDurationStateTypeDef

### pullDateRescanDuration
- **Type**: typing.Optional[typing.Literal['DAYS_14', 'DAYS_180', 'DAYS_30', 'DAYS_60', 'DAYS_90']]

### rescanDuration
- **Type**: typing.Optional[typing.Literal['DAYS_14', 'DAYS_180', 'DAYS_30', 'DAYS_60', 'DAYS_90', 'LIFETIME']]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'SUCCESS']]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# EnableDelegatedAdminAccountRequestRequestTypeDef

### delegatedAdminAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# EnableDelegatedAdminAccountResponseTypeDef

### delegatedAdminAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnableRequestRequestTypeDef

### resourceTypes
- **Type**: typing.Sequence[typing.Literal['EC2', 'ECR', 'LAMBDA', 'LAMBDA_CODE']]
- **Required**: Yes

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### clientToken
- **Type**: typing.Optional[str]


# EnableResponseTypeDef

### accounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.AccountTypeDef]
- **Required**: Yes

### failedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.FailedAccountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EpssDetailsTypeDef

### score
- **Type**: typing.Optional[float]


# EpssTypeDef

### score
- **Type**: typing.Optional[float]


# EvidenceTypeDef

### evidenceDetail
- **Type**: typing.Optional[str]

### evidenceRule
- **Type**: typing.Optional[str]

### severity
- **Type**: typing.Optional[str]


# ExploitObservedTypeDef

### firstSeen
- **Type**: typing.Optional[datetime.datetime]

### lastSeen
- **Type**: typing.Optional[datetime.datetime]


# ExploitabilityDetailsTypeDef

### lastKnownExploitAt
- **Type**: typing.Optional[datetime.datetime]


# FailedAccountTypeDef

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### errorCode
- **Type**: typing.Literal['ACCESS_DENIED', 'ACCOUNT_IS_ISOLATED', 'ALREADY_ENABLED', 'DISABLE_IN_PROGRESS', 'DISASSOCIATE_ALL_MEMBERS', 'ENABLE_IN_PROGRESS', 'EVENTBRIDGE_THROTTLED', 'EVENTBRIDGE_UNAVAILABLE', 'INTERNAL_ERROR', 'RESOURCE_NOT_FOUND', 'RESOURCE_SCAN_NOT_DISABLED', 'SSM_THROTTLED', 'SSM_UNAVAILABLE', 'SUSPEND_IN_PROGRESS']
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### resourceStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.ResourceStatusTypeDef]

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'DISABLING', 'ENABLED', 'ENABLING', 'SUSPENDED', 'SUSPENDING']]


# FailedMemberAccountEc2DeepInspectionStatusStateTypeDef

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### ec2ScanStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'DISABLING', 'ENABLED', 'ENABLING', 'SUSPENDED', 'SUSPENDING']]

### errorMessage
- **Type**: typing.Optional[str]


# FilterCriteriaExtraOutputTypeDef

### awsAccountId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### codeVulnerabilityDetectorName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### codeVulnerabilityDetectorTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### codeVulnerabilityFilePath
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### componentId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### componentType
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### ec2InstanceImageId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### ec2InstanceSubnetId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### ec2InstanceVpcId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### ecrImageArchitecture
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### ecrImageHash
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### ecrImagePushedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.DateFilterExtraOutputTypeDef]]

### ecrImageRegistry
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### ecrImageRepositoryName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### ecrImageTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### epssScore
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.NumberFilterTypeDef]]

### exploitAvailable
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### findingArn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### findingStatus
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### findingType
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### firstObservedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.DateFilterExtraOutputTypeDef]]

### fixAvailable
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### inspectorScore
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.NumberFilterTypeDef]]

### lambdaFunctionExecutionRoleArn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### lambdaFunctionLastModifiedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.DateFilterExtraOutputTypeDef]]

### lambdaFunctionLayers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### lambdaFunctionName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### lambdaFunctionRuntime
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### lastObservedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.DateFilterExtraOutputTypeDef]]

### networkProtocol
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### portRange
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.PortRangeFilterTypeDef]]

### relatedVulnerabilities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### resourceId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### resourceTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.MapFilterTypeDef]]

### resourceType
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### severity
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### title
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### updatedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.DateFilterExtraOutputTypeDef]]

### vendorSeverity
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### vulnerabilityId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### vulnerabilitySource
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### vulnerablePackages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.PackageFilterTypeDef]]


# FilterCriteriaOutputTypeDef

### awsAccountId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### codeVulnerabilityDetectorName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### codeVulnerabilityDetectorTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### codeVulnerabilityFilePath
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### componentId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### componentType
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### ec2InstanceImageId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### ec2InstanceSubnetId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### ec2InstanceVpcId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### ecrImageArchitecture
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### ecrImageHash
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### ecrImagePushedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.DateFilterOutputTypeDef]]

### ecrImageRegistry
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### ecrImageRepositoryName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### ecrImageTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### epssScore
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.NumberFilterTypeDef]]

### exploitAvailable
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### findingArn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### findingStatus
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### findingType
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### firstObservedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.DateFilterOutputTypeDef]]

### fixAvailable
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### inspectorScore
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.NumberFilterTypeDef]]

### lambdaFunctionExecutionRoleArn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### lambdaFunctionLastModifiedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.DateFilterOutputTypeDef]]

### lambdaFunctionLayers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### lambdaFunctionName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### lambdaFunctionRuntime
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### lastObservedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.DateFilterOutputTypeDef]]

### networkProtocol
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### portRange
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.PortRangeFilterTypeDef]]

### relatedVulnerabilities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### resourceId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### resourceTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.MapFilterTypeDef]]

### resourceType
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### severity
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### title
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### updatedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.DateFilterOutputTypeDef]]

### vendorSeverity
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### vulnerabilityId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### vulnerabilitySource
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### vulnerablePackages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.PackageFilterTypeDef]]


# FilterCriteriaTypeDef

### awsAccountId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### codeVulnerabilityDetectorName
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### codeVulnerabilityDetectorTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### codeVulnerabilityFilePath
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### componentId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### componentType
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### ec2InstanceImageId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### ec2InstanceSubnetId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### ec2InstanceVpcId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### ecrImageArchitecture
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### ecrImageHash
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### ecrImagePushedAt
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.DateFilterTypeDef]]

### ecrImageRegistry
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### ecrImageRepositoryName
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### ecrImageTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### epssScore
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.NumberFilterTypeDef]]

### exploitAvailable
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### findingArn
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### findingStatus
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### findingType
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### firstObservedAt
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.DateFilterTypeDef]]

### fixAvailable
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### inspectorScore
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.NumberFilterTypeDef]]

### lambdaFunctionExecutionRoleArn
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### lambdaFunctionLastModifiedAt
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.DateFilterTypeDef]]

### lambdaFunctionLayers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### lambdaFunctionName
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### lambdaFunctionRuntime
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### lastObservedAt
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.DateFilterTypeDef]]

### networkProtocol
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### portRange
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.PortRangeFilterTypeDef]]

### relatedVulnerabilities
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### resourceId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### resourceTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.MapFilterTypeDef]]

### resourceType
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### severity
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### title
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### updatedAt
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.DateFilterTypeDef]]

### vendorSeverity
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### vulnerabilityId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### vulnerabilitySource
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### vulnerablePackages
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.PackageFilterTypeDef]]


# FilterTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.FilterCriteriaOutputTypeDef'>
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


# FindingDetailTypeDef

### cisaData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.CisaDataTypeDef]

### cwes
- **Type**: typing.Optional[typing.List[str]]

### epssScore
- **Type**: typing.Optional[float]

### evidences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.EvidenceTypeDef]]

### exploitObserved
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.ExploitObservedTypeDef]

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


# FindingDetailsErrorTypeDef

### errorCode
- **Type**: typing.Literal['ACCESS_DENIED', 'FINDING_DETAILS_NOT_FOUND', 'INTERNAL_ERROR', 'INVALID_INPUT']
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### findingArn
- **Type**: <class 'str'>
- **Required**: Yes


# FindingTypeAggregationResponseTypeDef

### accountId
- **Type**: typing.Optional[str]

### severityCounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.SeverityCountsTypeDef]


# FindingTypeAggregationTypeDef

### findingType
- **Type**: typing.Optional[typing.Literal['CODE_VULNERABILITY', 'NETWORK_REACHABILITY', 'PACKAGE_VULNERABILITY']]

### resourceType
- **Type**: typing.Optional[typing.Literal['AWS_EC2_INSTANCE', 'AWS_ECR_CONTAINER_IMAGE', 'AWS_LAMBDA_FUNCTION']]

### sortBy
- **Type**: typing.Optional[typing.Literal['ALL', 'CRITICAL', 'HIGH']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# FindingTypeDef

### awsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### findingArn
- **Type**: <class 'str'>
- **Required**: Yes

### firstObservedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastObservedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### remediation
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.RemediationTypeDef'>
- **Required**: Yes

### resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.ResourceTypeDef]
- **Required**: Yes

### severity
- **Type**: typing.Literal['CRITICAL', 'HIGH', 'INFORMATIONAL', 'LOW', 'MEDIUM', 'UNTRIAGED']
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CLOSED', 'SUPPRESSED']
- **Required**: Yes

### type
- **Type**: typing.Literal['CODE_VULNERABILITY', 'NETWORK_REACHABILITY', 'PACKAGE_VULNERABILITY']
- **Required**: Yes

### codeVulnerabilityDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.CodeVulnerabilityDetailsTypeDef]

### epss
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.EpssDetailsTypeDef]

### exploitAvailable
- **Type**: typing.Optional[typing.Literal['NO', 'YES']]

### exploitabilityDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.ExploitabilityDetailsTypeDef]

### fixAvailable
- **Type**: typing.Optional[typing.Literal['NO', 'PARTIAL', 'YES']]

### inspectorScore
- **Type**: typing.Optional[float]

### inspectorScoreDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.InspectorScoreDetailsTypeDef]

### networkReachabilityDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.NetworkReachabilityDetailsTypeDef]

### packageVulnerabilityDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PackageVulnerabilityDetailsTypeDef]

### title
- **Type**: typing.Optional[str]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# FreeTrialAccountInfoTypeDef

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### freeTrialInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.FreeTrialInfoTypeDef]
- **Required**: Yes


# FreeTrialInfoErrorTypeDef

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: typing.Literal['ACCESS_DENIED', 'INTERNAL_ERROR']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# FreeTrialInfoTypeDef

### end
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### start
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'INACTIVE']
- **Required**: Yes

### type
- **Type**: typing.Literal['EC2', 'ECR', 'LAMBDA', 'LAMBDA_CODE']
- **Required**: Yes


# GetCisScanReportRequestRequestTypeDef

### scanArn
- **Type**: <class 'str'>
- **Required**: Yes

### reportFormat
- **Type**: typing.Optional[typing.Literal['CSV', 'PDF']]

### targetAccounts
- **Type**: typing.Optional[typing.Sequence[str]]


# GetCisScanReportResponseTypeDef

### status
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### url
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCisScanResultDetailsRequestGetCisScanResultDetailsPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.CisScanResultDetailsFilterCriteriaTypeDef]

### sortBy
- **Type**: typing.Optional[typing.Literal['CHECK_ID', 'STATUS']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PaginatorConfigTypeDef]


# GetCisScanResultDetailsRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.CisScanResultDetailsFilterCriteriaTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['CHECK_ID', 'STATUS']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# GetCisScanResultDetailsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### scanResultDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.CisScanResultDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConfigurationResponseTypeDef

### ec2Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.Ec2ConfigurationStateTypeDef'>
- **Required**: Yes

### ecrConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.EcrConfigurationStateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDelegatedAdminAccountResponseTypeDef

### delegatedAdmin
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.DelegatedAdminTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEc2DeepInspectionConfigurationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEncryptionKeyRequestRequestTypeDef

### resourceType
- **Type**: typing.Literal['AWS_EC2_INSTANCE', 'AWS_ECR_CONTAINER_IMAGE', 'AWS_ECR_REPOSITORY', 'AWS_LAMBDA_FUNCTION']
- **Required**: Yes

### scanType
- **Type**: typing.Literal['CODE', 'NETWORK', 'PACKAGE']
- **Required**: Yes


# GetEncryptionKeyResponseTypeDef

### kmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFindingsReportStatusRequestRequestTypeDef

### reportId
- **Type**: typing.Optional[str]


# GetFindingsReportStatusResponseTypeDef

### destination
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.DestinationTypeDef'>
- **Required**: Yes

### errorCode
- **Type**: typing.Literal['BUCKET_NOT_FOUND', 'INCOMPATIBLE_BUCKET_REGION', 'INTERNAL_ERROR', 'INVALID_PERMISSIONS', 'MALFORMED_KMS_KEY', 'NO_FINDINGS_FOUND']
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### filterCriteria
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.FilterCriteriaOutputTypeDef'>
- **Required**: Yes

### reportId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMemberRequestRequestTypeDef

### accountId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMemberResponseTypeDef

### member
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.MemberTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSbomExportRequestRequestTypeDef

### reportId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSbomExportResponseTypeDef

### errorCode
- **Type**: typing.Literal['BUCKET_NOT_FOUND', 'INCOMPATIBLE_BUCKET_REGION', 'INTERNAL_ERROR', 'INVALID_PERMISSIONS', 'MALFORMED_KMS_KEY', 'NO_FINDINGS_FOUND']
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### filterCriteria
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResourceFilterCriteriaOutputTypeDef'>
- **Required**: Yes

### format
- **Type**: typing.Literal['CYCLONEDX_1_4', 'SPDX_2_3']
- **Required**: Yes

### reportId
- **Type**: <class 'str'>
- **Required**: Yes

### s3Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.DestinationTypeDef'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImageLayerAggregationResponseTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.SeverityCountsTypeDef]


# ImageLayerAggregationTypeDef

### layerHashes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### repositories
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### resourceIds
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### sortBy
- **Type**: typing.Optional[typing.Literal['ALL', 'CRITICAL', 'HIGH']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# InspectorScoreDetailsTypeDef

### adjustedCvss
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.CvssScoreDetailsTypeDef]


# LambdaFunctionAggregationResponseTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.SeverityCountsTypeDef]


# LambdaFunctionAggregationTypeDef

### functionNames
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### functionTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.MapFilterTypeDef]]

### resourceIds
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### runtimes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### sortBy
- **Type**: typing.Optional[typing.Literal['ALL', 'CRITICAL', 'HIGH']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# LambdaFunctionMetadataTypeDef

### functionName
- **Type**: typing.Optional[str]

### functionTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### layers
- **Type**: typing.Optional[typing.List[str]]

### runtime
- **Type**: typing.Optional[typing.Literal['GO_1_X', 'JAVA_11', 'JAVA_17', 'JAVA_8', 'JAVA_8_AL2', 'NODEJS', 'NODEJS_12_X', 'NODEJS_14_X', 'NODEJS_16_X', 'NODEJS_18_X', 'PYTHON_3_10', 'PYTHON_3_7', 'PYTHON_3_8', 'PYTHON_3_9', 'UNSUPPORTED']]


# LambdaLayerAggregationResponseTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.SeverityCountsTypeDef]


# LambdaLayerAggregationTypeDef

### functionNames
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### layerArns
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### resourceIds
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### sortBy
- **Type**: typing.Optional[typing.Literal['ALL', 'CRITICAL', 'HIGH']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# LambdaVpcConfigTypeDef

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### subnetIds
- **Type**: typing.Optional[typing.List[str]]

### vpcId
- **Type**: typing.Optional[str]


# ListAccountPermissionsRequestListAccountPermissionsPaginateTypeDef

### service
- **Type**: typing.Optional[typing.Literal['EC2', 'ECR', 'LAMBDA']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PaginatorConfigTypeDef]


# ListAccountPermissionsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### service
- **Type**: typing.Optional[typing.Literal['EC2', 'ECR', 'LAMBDA']]


# ListAccountPermissionsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.PermissionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCisScanConfigurationsFilterCriteriaTypeDef

### scanConfigurationArnFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilterTypeDef]]

### scanNameFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilterTypeDef]]

### targetResourceTagFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.TagFilterTypeDef]]


# ListCisScanConfigurationsRequestListCisScanConfigurationsPaginateTypeDef

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.ListCisScanConfigurationsFilterCriteriaTypeDef]

### sortBy
- **Type**: typing.Optional[typing.Literal['SCAN_CONFIGURATION_ARN', 'SCAN_NAME']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PaginatorConfigTypeDef]


# ListCisScanConfigurationsRequestRequestTypeDef

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.ListCisScanConfigurationsFilterCriteriaTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['SCAN_CONFIGURATION_ARN', 'SCAN_NAME']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# ListCisScanConfigurationsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### scanConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.CisScanConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCisScanResultsAggregatedByChecksRequestListCisScanResultsAggregatedByChecksPaginateTypeDef

### scanArn
- **Type**: <class 'str'>
- **Required**: Yes

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.CisScanResultsAggregatedByChecksFilterCriteriaTypeDef]

### sortBy
- **Type**: typing.Optional[typing.Literal['CHECK_ID', 'FAILED_COUNTS', 'PLATFORM', 'SECURITY_LEVEL', 'TITLE']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PaginatorConfigTypeDef]


# ListCisScanResultsAggregatedByChecksRequestRequestTypeDef

### scanArn
- **Type**: <class 'str'>
- **Required**: Yes

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.CisScanResultsAggregatedByChecksFilterCriteriaTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['CHECK_ID', 'FAILED_COUNTS', 'PLATFORM', 'SECURITY_LEVEL', 'TITLE']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# ListCisScanResultsAggregatedByChecksResponseTypeDef

### checkAggregations
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.CisCheckAggregationTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCisScanResultsAggregatedByTargetResourceRequestListCisScanResultsAggregatedByTargetResourcePaginateTypeDef

### scanArn
- **Type**: <class 'str'>
- **Required**: Yes

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.CisScanResultsAggregatedByTargetResourceFilterCriteriaTypeDef]

### sortBy
- **Type**: typing.Optional[typing.Literal['ACCOUNT_ID', 'FAILED_COUNTS', 'PLATFORM', 'RESOURCE_ID', 'TARGET_STATUS', 'TARGET_STATUS_REASON']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PaginatorConfigTypeDef]


# ListCisScanResultsAggregatedByTargetResourceRequestRequestTypeDef

### scanArn
- **Type**: <class 'str'>
- **Required**: Yes

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.CisScanResultsAggregatedByTargetResourceFilterCriteriaTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['ACCOUNT_ID', 'FAILED_COUNTS', 'PLATFORM', 'RESOURCE_ID', 'TARGET_STATUS', 'TARGET_STATUS_REASON']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# ListCisScanResultsAggregatedByTargetResourceResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### targetResourceAggregations
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.CisTargetResourceAggregationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCisScansFilterCriteriaTypeDef

### failedChecksFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisNumberFilterTypeDef]]

### scanArnFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilterTypeDef]]

### scanAtFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisDateFilterTypeDef]]

### scanConfigurationArnFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilterTypeDef]]

### scanNameFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilterTypeDef]]

### scanStatusFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisScanStatusFilterTypeDef]]

### scheduledByFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilterTypeDef]]

### targetAccountIdFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilterTypeDef]]

### targetResourceIdFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisStringFilterTypeDef]]

### targetResourceTagFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.TagFilterTypeDef]]


# ListCisScansRequestListCisScansPaginateTypeDef

### detailLevel
- **Type**: typing.Optional[typing.Literal['MEMBER', 'ORGANIZATION']]

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.ListCisScansFilterCriteriaTypeDef]

### sortBy
- **Type**: typing.Optional[typing.Literal['FAILED_CHECKS', 'SCAN_START_DATE', 'SCHEDULED_BY', 'STATUS']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PaginatorConfigTypeDef]


# ListCisScansRequestRequestTypeDef

### detailLevel
- **Type**: typing.Optional[typing.Literal['MEMBER', 'ORGANIZATION']]

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.ListCisScansFilterCriteriaTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['FAILED_CHECKS', 'SCAN_START_DATE', 'SCHEDULED_BY', 'STATUS']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# ListCisScansResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### scans
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.CisScanTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCoverageRequestListCoveragePaginateTypeDef

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.CoverageFilterCriteriaTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PaginatorConfigTypeDef]


# ListCoverageRequestRequestTypeDef

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.CoverageFilterCriteriaTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListCoverageResponseTypeDef

### coveredResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.CoveredResourceTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCoverageStatisticsRequestListCoverageStatisticsPaginateTypeDef

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.CoverageFilterCriteriaTypeDef]

### groupBy
- **Type**: typing.Optional[typing.Literal['ACCOUNT_ID', 'ECR_REPOSITORY_NAME', 'RESOURCE_TYPE', 'SCAN_STATUS_CODE', 'SCAN_STATUS_REASON']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PaginatorConfigTypeDef]


# ListCoverageStatisticsRequestRequestTypeDef

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.CoverageFilterCriteriaTypeDef]

### groupBy
- **Type**: typing.Optional[typing.Literal['ACCOUNT_ID', 'ECR_REPOSITORY_NAME', 'RESOURCE_TYPE', 'SCAN_STATUS_CODE', 'SCAN_STATUS_REASON']]

### nextToken
- **Type**: typing.Optional[str]


# ListCoverageStatisticsResponseTypeDef

### countsByGroup
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.CountsTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### totalCounts
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDelegatedAdminAccountsRequestListDelegatedAdminAccountsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PaginatorConfigTypeDef]


# ListDelegatedAdminAccountsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDelegatedAdminAccountsResponseTypeDef

### delegatedAdminAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.DelegatedAdminAccountTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFiltersRequestListFiltersPaginateTypeDef

### action
- **Type**: typing.Optional[typing.Literal['NONE', 'SUPPRESS']]

### arns
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PaginatorConfigTypeDef]


# ListFiltersRequestRequestTypeDef

### action
- **Type**: typing.Optional[typing.Literal['NONE', 'SUPPRESS']]

### arns
- **Type**: typing.Optional[typing.Sequence[str]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListFiltersResponseTypeDef

### filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.FilterTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFindingAggregationsRequestListFindingAggregationsPaginateTypeDef

### aggregationType
- **Type**: typing.Literal['ACCOUNT', 'AMI', 'AWS_EC2_INSTANCE', 'AWS_ECR_CONTAINER', 'AWS_LAMBDA_FUNCTION', 'FINDING_TYPE', 'IMAGE_LAYER', 'LAMBDA_LAYER', 'PACKAGE', 'REPOSITORY', 'TITLE']
- **Required**: Yes

### accountIds
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### aggregationRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.AggregationRequestTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PaginatorConfigTypeDef]


# ListFindingAggregationsRequestRequestTypeDef

### aggregationType
- **Type**: typing.Literal['ACCOUNT', 'AMI', 'AWS_EC2_INSTANCE', 'AWS_ECR_CONTAINER', 'AWS_LAMBDA_FUNCTION', 'FINDING_TYPE', 'IMAGE_LAYER', 'LAMBDA_LAYER', 'PACKAGE', 'REPOSITORY', 'TITLE']
- **Required**: Yes

### accountIds
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### aggregationRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.AggregationRequestTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListFindingAggregationsResponseTypeDef

### aggregationType
- **Type**: typing.Literal['ACCOUNT', 'AMI', 'AWS_EC2_INSTANCE', 'AWS_ECR_CONTAINER', 'AWS_LAMBDA_FUNCTION', 'FINDING_TYPE', 'IMAGE_LAYER', 'LAMBDA_LAYER', 'PACKAGE', 'REPOSITORY', 'TITLE']
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### responses
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.AggregationResponseTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFindingsRequestListFindingsPaginateTypeDef

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.FilterCriteriaTypeDef]

### sortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.SortCriteriaTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PaginatorConfigTypeDef]


# ListFindingsRequestRequestTypeDef

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.FilterCriteriaTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.SortCriteriaTypeDef]


# ListFindingsResponseTypeDef

### findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.FindingTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMembersRequestListMembersPaginateTypeDef

### onlyAssociated
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PaginatorConfigTypeDef]


# ListMembersRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### onlyAssociated
- **Type**: typing.Optional[bool]


# ListMembersResponseTypeDef

### members
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.MemberTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListUsageTotalsRequestListUsageTotalsPaginateTypeDef

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PaginatorConfigTypeDef]


# ListUsageTotalsRequestRequestTypeDef

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListUsageTotalsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### totals
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.UsageTotalTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MapFilterTypeDef

### comparison
- **Type**: typing.Literal['EQUALS']
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[str]


# MemberAccountEc2DeepInspectionStatusStateTypeDef

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVATED', 'DEACTIVATED', 'FAILED', 'PENDING']]


# MemberAccountEc2DeepInspectionStatusTypeDef

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### activateDeepInspection
- **Type**: <class 'bool'>
- **Required**: Yes


# MemberTypeDef

### accountId
- **Type**: typing.Optional[str]

### delegatedAdminAccountId
- **Type**: typing.Optional[str]

### relationshipStatus
- **Type**: typing.Optional[typing.Literal['ACCOUNT_SUSPENDED', 'CANNOT_CREATE_DETECTOR_IN_ORG_MASTER', 'CREATED', 'DELETED', 'DISABLED', 'EMAIL_VERIFICATION_FAILED', 'EMAIL_VERIFICATION_IN_PROGRESS', 'ENABLED', 'INVITED', 'REGION_DISABLED', 'REMOVED', 'RESIGNED']]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# MonthlyScheduleTypeDef

### day
- **Type**: typing.Literal['FRI', 'MON', 'SAT', 'SUN', 'THU', 'TUE', 'WED']
- **Required**: Yes

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.TimeTypeDef'>
- **Required**: Yes


# NetworkPathTypeDef

### steps
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.StepTypeDef]]


# NetworkReachabilityDetailsTypeDef

### networkPath
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.NetworkPathTypeDef'>
- **Required**: Yes

### openPortRange
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.PortRangeTypeDef'>
- **Required**: Yes

### protocol
- **Type**: typing.Literal['TCP', 'UDP']
- **Required**: Yes


# NumberFilterTypeDef

### lowerInclusive
- **Type**: typing.Optional[float]

### upperInclusive
- **Type**: typing.Optional[float]


# PackageAggregationResponseTypeDef

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### severityCounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.SeverityCountsTypeDef]


# PackageAggregationTypeDef

### packageNames
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### sortBy
- **Type**: typing.Optional[typing.Literal['ALL', 'CRITICAL', 'HIGH']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# PackageFilterTypeDef

### architecture
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]

### epoch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.NumberFilterTypeDef]

### name
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]

### release
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]

### sourceLambdaLayerArn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]

### sourceLayerHash
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]

### version
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]


# PackageVulnerabilityDetailsTypeDef

### source
- **Type**: <class 'str'>
- **Required**: Yes

### vulnerabilityId
- **Type**: <class 'str'>
- **Required**: Yes

### cvss
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.CvssScoreTypeDef]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.VulnerablePackageTypeDef]]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PermissionTypeDef

### operation
- **Type**: typing.Literal['DISABLE_REPOSITORY', 'DISABLE_SCANNING', 'ENABLE_REPOSITORY', 'ENABLE_SCANNING']
- **Required**: Yes

### service
- **Type**: typing.Literal['EC2', 'ECR', 'LAMBDA']
- **Required**: Yes


# PortRangeFilterTypeDef

### beginInclusive
- **Type**: typing.Optional[int]

### endInclusive
- **Type**: typing.Optional[int]


# PortRangeTypeDef

### begin
- **Type**: <class 'int'>
- **Required**: Yes

### end
- **Type**: <class 'int'>
- **Required**: Yes


# RecommendationTypeDef

### Url
- **Type**: typing.Optional[str]

### text
- **Type**: typing.Optional[str]


# RemediationTypeDef

### recommendation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.RecommendationTypeDef]


# RepositoryAggregationResponseTypeDef

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### affectedImages
- **Type**: typing.Optional[int]

### severityCounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.SeverityCountsTypeDef]


# RepositoryAggregationTypeDef

### repositories
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### sortBy
- **Type**: typing.Optional[typing.Literal['AFFECTED_IMAGES', 'ALL', 'CRITICAL', 'HIGH']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# ResetEncryptionKeyRequestRequestTypeDef

### resourceType
- **Type**: typing.Literal['AWS_EC2_INSTANCE', 'AWS_ECR_CONTAINER_IMAGE', 'AWS_ECR_REPOSITORY', 'AWS_LAMBDA_FUNCTION']
- **Required**: Yes

### scanType
- **Type**: typing.Literal['CODE', 'NETWORK', 'PACKAGE']
- **Required**: Yes


# ResourceDetailsTypeDef

### awsEc2Instance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.AwsEc2InstanceDetailsTypeDef]

### awsEcrContainerImage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.AwsEcrContainerImageDetailsTypeDef]

### awsLambdaFunction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.AwsLambdaFunctionDetailsTypeDef]


# ResourceFilterCriteriaOutputTypeDef

### accountId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.ResourceStringFilterTypeDef]]

### ec2InstanceTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.ResourceMapFilterTypeDef]]

### ecrImageTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.ResourceStringFilterTypeDef]]

### ecrRepositoryName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.ResourceStringFilterTypeDef]]

### lambdaFunctionName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.ResourceStringFilterTypeDef]]

### lambdaFunctionTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.ResourceMapFilterTypeDef]]

### resourceId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.ResourceStringFilterTypeDef]]

### resourceType
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.ResourceStringFilterTypeDef]]


# ResourceFilterCriteriaTypeDef

### accountId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.ResourceStringFilterTypeDef]]

### ec2InstanceTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.ResourceMapFilterTypeDef]]

### ecrImageTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.ResourceStringFilterTypeDef]]

### ecrRepositoryName
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.ResourceStringFilterTypeDef]]

### lambdaFunctionName
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.ResourceStringFilterTypeDef]]

### lambdaFunctionTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.ResourceMapFilterTypeDef]]

### resourceId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.ResourceStringFilterTypeDef]]

### resourceType
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.ResourceStringFilterTypeDef]]


# ResourceMapFilterTypeDef

### comparison
- **Type**: typing.Literal['EQUALS']
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[str]


# ResourceScanMetadataTypeDef

### ec2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.Ec2MetadataTypeDef]

### ecrImage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.EcrContainerImageMetadataTypeDef]

### ecrRepository
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.EcrRepositoryMetadataTypeDef]

### lambdaFunction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.LambdaFunctionMetadataTypeDef]


# ResourceStateTypeDef

### ec2
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.StateTypeDef'>
- **Required**: Yes

### ecr
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.StateTypeDef'>
- **Required**: Yes

### lambdaCode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.StateTypeDef]


# ResourceStatusTypeDef

### ec2
- **Type**: typing.Literal['DISABLED', 'DISABLING', 'ENABLED', 'ENABLING', 'SUSPENDED', 'SUSPENDING']
- **Required**: Yes

### ecr
- **Type**: typing.Literal['DISABLED', 'DISABLING', 'ENABLED', 'ENABLING', 'SUSPENDED', 'SUSPENDING']
- **Required**: Yes

### lambdaCode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'DISABLING', 'ENABLED', 'ENABLING', 'SUSPENDED', 'SUSPENDING']]


# ResourceStringFilterTypeDef

### comparison
- **Type**: typing.Literal['EQUALS', 'NOT_EQUALS']
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# ResourceTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['AWS_EC2_INSTANCE', 'AWS_ECR_CONTAINER_IMAGE', 'AWS_ECR_REPOSITORY', 'AWS_LAMBDA_FUNCTION']
- **Required**: Yes

### details
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.ResourceDetailsTypeDef]

### partition
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


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


# ScanStatusTypeDef

### reason
- **Type**: typing.Literal['ACCESS_DENIED', 'DEEP_INSPECTION_COLLECTION_TIME_LIMIT_EXCEEDED', 'DEEP_INSPECTION_DAILY_SSM_INVENTORY_LIMIT_EXCEEDED', 'DEEP_INSPECTION_NO_INVENTORY', 'DEEP_INSPECTION_PACKAGE_COLLECTION_LIMIT_EXCEEDED', 'EC2_INSTANCE_STOPPED', 'EXCLUDED_BY_TAG', 'IMAGE_SIZE_EXCEEDED', 'INTERNAL_ERROR', 'NO_INVENTORY', 'NO_RESOURCES_FOUND', 'PENDING_DISABLE', 'PENDING_INITIAL_SCAN', 'RESOURCE_TERMINATED', 'SCAN_ELIGIBILITY_EXPIRED', 'SCAN_FREQUENCY_MANUAL', 'SCAN_FREQUENCY_SCAN_ON_PUSH', 'STALE_INVENTORY', 'SUCCESSFUL', 'UNMANAGED_EC2_INSTANCE', 'UNSUPPORTED_CONFIG_FILE', 'UNSUPPORTED_MEDIA_TYPE', 'UNSUPPORTED_OS', 'UNSUPPORTED_RUNTIME']
- **Required**: Yes

### statusCode
- **Type**: typing.Literal['ACTIVE', 'INACTIVE']
- **Required**: Yes


# ScheduleExtraOutputTypeDef

### daily
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.DailyScheduleTypeDef]

### monthly
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.MonthlyScheduleTypeDef]

### oneTime
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### weekly
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.WeeklyScheduleExtraOutputTypeDef]


# ScheduleOutputTypeDef

### daily
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.DailyScheduleTypeDef]

### monthly
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.MonthlyScheduleTypeDef]

### oneTime
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### weekly
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.WeeklyScheduleOutputTypeDef]


# ScheduleTypeDef

### daily
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.DailyScheduleTypeDef]

### monthly
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.MonthlyScheduleTypeDef]

### oneTime
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### weekly
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.WeeklyScheduleTypeDef]


# SearchVulnerabilitiesFilterCriteriaTypeDef

### vulnerabilityIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# SearchVulnerabilitiesRequestRequestTypeDef

### filterCriteria
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.SearchVulnerabilitiesFilterCriteriaTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchVulnerabilitiesRequestSearchVulnerabilitiesPaginateTypeDef

### filterCriteria
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.SearchVulnerabilitiesFilterCriteriaTypeDef'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.PaginatorConfigTypeDef]


# SearchVulnerabilitiesResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### vulnerabilities
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector2_classes.VulnerabilityTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SendCisSessionHealthRequestRequestTypeDef

### scanJobId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionToken
- **Type**: <class 'str'>
- **Required**: Yes


# SendCisSessionTelemetryRequestRequestTypeDef

### messages
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.CisSessionMessageTypeDef]
- **Required**: Yes

### scanJobId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionToken
- **Type**: <class 'str'>
- **Required**: Yes


# SeverityCountsTypeDef

### all
- **Type**: typing.Optional[int]

### critical
- **Type**: typing.Optional[int]

### high
- **Type**: typing.Optional[int]

### medium
- **Type**: typing.Optional[int]


# SortCriteriaTypeDef

### field
- **Type**: typing.Literal['AWS_ACCOUNT_ID', 'COMPONENT_TYPE', 'ECR_IMAGE_PUSHED_AT', 'ECR_IMAGE_REGISTRY', 'ECR_IMAGE_REPOSITORY_NAME', 'EPSS_SCORE', 'FINDING_STATUS', 'FINDING_TYPE', 'FIRST_OBSERVED_AT', 'INSPECTOR_SCORE', 'LAST_OBSERVED_AT', 'NETWORK_PROTOCOL', 'RESOURCE_TYPE', 'SEVERITY', 'VENDOR_SEVERITY', 'VULNERABILITY_ID', 'VULNERABILITY_SOURCE']
- **Required**: Yes

### sortOrder
- **Type**: typing.Literal['ASC', 'DESC']
- **Required**: Yes


# StartCisSessionMessageTypeDef

### sessionToken
- **Type**: <class 'str'>
- **Required**: Yes


# StartCisSessionRequestRequestTypeDef

### message
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.StartCisSessionMessageTypeDef'>
- **Required**: Yes

### scanJobId
- **Type**: <class 'str'>
- **Required**: Yes


# StateTypeDef

### errorCode
- **Type**: typing.Literal['ACCESS_DENIED', 'ACCOUNT_IS_ISOLATED', 'ALREADY_ENABLED', 'DISABLE_IN_PROGRESS', 'DISASSOCIATE_ALL_MEMBERS', 'ENABLE_IN_PROGRESS', 'EVENTBRIDGE_THROTTLED', 'EVENTBRIDGE_UNAVAILABLE', 'INTERNAL_ERROR', 'RESOURCE_NOT_FOUND', 'RESOURCE_SCAN_NOT_DISABLED', 'SSM_THROTTLED', 'SSM_UNAVAILABLE', 'SUSPEND_IN_PROGRESS']
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DISABLED', 'DISABLING', 'ENABLED', 'ENABLING', 'SUSPENDED', 'SUSPENDING']
- **Required**: Yes


# StatusCountsTypeDef

### failed
- **Type**: typing.Optional[int]

### passed
- **Type**: typing.Optional[int]

### skipped
- **Type**: typing.Optional[int]


# StepTypeDef

### componentId
- **Type**: <class 'str'>
- **Required**: Yes

### componentType
- **Type**: <class 'str'>
- **Required**: Yes


# StopCisMessageProgressTypeDef

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


# StopCisSessionMessageTypeDef

### progress
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.StopCisMessageProgressTypeDef'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'INTERRUPTED', 'SUCCESS', 'UNSUPPORTED_OS']
- **Required**: Yes

### benchmarkProfile
- **Type**: typing.Optional[str]

### benchmarkVersion
- **Type**: typing.Optional[str]

### computePlatform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.ComputePlatformTypeDef]

### reason
- **Type**: typing.Optional[str]


# StopCisSessionRequestRequestTypeDef

### message
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.StopCisSessionMessageTypeDef'>
- **Required**: Yes

### scanJobId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionToken
- **Type**: <class 'str'>
- **Required**: Yes


# StringFilterTypeDef

### comparison
- **Type**: typing.Literal['EQUALS', 'NOT_EQUALS', 'PREFIX']
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# SuggestedFixTypeDef

### code
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# TagFilterTypeDef

### comparison
- **Type**: typing.Literal['EQUALS']
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TimeTypeDef

### timeOfDay
- **Type**: <class 'str'>
- **Required**: Yes

### timezone
- **Type**: <class 'str'>
- **Required**: Yes


# TitleAggregationResponseTypeDef

### title
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### severityCounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.SeverityCountsTypeDef]

### vulnerabilityId
- **Type**: typing.Optional[str]


# TitleAggregationTypeDef

### findingType
- **Type**: typing.Optional[typing.Literal['CODE_VULNERABILITY', 'NETWORK_REACHABILITY', 'PACKAGE_VULNERABILITY']]

### resourceType
- **Type**: typing.Optional[typing.Literal['AWS_EC2_INSTANCE', 'AWS_ECR_CONTAINER_IMAGE', 'AWS_LAMBDA_FUNCTION']]

### sortBy
- **Type**: typing.Optional[typing.Literal['ALL', 'CRITICAL', 'HIGH']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]

### titles
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]

### vulnerabilityIds
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector2_classes.StringFilterTypeDef]]


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateCisScanConfigurationRequestRequestTypeDef

### scanConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### scanName
- **Type**: typing.Optional[str]

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.ScheduleTypeDef]

### securityLevel
- **Type**: typing.Optional[typing.Literal['LEVEL_1', 'LEVEL_2']]

### targets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.UpdateCisTargetsTypeDef]


# UpdateCisScanConfigurationResponseTypeDef

### scanConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateCisTargetsTypeDef

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### targetResourceTags
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]


# UpdateConfigurationRequestRequestTypeDef

### ec2Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.Ec2ConfigurationTypeDef]

### ecrConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.EcrConfigurationTypeDef]


# UpdateEc2DeepInspectionConfigurationRequestRequestTypeDef

### activateDeepInspection
- **Type**: typing.Optional[bool]

### packagePaths
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateEc2DeepInspectionConfigurationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEncryptionKeyRequestRequestTypeDef

### kmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: typing.Literal['AWS_EC2_INSTANCE', 'AWS_ECR_CONTAINER_IMAGE', 'AWS_ECR_REPOSITORY', 'AWS_LAMBDA_FUNCTION']
- **Required**: Yes

### scanType
- **Type**: typing.Literal['CODE', 'NETWORK', 'PACKAGE']
- **Required**: Yes


# UpdateFilterRequestRequestTypeDef

### filterArn
- **Type**: <class 'str'>
- **Required**: Yes

### action
- **Type**: typing.Optional[typing.Literal['NONE', 'SUPPRESS']]

### description
- **Type**: typing.Optional[str]

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.FilterCriteriaTypeDef]

### name
- **Type**: typing.Optional[str]

### reason
- **Type**: typing.Optional[str]


# UpdateFilterResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateOrgEc2DeepInspectionConfigurationRequestRequestTypeDef

### orgPackagePaths
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateOrganizationConfigurationRequestRequestTypeDef

### autoEnable
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.AutoEnableTypeDef'>
- **Required**: Yes


# UpdateOrganizationConfigurationResponseTypeDef

### autoEnable
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.AutoEnableTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UsageTotalTypeDef

### accountId
- **Type**: typing.Optional[str]

### usage
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector2_classes.UsageTypeDef]]


# UsageTypeDef

### currency
- **Type**: typing.Optional[typing.Literal['USD']]

### estimatedMonthlyCost
- **Type**: typing.Optional[float]

### total
- **Type**: typing.Optional[float]

### type
- **Type**: typing.Optional[typing.Literal['EC2_INSTANCE_HOURS', 'ECR_INITIAL_SCAN', 'ECR_RESCAN', 'LAMBDA_FUNCTION_CODE_HOURS', 'LAMBDA_FUNCTION_HOURS']]


# VulnerabilityTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### atigData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.AtigDataTypeDef]

### cisaData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.CisaDataTypeDef]

### cvss2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.Cvss2TypeDef]

### cvss3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.Cvss3TypeDef]

### cwes
- **Type**: typing.Optional[typing.List[str]]

### description
- **Type**: typing.Optional[str]

### detectionPlatforms
- **Type**: typing.Optional[typing.List[str]]

### epss
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.EpssTypeDef]

### exploitObserved
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector2_classes.ExploitObservedTypeDef]

### referenceUrls
- **Type**: typing.Optional[typing.List[str]]

### relatedVulnerabilities
- **Type**: typing.Optional[typing.List[str]]

### source
- **Type**: typing.Optional[typing.Literal['NVD']]

### sourceUrl
- **Type**: typing.Optional[str]

### vendorCreatedAt
- **Type**: typing.Optional[datetime.datetime]

### vendorSeverity
- **Type**: typing.Optional[str]

### vendorUpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# VulnerablePackageTypeDef

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
- **Type**: typing.Optional[typing.Literal['BUNDLER', 'CARGO', 'COMPOSER', 'GEMSPEC', 'GOBINARY', 'GOMOD', 'JAR', 'NODEPKG', 'NPM', 'NUGET', 'OS', 'PIP', 'PIPENV', 'POETRY', 'POM', 'PYTHONPKG', 'YARN']]

### release
- **Type**: typing.Optional[str]

### remediation
- **Type**: typing.Optional[str]

### sourceLambdaLayerArn
- **Type**: typing.Optional[str]

### sourceLayerHash
- **Type**: typing.Optional[str]


# WeeklyScheduleExtraOutputTypeDef

### days
- **Type**: typing.List[typing.Literal['FRI', 'MON', 'SAT', 'SUN', 'THU', 'TUE', 'WED']]
- **Required**: Yes

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.TimeTypeDef'>
- **Required**: Yes


# WeeklyScheduleOutputTypeDef

### days
- **Type**: typing.List[typing.Literal['FRI', 'MON', 'SAT', 'SUN', 'THU', 'TUE', 'WED']]
- **Required**: Yes

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.TimeTypeDef'>
- **Required**: Yes


# WeeklyScheduleTypeDef

### days
- **Type**: typing.Sequence[typing.Literal['FRI', 'MON', 'SAT', 'SUN', 'THU', 'TUE', 'WED']]
- **Required**: Yes

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector2_classes.TimeTypeDef'>
- **Required**: Yes


