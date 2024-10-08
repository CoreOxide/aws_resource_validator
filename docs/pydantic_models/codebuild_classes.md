# Pydantic Models in codebuild_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDeleteBuildsInputRequestTypeDef

### ids
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchDeleteBuildsOutputTypeDef

### buildsDeleted
- **Type**: typing.List[str]
- **Required**: Yes

### buildsNotDeleted
- **Type**: typing.List[aws_resource_validator.pydantic_models.codebuild_classes.BuildNotDeletedTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetBuildBatchesInputRequestTypeDef

### ids
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetBuildBatchesOutputTypeDef

### buildBatches
- **Type**: typing.List[aws_resource_validator.pydantic_models.codebuild_classes.BuildBatchTypeDef]
- **Required**: Yes

### buildBatchesNotFound
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetBuildsInputRequestTypeDef

### ids
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetBuildsOutputTypeDef

### builds
- **Type**: typing.List[aws_resource_validator.pydantic_models.codebuild_classes.BuildTypeDef]
- **Required**: Yes

### buildsNotFound
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetFleetsInputRequestTypeDef

### names
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetFleetsOutputTypeDef

### fleets
- **Type**: typing.List[aws_resource_validator.pydantic_models.codebuild_classes.FleetTypeDef]
- **Required**: Yes

### fleetsNotFound
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetProjectsInputRequestTypeDef

### names
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetProjectsOutputTypeDef

### projects
- **Type**: typing.List[aws_resource_validator.pydantic_models.codebuild_classes.ProjectTypeDef]
- **Required**: Yes

### projectsNotFound
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetReportGroupsInputRequestTypeDef

### reportGroupArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetReportGroupsOutputTypeDef

### reportGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.codebuild_classes.ReportGroupTypeDef]
- **Required**: Yes

### reportGroupsNotFound
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetReportsInputRequestTypeDef

### reportArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetReportsOutputTypeDef

### reports
- **Type**: typing.List[aws_resource_validator.pydantic_models.codebuild_classes.ReportTypeDef]
- **Required**: Yes

### reportsNotFound
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchRestrictionsOutputTypeDef

### maximumBuildsAllowed
- **Type**: typing.Optional[int]

### computeTypesAllowed
- **Type**: typing.Optional[typing.List[str]]


# BatchRestrictionsTypeDef

### maximumBuildsAllowed
- **Type**: typing.Optional[int]

### computeTypesAllowed
- **Type**: typing.Optional[typing.Sequence[str]]


# BuildArtifactsTypeDef

### location
- **Type**: typing.Optional[str]

### sha256sum
- **Type**: typing.Optional[str]

### md5sum
- **Type**: typing.Optional[str]

### overrideArtifactName
- **Type**: typing.Optional[bool]

### encryptionDisabled
- **Type**: typing.Optional[bool]

### artifactIdentifier
- **Type**: typing.Optional[str]

### bucketOwnerAccess
- **Type**: typing.Optional[typing.Literal['FULL', 'NONE', 'READ_ONLY']]


# BuildBatchFilterTypeDef

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'FAULT', 'IN_PROGRESS', 'STOPPED', 'SUCCEEDED', 'TIMED_OUT']]


# BuildBatchPhaseTypeDef

### phaseType
- **Type**: typing.Optional[typing.Literal['COMBINE_ARTIFACTS', 'DOWNLOAD_BATCHSPEC', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'SUBMITTED', 'SUCCEEDED']]

### phaseStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'FAULT', 'IN_PROGRESS', 'STOPPED', 'SUCCEEDED', 'TIMED_OUT']]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### durationInSeconds
- **Type**: typing.Optional[int]

### contexts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild_classes.PhaseContextTypeDef]]


# BuildBatchTypeDef

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### currentPhase
- **Type**: typing.Optional[str]

### buildBatchStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'FAULT', 'IN_PROGRESS', 'STOPPED', 'SUCCEEDED', 'TIMED_OUT']]

### sourceVersion
- **Type**: typing.Optional[str]

### resolvedSourceVersion
- **Type**: typing.Optional[str]

### projectName
- **Type**: typing.Optional[str]

### phases
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild_classes.BuildBatchPhaseTypeDef]]

### source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectSourceTypeDef]

### secondarySources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild_classes.ProjectSourceTypeDef]]

### secondarySourceVersions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild_classes.ProjectSourceVersionTypeDef]]

### artifacts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.BuildArtifactsTypeDef]

### secondaryArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild_classes.BuildArtifactsTypeDef]]

### cache
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectCacheOutputTypeDef]

### environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectEnvironmentOutputTypeDef]

### serviceRole
- **Type**: typing.Optional[str]

### logConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.LogsConfigTypeDef]

### buildTimeoutInMinutes
- **Type**: typing.Optional[int]

### queuedTimeoutInMinutes
- **Type**: typing.Optional[int]

### complete
- **Type**: typing.Optional[bool]

### initiator
- **Type**: typing.Optional[str]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.VpcConfigOutputTypeDef]

### encryptionKey
- **Type**: typing.Optional[str]

### buildBatchNumber
- **Type**: typing.Optional[int]

### fileSystemLocations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild_classes.ProjectFileSystemLocationTypeDef]]

### buildBatchConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectBuildBatchConfigOutputTypeDef]

### buildGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild_classes.BuildGroupTypeDef]]

### debugSessionEnabled
- **Type**: typing.Optional[bool]


# BuildGroupTypeDef

### identifier
- **Type**: typing.Optional[str]

### dependsOn
- **Type**: typing.Optional[typing.List[str]]

### ignoreFailure
- **Type**: typing.Optional[bool]

### currentBuildSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.BuildSummaryTypeDef]

### priorBuildSummaryList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild_classes.BuildSummaryTypeDef]]


# BuildNotDeletedTypeDef

### id
- **Type**: typing.Optional[str]

### statusCode
- **Type**: typing.Optional[str]


# BuildPhaseTypeDef

### phaseType
- **Type**: typing.Optional[typing.Literal['BUILD', 'COMPLETED', 'DOWNLOAD_SOURCE', 'FINALIZING', 'INSTALL', 'POST_BUILD', 'PRE_BUILD', 'PROVISIONING', 'QUEUED', 'SUBMITTED', 'UPLOAD_ARTIFACTS']]

### phaseStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'FAULT', 'IN_PROGRESS', 'STOPPED', 'SUCCEEDED', 'TIMED_OUT']]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### durationInSeconds
- **Type**: typing.Optional[int]

### contexts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild_classes.PhaseContextTypeDef]]


# BuildStatusConfigTypeDef

