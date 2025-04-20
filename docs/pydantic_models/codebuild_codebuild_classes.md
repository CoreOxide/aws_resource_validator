# Codebuild Codebuild Classes

# AutoRetryConfig

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

# BatchDeleteBuildsInput

### ids
- **Type**: typing.List[str]
- **Required**: Yes


# BatchDeleteBuildsOutput

### buildsDeleted
- **Type**: typing.List[str]
- **Required**: Yes

### buildsNotDeleted
- **Type**: typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.BuildNotDeleted]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetBuildBatchesInput

### ids
- **Type**: typing.List[str]
- **Required**: Yes


# BatchGetBuildBatchesOutput

### buildBatches
- **Type**: typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.BuildBatch]
- **Required**: Yes

### buildBatchesNotFound
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetBuildsInput

### ids
- **Type**: typing.List[str]
- **Required**: Yes


# BatchGetBuildsOutput

### builds
- **Type**: typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.Build]
- **Required**: Yes

### buildsNotFound
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetFleetsInput

### names
- **Type**: typing.List[str]
- **Required**: Yes


# BatchGetFleetsOutput

### fleets
- **Type**: typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.Fleet]
- **Required**: Yes

### fleetsNotFound
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetProjectsInput

### names
- **Type**: typing.List[str]
- **Required**: Yes


# BatchGetProjectsOutput

### projects
- **Type**: typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.Project]
- **Required**: Yes

### projectsNotFound
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetReportGroupsInput

### reportGroupArns
- **Type**: typing.List[str]
- **Required**: Yes


# BatchGetReportGroupsOutput

### reportGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ReportGroup]
- **Required**: Yes

### reportGroupsNotFound
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetReportsInput

### reportArns
- **Type**: typing.List[str]
- **Required**: Yes


# BatchGetReportsOutput

### reports
- **Type**: typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.Report]
- **Required**: Yes

### reportsNotFound
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes


# BatchRestrictions

### maximumBuildsAllowed
- **Type**: typing.Optional[int]

### computeTypesAllowed
- **Type**: typing.Optional[typing.List[str]]

### fleetsAllowed
- **Type**: typing.Optional[typing.List[str]]


# BatchRestrictionsOutput

### maximumBuildsAllowed
- **Type**: typing.Optional[int]

### computeTypesAllowed
- **Type**: typing.Optional[typing.List[str]]

### fleetsAllowed
- **Type**: typing.Optional[typing.List[str]]


# Build

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.BuildPhase]]

### source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectSource]

### secondarySources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectSource]]

### secondarySourceVersions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectSourceVersion]]

### artifacts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.BuildArtifacts]

### secondaryArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.BuildArtifacts]]

### cache
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectCacheOutput]

### environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectEnvironmentOutput]

### serviceRole
- **Type**: typing.Optional[str]

### logs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.LogsLocation]

### timeoutInMinutes
- **Type**: typing.Optional[int]

### queuedTimeoutInMinutes
- **Type**: typing.Optional[int]

### buildComplete
- **Type**: typing.Optional[bool]

### initiator
- **Type**: typing.Optional[str]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.VpcConfigOutput]

### networkInterface
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.NetworkInterface]

### encryptionKey
- **Type**: typing.Optional[str]

### exportedEnvironmentVariables
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ExportedEnvironmentVariable]]

### reportArns
- **Type**: typing.Optional[typing.List[str]]

### fileSystemLocations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectFileSystemLocation]]

### debugSession
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.DebugSession]

### buildBatchArn
- **Type**: typing.Optional[str]

### autoRetryConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.AutoRetryConfig]


# BuildArtifacts

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


# BuildBatch

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.BuildBatchPhase]]

### source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectSource]

### secondarySources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectSource]]

### secondarySourceVersions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectSourceVersion]]

### artifacts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.BuildArtifacts]

### secondaryArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.BuildArtifacts]]

### cache
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectCacheOutput]

### environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectEnvironmentOutput]

### serviceRole
- **Type**: typing.Optional[str]

### logConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.LogsConfig]

### buildTimeoutInMinutes
- **Type**: typing.Optional[int]

### queuedTimeoutInMinutes
- **Type**: typing.Optional[int]

### complete
- **Type**: typing.Optional[bool]

### initiator
- **Type**: typing.Optional[str]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.VpcConfigOutput]

### encryptionKey
- **Type**: typing.Optional[str]

### buildBatchNumber
- **Type**: typing.Optional[int]

### fileSystemLocations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectFileSystemLocation]]

### buildBatchConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectBuildBatchConfigOutput]

### buildGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.BuildGroup]]

### debugSessionEnabled
- **Type**: typing.Optional[bool]

### reportArns
- **Type**: typing.Optional[typing.List[str]]


# BuildBatchFilter

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'FAULT', 'IN_PROGRESS', 'STOPPED', 'SUCCEEDED', 'TIMED_OUT']]


# BuildBatchPhase

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.PhaseContext]]


# BuildGroup

### identifier
- **Type**: typing.Optional[str]

