# Proton Classes

# AcceptEnvironmentAccountConnectionInputRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# AcceptEnvironmentAccountConnectionOutputTypeDef

### environmentAccountConnection
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.EnvironmentAccountConnectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AccountSettingsTypeDef

### pipelineCodebuildRoleArn
- **Type**: typing.Optional[str]

### pipelineProvisioningRepository
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.RepositoryBranchTypeDef]

### pipelineServiceRoleArn
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelComponentDeploymentInputRequestTypeDef

### componentName
- **Type**: <class 'str'>
- **Required**: Yes


# CancelComponentDeploymentOutputTypeDef

### component
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ComponentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CancelEnvironmentDeploymentInputRequestTypeDef

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes


# CancelEnvironmentDeploymentOutputTypeDef

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.EnvironmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CancelServiceInstanceDeploymentInputRequestTypeDef

### serviceInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes


# CancelServiceInstanceDeploymentOutputTypeDef

### serviceInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ServiceInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CancelServicePipelineDeploymentInputRequestTypeDef

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes


# CancelServicePipelineDeploymentOutputTypeDef

### pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ServicePipelineTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CompatibleEnvironmentTemplateInputTypeDef

### majorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes


# CompatibleEnvironmentTemplateTypeDef

### majorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes


# ComponentStateTypeDef

### serviceInstanceName
- **Type**: typing.Optional[str]

### serviceName
- **Type**: typing.Optional[str]

### serviceSpec
- **Type**: typing.Optional[str]

### templateFile
- **Type**: typing.Optional[str]


# ComponentSummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### deploymentStatus
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### lastModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentStatusMessage
- **Type**: typing.Optional[str]

### lastAttemptedDeploymentId
- **Type**: typing.Optional[str]

### lastDeploymentAttemptedAt
- **Type**: typing.Optional[datetime.datetime]

### lastDeploymentSucceededAt
- **Type**: typing.Optional[datetime.datetime]

### lastSucceededDeploymentId
- **Type**: typing.Optional[str]

### serviceInstanceName
- **Type**: typing.Optional[str]

### serviceName
- **Type**: typing.Optional[str]


# ComponentTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### deploymentStatus
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### lastModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentStatusMessage
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### lastAttemptedDeploymentId
- **Type**: typing.Optional[str]

### lastClientRequestToken
- **Type**: typing.Optional[str]

### lastDeploymentAttemptedAt
- **Type**: typing.Optional[datetime.datetime]

### lastDeploymentSucceededAt
- **Type**: typing.Optional[datetime.datetime]

### lastSucceededDeploymentId
- **Type**: typing.Optional[str]

### serviceInstanceName
- **Type**: typing.Optional[str]

### serviceName
- **Type**: typing.Optional[str]

### serviceSpec
- **Type**: typing.Optional[str]


# CountsSummaryTypeDef

### components
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.ResourceCountsSummaryTypeDef]

### environmentTemplates
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.ResourceCountsSummaryTypeDef]

### environments
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.ResourceCountsSummaryTypeDef]

### pipelines
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.ResourceCountsSummaryTypeDef]

### serviceInstances
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.ResourceCountsSummaryTypeDef]

### serviceTemplates
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.ResourceCountsSummaryTypeDef]

### services
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.ResourceCountsSummaryTypeDef]


# CreateComponentInputRequestTypeDef

### manifest
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### templateFile
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### environmentName
- **Type**: typing.Optional[str]

### serviceInstanceName
- **Type**: typing.Optional[str]

### serviceName
- **Type**: typing.Optional[str]

### serviceSpec
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.proton_classes.TagTypeDef]]


# CreateComponentOutputTypeDef

### component
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ComponentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEnvironmentAccountConnectionInputRequestTypeDef

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### managementAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### codebuildRoleArn
- **Type**: typing.Optional[str]

### componentRoleArn
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.proton_classes.TagTypeDef]]


# CreateEnvironmentAccountConnectionOutputTypeDef

### environmentAccountConnection
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.EnvironmentAccountConnectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEnvironmentInputRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'str'>
- **Required**: Yes

### templateMajorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### codebuildRoleArn
- **Type**: typing.Optional[str]

### componentRoleArn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### environmentAccountConnectionId
- **Type**: typing.Optional[str]

### protonServiceRoleArn
- **Type**: typing.Optional[str]

### provisioningRepository
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.RepositoryBranchInputTypeDef]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.proton_classes.TagTypeDef]]

### templateMinorVersion
- **Type**: typing.Optional[str]


# CreateEnvironmentOutputTypeDef

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.EnvironmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEnvironmentTemplateInputRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### encryptionKey
- **Type**: typing.Optional[str]

### provisioning
- **Type**: typing.Optional[typing.Literal['CUSTOMER_MANAGED']]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.proton_classes.TagTypeDef]]


# CreateEnvironmentTemplateOutputTypeDef

### environmentTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.EnvironmentTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEnvironmentTemplateVersionInputRequestTypeDef

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.TemplateVersionSourceInputTypeDef'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### majorVersion
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.proton_classes.TagTypeDef]]


# CreateEnvironmentTemplateVersionOutputTypeDef

### environmentTemplateVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.EnvironmentTemplateVersionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRepositoryInputRequestTypeDef

### connectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### provider
- **Type**: typing.Literal['BITBUCKET', 'GITHUB', 'GITHUB_ENTERPRISE']
- **Required**: Yes

### encryptionKey
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.proton_classes.TagTypeDef]]


# CreateRepositoryOutputTypeDef

### repository
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.RepositoryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateServiceInputRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'str'>
- **Required**: Yes

### templateMajorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### repositoryConnectionArn
- **Type**: typing.Optional[str]

### repositoryId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.proton_classes.TagTypeDef]]

### templateMinorVersion
- **Type**: typing.Optional[str]


# CreateServiceInstanceInputRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.proton_classes.TagTypeDef]]

### templateMajorVersion
- **Type**: typing.Optional[str]

### templateMinorVersion
- **Type**: typing.Optional[str]


# CreateServiceInstanceOutputTypeDef

### serviceInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ServiceInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateServiceOutputTypeDef

### service
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ServiceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateServiceSyncConfigInputRequestTypeDef

### branch
- **Type**: <class 'str'>
- **Required**: Yes

### filePath
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryProvider
- **Type**: typing.Literal['BITBUCKET', 'GITHUB', 'GITHUB_ENTERPRISE']
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateServiceSyncConfigOutputTypeDef

### serviceSyncConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ServiceSyncConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateServiceTemplateInputRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### encryptionKey
- **Type**: typing.Optional[str]

### pipelineProvisioning
- **Type**: typing.Optional[typing.Literal['CUSTOMER_MANAGED']]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.proton_classes.TagTypeDef]]


# CreateServiceTemplateOutputTypeDef

### serviceTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ServiceTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateServiceTemplateVersionInputRequestTypeDef

### compatibleEnvironmentTemplates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.proton_classes.CompatibleEnvironmentTemplateInputTypeDef]
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.TemplateVersionSourceInputTypeDef'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### majorVersion
- **Type**: typing.Optional[str]

### supportedComponentSources
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DIRECTLY_DEFINED']]]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.proton_classes.TagTypeDef]]


# CreateServiceTemplateVersionOutputTypeDef

### serviceTemplateVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ServiceTemplateVersionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTemplateSyncConfigInputRequestTypeDef

### branch
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryProvider
- **Type**: typing.Literal['BITBUCKET', 'GITHUB', 'GITHUB_ENTERPRISE']
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### templateType
- **Type**: typing.Literal['ENVIRONMENT', 'SERVICE']
- **Required**: Yes

### subdirectory
- **Type**: typing.Optional[str]


# CreateTemplateSyncConfigOutputTypeDef

### templateSyncConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.TemplateSyncConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteComponentInputRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteComponentOutputTypeDef

### component
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ComponentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDeploymentInputRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeploymentOutputTypeDef

### deployment
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.DeploymentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteEnvironmentAccountConnectionInputRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentAccountConnectionOutputTypeDef

### environmentAccountConnection
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.EnvironmentAccountConnectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteEnvironmentInputRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentOutputTypeDef

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.EnvironmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteEnvironmentTemplateInputRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentTemplateOutputTypeDef

### environmentTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.EnvironmentTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteEnvironmentTemplateVersionInputRequestTypeDef

### majorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### minorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentTemplateVersionOutputTypeDef

### environmentTemplateVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.EnvironmentTemplateVersionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteRepositoryInputRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### provider
- **Type**: typing.Literal['BITBUCKET', 'GITHUB', 'GITHUB_ENTERPRISE']
- **Required**: Yes


# DeleteRepositoryOutputTypeDef

### repository
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.RepositoryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteServiceInputRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceOutputTypeDef

### service
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ServiceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteServiceSyncConfigInputRequestTypeDef

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceSyncConfigOutputTypeDef

### serviceSyncConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ServiceSyncConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteServiceTemplateInputRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceTemplateOutputTypeDef

### serviceTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ServiceTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteServiceTemplateVersionInputRequestTypeDef

### majorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### minorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceTemplateVersionOutputTypeDef

### serviceTemplateVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ServiceTemplateVersionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteTemplateSyncConfigInputRequestTypeDef

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### templateType
- **Type**: typing.Literal['ENVIRONMENT', 'SERVICE']
- **Required**: Yes


# DeleteTemplateSyncConfigOutputTypeDef

### templateSyncConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.TemplateSyncConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeploymentStateTypeDef

### component
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.ComponentStateTypeDef]

### environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.EnvironmentStateTypeDef]

### serviceInstance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.ServiceInstanceStateTypeDef]

### servicePipeline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.ServicePipelineStateTypeDef]


# DeploymentSummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### deploymentStatus
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### targetArn
- **Type**: <class 'str'>
- **Required**: Yes

### targetResourceCreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### targetResourceType
- **Type**: typing.Literal['COMPONENT', 'ENVIRONMENT', 'SERVICE_INSTANCE', 'SERVICE_PIPELINE']
- **Required**: Yes

### completedAt
- **Type**: typing.Optional[datetime.datetime]

### componentName
- **Type**: typing.Optional[str]

### lastAttemptedDeploymentId
- **Type**: typing.Optional[str]

