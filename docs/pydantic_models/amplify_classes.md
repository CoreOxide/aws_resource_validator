# Amplify Classes

# App

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### platform
- **Type**: typing.Literal['WEB', 'WEB_COMPUTE', 'WEB_DYNAMIC']
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### environmentVariables
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### defaultDomain
- **Type**: <class 'str'>
- **Required**: Yes

### enableBranchAutoBuild
- **Type**: <class 'bool'>
- **Required**: Yes

### enableBasicAuth
- **Type**: <class 'bool'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### computeRoleArn
- **Type**: typing.Optional[str]

### iamServiceRoleArn
- **Type**: typing.Optional[str]

### enableBranchAutoDeletion
- **Type**: typing.Optional[bool]

### basicAuthCredentials
- **Type**: typing.Optional[str]

### customRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplify_classes.CustomRule]]

### productionBranch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.ProductionBranch]

### buildSpec
- **Type**: typing.Optional[str]

### customHeaders
- **Type**: typing.Optional[str]

### enableAutoBranchCreation
- **Type**: typing.Optional[bool]

### autoBranchCreationPatterns
- **Type**: typing.Optional[typing.List[str]]

### autoBranchCreationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.AutoBranchCreationConfigOutput]

### repositoryCloneMethod
- **Type**: typing.Optional[typing.Literal['SIGV4', 'SSH', 'TOKEN']]

### cacheConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.CacheConfig]

### webhookCreateTime
- **Type**: typing.Optional[datetime.datetime]

### wafConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.WafConfiguration]


# Artifact

### artifactFileName
- **Type**: <class 'str'>
- **Required**: Yes

### artifactId
- **Type**: <class 'str'>
- **Required**: Yes


# AutoBranchCreationConfig

### stage
- **Type**: typing.Optional[typing.Literal['BETA', 'DEVELOPMENT', 'EXPERIMENTAL', 'PRODUCTION', 'PULL_REQUEST']]

### framework
- **Type**: typing.Optional[str]

### enableAutoBuild
- **Type**: typing.Optional[bool]

### environmentVariables
- **Type**: typing.Optional[typing.Mapping[str, str]]

### basicAuthCredentials
- **Type**: typing.Optional[str]

### enableBasicAuth
- **Type**: typing.Optional[bool]

### enablePerformanceMode
- **Type**: typing.Optional[bool]

### buildSpec
- **Type**: typing.Optional[str]

### enablePullRequestPreview
- **Type**: typing.Optional[bool]

### pullRequestEnvironmentName
- **Type**: typing.Optional[str]


# AutoBranchCreationConfigOutput

### stage
- **Type**: typing.Optional[typing.Literal['BETA', 'DEVELOPMENT', 'EXPERIMENTAL', 'PRODUCTION', 'PULL_REQUEST']]

### framework
- **Type**: typing.Optional[str]

### enableAutoBuild
- **Type**: typing.Optional[bool]

### environmentVariables
- **Type**: typing.Optional[typing.Dict[str, str]]

### basicAuthCredentials
- **Type**: typing.Optional[str]

### enableBasicAuth
- **Type**: typing.Optional[bool]

### enablePerformanceMode
- **Type**: typing.Optional[bool]

### buildSpec
- **Type**: typing.Optional[str]

### enablePullRequestPreview
- **Type**: typing.Optional[bool]

### pullRequestEnvironmentName
- **Type**: typing.Optional[str]


# AutoBranchCreationConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Backend

### stackArn
- **Type**: typing.Optional[str]


# BackendEnvironment

### backendEnvironmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### stackName
- **Type**: typing.Optional[str]

### deploymentArtifacts
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Branch

### branchArn
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### stage
- **Type**: typing.Literal['BETA', 'DEVELOPMENT', 'EXPERIMENTAL', 'PRODUCTION', 'PULL_REQUEST']
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### enableNotification
- **Type**: <class 'bool'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### environmentVariables
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### enableAutoBuild
- **Type**: <class 'bool'>
- **Required**: Yes

### customDomains
- **Type**: typing.List[str]
- **Required**: Yes

### framework
- **Type**: <class 'str'>
- **Required**: Yes

### activeJobId
- **Type**: <class 'str'>
- **Required**: Yes

### totalNumberOfJobs
- **Type**: <class 'str'>
- **Required**: Yes

### enableBasicAuth
- **Type**: <class 'bool'>
- **Required**: Yes

### ttl
- **Type**: <class 'str'>
- **Required**: Yes

### enablePullRequestPreview
- **Type**: <class 'bool'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### enablePerformanceMode
- **Type**: typing.Optional[bool]