### context
- **Type**: typing.Optional[str]

### targetUrl
- **Type**: typing.Optional[str]


# BuildSummaryTypeDef

### arn
- **Type**: typing.Optional[str]

### requestedOn
- **Type**: typing.Optional[datetime.datetime]

### buildStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'FAULT', 'IN_PROGRESS', 'STOPPED', 'SUCCEEDED', 'TIMED_OUT']]

### primaryArtifact
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ResolvedArtifactTypeDef]

### secondaryArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild_classes.ResolvedArtifactTypeDef]]


# BuildTypeDef

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### buildNumber
- **Type**: typing.Optional[int]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### currentPhase
- **Type**: typing.Optional[str]

### buildStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'FAULT', 'IN_PROGRESS', 'STOPPED', 'SUCCEEDED', 'TIMED_OUT']]

### sourceVersion
- **Type**: typing.Optional[str]

### resolvedSourceVersion
- **Type**: typing.Optional[str]

### projectName
- **Type**: typing.Optional[str]

### phases
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild_classes.BuildPhaseTypeDef]]

### source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectSourceTypeDef]

### secondarySources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild_classes.ProjectSourceTypeDef]]

### secondarySourceVersions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild_classes.ProjectSourceVersionTypeDef]]

### artifacts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.BuildArtifactsTypeDef]

### secondaryArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild_classes.BuildArtifactsTypeDef]]

### cache
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectCacheOutputTypeDef]

### environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectEnvironmentOutputTypeDef]

### serviceRole
- **Type**: typing.Optional[str]

### logs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.LogsLocationTypeDef]

### timeoutInMinutes
- **Type**: typing.Optional[int]

### queuedTimeoutInMinutes
- **Type**: typing.Optional[int]

### buildComplete
- **Type**: typing.Optional[bool]

### initiator
- **Type**: typing.Optional[str]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.VpcConfigOutputTypeDef]

### networkInterface
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.NetworkInterfaceTypeDef]

### encryptionKey
- **Type**: typing.Optional[str]

### exportedEnvironmentVariables
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild_classes.ExportedEnvironmentVariableTypeDef]]

### reportArns
- **Type**: typing.Optional[typing.List[str]]

### fileSystemLocations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild_classes.ProjectFileSystemLocationTypeDef]]

### debugSession
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.DebugSessionTypeDef]

### buildBatchArn
- **Type**: typing.Optional[str]


# CloudWatchLogsConfigTypeDef

### status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### groupName
- **Type**: typing.Optional[str]

### streamName
- **Type**: typing.Optional[str]


# CodeCoverageReportSummaryTypeDef

### lineCoveragePercentage
- **Type**: typing.Optional[float]

### linesCovered
- **Type**: typing.Optional[int]

### linesMissed
- **Type**: typing.Optional[int]

### branchCoveragePercentage
- **Type**: typing.Optional[float]

### branchesCovered
- **Type**: typing.Optional[int]

### branchesMissed
- **Type**: typing.Optional[int]


# CodeCoverageTypeDef

### id
- **Type**: typing.Optional[str]

### reportARN
- **Type**: typing.Optional[str]

### filePath
- **Type**: typing.Optional[str]

### lineCoveragePercentage
- **Type**: typing.Optional[float]

### linesCovered
- **Type**: typing.Optional[int]

### linesMissed
- **Type**: typing.Optional[int]

### branchCoveragePercentage
- **Type**: typing.Optional[float]

### branchesCovered
- **Type**: typing.Optional[int]

### branchesMissed
- **Type**: typing.Optional[int]

### expired
- **Type**: typing.Optional[datetime.datetime]


# CreateFleetInputRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### baseCapacity
- **Type**: <class 'int'>
- **Required**: Yes

### environmentType
- **Type**: typing.Literal['ARM_CONTAINER', 'ARM_LAMBDA_CONTAINER', 'LINUX_CONTAINER', 'LINUX_GPU_CONTAINER', 'LINUX_LAMBDA_CONTAINER', 'WINDOWS_CONTAINER', 'WINDOWS_SERVER_2019_CONTAINER']
- **Required**: Yes

### computeType
- **Type**: typing.Literal['BUILD_GENERAL1_2XLARGE', 'BUILD_GENERAL1_LARGE', 'BUILD_GENERAL1_MEDIUM', 'BUILD_GENERAL1_SMALL', 'BUILD_GENERAL1_XLARGE', 'BUILD_LAMBDA_10GB', 'BUILD_LAMBDA_1GB', 'BUILD_LAMBDA_2GB', 'BUILD_LAMBDA_4GB', 'BUILD_LAMBDA_8GB']
- **Required**: Yes

### scalingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ScalingConfigurationInputTypeDef]

### overflowBehavior
- **Type**: typing.Optional[typing.Literal['ON_DEMAND', 'QUEUE']]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.VpcConfigTypeDef]

### fleetServiceRole
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codebuild_classes.TagTypeDef]]


# CreateFleetOutputTypeDef

### fleet
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.FleetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProjectInputRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ProjectSourceTypeDef'>
- **Required**: Yes

### artifacts
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ProjectArtifactsTypeDef'>
- **Required**: Yes

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ProjectEnvironmentTypeDef'>
- **Required**: Yes

### serviceRole
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### secondarySources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codebuild_classes.ProjectSourceTypeDef]]

### sourceVersion
- **Type**: typing.Optional[str]

### secondarySourceVersions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codebuild_classes.ProjectSourceVersionTypeDef]]

### secondaryArtifacts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codebuild_classes.ProjectArtifactsTypeDef]]

### cache
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectCacheTypeDef]

### timeoutInMinutes
- **Type**: typing.Optional[int]

### queuedTimeoutInMinutes
- **Type**: typing.Optional[int]

### encryptionKey
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codebuild_classes.TagTypeDef]]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.VpcConfigTypeDef]

### badgeEnabled
- **Type**: typing.Optional[bool]

### logsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.LogsConfigTypeDef]

### fileSystemLocations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codebuild_classes.ProjectFileSystemLocationTypeDef]]

### buildBatchConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectBuildBatchConfigTypeDef]

### concurrentBuildLimit
- **Type**: typing.Optional[int]


# CreateProjectOutputTypeDef

### project
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ProjectTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateReportGroupInputRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['CODE_COVERAGE', 'TEST']
- **Required**: Yes

### exportConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ReportExportConfigTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codebuild_classes.TagTypeDef]]


# CreateReportGroupOutputTypeDef

### reportGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ReportGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWebhookInputRequestTypeDef

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### branchFilter
- **Type**: typing.Optional[str]

