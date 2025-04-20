# Emr Containers Emr Containers Classes

# AuthorizationConfiguration

### lakeFormationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.LakeFormationConfiguration]

### encryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.EncryptionConfiguration]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelJobRunRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### virtualClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelJobRunResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### virtualClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes


# Certificate

### certificateArn
- **Type**: typing.Optional[str]

### certificateData
- **Type**: typing.Optional[str]


# CloudWatchMonitoringConfiguration

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### logStreamNamePrefix
- **Type**: typing.Optional[str]


# Configuration

### classification
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.Optional[typing.Dict[str, str]]

### configurations
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# ConfigurationOutput

### classification
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.Optional[typing.Dict[str, str]]

### configurations
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# ConfigurationOverrides

### applicationConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.Configuration]]

### monitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.MonitoringConfiguration]


# ConfigurationOverridesOutput

### applicationConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ConfigurationOutput]]

### monitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.MonitoringConfiguration]


# ConfigurationOverridesPaginator

### applicationConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ConfigurationPaginator]]

### monitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.MonitoringConfiguration]


# ConfigurationPaginator

### classification
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.Optional[typing.Dict[str, str]]

### configurations
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# ContainerInfo

### eksInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.EksInfo]


# ContainerLogRotationConfiguration

### rotationSize
- **Type**: <class 'str'>
- **Required**: Yes

### maxFilesToKeep
- **Type**: <class 'int'>
- **Required**: Yes


# ContainerProvider

### type
- **Type**: typing.Literal['EKS']
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### info
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ContainerInfo]


# CreateJobTemplateRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### jobTemplateData
- **Type**: typing.Union[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.JobTemplateData, aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.JobTemplateDataOutput]
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### kmsKeyArn
- **Type**: typing.Optional[str]


# CreateJobTemplateResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes


# CreateManagedEndpointRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### virtualClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### releaseLabel
- **Type**: <class 'str'>
- **Required**: Yes

### executionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### certificateArn
- **Type**: typing.Optional[str]

### configurationOverrides
- **Type**: typing.Union[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ConfigurationOverrides, aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ConfigurationOverridesOutput, NoneType]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateManagedEndpointResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### virtualClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSecurityConfigurationRequest

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### securityConfigurationData
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.SecurityConfigurationData'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateSecurityConfigurationResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVirtualClusterRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### containerProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ContainerProvider'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### securityConfigurationId
- **Type**: typing.Optional[str]


# CreateVirtualClusterResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes


# Credentials

### token
- **Type**: typing.Optional[str]


# DeleteJobTemplateRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteJobTemplateResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteManagedEndpointRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### virtualClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteManagedEndpointResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### virtualClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteVirtualClusterRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVirtualClusterResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeJobRunRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### virtualClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeJobRunResponse

### jobRun
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.JobRun'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeJobTemplateRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeJobTemplateResponse

### jobTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.JobTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeManagedEndpointRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### virtualClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeManagedEndpointResponse

### endpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.Endpoint'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSecurityConfigurationRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSecurityConfigurationResponse

### securityConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.SecurityConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeVirtualClusterRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeVirtualClusterResponse

### virtualCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.VirtualCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes


# EksInfo

### namespace
- **Type**: typing.Optional[str]


# EncryptionConfiguration

### inTransitEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.InTransitEncryptionConfiguration]


# Endpoint

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### virtualClusterId
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'TERMINATED', 'TERMINATED_WITH_ERRORS', 'TERMINATING']]

### releaseLabel
- **Type**: typing.Optional[str]

### executionRoleArn
- **Type**: typing.Optional[str]

### certificateArn
- **Type**: typing.Optional[str]

### certificateAuthority
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.Certificate]

### configurationOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ConfigurationOverridesOutput]

### serverUrl
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### securityGroup
- **Type**: typing.Optional[str]

### subnetIds
- **Type**: typing.Optional[typing.List[str]]

### stateDetails
- **Type**: typing.Optional[str]

