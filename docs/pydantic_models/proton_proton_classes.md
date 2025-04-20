# Proton Proton Classes

# AcceptEnvironmentAccountConnectionInput

### id
- **Type**: <class 'str'>
- **Required**: Yes


# AcceptEnvironmentAccountConnectionOutput

### environmentAccountConnection
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.EnvironmentAccountConnection'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# AccountSettings

### pipelineCodebuildRoleArn
- **Type**: typing.Optional[str]

### pipelineProvisioningRepository
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.RepositoryBranch]

### pipelineServiceRoleArn
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelComponentDeploymentInput

### componentName
- **Type**: <class 'str'>
- **Required**: Yes


# CancelComponentDeploymentOutput

### component
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.Component'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# CancelEnvironmentDeploymentInput

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes


# CancelEnvironmentDeploymentOutput

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.Environment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# CancelServiceInstanceDeploymentInput

### serviceInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes


# CancelServiceInstanceDeploymentOutput

### serviceInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ServiceInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# CancelServicePipelineDeploymentInput

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes


# CancelServicePipelineDeploymentOutput

### pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ServicePipeline'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# CompatibleEnvironmentTemplate

### majorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes


# CompatibleEnvironmentTemplateInput

### majorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes


# Component

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


# ComponentState

### serviceInstanceName
- **Type**: typing.Optional[str]

### serviceName
- **Type**: typing.Optional[str]

### serviceSpec
- **Type**: typing.Optional[str]

### templateFile
- **Type**: typing.Optional[str]


# ComponentSummary

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


# CountsSummary

### components
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.ResourceCountsSummary]

### environmentTemplates
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.ResourceCountsSummary]

### environments
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.ResourceCountsSummary]

### pipelines
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.ResourceCountsSummary]

### serviceInstances
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.ResourceCountsSummary]

### serviceTemplates
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.ResourceCountsSummary]

### services
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.ResourceCountsSummary]


# CreateComponentInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.Tag]]


# CreateComponentOutput

### component
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.Component'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEnvironmentAccountConnectionInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.Tag]]


# CreateEnvironmentAccountConnectionOutput

### environmentAccountConnection
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.EnvironmentAccountConnection'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEnvironmentInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.RepositoryBranchInput]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.Tag]]

### templateMinorVersion
- **Type**: typing.Optional[str]


# CreateEnvironmentOutput

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.Environment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEnvironmentTemplateInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.Tag]]


# CreateEnvironmentTemplateOutput

### environmentTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.EnvironmentTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEnvironmentTemplateVersionInput

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.TemplateVersionSourceInput'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.Tag]]


# CreateEnvironmentTemplateVersionOutput

### environmentTemplateVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.EnvironmentTemplateVersion'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRepositoryInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.Tag]]


# CreateRepositoryOutput

### repository
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.Repository'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# CreateServiceInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.Tag]]

### templateMinorVersion
- **Type**: typing.Optional[str]


# CreateServiceInstanceInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.Tag]]

### templateMajorVersion
- **Type**: typing.Optional[str]

### templateMinorVersion
- **Type**: typing.Optional[str]


# CreateServiceInstanceOutput

### serviceInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ServiceInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# CreateServiceOutput

### service
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.Service'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# CreateServiceSyncConfigInput

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


# CreateServiceSyncConfigOutput

### serviceSyncConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ServiceSyncConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# CreateServiceTemplateInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.Tag]]


# CreateServiceTemplateOutput

### serviceTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ServiceTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# CreateServiceTemplateVersionInput

### compatibleEnvironmentTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.CompatibleEnvironmentTemplateInput]
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.TemplateVersionSourceInput'>
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
- **Type**: typing.Optional[typing.List[typing.Literal['DIRECTLY_DEFINED']]]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.Tag]]


# CreateServiceTemplateVersionOutput

### serviceTemplateVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ServiceTemplateVersion'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTemplateSyncConfigInput

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


# CreateTemplateSyncConfigOutput

### templateSyncConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.TemplateSyncConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteComponentInput

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteComponentOutput

### component
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.Component'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDeploymentInput

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeploymentOutput

### deployment
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.Deployment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteEnvironmentAccountConnectionInput

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentAccountConnectionOutput

### environmentAccountConnection
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.EnvironmentAccountConnection'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteEnvironmentInput

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentOutput

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.Environment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteEnvironmentTemplateInput

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentTemplateOutput

### environmentTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.EnvironmentTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteEnvironmentTemplateVersionInput

### majorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### minorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentTemplateVersionOutput

### environmentTemplateVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.EnvironmentTemplateVersion'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteRepositoryInput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### provider
- **Type**: typing.Literal['BITBUCKET', 'GITHUB', 'GITHUB_ENTERPRISE']
- **Required**: Yes


# DeleteRepositoryOutput

### repository
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.Repository'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteServiceInput

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceOutput

### service
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.Service'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteServiceSyncConfigInput

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceSyncConfigOutput

### serviceSyncConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ServiceSyncConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteServiceTemplateInput

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceTemplateOutput

### serviceTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ServiceTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteServiceTemplateVersionInput

### majorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### minorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceTemplateVersionOutput

### serviceTemplateVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ServiceTemplateVersion'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteTemplateSyncConfigInput

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### templateType
- **Type**: typing.Literal['ENVIRONMENT', 'SERVICE']
- **Required**: Yes


# DeleteTemplateSyncConfigOutput

### templateSyncConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.TemplateSyncConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# Deployment

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.DeploymentState]

### lastAttemptedDeploymentId
- **Type**: typing.Optional[str]

### lastSucceededDeploymentId
- **Type**: typing.Optional[str]

### serviceInstanceName
- **Type**: typing.Optional[str]

### serviceName
- **Type**: typing.Optional[str]

### targetState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.DeploymentState]


# DeploymentState

### component
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.ComponentState]

### environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.EnvironmentState]

### serviceInstance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.ServiceInstanceState]

### servicePipeline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.ServicePipelineState]


# DeploymentSummary

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


# Environment

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.RepositoryBranch]

### spec
- **Type**: typing.Optional[str]


# EnvironmentAccountConnection

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


# EnvironmentAccountConnectionSummary

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


# EnvironmentState

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


# EnvironmentSummary

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


# EnvironmentTemplate

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


# EnvironmentTemplateFilter

### majorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes


# EnvironmentTemplateSummary

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


# EnvironmentTemplateVersion

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


# EnvironmentTemplateVersionSummary

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


# GetAccountSettingsOutput

### accountSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.AccountSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# GetComponentInput

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetComponentInputWait

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetComponentInputWaitExtra

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetComponentOutput

### component
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.Component'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# GetDeploymentInput

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


# GetDeploymentOutput

### deployment
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.Deployment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# GetEnvironmentAccountConnectionInput

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentAccountConnectionOutput

### environmentAccountConnection
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.EnvironmentAccountConnection'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# GetEnvironmentInput

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentInputWait

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetEnvironmentOutput

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.Environment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# GetEnvironmentTemplateInput

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentTemplateOutput

### environmentTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.EnvironmentTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# GetEnvironmentTemplateVersionInput

### majorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### minorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentTemplateVersionInputWait

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
- **Type**: <class 'NoneType'>


# GetEnvironmentTemplateVersionOutput

### environmentTemplateVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.EnvironmentTemplateVersion'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# GetRepositoryInput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### provider
- **Type**: typing.Literal['BITBUCKET', 'GITHUB', 'GITHUB_ENTERPRISE']
- **Required**: Yes


# GetRepositoryOutput

### repository
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.Repository'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# GetRepositorySyncStatusInput

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


# GetRepositorySyncStatusOutput

### latestSync
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.RepositorySyncAttempt'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourcesSummaryOutput

### counts
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.CountsSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# GetServiceInput

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceInputWait

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetServiceInputWaitExtra

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetServiceInputWaitExtraExtra

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetServiceInputWaitExtraExtraExtra

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetServiceInstanceInput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceInstanceInputWait

### name
- **Type**: <class 'str'>
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetServiceInstanceOutput

### serviceInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ServiceInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# GetServiceInstanceSyncStatusInput

### serviceInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceInstanceSyncStatusOutput

### desiredState
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.Revision'>
- **Required**: Yes

### latestSuccessfulSync
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResourceSyncAttempt'>
- **Required**: Yes

