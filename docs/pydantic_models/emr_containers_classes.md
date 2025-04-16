# Emr Containers Classes

# AuthorizationConfiguration

### lakeFormationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.LakeFormationConfiguration]

### encryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.EncryptionConfiguration]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: typing.Optional[typing.Mapping[str, str]]

### configurations
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]


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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.emr_containers_classes.Configuration]]

### monitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.MonitoringConfiguration]


# ConfigurationOverridesOutput

### applicationConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_containers_classes.ConfigurationOutput]]

### monitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.MonitoringConfiguration]


# ConfigurationOverridesPaginator

### applicationConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_containers_classes.ConfigurationPaginator]]

### monitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.MonitoringConfiguration]


# ConfigurationOverridesUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.EksInfo]


# ContainerLogRotationConfiguration

### rotationSize
- **Type**: <class 'str'>
- **Required**: Yes

### maxFilesToKeep
- **Type**: <class 'int'>
- **Required**: Yes


# ContainerProvider

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateJobTemplateRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### jobTemplateData
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.JobTemplateDataUnion'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### kmsKeyArn
- **Type**: typing.Optional[str]


# CreateSecurityConfigurationRequest

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### securityConfigurationData
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.SecurityConfigurationData'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateVirtualClusterRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### containerProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ContainerProvider'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### securityConfigurationId
- **Type**: typing.Optional[str]


# Credentials

### token
- **Type**: typing.Optional[str]


# DescribeJobRunResponse

### jobRun
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.JobRun'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeJobTemplateResponse

### jobTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.JobTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeManagedEndpointResponse

### endpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.Endpoint'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSecurityConfigurationResponse

### securityConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.SecurityConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeVirtualClusterResponse

### virtualCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.VirtualCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes


# EksInfo

### namespace
- **Type**: typing.Optional[str]


# EncryptionConfiguration

### inTransitEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.InTransitEncryptionConfiguration]


# Endpoint

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EndpointPaginator

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# InTransitEncryptionConfiguration

### tlsCertificateConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.TLSCertificateConfiguration]


# JobDriver

### sparkSubmitJobDriver
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.SparkSubmitJobDriver]

### sparkSqlJobDriver
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.SparkSqlJobDriver]


# JobDriverOutput

### sparkSubmitJobDriver
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.SparkSubmitJobDriverOutput]

### sparkSqlJobDriver
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.SparkSqlJobDriver]


# JobDriverUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobRun

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobRunPaginator

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobTemplate

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobTemplateData

### executionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### releaseLabel
- **Type**: <class 'str'>
- **Required**: Yes

### jobDriver
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.JobDriver'>
- **Required**: Yes

### configurationOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.ParametricConfigurationOverrides]

### parameterConfiguration
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.emr_containers_classes.TemplateParameterConfiguration]]

### jobTags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# JobTemplateDataOutput

### executionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### releaseLabel
- **Type**: <class 'str'>
- **Required**: Yes

### jobDriver
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.JobDriverOutput'>
- **Required**: Yes

### configurationOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.ParametricConfigurationOverridesOutput]

### parameterConfiguration
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.emr_containers_classes.TemplateParameterConfiguration]]

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
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.JobDriverOutput'>
- **Required**: Yes

### configurationOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.ParametricConfigurationOverridesPaginator]

### parameterConfiguration
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.emr_containers_classes.TemplateParameterConfiguration]]

### jobTags
- **Type**: typing.Optional[typing.Dict[str, str]]


# JobTemplateDataUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobTemplatePaginator

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LakeFormationConfiguration

### authorizedSessionTagValue
- **Type**: typing.Optional[str]

### secureNamespaceInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.SecureNamespaceInfo]

### queryEngineRoleArn
- **Type**: typing.Optional[str]


# ListJobRunsRequest

### virtualClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.Timestamp]

### createdAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.Timestamp]

### name
- **Type**: typing.Optional[str]

### states
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CANCELLED', 'CANCEL_PENDING', 'COMPLETED', 'FAILED', 'PENDING', 'RUNNING', 'SUBMITTED']]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListJobRunsRequestPaginate

### virtualClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.Timestamp]

### createdAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.Timestamp]

### name
- **Type**: typing.Optional[str]

### states
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CANCELLED', 'CANCEL_PENDING', 'COMPLETED', 'FAILED', 'PENDING', 'RUNNING', 'SUBMITTED']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.PaginatorConfig]


# ListJobRunsResponse

### jobRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_containers_classes.JobRun]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobRunsResponsePaginator

### jobRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_containers_classes.JobRunPaginator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobTemplatesRequest

### createdAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.Timestamp]

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.Timestamp]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListJobTemplatesRequestPaginate

### createdAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.Timestamp]

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.Timestamp]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.PaginatorConfig]


# ListJobTemplatesResponse

### templates
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_containers_classes.JobTemplate]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobTemplatesResponsePaginator

### templates
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_containers_classes.JobTemplatePaginator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListManagedEndpointsResponse

### endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_containers_classes.Endpoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListManagedEndpointsResponsePaginator

### endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_containers_classes.EndpointPaginator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSecurityConfigurationsRequest

### createdAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.Timestamp]

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.Timestamp]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSecurityConfigurationsRequestPaginate

### createdAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.Timestamp]

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.Timestamp]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.PaginatorConfig]


# ListSecurityConfigurationsResponse

### securityConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_containers_classes.SecurityConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadata'>
- **Required**: Yes


# ListVirtualClustersRequest

### containerProviderId
- **Type**: typing.Optional[str]

### containerProviderType
- **Type**: typing.Optional[typing.Literal['EKS']]

### createdAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.Timestamp]

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.Timestamp]

### states
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ARRESTED', 'RUNNING', 'TERMINATED', 'TERMINATING']]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.Timestamp]

### createdBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.Timestamp]

### states
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ARRESTED', 'RUNNING', 'TERMINATED', 'TERMINATING']]]

### eksAccessEntryIntegrated
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.PaginatorConfig]


# ListVirtualClustersResponse

### virtualClusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_containers_classes.VirtualCluster]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.ManagedLogs]

### persistentAppUI
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### cloudWatchMonitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.CloudWatchMonitoringConfiguration]

### s3MonitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.S3MonitoringConfiguration]

### containerLogRotationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.ContainerLogRotationConfiguration]


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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.emr_containers_classes.Configuration]]

### monitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.ParametricMonitoringConfiguration]


# ParametricConfigurationOverridesOutput

### applicationConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_containers_classes.ConfigurationOutput]]

### monitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.ParametricMonitoringConfiguration]


# ParametricConfigurationOverridesPaginator

### applicationConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_containers_classes.ConfigurationPaginator]]

### monitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.ParametricMonitoringConfiguration]


# ParametricMonitoringConfiguration

### persistentAppUI
- **Type**: typing.Optional[str]

### cloudWatchMonitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.ParametricCloudWatchMonitoringConfiguration]

### s3MonitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.ParametricS3MonitoringConfiguration]


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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SecurityConfigurationData

### authorizationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.AuthorizationConfiguration]


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
- **Type**: typing.Optional[typing.Sequence[str]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.JobDriverUnion]

### configurationOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.ConfigurationOverridesUnion]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### jobTemplateId
- **Type**: typing.Optional[str]

### jobTemplateParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### retryPolicyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.RetryPolicyConfiguration]


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
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TemplateParameterConfiguration

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# VirtualCluster

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