### dependsOn
- **Type**: typing.Optional[typing.List[str]]

### ignoreFailure
- **Type**: typing.Optional[bool]

### currentBuildSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.BuildSummary]

### priorBuildSummaryList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.BuildSummary]]


# BuildNotDeleted

### id
- **Type**: typing.Optional[str]

### statusCode
- **Type**: typing.Optional[str]


# BuildPhase

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.PhaseContext]]


# BuildStatusConfig

### context
- **Type**: typing.Optional[str]

### targetUrl
- **Type**: typing.Optional[str]


# BuildSummary

### arn
- **Type**: typing.Optional[str]

### requestedOn
- **Type**: typing.Optional[datetime.datetime]

### buildStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'FAULT', 'IN_PROGRESS', 'STOPPED', 'SUCCEEDED', 'TIMED_OUT']]

### primaryArtifact
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResolvedArtifact]

### secondaryArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResolvedArtifact]]


# CloudWatchLogsConfig

### status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### groupName
- **Type**: typing.Optional[str]

### streamName
- **Type**: typing.Optional[str]


# CodeCoverage

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


# CodeCoverageReportSummary

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


# ComputeConfiguration

### vCpu
- **Type**: typing.Optional[int]

### memory
- **Type**: typing.Optional[int]

### disk
- **Type**: typing.Optional[int]

### machineType
- **Type**: typing.Optional[typing.Literal['GENERAL', 'NVME']]


# CreateFleetInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ComputeConfiguration]

### scalingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ScalingConfigurationInput]

### overflowBehavior
- **Type**: typing.Optional[typing.Literal['ON_DEMAND', 'QUEUE']]

### vpcConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.VpcConfig, aws_resource_validator.pydantic_models.codebuild.codebuild_classes.VpcConfigOutput, NoneType]

### proxyConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProxyConfiguration, aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProxyConfigurationOutput, NoneType]

### imageId
- **Type**: typing.Optional[str]

### fleetServiceRole
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.Tag]]


# CreateFleetOutput

### fleet
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.Fleet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProjectInput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectSource'>
- **Required**: Yes

### artifacts
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectArtifacts'>
- **Required**: Yes

### environment
- **Type**: typing.Union[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectEnvironment, aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectEnvironmentOutput]
- **Required**: Yes

### serviceRole
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### secondarySources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectSource]]

### sourceVersion
- **Type**: typing.Optional[str]

### secondarySourceVersions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectSourceVersion]]

### secondaryArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectArtifacts]]

### cache
- **Type**: typing.Union[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectCache, aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectCacheOutput, NoneType]

### timeoutInMinutes
- **Type**: typing.Optional[int]

### queuedTimeoutInMinutes
- **Type**: typing.Optional[int]

### encryptionKey
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.Tag]]

### vpcConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.VpcConfig, aws_resource_validator.pydantic_models.codebuild.codebuild_classes.VpcConfigOutput, NoneType]

### badgeEnabled
- **Type**: typing.Optional[bool]

### logsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.LogsConfig]

### fileSystemLocations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectFileSystemLocation]]

### buildBatchConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectBuildBatchConfig, aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectBuildBatchConfigOutput, NoneType]

### concurrentBuildLimit
- **Type**: typing.Optional[int]

### autoRetryLimit
- **Type**: typing.Optional[int]


# CreateProjectOutput

### project
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.Project'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes


# CreateReportGroupInput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['CODE_COVERAGE', 'TEST']
- **Required**: Yes

### exportConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ReportExportConfig'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.Tag]]


# CreateReportGroupOutput

### reportGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ReportGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWebhookInput

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### branchFilter
- **Type**: typing.Optional[str]

### filterGroups
- **Type**: typing.Optional[typing.List[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.WebhookFilter]]]

### buildType
- **Type**: typing.Optional[typing.Literal['BUILD', 'BUILD_BATCH', 'RUNNER_BUILDKITE_BUILD']]

### manualCreation
- **Type**: typing.Optional[bool]

### scopeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ScopeConfiguration]


# CreateWebhookOutput

### webhook
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.Webhook'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes


# DebugSession

### sessionEnabled
- **Type**: typing.Optional[bool]

### sessionTarget
- **Type**: typing.Optional[str]


# DeleteBuildBatchInput

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBuildBatchOutput

### statusCode
- **Type**: <class 'str'>
- **Required**: Yes

### buildsDeleted
- **Type**: typing.List[str]
- **Required**: Yes

### buildsNotDeleted
- **Type**: typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.BuildNotDeleted]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteFleetInput

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProjectInput

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReportGroupInput

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### deleteReports
- **Type**: typing.Optional[bool]


# DeleteReportInput

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourcePolicyInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSourceCredentialsInput

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSourceCredentialsOutput

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteWebhookInput

### projectName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCodeCoveragesInput

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


# DescribeCodeCoveragesInputPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.PaginatorConfig]


# DescribeCodeCoveragesOutput

### codeCoverages
- **Type**: typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.CodeCoverage]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeTestCasesInput

### reportArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.TestCaseFilter]


# DescribeTestCasesInputPaginate

### reportArn
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.TestCaseFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.PaginatorConfig]


# DescribeTestCasesOutput

### testCases
- **Type**: typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.TestCase]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# EnvironmentImage

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### versions
- **Type**: typing.Optional[typing.List[str]]


# EnvironmentLanguage

### language
- **Type**: typing.Optional[typing.Literal['ANDROID', 'BASE', 'DOCKER', 'DOTNET', 'GOLANG', 'JAVA', 'NODE_JS', 'PHP', 'PYTHON', 'RUBY']]

### images
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.EnvironmentImage]]


# EnvironmentPlatform

### platform
- **Type**: typing.Optional[typing.Literal['AMAZON_LINUX', 'DEBIAN', 'UBUNTU', 'WINDOWS_SERVER']]

### languages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.EnvironmentLanguage]]


# EnvironmentVariable

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['PARAMETER_STORE', 'PLAINTEXT', 'SECRETS_MANAGER']]


# ExportedEnvironmentVariable

### name
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# Fleet

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.FleetStatus]

### baseCapacity
- **Type**: typing.Optional[int]

### environmentType
- **Type**: typing.Optional[typing.Literal['ARM_CONTAINER', 'ARM_EC2', 'ARM_LAMBDA_CONTAINER', 'LINUX_CONTAINER', 'LINUX_EC2', 'LINUX_GPU_CONTAINER', 'LINUX_LAMBDA_CONTAINER', 'MAC_ARM', 'WINDOWS_CONTAINER', 'WINDOWS_EC2', 'WINDOWS_SERVER_2019_CONTAINER']]

### computeType
- **Type**: typing.Optional[typing.Literal['ATTRIBUTE_BASED_COMPUTE', 'BUILD_GENERAL1_2XLARGE', 'BUILD_GENERAL1_LARGE', 'BUILD_GENERAL1_MEDIUM', 'BUILD_GENERAL1_SMALL', 'BUILD_GENERAL1_XLARGE', 'BUILD_LAMBDA_10GB', 'BUILD_LAMBDA_1GB', 'BUILD_LAMBDA_2GB', 'BUILD_LAMBDA_4GB', 'BUILD_LAMBDA_8GB']]

### computeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ComputeConfiguration]

### scalingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ScalingConfigurationOutput]

### overflowBehavior
- **Type**: typing.Optional[typing.Literal['ON_DEMAND', 'QUEUE']]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.VpcConfigOutput]

### proxyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProxyConfigurationOutput]

### imageId
- **Type**: typing.Optional[str]

### fleetServiceRole
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.Tag]]


# FleetProxyRule

### type
- **Type**: typing.Literal['DOMAIN', 'IP']
- **Required**: Yes

### effect
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### entities
- **Type**: typing.List[str]
- **Required**: Yes


# FleetProxyRuleOutput

### type
- **Type**: typing.Literal['DOMAIN', 'IP']
- **Required**: Yes

### effect
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### entities
- **Type**: typing.List[str]
- **Required**: Yes


# FleetStatus

### statusCode
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETING', 'PENDING_DELETION', 'ROTATING', 'UPDATE_ROLLBACK_FAILED', 'UPDATING']]

### context
- **Type**: typing.Optional[typing.Literal['ACTION_REQUIRED', 'CREATE_FAILED', 'INSUFFICIENT_CAPACITY', 'PENDING_DELETION', 'UPDATE_FAILED']]

### message
- **Type**: typing.Optional[str]


# GetReportGroupTrendInput

### reportGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### trendField
- **Type**: typing.Literal['BRANCHES_COVERED', 'BRANCHES_MISSED', 'BRANCH_COVERAGE', 'DURATION', 'LINES_COVERED', 'LINES_MISSED', 'LINE_COVERAGE', 'PASS_RATE', 'TOTAL']
- **Required**: Yes

### numOfReports
- **Type**: typing.Optional[int]


# GetReportGroupTrendOutput

### stats
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ReportGroupTrendStats'>
- **Required**: Yes

### rawData
- **Type**: typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ReportWithRawData]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourcePolicyInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourcePolicyOutput

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes


# GitSubmodulesConfig

### fetchSubmodules
- **Type**: <class 'bool'>
- **Required**: Yes


# ImportSourceCredentialsInput

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


# ImportSourceCredentialsOutput

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes


# InvalidateProjectCacheInput

### projectName
- **Type**: <class 'str'>
- **Required**: Yes


# ListBuildBatchesForProjectInput

### projectName
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.BuildBatchFilter]

### maxResults
- **Type**: typing.Optional[int]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### nextToken
- **Type**: typing.Optional[str]


# ListBuildBatchesForProjectInputPaginate

### projectName
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.BuildBatchFilter]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.PaginatorConfig]


# ListBuildBatchesForProjectOutput

### ids
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBuildBatchesInput

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.BuildBatchFilter]

### maxResults
- **Type**: typing.Optional[int]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### nextToken
- **Type**: typing.Optional[str]