### failureReason
- **Type**: typing.Optional[typing.Literal['CLUSTER_UNAVAILABLE', 'INTERNAL_ERROR', 'USER_ERROR', 'VALIDATION_ERROR']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# EndpointPaginator

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### virtualClusterId
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'TERMINATED', 'TERMINATED_WITH_ERRORS', 'TERMINATING']]

### releaseLabel
- **Type**: typing.Optional[str]

### executionRoleArn
- **Type**: typing.Optional[str]

### certificateArn
- **Type**: typing.Optional[str]

### certificateAuthority
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.Certificate]

### configurationOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ConfigurationOverridesPaginator]

### serverUrl
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### securityGroup
- **Type**: typing.Optional[str]

### subnetIds
- **Type**: typing.Optional[typing.List[str]]

### stateDetails
- **Type**: typing.Optional[str]

### failureReason
- **Type**: typing.Optional[typing.Literal['CLUSTER_UNAVAILABLE', 'INTERNAL_ERROR', 'USER_ERROR', 'VALIDATION_ERROR']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# GetManagedEndpointSessionCredentialsRequest

### endpointIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### virtualClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### executionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### credentialType
- **Type**: <class 'str'>
- **Required**: Yes

### durationInSeconds
- **Type**: typing.Optional[int]

### logContext
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


# GetManagedEndpointSessionCredentialsResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.Credentials'>
- **Required**: Yes

### expiresAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes


# InTransitEncryptionConfiguration

### tlsCertificateConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.TLSCertificateConfiguration]


# JobDriver

### sparkSubmitJobDriver
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.SparkSubmitJobDriver]

### sparkSqlJobDriver
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.SparkSqlJobDriver]


# JobDriverOutput

### sparkSubmitJobDriver
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.SparkSubmitJobDriverOutput]

### sparkSqlJobDriver
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.SparkSqlJobDriver]


# JobRun

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### virtualClusterId
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCEL_PENDING', 'COMPLETED', 'FAILED', 'PENDING', 'RUNNING', 'SUBMITTED']]

### clientToken
- **Type**: typing.Optional[str]

### executionRoleArn
- **Type**: typing.Optional[str]

### releaseLabel
- **Type**: typing.Optional[str]

### configurationOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ConfigurationOverridesOutput]

### jobDriver
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.JobDriverOutput]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### finishedAt
- **Type**: typing.Optional[datetime.datetime]

### stateDetails
- **Type**: typing.Optional[str]

### failureReason
- **Type**: typing.Optional[typing.Literal['CLUSTER_UNAVAILABLE', 'INTERNAL_ERROR', 'USER_ERROR', 'VALIDATION_ERROR']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### retryPolicyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.RetryPolicyConfiguration]

### retryPolicyExecution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.RetryPolicyExecution]


# JobRunPaginator

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### virtualClusterId
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCEL_PENDING', 'COMPLETED', 'FAILED', 'PENDING', 'RUNNING', 'SUBMITTED']]

### clientToken
- **Type**: typing.Optional[str]

### executionRoleArn
- **Type**: typing.Optional[str]

### releaseLabel
- **Type**: typing.Optional[str]

### configurationOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ConfigurationOverridesPaginator]

### jobDriver
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.JobDriverOutput]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### finishedAt
- **Type**: typing.Optional[datetime.datetime]

### stateDetails
- **Type**: typing.Optional[str]

### failureReason
- **Type**: typing.Optional[typing.Literal['CLUSTER_UNAVAILABLE', 'INTERNAL_ERROR', 'USER_ERROR', 'VALIDATION_ERROR']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### retryPolicyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.RetryPolicyConfiguration]

### retryPolicyExecution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.RetryPolicyExecution]


# JobTemplate

### jobTemplateData
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.JobTemplateDataOutput'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### kmsKeyArn
- **Type**: typing.Optional[str]

### decryptionError
- **Type**: typing.Optional[str]


# JobTemplateData

### executionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### releaseLabel
- **Type**: <class 'str'>
- **Required**: Yes

### jobDriver
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.JobDriver'>
- **Required**: Yes

### configurationOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ParametricConfigurationOverrides]

### parameterConfiguration
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.TemplateParameterConfiguration]]

### jobTags
- **Type**: typing.Optional[typing.Dict[str, str]]


