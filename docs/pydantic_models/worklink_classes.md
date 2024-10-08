# Pydantic Models in worklink_classes

# AssociateDomainRequestRequestTypeDef

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### AcmCertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]


# AssociateWebsiteAuthorizationProviderRequestRequestTypeDef

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizationProviderType
- **Type**: typing.Literal['SAML']
- **Required**: Yes

### DomainName
- **Type**: typing.Optional[str]


# AssociateWebsiteAuthorizationProviderResponseTypeDef

### AuthorizationProviderId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.worklink_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateWebsiteCertificateAuthorityRequestRequestTypeDef

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### Certificate
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]


# AssociateWebsiteCertificateAuthorityResponseTypeDef

### WebsiteCaId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.worklink_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateFleetRequestRequestTypeDef

### FleetName
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### OptimizeForEndUserLocation
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateFleetResponseTypeDef

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.worklink_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteFleetRequestRequestTypeDef

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAuditStreamConfigurationRequestRequestTypeDef

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAuditStreamConfigurationResponseTypeDef

### AuditStreamArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.worklink_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCompanyNetworkConfigurationRequestRequestTypeDef

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCompanyNetworkConfigurationResponseTypeDef

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.worklink_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDevicePolicyConfigurationRequestRequestTypeDef

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDevicePolicyConfigurationResponseTypeDef

### DeviceCaCertificate
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.worklink_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDeviceRequestRequestTypeDef

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDeviceResponseTypeDef

### Status
- **Type**: typing.Literal['ACTIVE', 'SIGNED_OUT']
- **Required**: Yes

### Model
- **Type**: <class 'str'>
- **Required**: Yes

### Manufacturer
- **Type**: <class 'str'>
- **Required**: Yes

### OperatingSystem
- **Type**: <class 'str'>
- **Required**: Yes

### OperatingSystemVersion
- **Type**: <class 'str'>
- **Required**: Yes

### PatchLevel
- **Type**: <class 'str'>
- **Required**: Yes

### FirstAccessedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastAccessedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.worklink_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDomainRequestRequestTypeDef

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDomainResponseTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DomainStatus
- **Type**: typing.Literal['ACTIVE', 'ASSOCIATING', 'DISASSOCIATED', 'DISASSOCIATING', 'FAILED_TO_ASSOCIATE', 'FAILED_TO_DISASSOCIATE', 'INACTIVE', 'PENDING_VALIDATION']
- **Required**: Yes

### AcmCertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.worklink_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFleetMetadataRequestRequestTypeDef

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFleetMetadataResponseTypeDef

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FleetName
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### OptimizeForEndUserLocation
- **Type**: <class 'bool'>
- **Required**: Yes

### CompanyCode
- **Type**: <class 'str'>
- **Required**: Yes

### FleetStatus
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'FAILED_TO_CREATE', 'FAILED_TO_DELETE']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.worklink_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeIdentityProviderConfigurationRequestRequestTypeDef

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeIdentityProviderConfigurationResponseTypeDef

### IdentityProviderType
- **Type**: typing.Literal['SAML']
- **Required**: Yes

### ServiceProviderSamlMetadata
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityProviderSamlMetadata
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.worklink_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeWebsiteCertificateAuthorityRequestRequestTypeDef

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### WebsiteCaId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWebsiteCertificateAuthorityResponseTypeDef

### Certificate
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.worklink_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeviceSummaryTypeDef

### DeviceId
- **Type**: typing.Optional[str]

### DeviceStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'SIGNED_OUT']]


# DisassociateDomainRequestRequestTypeDef

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateWebsiteAuthorizationProviderRequestRequestTypeDef

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizationProviderId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateWebsiteCertificateAuthorityRequestRequestTypeDef

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### WebsiteCaId
- **Type**: <class 'str'>
- **Required**: Yes


# DomainSummaryTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DomainStatus
- **Type**: typing.Literal['ACTIVE', 'ASSOCIATING', 'DISASSOCIATED', 'DISASSOCIATING', 'FAILED_TO_ASSOCIATE', 'FAILED_TO_DISASSOCIATE', 'INACTIVE', 'PENDING_VALIDATION']
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]


# FleetSummaryTypeDef

### FleetArn
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### FleetName
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### CompanyCode
- **Type**: typing.Optional[str]

### FleetStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'FAILED_TO_CREATE', 'FAILED_TO_DELETE']]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ListDevicesRequestRequestTypeDef

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDevicesResponseTypeDef

### Devices
- **Type**: typing.List[aws_resource_validator.pydantic_models.worklink_classes.DeviceSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.worklink_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDomainsRequestRequestTypeDef

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDomainsResponseTypeDef

### Domains
- **Type**: typing.List[aws_resource_validator.pydantic_models.worklink_classes.DomainSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.worklink_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFleetsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListFleetsResponseTypeDef

### FleetSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.worklink_classes.FleetSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.worklink_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.worklink_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWebsiteAuthorizationProvidersRequestRequestTypeDef

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListWebsiteAuthorizationProvidersResponseTypeDef

### WebsiteAuthorizationProviders
- **Type**: typing.List[aws_resource_validator.pydantic_models.worklink_classes.WebsiteAuthorizationProviderSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.worklink_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWebsiteCertificateAuthoritiesRequestRequestTypeDef

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListWebsiteCertificateAuthoritiesResponseTypeDef

### WebsiteCertificateAuthorities
- **Type**: typing.List[aws_resource_validator.pydantic_models.worklink_classes.WebsiteCaSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.worklink_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HostId
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


# RestoreDomainAccessRequestRequestTypeDef

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# RevokeDomainAccessRequestRequestTypeDef

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# SignOutUserRequestRequestTypeDef

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAuditStreamConfigurationRequestRequestTypeDef

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### AuditStreamArn
- **Type**: typing.Optional[str]


# UpdateCompanyNetworkConfigurationRequestRequestTypeDef

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDevicePolicyConfigurationRequestRequestTypeDef

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceCaCertificate
- **Type**: typing.Optional[str]


# UpdateDomainMetadataRequestRequestTypeDef

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]


# UpdateFleetMetadataRequestRequestTypeDef

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### OptimizeForEndUserLocation
- **Type**: typing.Optional[bool]


# UpdateIdentityProviderConfigurationRequestRequestTypeDef

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityProviderType
- **Type**: typing.Literal['SAML']
- **Required**: Yes

### IdentityProviderSamlMetadata
- **Type**: typing.Optional[str]


# WebsiteAuthorizationProviderSummaryTypeDef

### AuthorizationProviderType
- **Type**: typing.Literal['SAML']
- **Required**: Yes

### AuthorizationProviderId
- **Type**: typing.Optional[str]

### DomainName
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]


# WebsiteCaSummaryTypeDef

### WebsiteCaId
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### DisplayName
- **Type**: typing.Optional[str]