### latestSync
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResourceSyncAttempt'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# GetServiceOutput

### service
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.Service'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# GetServiceSyncBlockerSummaryInput

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### serviceInstanceName
- **Type**: typing.Optional[str]


# GetServiceSyncBlockerSummaryOutput

### serviceSyncBlockerSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ServiceSyncBlockerSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# GetServiceSyncConfigInput

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceSyncConfigOutput

### serviceSyncConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ServiceSyncConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# GetServiceTemplateInput

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceTemplateOutput

### serviceTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ServiceTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# GetServiceTemplateVersionInput

### majorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### minorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceTemplateVersionInputWait

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
- **Type**: <class 'NoneType'>


# GetServiceTemplateVersionOutput

### serviceTemplateVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ServiceTemplateVersion'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# GetTemplateSyncConfigInput

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### templateType
- **Type**: typing.Literal['ENVIRONMENT', 'SERVICE']
- **Required**: Yes


# GetTemplateSyncConfigOutput

### templateSyncConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.TemplateSyncConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# GetTemplateSyncStatusInput

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### templateType
- **Type**: typing.Literal['ENVIRONMENT', 'SERVICE']
- **Required**: Yes

### templateVersion
- **Type**: <class 'str'>
- **Required**: Yes


# GetTemplateSyncStatusOutput

### desiredState
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.Revision'>
- **Required**: Yes

### latestSuccessfulSync
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResourceSyncAttempt'>
- **Required**: Yes

### latestSync
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResourceSyncAttempt'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# ListComponentOutputsInput

### componentName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListComponentOutputsInputPaginate

### componentName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.PaginatorConfig]


# ListComponentOutputsOutput

### outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.Output]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListComponentProvisionedResourcesInput

### componentName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListComponentProvisionedResourcesInputPaginate

### componentName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.PaginatorConfig]


# ListComponentProvisionedResourcesOutput

### provisionedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.ProvisionedResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListComponentsInput

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


# ListComponentsInputPaginate

### environmentName
- **Type**: typing.Optional[str]

### serviceInstanceName
- **Type**: typing.Optional[str]

### serviceName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.PaginatorConfig]


# ListComponentsOutput

### components
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.ComponentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDeploymentsInput

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


# ListDeploymentsInputPaginate

### componentName
- **Type**: typing.Optional[str]

### environmentName
- **Type**: typing.Optional[str]

### serviceInstanceName
- **Type**: typing.Optional[str]

### serviceName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.PaginatorConfig]


# ListDeploymentsOutput

### deployments
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.DeploymentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentAccountConnectionsInput

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
- **Type**: typing.Optional[typing.List[typing.Literal['CONNECTED', 'PENDING', 'REJECTED']]]


# ListEnvironmentAccountConnectionsInputPaginate

### requestedBy
- **Type**: typing.Literal['ENVIRONMENT_ACCOUNT', 'MANAGEMENT_ACCOUNT']
- **Required**: Yes

### environmentName
- **Type**: typing.Optional[str]

### statuses
- **Type**: typing.Optional[typing.List[typing.Literal['CONNECTED', 'PENDING', 'REJECTED']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.PaginatorConfig]


# ListEnvironmentAccountConnectionsOutput

### environmentAccountConnections
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.EnvironmentAccountConnectionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentOutputsInput

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentOutputsInputPaginate

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.PaginatorConfig]


# ListEnvironmentOutputsOutput

### outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.Output]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentProvisionedResourcesInput

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentProvisionedResourcesInputPaginate

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.PaginatorConfig]


# ListEnvironmentProvisionedResourcesOutput

### provisionedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.ProvisionedResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentTemplateVersionsInput

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### majorVersion
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentTemplateVersionsInputPaginate

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### majorVersion
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.PaginatorConfig]


# ListEnvironmentTemplateVersionsOutput

### templateVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.EnvironmentTemplateVersionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentTemplatesInput

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentTemplatesInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.PaginatorConfig]


# ListEnvironmentTemplatesOutput

### templates
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.EnvironmentTemplateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentsInput

### environmentTemplates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.EnvironmentTemplateFilter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentsInputPaginate

### environmentTemplates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.EnvironmentTemplateFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.PaginatorConfig]