### filterGroups
- **Type**: typing.Optional[typing.Sequence[typing.Sequence[aws_resource_validator.pydantic_models.codebuild_classes.WebhookFilterTypeDef]]]

### buildType
- **Type**: typing.Optional[typing.Literal['BUILD', 'BUILD_BATCH']]

### manualCreation
- **Type**: typing.Optional[bool]

### scopeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ScopeConfigurationTypeDef]


# CreateWebhookOutputTypeDef

### webhook
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.WebhookTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DebugSessionTypeDef

### sessionEnabled
- **Type**: typing.Optional[bool]

### sessionTarget
- **Type**: typing.Optional[str]


# DeleteBuildBatchInputRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBuildBatchOutputTypeDef

### statusCode
- **Type**: <class 'str'>
- **Required**: Yes

### buildsDeleted
- **Type**: typing.List[str]
- **Required**: Yes

### buildsNotDeleted
- **Type**: typing.List[aws_resource_validator.pydantic_models.codebuild_classes.BuildNotDeletedTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteFleetInputRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProjectInputRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReportGroupInputRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### deleteReports
- **Type**: typing.Optional[bool]


# DeleteReportInputRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourcePolicyInputRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSourceCredentialsInputRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSourceCredentialsOutputTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteWebhookInputRequestTypeDef

### projectName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCodeCoveragesInputDescribeCodeCoveragesPaginateTypeDef

### reportArn
- **Type**: <class 'str'>
- **Required**: Yes

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### sortBy
- **Type**: typing.Optional[typing.Literal['FILE_PATH', 'LINE_COVERAGE_PERCENTAGE']]

### minLineCoveragePercentage
- **Type**: typing.Optional[float]

### maxLineCoveragePercentage
- **Type**: typing.Optional[float]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.PaginatorConfigTypeDef]


# DescribeCodeCoveragesInputRequestTypeDef

### reportArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### sortBy
- **Type**: typing.Optional[typing.Literal['FILE_PATH', 'LINE_COVERAGE_PERCENTAGE']]

### minLineCoveragePercentage
- **Type**: typing.Optional[float]

### maxLineCoveragePercentage
- **Type**: typing.Optional[float]


# DescribeCodeCoveragesOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### codeCoverages
- **Type**: typing.List[aws_resource_validator.pydantic_models.codebuild_classes.CodeCoverageTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTestCasesInputDescribeTestCasesPaginateTypeDef

### reportArn
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.TestCaseFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.PaginatorConfigTypeDef]


# DescribeTestCasesInputRequestTypeDef

### reportArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.TestCaseFilterTypeDef]


# DescribeTestCasesOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### testCases
- **Type**: typing.List[aws_resource_validator.pydantic_models.codebuild_classes.TestCaseTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnvironmentImageTypeDef

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### versions
- **Type**: typing.Optional[typing.List[str]]


# EnvironmentLanguageTypeDef

### language
- **Type**: typing.Optional[typing.Literal['ANDROID', 'BASE', 'DOCKER', 'DOTNET', 'GOLANG', 'JAVA', 'NODE_JS', 'PHP', 'PYTHON', 'RUBY']]

### images
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild_classes.EnvironmentImageTypeDef]]


# EnvironmentPlatformTypeDef

### platform
- **Type**: typing.Optional[typing.Literal['AMAZON_LINUX', 'DEBIAN', 'UBUNTU', 'WINDOWS_SERVER']]

### languages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild_classes.EnvironmentLanguageTypeDef]]


# EnvironmentVariableTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['PARAMETER_STORE', 'PLAINTEXT', 'SECRETS_MANAGER']]


# ExportedEnvironmentVariableTypeDef

### name
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# FleetStatusTypeDef

### statusCode
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETING', 'PENDING_DELETION', 'ROTATING', 'UPDATE_ROLLBACK_FAILED', 'UPDATING']]

### context
- **Type**: typing.Optional[typing.Literal['ACTION_REQUIRED', 'CREATE_FAILED', 'UPDATE_FAILED']]

### message
- **Type**: typing.Optional[str]


# FleetTypeDef

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### created
- **Type**: typing.Optional[datetime.datetime]

### lastModified
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.FleetStatusTypeDef]

### baseCapacity
- **Type**: typing.Optional[int]

### environmentType
- **Type**: typing.Optional[typing.Literal['ARM_CONTAINER', 'ARM_LAMBDA_CONTAINER', 'LINUX_CONTAINER', 'LINUX_GPU_CONTAINER', 'LINUX_LAMBDA_CONTAINER', 'WINDOWS_CONTAINER', 'WINDOWS_SERVER_2019_CONTAINER']]

### computeType
- **Type**: typing.Optional[typing.Literal['BUILD_GENERAL1_2XLARGE', 'BUILD_GENERAL1_LARGE', 'BUILD_GENERAL1_MEDIUM', 'BUILD_GENERAL1_SMALL', 'BUILD_GENERAL1_XLARGE', 'BUILD_LAMBDA_10GB', 'BUILD_LAMBDA_1GB', 'BUILD_LAMBDA_2GB', 'BUILD_LAMBDA_4GB', 'BUILD_LAMBDA_8GB']]

### scalingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ScalingConfigurationOutputTypeDef]

### overflowBehavior
- **Type**: typing.Optional[typing.Literal['ON_DEMAND', 'QUEUE']]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.VpcConfigOutputTypeDef]

### fleetServiceRole
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild_classes.TagTypeDef]]


# GetReportGroupTrendInputRequestTypeDef

### reportGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### trendField
- **Type**: typing.Literal['BRANCHES_COVERED', 'BRANCHES_MISSED', 'BRANCH_COVERAGE', 'DURATION', 'LINES_COVERED', 'LINES_MISSED', 'LINE_COVERAGE', 'PASS_RATE', 'TOTAL']
- **Required**: Yes

### numOfReports
- **Type**: typing.Optional[int]


# GetReportGroupTrendOutputTypeDef

### stats
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ReportGroupTrendStatsTypeDef'>
- **Required**: Yes