### lastSucceededDeploymentId
- **Type**: typing.Optional[str]

### serviceInstanceName
- **Type**: typing.Optional[str]

### serviceName
- **Type**: typing.Optional[str]


# DeploymentTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### deploymentStatus
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### targetArn
- **Type**: <class 'str'>
- **Required**: Yes

### targetResourceCreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### targetResourceType
- **Type**: typing.Literal['COMPONENT', 'ENVIRONMENT', 'SERVICE_INSTANCE', 'SERVICE_PIPELINE']
- **Required**: Yes

### completedAt
- **Type**: typing.Optional[datetime.datetime]

### componentName
- **Type**: typing.Optional[str]

### deploymentStatusMessage
- **Type**: typing.Optional[str]

### initialState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.DeploymentStateTypeDef]

### lastAttemptedDeploymentId
- **Type**: typing.Optional[str]

### lastSucceededDeploymentId
- **Type**: typing.Optional[str]

### serviceInstanceName
- **Type**: typing.Optional[str]

### serviceName
- **Type**: typing.Optional[str]

### targetState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.DeploymentStateTypeDef]


# EnvironmentAccountConnectionSummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### environmentAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### managementAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### requestedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CONNECTED', 'PENDING', 'REJECTED']
- **Required**: Yes

### componentRoleArn
- **Type**: typing.Optional[str]


# EnvironmentAccountConnectionTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### environmentAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### managementAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### requestedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CONNECTED', 'PENDING', 'REJECTED']
- **Required**: Yes

### codebuildRoleArn
- **Type**: typing.Optional[str]

### componentRoleArn
- **Type**: typing.Optional[str]


# EnvironmentStateTypeDef

### templateMajorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateMinorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: typing.Optional[str]


# EnvironmentSummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### deploymentStatus
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### lastDeploymentAttemptedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastDeploymentSucceededAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### templateMajorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateMinorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### componentRoleArn
- **Type**: typing.Optional[str]

### deploymentStatusMessage
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### environmentAccountConnectionId
- **Type**: typing.Optional[str]

### environmentAccountId
- **Type**: typing.Optional[str]

### lastAttemptedDeploymentId
- **Type**: typing.Optional[str]

### lastSucceededDeploymentId
- **Type**: typing.Optional[str]

### protonServiceRoleArn
- **Type**: typing.Optional[str]

### provisioning
- **Type**: typing.Optional[typing.Literal['CUSTOMER_MANAGED']]


# EnvironmentTemplateFilterTypeDef

### majorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes


# EnvironmentTemplateSummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### provisioning
- **Type**: typing.Optional[typing.Literal['CUSTOMER_MANAGED']]

### recommendedVersion
- **Type**: typing.Optional[str]


# EnvironmentTemplateTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### encryptionKey
- **Type**: typing.Optional[str]

### provisioning
- **Type**: typing.Optional[typing.Literal['CUSTOMER_MANAGED']]

### recommendedVersion
- **Type**: typing.Optional[str]


# EnvironmentTemplateVersionSummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### majorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### minorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DRAFT', 'PUBLISHED', 'REGISTRATION_FAILED', 'REGISTRATION_IN_PROGRESS']
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### recommendedMinorVersion
- **Type**: typing.Optional[str]

### statusMessage
- **Type**: typing.Optional[str]


# EnvironmentTemplateVersionTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### majorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### minorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DRAFT', 'PUBLISHED', 'REGISTRATION_FAILED', 'REGISTRATION_IN_PROGRESS']
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### recommendedMinorVersion
- **Type**: typing.Optional[str]

### schema
- **Type**: typing.Optional[str]

### statusMessage
- **Type**: typing.Optional[str]


# EnvironmentTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### deploymentStatus
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### lastDeploymentAttemptedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastDeploymentSucceededAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### templateMajorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateMinorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### codebuildRoleArn
- **Type**: typing.Optional[str]

### componentRoleArn
- **Type**: typing.Optional[str]

### deploymentStatusMessage
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### environmentAccountConnectionId
- **Type**: typing.Optional[str]

### environmentAccountId
- **Type**: typing.Optional[str]

### lastAttemptedDeploymentId
- **Type**: typing.Optional[str]

### lastSucceededDeploymentId
- **Type**: typing.Optional[str]

### protonServiceRoleArn
- **Type**: typing.Optional[str]

### provisioning
- **Type**: typing.Optional[typing.Literal['CUSTOMER_MANAGED']]

### provisioningRepository
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.RepositoryBranchTypeDef]

### spec
- **Type**: typing.Optional[str]


# GetAccountSettingsOutputTypeDef

### accountSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.AccountSettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetComponentInputComponentDeletedWaitTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.WaiterConfigTypeDef]


# GetComponentInputComponentDeployedWaitTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.WaiterConfigTypeDef]


# GetComponentInputRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetComponentOutputTypeDef

### component
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ComponentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDeploymentInputRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### componentName
- **Type**: typing.Optional[str]

### environmentName
- **Type**: typing.Optional[str]

### serviceInstanceName
- **Type**: typing.Optional[str]

### serviceName
- **Type**: typing.Optional[str]


# GetDeploymentOutputTypeDef