# JobTemplateDataOutput

### executionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### releaseLabel
- **Type**: <class 'str'>
- **Required**: Yes

### jobDriver
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.JobDriverOutput'>
- **Required**: Yes

### configurationOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ParametricConfigurationOverridesOutput]

### parameterConfiguration
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.TemplateParameterConfiguration]]

### jobTags
- **Type**: typing.Optional[typing.Dict[str, str]]


# JobTemplateDataPaginator

### executionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### releaseLabel
- **Type**: <class 'str'>
- **Required**: Yes

### jobDriver
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.JobDriverOutput'>
- **Required**: Yes

### configurationOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ParametricConfigurationOverridesPaginator]

### parameterConfiguration
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.TemplateParameterConfiguration]]

### jobTags
- **Type**: typing.Optional[typing.Dict[str, str]]


# JobTemplatePaginator

### jobTemplateData
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.JobTemplateDataPaginator'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### kmsKeyArn
- **Type**: typing.Optional[str]

### decryptionError
- **Type**: typing.Optional[str]


# LakeFormationConfiguration

### authorizedSessionTagValue
- **Type**: typing.Optional[str]

### secureNamespaceInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.SecureNamespaceInfo]

### queryEngineRoleArn
- **Type**: typing.Optional[str]


# ListJobRunsRequest

### virtualClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### name
- **Type**: typing.Optional[str]

