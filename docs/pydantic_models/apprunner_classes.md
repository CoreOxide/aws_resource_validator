# Apprunner Classes

# AssociateCustomDomainRequest

### ServiceArn
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### EnableWWWSubdomain
- **Type**: typing.Optional[bool]


# AssociateCustomDomainResponse

### DNSTarget
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceArn
- **Type**: <class 'str'>
- **Required**: Yes

### CustomDomain
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.CustomDomain'>
- **Required**: Yes

### VpcDNSTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.apprunner.apprunner_classes.VpcDNSTarget]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes


# AuthenticationConfiguration

### ConnectionArn
- **Type**: typing.Optional[str]

### AccessRoleArn
- **Type**: typing.Optional[str]


# AutoScalingConfiguration

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


# AutoScalingConfigurationSummary

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


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CertificateValidationRecord

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING_VALIDATION', 'SUCCESS']]


# CodeConfiguration

### ConfigurationSource
- **Type**: typing.Literal['API', 'REPOSITORY']
- **Required**: Yes

### CodeConfigurationValues
- **Type**: <class 'NoneType'>


# CodeConfigurationOutput

### ConfigurationSource
- **Type**: typing.Literal['API', 'REPOSITORY']
- **Required**: Yes

### CodeConfigurationValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apprunner.apprunner_classes.CodeConfigurationValuesOutput]


# CodeConfigurationValues

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


# CodeConfigurationValuesOutput

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


# CodeRepository

### RepositoryUrl
- **Type**: <class 'str'>
- **Required**: Yes

### SourceCodeVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.SourceCodeVersion'>
- **Required**: Yes

### CodeConfiguration
- **Type**: <class 'NoneType'>

### SourceDirectory
- **Type**: typing.Optional[str]


# CodeRepositoryOutput

### RepositoryUrl
- **Type**: <class 'str'>
- **Required**: Yes

### SourceCodeVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.SourceCodeVersion'>
- **Required**: Yes

### CodeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apprunner.apprunner_classes.CodeConfigurationOutput]

### SourceDirectory
- **Type**: typing.Optional[str]


# Connection

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


# ConnectionSummary

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


# CreateAutoScalingConfigurationRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.apprunner.apprunner_classes.Tag]]


# CreateAutoScalingConfigurationResponse

### AutoScalingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.AutoScalingConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes


# CreateConnectionRequest

### ConnectionName
- **Type**: <class 'str'>
- **Required**: Yes

### ProviderType
- **Type**: typing.Literal['BITBUCKET', 'GITHUB']
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.apprunner.apprunner_classes.Tag]]


# CreateConnectionResponse

### Connection
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.Connection'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes


# CreateObservabilityConfigurationRequest

### ObservabilityConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### TraceConfiguration
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.apprunner.apprunner_classes.Tag]]


# CreateObservabilityConfigurationResponse

### ObservabilityConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ObservabilityConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes


# CreateServiceRequest

### ServiceName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.apprunner.apprunner_classes.SourceConfiguration, aws_resource_validator.pydantic_models.apprunner.apprunner_classes.SourceConfigurationOutput]
- **Required**: Yes

### InstanceConfiguration
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.apprunner.apprunner_classes.Tag]]

### EncryptionConfiguration
- **Type**: <class 'NoneType'>

### HealthCheckConfiguration
- **Type**: <class 'NoneType'>

### AutoScalingConfigurationArn
- **Type**: typing.Optional[str]

### NetworkConfiguration
- **Type**: <class 'NoneType'>

### ObservabilityConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ServiceObservabilityConfiguration]


# CreateServiceResponse

### Service
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.Service'>
- **Required**: Yes

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVpcConnectorRequest

### VpcConnectorName
- **Type**: <class 'str'>
- **Required**: Yes

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.apprunner.apprunner_classes.Tag]]


# CreateVpcConnectorResponse

### VpcConnector
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.VpcConnector'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVpcIngressConnectionRequest

### ServiceArn
- **Type**: <class 'str'>
- **Required**: Yes

### VpcIngressConnectionName
- **Type**: <class 'str'>
- **Required**: Yes

### IngressVpcConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.IngressVpcConfiguration'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.apprunner.apprunner_classes.Tag]]


# CreateVpcIngressConnectionResponse

### VpcIngressConnection
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.VpcIngressConnection'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes


# CustomDomain

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.apprunner.apprunner_classes.CertificateValidationRecord]]


# DeleteAutoScalingConfigurationRequest

### AutoScalingConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### DeleteAllRevisions
- **Type**: typing.Optional[bool]


# DeleteAutoScalingConfigurationResponse

### AutoScalingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.AutoScalingConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteConnectionRequest

### ConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConnectionResponse

### Connection
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.Connection'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteObservabilityConfigurationRequest

### ObservabilityConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteObservabilityConfigurationResponse

### ObservabilityConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ObservabilityConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteServiceRequest

### ServiceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceResponse

### Service
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.Service'>
- **Required**: Yes

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteVpcConnectorRequest

### VpcConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVpcConnectorResponse

### VpcConnector
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.VpcConnector'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteVpcIngressConnectionRequest

### VpcIngressConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVpcIngressConnectionResponse

### VpcIngressConnection
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.VpcIngressConnection'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAutoScalingConfigurationRequest

### AutoScalingConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAutoScalingConfigurationResponse

### AutoScalingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.AutoScalingConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCustomDomainsRequest

### ServiceArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeCustomDomainsResponse

### DNSTarget
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceArn
- **Type**: <class 'str'>
- **Required**: Yes

### CustomDomains
- **Type**: typing.List[aws_resource_validator.pydantic_models.apprunner.apprunner_classes.CustomDomain]
- **Required**: Yes

### VpcDNSTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.apprunner.apprunner_classes.VpcDNSTarget]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeObservabilityConfigurationRequest

### ObservabilityConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeObservabilityConfigurationResponse

### ObservabilityConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ObservabilityConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeServiceRequest

### ServiceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeServiceResponse

### Service
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.Service'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeVpcConnectorRequest

### VpcConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeVpcConnectorResponse

### VpcConnector
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.VpcConnector'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeVpcIngressConnectionRequest

### VpcIngressConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeVpcIngressConnectionResponse

### VpcIngressConnection
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.VpcIngressConnection'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateCustomDomainRequest

### ServiceArn
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateCustomDomainResponse

### DNSTarget
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceArn
- **Type**: <class 'str'>
- **Required**: Yes

### CustomDomain
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.CustomDomain'>
- **Required**: Yes

### VpcDNSTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.apprunner.apprunner_classes.VpcDNSTarget]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes


# EgressConfiguration

### EgressType
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'VPC']]

### VpcConnectorArn
- **Type**: typing.Optional[str]


# EncryptionConfiguration

### KmsKey
- **Type**: <class 'str'>
- **Required**: Yes


# HealthCheckConfiguration

### Protocol
- **Type**: typing.Optional[typing.Literal['HTTP', 'TCP']]

### Path
- **Type**: typing.Optional[str]

### Interval
- **Type**: typing.Optional[int]

### Timeout
- **Type**: typing.Optional[int]

### HealthyThreshold
- **Type**: typing.Optional[int]

### UnhealthyThreshold
- **Type**: typing.Optional[int]


# ImageConfiguration

### RuntimeEnvironmentVariables
- **Type**: typing.Optional[typing.Dict[str, str]]

### StartCommand
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[str]

### RuntimeEnvironmentSecrets
- **Type**: typing.Optional[typing.Dict[str, str]]


# ImageConfigurationOutput

### RuntimeEnvironmentVariables
- **Type**: typing.Optional[typing.Dict[str, str]]

### StartCommand
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[str]

### RuntimeEnvironmentSecrets
- **Type**: typing.Optional[typing.Dict[str, str]]


# ImageRepository

### ImageIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ImageRepositoryType
- **Type**: typing.Literal['ECR', 'ECR_PUBLIC']
- **Required**: Yes

### ImageConfiguration
- **Type**: <class 'NoneType'>