### deployment
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.DeploymentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEnvironmentAccountConnectionInputRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentAccountConnectionOutputTypeDef

### environmentAccountConnection
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.EnvironmentAccountConnectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEnvironmentInputEnvironmentDeployedWaitTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.WaiterConfigTypeDef]


# GetEnvironmentInputRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentOutputTypeDef

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.EnvironmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEnvironmentTemplateInputRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentTemplateOutputTypeDef

### environmentTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.EnvironmentTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEnvironmentTemplateVersionInputEnvironmentTemplateVersionRegisteredWaitTypeDef

### majorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### minorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.WaiterConfigTypeDef]


# GetEnvironmentTemplateVersionInputRequestTypeDef

### majorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### minorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentTemplateVersionOutputTypeDef

### environmentTemplateVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.EnvironmentTemplateVersionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRepositoryInputRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### provider
- **Type**: typing.Literal['BITBUCKET', 'GITHUB', 'GITHUB_ENTERPRISE']
- **Required**: Yes


# GetRepositoryOutputTypeDef

### repository
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.RepositoryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRepositorySyncStatusInputRequestTypeDef

### branch
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryProvider
- **Type**: typing.Literal['BITBUCKET', 'GITHUB', 'GITHUB_ENTERPRISE']
- **Required**: Yes

### syncType
- **Type**: typing.Literal['SERVICE_SYNC', 'TEMPLATE_SYNC']
- **Required**: Yes


# GetRepositorySyncStatusOutputTypeDef

### latestSync
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.RepositorySyncAttemptTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourcesSummaryOutputTypeDef

### counts
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.CountsSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetServiceInputRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceInputServiceCreatedWaitTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.WaiterConfigTypeDef]


# GetServiceInputServiceDeletedWaitTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.WaiterConfigTypeDef]


# GetServiceInputServicePipelineDeployedWaitTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.WaiterConfigTypeDef]


# GetServiceInputServiceUpdatedWaitTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.WaiterConfigTypeDef]


# GetServiceInstanceInputRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceInstanceInputServiceInstanceDeployedWaitTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.WaiterConfigTypeDef]


# GetServiceInstanceOutputTypeDef

### serviceInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ServiceInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetServiceInstanceSyncStatusInputRequestTypeDef

### serviceInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceInstanceSyncStatusOutputTypeDef

### desiredState
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.RevisionTypeDef'>
- **Required**: Yes

### latestSuccessfulSync
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResourceSyncAttemptTypeDef'>
- **Required**: Yes

### latestSync
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResourceSyncAttemptTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetServiceOutputTypeDef

### service
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ServiceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetServiceSyncBlockerSummaryInputRequestTypeDef

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### serviceInstanceName
- **Type**: typing.Optional[str]


# GetServiceSyncBlockerSummaryOutputTypeDef

### serviceSyncBlockerSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ServiceSyncBlockerSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetServiceSyncConfigInputRequestTypeDef

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceSyncConfigOutputTypeDef

### serviceSyncConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ServiceSyncConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetServiceTemplateInputRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceTemplateOutputTypeDef

### serviceTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ServiceTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetServiceTemplateVersionInputRequestTypeDef

### majorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### minorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceTemplateVersionInputServiceTemplateVersionRegisteredWaitTypeDef

### majorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### minorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.WaiterConfigTypeDef]


# GetServiceTemplateVersionOutputTypeDef

### serviceTemplateVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ServiceTemplateVersionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTemplateSyncConfigInputRequestTypeDef

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### templateType
- **Type**: typing.Literal['ENVIRONMENT', 'SERVICE']
- **Required**: Yes


# GetTemplateSyncConfigOutputTypeDef

### templateSyncConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.TemplateSyncConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTemplateSyncStatusInputRequestTypeDef

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### templateType
- **Type**: typing.Literal['ENVIRONMENT', 'SERVICE']
- **Required**: Yes

### templateVersion
- **Type**: <class 'str'>
- **Required**: Yes


# GetTemplateSyncStatusOutputTypeDef

### desiredState
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.RevisionTypeDef'>
- **Required**: Yes

### latestSuccessfulSync
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResourceSyncAttemptTypeDef'>
- **Required**: Yes

### latestSync
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResourceSyncAttemptTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListComponentOutputsInputListComponentOutputsPaginateTypeDef

### componentName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListComponentOutputsInputRequestTypeDef

### componentName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListComponentOutputsOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.OutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListComponentProvisionedResourcesInputListComponentProvisionedResourcesPaginateTypeDef

### componentName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListComponentProvisionedResourcesInputRequestTypeDef

### componentName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListComponentProvisionedResourcesOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### provisionedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.ProvisionedResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListComponentsInputListComponentsPaginateTypeDef

### environmentName
- **Type**: typing.Optional[str]

### serviceInstanceName
- **Type**: typing.Optional[str]

### serviceName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListComponentsInputRequestTypeDef

### environmentName
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### serviceInstanceName
- **Type**: typing.Optional[str]

### serviceName
- **Type**: typing.Optional[str]


# ListComponentsOutputTypeDef

### components
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.ComponentSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDeploymentsInputListDeploymentsPaginateTypeDef