### rawData
- **Type**: typing.List[aws_resource_validator.pydantic_models.codebuild_classes.ReportWithRawDataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourcePolicyInputRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourcePolicyOutputTypeDef

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GitSubmodulesConfigTypeDef

### fetchSubmodules
- **Type**: <class 'bool'>
- **Required**: Yes


# ImportSourceCredentialsInputRequestTypeDef

### token
- **Type**: <class 'str'>
- **Required**: Yes

### serverType
- **Type**: typing.Literal['BITBUCKET', 'GITHUB', 'GITHUB_ENTERPRISE', 'GITLAB', 'GITLAB_SELF_MANAGED']
- **Required**: Yes

### authType
- **Type**: typing.Literal['BASIC_AUTH', 'CODECONNECTIONS', 'OAUTH', 'PERSONAL_ACCESS_TOKEN']
- **Required**: Yes

### username
- **Type**: typing.Optional[str]

### shouldOverwrite
- **Type**: typing.Optional[bool]


# ImportSourceCredentialsOutputTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InvalidateProjectCacheInputRequestTypeDef

### projectName
- **Type**: <class 'str'>
- **Required**: Yes


# ListBuildBatchesForProjectInputListBuildBatchesForProjectPaginateTypeDef

### projectName
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.BuildBatchFilterTypeDef]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.PaginatorConfigTypeDef]


# ListBuildBatchesForProjectInputRequestTypeDef

### projectName
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.BuildBatchFilterTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### nextToken
- **Type**: typing.Optional[str]


# ListBuildBatchesForProjectOutputTypeDef

### ids
- **Type**: typing.List[str]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBuildBatchesInputListBuildBatchesPaginateTypeDef

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.BuildBatchFilterTypeDef]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.PaginatorConfigTypeDef]


# ListBuildBatchesInputRequestTypeDef

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.BuildBatchFilterTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### nextToken
- **Type**: typing.Optional[str]


# ListBuildBatchesOutputTypeDef

### ids
- **Type**: typing.List[str]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBuildsForProjectInputListBuildsForProjectPaginateTypeDef

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.PaginatorConfigTypeDef]


# ListBuildsForProjectInputRequestTypeDef

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### nextToken
- **Type**: typing.Optional[str]


# ListBuildsForProjectOutputTypeDef

### ids
- **Type**: typing.List[str]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBuildsInputListBuildsPaginateTypeDef

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.PaginatorConfigTypeDef]


# ListBuildsInputRequestTypeDef

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### nextToken
- **Type**: typing.Optional[str]


# ListBuildsOutputTypeDef

### ids
- **Type**: typing.List[str]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCuratedEnvironmentImagesOutputTypeDef

### platforms
- **Type**: typing.List[aws_resource_validator.pydantic_models.codebuild_classes.EnvironmentPlatformTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFleetsInputRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### sortBy
- **Type**: typing.Optional[typing.Literal['CREATED_TIME', 'LAST_MODIFIED_TIME', 'NAME']]


# ListFleetsOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### fleets
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProjectsInputListProjectsPaginateTypeDef

### sortBy
- **Type**: typing.Optional[typing.Literal['CREATED_TIME', 'LAST_MODIFIED_TIME', 'NAME']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.PaginatorConfigTypeDef]


# ListProjectsInputRequestTypeDef

### sortBy
- **Type**: typing.Optional[typing.Literal['CREATED_TIME', 'LAST_MODIFIED_TIME', 'NAME']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### nextToken
- **Type**: typing.Optional[str]


# ListProjectsOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### projects
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListReportGroupsInputListReportGroupsPaginateTypeDef

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### sortBy
- **Type**: typing.Optional[typing.Literal['CREATED_TIME', 'LAST_MODIFIED_TIME', 'NAME']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.PaginatorConfigTypeDef]


# ListReportGroupsInputRequestTypeDef

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### sortBy
- **Type**: typing.Optional[typing.Literal['CREATED_TIME', 'LAST_MODIFIED_TIME', 'NAME']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListReportGroupsOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### reportGroups
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListReportsForReportGroupInputListReportsForReportGroupPaginateTypeDef

### reportGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ReportFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.PaginatorConfigTypeDef]


# ListReportsForReportGroupInputRequestTypeDef

### reportGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### maxResults
- **Type**: typing.Optional[int]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ReportFilterTypeDef]


# ListReportsForReportGroupOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### reports
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListReportsInputListReportsPaginateTypeDef

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ReportFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.PaginatorConfigTypeDef]


# ListReportsInputRequestTypeDef

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ReportFilterTypeDef]


# ListReportsOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### reports
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSharedProjectsInputListSharedProjectsPaginateTypeDef

### sortBy
- **Type**: typing.Optional[typing.Literal['ARN', 'MODIFIED_TIME']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.PaginatorConfigTypeDef]


# ListSharedProjectsInputRequestTypeDef