# ListBuildBatchesInputPaginate

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.BuildBatchFilter]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.PaginatorConfig]


# ListBuildBatchesOutput

### ids
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBuildsForProjectInput

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### nextToken
- **Type**: typing.Optional[str]


# ListBuildsForProjectInputPaginate

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.PaginatorConfig]


# ListBuildsForProjectOutput

### ids
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBuildsInput

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### nextToken
- **Type**: typing.Optional[str]


# ListBuildsInputPaginate

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.PaginatorConfig]


# ListBuildsOutput

### ids
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCuratedEnvironmentImagesOutput

### platforms
- **Type**: typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.EnvironmentPlatform]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes


# ListFleetsInput

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### sortBy
- **Type**: typing.Optional[typing.Literal['CREATED_TIME', 'LAST_MODIFIED_TIME', 'NAME']]


# ListFleetsOutput

### fleets
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProjectsInput

### sortBy
- **Type**: typing.Optional[typing.Literal['CREATED_TIME', 'LAST_MODIFIED_TIME', 'NAME']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### nextToken
- **Type**: typing.Optional[str]


# ListProjectsInputPaginate

### sortBy
- **Type**: typing.Optional[typing.Literal['CREATED_TIME', 'LAST_MODIFIED_TIME', 'NAME']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.PaginatorConfig]


# ListProjectsOutput

### projects
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReportGroupsInput

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### sortBy
- **Type**: typing.Optional[typing.Literal['CREATED_TIME', 'LAST_MODIFIED_TIME', 'NAME']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListReportGroupsInputPaginate

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### sortBy
- **Type**: typing.Optional[typing.Literal['CREATED_TIME', 'LAST_MODIFIED_TIME', 'NAME']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.PaginatorConfig]


# ListReportGroupsOutput

### reportGroups
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReportsForReportGroupInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ReportFilter]


# ListReportsForReportGroupInputPaginate

### reportGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ReportFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.PaginatorConfig]


# ListReportsForReportGroupOutput

### reports
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReportsInput

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ReportFilter]


# ListReportsInputPaginate

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ReportFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.PaginatorConfig]


# ListReportsOutput

### reports
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSharedProjectsInput

### sortBy
- **Type**: typing.Optional[typing.Literal['ARN', 'MODIFIED_TIME']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSharedProjectsInputPaginate

### sortBy
- **Type**: typing.Optional[typing.Literal['ARN', 'MODIFIED_TIME']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.PaginatorConfig]


# ListSharedProjectsOutput

### projects
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSharedReportGroupsInput

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### sortBy
- **Type**: typing.Optional[typing.Literal['ARN', 'MODIFIED_TIME']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListSharedReportGroupsInputPaginate

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### sortBy
- **Type**: typing.Optional[typing.Literal['ARN', 'MODIFIED_TIME']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.PaginatorConfig]


# ListSharedReportGroupsOutput

### reportGroups
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSourceCredentialsOutput

### sourceCredentialsInfos
- **Type**: typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.SourceCredentialsInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes


# LogsConfig

### cloudWatchLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.CloudWatchLogsConfig]

### s3Logs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.S3LogsConfig]


# LogsLocation

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.CloudWatchLogsConfig]

### s3Logs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.S3LogsConfig]


# NetworkInterface

### subnetId
- **Type**: typing.Optional[str]

### networkInterfaceId
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PhaseContext

### statusCode
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]


# Project

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectSource]

### secondarySources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectSource]]

### sourceVersion
- **Type**: typing.Optional[str]

### secondarySourceVersions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectSourceVersion]]

### artifacts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectArtifacts]

### secondaryArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectArtifacts]]

### cache
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectCacheOutput]

### environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectEnvironmentOutput]

### serviceRole
- **Type**: typing.Optional[str]

### timeoutInMinutes
- **Type**: typing.Optional[int]

### queuedTimeoutInMinutes
- **Type**: typing.Optional[int]

### encryptionKey
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.Tag]]

### created
- **Type**: typing.Optional[datetime.datetime]

### lastModified
- **Type**: typing.Optional[datetime.datetime]

### webhook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.Webhook]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.VpcConfigOutput]

### badge
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectBadge]

### logsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.LogsConfig]

### fileSystemLocations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectFileSystemLocation]]

### buildBatchConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectBuildBatchConfigOutput]

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


# ProjectArtifacts

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


# ProjectBadge

### badgeEnabled
- **Type**: typing.Optional[bool]

### badgeRequestUrl
- **Type**: typing.Optional[str]


# ProjectBuildBatchConfig

### serviceRole
- **Type**: typing.Optional[str]

### combineArtifacts
- **Type**: typing.Optional[bool]

### restrictions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.BatchRestrictions]

### timeoutInMins
- **Type**: typing.Optional[int]

### batchReportMode
- **Type**: typing.Optional[typing.Literal['REPORT_AGGREGATED_BATCH', 'REPORT_INDIVIDUAL_BUILDS']]


# ProjectBuildBatchConfigOutput

