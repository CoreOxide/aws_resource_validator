# rolesanywhere_classes

# AttributeMappingTypeDef

### certificateField
- **Type**: typing.Optional[typing.Literal['x509Issuer', 'x509SAN', 'x509Subject']]

### mappingRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rolesanywhere_classes.MappingRuleTypeDef]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateProfileRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### roleArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### durationSeconds
- **Type**: typing.Optional[int]

### enabled
- **Type**: typing.Optional[bool]

### managedPolicyArns
- **Type**: typing.Optional[typing.Sequence[str]]

### requireInstanceProperties
- **Type**: typing.Optional[bool]

### sessionPolicy
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rolesanywhere_classes.TagTypeDef]]


# CreateTrustAnchorRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere_classes.SourceTypeDef'>
- **Required**: Yes

### enabled
- **Type**: typing.Optional[bool]

### notificationSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rolesanywhere_classes.NotificationSettingTypeDef]]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rolesanywhere_classes.TagTypeDef]]


# CredentialSummaryTypeDef

### enabled
- **Type**: typing.Optional[bool]

### failed
- **Type**: typing.Optional[bool]

### issuer
- **Type**: typing.Optional[str]

### seenAt
- **Type**: typing.Optional[datetime.datetime]

### serialNumber
- **Type**: typing.Optional[str]

### x509CertificateData
- **Type**: typing.Optional[str]


# CrlDetailResponseTypeDef

### crl
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere_classes.CrlDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CrlDetailTypeDef

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### crlArn
- **Type**: typing.Optional[str]

### crlData
- **Type**: typing.Optional[bytes]

### crlId
- **Type**: typing.Optional[str]

### enabled
- **Type**: typing.Optional[bool]

### name
- **Type**: typing.Optional[str]

### trustAnchorArn
- **Type**: typing.Optional[str]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# DeleteAttributeMappingRequestRequestTypeDef

### certificateField
- **Type**: typing.Literal['x509Issuer', 'x509SAN', 'x509Subject']
- **Required**: Yes

### profileId
- **Type**: <class 'str'>
- **Required**: Yes

### specifiers
- **Type**: typing.Optional[typing.Sequence[str]]


# DeleteAttributeMappingResponseTypeDef

### profile
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere_classes.ProfileDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImportCrlRequestRequestTypeDef

### crlData
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### trustAnchorArn
- **Type**: <class 'str'>
- **Required**: Yes

### enabled
- **Type**: typing.Optional[bool]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rolesanywhere_classes.TagTypeDef]]


# InstancePropertyTypeDef

### failed
- **Type**: typing.Optional[bool]

### properties
- **Type**: typing.Optional[typing.Dict[str, str]]

### seenAt
- **Type**: typing.Optional[datetime.datetime]


# ListCrlsResponseTypeDef

### crls
- **Type**: typing.List[aws_resource_validator.pydantic_models.rolesanywhere_classes.CrlDetailTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProfilesResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### profiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.rolesanywhere_classes.ProfileDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRequestListCrlsPaginateTypeDef

### pageSize
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rolesanywhere_classes.PaginatorConfigTypeDef]


# ListRequestListProfilesPaginateTypeDef

### pageSize
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rolesanywhere_classes.PaginatorConfigTypeDef]


# ListRequestListSubjectsPaginateTypeDef

### pageSize
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rolesanywhere_classes.PaginatorConfigTypeDef]


# ListRequestListTrustAnchorsPaginateTypeDef

### pageSize
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rolesanywhere_classes.PaginatorConfigTypeDef]


# ListRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### pageSize
- **Type**: typing.Optional[int]


# ListSubjectsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### subjects
- **Type**: typing.List[aws_resource_validator.pydantic_models.rolesanywhere_classes.SubjectSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.rolesanywhere_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTrustAnchorsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### trustAnchors
- **Type**: typing.List[aws_resource_validator.pydantic_models.rolesanywhere_classes.TrustAnchorDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MappingRuleTypeDef

### specifier
- **Type**: <class 'str'>
- **Required**: Yes


# NotificationSettingDetailTypeDef

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### event
- **Type**: typing.Literal['CA_CERTIFICATE_EXPIRY', 'END_ENTITY_CERTIFICATE_EXPIRY']
- **Required**: Yes

### channel
- **Type**: typing.Optional[typing.Literal['ALL']]

### configuredBy
- **Type**: typing.Optional[str]

### threshold
- **Type**: typing.Optional[int]


# NotificationSettingKeyTypeDef

### event
- **Type**: typing.Literal['CA_CERTIFICATE_EXPIRY', 'END_ENTITY_CERTIFICATE_EXPIRY']
- **Required**: Yes

### channel
- **Type**: typing.Optional[typing.Literal['ALL']]


# NotificationSettingTypeDef

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### event
- **Type**: typing.Literal['CA_CERTIFICATE_EXPIRY', 'END_ENTITY_CERTIFICATE_EXPIRY']
- **Required**: Yes

### channel
- **Type**: typing.Optional[typing.Literal['ALL']]

### threshold
- **Type**: typing.Optional[int]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProfileDetailResponseTypeDef

### profile
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere_classes.ProfileDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ProfileDetailTypeDef

### attributeMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rolesanywhere_classes.AttributeMappingTypeDef]]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### durationSeconds
- **Type**: typing.Optional[int]

### enabled
- **Type**: typing.Optional[bool]

### managedPolicyArns
- **Type**: typing.Optional[typing.List[str]]

### name
- **Type**: typing.Optional[str]

### profileArn
- **Type**: typing.Optional[str]

### profileId
- **Type**: typing.Optional[str]

### requireInstanceProperties
- **Type**: typing.Optional[bool]

### roleArns
- **Type**: typing.Optional[typing.List[str]]

### sessionPolicy
- **Type**: typing.Optional[str]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# PutAttributeMappingRequestRequestTypeDef

### certificateField
- **Type**: typing.Literal['x509Issuer', 'x509SAN', 'x509Subject']
- **Required**: Yes

### mappingRules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.rolesanywhere_classes.MappingRuleTypeDef]
- **Required**: Yes

### profileId
- **Type**: <class 'str'>
- **Required**: Yes


# PutAttributeMappingResponseTypeDef

### profile
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere_classes.ProfileDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutNotificationSettingsRequestRequestTypeDef

### notificationSettings
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.rolesanywhere_classes.NotificationSettingTypeDef]
- **Required**: Yes

### trustAnchorId
- **Type**: <class 'str'>
- **Required**: Yes


# PutNotificationSettingsResponseTypeDef

### trustAnchor
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere_classes.TrustAnchorDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResetNotificationSettingsRequestRequestTypeDef

### notificationSettingKeys
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.rolesanywhere_classes.NotificationSettingKeyTypeDef]
- **Required**: Yes

### trustAnchorId
- **Type**: <class 'str'>
- **Required**: Yes


# ResetNotificationSettingsResponseTypeDef

### trustAnchor
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere_classes.TrustAnchorDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere_classes.ResponseMetadataTypeDef'>
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


# ScalarCrlRequestRequestTypeDef

### crlId
- **Type**: <class 'str'>
- **Required**: Yes


# ScalarProfileRequestRequestTypeDef

### profileId
- **Type**: <class 'str'>
- **Required**: Yes


# ScalarSubjectRequestRequestTypeDef

### subjectId
- **Type**: <class 'str'>
- **Required**: Yes


# ScalarTrustAnchorRequestRequestTypeDef

### trustAnchorId
- **Type**: <class 'str'>
- **Required**: Yes


# SourceDataTypeDef

### acmPcaArn
- **Type**: typing.Optional[str]

### x509CertificateData
- **Type**: typing.Optional[str]


# SourceTypeDef

### sourceData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rolesanywhere_classes.SourceDataTypeDef]

### sourceType
- **Type**: typing.Optional[typing.Literal['AWS_ACM_PCA', 'CERTIFICATE_BUNDLE', 'SELF_SIGNED_REPOSITORY']]


# SubjectDetailResponseTypeDef

### subject
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere_classes.SubjectDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SubjectDetailTypeDef

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### credentials
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rolesanywhere_classes.CredentialSummaryTypeDef]]

### enabled
- **Type**: typing.Optional[bool]

### instanceProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rolesanywhere_classes.InstancePropertyTypeDef]]

### lastSeenAt
- **Type**: typing.Optional[datetime.datetime]

### subjectArn
- **Type**: typing.Optional[str]

### subjectId
- **Type**: typing.Optional[str]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### x509Subject
- **Type**: typing.Optional[str]


# SubjectSummaryTypeDef

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### enabled
- **Type**: typing.Optional[bool]

### lastSeenAt
- **Type**: typing.Optional[datetime.datetime]

### subjectArn
- **Type**: typing.Optional[str]

### subjectId
- **Type**: typing.Optional[str]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### x509Subject
- **Type**: typing.Optional[str]


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.rolesanywhere_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TrustAnchorDetailResponseTypeDef

### trustAnchor
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere_classes.TrustAnchorDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TrustAnchorDetailTypeDef

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### enabled
- **Type**: typing.Optional[bool]

### name
- **Type**: typing.Optional[str]

### notificationSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rolesanywhere_classes.NotificationSettingDetailTypeDef]]

### source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rolesanywhere_classes.SourceTypeDef]

### trustAnchorArn
- **Type**: typing.Optional[str]

### trustAnchorId
- **Type**: typing.Optional[str]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateCrlRequestRequestTypeDef

### crlId
- **Type**: <class 'str'>
- **Required**: Yes

### crlData
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]

### name
- **Type**: typing.Optional[str]


# UpdateProfileRequestRequestTypeDef

### profileId
- **Type**: <class 'str'>
- **Required**: Yes

### durationSeconds
- **Type**: typing.Optional[int]

### managedPolicyArns
- **Type**: typing.Optional[typing.Sequence[str]]

### name
- **Type**: typing.Optional[str]

### roleArns
- **Type**: typing.Optional[typing.Sequence[str]]

### sessionPolicy
- **Type**: typing.Optional[str]


# UpdateTrustAnchorRequestRequestTypeDef

### trustAnchorId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rolesanywhere_classes.SourceTypeDef]


