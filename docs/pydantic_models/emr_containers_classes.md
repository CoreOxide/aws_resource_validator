# Emr Containers Classes

# AuthorizationConfigurationTypeDef

### lakeFormationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.LakeFormationConfigurationTypeDef]

### encryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.EncryptionConfigurationTypeDef]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CertificateTypeDef

### certificateArn
- **Type**: typing.Optional[str]

### certificateData
- **Type**: typing.Optional[str]


# CloudWatchMonitoringConfigurationTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### logStreamNamePrefix
- **Type**: typing.Optional[str]


# ConfigurationOutputTypeDef

### classification
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.Optional[typing.Dict[str, str]]

### configurations
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# ConfigurationOverridesOutputTypeDef

### applicationConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_containers_classes.ConfigurationOutputTypeDef]]

### monitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.MonitoringConfigurationTypeDef]


# ConfigurationOverridesPaginatorTypeDef

### applicationConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_containers_classes.ConfigurationPaginatorTypeDef]]

### monitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.MonitoringConfigurationTypeDef]


# ConfigurationOverridesTypeDef

### applicationConfiguration
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.emr_containers_classes.ConfigurationTypeDef]]

### monitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.MonitoringConfigurationTypeDef]


# ConfigurationOverridesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfigurationPaginatorTypeDef

### classification
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.Optional[typing.Dict[str, str]]

### configurations
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# ConfigurationTypeDef

### classification
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.Optional[typing.Mapping[str, str]]

### configurations
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]


# ContainerInfoTypeDef

### eksInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.EksInfoTypeDef]


# ContainerLogRotationConfigurationTypeDef

### rotationSize
- **Type**: <class 'str'>
- **Required**: Yes

### maxFilesToKeep
- **Type**: <class 'int'>
- **Required**: Yes


# ContainerProviderTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateJobTemplateRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### jobTemplateData
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.JobTemplateDataUnionTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### kmsKeyArn
- **Type**: typing.Optional[str]


# CreateSecurityConfigurationRequestTypeDef

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### securityConfigurationData
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.SecurityConfigurationDataTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateVirtualClusterRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### containerProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ContainerProviderTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### securityConfigurationId
- **Type**: typing.Optional[str]


# CredentialsTypeDef

### token
- **Type**: typing.Optional[str]


# DescribeJobRunResponseTypeDef

### jobRun
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.JobRunTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeJobTemplateResponseTypeDef

### jobTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.JobTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeManagedEndpointResponseTypeDef

### endpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.EndpointTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSecurityConfigurationResponseTypeDef

### securityConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.SecurityConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeVirtualClusterResponseTypeDef

### virtualCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.VirtualClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EksInfoTypeDef

### namespace
- **Type**: typing.Optional[str]


# EncryptionConfigurationTypeDef

### inTransitEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.InTransitEncryptionConfigurationTypeDef]


# EndpointPaginatorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EndpointTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetManagedEndpointSessionCredentialsRequestTypeDef

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


# InTransitEncryptionConfigurationTypeDef

### tlsCertificateConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.TLSCertificateConfigurationTypeDef]


# JobDriverOutputTypeDef

### sparkSubmitJobDriver
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.SparkSubmitJobDriverOutputTypeDef]

### sparkSqlJobDriver
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.SparkSqlJobDriverTypeDef]


# JobDriverTypeDef

### sparkSubmitJobDriver
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.SparkSubmitJobDriverTypeDef]

### sparkSqlJobDriver
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.SparkSqlJobDriverTypeDef]


# JobDriverUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobRunPaginatorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobRunTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobTemplateDataOutputTypeDef

### executionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### releaseLabel
- **Type**: <class 'str'>
- **Required**: Yes

### jobDriver
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.JobDriverOutputTypeDef'>
- **Required**: Yes

### configurationOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.ParametricConfigurationOverridesOutputTypeDef]

### parameterConfiguration
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.emr_containers_classes.TemplateParameterConfigurationTypeDef]]

