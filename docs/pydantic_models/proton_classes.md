# Proton Classes

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

# CancelComponentDeploymentInputTypeDef

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


# CancelEnvironmentDeploymentInputTypeDef

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


# CancelServiceInstanceDeploymentInputTypeDef

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


# CancelServicePipelineDeploymentInputTypeDef

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


# CreateComponentInputTypeDef

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


# CreateEnvironmentAccountConnectionInputTypeDef

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


# CreateEnvironmentInputTypeDef

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


# CreateEnvironmentTemplateInputTypeDef

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


# CreateEnvironmentTemplateVersionInputTypeDef

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


# CreateRepositoryInputTypeDef

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


# CreateServiceInputTypeDef

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


# CreateServiceInstanceInputTypeDef

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


# CreateServiceSyncConfigInputTypeDef

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


# CreateServiceTemplateInputTypeDef

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


# CreateServiceTemplateVersionInputTypeDef

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


# CreateTemplateSyncConfigInputTypeDef

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


# DeleteComponentInputTypeDef

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


# DeleteDeploymentOutputTypeDef

### deployment
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.DeploymentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteEnvironmentAccountConnectionOutputTypeDef

### environmentAccountConnection
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.EnvironmentAccountConnectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteEnvironmentInputTypeDef

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


# DeleteEnvironmentTemplateInputTypeDef

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


# DeleteEnvironmentTemplateVersionInputTypeDef

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


# DeleteRepositoryInputTypeDef

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


# DeleteServiceInputTypeDef

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


# DeleteServiceSyncConfigInputTypeDef

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


# DeleteServiceTemplateInputTypeDef

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


# DeleteServiceTemplateVersionInputTypeDef

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


# DeleteTemplateSyncConfigInputTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeploymentTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EnvironmentAccountConnectionSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EnvironmentAccountConnectionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# GetComponentInputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetComponentInputWaitExtraTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.WaiterConfigTypeDef]


# GetComponentInputWaitTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.WaiterConfigTypeDef]


# GetComponentOutputTypeDef

### component
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ComponentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDeploymentOutputTypeDef

### deployment
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.DeploymentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEnvironmentAccountConnectionOutputTypeDef

### environmentAccountConnection
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.EnvironmentAccountConnectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEnvironmentInputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentInputWaitTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.WaiterConfigTypeDef]


# GetEnvironmentOutputTypeDef

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.EnvironmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEnvironmentTemplateInputTypeDef

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


# GetEnvironmentTemplateVersionInputTypeDef

### majorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### minorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentTemplateVersionInputWaitTypeDef

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


# GetEnvironmentTemplateVersionOutputTypeDef

### environmentTemplateVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.EnvironmentTemplateVersionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRepositoryInputTypeDef

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


# GetRepositorySyncStatusInputTypeDef

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


# GetServiceInputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceInputWaitExtraExtraExtraTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.WaiterConfigTypeDef]


# GetServiceInputWaitExtraExtraTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.WaiterConfigTypeDef]


# GetServiceInputWaitExtraTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.WaiterConfigTypeDef]


# GetServiceInputWaitTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.WaiterConfigTypeDef]


# GetServiceInstanceInputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceInstanceInputWaitTypeDef

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


# GetServiceInstanceSyncStatusInputTypeDef

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


# GetServiceSyncBlockerSummaryInputTypeDef

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


# GetServiceSyncConfigInputTypeDef

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


# GetServiceTemplateInputTypeDef

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


# GetServiceTemplateVersionInputTypeDef

### majorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### minorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceTemplateVersionInputWaitTypeDef

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


# GetTemplateSyncConfigInputTypeDef

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


# GetTemplateSyncStatusInputTypeDef

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


# ListComponentOutputsInputPaginateTypeDef

### componentName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListComponentOutputsInputTypeDef

### componentName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListComponentOutputsOutputTypeDef

### outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.OutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListComponentProvisionedResourcesInputPaginateTypeDef

### componentName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListComponentProvisionedResourcesInputTypeDef

### componentName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListComponentProvisionedResourcesOutputTypeDef

### provisionedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.ProvisionedResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListComponentsInputPaginateTypeDef

### environmentName
- **Type**: typing.Optional[str]

### serviceInstanceName
- **Type**: typing.Optional[str]

### serviceName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListComponentsInputTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDeploymentsInputPaginateTypeDef

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


# ListDeploymentsInputTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentAccountConnectionsInputPaginateTypeDef

### requestedBy
- **Type**: typing.Literal['ENVIRONMENT_ACCOUNT', 'MANAGEMENT_ACCOUNT']
- **Required**: Yes

### environmentName
- **Type**: typing.Optional[str]

### statuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CONNECTED', 'PENDING', 'REJECTED']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListEnvironmentAccountConnectionsInputTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentOutputsInputPaginateTypeDef

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListEnvironmentOutputsInputTypeDef

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentOutputsOutputTypeDef

### outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.OutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentProvisionedResourcesInputPaginateTypeDef

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListEnvironmentProvisionedResourcesInputTypeDef

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentProvisionedResourcesOutputTypeDef

### provisionedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.ProvisionedResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentTemplateVersionsInputPaginateTypeDef

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### majorVersion
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListEnvironmentTemplateVersionsInputTypeDef

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

### templateVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.EnvironmentTemplateVersionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentTemplatesInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListEnvironmentTemplatesInputTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentTemplatesOutputTypeDef

### templates
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.EnvironmentTemplateSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentsInputPaginateTypeDef

### environmentTemplates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.proton_classes.EnvironmentTemplateFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListEnvironmentsInputTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRepositoriesInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListRepositoriesInputTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListRepositoriesOutputTypeDef

### repositories
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.RepositorySummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRepositorySyncDefinitionsInputPaginateTypeDef

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


# ListRepositorySyncDefinitionsInputTypeDef

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

### syncDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.RepositorySyncDefinitionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServiceInstanceOutputsInputPaginateTypeDef

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


# ListServiceInstanceOutputsInputTypeDef

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

### outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.OutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServiceInstanceProvisionedResourcesInputPaginateTypeDef

### serviceInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListServiceInstanceProvisionedResourcesInputTypeDef

### serviceInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServiceInstanceProvisionedResourcesOutputTypeDef

### provisionedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.ProvisionedResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServiceInstancesFilterTypeDef

### key
- **Type**: typing.Optional[typing.Literal['createdAtAfter', 'createdAtBefore', 'deployedTemplateVersionStatus', 'deploymentStatus', 'environmentName', 'lastDeploymentAttemptedAtAfter', 'lastDeploymentAttemptedAtBefore', 'name', 'serviceName', 'templateName']]

### value
- **Type**: typing.Optional[str]


# ListServiceInstancesInputPaginateTypeDef

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


# ListServiceInstancesInputTypeDef

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

### serviceInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.ServiceInstanceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServicePipelineOutputsInputPaginateTypeDef

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListServicePipelineOutputsInputTypeDef

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListServicePipelineOutputsOutputTypeDef

### outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.OutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServicePipelineProvisionedResourcesInputPaginateTypeDef

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListServicePipelineProvisionedResourcesInputTypeDef

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServicePipelineProvisionedResourcesOutputTypeDef

### provisionedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.ProvisionedResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServiceTemplateVersionsInputPaginateTypeDef

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### majorVersion
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListServiceTemplateVersionsInputTypeDef

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

### templateVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.ServiceTemplateVersionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServiceTemplatesInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListServiceTemplatesInputTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListServiceTemplatesOutputTypeDef

### templates
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.ServiceTemplateSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServicesInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListServicesInputTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListServicesOutputTypeDef

### services
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.ServiceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInputPaginateTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton_classes.PaginatorConfigTypeDef]


# ListTagsForResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceOutputTypeDef

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# NotifyResourceDeploymentStatusChangeInputTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagResourceInputTypeDef

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


# UntagResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAccountSettingsInputTypeDef

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


# UpdateComponentInputTypeDef

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


# UpdateEnvironmentAccountConnectionOutputTypeDef

### environmentAccountConnection
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.EnvironmentAccountConnectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEnvironmentInputTypeDef

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


# UpdateEnvironmentTemplateInputTypeDef

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


# UpdateEnvironmentTemplateVersionInputTypeDef

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


# UpdateServiceInputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### spec
- **Type**: typing.Optional[str]


# UpdateServiceInstanceInputTypeDef

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


# UpdateServicePipelineInputTypeDef

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


# UpdateServiceSyncConfigInputTypeDef

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


# UpdateServiceTemplateInputTypeDef

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


# UpdateServiceTemplateVersionInputTypeDef

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


# UpdateTemplateSyncConfigInputTypeDef

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