### thumbnailUrl
- **Type**: typing.Optional[str]

### basicAuthCredentials
- **Type**: typing.Optional[str]

### buildSpec
- **Type**: typing.Optional[str]

### associatedResources
- **Type**: typing.Optional[typing.List[str]]

### pullRequestEnvironmentName
- **Type**: typing.Optional[str]

### destinationBranch
- **Type**: typing.Optional[str]

### sourceBranch
- **Type**: typing.Optional[str]

### backendEnvironmentArn
- **Type**: typing.Optional[str]

### backend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.Backend]

### computeRoleArn
- **Type**: typing.Optional[str]


# CacheConfig

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Certificate

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CertificateSettings

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAppRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### repository
- **Type**: typing.Optional[str]

### platform
- **Type**: typing.Optional[typing.Literal['WEB', 'WEB_COMPUTE', 'WEB_DYNAMIC']]

### computeRoleArn
- **Type**: typing.Optional[str]

### iamServiceRoleArn
- **Type**: typing.Optional[str]

### oauthToken
- **Type**: typing.Optional[str]

### accessToken
- **Type**: typing.Optional[str]

### environmentVariables
- **Type**: typing.Optional[typing.Mapping[str, str]]

### enableBranchAutoBuild
- **Type**: typing.Optional[bool]

### enableBranchAutoDeletion
- **Type**: typing.Optional[bool]

### enableBasicAuth
- **Type**: typing.Optional[bool]

### basicAuthCredentials
- **Type**: typing.Optional[str]

### customRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.amplify_classes.CustomRule]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### buildSpec
- **Type**: typing.Optional[str]

### customHeaders
- **Type**: typing.Optional[str]

### enableAutoBranchCreation
- **Type**: typing.Optional[bool]

### autoBranchCreationPatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### autoBranchCreationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.AutoBranchCreationConfigUnion]

### cacheConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.CacheConfig]


# CreateAppResult

### app
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.App'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes


# CreateBackendEnvironmentRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### stackName
- **Type**: typing.Optional[str]

### deploymentArtifacts
- **Type**: typing.Optional[str]


# CreateBackendEnvironmentResult

### backendEnvironment
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.BackendEnvironment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes


# CreateBranchRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### stage
- **Type**: typing.Optional[typing.Literal['BETA', 'DEVELOPMENT', 'EXPERIMENTAL', 'PRODUCTION', 'PULL_REQUEST']]

### framework
- **Type**: typing.Optional[str]

### enableNotification
- **Type**: typing.Optional[bool]

### enableAutoBuild
- **Type**: typing.Optional[bool]

### environmentVariables
- **Type**: typing.Optional[typing.Mapping[str, str]]

### basicAuthCredentials
- **Type**: typing.Optional[str]

### enableBasicAuth
- **Type**: typing.Optional[bool]

### enablePerformanceMode
- **Type**: typing.Optional[bool]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### buildSpec
- **Type**: typing.Optional[str]

### ttl
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### enablePullRequestPreview
- **Type**: typing.Optional[bool]

### pullRequestEnvironmentName
- **Type**: typing.Optional[str]

### backendEnvironmentArn
- **Type**: typing.Optional[str]

### backend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.Backend]

### computeRoleArn
- **Type**: typing.Optional[str]


# CreateBranchResult

### branch
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.Branch'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDeploymentRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes

### fileMap
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateDeploymentResult

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### fileUploadUrls
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### zipUploadUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDomainAssociationRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### subDomainSettings
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.amplify_classes.SubDomainSetting]
- **Required**: Yes

### enableAutoSubDomain
- **Type**: typing.Optional[bool]

### autoSubDomainCreationPatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### autoSubDomainIAMRole
- **Type**: typing.Optional[str]

### certificateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.CertificateSettings]


# CreateDomainAssociationResult

### domainAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.DomainAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWebhookRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# CreateWebhookResult

### webhook
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.Webhook'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes


# CustomRule

### source
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[str]

### condition
- **Type**: typing.Optional[str]


# DeleteAppRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAppResult

### app
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.App'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteBackendEnvironmentRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBackendEnvironmentResult

### backendEnvironment
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.BackendEnvironment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteBranchRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBranchResult

### branch
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.Branch'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDomainAssociationRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### domainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainAssociationResult

### domainAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.DomainAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteJobRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteJobResult

### jobSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.JobSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteWebhookRequest

### webhookId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWebhookResult

### webhook
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.Webhook'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes


# DomainAssociation

### domainAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### enableAutoSubDomain
- **Type**: <class 'bool'>
- **Required**: Yes