### sortBy
- **Type**: typing.Optional[typing.Literal['ARN', 'MODIFIED_TIME']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSharedProjectsOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### projects
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSharedReportGroupsInputListSharedReportGroupsPaginateTypeDef

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### sortBy
- **Type**: typing.Optional[typing.Literal['ARN', 'MODIFIED_TIME']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.PaginatorConfigTypeDef]


# ListSharedReportGroupsInputRequestTypeDef

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### sortBy
- **Type**: typing.Optional[typing.Literal['ARN', 'MODIFIED_TIME']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListSharedReportGroupsOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### reportGroups
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSourceCredentialsOutputTypeDef

### sourceCredentialsInfos
- **Type**: typing.List[aws_resource_validator.pydantic_models.codebuild_classes.SourceCredentialsInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LogsConfigTypeDef

### cloudWatchLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.CloudWatchLogsConfigTypeDef]

### s3Logs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.S3LogsConfigTypeDef]


# LogsLocationTypeDef

### groupName
- **Type**: typing.Optional[str]

### streamName
- **Type**: typing.Optional[str]

### deepLink
- **Type**: typing.Optional[str]

### s3DeepLink
- **Type**: typing.Optional[str]

### cloudWatchLogsArn
- **Type**: typing.Optional[str]

### s3LogsArn
- **Type**: typing.Optional[str]

### cloudWatchLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.CloudWatchLogsConfigTypeDef]

### s3Logs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.S3LogsConfigTypeDef]


# NetworkInterfaceTypeDef

### subnetId
- **Type**: typing.Optional[str]

### networkInterfaceId
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PhaseContextTypeDef

### statusCode
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]


# ProjectArtifactsTypeDef

### type
- **Type**: typing.Literal['CODEPIPELINE', 'NO_ARTIFACTS', 'S3']
- **Required**: Yes

### location
- **Type**: typing.Optional[str]

### path
- **Type**: typing.Optional[str]

### namespaceType
- **Type**: typing.Optional[typing.Literal['BUILD_ID', 'NONE']]

### name
- **Type**: typing.Optional[str]

### packaging
- **Type**: typing.Optional[typing.Literal['NONE', 'ZIP']]

### overrideArtifactName
- **Type**: typing.Optional[bool]

### encryptionDisabled
- **Type**: typing.Optional[bool]

### artifactIdentifier
- **Type**: typing.Optional[str]

### bucketOwnerAccess
- **Type**: typing.Optional[typing.Literal['FULL', 'NONE', 'READ_ONLY']]


# ProjectBadgeTypeDef

### badgeEnabled
- **Type**: typing.Optional[bool]

### badgeRequestUrl
- **Type**: typing.Optional[str]


# ProjectBuildBatchConfigOutputTypeDef

### serviceRole
- **Type**: typing.Optional[str]

### combineArtifacts
- **Type**: typing.Optional[bool]

### restrictions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.BatchRestrictionsOutputTypeDef]

### timeoutInMins
- **Type**: typing.Optional[int]

### batchReportMode
- **Type**: typing.Optional[typing.Literal['REPORT_AGGREGATED_BATCH', 'REPORT_INDIVIDUAL_BUILDS']]


# ProjectBuildBatchConfigTypeDef

### serviceRole
- **Type**: typing.Optional[str]

### combineArtifacts
- **Type**: typing.Optional[bool]

### restrictions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.BatchRestrictionsTypeDef]

### timeoutInMins
- **Type**: typing.Optional[int]

### batchReportMode
- **Type**: typing.Optional[typing.Literal['REPORT_AGGREGATED_BATCH', 'REPORT_INDIVIDUAL_BUILDS']]


# ProjectCacheOutputTypeDef

### type
- **Type**: typing.Literal['LOCAL', 'NO_CACHE', 'S3']
- **Required**: Yes

### location
- **Type**: typing.Optional[str]

### modes
- **Type**: typing.Optional[typing.List[typing.Literal['LOCAL_CUSTOM_CACHE', 'LOCAL_DOCKER_LAYER_CACHE', 'LOCAL_SOURCE_CACHE']]]


# ProjectCacheTypeDef

### type
- **Type**: typing.Literal['LOCAL', 'NO_CACHE', 'S3']
- **Required**: Yes

### location
- **Type**: typing.Optional[str]

### modes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['LOCAL_CUSTOM_CACHE', 'LOCAL_DOCKER_LAYER_CACHE', 'LOCAL_SOURCE_CACHE']]]


# ProjectEnvironmentOutputTypeDef

### type
- **Type**: typing.Literal['ARM_CONTAINER', 'ARM_LAMBDA_CONTAINER', 'LINUX_CONTAINER', 'LINUX_GPU_CONTAINER', 'LINUX_LAMBDA_CONTAINER', 'WINDOWS_CONTAINER', 'WINDOWS_SERVER_2019_CONTAINER']
- **Required**: Yes

### image
- **Type**: <class 'str'>
- **Required**: Yes

### computeType
- **Type**: typing.Literal['BUILD_GENERAL1_2XLARGE', 'BUILD_GENERAL1_LARGE', 'BUILD_GENERAL1_MEDIUM', 'BUILD_GENERAL1_SMALL', 'BUILD_GENERAL1_XLARGE', 'BUILD_LAMBDA_10GB', 'BUILD_LAMBDA_1GB', 'BUILD_LAMBDA_2GB', 'BUILD_LAMBDA_4GB', 'BUILD_LAMBDA_8GB']
- **Required**: Yes

### fleet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectFleetTypeDef]

### environmentVariables
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild_classes.EnvironmentVariableTypeDef]]

### privilegedMode
- **Type**: typing.Optional[bool]

### certificate
- **Type**: typing.Optional[str]

### registryCredential
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.RegistryCredentialTypeDef]

### imagePullCredentialsType
- **Type**: typing.Optional[typing.Literal['CODEBUILD', 'SERVICE_ROLE']]


# ProjectEnvironmentTypeDef

### type
- **Type**: typing.Literal['ARM_CONTAINER', 'ARM_LAMBDA_CONTAINER', 'LINUX_CONTAINER', 'LINUX_GPU_CONTAINER', 'LINUX_LAMBDA_CONTAINER', 'WINDOWS_CONTAINER', 'WINDOWS_SERVER_2019_CONTAINER']
- **Required**: Yes

### image
- **Type**: <class 'str'>
- **Required**: Yes

### computeType
- **Type**: typing.Literal['BUILD_GENERAL1_2XLARGE', 'BUILD_GENERAL1_LARGE', 'BUILD_GENERAL1_MEDIUM', 'BUILD_GENERAL1_SMALL', 'BUILD_GENERAL1_XLARGE', 'BUILD_LAMBDA_10GB', 'BUILD_LAMBDA_1GB', 'BUILD_LAMBDA_2GB', 'BUILD_LAMBDA_4GB', 'BUILD_LAMBDA_8GB']
- **Required**: Yes

### fleet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectFleetTypeDef]

### environmentVariables
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codebuild_classes.EnvironmentVariableTypeDef]]

### privilegedMode
- **Type**: typing.Optional[bool]

### certificate
- **Type**: typing.Optional[str]

### registryCredential
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.RegistryCredentialTypeDef]

### imagePullCredentialsType
- **Type**: typing.Optional[typing.Literal['CODEBUILD', 'SERVICE_ROLE']]


# ProjectFileSystemLocationTypeDef

### type
- **Type**: typing.Optional[typing.Literal['EFS']]

### location
- **Type**: typing.Optional[str]

### mountPoint
- **Type**: typing.Optional[str]

### identifier
- **Type**: typing.Optional[str]

### mountOptions
- **Type**: typing.Optional[str]


# ProjectFleetTypeDef

### fleetArn
- **Type**: typing.Optional[str]


# ProjectSourceTypeDef

### type
- **Type**: typing.Literal['BITBUCKET', 'CODECOMMIT', 'CODEPIPELINE', 'GITHUB', 'GITHUB_ENTERPRISE', 'GITLAB', 'GITLAB_SELF_MANAGED', 'NO_SOURCE', 'S3']
- **Required**: Yes

### location
- **Type**: typing.Optional[str]

### gitCloneDepth
- **Type**: typing.Optional[int]

### gitSubmodulesConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.GitSubmodulesConfigTypeDef]

### buildspec
- **Type**: typing.Optional[str]

### auth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.SourceAuthTypeDef]

### reportBuildStatus
- **Type**: typing.Optional[bool]

### buildStatusConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.BuildStatusConfigTypeDef]

### insecureSsl
- **Type**: typing.Optional[bool]

### sourceIdentifier
- **Type**: typing.Optional[str]


# ProjectSourceVersionTypeDef

### sourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### sourceVersion
- **Type**: <class 'str'>
- **Required**: Yes


# ProjectTypeDef

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectSourceTypeDef]

### secondarySources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild_classes.ProjectSourceTypeDef]]

### sourceVersion
- **Type**: typing.Optional[str]