# ImageRepositoryOutput

### ImageIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ImageRepositoryType
- **Type**: typing.Literal['ECR', 'ECR_PUBLIC']
- **Required**: Yes

### ImageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ImageConfigurationOutput]


# IngressConfiguration

### IsPubliclyAccessible
- **Type**: typing.Optional[bool]


# IngressVpcConfiguration

### VpcId
- **Type**: typing.Optional[str]

### VpcEndpointId
- **Type**: typing.Optional[str]


# InstanceConfiguration

### Cpu
- **Type**: typing.Optional[str]

### Memory
- **Type**: typing.Optional[str]

### InstanceRoleArn
- **Type**: typing.Optional[str]


# ListAutoScalingConfigurationsRequest

### AutoScalingConfigurationName
- **Type**: typing.Optional[str]

### LatestOnly
- **Type**: typing.Optional[bool]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAutoScalingConfigurationsResponse

### AutoScalingConfigurationSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.apprunner.apprunner_classes.AutoScalingConfigurationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConnectionsRequest

### ConnectionName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListConnectionsResponse

### ConnectionSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ConnectionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListObservabilityConfigurationsRequest

### ObservabilityConfigurationName
- **Type**: typing.Optional[str]

### LatestOnly
- **Type**: typing.Optional[bool]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListObservabilityConfigurationsResponse

### ObservabilityConfigurationSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ObservabilityConfigurationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOperationsRequest

### ServiceArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListOperationsResponse

### OperationSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.apprunner.apprunner_classes.OperationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListServicesForAutoScalingConfigurationRequest

### AutoScalingConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListServicesForAutoScalingConfigurationResponse

### ServiceArnList
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListServicesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListServicesResponse

### ServiceSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ServiceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.apprunner.apprunner_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes


# ListVpcConnectorsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListVpcConnectorsResponse

### VpcConnectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.apprunner.apprunner_classes.VpcConnector]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListVpcIngressConnectionsFilter

### ServiceArn
- **Type**: typing.Optional[str]

### VpcEndpointId
- **Type**: typing.Optional[str]


# ListVpcIngressConnectionsRequest

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ListVpcIngressConnectionsFilter]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListVpcIngressConnectionsResponse

### VpcIngressConnectionSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.apprunner.apprunner_classes.VpcIngressConnectionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# NetworkConfiguration

### EgressConfiguration
- **Type**: <class 'NoneType'>

### IngressConfiguration
- **Type**: <class 'NoneType'>

### IpAddressType
- **Type**: typing.Optional[typing.Literal['DUAL_STACK', 'IPV4']]


# ObservabilityConfiguration

### ObservabilityConfigurationArn
- **Type**: typing.Optional[str]

### ObservabilityConfigurationName
- **Type**: typing.Optional[str]

### TraceConfiguration
- **Type**: <class 'NoneType'>

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


# ObservabilityConfigurationSummary

### ObservabilityConfigurationArn
- **Type**: typing.Optional[str]

### ObservabilityConfigurationName
- **Type**: typing.Optional[str]

### ObservabilityConfigurationRevision
- **Type**: typing.Optional[int]


# OperationSummary

### Id
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['CREATE_SERVICE', 'DELETE_SERVICE', 'PAUSE_SERVICE', 'RESUME_SERVICE', 'START_DEPLOYMENT', 'UPDATE_SERVICE']]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'PENDING', 'ROLLBACK_FAILED', 'ROLLBACK_IN_PROGRESS', 'ROLLBACK_SUCCEEDED', 'SUCCEEDED']]

### TargetArn
- **Type**: typing.Optional[str]

### StartedAt
- **Type**: typing.Optional[datetime.datetime]

### EndedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# PauseServiceRequest

### ServiceArn
- **Type**: <class 'str'>
- **Required**: Yes


# PauseServiceResponse

### Service
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.Service'>
- **Required**: Yes

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes


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


# ResumeServiceRequest

### ServiceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ResumeServiceResponse

### Service
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.Service'>
- **Required**: Yes

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes


# Service

