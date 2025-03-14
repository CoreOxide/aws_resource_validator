# Apprunner Classes

# AssociateCustomDomainRequestTypeDef

### ServiceArn
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### EnableWWWSubdomain
- **Type**: typing.Optional[bool]


# AssociateCustomDomainResponseTypeDef

### DNSTarget
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceArn
- **Type**: <class 'str'>
- **Required**: Yes

### CustomDomain
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.CustomDomainTypeDef'>
- **Required**: Yes

### VpcDNSTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.apprunner_classes.VpcDNSTargetTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AuthenticationConfigurationTypeDef

### ConnectionArn
- **Type**: typing.Optional[str]

### AccessRoleArn
- **Type**: typing.Optional[str]


# AutoScalingConfigurationSummaryTypeDef

### AutoScalingConfigurationArn
- **Type**: typing.Optional[str]

### AutoScalingConfigurationName
- **Type**: typing.Optional[str]

### AutoScalingConfigurationRevision
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### HasAssociatedService
- **Type**: typing.Optional[bool]

### IsDefault
- **Type**: typing.Optional[bool]


# AutoScalingConfigurationTypeDef

### AutoScalingConfigurationArn
- **Type**: typing.Optional[str]

### AutoScalingConfigurationName
- **Type**: typing.Optional[str]

### AutoScalingConfigurationRevision
- **Type**: typing.Optional[int]

### Latest
- **Type**: typing.Optional[bool]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### MaxConcurrency
- **Type**: typing.Optional[int]

### MinSize
- **Type**: typing.Optional[int]

### MaxSize
- **Type**: typing.Optional[int]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### DeletedAt
- **Type**: typing.Optional[datetime.datetime]

### HasAssociatedService
- **Type**: typing.Optional[bool]

### IsDefault
- **Type**: typing.Optional[bool]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CertificateValidationRecordTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CodeConfigurationOutputTypeDef

### ConfigurationSource
- **Type**: typing.Literal['API', 'REPOSITORY']
- **Required**: Yes

### CodeConfigurationValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apprunner_classes.CodeConfigurationValuesOutputTypeDef]


# CodeConfigurationTypeDef

### ConfigurationSource
- **Type**: typing.Literal['API', 'REPOSITORY']
- **Required**: Yes

### CodeConfigurationValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apprunner_classes.CodeConfigurationValuesTypeDef]


# CodeConfigurationValuesOutputTypeDef

### Runtime
- **Type**: typing.Literal['CORRETTO_11', 'CORRETTO_8', 'DOTNET_6', 'GO_1', 'NODEJS_12', 'NODEJS_14', 'NODEJS_16', 'NODEJS_18', 'PHP_81', 'PYTHON_3', 'PYTHON_311', 'RUBY_31']
- **Required**: Yes

### BuildCommand
- **Type**: typing.Optional[str]

### StartCommand
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[str]

### RuntimeEnvironmentVariables
- **Type**: typing.Optional[typing.Dict[str, str]]

### RuntimeEnvironmentSecrets
- **Type**: typing.Optional[typing.Dict[str, str]]


# CodeConfigurationValuesTypeDef

### Runtime
- **Type**: typing.Literal['CORRETTO_11', 'CORRETTO_8', 'DOTNET_6', 'GO_1', 'NODEJS_12', 'NODEJS_14', 'NODEJS_16', 'NODEJS_18', 'PHP_81', 'PYTHON_3', 'PYTHON_311', 'RUBY_31']
- **Required**: Yes

### BuildCommand
- **Type**: typing.Optional[str]

### StartCommand
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[str]

### RuntimeEnvironmentVariables
- **Type**: typing.Optional[typing.Mapping[str, str]]

### RuntimeEnvironmentSecrets
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CodeRepositoryOutputTypeDef

### RepositoryUrl
- **Type**: <class 'str'>
- **Required**: Yes

### SourceCodeVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.SourceCodeVersionTypeDef'>
- **Required**: Yes

### CodeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apprunner_classes.CodeConfigurationOutputTypeDef]

### SourceDirectory
- **Type**: typing.Optional[str]


# CodeRepositoryTypeDef

### RepositoryUrl
- **Type**: <class 'str'>
- **Required**: Yes

### SourceCodeVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.SourceCodeVersionTypeDef'>
- **Required**: Yes

### CodeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apprunner_classes.CodeConfigurationTypeDef]

### SourceDirectory
- **Type**: typing.Optional[str]


# ConnectionSummaryTypeDef

### ConnectionName
- **Type**: typing.Optional[str]

### ConnectionArn
- **Type**: typing.Optional[str]

### ProviderType
- **Type**: typing.Optional[typing.Literal['BITBUCKET', 'GITHUB']]