# ListEnvironmentsOutput

### environments
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.EnvironmentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRepositoriesInput

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListRepositoriesInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.PaginatorConfig]


# ListRepositoriesOutput

### repositories
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.RepositorySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRepositorySyncDefinitionsInput

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


# ListRepositorySyncDefinitionsInputPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.PaginatorConfig]


# ListRepositorySyncDefinitionsOutput

### syncDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.RepositorySyncDefinition]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServiceInstanceOutputsInput

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


# ListServiceInstanceOutputsInputPaginate

### serviceInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.PaginatorConfig]


# ListServiceInstanceOutputsOutput

### outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.Output]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServiceInstanceProvisionedResourcesInput

### serviceInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServiceInstanceProvisionedResourcesInputPaginate

### serviceInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.PaginatorConfig]


# ListServiceInstanceProvisionedResourcesOutput

### provisionedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.ProvisionedResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServiceInstancesFilter

### key
- **Type**: typing.Optional[typing.Literal['createdAtAfter', 'createdAtBefore', 'deployedTemplateVersionStatus', 'deploymentStatus', 'environmentName', 'lastDeploymentAttemptedAtAfter', 'lastDeploymentAttemptedAtBefore', 'name', 'serviceName', 'templateName']]

### value
- **Type**: typing.Optional[str]


# ListServiceInstancesInput

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.ListServiceInstancesFilter]]

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


# ListServiceInstancesInputPaginate

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.ListServiceInstancesFilter]]

### serviceName
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['createdAt', 'deploymentStatus', 'environmentName', 'lastDeploymentAttemptedAt', 'name', 'serviceName', 'templateName']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.PaginatorConfig]


# ListServiceInstancesOutput

### serviceInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.ServiceInstanceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServicePipelineOutputsInput

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListServicePipelineOutputsInputPaginate

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.PaginatorConfig]


# ListServicePipelineOutputsOutput

### outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.Output]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServicePipelineProvisionedResourcesInput

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServicePipelineProvisionedResourcesInputPaginate

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.PaginatorConfig]


# ListServicePipelineProvisionedResourcesOutput

### provisionedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.ProvisionedResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServiceTemplateVersionsInput

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### majorVersion
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListServiceTemplateVersionsInputPaginate

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### majorVersion
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.PaginatorConfig]


# ListServiceTemplateVersionsOutput

### templateVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.ServiceTemplateVersionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServiceTemplatesInput

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListServiceTemplatesInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.PaginatorConfig]


# ListServiceTemplatesOutput

### templates
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.ServiceTemplateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServicesInput

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListServicesInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.PaginatorConfig]


# ListServicesOutput

### services
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.ServiceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInputPaginate

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.PaginatorConfig]


# ListTagsForResourceOutput

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# NotifyResourceDeploymentStatusChangeInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: typing.Optional[str]

### outputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.Output]]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']]

### statusMessage
- **Type**: typing.Optional[str]


# Output

### key
- **Type**: typing.Optional[str]

### valueString
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProvisionedResource

### identifier
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### provisioningEngine
- **Type**: typing.Optional[typing.Literal['CLOUDFORMATION', 'TERRAFORM']]


# RejectEnvironmentAccountConnectionInput

### id
- **Type**: <class 'str'>
- **Required**: Yes


# RejectEnvironmentAccountConnectionOutput

### environmentAccountConnection
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.EnvironmentAccountConnection'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# Repository

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


# RepositoryBranch

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


# RepositoryBranchInput

### branch
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### provider
- **Type**: typing.Literal['BITBUCKET', 'GITHUB', 'GITHUB_ENTERPRISE']
- **Required**: Yes


# RepositorySummary

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


# RepositorySyncAttempt

### events
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.RepositorySyncEvent]
- **Required**: Yes

### startedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'INITIATED', 'IN_PROGRESS', 'QUEUED', 'SUCCEEDED']
- **Required**: Yes


# RepositorySyncDefinition

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


# RepositorySyncEvent

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


# ResourceCountsSummary

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


# ResourceSyncAttempt

### events
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.ResourceSyncEvent]
- **Required**: Yes

### initialRevision
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.Revision'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.Revision'>
- **Required**: Yes


