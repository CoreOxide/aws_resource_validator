# amplify_classes

# AppTypeDef

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

### iamServiceRoleArn
- **Type**: typing.Optional[str]

### enableBranchAutoDeletion
- **Type**: typing.Optional[bool]

### basicAuthCredentials
- **Type**: typing.Optional[str]

### customRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplify_classes.CustomRuleTypeDef]]

### productionBranch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.ProductionBranchTypeDef]

### buildSpec
- **Type**: typing.Optional[str]

### customHeaders
- **Type**: typing.Optional[str]

### enableAutoBranchCreation
- **Type**: typing.Optional[bool]

### autoBranchCreationPatterns
- **Type**: typing.Optional[typing.List[str]]

### autoBranchCreationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.AutoBranchCreationConfigOutputTypeDef]

### repositoryCloneMethod
- **Type**: typing.Optional[typing.Literal['SIGV4', 'SSH', 'TOKEN']]


# ArtifactTypeDef

### artifactFileName
- **Type**: <class 'str'>
- **Required**: Yes

### artifactId
- **Type**: <class 'str'>
- **Required**: Yes


# AutoBranchCreationConfigExtraOutputTypeDef

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


# AutoBranchCreationConfigOutputTypeDef

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


# AutoBranchCreationConfigTypeDef

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


# BackendEnvironmentTypeDef

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


# BackendTypeDef

### stackArn
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BranchTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.BackendTypeDef]


# CertificateSettingsTypeDef

### type
- **Type**: typing.Literal['AMPLIFY_MANAGED', 'CUSTOM']
- **Required**: Yes

### customCertificateArn
- **Type**: typing.Optional[str]


# CertificateTypeDef

### type
- **Type**: typing.Literal['AMPLIFY_MANAGED', 'CUSTOM']
- **Required**: Yes

### customCertificateArn
- **Type**: typing.Optional[str]

### certificateVerificationDNSRecord
- **Type**: typing.Optional[str]


# CreateAppRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### repository
- **Type**: typing.Optional[str]

### platform
- **Type**: typing.Optional[typing.Literal['WEB', 'WEB_COMPUTE', 'WEB_DYNAMIC']]

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.amplify_classes.CustomRuleTypeDef]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.AutoBranchCreationConfigTypeDef]


# CreateAppResultTypeDef

### app
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.AppTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateBackendEnvironmentRequestRequestTypeDef

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


# CreateBackendEnvironmentResultTypeDef

### backendEnvironment
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.BackendEnvironmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateBranchRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.BackendTypeDef]


# CreateBranchResultTypeDef

### branch
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.BranchTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDeploymentRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes

### fileMap
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateDeploymentResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDomainAssociationRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### subDomainSettings
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.amplify_classes.SubDomainSettingTypeDef]
- **Required**: Yes

### enableAutoSubDomain
- **Type**: typing.Optional[bool]

### autoSubDomainCreationPatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### autoSubDomainIAMRole
- **Type**: typing.Optional[str]

### certificateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.CertificateSettingsTypeDef]


# CreateDomainAssociationResultTypeDef

### domainAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.DomainAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWebhookRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# CreateWebhookResultTypeDef

### webhook
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.WebhookTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomRuleTypeDef

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


# DeleteAppRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAppResultTypeDef

### app
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.AppTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteBackendEnvironmentRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBackendEnvironmentResultTypeDef

### backendEnvironment
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.BackendEnvironmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteBranchRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBranchResultTypeDef

### branch
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.BranchTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDomainAssociationRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### domainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainAssociationResultTypeDef

### domainAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.DomainAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteJobRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteJobResultTypeDef

### jobSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.JobSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteWebhookRequestRequestTypeDef

### webhookId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWebhookResultTypeDef

### webhook
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.WebhookTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DomainAssociationTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplify_classes.SubDomainTypeDef]
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.CertificateTypeDef]


# GenerateAccessLogsRequestRequestTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# GenerateAccessLogsResultTypeDef

### logUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAppRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAppResultTypeDef

### app
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.AppTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetArtifactUrlRequestRequestTypeDef

### artifactId
- **Type**: <class 'str'>
- **Required**: Yes


# GetArtifactUrlResultTypeDef

### artifactId
- **Type**: <class 'str'>
- **Required**: Yes

### artifactUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBackendEnvironmentRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes


# GetBackendEnvironmentResultTypeDef

### backendEnvironment
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.BackendEnvironmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBranchRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes


# GetBranchResultTypeDef

### branch
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.BranchTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDomainAssociationRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### domainName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDomainAssociationResultTypeDef

### domainAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.DomainAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetJobRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetJobResultTypeDef

### job
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.JobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWebhookRequestRequestTypeDef

### webhookId
- **Type**: <class 'str'>
- **Required**: Yes


# GetWebhookResultTypeDef

### webhook
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.WebhookTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# JobSummaryTypeDef

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
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'FAILED', 'PENDING', 'PROVISIONING', 'RUNNING', 'SUCCEED']
- **Required**: Yes

### jobType
- **Type**: typing.Literal['MANUAL', 'RELEASE', 'RETRY', 'WEB_HOOK']
- **Required**: Yes

### endTime
- **Type**: typing.Optional[datetime.datetime]


# JobTypeDef

### summary
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.JobSummaryTypeDef'>
- **Required**: Yes

### steps
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplify_classes.StepTypeDef]
- **Required**: Yes


# ListAppsRequestListAppsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.PaginatorConfigTypeDef]


# ListAppsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAppsResultTypeDef

### apps
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplify_classes.AppTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListArtifactsRequestRequestTypeDef

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


# ListArtifactsResultTypeDef

### artifacts
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplify_classes.ArtifactTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBackendEnvironmentsRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListBackendEnvironmentsResultTypeDef

### backendEnvironments
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplify_classes.BackendEnvironmentTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBranchesRequestListBranchesPaginateTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.PaginatorConfigTypeDef]


# ListBranchesRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListBranchesResultTypeDef

### branches
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplify_classes.BranchTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDomainAssociationsRequestListDomainAssociationsPaginateTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.PaginatorConfigTypeDef]


# ListDomainAssociationsRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDomainAssociationsResultTypeDef

### domainAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplify_classes.DomainAssociationTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListJobsRequestListJobsPaginateTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.PaginatorConfigTypeDef]


# ListJobsRequestRequestTypeDef

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


# ListJobsResultTypeDef

### jobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplify_classes.JobSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWebhooksRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListWebhooksResultTypeDef

### webhooks
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplify_classes.WebhookTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProductionBranchTypeDef

### lastDeployTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[str]

### thumbnailUrl
- **Type**: typing.Optional[str]

### branchName
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


# StartDeploymentRequestRequestTypeDef

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


# StartDeploymentResultTypeDef

### jobSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.JobSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartJobRequestRequestTypeDef

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
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# StartJobResultTypeDef

### jobSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.JobSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StepTypeDef

### stepName
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'FAILED', 'PENDING', 'PROVISIONING', 'RUNNING', 'SUCCEED']
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


# StopJobRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# StopJobResultTypeDef

### jobSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.JobSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SubDomainSettingTypeDef

### prefix
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes


# SubDomainTypeDef

### subDomainSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.SubDomainSettingTypeDef'>
- **Required**: Yes

### verified
- **Type**: <class 'bool'>
- **Required**: Yes

### dnsRecord
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAppRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### platform
- **Type**: typing.Optional[typing.Literal['WEB', 'WEB_COMPUTE', 'WEB_DYNAMIC']]

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.amplify_classes.CustomRuleTypeDef]]

### buildSpec
- **Type**: typing.Optional[str]

### customHeaders
- **Type**: typing.Optional[str]

### enableAutoBranchCreation
- **Type**: typing.Optional[bool]

### autoBranchCreationPatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### autoBranchCreationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.AutoBranchCreationConfigTypeDef]

### repository
- **Type**: typing.Optional[str]

### oauthToken
- **Type**: typing.Optional[str]

### accessToken
- **Type**: typing.Optional[str]


# UpdateAppResultTypeDef

### app
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.AppTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateBranchRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.BackendTypeDef]


# UpdateBranchResultTypeDef

### branch
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.BranchTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDomainAssociationRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### enableAutoSubDomain
- **Type**: typing.Optional[bool]

### subDomainSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.amplify_classes.SubDomainSettingTypeDef]]

### autoSubDomainCreationPatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### autoSubDomainIAMRole
- **Type**: typing.Optional[str]

### certificateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplify_classes.CertificateSettingsTypeDef]


# UpdateDomainAssociationResultTypeDef

### domainAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.DomainAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateWebhookRequestRequestTypeDef

### webhookId
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# UpdateWebhookResultTypeDef

### webhook
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.WebhookTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplify_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WebhookTypeDef

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