### Status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DELETED', 'ERROR', 'PENDING_HANDSHAKE']]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]


# ConnectionTypeDef

### ConnectionName
- **Type**: typing.Optional[str]

### ConnectionArn
- **Type**: typing.Optional[str]

### ProviderType
- **Type**: typing.Optional[typing.Literal['BITBUCKET', 'GITHUB']]

### Status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DELETED', 'ERROR', 'PENDING_HANDSHAKE']]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]


# CreateAutoScalingConfigurationRequestTypeDef

### AutoScalingConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxConcurrency
- **Type**: typing.Optional[int]

### MinSize
- **Type**: typing.Optional[int]

### MaxSize
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apprunner_classes.TagTypeDef]]


# CreateAutoScalingConfigurationResponseTypeDef

### AutoScalingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.AutoScalingConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateConnectionRequestTypeDef

### ConnectionName
- **Type**: <class 'str'>
- **Required**: Yes

### ProviderType
- **Type**: typing.Literal['BITBUCKET', 'GITHUB']
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apprunner_classes.TagTypeDef]]


# CreateConnectionResponseTypeDef

### Connection
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ConnectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateObservabilityConfigurationRequestTypeDef

### ObservabilityConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### TraceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apprunner_classes.TraceConfigurationTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apprunner_classes.TagTypeDef]]


# CreateObservabilityConfigurationResponseTypeDef

### ObservabilityConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ObservabilityConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateServiceResponseTypeDef

### Service
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ServiceTypeDef'>
- **Required**: Yes

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVpcConnectorRequestTypeDef

### VpcConnectorName
- **Type**: <class 'str'>
- **Required**: Yes

### Subnets
- **Type**: typing.Sequence[str]
- **Required**: Yes

### SecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apprunner_classes.TagTypeDef]]


# CreateVpcConnectorResponseTypeDef

### VpcConnector
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.VpcConnectorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVpcIngressConnectionRequestTypeDef

### ServiceArn
- **Type**: <class 'str'>
- **Required**: Yes

### VpcIngressConnectionName
- **Type**: <class 'str'>
- **Required**: Yes

### IngressVpcConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.IngressVpcConfigurationTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apprunner_classes.TagTypeDef]]


# CreateVpcIngressConnectionResponseTypeDef

### VpcIngressConnection
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.VpcIngressConnectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomDomainTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### EnableWWWSubdomain
- **Type**: <class 'bool'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'BINDING_CERTIFICATE', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING', 'PENDING_CERTIFICATE_DNS_VALIDATION']
- **Required**: Yes

### CertificateValidationRecords
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.apprunner_classes.CertificateValidationRecordTypeDef]]


# DeleteAutoScalingConfigurationRequestTypeDef

### AutoScalingConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### DeleteAllRevisions
- **Type**: typing.Optional[bool]


# DeleteAutoScalingConfigurationResponseTypeDef

### AutoScalingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.AutoScalingConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteConnectionRequestTypeDef

### ConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConnectionResponseTypeDef

### Connection
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ConnectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteObservabilityConfigurationRequestTypeDef

### ObservabilityConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteObservabilityConfigurationResponseTypeDef

### ObservabilityConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ObservabilityConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteServiceRequestTypeDef

### ServiceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceResponseTypeDef

### Service
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ServiceTypeDef'>
- **Required**: Yes

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteVpcConnectorRequestTypeDef

### VpcConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVpcConnectorResponseTypeDef

### VpcConnector
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.VpcConnectorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteVpcIngressConnectionRequestTypeDef

### VpcIngressConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVpcIngressConnectionResponseTypeDef

### VpcIngressConnection
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.VpcIngressConnectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAutoScalingConfigurationRequestTypeDef

### AutoScalingConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAutoScalingConfigurationResponseTypeDef

### AutoScalingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.AutoScalingConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCustomDomainsRequestTypeDef

### ServiceArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeCustomDomainsResponseTypeDef

### DNSTarget
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceArn
- **Type**: <class 'str'>
- **Required**: Yes

### CustomDomains
- **Type**: typing.List[aws_resource_validator.pydantic_models.apprunner_classes.CustomDomainTypeDef]
- **Required**: Yes

### VpcDNSTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.apprunner_classes.VpcDNSTargetTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeObservabilityConfigurationRequestTypeDef

### ObservabilityConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeObservabilityConfigurationResponseTypeDef

### ObservabilityConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ObservabilityConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeServiceRequestTypeDef

### ServiceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeServiceResponseTypeDef

### Service
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ServiceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeVpcConnectorRequestTypeDef

### VpcConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeVpcConnectorResponseTypeDef

### VpcConnector
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.VpcConnectorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeVpcIngressConnectionRequestTypeDef

### VpcIngressConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeVpcIngressConnectionResponseTypeDef

### VpcIngressConnection
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.VpcIngressConnectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateCustomDomainRequestTypeDef

### ServiceArn
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateCustomDomainResponseTypeDef

### DNSTarget
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceArn
- **Type**: <class 'str'>
- **Required**: Yes

### CustomDomain
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.CustomDomainTypeDef'>
- **Required**: Yes

### VpcDNSTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.apprunner_classes.VpcDNSTargetTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EgressConfigurationTypeDef

### EgressType
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'VPC']]

### VpcConnectorArn
- **Type**: typing.Optional[str]


# EncryptionConfigurationTypeDef

### KmsKey
- **Type**: <class 'str'>
- **Required**: Yes


# HealthCheckConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImageConfigurationOutputTypeDef

### RuntimeEnvironmentVariables
- **Type**: typing.Optional[typing.Dict[str, str]]

### StartCommand
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[str]

### RuntimeEnvironmentSecrets
- **Type**: typing.Optional[typing.Dict[str, str]]


# ImageConfigurationTypeDef

### RuntimeEnvironmentVariables
- **Type**: typing.Optional[typing.Mapping[str, str]]

### StartCommand
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[str]

### RuntimeEnvironmentSecrets
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ImageRepositoryOutputTypeDef

### ImageIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ImageRepositoryType
- **Type**: typing.Literal['ECR', 'ECR_PUBLIC']
- **Required**: Yes

### ImageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apprunner_classes.ImageConfigurationOutputTypeDef]


# ImageRepositoryTypeDef

### ImageIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ImageRepositoryType
- **Type**: typing.Literal['ECR', 'ECR_PUBLIC']
- **Required**: Yes

### ImageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apprunner_classes.ImageConfigurationTypeDef]


# IngressConfigurationTypeDef

### IsPubliclyAccessible
- **Type**: typing.Optional[bool]


# IngressVpcConfigurationTypeDef

### VpcId
- **Type**: typing.Optional[str]

### VpcEndpointId
- **Type**: typing.Optional[str]


# InstanceConfigurationTypeDef

### Cpu
- **Type**: typing.Optional[str]

### Memory
- **Type**: typing.Optional[str]

### InstanceRoleArn
- **Type**: typing.Optional[str]


# ListAutoScalingConfigurationsRequestTypeDef

### AutoScalingConfigurationName
- **Type**: typing.Optional[str]

### LatestOnly
- **Type**: typing.Optional[bool]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAutoScalingConfigurationsResponseTypeDef

### AutoScalingConfigurationSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.apprunner_classes.AutoScalingConfigurationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConnectionsRequestTypeDef

### ConnectionName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListConnectionsResponseTypeDef

### ConnectionSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.apprunner_classes.ConnectionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListObservabilityConfigurationsRequestTypeDef

### ObservabilityConfigurationName
- **Type**: typing.Optional[str]

### LatestOnly
- **Type**: typing.Optional[bool]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListObservabilityConfigurationsResponseTypeDef

### ObservabilityConfigurationSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.apprunner_classes.ObservabilityConfigurationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOperationsRequestTypeDef

### ServiceArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListOperationsResponseTypeDef

### OperationSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.apprunner_classes.OperationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListServicesForAutoScalingConfigurationRequestTypeDef

### AutoScalingConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListServicesForAutoScalingConfigurationResponseTypeDef

### ServiceArnList
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListServicesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListServicesResponseTypeDef

### ServiceSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.apprunner_classes.ServiceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.apprunner_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVpcConnectorsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListVpcConnectorsResponseTypeDef

### VpcConnectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.apprunner_classes.VpcConnectorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListVpcIngressConnectionsFilterTypeDef

### ServiceArn
- **Type**: typing.Optional[str]

### VpcEndpointId
- **Type**: typing.Optional[str]


# ListVpcIngressConnectionsRequestTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apprunner_classes.ListVpcIngressConnectionsFilterTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListVpcIngressConnectionsResponseTypeDef

### VpcIngressConnectionSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.apprunner_classes.VpcIngressConnectionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# NetworkConfigurationTypeDef

### EgressConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apprunner_classes.EgressConfigurationTypeDef]

### IngressConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apprunner_classes.IngressConfigurationTypeDef]

### IpAddressType
- **Type**: typing.Optional[typing.Literal['DUAL_STACK', 'IPV4']]


# ObservabilityConfigurationSummaryTypeDef

### ObservabilityConfigurationArn
- **Type**: typing.Optional[str]

### ObservabilityConfigurationName
- **Type**: typing.Optional[str]