### secondarySourceVersions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild_classes.ProjectSourceVersionTypeDef]]

### artifacts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectArtifactsTypeDef]

### secondaryArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild_classes.ProjectArtifactsTypeDef]]

### cache
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectCacheOutputTypeDef]

### environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectEnvironmentOutputTypeDef]

### serviceRole
- **Type**: typing.Optional[str]

### timeoutInMinutes
- **Type**: typing.Optional[int]

### queuedTimeoutInMinutes
- **Type**: typing.Optional[int]

### encryptionKey
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild_classes.TagTypeDef]]

### created
- **Type**: typing.Optional[datetime.datetime]

### lastModified
- **Type**: typing.Optional[datetime.datetime]

### webhook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.WebhookTypeDef]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.VpcConfigOutputTypeDef]

### badge
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectBadgeTypeDef]

### logsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.LogsConfigTypeDef]

### fileSystemLocations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild_classes.ProjectFileSystemLocationTypeDef]]

### buildBatchConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectBuildBatchConfigOutputTypeDef]

### concurrentBuildLimit
- **Type**: typing.Optional[int]

### projectVisibility
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'PUBLIC_READ']]

### publicProjectAlias
- **Type**: typing.Optional[str]

### resourceAccessRole
- **Type**: typing.Optional[str]


# PutResourcePolicyInputRequestTypeDef

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# PutResourcePolicyOutputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegistryCredentialTypeDef

### credential
- **Type**: <class 'str'>
- **Required**: Yes

### credentialProvider
- **Type**: typing.Literal['SECRETS_MANAGER']
- **Required**: Yes


# ReportExportConfigTypeDef

### exportConfigType
- **Type**: typing.Optional[typing.Literal['NO_EXPORT', 'S3']]

### s3Destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.S3ReportExportConfigTypeDef]


# ReportFilterTypeDef

### status
- **Type**: typing.Optional[typing.Literal['DELETING', 'FAILED', 'GENERATING', 'INCOMPLETE', 'SUCCEEDED']]


# ReportGroupTrendStatsTypeDef

### average
- **Type**: typing.Optional[str]

### max
- **Type**: typing.Optional[str]

### min
- **Type**: typing.Optional[str]


# ReportGroupTypeDef

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['CODE_COVERAGE', 'TEST']]

### exportConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ReportExportConfigTypeDef]

### created
- **Type**: typing.Optional[datetime.datetime]

### lastModified
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild_classes.TagTypeDef]]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING']]


# ReportTypeDef

### arn
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['CODE_COVERAGE', 'TEST']]

### name
- **Type**: typing.Optional[str]

### reportGroupArn
- **Type**: typing.Optional[str]

### executionId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DELETING', 'FAILED', 'GENERATING', 'INCOMPLETE', 'SUCCEEDED']]

### created
- **Type**: typing.Optional[datetime.datetime]

### expired
- **Type**: typing.Optional[datetime.datetime]

### exportConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ReportExportConfigTypeDef]

### truncated
- **Type**: typing.Optional[bool]

### testSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.TestReportSummaryTypeDef]

### codeCoverageSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.CodeCoverageReportSummaryTypeDef]


# ReportWithRawDataTypeDef

### reportArn
- **Type**: typing.Optional[str]

### data
- **Type**: typing.Optional[str]


# ResolvedArtifactTypeDef

### type
- **Type**: typing.Optional[typing.Literal['CODEPIPELINE', 'NO_ARTIFACTS', 'S3']]

### location
- **Type**: typing.Optional[str]

### identifier
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


# RetryBuildBatchInputRequestTypeDef

### id
- **Type**: typing.Optional[str]

### idempotencyToken
- **Type**: typing.Optional[str]

### retryType
- **Type**: typing.Optional[typing.Literal['RETRY_ALL_BUILDS', 'RETRY_FAILED_BUILDS']]


# RetryBuildBatchOutputTypeDef

### buildBatch
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.BuildBatchTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RetryBuildInputRequestTypeDef

### id
- **Type**: typing.Optional[str]

### idempotencyToken
- **Type**: typing.Optional[str]


# RetryBuildOutputTypeDef

### build
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.BuildTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# S3LogsConfigTypeDef

### status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### location
- **Type**: typing.Optional[str]

### encryptionDisabled
- **Type**: typing.Optional[bool]

### bucketOwnerAccess
- **Type**: typing.Optional[typing.Literal['FULL', 'NONE', 'READ_ONLY']]


# S3ReportExportConfigTypeDef

### bucket
- **Type**: typing.Optional[str]

### bucketOwner
- **Type**: typing.Optional[str]

### path
- **Type**: typing.Optional[str]

### packaging
- **Type**: typing.Optional[typing.Literal['NONE', 'ZIP']]

### encryptionKey
- **Type**: typing.Optional[str]

### encryptionDisabled
- **Type**: typing.Optional[bool]


# ScalingConfigurationInputTypeDef

### scalingType
- **Type**: typing.Optional[typing.Literal['TARGET_TRACKING_SCALING']]

### targetTrackingScalingConfigs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codebuild_classes.TargetTrackingScalingConfigurationTypeDef]]

### maxCapacity
- **Type**: typing.Optional[int]


# ScalingConfigurationOutputTypeDef

### scalingType
- **Type**: typing.Optional[typing.Literal['TARGET_TRACKING_SCALING']]

### targetTrackingScalingConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild_classes.TargetTrackingScalingConfigurationTypeDef]]

### maxCapacity
- **Type**: typing.Optional[int]

### desiredCapacity
- **Type**: typing.Optional[int]


# ScopeConfigurationTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### scope
- **Type**: typing.Literal['GITHUB_GLOBAL', 'GITHUB_ORGANIZATION']
- **Required**: Yes

### domain
- **Type**: typing.Optional[str]


# SourceAuthTypeDef

### type
- **Type**: typing.Literal['CODECONNECTIONS', 'OAUTH']
- **Required**: Yes

### resource
- **Type**: typing.Optional[str]


# SourceCredentialsInfoTypeDef

### arn
- **Type**: typing.Optional[str]

### serverType
- **Type**: typing.Optional[typing.Literal['BITBUCKET', 'GITHUB', 'GITHUB_ENTERPRISE', 'GITLAB', 'GITLAB_SELF_MANAGED']]

### authType
- **Type**: typing.Optional[typing.Literal['BASIC_AUTH', 'CODECONNECTIONS', 'OAUTH', 'PERSONAL_ACCESS_TOKEN']]

### resource
- **Type**: typing.Optional[str]


# StartBuildBatchInputRequestTypeDef

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### secondarySourcesOverride
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codebuild_classes.ProjectSourceTypeDef]]