### states
- **Type**: typing.Optional[typing.List[typing.Literal['CANCELLED', 'CANCEL_PENDING', 'COMPLETED', 'FAILED', 'PENDING', 'RUNNING', 'SUBMITTED']]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListJobRunsRequestPaginate

### virtualClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### name
- **Type**: typing.Optional[str]

### states
- **Type**: typing.Optional[typing.List[typing.Literal['CANCELLED', 'CANCEL_PENDING', 'COMPLETED', 'FAILED', 'PENDING', 'RUNNING', 'SUBMITTED']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.PaginatorConfig]


# ListJobRunsResponse

### jobRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.JobRun]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobRunsResponsePaginator

### jobRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.JobRunPaginator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobTemplatesRequest

### createdAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListJobTemplatesRequestPaginate

### createdAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.PaginatorConfig]


# ListJobTemplatesResponse

### templates
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.JobTemplate]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobTemplatesResponsePaginator

### templates
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.JobTemplatePaginator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListManagedEndpointsRequest

### virtualClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### types
- **Type**: typing.Optional[typing.List[str]]

### states
- **Type**: typing.Optional[typing.List[typing.Literal['ACTIVE', 'CREATING', 'TERMINATED', 'TERMINATED_WITH_ERRORS', 'TERMINATING']]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListManagedEndpointsRequestPaginate

### virtualClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### types
- **Type**: typing.Optional[typing.List[str]]

### states
- **Type**: typing.Optional[typing.List[typing.Literal['ACTIVE', 'CREATING', 'TERMINATED', 'TERMINATED_WITH_ERRORS', 'TERMINATING']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.PaginatorConfig]


# ListManagedEndpointsResponse

### endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.Endpoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListManagedEndpointsResponsePaginator

### endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.EndpointPaginator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSecurityConfigurationsRequest

### createdAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSecurityConfigurationsRequestPaginate

### createdAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.PaginatorConfig]


# ListSecurityConfigurationsResponse

### securityConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.SecurityConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes


# ListVirtualClustersRequest

### containerProviderId
- **Type**: typing.Optional[str]

### containerProviderType
- **Type**: typing.Optional[typing.Literal['EKS']]

### createdAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### states
- **Type**: typing.Optional[typing.List[typing.Literal['ARRESTED', 'RUNNING', 'TERMINATED', 'TERMINATING']]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### eksAccessEntryIntegrated
- **Type**: typing.Optional[bool]


# ListVirtualClustersRequestPaginate

### containerProviderId
- **Type**: typing.Optional[str]

### containerProviderType
- **Type**: typing.Optional[typing.Literal['EKS']]

### createdAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### states
- **Type**: typing.Optional[typing.List[typing.Literal['ARRESTED', 'RUNNING', 'TERMINATED', 'TERMINATING']]]

### eksAccessEntryIntegrated
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.PaginatorConfig]


# ListVirtualClustersResponse

### virtualClusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.VirtualCluster]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ManagedLogs

### allowAWSToRetainLogs
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### encryptionKeyArn
- **Type**: typing.Optional[str]


# MonitoringConfiguration

### managedLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ManagedLogs]

### persistentAppUI
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### cloudWatchMonitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.CloudWatchMonitoringConfiguration]

### s3MonitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.S3MonitoringConfiguration]

### containerLogRotationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ContainerLogRotationConfiguration]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParametricCloudWatchMonitoringConfiguration

### logGroupName
- **Type**: typing.Optional[str]

### logStreamNamePrefix
- **Type**: typing.Optional[str]


# ParametricConfigurationOverrides

### applicationConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.Configuration]]

### monitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ParametricMonitoringConfiguration]


# ParametricConfigurationOverridesOutput

### applicationConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ConfigurationOutput]]

### monitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ParametricMonitoringConfiguration]


# ParametricConfigurationOverridesPaginator

### applicationConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ConfigurationPaginator]]

### monitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ParametricMonitoringConfiguration]


# ParametricMonitoringConfiguration

### persistentAppUI
- **Type**: typing.Optional[str]

### cloudWatchMonitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ParametricCloudWatchMonitoringConfiguration]

### s3MonitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ParametricS3MonitoringConfiguration]


# ParametricS3MonitoringConfiguration

### logUri
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


# RetryPolicyConfiguration

### maxAttempts
- **Type**: <class 'int'>
- **Required**: Yes


# RetryPolicyExecution

### currentAttemptCount
- **Type**: <class 'int'>
- **Required**: Yes


# S3MonitoringConfiguration

### logUri
- **Type**: <class 'str'>
- **Required**: Yes


# SecureNamespaceInfo

### clusterId
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[str]


# SecurityConfiguration

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### securityConfigurationData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.SecurityConfigurationData]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# SecurityConfigurationData

### authorizationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.AuthorizationConfiguration]


# SparkSqlJobDriver

### entryPoint
- **Type**: typing.Optional[str]

### sparkSqlParameters
- **Type**: typing.Optional[str]


# SparkSubmitJobDriver

### entryPoint
- **Type**: <class 'str'>
- **Required**: Yes

### entryPointArguments
- **Type**: typing.Optional[typing.List[str]]

### sparkSubmitParameters
- **Type**: typing.Optional[str]


# SparkSubmitJobDriverOutput

### entryPoint
- **Type**: <class 'str'>
- **Required**: Yes

### entryPointArguments
- **Type**: typing.Optional[typing.List[str]]

### sparkSubmitParameters
- **Type**: typing.Optional[str]


# StartJobRunRequest

### virtualClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### executionRoleArn
- **Type**: typing.Optional[str]

### releaseLabel
- **Type**: typing.Optional[str]

### jobDriver
- **Type**: typing.Union[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.JobDriver, aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.JobDriverOutput, NoneType]

### configurationOverrides
- **Type**: typing.Union[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ConfigurationOverrides, aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ConfigurationOverridesOutput, NoneType]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### jobTemplateId
- **Type**: typing.Optional[str]

### jobTemplateParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### retryPolicyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.RetryPolicyConfiguration]


# StartJobRunResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### virtualClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes


# TLSCertificateConfiguration

### certificateProviderType
- **Type**: typing.Optional[typing.Literal['PEM']]

### publicCertificateSecretArn
- **Type**: typing.Optional[str]

### privateCertificateSecretArn
- **Type**: typing.Optional[str]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TemplateParameterConfiguration

### type
- **Type**: typing.Optional[typing.Literal['NUMBER', 'STRING']]

### defaultValue
- **Type**: typing.Optional[str]


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# VirtualCluster

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['ARRESTED', 'RUNNING', 'TERMINATED', 'TERMINATING']]

### containerProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers.emr_containers_classes.ContainerProvider]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### securityConfigurationId
- **Type**: typing.Optional[str]