### componentName
- **Type**: typing.Optional[str]

### environmentName
- **Type**: typing.Optional[str]

### serviceInstanceName
- **Type**: typing.Optional[str]

### serviceName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListDeploymentsInputRequestTypeDef

### componentName
- **Type**: typing.Optional[str]

### environmentName
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### serviceInstanceName
- **Type**: typing.Optional[str]

### serviceName
- **Type**: typing.Optional[str]


# ListDeploymentsOutputTypeDef

### deployments
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.DeploymentSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEnvironmentAccountConnectionsInputListEnvironmentAccountConnectionsPaginateTypeDef

### requestedBy
- **Type**: typing.Literal['ENVIRONMENT_ACCOUNT', 'MANAGEMENT_ACCOUNT']
- **Required**: Yes

### environmentName
- **Type**: typing.Optional[str]

### statuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CONNECTED', 'PENDING', 'REJECTED']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListEnvironmentAccountConnectionsInputRequestTypeDef

### requestedBy
- **Type**: typing.Literal['ENVIRONMENT_ACCOUNT', 'MANAGEMENT_ACCOUNT']
- **Required**: Yes

### environmentName
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### statuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CONNECTED', 'PENDING', 'REJECTED']]]


# ListEnvironmentAccountConnectionsOutputTypeDef

### environmentAccountConnections
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.EnvironmentAccountConnectionSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEnvironmentOutputsInputListEnvironmentOutputsPaginateTypeDef

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListEnvironmentOutputsInputRequestTypeDef

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentOutputsOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.OutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEnvironmentProvisionedResourcesInputListEnvironmentProvisionedResourcesPaginateTypeDef

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListEnvironmentProvisionedResourcesInputRequestTypeDef

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentProvisionedResourcesOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### provisionedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.ProvisionedResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEnvironmentTemplateVersionsInputListEnvironmentTemplateVersionsPaginateTypeDef

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### majorVersion
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListEnvironmentTemplateVersionsInputRequestTypeDef

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### majorVersion
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentTemplateVersionsOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### templateVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.EnvironmentTemplateVersionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEnvironmentTemplatesInputListEnvironmentTemplatesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListEnvironmentTemplatesInputRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentTemplatesOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### templates
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.EnvironmentTemplateSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEnvironmentsInputListEnvironmentsPaginateTypeDef

### environmentTemplates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.proton_classes.EnvironmentTemplateFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListEnvironmentsInputRequestTypeDef

### environmentTemplates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.proton_classes.EnvironmentTemplateFilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentsOutputTypeDef

### environments
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.EnvironmentSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRepositoriesInputListRepositoriesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListRepositoriesInputRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListRepositoriesOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### repositories
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.RepositorySummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRepositorySyncDefinitionsInputListRepositorySyncDefinitionsPaginateTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryProvider
- **Type**: typing.Literal['BITBUCKET', 'GITHUB', 'GITHUB_ENTERPRISE']
- **Required**: Yes

### syncType
- **Type**: typing.Literal['SERVICE_SYNC', 'TEMPLATE_SYNC']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListRepositorySyncDefinitionsInputRequestTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryProvider
- **Type**: typing.Literal['BITBUCKET', 'GITHUB', 'GITHUB_ENTERPRISE']
- **Required**: Yes

### syncType
- **Type**: typing.Literal['SERVICE_SYNC', 'TEMPLATE_SYNC']
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRepositorySyncDefinitionsOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### syncDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.RepositorySyncDefinitionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListServiceInstanceOutputsInputListServiceInstanceOutputsPaginateTypeDef

### serviceInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListServiceInstanceOutputsInputRequestTypeDef

### serviceInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListServiceInstanceOutputsOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.OutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListServiceInstanceProvisionedResourcesInputListServiceInstanceProvisionedResourcesPaginateTypeDef

### serviceInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListServiceInstanceProvisionedResourcesInputRequestTypeDef

### serviceInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServiceInstanceProvisionedResourcesOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### provisionedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.ProvisionedResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListServiceInstancesFilterTypeDef

### key
- **Type**: typing.Optional[typing.Literal['createdAtAfter', 'createdAtBefore', 'deployedTemplateVersionStatus', 'deploymentStatus', 'environmentName', 'lastDeploymentAttemptedAtAfter', 'lastDeploymentAttemptedAtBefore', 'name', 'serviceName', 'templateName']]

### value
- **Type**: typing.Optional[str]


# ListServiceInstancesInputListServiceInstancesPaginateTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.proton_classes.ListServiceInstancesFilterTypeDef]]

