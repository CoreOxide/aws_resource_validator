# Codebuild Classes

# AutoRetryConfigTypeDef

### autoRetryLimit
- **Type**: typing.Optional[int]

### autoRetryNumber
- **Type**: typing.Optional[int]

### nextAutoRetry
- **Type**: typing.Optional[str]

### previousAutoRetry
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDeleteBuildsInputTypeDef

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


# BatchGetBuildBatchesInputTypeDef

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


# BatchGetBuildsInputTypeDef

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


# BatchGetFleetsInputTypeDef

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


# BatchGetProjectsInputTypeDef

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


# BatchGetReportGroupsInputTypeDef

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


# BatchGetReportsInputTypeDef

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

### fleetsAllowed
- **Type**: typing.Optional[typing.List[str]]


# BatchRestrictionsTypeDef

### maximumBuildsAllowed
- **Type**: typing.Optional[int]

### computeTypesAllowed
- **Type**: typing.Optional[typing.Sequence[str]]

### fleetsAllowed
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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComputeConfigurationTypeDef

### vCpu
- **Type**: typing.Optional[int]

### memory
- **Type**: typing.Optional[int]

### disk
- **Type**: typing.Optional[int]

### machineType
- **Type**: typing.Optional[typing.Literal['GENERAL', 'NVME']]


# CreateFleetInputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### baseCapacity
- **Type**: <class 'int'>
- **Required**: Yes

### environmentType
- **Type**: typing.Literal['ARM_CONTAINER', 'ARM_EC2', 'ARM_LAMBDA_CONTAINER', 'LINUX_CONTAINER', 'LINUX_EC2', 'LINUX_GPU_CONTAINER', 'LINUX_LAMBDA_CONTAINER', 'MAC_ARM', 'WINDOWS_CONTAINER', 'WINDOWS_EC2', 'WINDOWS_SERVER_2019_CONTAINER']
- **Required**: Yes

### computeType
- **Type**: typing.Literal['ATTRIBUTE_BASED_COMPUTE', 'BUILD_GENERAL1_2XLARGE', 'BUILD_GENERAL1_LARGE', 'BUILD_GENERAL1_MEDIUM', 'BUILD_GENERAL1_SMALL', 'BUILD_GENERAL1_XLARGE', 'BUILD_LAMBDA_10GB', 'BUILD_LAMBDA_1GB', 'BUILD_LAMBDA_2GB', 'BUILD_LAMBDA_4GB', 'BUILD_LAMBDA_8GB']
- **Required**: Yes

### computeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ComputeConfigurationTypeDef]

### scalingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ScalingConfigurationInputTypeDef]

### overflowBehavior
- **Type**: typing.Optional[typing.Literal['ON_DEMAND', 'QUEUE']]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.VpcConfigUnionTypeDef]

### proxyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProxyConfigurationUnionTypeDef]

### imageId
- **Type**: typing.Optional[str]

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


# CreateProjectInputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ProjectEnvironmentUnionTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectCacheUnionTypeDef]

### timeoutInMinutes
- **Type**: typing.Optional[int]

### queuedTimeoutInMinutes
- **Type**: typing.Optional[int]

### encryptionKey
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codebuild_classes.TagTypeDef]]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.VpcConfigUnionTypeDef]

### badgeEnabled
- **Type**: typing.Optional[bool]

### logsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.LogsConfigTypeDef]

### fileSystemLocations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codebuild_classes.ProjectFileSystemLocationTypeDef]]

### buildBatchConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectBuildBatchConfigUnionTypeDef]

### concurrentBuildLimit
- **Type**: typing.Optional[int]

### autoRetryLimit
- **Type**: typing.Optional[int]


# CreateProjectOutputTypeDef

### project
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ProjectTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateReportGroupOutputTypeDef

### reportGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ReportGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWebhookInputTypeDef

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### branchFilter
- **Type**: typing.Optional[str]

### filterGroups
- **Type**: typing.Optional[typing.Sequence[typing.Sequence[aws_resource_validator.pydantic_models.codebuild_classes.WebhookFilterTypeDef]]]

### buildType
- **Type**: typing.Optional[typing.Literal['BUILD', 'BUILD_BATCH', 'RUNNER_BUILDKITE_BUILD']]

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


# DeleteFleetInputTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProjectInputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReportGroupInputTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### deleteReports
- **Type**: typing.Optional[bool]


# DeleteReportInputTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourcePolicyInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSourceCredentialsInputTypeDef

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


# DeleteWebhookInputTypeDef

### projectName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCodeCoveragesInputPaginateTypeDef

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


# DescribeCodeCoveragesInputTypeDef

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

### codeCoverages
- **Type**: typing.List[aws_resource_validator.pydantic_models.codebuild_classes.CodeCoverageTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeTestCasesOutputTypeDef

### testCases
- **Type**: typing.List[aws_resource_validator.pydantic_models.codebuild_classes.TestCaseTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ExportedEnvironmentVariableTypeDef

### name
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# FleetProxyRuleOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FleetProxyRuleTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FleetStatusTypeDef

### statusCode
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETING', 'PENDING_DELETION', 'ROTATING', 'UPDATE_ROLLBACK_FAILED', 'UPDATING']]

### context
- **Type**: typing.Optional[typing.Literal['ACTION_REQUIRED', 'CREATE_FAILED', 'INSUFFICIENT_CAPACITY', 'PENDING_DELETION', 'UPDATE_FAILED']]

### message
- **Type**: typing.Optional[str]


# FleetTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetReportGroupTrendInputTypeDef

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


# GetResourcePolicyInputTypeDef

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


# ImportSourceCredentialsInputTypeDef

### token
- **Type**: <class 'str'>
- **Required**: Yes

### serverType
- **Type**: typing.Literal['BITBUCKET', 'GITHUB', 'GITHUB_ENTERPRISE', 'GITLAB', 'GITLAB_SELF_MANAGED']
- **Required**: Yes

### authType
- **Type**: typing.Literal['BASIC_AUTH', 'CODECONNECTIONS', 'OAUTH', 'PERSONAL_ACCESS_TOKEN', 'SECRETS_MANAGER']
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


# InvalidateProjectCacheInputTypeDef

### projectName
- **Type**: <class 'str'>
- **Required**: Yes


# ListBuildBatchesForProjectOutputTypeDef

### ids
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBuildBatchesOutputTypeDef

### ids
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBuildsForProjectInputPaginateTypeDef

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.PaginatorConfigTypeDef]


# ListBuildsForProjectInputTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBuildsInputPaginateTypeDef

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.PaginatorConfigTypeDef]


# ListBuildsInputTypeDef

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### nextToken
- **Type**: typing.Optional[str]


# ListBuildsOutputTypeDef

### ids
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCuratedEnvironmentImagesOutputTypeDef