### domainStatus
- **Type**: typing.Literal['AVAILABLE', 'AWAITING_APP_CNAME', 'CREATING', 'FAILED', 'IMPORTING_CUSTOM_CERTIFICATE', 'IN_PROGRESS', 'PENDING_DEPLOYMENT', 'PENDING_VERIFICATION', 'REQUESTING_CERTIFICATE', 'UPDATING']
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### subDomains
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplify_classes.SubDomain]
- **Required**: Yes

### autoSubDomainCreationPatterns
- **Type**: typing.Optional[typing.List[str]]

### autoSubDomainIAMRole
- **Type**: typing.Optional[str]

### updateStatus
- **Type**: typing.Optional[typing.Literal['AWAITING_APP_CNAME', 'IMPORTING_CUSTOM_CERTIFICATE', 'PENDING_DEPLOYMENT', 'PENDING_VERIFICATION', 'REQUESTING_CERTIFICATE', 'UPDATE_COMPLETE', 'UPDATE_FAILED']]

### certificateVerificationDNSRecord
- **Type**: typing.Optional[str]

### certificate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.Certificate]


# GenerateAccessLogsRequest

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.Timestamp]

### endTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.Timestamp]


# GenerateAccessLogsResult

### logUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes


# GetAppRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAppResult

### app
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.App'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes


# GetArtifactUrlRequest

### artifactId
- **Type**: <class 'str'>
- **Required**: Yes


# GetArtifactUrlResult

### artifactId
- **Type**: <class 'str'>
- **Required**: Yes

### artifactUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes


# GetBackendEnvironmentRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes


# GetBackendEnvironmentResult

### backendEnvironment
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.BackendEnvironment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes


# GetBranchRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes


# GetBranchResult

### branch
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.Branch'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes


# GetDomainAssociationRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### domainName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDomainAssociationResult

### domainAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.DomainAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes


# GetJobRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetJobResult

### job
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.Job'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes


# GetWebhookRequest

### webhookId
- **Type**: <class 'str'>
- **Required**: Yes


# GetWebhookResult

### webhook
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.Webhook'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes


# Job

### summary
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.JobSummary'>
- **Required**: Yes

### steps
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplify_classes.Step]
- **Required**: Yes


# JobSummary

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### commitId
- **Type**: <class 'str'>
- **Required**: Yes

### commitMessage
- **Type**: <class 'str'>
- **Required**: Yes

### commitTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'CREATED', 'FAILED', 'PENDING', 'PROVISIONING', 'RUNNING', 'SUCCEED']
- **Required**: Yes

### jobType
- **Type**: typing.Literal['MANUAL', 'RELEASE', 'RETRY', 'WEB_HOOK']
- **Required**: Yes

### endTime
- **Type**: typing.Optional[datetime.datetime]

### sourceUrl
- **Type**: typing.Optional[str]

### sourceUrlType
- **Type**: typing.Optional[typing.Literal['BUCKET_PREFIX', 'ZIP']]


# ListAppsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAppsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.PaginatorConfig]


# ListAppsResult

### apps
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplify_classes.App]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListArtifactsRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListArtifactsResult

### artifacts
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplify_classes.Artifact]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBackendEnvironmentsRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListBackendEnvironmentsResult

### backendEnvironments
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplify_classes.BackendEnvironment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBranchesRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListBranchesRequestPaginate

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.PaginatorConfig]


# ListBranchesResult

### branches
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplify_classes.Branch]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDomainAssociationsRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDomainAssociationsRequestPaginate

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.PaginatorConfig]


# ListDomainAssociationsResult

### domainAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplify_classes.DomainAssociation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobsRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListJobsRequestPaginate

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.PaginatorConfig]


# ListJobsResult

### jobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplify_classes.JobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes


# ListWebhooksRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListWebhooksResult

### webhooks
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplify_classes.Webhook]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProductionBranch

### lastDeployTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[str]

### thumbnailUrl
- **Type**: typing.Optional[str]

### branchName
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


# StartDeploymentRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: typing.Optional[str]

### sourceUrl
- **Type**: typing.Optional[str]

### sourceUrlType
- **Type**: typing.Optional[typing.Literal['BUCKET_PREFIX', 'ZIP']]


# StartDeploymentResult

### jobSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.JobSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes


# StartJobRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes

### jobType
- **Type**: typing.Literal['MANUAL', 'RELEASE', 'RETRY', 'WEB_HOOK']
- **Required**: Yes

### jobId
- **Type**: typing.Optional[str]

### jobReason
- **Type**: typing.Optional[str]

### commitId
- **Type**: typing.Optional[str]

