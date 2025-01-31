# Emr Containers Classes

# AuthorizationConfigurationTypeDef

### lakeFormationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.LakeFormationConfigurationTypeDef]

### encryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.EncryptionConfigurationTypeDef]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelJobRunRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### virtualClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelJobRunResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### virtualClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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
- **Type**: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]


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

### type
- **Type**: typing.Literal['EKS']
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### info
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.ContainerInfoTypeDef]


# CreateJobTemplateRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### jobTemplateData
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.JobTemplateDataTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### kmsKeyArn
- **Type**: typing.Optional[str]


# CreateJobTemplateResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateManagedEndpointRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.ConfigurationOverridesTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateManagedEndpointResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSecurityConfigurationRequestRequestTypeDef

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


# CreateSecurityConfigurationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVirtualClusterRequestRequestTypeDef

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


# CreateVirtualClusterResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CredentialsTypeDef

### token
- **Type**: typing.Optional[str]


# DeleteJobTemplateRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteJobTemplateResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteManagedEndpointRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### virtualClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteManagedEndpointResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### virtualClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteVirtualClusterRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVirtualClusterResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeJobRunRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### virtualClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeJobRunResponseTypeDef

### jobRun
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.JobRunTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeJobTemplateRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeJobTemplateResponseTypeDef

### jobTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.JobTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeManagedEndpointRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### virtualClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeManagedEndpointResponseTypeDef

### endpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.EndpointTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSecurityConfigurationRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSecurityConfigurationResponseTypeDef

### securityConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.SecurityConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeVirtualClusterRequestRequestTypeDef

### id
- **Type**: <class 'str'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.CertificateTypeDef]

### configurationOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.ConfigurationOverridesPaginatorTypeDef]

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


# EndpointTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.CertificateTypeDef]

### configurationOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.ConfigurationOverridesTypeDef]

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


# GetManagedEndpointSessionCredentialsRequestRequestTypeDef

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


# GetManagedEndpointSessionCredentialsResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.CredentialsTypeDef'>
- **Required**: Yes

### expiresAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InTransitEncryptionConfigurationTypeDef

### tlsCertificateConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.TLSCertificateConfigurationTypeDef]


# JobDriverPaginatorTypeDef

### sparkSubmitJobDriver
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.SparkSubmitJobDriverPaginatorTypeDef]

### sparkSqlJobDriver
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.SparkSqlJobDriverTypeDef]


# JobDriverTypeDef

### sparkSubmitJobDriver
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.SparkSubmitJobDriverTypeDef]

### sparkSqlJobDriver
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.SparkSqlJobDriverTypeDef]


# JobRunPaginatorTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.ConfigurationOverridesPaginatorTypeDef]

### jobDriver
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.JobDriverPaginatorTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.RetryPolicyConfigurationTypeDef]

### retryPolicyExecution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.RetryPolicyExecutionTypeDef]


# JobRunTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.ConfigurationOverridesTypeDef]

### jobDriver
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.JobDriverTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.RetryPolicyConfigurationTypeDef]

### retryPolicyExecution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.RetryPolicyExecutionTypeDef]


# JobTemplateDataPaginatorTypeDef

### executionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### releaseLabel
- **Type**: <class 'str'>
- **Required**: Yes

### jobDriver
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.JobDriverPaginatorTypeDef'>
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


# JobTemplatePaginatorTypeDef

### jobTemplateData
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.JobTemplateDataPaginatorTypeDef'>
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


# JobTemplateTypeDef

### jobTemplateData
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.JobTemplateDataTypeDef'>
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


# LakeFormationConfigurationTypeDef

### authorizedSessionTagValue
- **Type**: typing.Optional[str]

### secureNamespaceInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.SecureNamespaceInfoTypeDef]

### queryEngineRoleArn
- **Type**: typing.Optional[str]


# ListJobRunsRequestListJobRunsPaginateTypeDef

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
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CANCELLED', 'CANCEL_PENDING', 'COMPLETED', 'FAILED', 'PENDING', 'RUNNING', 'SUBMITTED']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.PaginatorConfigTypeDef]


# ListJobRunsRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CANCELLED', 'CANCEL_PENDING', 'COMPLETED', 'FAILED', 'PENDING', 'RUNNING', 'SUBMITTED']]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListJobRunsResponsePaginatorTypeDef

### jobRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_containers_classes.JobRunPaginatorTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListJobRunsResponseTypeDef

### jobRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_containers_classes.JobRunTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListJobTemplatesRequestListJobTemplatesPaginateTypeDef

### createdAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.PaginatorConfigTypeDef]


# ListJobTemplatesRequestRequestTypeDef

### createdAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListJobTemplatesResponsePaginatorTypeDef

### templates
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_containers_classes.JobTemplatePaginatorTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListJobTemplatesResponseTypeDef

### templates
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_containers_classes.JobTemplateTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListManagedEndpointsRequestListManagedEndpointsPaginateTypeDef

### virtualClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### types
- **Type**: typing.Optional[typing.Sequence[str]]

### states
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ACTIVE', 'CREATING', 'TERMINATED', 'TERMINATED_WITH_ERRORS', 'TERMINATING']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.PaginatorConfigTypeDef]


# ListManagedEndpointsRequestRequestTypeDef

### virtualClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### types
- **Type**: typing.Optional[typing.Sequence[str]]

### states
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ACTIVE', 'CREATING', 'TERMINATED', 'TERMINATED_WITH_ERRORS', 'TERMINATING']]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListManagedEndpointsResponsePaginatorTypeDef

### endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_containers_classes.EndpointPaginatorTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListManagedEndpointsResponseTypeDef

### endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_containers_classes.EndpointTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSecurityConfigurationsRequestListSecurityConfigurationsPaginateTypeDef

### createdAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.PaginatorConfigTypeDef]


# ListSecurityConfigurationsRequestRequestTypeDef

### createdAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSecurityConfigurationsResponseTypeDef

### securityConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_containers_classes.SecurityConfigurationTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVirtualClustersRequestListVirtualClustersPaginateTypeDef

### containerProviderId
- **Type**: typing.Optional[str]

### containerProviderType
- **Type**: typing.Optional[typing.Literal['EKS']]

### createdAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### states
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ARRESTED', 'RUNNING', 'TERMINATED', 'TERMINATING']]]

### eksAccessEntryIntegrated
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.PaginatorConfigTypeDef]


# ListVirtualClustersRequestRequestTypeDef

### containerProviderId
- **Type**: typing.Optional[str]

### containerProviderType
- **Type**: typing.Optional[typing.Literal['EKS']]

### createdAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MonitoringConfigurationTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.SecurityConfigurationDataTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# SparkSqlJobDriverTypeDef

### entryPoint
- **Type**: typing.Optional[str]

### sparkSqlParameters
- **Type**: typing.Optional[str]


# SparkSubmitJobDriverPaginatorTypeDef

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


# StartJobRunRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.JobDriverTypeDef]

### configurationOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.ConfigurationOverridesTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### jobTemplateId
- **Type**: typing.Optional[str]

### jobTemplateParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### retryPolicyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.RetryPolicyConfigurationTypeDef]


# StartJobRunResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_containers_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TLSCertificateConfigurationTypeDef

### certificateProviderType
- **Type**: typing.Optional[typing.Literal['PEM']]

### publicCertificateSecretArn
- **Type**: typing.Optional[str]

### privateCertificateSecretArn
- **Type**: typing.Optional[str]


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TemplateParameterConfigurationTypeDef

### type
- **Type**: typing.Optional[typing.Literal['NUMBER', 'STRING']]

### defaultValue
- **Type**: typing.Optional[str]


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# VirtualClusterTypeDef

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['ARRESTED', 'RUNNING', 'TERMINATED', 'TERMINATING']]

### containerProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_containers_classes.ContainerProviderTypeDef]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### securityConfigurationId
- **Type**: typing.Optional[str]