# ResourceSyncEvent

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


# Revision

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


# S3ObjectSource

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes


# Service

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.ServicePipeline]

### repositoryConnectionArn
- **Type**: typing.Optional[str]

### repositoryId
- **Type**: typing.Optional[str]

### statusMessage
- **Type**: typing.Optional[str]


# ServiceInstance

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


# ServiceInstanceState

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


# ServiceInstanceSummary

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


# ServicePipeline

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


# ServicePipelineState

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


# ServiceSummary

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


# ServiceSyncBlockerSummary

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### latestBlockers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.SyncBlocker]]

### serviceInstanceName
- **Type**: typing.Optional[str]


# ServiceSyncConfig

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


# ServiceTemplate

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


# ServiceTemplateSummary

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


# ServiceTemplateVersion

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### compatibleEnvironmentTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.CompatibleEnvironmentTemplate]
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


# ServiceTemplateVersionSummary

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


# SyncBlocker

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.SyncBlockerContext]]

### resolvedAt
- **Type**: typing.Optional[datetime.datetime]

### resolvedReason
- **Type**: typing.Optional[str]


# SyncBlockerContext

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# Tag

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.Tag]
- **Required**: Yes


# TemplateSyncConfig

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


# TemplateVersionSourceInput

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.S3ObjectSource]


# UntagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAccountSettingsInput

### deletePipelineProvisioningRepository
- **Type**: typing.Optional[bool]

### pipelineCodebuildRoleArn
- **Type**: typing.Optional[str]

### pipelineProvisioningRepository
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.RepositoryBranchInput]

### pipelineServiceRoleArn
- **Type**: typing.Optional[str]


# UpdateAccountSettingsOutput

### accountSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.AccountSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateComponentInput

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


# UpdateComponentOutput

### component
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.Component'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEnvironmentAccountConnectionInput

### id
- **Type**: <class 'str'>
- **Required**: Yes

### codebuildRoleArn
- **Type**: typing.Optional[str]

### componentRoleArn
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]


# UpdateEnvironmentAccountConnectionOutput

### environmentAccountConnection
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.EnvironmentAccountConnection'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEnvironmentInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.proton.proton_classes.RepositoryBranchInput]

### spec
- **Type**: typing.Optional[str]

### templateMajorVersion
- **Type**: typing.Optional[str]

### templateMinorVersion
- **Type**: typing.Optional[str]


# UpdateEnvironmentOutput

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.Environment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEnvironmentTemplateInput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]


# UpdateEnvironmentTemplateOutput

### environmentTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.EnvironmentTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEnvironmentTemplateVersionInput

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


# UpdateEnvironmentTemplateVersionOutput

### environmentTemplateVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.EnvironmentTemplateVersion'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateServiceInput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### spec
- **Type**: typing.Optional[str]


# UpdateServiceInstanceInput

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


# UpdateServiceInstanceOutput

### serviceInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ServiceInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateServiceOutput

### service
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.Service'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateServicePipelineInput

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


# UpdateServicePipelineOutput

### pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ServicePipeline'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateServiceSyncBlockerInput

### id
- **Type**: <class 'str'>
- **Required**: Yes

### resolvedReason
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateServiceSyncBlockerOutput

### serviceInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### serviceSyncBlocker
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.SyncBlocker'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateServiceSyncConfigInput

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


# UpdateServiceSyncConfigOutput

### serviceSyncConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ServiceSyncConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateServiceTemplateInput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]


# UpdateServiceTemplateOutput

### serviceTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ServiceTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateServiceTemplateVersionInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.proton.proton_classes.CompatibleEnvironmentTemplateInput]]

### description
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DRAFT', 'PUBLISHED', 'REGISTRATION_FAILED', 'REGISTRATION_IN_PROGRESS']]

### supportedComponentSources
- **Type**: typing.Optional[typing.List[typing.Literal['DIRECTLY_DEFINED']]]


# UpdateServiceTemplateVersionOutput

### serviceTemplateVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ServiceTemplateVersion'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTemplateSyncConfigInput

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


# UpdateTemplateSyncConfigOutput

### templateSyncConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.TemplateSyncConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.proton.proton_classes.ResponseMetadata'>
- **Required**: Yes


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