### secondarySourcesVersionOverride
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codebuild_classes.ProjectSourceVersionTypeDef]]

### sourceVersion
- **Type**: typing.Optional[str]

### artifactsOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectArtifactsTypeDef]

### secondaryArtifactsOverride
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codebuild_classes.ProjectArtifactsTypeDef]]

### environmentVariablesOverride
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codebuild_classes.EnvironmentVariableTypeDef]]

### sourceTypeOverride
- **Type**: typing.Optional[typing.Literal['BITBUCKET', 'CODECOMMIT', 'CODEPIPELINE', 'GITHUB', 'GITHUB_ENTERPRISE', 'GITLAB', 'GITLAB_SELF_MANAGED', 'NO_SOURCE', 'S3']]

### sourceLocationOverride
- **Type**: typing.Optional[str]

### sourceAuthOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.SourceAuthTypeDef]

### gitCloneDepthOverride
- **Type**: typing.Optional[int]

### gitSubmodulesConfigOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.GitSubmodulesConfigTypeDef]

### buildspecOverride
- **Type**: typing.Optional[str]

### insecureSslOverride
- **Type**: typing.Optional[bool]

### reportBuildBatchStatusOverride
- **Type**: typing.Optional[bool]

### environmentTypeOverride
- **Type**: typing.Optional[typing.Literal['ARM_CONTAINER', 'ARM_LAMBDA_CONTAINER', 'LINUX_CONTAINER', 'LINUX_GPU_CONTAINER', 'LINUX_LAMBDA_CONTAINER', 'WINDOWS_CONTAINER', 'WINDOWS_SERVER_2019_CONTAINER']]

### imageOverride
- **Type**: typing.Optional[str]

### computeTypeOverride
- **Type**: typing.Optional[typing.Literal['BUILD_GENERAL1_2XLARGE', 'BUILD_GENERAL1_LARGE', 'BUILD_GENERAL1_MEDIUM', 'BUILD_GENERAL1_SMALL', 'BUILD_GENERAL1_XLARGE', 'BUILD_LAMBDA_10GB', 'BUILD_LAMBDA_1GB', 'BUILD_LAMBDA_2GB', 'BUILD_LAMBDA_4GB', 'BUILD_LAMBDA_8GB']]

### certificateOverride
- **Type**: typing.Optional[str]

### cacheOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectCacheTypeDef]

### serviceRoleOverride
- **Type**: typing.Optional[str]

### privilegedModeOverride
- **Type**: typing.Optional[bool]

### buildTimeoutInMinutesOverride
- **Type**: typing.Optional[int]

### queuedTimeoutInMinutesOverride
- **Type**: typing.Optional[int]

### encryptionKeyOverride
- **Type**: typing.Optional[str]

### idempotencyToken
- **Type**: typing.Optional[str]

### logsConfigOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.LogsConfigTypeDef]

### registryCredentialOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.RegistryCredentialTypeDef]

### imagePullCredentialsTypeOverride
- **Type**: typing.Optional[typing.Literal['CODEBUILD', 'SERVICE_ROLE']]

### buildBatchConfigOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectBuildBatchConfigTypeDef]

### debugSessionEnabled
- **Type**: typing.Optional[bool]


# StartBuildBatchOutputTypeDef

### buildBatch
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.BuildBatchTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartBuildInputRequestTypeDef

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### secondarySourcesOverride
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codebuild_classes.ProjectSourceTypeDef]]

### secondarySourcesVersionOverride
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codebuild_classes.ProjectSourceVersionTypeDef]]

### sourceVersion
- **Type**: typing.Optional[str]

### artifactsOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectArtifactsTypeDef]

### secondaryArtifactsOverride
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codebuild_classes.ProjectArtifactsTypeDef]]

### environmentVariablesOverride
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codebuild_classes.EnvironmentVariableTypeDef]]

### sourceTypeOverride
- **Type**: typing.Optional[typing.Literal['BITBUCKET', 'CODECOMMIT', 'CODEPIPELINE', 'GITHUB', 'GITHUB_ENTERPRISE', 'GITLAB', 'GITLAB_SELF_MANAGED', 'NO_SOURCE', 'S3']]

### sourceLocationOverride
- **Type**: typing.Optional[str]

### sourceAuthOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.SourceAuthTypeDef]

### gitCloneDepthOverride
- **Type**: typing.Optional[int]

### gitSubmodulesConfigOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.GitSubmodulesConfigTypeDef]

### buildspecOverride
- **Type**: typing.Optional[str]

### insecureSslOverride
- **Type**: typing.Optional[bool]

### reportBuildStatusOverride
- **Type**: typing.Optional[bool]

### buildStatusConfigOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.BuildStatusConfigTypeDef]

### environmentTypeOverride
- **Type**: typing.Optional[typing.Literal['ARM_CONTAINER', 'ARM_LAMBDA_CONTAINER', 'LINUX_CONTAINER', 'LINUX_GPU_CONTAINER', 'LINUX_LAMBDA_CONTAINER', 'WINDOWS_CONTAINER', 'WINDOWS_SERVER_2019_CONTAINER']]

### imageOverride
- **Type**: typing.Optional[str]

### computeTypeOverride
- **Type**: typing.Optional[typing.Literal['BUILD_GENERAL1_2XLARGE', 'BUILD_GENERAL1_LARGE', 'BUILD_GENERAL1_MEDIUM', 'BUILD_GENERAL1_SMALL', 'BUILD_GENERAL1_XLARGE', 'BUILD_LAMBDA_10GB', 'BUILD_LAMBDA_1GB', 'BUILD_LAMBDA_2GB', 'BUILD_LAMBDA_4GB', 'BUILD_LAMBDA_8GB']]

### certificateOverride
- **Type**: typing.Optional[str]

### cacheOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectCacheTypeDef]

### serviceRoleOverride
- **Type**: typing.Optional[str]

### privilegedModeOverride
- **Type**: typing.Optional[bool]

### timeoutInMinutesOverride
- **Type**: typing.Optional[int]

### queuedTimeoutInMinutesOverride
- **Type**: typing.Optional[int]

### encryptionKeyOverride
- **Type**: typing.Optional[str]

### idempotencyToken
- **Type**: typing.Optional[str]

### logsConfigOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.LogsConfigTypeDef]

### registryCredentialOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.RegistryCredentialTypeDef]

### imagePullCredentialsTypeOverride
- **Type**: typing.Optional[typing.Literal['CODEBUILD', 'SERVICE_ROLE']]

### debugSessionEnabled
- **Type**: typing.Optional[bool]

### fleetOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectFleetTypeDef]


# StartBuildOutputTypeDef

### build
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.BuildTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopBuildBatchInputRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# StopBuildBatchOutputTypeDef

### buildBatch
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.BuildBatchTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopBuildInputRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# StopBuildOutputTypeDef

### build
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.BuildTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagTypeDef

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# TargetTrackingScalingConfigurationTypeDef

### metricType
- **Type**: typing.Optional[typing.Literal['FLEET_UTILIZATION_RATE']]

### targetValue
- **Type**: typing.Optional[float]


# TestCaseFilterTypeDef

### status
- **Type**: typing.Optional[str]

### keyword
- **Type**: typing.Optional[str]


# TestCaseTypeDef

### reportArn
- **Type**: typing.Optional[str]

### testRawDataPath
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### durationInNanoSeconds
- **Type**: typing.Optional[int]

### message
- **Type**: typing.Optional[str]

### expired
- **Type**: typing.Optional[datetime.datetime]


# TestReportSummaryTypeDef

### total
- **Type**: <class 'int'>
- **Required**: Yes

### statusCounts
- **Type**: typing.Dict[str, int]
- **Required**: Yes

### durationInNanoSeconds
- **Type**: <class 'int'>
- **Required**: Yes


# UpdateFleetInputRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### baseCapacity
- **Type**: typing.Optional[int]

### environmentType
- **Type**: typing.Optional[typing.Literal['ARM_CONTAINER', 'ARM_LAMBDA_CONTAINER', 'LINUX_CONTAINER', 'LINUX_GPU_CONTAINER', 'LINUX_LAMBDA_CONTAINER', 'WINDOWS_CONTAINER', 'WINDOWS_SERVER_2019_CONTAINER']]

### computeType
- **Type**: typing.Optional[typing.Literal['BUILD_GENERAL1_2XLARGE', 'BUILD_GENERAL1_LARGE', 'BUILD_GENERAL1_MEDIUM', 'BUILD_GENERAL1_SMALL', 'BUILD_GENERAL1_XLARGE', 'BUILD_LAMBDA_10GB', 'BUILD_LAMBDA_1GB', 'BUILD_LAMBDA_2GB', 'BUILD_LAMBDA_4GB', 'BUILD_LAMBDA_8GB']]

### scalingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ScalingConfigurationInputTypeDef]

### overflowBehavior
- **Type**: typing.Optional[typing.Literal['ON_DEMAND', 'QUEUE']]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.VpcConfigTypeDef]

### fleetServiceRole
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codebuild_classes.TagTypeDef]]


# UpdateFleetOutputTypeDef

### fleet
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.FleetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateProjectInputRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectSourceTypeDef]

### secondarySources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codebuild_classes.ProjectSourceTypeDef]]

### sourceVersion
- **Type**: typing.Optional[str]

### secondarySourceVersions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codebuild_classes.ProjectSourceVersionTypeDef]]

### artifacts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectArtifactsTypeDef]

### secondaryArtifacts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codebuild_classes.ProjectArtifactsTypeDef]]

### cache
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectCacheTypeDef]

### environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectEnvironmentTypeDef]

### serviceRole
- **Type**: typing.Optional[str]

### timeoutInMinutes
- **Type**: typing.Optional[int]

### queuedTimeoutInMinutes
- **Type**: typing.Optional[int]

### encryptionKey
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codebuild_classes.TagTypeDef]]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.VpcConfigTypeDef]

### badgeEnabled
- **Type**: typing.Optional[bool]

### logsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.LogsConfigTypeDef]

### fileSystemLocations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codebuild_classes.ProjectFileSystemLocationTypeDef]]

### buildBatchConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectBuildBatchConfigTypeDef]

### concurrentBuildLimit
- **Type**: typing.Optional[int]


# UpdateProjectOutputTypeDef

### project
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ProjectTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateProjectVisibilityInputRequestTypeDef

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes

### projectVisibility
- **Type**: typing.Literal['PRIVATE', 'PUBLIC_READ']
- **Required**: Yes

### resourceAccessRole
- **Type**: typing.Optional[str]


# UpdateProjectVisibilityOutputTypeDef

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes

### publicProjectAlias
- **Type**: <class 'str'>
- **Required**: Yes

### projectVisibility
- **Type**: typing.Literal['PRIVATE', 'PUBLIC_READ']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateReportGroupInputRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### exportConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ReportExportConfigTypeDef]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codebuild_classes.TagTypeDef]]


# UpdateReportGroupOutputTypeDef

### reportGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ReportGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateWebhookInputRequestTypeDef

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### branchFilter
- **Type**: typing.Optional[str]

### rotateSecret
- **Type**: typing.Optional[bool]

### filterGroups
- **Type**: typing.Optional[typing.Sequence[typing.Sequence[aws_resource_validator.pydantic_models.codebuild_classes.WebhookFilterTypeDef]]]

### buildType
- **Type**: typing.Optional[typing.Literal['BUILD', 'BUILD_BATCH']]


# UpdateWebhookOutputTypeDef

### webhook
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.WebhookTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VpcConfigOutputTypeDef

### vpcId
- **Type**: typing.Optional[str]

### subnets
- **Type**: typing.Optional[typing.List[str]]

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# VpcConfigTypeDef

### vpcId
- **Type**: typing.Optional[str]

### subnets
- **Type**: typing.Optional[typing.Sequence[str]]

### securityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]


# WebhookFilterTypeDef

### type
- **Type**: typing.Literal['ACTOR_ACCOUNT_ID', 'BASE_REF', 'COMMIT_MESSAGE', 'EVENT', 'FILE_PATH', 'HEAD_REF', 'RELEASE_NAME', 'TAG_NAME', 'WORKFLOW_NAME']
- **Required**: Yes

### pattern
- **Type**: <class 'str'>
- **Required**: Yes

### excludeMatchedPattern
- **Type**: typing.Optional[bool]


# WebhookTypeDef

### url
- **Type**: typing.Optional[str]

### payloadUrl
- **Type**: typing.Optional[str]

### secret
- **Type**: typing.Optional[str]

### branchFilter
- **Type**: typing.Optional[str]

### filterGroups
- **Type**: typing.Optional[typing.List[typing.List[aws_resource_validator.pydantic_models.codebuild_classes.WebhookFilterTypeDef]]]

### buildType
- **Type**: typing.Optional[typing.Literal['BUILD', 'BUILD_BATCH']]

### manualCreation
- **Type**: typing.Optional[bool]

### lastModifiedSecret
- **Type**: typing.Optional[datetime.datetime]

### scopeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ScopeConfigurationTypeDef]