### ServiceName
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceId
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CREATE_FAILED', 'DELETED', 'DELETE_FAILED', 'OPERATION_IN_PROGRESS', 'PAUSED', 'RUNNING']
- **Required**: Yes

### SourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.SourceConfigurationOutput'>
- **Required**: Yes

### InstanceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.InstanceConfiguration'>
- **Required**: Yes

### AutoScalingConfigurationSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.AutoScalingConfigurationSummary'>
- **Required**: Yes

### NetworkConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.NetworkConfiguration'>
- **Required**: Yes

### ServiceUrl
- **Type**: typing.Optional[str]

### DeletedAt
- **Type**: typing.Optional[datetime.datetime]

### EncryptionConfiguration
- **Type**: <class 'NoneType'>

### HealthCheckConfiguration
- **Type**: <class 'NoneType'>

### ObservabilityConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ServiceObservabilityConfiguration]


# ServiceObservabilityConfiguration

### ObservabilityEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### ObservabilityConfigurationArn
- **Type**: typing.Optional[str]


# ServiceSummary

### ServiceName
- **Type**: typing.Optional[str]

### ServiceId
- **Type**: typing.Optional[str]

### ServiceArn
- **Type**: typing.Optional[str]

### ServiceUrl
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'DELETED', 'DELETE_FAILED', 'OPERATION_IN_PROGRESS', 'PAUSED', 'RUNNING']]


# SourceCodeVersion

### Type
- **Type**: typing.Literal['BRANCH']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# SourceConfiguration

### CodeRepository
- **Type**: <class 'NoneType'>

### ImageRepository
- **Type**: <class 'NoneType'>

### AutoDeploymentsEnabled
- **Type**: typing.Optional[bool]

### AuthenticationConfiguration
- **Type**: <class 'NoneType'>


# SourceConfigurationOutput

### CodeRepository
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apprunner.apprunner_classes.CodeRepositoryOutput]

### ImageRepository
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ImageRepositoryOutput]

### AutoDeploymentsEnabled
- **Type**: typing.Optional[bool]

### AuthenticationConfiguration
- **Type**: <class 'NoneType'>


# StartDeploymentRequest

### ServiceArn
- **Type**: <class 'str'>
- **Required**: Yes


# StartDeploymentResponse

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.apprunner.apprunner_classes.Tag]
- **Required**: Yes


# TraceConfiguration

### Vendor
- **Type**: typing.Literal['AWSXRAY']
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateDefaultAutoScalingConfigurationRequest

### AutoScalingConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateDefaultAutoScalingConfigurationResponse

### AutoScalingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.AutoScalingConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateServiceRequest

### ServiceArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.apprunner.apprunner_classes.SourceConfiguration, aws_resource_validator.pydantic_models.apprunner.apprunner_classes.SourceConfigurationOutput, NoneType]

### InstanceConfiguration
- **Type**: <class 'NoneType'>

### AutoScalingConfigurationArn
- **Type**: typing.Optional[str]

### HealthCheckConfiguration
- **Type**: <class 'NoneType'>

### NetworkConfiguration
- **Type**: <class 'NoneType'>

### ObservabilityConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ServiceObservabilityConfiguration]


# UpdateServiceResponse

### Service
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.Service'>
- **Required**: Yes

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateVpcIngressConnectionRequest

### VpcIngressConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### IngressVpcConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.IngressVpcConfiguration'>
- **Required**: Yes


# UpdateVpcIngressConnectionResponse

### VpcIngressConnection
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.VpcIngressConnection'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apprunner.apprunner_classes.ResponseMetadata'>
- **Required**: Yes


# VpcConnector

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


# VpcDNSTarget

### VpcIngressConnectionArn
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### DomainName
- **Type**: typing.Optional[str]


# VpcIngressConnection

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
- **Type**: <class 'NoneType'>

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### DeletedAt
- **Type**: typing.Optional[datetime.datetime]


# VpcIngressConnectionSummary

### VpcIngressConnectionArn
- **Type**: typing.Optional[str]

### ServiceArn
- **Type**: typing.Optional[str]