### commitMessage
- **Type**: typing.Optional[str]

### commitTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.Timestamp]


# StartJobResult

### jobSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.JobSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes


# Step

### stepName
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'CREATED', 'FAILED', 'PENDING', 'PROVISIONING', 'RUNNING', 'SUCCEED']
- **Required**: Yes

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### logUrl
- **Type**: typing.Optional[str]

### artifactsUrl
- **Type**: typing.Optional[str]

### testArtifactsUrl
- **Type**: typing.Optional[str]

### testConfigUrl
- **Type**: typing.Optional[str]

### screenshots
- **Type**: typing.Optional[typing.Dict[str, str]]

### statusReason
- **Type**: typing.Optional[str]

### context
- **Type**: typing.Optional[str]


# StopJobRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# StopJobResult

### jobSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.JobSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes


# SubDomain

### subDomainSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.SubDomainSetting'>
- **Required**: Yes

### verified
- **Type**: <class 'bool'>
- **Required**: Yes

### dnsRecord
- **Type**: <class 'str'>
- **Required**: Yes


# SubDomainSetting

### prefix
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAppRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### platform
- **Type**: typing.Optional[typing.Literal['WEB', 'WEB_COMPUTE', 'WEB_DYNAMIC']]

### computeRoleArn
- **Type**: typing.Optional[str]

### iamServiceRoleArn
- **Type**: typing.Optional[str]

### environmentVariables
- **Type**: typing.Optional[typing.Mapping[str, str]]

### enableBranchAutoBuild
- **Type**: typing.Optional[bool]

### enableBranchAutoDeletion
- **Type**: typing.Optional[bool]

### enableBasicAuth
- **Type**: typing.Optional[bool]

### basicAuthCredentials
- **Type**: typing.Optional[str]

### customRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.amplify_classes.CustomRule]]

### buildSpec
- **Type**: typing.Optional[str]

### customHeaders
- **Type**: typing.Optional[str]

### enableAutoBranchCreation
- **Type**: typing.Optional[bool]

### autoBranchCreationPatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### autoBranchCreationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.AutoBranchCreationConfigUnion]

### repository
- **Type**: typing.Optional[str]

### oauthToken
- **Type**: typing.Optional[str]

### accessToken
- **Type**: typing.Optional[str]

### cacheConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.CacheConfig]


# UpdateAppResult

### app
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.App'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateBranchRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### framework
- **Type**: typing.Optional[str]

### stage
- **Type**: typing.Optional[typing.Literal['BETA', 'DEVELOPMENT', 'EXPERIMENTAL', 'PRODUCTION', 'PULL_REQUEST']]

### enableNotification
- **Type**: typing.Optional[bool]

### enableAutoBuild
- **Type**: typing.Optional[bool]

### environmentVariables
- **Type**: typing.Optional[typing.Mapping[str, str]]

### basicAuthCredentials
- **Type**: typing.Optional[str]

### enableBasicAuth
- **Type**: typing.Optional[bool]

### enablePerformanceMode
- **Type**: typing.Optional[bool]

### buildSpec
- **Type**: typing.Optional[str]

### ttl
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### enablePullRequestPreview
- **Type**: typing.Optional[bool]

### pullRequestEnvironmentName
- **Type**: typing.Optional[str]

### backendEnvironmentArn
- **Type**: typing.Optional[str]

### backend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.Backend]

### computeRoleArn
- **Type**: typing.Optional[str]


# UpdateBranchResult

### branch
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.Branch'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDomainAssociationRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### enableAutoSubDomain
- **Type**: typing.Optional[bool]

### subDomainSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.amplify_classes.SubDomainSetting]]

### autoSubDomainCreationPatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### autoSubDomainIAMRole
- **Type**: typing.Optional[str]

### certificateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.CertificateSettings]


# UpdateDomainAssociationResult

### domainAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.DomainAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateWebhookRequest

### webhookId
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# UpdateWebhookResult

### webhook
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.Webhook'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadata'>
- **Required**: Yes


# WafConfiguration

### webAclArn
- **Type**: typing.Optional[str]

### wafStatus
- **Type**: typing.Optional[typing.Literal['ASSOCIATING', 'ASSOCIATION_FAILED', 'ASSOCIATION_SUCCESS', 'DISASSOCIATING', 'DISASSOCIATION_FAILED']]

### statusReason
- **Type**: typing.Optional[str]


# Webhook

### webhookArn
- **Type**: <class 'str'>
- **Required**: Yes

### webhookId
- **Type**: <class 'str'>
- **Required**: Yes

### webhookUrl
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