### platforms
- **Type**: typing.List[aws_resource_validator.pydantic_models.codebuild_classes.EnvironmentPlatformTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFleetsInputTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### sortBy
- **Type**: typing.Optional[typing.Literal['CREATED_TIME', 'LAST_MODIFIED_TIME', 'NAME']]


# ListFleetsOutputTypeDef

### fleets
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProjectsInputPaginateTypeDef

### sortBy
- **Type**: typing.Optional[typing.Literal['CREATED_TIME', 'LAST_MODIFIED_TIME', 'NAME']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.PaginatorConfigTypeDef]


# ListProjectsInputTypeDef

### sortBy
- **Type**: typing.Optional[typing.Literal['CREATED_TIME', 'LAST_MODIFIED_TIME', 'NAME']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### nextToken
- **Type**: typing.Optional[str]


# ListProjectsOutputTypeDef

### projects
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReportGroupsInputPaginateTypeDef

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### sortBy
- **Type**: typing.Optional[typing.Literal['CREATED_TIME', 'LAST_MODIFIED_TIME', 'NAME']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.PaginatorConfigTypeDef]


# ListReportGroupsInputTypeDef

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### sortBy
- **Type**: typing.Optional[typing.Literal['CREATED_TIME', 'LAST_MODIFIED_TIME', 'NAME']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListReportGroupsOutputTypeDef

### reportGroups
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReportsForReportGroupOutputTypeDef

### reports
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReportsOutputTypeDef

### reports
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSharedProjectsInputPaginateTypeDef

### sortBy
- **Type**: typing.Optional[typing.Literal['ARN', 'MODIFIED_TIME']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.PaginatorConfigTypeDef]


# ListSharedProjectsInputTypeDef

### sortBy
- **Type**: typing.Optional[typing.Literal['ARN', 'MODIFIED_TIME']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSharedProjectsOutputTypeDef

### projects
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSharedReportGroupsInputPaginateTypeDef

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### sortBy
- **Type**: typing.Optional[typing.Literal['ARN', 'MODIFIED_TIME']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.PaginatorConfigTypeDef]


# ListSharedReportGroupsInputTypeDef

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### sortBy
- **Type**: typing.Optional[typing.Literal['ARN', 'MODIFIED_TIME']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListSharedReportGroupsOutputTypeDef

### reportGroups
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# ProjectBuildBatchConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProjectCacheOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProjectCacheUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProjectEnvironmentOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProjectEnvironmentUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProjectFileSystemLocationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProjectFleetTypeDef

### fleetArn
- **Type**: typing.Optional[str]


# ProjectSourceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

### autoRetryLimit
- **Type**: typing.Optional[int]


# ProxyConfigurationOutputTypeDef

### defaultBehavior
- **Type**: typing.Optional[typing.Literal['ALLOW_ALL', 'DENY_ALL']]

### orderedProxyRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild_classes.FleetProxyRuleOutputTypeDef]]


# ProxyConfigurationTypeDef

### defaultBehavior
- **Type**: typing.Optional[typing.Literal['ALLOW_ALL', 'DENY_ALL']]

### orderedProxyRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codebuild_classes.FleetProxyRuleTypeDef]]


# ProxyConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PutResourcePolicyInputTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ReportGroupTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ReportTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ReportWithRawDataTypeDef

### reportArn
- **Type**: typing.Optional[str]

### data
- **Type**: typing.Optional[str]


# ResolvedArtifactTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# RetryBuildBatchOutputTypeDef

### buildBatch
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.BuildBatchTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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
- **Type**: typing.Literal['GITHUB_GLOBAL', 'GITHUB_ORGANIZATION', 'GITLAB_GROUP']
- **Required**: Yes

### domain
- **Type**: typing.Optional[str]


# SourceAuthTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SourceCredentialsInfoTypeDef

### arn
- **Type**: typing.Optional[str]

### serverType
- **Type**: typing.Optional[typing.Literal['BITBUCKET', 'GITHUB', 'GITHUB_ENTERPRISE', 'GITLAB', 'GITLAB_SELF_MANAGED']]

### authType
- **Type**: typing.Optional[typing.Literal['BASIC_AUTH', 'CODECONNECTIONS', 'OAUTH', 'PERSONAL_ACCESS_TOKEN', 'SECRETS_MANAGER']]

### resource
- **Type**: typing.Optional[str]


# StartBuildBatchInputTypeDef

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
- **Type**: typing.Optional[typing.Literal['ARM_CONTAINER', 'ARM_EC2', 'ARM_LAMBDA_CONTAINER', 'LINUX_CONTAINER', 'LINUX_EC2', 'LINUX_GPU_CONTAINER', 'LINUX_LAMBDA_CONTAINER', 'MAC_ARM', 'WINDOWS_CONTAINER', 'WINDOWS_EC2', 'WINDOWS_SERVER_2019_CONTAINER']]

### imageOverride
- **Type**: typing.Optional[str]

### computeTypeOverride
- **Type**: typing.Optional[typing.Literal['ATTRIBUTE_BASED_COMPUTE', 'BUILD_GENERAL1_2XLARGE', 'BUILD_GENERAL1_LARGE', 'BUILD_GENERAL1_MEDIUM', 'BUILD_GENERAL1_SMALL', 'BUILD_GENERAL1_XLARGE', 'BUILD_LAMBDA_10GB', 'BUILD_LAMBDA_1GB', 'BUILD_LAMBDA_2GB', 'BUILD_LAMBDA_4GB', 'BUILD_LAMBDA_8GB']]

### certificateOverride
- **Type**: typing.Optional[str]

### cacheOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectCacheUnionTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectBuildBatchConfigUnionTypeDef]

### debugSessionEnabled
- **Type**: typing.Optional[bool]


# StartBuildBatchOutputTypeDef

### buildBatch
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.BuildBatchTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartBuildInputTypeDef

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
- **Type**: typing.Optional[typing.Literal['ARM_CONTAINER', 'ARM_EC2', 'ARM_LAMBDA_CONTAINER', 'LINUX_CONTAINER', 'LINUX_EC2', 'LINUX_GPU_CONTAINER', 'LINUX_LAMBDA_CONTAINER', 'MAC_ARM', 'WINDOWS_CONTAINER', 'WINDOWS_EC2', 'WINDOWS_SERVER_2019_CONTAINER']]

### imageOverride
- **Type**: typing.Optional[str]

### computeTypeOverride
- **Type**: typing.Optional[typing.Literal['ATTRIBUTE_BASED_COMPUTE', 'BUILD_GENERAL1_2XLARGE', 'BUILD_GENERAL1_LARGE', 'BUILD_GENERAL1_MEDIUM', 'BUILD_GENERAL1_SMALL', 'BUILD_GENERAL1_XLARGE', 'BUILD_LAMBDA_10GB', 'BUILD_LAMBDA_1GB', 'BUILD_LAMBDA_2GB', 'BUILD_LAMBDA_4GB', 'BUILD_LAMBDA_8GB']]

### certificateOverride
- **Type**: typing.Optional[str]

### cacheOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectCacheUnionTypeDef]

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

### autoRetryLimitOverride
- **Type**: typing.Optional[int]


# StartBuildOutputTypeDef

### build
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.BuildTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopBuildBatchOutputTypeDef

### buildBatch
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.BuildBatchTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
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

### testSuiteName
- **Type**: typing.Optional[str]


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


# UpdateFleetInputTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### baseCapacity
- **Type**: typing.Optional[int]

### environmentType
- **Type**: typing.Optional[typing.Literal['ARM_CONTAINER', 'ARM_EC2', 'ARM_LAMBDA_CONTAINER', 'LINUX_CONTAINER', 'LINUX_EC2', 'LINUX_GPU_CONTAINER', 'LINUX_LAMBDA_CONTAINER', 'MAC_ARM', 'WINDOWS_CONTAINER', 'WINDOWS_EC2', 'WINDOWS_SERVER_2019_CONTAINER']]

### computeType
- **Type**: typing.Optional[typing.Literal['ATTRIBUTE_BASED_COMPUTE', 'BUILD_GENERAL1_2XLARGE', 'BUILD_GENERAL1_LARGE', 'BUILD_GENERAL1_MEDIUM', 'BUILD_GENERAL1_SMALL', 'BUILD_GENERAL1_XLARGE', 'BUILD_LAMBDA_10GB', 'BUILD_LAMBDA_1GB', 'BUILD_LAMBDA_2GB', 'BUILD_LAMBDA_4GB', 'BUILD_LAMBDA_8GB']]

### computeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ComputeConfigurationTypeDef]

### scalingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ScalingConfigurationInputTypeDef]

### overflowBehavior
- **Type**: typing.Optional[typing.Literal['ON_DEMAND', 'QUEUE']]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.VpcConfigUnionTypeDef]

### proxyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProxyConfigurationUnionTypeDef]

### imageId
- **Type**: typing.Optional[str]

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


# UpdateProjectInputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectCacheUnionTypeDef]

### environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectEnvironmentUnionTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.VpcConfigUnionTypeDef]

### badgeEnabled
- **Type**: typing.Optional[bool]

### logsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.LogsConfigTypeDef]

### fileSystemLocations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codebuild_classes.ProjectFileSystemLocationTypeDef]]

### buildBatchConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ProjectBuildBatchConfigUnionTypeDef]

### concurrentBuildLimit
- **Type**: typing.Optional[int]

### autoRetryLimit
- **Type**: typing.Optional[int]


# UpdateProjectOutputTypeDef

### project
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ProjectTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateProjectVisibilityInputTypeDef

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


# UpdateReportGroupInputTypeDef

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


# UpdateWebhookInputTypeDef

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
- **Type**: typing.Optional[typing.Literal['BUILD', 'BUILD_BATCH', 'RUNNER_BUILDKITE_BUILD']]


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


# VpcConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WebhookFilterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: typing.Optional[typing.Literal['BUILD', 'BUILD_BATCH', 'RUNNER_BUILDKITE_BUILD']]

### manualCreation
- **Type**: typing.Optional[bool]

### lastModifiedSecret
- **Type**: typing.Optional[datetime.datetime]

### scopeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild_classes.ScopeConfigurationTypeDef]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETING']]

### statusMessage
- **Type**: typing.Optional[str]


