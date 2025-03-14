# Pca Connector Scep Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChallengeMetadataSummaryTypeDef

### Arn
- **Type**: typing.Optional[str]

### ConnectorArn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# ChallengeMetadataTypeDef

### Arn
- **Type**: typing.Optional[str]

### ConnectorArn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# ChallengeTypeDef

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


# ConnectorSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConnectorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateChallengeRequestTypeDef

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateChallengeResponseTypeDef

### Challenge
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_scep_classes.ChallengeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_scep_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateConnectorRequestTypeDef

### CertificateAuthorityArn
- **Type**: <class 'str'>
- **Required**: Yes

### MobileDeviceManagement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_scep_classes.MobileDeviceManagementTypeDef]

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateConnectorResponseTypeDef

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_scep_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteChallengeRequestTypeDef

### ChallengeArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConnectorRequestTypeDef

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_scep_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetChallengeMetadataRequestTypeDef

### ChallengeArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetChallengeMetadataResponseTypeDef

### ChallengeMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_scep_classes.ChallengeMetadataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_scep_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetChallengePasswordRequestTypeDef

### ChallengeArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetChallengePasswordResponseTypeDef

### Password
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_scep_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConnectorRequestTypeDef

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetConnectorResponseTypeDef

### Connector
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_scep_classes.ConnectorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_scep_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IntuneConfigurationTypeDef

### AzureApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: <class 'str'>
- **Required**: Yes


# ListChallengeMetadataRequestPaginateTypeDef

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_scep_classes.PaginatorConfigTypeDef]


# ListChallengeMetadataRequestTypeDef

### ConnectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListChallengeMetadataResponseTypeDef

### Challenges
- **Type**: typing.List[aws_resource_validator.pydantic_models.pca_connector_scep_classes.ChallengeMetadataSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_scep_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConnectorsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_scep_classes.PaginatorConfigTypeDef]


# ListConnectorsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListConnectorsResponseTypeDef

### Connectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.pca_connector_scep_classes.ConnectorSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_scep_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pca_connector_scep_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MobileDeviceManagementTypeDef

### Intune
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pca_connector_scep_classes.IntuneConfigurationTypeDef]


# OpenIdConfigurationTypeDef

### Issuer
- **Type**: typing.Optional[str]

### Subject
- **Type**: typing.Optional[str]

### Audience
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
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


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