### jobTags
- **Type**: typing.Optional[typing.Dict[str, str]]


# JobTemplateDataPaginatorTypeDef

### executionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### releaseLabel
- **Type**: <class 'str'>
- **Required**: Yes

### jobDriver
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.JobDriverOutputTypeDef'>
- **Required**: Yes

### configurationOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.ParametricConfigurationOverridesPaginatorTypeDef]

### parameterConfiguration
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.emr_containers_classes.TemplateParameterConfigurationTypeDef]]

### jobTags
- **Type**: typing.Optional[typing.Dict[str, str]]


# JobTemplateDataTypeDef

### executionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### releaseLabel
- **Type**: <class 'str'>
- **Required**: Yes

### jobDriver
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.JobDriverTypeDef'>
- **Required**: Yes

### configurationOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.ParametricConfigurationOverridesTypeDef]

### parameterConfiguration
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.emr_containers_classes.TemplateParameterConfigurationTypeDef]]

### jobTags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# JobTemplateDataUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobTemplatePaginatorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobTemplateTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LakeFormationConfigurationTypeDef

### authorizedSessionTagValue
- **Type**: typing.Optional[str]

### secureNamespaceInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.SecureNamespaceInfoTypeDef]

### queryEngineRoleArn
- **Type**: typing.Optional[str]


# ListJobRunsRequestPaginateTypeDef

### virtualClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.TimestampTypeDef]

### createdAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.TimestampTypeDef]

### name
- **Type**: typing.Optional[str]

### states
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CANCELLED', 'CANCEL_PENDING', 'COMPLETED', 'FAILED', 'PENDING', 'RUNNING', 'SUBMITTED']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.PaginatorConfigTypeDef]


# ListJobRunsRequestTypeDef

### virtualClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.TimestampTypeDef]

### createdAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.TimestampTypeDef]

### name
- **Type**: typing.Optional[str]

### states
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CANCELLED', 'CANCEL_PENDING', 'COMPLETED', 'FAILED', 'PENDING', 'RUNNING', 'SUBMITTED']]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListJobRunsResponsePaginatorTypeDef

### jobRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_containers_classes.JobRunPaginatorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobRunsResponseTypeDef

### jobRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_containers_classes.JobRunTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobTemplatesRequestPaginateTypeDef

### createdAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.TimestampTypeDef]

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.TimestampTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.PaginatorConfigTypeDef]


# ListJobTemplatesRequestTypeDef

### createdAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.TimestampTypeDef]

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.TimestampTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListJobTemplatesResponsePaginatorTypeDef

### templates
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_containers_classes.JobTemplatePaginatorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobTemplatesResponseTypeDef

### templates
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_containers_classes.JobTemplateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListManagedEndpointsResponsePaginatorTypeDef

### endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_containers_classes.EndpointPaginatorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListManagedEndpointsResponseTypeDef

### endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_containers_classes.EndpointTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSecurityConfigurationsRequestPaginateTypeDef

### createdAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.TimestampTypeDef]

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.TimestampTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.PaginatorConfigTypeDef]


# ListSecurityConfigurationsRequestTypeDef

### createdAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.TimestampTypeDef]

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.TimestampTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSecurityConfigurationsResponseTypeDef

### securityConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_containers_classes.SecurityConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVirtualClustersRequestPaginateTypeDef

### containerProviderId
- **Type**: typing.Optional[str]

### containerProviderType
- **Type**: typing.Optional[typing.Literal['EKS']]

### createdAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.TimestampTypeDef]

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.TimestampTypeDef]

### states
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ARRESTED', 'RUNNING', 'TERMINATED', 'TERMINATING']]]

### eksAccessEntryIntegrated
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.PaginatorConfigTypeDef]


# ListVirtualClustersRequestTypeDef

### containerProviderId
- **Type**: typing.Optional[str]

### containerProviderType
- **Type**: typing.Optional[typing.Literal['EKS']]

### createdAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.TimestampTypeDef]

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.TimestampTypeDef]

### states
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ARRESTED', 'RUNNING', 'TERMINATED', 'TERMINATING']]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### eksAccessEntryIntegrated
- **Type**: typing.Optional[bool]


# ListVirtualClustersResponseTypeDef

### virtualClusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_containers_classes.VirtualClusterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ManagedLogsTypeDef

### allowAWSToRetainLogs
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### encryptionKeyArn
- **Type**: typing.Optional[str]


# MonitoringConfigurationTypeDef

### managedLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.ManagedLogsTypeDef]

### persistentAppUI
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### cloudWatchMonitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.CloudWatchMonitoringConfigurationTypeDef]

### s3MonitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.S3MonitoringConfigurationTypeDef]

### containerLogRotationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.ContainerLogRotationConfigurationTypeDef]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParametricCloudWatchMonitoringConfigurationTypeDef

### logGroupName
- **Type**: typing.Optional[str]

### logStreamNamePrefix
- **Type**: typing.Optional[str]


# ParametricConfigurationOverridesOutputTypeDef

### applicationConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_containers_classes.ConfigurationOutputTypeDef]]

### monitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.ParametricMonitoringConfigurationTypeDef]


# ParametricConfigurationOverridesPaginatorTypeDef

### applicationConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_containers_classes.ConfigurationPaginatorTypeDef]]

### monitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.ParametricMonitoringConfigurationTypeDef]


# ParametricConfigurationOverridesTypeDef

### applicationConfiguration
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.emr_containers_classes.ConfigurationTypeDef]]

### monitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.ParametricMonitoringConfigurationTypeDef]


# ParametricMonitoringConfigurationTypeDef

### persistentAppUI
- **Type**: typing.Optional[str]

### cloudWatchMonitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.ParametricCloudWatchMonitoringConfigurationTypeDef]

### s3MonitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.ParametricS3MonitoringConfigurationTypeDef]


# ParametricS3MonitoringConfigurationTypeDef

### logUri
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


# RetryPolicyConfigurationTypeDef

### maxAttempts
- **Type**: <class 'int'>
- **Required**: Yes


# RetryPolicyExecutionTypeDef

### currentAttemptCount
- **Type**: <class 'int'>
- **Required**: Yes


# S3MonitoringConfigurationTypeDef

### logUri
- **Type**: <class 'str'>
- **Required**: Yes


# SecureNamespaceInfoTypeDef

### clusterId
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[str]


# SecurityConfigurationDataTypeDef

### authorizationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.AuthorizationConfigurationTypeDef]


# SecurityConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SparkSqlJobDriverTypeDef

### entryPoint
- **Type**: typing.Optional[str]

### sparkSqlParameters
- **Type**: typing.Optional[str]


# SparkSubmitJobDriverOutputTypeDef

### entryPoint
- **Type**: <class 'str'>
- **Required**: Yes

### entryPointArguments
- **Type**: typing.Optional[typing.List[str]]

### sparkSubmitParameters
- **Type**: typing.Optional[str]


# SparkSubmitJobDriverTypeDef

### entryPoint
- **Type**: <class 'str'>
- **Required**: Yes

### entryPointArguments
- **Type**: typing.Optional[typing.Sequence[str]]

### sparkSubmitParameters
- **Type**: typing.Optional[str]


# StartJobRunRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.JobDriverUnionTypeDef]

### configurationOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.ConfigurationOverridesUnionTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### jobTemplateId
- **Type**: typing.Optional[str]

### jobTemplateParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### retryPolicyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.RetryPolicyConfigurationTypeDef]


# TLSCertificateConfigurationTypeDef

### certificateProviderType
- **Type**: typing.Optional[typing.Literal['PEM']]

### publicCertificateSecretArn
- **Type**: typing.Optional[str]

### privateCertificateSecretArn
- **Type**: typing.Optional[str]


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TemplateParameterConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# VirtualClusterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