### serviceRole
- **Type**: typing.Optional[str]

### combineArtifacts
- **Type**: typing.Optional[bool]

### restrictions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.BatchRestrictionsOutput]

### timeoutInMins
- **Type**: typing.Optional[int]

### batchReportMode
- **Type**: typing.Optional[typing.Literal['REPORT_AGGREGATED_BATCH', 'REPORT_INDIVIDUAL_BUILDS']]


# ProjectCache

### type
- **Type**: typing.Literal['LOCAL', 'NO_CACHE', 'S3']
- **Required**: Yes

### location
- **Type**: typing.Optional[str]

### modes
- **Type**: typing.Optional[typing.List[typing.Literal['LOCAL_CUSTOM_CACHE', 'LOCAL_DOCKER_LAYER_CACHE', 'LOCAL_SOURCE_CACHE']]]


# ProjectCacheOutput

### type
- **Type**: typing.Literal['LOCAL', 'NO_CACHE', 'S3']
- **Required**: Yes

### location
- **Type**: typing.Optional[str]

### modes
- **Type**: typing.Optional[typing.List[typing.Literal['LOCAL_CUSTOM_CACHE', 'LOCAL_DOCKER_LAYER_CACHE', 'LOCAL_SOURCE_CACHE']]]


# ProjectEnvironment

### type
- **Type**: typing.Literal['ARM_CONTAINER', 'ARM_EC2', 'ARM_LAMBDA_CONTAINER', 'LINUX_CONTAINER', 'LINUX_EC2', 'LINUX_GPU_CONTAINER', 'LINUX_LAMBDA_CONTAINER', 'MAC_ARM', 'WINDOWS_CONTAINER', 'WINDOWS_EC2', 'WINDOWS_SERVER_2019_CONTAINER']
- **Required**: Yes

### image
- **Type**: <class 'str'>
- **Required**: Yes

### computeType
- **Type**: typing.Literal['ATTRIBUTE_BASED_COMPUTE', 'BUILD_GENERAL1_2XLARGE', 'BUILD_GENERAL1_LARGE', 'BUILD_GENERAL1_MEDIUM', 'BUILD_GENERAL1_SMALL', 'BUILD_GENERAL1_XLARGE', 'BUILD_LAMBDA_10GB', 'BUILD_LAMBDA_1GB', 'BUILD_LAMBDA_2GB', 'BUILD_LAMBDA_4GB', 'BUILD_LAMBDA_8GB']
- **Required**: Yes

### computeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ComputeConfiguration]

### fleet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectFleet]

### environmentVariables
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.EnvironmentVariable]]

### privilegedMode
- **Type**: typing.Optional[bool]

### certificate
- **Type**: typing.Optional[str]

### registryCredential
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.RegistryCredential]

### imagePullCredentialsType
- **Type**: typing.Optional[typing.Literal['CODEBUILD', 'SERVICE_ROLE']]


# ProjectEnvironmentOutput

### type
- **Type**: typing.Literal['ARM_CONTAINER', 'ARM_EC2', 'ARM_LAMBDA_CONTAINER', 'LINUX_CONTAINER', 'LINUX_EC2', 'LINUX_GPU_CONTAINER', 'LINUX_LAMBDA_CONTAINER', 'MAC_ARM', 'WINDOWS_CONTAINER', 'WINDOWS_EC2', 'WINDOWS_SERVER_2019_CONTAINER']
- **Required**: Yes

### image
- **Type**: <class 'str'>
- **Required**: Yes

### computeType
- **Type**: typing.Literal['ATTRIBUTE_BASED_COMPUTE', 'BUILD_GENERAL1_2XLARGE', 'BUILD_GENERAL1_LARGE', 'BUILD_GENERAL1_MEDIUM', 'BUILD_GENERAL1_SMALL', 'BUILD_GENERAL1_XLARGE', 'BUILD_LAMBDA_10GB', 'BUILD_LAMBDA_1GB', 'BUILD_LAMBDA_2GB', 'BUILD_LAMBDA_4GB', 'BUILD_LAMBDA_8GB']
- **Required**: Yes

### computeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ComputeConfiguration]

### fleet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectFleet]

### environmentVariables
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.EnvironmentVariable]]

### privilegedMode
- **Type**: typing.Optional[bool]

### certificate
- **Type**: typing.Optional[str]

### registryCredential
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.RegistryCredential]

### imagePullCredentialsType
- **Type**: typing.Optional[typing.Literal['CODEBUILD', 'SERVICE_ROLE']]


# ProjectFileSystemLocation

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


# ProjectFleet

### fleetArn
- **Type**: typing.Optional[str]


# ProjectSource

### type
- **Type**: typing.Literal['BITBUCKET', 'CODECOMMIT', 'CODEPIPELINE', 'GITHUB', 'GITHUB_ENTERPRISE', 'GITLAB', 'GITLAB_SELF_MANAGED', 'NO_SOURCE', 'S3']
- **Required**: Yes

### location
- **Type**: typing.Optional[str]

### gitCloneDepth
- **Type**: typing.Optional[int]

### gitSubmodulesConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.GitSubmodulesConfig]

### buildspec
- **Type**: typing.Optional[str]

### auth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.SourceAuth]

### reportBuildStatus
- **Type**: typing.Optional[bool]

### buildStatusConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.BuildStatusConfig]

### insecureSsl
- **Type**: typing.Optional[bool]

### sourceIdentifier
- **Type**: typing.Optional[str]


# ProjectSourceVersion

### sourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### sourceVersion
- **Type**: <class 'str'>
- **Required**: Yes


# ProxyConfiguration

### defaultBehavior
- **Type**: typing.Optional[typing.Literal['ALLOW_ALL', 'DENY_ALL']]

### orderedProxyRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.FleetProxyRule]]


# ProxyConfigurationOutput

### defaultBehavior
- **Type**: typing.Optional[typing.Literal['ALLOW_ALL', 'DENY_ALL']]

### orderedProxyRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.FleetProxyRuleOutput]]


# PutResourcePolicyInput

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# PutResourcePolicyOutput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes


# RegistryCredential

### credential
- **Type**: <class 'str'>
- **Required**: Yes

### credentialProvider
- **Type**: typing.Literal['SECRETS_MANAGER']
- **Required**: Yes


# Report

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ReportExportConfig]

### truncated
- **Type**: typing.Optional[bool]

### testSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.TestReportSummary]

### codeCoverageSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.CodeCoverageReportSummary]


# ReportExportConfig

### exportConfigType
- **Type**: typing.Optional[typing.Literal['NO_EXPORT', 'S3']]

### s3Destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.S3ReportExportConfig]


# ReportFilter

### status
- **Type**: typing.Optional[typing.Literal['DELETING', 'FAILED', 'GENERATING', 'INCOMPLETE', 'SUCCEEDED']]


# ReportGroup

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['CODE_COVERAGE', 'TEST']]

### exportConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ReportExportConfig]

### created
- **Type**: typing.Optional[datetime.datetime]

### lastModified
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.Tag]]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING']]


# ReportGroupTrendStats

### average
- **Type**: typing.Optional[str]

### max
- **Type**: typing.Optional[str]

### min
- **Type**: typing.Optional[str]


# ReportWithRawData

### reportArn
- **Type**: typing.Optional[str]

### data
- **Type**: typing.Optional[str]


# ResolvedArtifact

### type
- **Type**: typing.Optional[typing.Literal['CODEPIPELINE', 'NO_ARTIFACTS', 'S3']]

### location
- **Type**: typing.Optional[str]

### identifier
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


# RetryBuildBatchInput

### id
- **Type**: typing.Optional[str]

### idempotencyToken
- **Type**: typing.Optional[str]

### retryType
- **Type**: typing.Optional[typing.Literal['RETRY_ALL_BUILDS', 'RETRY_FAILED_BUILDS']]


# RetryBuildBatchOutput

### buildBatch
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.BuildBatch'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes


# RetryBuildInput

### id
- **Type**: typing.Optional[str]

### idempotencyToken
- **Type**: typing.Optional[str]


# RetryBuildOutput

### build
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.Build'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes


# S3LogsConfig

### status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### location
- **Type**: typing.Optional[str]

### encryptionDisabled
- **Type**: typing.Optional[bool]

### bucketOwnerAccess
- **Type**: typing.Optional[typing.Literal['FULL', 'NONE', 'READ_ONLY']]


# S3ReportExportConfig

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


# ScalingConfigurationInput

### scalingType
- **Type**: typing.Optional[typing.Literal['TARGET_TRACKING_SCALING']]

### targetTrackingScalingConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.TargetTrackingScalingConfiguration]]

### maxCapacity
- **Type**: typing.Optional[int]


# ScalingConfigurationOutput

### scalingType
- **Type**: typing.Optional[typing.Literal['TARGET_TRACKING_SCALING']]

### targetTrackingScalingConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.TargetTrackingScalingConfiguration]]

### maxCapacity
- **Type**: typing.Optional[int]

### desiredCapacity
- **Type**: typing.Optional[int]


# ScopeConfiguration

### name
- **Type**: <class 'str'>
- **Required**: Yes

### scope
- **Type**: typing.Literal['GITHUB_GLOBAL', 'GITHUB_ORGANIZATION', 'GITLAB_GROUP']
- **Required**: Yes

### domain
- **Type**: typing.Optional[str]


# SourceAuth

### type
- **Type**: typing.Literal['CODECONNECTIONS', 'OAUTH', 'SECRETS_MANAGER']
- **Required**: Yes

### resource
- **Type**: typing.Optional[str]


# SourceCredentialsInfo

### arn
- **Type**: typing.Optional[str]

### serverType
- **Type**: typing.Optional[typing.Literal['BITBUCKET', 'GITHUB', 'GITHUB_ENTERPRISE', 'GITLAB', 'GITLAB_SELF_MANAGED']]

### authType
- **Type**: typing.Optional[typing.Literal['BASIC_AUTH', 'CODECONNECTIONS', 'OAUTH', 'PERSONAL_ACCESS_TOKEN', 'SECRETS_MANAGER']]