### ObservabilityConfigurationRevision
- **Type**: typing.Optional[int]


# ObservabilityConfigurationTypeDef

### ObservabilityConfigurationArn
- **Type**: typing.Optional[str]

### ObservabilityConfigurationName
- **Type**: typing.Optional[str]

### TraceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apprunner_classes.TraceConfigurationTypeDef]

### ObservabilityConfigurationRevision
- **Type**: typing.Optional[int]

### Latest
- **Type**: typing.Optional[bool]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### DeletedAt
- **Type**: typing.Optional[datetime.datetime]


# OperationSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PauseServiceRequestTypeDef

### ServiceArn
- **Type**: <class 'str'>
- **Required**: Yes


# PauseServiceResponseTypeDef

### Service
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ServiceTypeDef'>
- **Required**: Yes

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# ResumeServiceRequestTypeDef

### ServiceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ResumeServiceResponseTypeDef

### Service
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ServiceTypeDef'>
- **Required**: Yes

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ServiceObservabilityConfigurationTypeDef

### ObservabilityEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### ObservabilityConfigurationArn
- **Type**: typing.Optional[str]


# ServiceSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServiceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SourceCodeVersionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SourceConfigurationOutputTypeDef

### CodeRepository
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apprunner_classes.CodeRepositoryOutputTypeDef]

### ImageRepository
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apprunner_classes.ImageRepositoryOutputTypeDef]

### AutoDeploymentsEnabled
- **Type**: typing.Optional[bool]

### AuthenticationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apprunner_classes.AuthenticationConfigurationTypeDef]


# SourceConfigurationTypeDef

### CodeRepository
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apprunner_classes.CodeRepositoryTypeDef]

### ImageRepository
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apprunner_classes.ImageRepositoryTypeDef]

### AutoDeploymentsEnabled
- **Type**: typing.Optional[bool]

### AuthenticationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apprunner_classes.AuthenticationConfigurationTypeDef]


# SourceConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StartDeploymentRequestTypeDef

### ServiceArn
- **Type**: <class 'str'>
- **Required**: Yes


# StartDeploymentResponseTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.apprunner_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TraceConfigurationTypeDef

### Vendor
- **Type**: typing.Literal['AWSXRAY']
- **Required**: Yes


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDefaultAutoScalingConfigurationRequestTypeDef

### AutoScalingConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateDefaultAutoScalingConfigurationResponseTypeDef

### AutoScalingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.AutoScalingConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateServiceRequestTypeDef

### ServiceArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apprunner_classes.SourceConfigurationUnionTypeDef]

### InstanceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apprunner_classes.InstanceConfigurationTypeDef]

### AutoScalingConfigurationArn
- **Type**: typing.Optional[str]

### HealthCheckConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apprunner_classes.HealthCheckConfigurationTypeDef]

### NetworkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apprunner_classes.NetworkConfigurationTypeDef]

### ObservabilityConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apprunner_classes.ServiceObservabilityConfigurationTypeDef]


# UpdateServiceResponseTypeDef

### Service
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ServiceTypeDef'>
- **Required**: Yes

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateVpcIngressConnectionRequestTypeDef

### VpcIngressConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### IngressVpcConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.IngressVpcConfigurationTypeDef'>
- **Required**: Yes


# UpdateVpcIngressConnectionResponseTypeDef

### VpcIngressConnection
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.VpcIngressConnectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VpcConnectorTypeDef

### VpcConnectorName
- **Type**: typing.Optional[str]

### VpcConnectorArn
- **Type**: typing.Optional[str]

### VpcConnectorRevision
- **Type**: typing.Optional[int]

### Subnets
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### DeletedAt
- **Type**: typing.Optional[datetime.datetime]


# VpcDNSTargetTypeDef

### VpcIngressConnectionArn
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### DomainName
- **Type**: typing.Optional[str]


# VpcIngressConnectionSummaryTypeDef

### VpcIngressConnectionArn
- **Type**: typing.Optional[str]

### ServiceArn
- **Type**: typing.Optional[str]


# VpcIngressConnectionTypeDef

### VpcIngressConnectionArn
- **Type**: typing.Optional[str]

### VpcIngressConnectionName
- **Type**: typing.Optional[str]

### ServiceArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DELETED', 'FAILED_CREATION', 'FAILED_DELETION', 'FAILED_UPDATE', 'PENDING_CREATION', 'PENDING_DELETION', 'PENDING_UPDATE']]

### AccountId
- **Type**: typing.Optional[str]

### DomainName
- **Type**: typing.Optional[str]

### IngressVpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apprunner_classes.IngressVpcConfigurationTypeDef]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### DeletedAt
- **Type**: typing.Optional[datetime.datetime]