### serviceName
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['createdAt', 'deploymentStatus', 'environmentName', 'lastDeploymentAttemptedAt', 'name', 'serviceName', 'templateName']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListServiceInstancesInputRequestTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.proton_classes.ListServiceInstancesFilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### serviceName
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['createdAt', 'deploymentStatus', 'environmentName', 'lastDeploymentAttemptedAt', 'name', 'serviceName', 'templateName']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# ListServiceInstancesOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### serviceInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.ServiceInstanceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListServicePipelineOutputsInputListServicePipelineOutputsPaginateTypeDef

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListServicePipelineOutputsInputRequestTypeDef

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListServicePipelineOutputsOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.OutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListServicePipelineProvisionedResourcesInputListServicePipelineProvisionedResourcesPaginateTypeDef

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListServicePipelineProvisionedResourcesInputRequestTypeDef

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServicePipelineProvisionedResourcesOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### provisionedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.ProvisionedResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListServiceTemplateVersionsInputListServiceTemplateVersionsPaginateTypeDef

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### majorVersion
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListServiceTemplateVersionsInputRequestTypeDef

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### majorVersion
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListServiceTemplateVersionsOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### templateVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.ServiceTemplateVersionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListServiceTemplatesInputListServiceTemplatesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListServiceTemplatesInputRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListServiceTemplatesOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### templates
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.ServiceTemplateSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListServicesInputListServicesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListServicesInputRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListServicesOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### services
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.ServiceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceInputListTagsForResourcePaginateTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListTagsForResourceInputRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# NotifyResourceDeploymentStatusChangeInputRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: typing.Optional[str]

### outputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.proton_classes.OutputTypeDef]]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']]

### statusMessage
- **Type**: typing.Optional[str]


# OutputTypeDef

### key
- **Type**: typing.Optional[str]

### valueString
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProvisionedResourceTypeDef

### identifier
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### provisioningEngine
- **Type**: typing.Optional[typing.Literal['CLOUDFORMATION', 'TERRAFORM']]


# RejectEnvironmentAccountConnectionInputRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# RejectEnvironmentAccountConnectionOutputTypeDef

### environmentAccountConnection
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.EnvironmentAccountConnectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RepositoryBranchInputTypeDef

### branch
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### provider
- **Type**: typing.Literal['BITBUCKET', 'GITHUB', 'GITHUB_ENTERPRISE']
- **Required**: Yes


# RepositoryBranchTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### branch
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### provider
- **Type**: typing.Literal['BITBUCKET', 'GITHUB', 'GITHUB_ENTERPRISE']
- **Required**: Yes


# RepositorySummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### connectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### provider
- **Type**: typing.Literal['BITBUCKET', 'GITHUB', 'GITHUB_ENTERPRISE']
- **Required**: Yes


# RepositorySyncAttemptTypeDef

### events
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.RepositorySyncEventTypeDef]
- **Required**: Yes

### startedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'INITIATED', 'IN_PROGRESS', 'QUEUED', 'SUCCEEDED']
- **Required**: Yes


# RepositorySyncDefinitionTypeDef

### branch
- **Type**: <class 'str'>
- **Required**: Yes

### directory
- **Type**: <class 'str'>
- **Required**: Yes

### parent
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: <class 'str'>
- **Required**: Yes


# RepositorySyncEventTypeDef

### event
- **Type**: <class 'str'>
- **Required**: Yes

### time
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### externalId
- **Type**: typing.Optional[str]


# RepositoryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### connectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### provider
- **Type**: typing.Literal['BITBUCKET', 'GITHUB', 'GITHUB_ENTERPRISE']
- **Required**: Yes

### encryptionKey
- **Type**: typing.Optional[str]


# ResourceCountsSummaryTypeDef

### total
- **Type**: <class 'int'>
- **Required**: Yes

### behindMajor
- **Type**: typing.Optional[int]

### behindMinor
- **Type**: typing.Optional[int]

### failed
- **Type**: typing.Optional[int]

### upToDate
- **Type**: typing.Optional[int]


# ResourceSyncAttemptTypeDef

### events
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.ResourceSyncEventTypeDef]
- **Required**: Yes

### initialRevision
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.RevisionTypeDef'>
- **Required**: Yes

### startedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'INITIATED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### target
- **Type**: <class 'str'>
- **Required**: Yes

### targetRevision
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.RevisionTypeDef'>
- **Required**: Yes


# ResourceSyncEventTypeDef

### event
- **Type**: <class 'str'>
- **Required**: Yes

### time
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### externalId
- **Type**: typing.Optional[str]


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HostId
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


# RevisionTypeDef

### branch
- **Type**: <class 'str'>
- **Required**: Yes

### directory
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryProvider
- **Type**: typing.Literal['BITBUCKET', 'GITHUB', 'GITHUB_ENTERPRISE']
- **Required**: Yes

### sha
- **Type**: <class 'str'>
- **Required**: Yes


# S3ObjectSourceTypeDef

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes


# ServiceInstanceStateTypeDef

### spec
- **Type**: <class 'str'>
- **Required**: Yes

### templateMajorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateMinorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### lastSuccessfulComponentDeploymentIds
- **Type**: typing.Optional[typing.List[str]]

### lastSuccessfulEnvironmentDeploymentId
- **Type**: typing.Optional[str]

### lastSuccessfulServicePipelineDeploymentId
- **Type**: typing.Optional[str]


# ServiceInstanceSummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### deploymentStatus
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### lastDeploymentAttemptedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastDeploymentSucceededAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### templateMajorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateMinorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentStatusMessage
- **Type**: typing.Optional[str]

### lastAttemptedDeploymentId
- **Type**: typing.Optional[str]