### resource
- **Type**: typing.Optional[str]


# StartBuildBatchInput

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### secondarySourcesOverride
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectSource]]

### secondarySourcesVersionOverride
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectSourceVersion]]

### sourceVersion
- **Type**: typing.Optional[str]

### artifactsOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectArtifacts]

### secondaryArtifactsOverride
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectArtifacts]]

### environmentVariablesOverride
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.EnvironmentVariable]]

### sourceTypeOverride
- **Type**: typing.Optional[typing.Literal['BITBUCKET', 'CODECOMMIT', 'CODEPIPELINE', 'GITHUB', 'GITHUB_ENTERPRISE', 'GITLAB', 'GITLAB_SELF_MANAGED', 'NO_SOURCE', 'S3']]

### sourceLocationOverride
- **Type**: typing.Optional[str]

### sourceAuthOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.SourceAuth]

### gitCloneDepthOverride
- **Type**: typing.Optional[int]

### gitSubmodulesConfigOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.GitSubmodulesConfig]

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectCache, aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectCacheOutput, NoneType]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.LogsConfig]

### registryCredentialOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.RegistryCredential]

### imagePullCredentialsTypeOverride
- **Type**: typing.Optional[typing.Literal['CODEBUILD', 'SERVICE_ROLE']]

### buildBatchConfigOverride
- **Type**: typing.Union[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectBuildBatchConfig, aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectBuildBatchConfigOutput, NoneType]

### debugSessionEnabled
- **Type**: typing.Optional[bool]


# StartBuildBatchOutput

### buildBatch
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.BuildBatch'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes


# StartBuildInput

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### secondarySourcesOverride
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectSource]]

### secondarySourcesVersionOverride
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectSourceVersion]]

### sourceVersion
- **Type**: typing.Optional[str]

### artifactsOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectArtifacts]

### secondaryArtifactsOverride
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectArtifacts]]

### environmentVariablesOverride
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.EnvironmentVariable]]

### sourceTypeOverride
- **Type**: typing.Optional[typing.Literal['BITBUCKET', 'CODECOMMIT', 'CODEPIPELINE', 'GITHUB', 'GITHUB_ENTERPRISE', 'GITLAB', 'GITLAB_SELF_MANAGED', 'NO_SOURCE', 'S3']]

### sourceLocationOverride
- **Type**: typing.Optional[str]

### sourceAuthOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.SourceAuth]

### gitCloneDepthOverride
- **Type**: typing.Optional[int]

### gitSubmodulesConfigOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.GitSubmodulesConfig]

### buildspecOverride
- **Type**: typing.Optional[str]

### insecureSslOverride
- **Type**: typing.Optional[bool]

### reportBuildStatusOverride
- **Type**: typing.Optional[bool]

### buildStatusConfigOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.BuildStatusConfig]

### environmentTypeOverride
- **Type**: typing.Optional[typing.Literal['ARM_CONTAINER', 'ARM_EC2', 'ARM_LAMBDA_CONTAINER', 'LINUX_CONTAINER', 'LINUX_EC2', 'LINUX_GPU_CONTAINER', 'LINUX_LAMBDA_CONTAINER', 'MAC_ARM', 'WINDOWS_CONTAINER', 'WINDOWS_EC2', 'WINDOWS_SERVER_2019_CONTAINER']]

### imageOverride
- **Type**: typing.Optional[str]

### computeTypeOverride
- **Type**: typing.Optional[typing.Literal['ATTRIBUTE_BASED_COMPUTE', 'BUILD_GENERAL1_2XLARGE', 'BUILD_GENERAL1_LARGE', 'BUILD_GENERAL1_MEDIUM', 'BUILD_GENERAL1_SMALL', 'BUILD_GENERAL1_XLARGE', 'BUILD_LAMBDA_10GB', 'BUILD_LAMBDA_1GB', 'BUILD_LAMBDA_2GB', 'BUILD_LAMBDA_4GB', 'BUILD_LAMBDA_8GB']]

### certificateOverride
- **Type**: typing.Optional[str]

### cacheOverride
- **Type**: typing.Union[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectCache, aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectCacheOutput, NoneType]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.LogsConfig]

### registryCredentialOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.RegistryCredential]

### imagePullCredentialsTypeOverride
- **Type**: typing.Optional[typing.Literal['CODEBUILD', 'SERVICE_ROLE']]

### debugSessionEnabled
- **Type**: typing.Optional[bool]

### fleetOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectFleet]

### autoRetryLimitOverride
- **Type**: typing.Optional[int]


# StartBuildOutput

### build
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.Build'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes


# StopBuildBatchInput

### id
- **Type**: <class 'str'>
- **Required**: Yes


# StopBuildBatchOutput

### buildBatch
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.BuildBatch'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes


# StopBuildInput

### id
- **Type**: <class 'str'>
- **Required**: Yes


# StopBuildOutput

### build
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.Build'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# TargetTrackingScalingConfiguration

