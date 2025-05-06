# Pca Connector Scep Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Challenge

### Arn
- **Type**: typing.Optional[str]

### ConnectorArn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### Password
- **Type**: typing.Optional[str]


# ChallengeMetadata

### Arn
- **Type**: typing.Optional[str]

### ConnectorArn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# ChallengeMetadataSummary

### Arn
- **Type**: typing.Optional[str]

### ConnectorArn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# Connector

### Arn
- **Type**: typing.Optional[str]

### CertificateAuthorityArn
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['GENERAL_PURPOSE', 'INTUNE']]

### MobileDeviceManagement
- **Type**: <class 'NoneType'>

### OpenIdConfiguration
- **Type**: <class 'NoneType'>

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']]

### StatusReason
- **Type**: typing.Optional[typing.Literal['INTERNAL_FAILURE', 'PRIVATECA_ACCESS_DENIED', 'PRIVATECA_INVALID_STATE', 'PRIVATECA_RESOURCE_NOT_FOUND']]

### Endpoint
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# ConnectorSummary

### Arn
- **Type**: typing.Optional[str]

### CertificateAuthorityArn
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['GENERAL_PURPOSE', 'INTUNE']]

### MobileDeviceManagement
- **Type**: <class 'NoneType'>

### OpenIdConfiguration
- **Type**: <class 'NoneType'>

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']]

### StatusReason
- **Type**: typing.Optional[typing.Literal['INTERNAL_FAILURE', 'PRIVATECA_ACCESS_DENIED', 'PRIVATECA_INVALID_STATE', 'PRIVATECA_RESOURCE_NOT_FOUND']]

### Endpoint
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# CreateChallengeRequest

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateChallengeResponse

### Challenge
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_scep.pca_connector_scep_classes.Challenge'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_scep.pca_connector_scep_classes.ResponseMetadata'>
- **Required**: Yes


# CreateConnectorRequest

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### MobileDeviceManagement
- **Type**: <class 'NoneType'>

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateConnectorResponse

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_scep.pca_connector_scep_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteChallengeRequest

### ChallengeArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConnectorRequest

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_scep.pca_connector_scep_classes.ResponseMetadata'>
- **Required**: Yes


# GetChallengeMetadataRequest

### ChallengeArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetChallengeMetadataResponse

### ChallengeMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_scep.pca_connector_scep_classes.ChallengeMetadata'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_scep.pca_connector_scep_classes.ResponseMetadata'>
- **Required**: Yes


# GetChallengePasswordRequest

### ChallengeArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetChallengePasswordResponse

### Password
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_scep.pca_connector_scep_classes.ResponseMetadata'>
- **Required**: Yes


# GetConnectorRequest

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetConnectorResponse

### Connector
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_scep.pca_connector_scep_classes.Connector'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_scep.pca_connector_scep_classes.ResponseMetadata'>
- **Required**: Yes


# IntuneConfiguration

### AzureApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: <class 'str'>
- **Required**: Yes


# ListChallengeMetadataRequest

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListChallengeMetadataRequestPaginate

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_scep.pca_connector_scep_classes.PaginatorConfig]


# ListChallengeMetadataResponse

### Challenges
- **Type**: typing.List[aws_resource_validator.pydantic_models.pca_connector_scep.pca_connector_scep_classes.ChallengeMetadataSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_scep.pca_connector_scep_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConnectorsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListConnectorsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_scep.pca_connector_scep_classes.PaginatorConfig]


# ListConnectorsResponse

### Connectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.pca_connector_scep.pca_connector_scep_classes.ConnectorSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_scep.pca_connector_scep_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_scep.pca_connector_scep_classes.ResponseMetadata'>
- **Required**: Yes


# MobileDeviceManagement

### Intune
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_scep.pca_connector_scep_classes.IntuneConfiguration]


# OpenIdConfiguration

### Issuer
- **Type**: typing.Optional[str]

### Subject
- **Type**: typing.Optional[str]

### Audience
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
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


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