### lastSucceededDeploymentId
- **Type**: typing.Optional[str]


# ServiceInstanceTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### deploymentStatus
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### lastDeploymentAttemptedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastDeploymentSucceededAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### templateMajorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateMinorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentStatusMessage
- **Type**: typing.Optional[str]

### lastAttemptedDeploymentId
- **Type**: typing.Optional[str]

### lastClientRequestToken
- **Type**: typing.Optional[str]

### lastSucceededDeploymentId
- **Type**: typing.Optional[str]

### spec
- **Type**: typing.Optional[str]


# ServicePipelineStateTypeDef

### templateMajorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateMinorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: typing.Optional[str]


# ServicePipelineTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### deploymentStatus
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### lastDeploymentAttemptedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastDeploymentSucceededAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### templateMajorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateMinorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentStatusMessage
- **Type**: typing.Optional[str]

### lastAttemptedDeploymentId
- **Type**: typing.Optional[str]

### lastSucceededDeploymentId
- **Type**: typing.Optional[str]

### spec
- **Type**: typing.Optional[str]


# ServiceSummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_FAILED_CLEANUP_COMPLETE', 'CREATE_FAILED_CLEANUP_FAILED', 'CREATE_FAILED_CLEANUP_IN_PROGRESS', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'UPDATE_COMPLETE_CLEANUP_FAILED', 'UPDATE_FAILED', 'UPDATE_FAILED_CLEANUP_COMPLETE', 'UPDATE_FAILED_CLEANUP_FAILED', 'UPDATE_FAILED_CLEANUP_IN_PROGRESS', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### statusMessage
- **Type**: typing.Optional[str]


# ServiceSyncBlockerSummaryTypeDef

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### latestBlockers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.proton_classes.SyncBlockerTypeDef]]

### serviceInstanceName
- **Type**: typing.Optional[str]


# ServiceSyncConfigTypeDef

### branch
- **Type**: <class 'str'>
- **Required**: Yes

### filePath
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryProvider
- **Type**: typing.Literal['BITBUCKET', 'GITHUB', 'GITHUB_ENTERPRISE']
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes


# ServiceTemplateSummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### pipelineProvisioning
- **Type**: typing.Optional[typing.Literal['CUSTOMER_MANAGED']]

### recommendedVersion
- **Type**: typing.Optional[str]


# ServiceTemplateTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### encryptionKey
- **Type**: typing.Optional[str]

### pipelineProvisioning
- **Type**: typing.Optional[typing.Literal['CUSTOMER_MANAGED']]

### recommendedVersion
- **Type**: typing.Optional[str]


# ServiceTemplateVersionSummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### majorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### minorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DRAFT', 'PUBLISHED', 'REGISTRATION_FAILED', 'REGISTRATION_IN_PROGRESS']
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### recommendedMinorVersion
- **Type**: typing.Optional[str]

### statusMessage
- **Type**: typing.Optional[str]


# ServiceTemplateVersionTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### compatibleEnvironmentTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.CompatibleEnvironmentTemplateTypeDef]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### majorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### minorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DRAFT', 'PUBLISHED', 'REGISTRATION_FAILED', 'REGISTRATION_IN_PROGRESS']
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### recommendedMinorVersion
- **Type**: typing.Optional[str]

### schema
- **Type**: typing.Optional[str]

### statusMessage
- **Type**: typing.Optional[str]

### supportedComponentSources
- **Type**: typing.Optional[typing.List[typing.Literal['DIRECTLY_DEFINED']]]


# ServiceTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_FAILED_CLEANUP_COMPLETE', 'CREATE_FAILED_CLEANUP_FAILED', 'CREATE_FAILED_CLEANUP_IN_PROGRESS', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'UPDATE_COMPLETE_CLEANUP_FAILED', 'UPDATE_FAILED', 'UPDATE_FAILED_CLEANUP_COMPLETE', 'UPDATE_FAILED_CLEANUP_FAILED', 'UPDATE_FAILED_CLEANUP_IN_PROGRESS', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### pipeline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.ServicePipelineTypeDef]

### repositoryConnectionArn
- **Type**: typing.Optional[str]

### repositoryId
- **Type**: typing.Optional[str]

### statusMessage
- **Type**: typing.Optional[str]


# SyncBlockerContextTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# SyncBlockerTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdReason
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'RESOLVED']
- **Required**: Yes

### type
- **Type**: typing.Literal['AUTOMATED']
- **Required**: Yes

### contexts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.proton_classes.SyncBlockerContextTypeDef]]

### resolvedAt
- **Type**: typing.Optional[datetime.datetime]

### resolvedReason
- **Type**: typing.Optional[str]


# TagResourceInputRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.proton_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TemplateSyncConfigTypeDef

### branch
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryProvider
- **Type**: typing.Literal['BITBUCKET', 'GITHUB', 'GITHUB_ENTERPRISE']
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### templateType
- **Type**: typing.Literal['ENVIRONMENT', 'SERVICE']
- **Required**: Yes

### subdirectory
- **Type**: typing.Optional[str]


# TemplateVersionSourceInputTypeDef

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.S3ObjectSourceTypeDef]


# UntagResourceInputRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAccountSettingsInputRequestTypeDef

### deletePipelineProvisioningRepository
- **Type**: typing.Optional[bool]

### pipelineCodebuildRoleArn
- **Type**: typing.Optional[str]

### pipelineProvisioningRepository
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.RepositoryBranchInputTypeDef]

### pipelineServiceRoleArn
- **Type**: typing.Optional[str]


# UpdateAccountSettingsOutputTypeDef

### accountSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.AccountSettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateComponentInputRequestTypeDef

### deploymentType
- **Type**: typing.Literal['CURRENT_VERSION', 'NONE']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### serviceInstanceName
- **Type**: typing.Optional[str]

### serviceName
- **Type**: typing.Optional[str]

### serviceSpec
- **Type**: typing.Optional[str]

### templateFile
- **Type**: typing.Optional[str]


# UpdateComponentOutputTypeDef

### component
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ComponentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEnvironmentAccountConnectionInputRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### codebuildRoleArn
- **Type**: typing.Optional[str]

### componentRoleArn
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]


# UpdateEnvironmentAccountConnectionOutputTypeDef

### environmentAccountConnection
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.EnvironmentAccountConnectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEnvironmentInputRequestTypeDef

### deploymentType
- **Type**: typing.Literal['CURRENT_VERSION', 'MAJOR_VERSION', 'MINOR_VERSION', 'NONE']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### codebuildRoleArn
- **Type**: typing.Optional[str]

### componentRoleArn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### environmentAccountConnectionId
- **Type**: typing.Optional[str]

### protonServiceRoleArn
- **Type**: typing.Optional[str]

### provisioningRepository
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.RepositoryBranchInputTypeDef]

### spec
- **Type**: typing.Optional[str]

### templateMajorVersion
- **Type**: typing.Optional[str]

### templateMinorVersion
- **Type**: typing.Optional[str]


# UpdateEnvironmentOutputTypeDef

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.EnvironmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEnvironmentTemplateInputRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]


# UpdateEnvironmentTemplateOutputTypeDef

### environmentTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.EnvironmentTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEnvironmentTemplateVersionInputRequestTypeDef

### majorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### minorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DRAFT', 'PUBLISHED', 'REGISTRATION_FAILED', 'REGISTRATION_IN_PROGRESS']]


# UpdateEnvironmentTemplateVersionOutputTypeDef

### environmentTemplateVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.EnvironmentTemplateVersionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateServiceInputRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### spec
- **Type**: typing.Optional[str]


# UpdateServiceInstanceInputRequestTypeDef

### deploymentType
- **Type**: typing.Literal['CURRENT_VERSION', 'MAJOR_VERSION', 'MINOR_VERSION', 'NONE']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### spec
- **Type**: typing.Optional[str]

### templateMajorVersion
- **Type**: typing.Optional[str]

### templateMinorVersion
- **Type**: typing.Optional[str]


# UpdateServiceInstanceOutputTypeDef

### serviceInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ServiceInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateServiceOutputTypeDef

### service
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ServiceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateServicePipelineInputRequestTypeDef

### deploymentType
- **Type**: typing.Literal['CURRENT_VERSION', 'MAJOR_VERSION', 'MINOR_VERSION', 'NONE']
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'str'>
- **Required**: Yes

### templateMajorVersion
- **Type**: typing.Optional[str]

### templateMinorVersion
- **Type**: typing.Optional[str]


# UpdateServicePipelineOutputTypeDef

### pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ServicePipelineTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateServiceSyncBlockerInputRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### resolvedReason
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateServiceSyncBlockerOutputTypeDef

### serviceInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### serviceSyncBlocker
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.SyncBlockerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateServiceSyncConfigInputRequestTypeDef

### branch
- **Type**: <class 'str'>
- **Required**: Yes

### filePath
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryProvider
- **Type**: typing.Literal['BITBUCKET', 'GITHUB', 'GITHUB_ENTERPRISE']
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateServiceSyncConfigOutputTypeDef

### serviceSyncConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ServiceSyncConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateServiceTemplateInputRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]


# UpdateServiceTemplateOutputTypeDef

### serviceTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ServiceTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateServiceTemplateVersionInputRequestTypeDef

### majorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### minorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### compatibleEnvironmentTemplates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.proton_classes.CompatibleEnvironmentTemplateInputTypeDef]]

### description
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DRAFT', 'PUBLISHED', 'REGISTRATION_FAILED', 'REGISTRATION_IN_PROGRESS']]

### supportedComponentSources
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DIRECTLY_DEFINED']]]


# UpdateServiceTemplateVersionOutputTypeDef

### serviceTemplateVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ServiceTemplateVersionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTemplateSyncConfigInputRequestTypeDef

### branch
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryProvider
- **Type**: typing.Literal['BITBUCKET', 'GITHUB', 'GITHUB_ENTERPRISE']
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### templateType
- **Type**: typing.Literal['ENVIRONMENT', 'SERVICE']
- **Required**: Yes

### subdirectory
- **Type**: typing.Optional[str]


# UpdateTemplateSyncConfigOutputTypeDef

### templateSyncConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.TemplateSyncConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