### metricType
- **Type**: typing.Optional[typing.Literal['FLEET_UTILIZATION_RATE']]

### targetValue
- **Type**: typing.Optional[float]


# TestCase

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


# TestCaseFilter

### status
- **Type**: typing.Optional[str]

### keyword
- **Type**: typing.Optional[str]


# TestReportSummary

### total
- **Type**: <class 'int'>
- **Required**: Yes

### statusCounts
- **Type**: typing.Dict[str, int]
- **Required**: Yes

### durationInNanoSeconds
- **Type**: <class 'int'>
- **Required**: Yes


# UpdateFleetInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ComputeConfiguration]

### scalingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ScalingConfigurationInput]

### overflowBehavior
- **Type**: typing.Optional[typing.Literal['ON_DEMAND', 'QUEUE']]

### vpcConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.VpcConfig, aws_resource_validator.pydantic_models.codebuild.codebuild_classes.VpcConfigOutput, NoneType]

### proxyConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProxyConfiguration, aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProxyConfigurationOutput, NoneType]

### imageId
- **Type**: typing.Optional[str]

### fleetServiceRole
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.Tag]]


# UpdateFleetOutput

### fleet
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.Fleet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateProjectInput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectSource]

### secondarySources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectSource]]

### sourceVersion
- **Type**: typing.Optional[str]

### secondarySourceVersions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectSourceVersion]]

### artifacts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectArtifacts]

### secondaryArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectArtifacts]]

### cache
- **Type**: typing.Union[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectCache, aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectCacheOutput, NoneType]

### environment
- **Type**: typing.Union[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectEnvironment, aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectEnvironmentOutput, NoneType]

### serviceRole
- **Type**: typing.Optional[str]

### timeoutInMinutes
- **Type**: typing.Optional[int]

### queuedTimeoutInMinutes
- **Type**: typing.Optional[int]

### encryptionKey
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.Tag]]

### vpcConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.VpcConfig, aws_resource_validator.pydantic_models.codebuild.codebuild_classes.VpcConfigOutput, NoneType]

### badgeEnabled
- **Type**: typing.Optional[bool]

### logsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.LogsConfig]

### fileSystemLocations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectFileSystemLocation]]

### buildBatchConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectBuildBatchConfig, aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ProjectBuildBatchConfigOutput, NoneType]

### concurrentBuildLimit
- **Type**: typing.Optional[int]

### autoRetryLimit
- **Type**: typing.Optional[int]


# UpdateProjectOutput

### project
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.Project'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateProjectVisibilityInput

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes

### projectVisibility
- **Type**: typing.Literal['PRIVATE', 'PUBLIC_READ']
- **Required**: Yes

### resourceAccessRole
- **Type**: typing.Optional[str]


# UpdateProjectVisibilityOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateReportGroupInput

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### exportConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ReportExportConfig]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.Tag]]


# UpdateReportGroupOutput

### reportGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ReportGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateWebhookInput

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### branchFilter
- **Type**: typing.Optional[str]

### rotateSecret
- **Type**: typing.Optional[bool]

### filterGroups
- **Type**: typing.Optional[typing.List[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.WebhookFilter]]]

### buildType
- **Type**: typing.Optional[typing.Literal['BUILD', 'BUILD_BATCH', 'RUNNER_BUILDKITE_BUILD']]


# UpdateWebhookOutput

### webhook
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.Webhook'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ResponseMetadata'>
- **Required**: Yes


# VpcConfig

### vpcId
- **Type**: typing.Optional[str]

### subnets
- **Type**: typing.Optional[typing.List[str]]

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# VpcConfigOutput

### vpcId
- **Type**: typing.Optional[str]

### subnets
- **Type**: typing.Optional[typing.List[str]]

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# Webhook

### url
- **Type**: typing.Optional[str]

### payloadUrl
- **Type**: typing.Optional[str]

### secret
- **Type**: typing.Optional[str]

### branchFilter
- **Type**: typing.Optional[str]

### filterGroups
- **Type**: typing.Optional[typing.List[typing.List[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.WebhookFilter]]]

### buildType
- **Type**: typing.Optional[typing.Literal['BUILD', 'BUILD_BATCH', 'RUNNER_BUILDKITE_BUILD']]

### manualCreation
- **Type**: typing.Optional[bool]

### lastModifiedSecret
- **Type**: typing.Optional[datetime.datetime]

### scopeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codebuild.codebuild_classes.ScopeConfiguration]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETING']]

### statusMessage
- **Type**: typing.Optional[str]


# WebhookFilter

### type
- **Type**: typing.Literal['ACTOR_ACCOUNT_ID', 'BASE_REF', 'COMMIT_MESSAGE', 'EVENT', 'FILE_PATH', 'HEAD_REF', 'RELEASE_NAME', 'REPOSITORY_NAME', 'TAG_NAME', 'WORKFLOW_NAME']
- **Required**: Yes

### pattern
- **Type**: <class 'str'>
- **Required**: Yes

### excludeMatchedPattern
- **Type**: typing.Optional[bool]


