# Rolesanywhere Classes

# AttributeMappingTypeDef

### certificateField
- **Type**: typing.Optional[typing.Literal['x509Issuer', 'x509SAN', 'x509Subject']]

### mappingRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rolesanywhere_classes.MappingRuleTypeDef]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateProfileRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### roleArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### acceptRoleSessionName
- **Type**: typing.Optional[bool]

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


# CreateTrustAnchorRequestTypeDef

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


# DeleteAttributeMappingRequestTypeDef

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


# ImportCrlRequestTypeDef

### crlData
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere_classes.BlobTypeDef'>
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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProfilesResponseTypeDef

### profiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.rolesanywhere_classes.ProfileDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRequestPaginateExtraExtraExtraTypeDef

### pageSize
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rolesanywhere_classes.PaginatorConfigTypeDef]


# ListRequestPaginateExtraExtraTypeDef

### pageSize
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rolesanywhere_classes.PaginatorConfigTypeDef]


# ListRequestPaginateExtraTypeDef

### pageSize
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rolesanywhere_classes.PaginatorConfigTypeDef]


# ListRequestPaginateTypeDef

### pageSize
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rolesanywhere_classes.PaginatorConfigTypeDef]


# ListRequestRequestExtraExtraTypeDef

### nextToken
- **Type**: typing.Optional[str]

### pageSize
- **Type**: typing.Optional[int]


# ListRequestRequestExtraTypeDef

### nextToken
- **Type**: typing.Optional[str]

### pageSize
- **Type**: typing.Optional[int]


# ListRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### pageSize
- **Type**: typing.Optional[int]


# ListRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### pageSize
- **Type**: typing.Optional[int]


# ListSubjectsResponseTypeDef

### subjects
- **Type**: typing.List[aws_resource_validator.pydantic_models.rolesanywhere_classes.SubjectSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

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

### trustAnchors
- **Type**: typing.List[aws_resource_validator.pydantic_models.rolesanywhere_classes.TrustAnchorDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


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

### acceptRoleSessionName
- **Type**: typing.Optional[bool]

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


# PutAttributeMappingRequestTypeDef

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


# PutNotificationSettingsRequestTypeDef

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


# ResetNotificationSettingsRequestTypeDef

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


# ScalarCrlRequestRequestExtraExtraTypeDef

### crlId
- **Type**: <class 'str'>
- **Required**: Yes


# ScalarCrlRequestRequestExtraTypeDef

### crlId
- **Type**: <class 'str'>
- **Required**: Yes


# ScalarCrlRequestRequestTypeDef

### crlId
- **Type**: <class 'str'>
- **Required**: Yes


# ScalarCrlRequestTypeDef

### crlId
- **Type**: <class 'str'>
- **Required**: Yes


# ScalarProfileRequestRequestExtraExtraTypeDef

### profileId
- **Type**: <class 'str'>
- **Required**: Yes


# ScalarProfileRequestRequestExtraTypeDef

### profileId
- **Type**: <class 'str'>
- **Required**: Yes


# ScalarProfileRequestRequestTypeDef

### profileId
- **Type**: <class 'str'>
- **Required**: Yes


# ScalarProfileRequestTypeDef

### profileId
- **Type**: <class 'str'>
- **Required**: Yes


# ScalarSubjectRequestTypeDef

### subjectId
- **Type**: <class 'str'>
- **Required**: Yes


# ScalarTrustAnchorRequestRequestExtraExtraTypeDef

### trustAnchorId
- **Type**: <class 'str'>
- **Required**: Yes


# ScalarTrustAnchorRequestRequestExtraTypeDef

### trustAnchorId
- **Type**: <class 'str'>
- **Required**: Yes


# ScalarTrustAnchorRequestRequestTypeDef

### trustAnchorId
- **Type**: <class 'str'>
- **Required**: Yes


# ScalarTrustAnchorRequestTypeDef

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


# TagResourceRequestTypeDef

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


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateCrlRequestTypeDef

### crlId
- **Type**: <class 'str'>
- **Required**: Yes

### crlData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rolesanywhere_classes.BlobTypeDef]

### name
- **Type**: typing.Optional[str]


# UpdateProfileRequestTypeDef

### profileId
- **Type**: <class 'str'>
- **Required**: Yes

### acceptRoleSessionName
- **Type**: typing.Optional[bool]

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


# UpdateTrustAnchorRequestTypeDef

### trustAnchorId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rolesanywhere_classes.SourceTypeDef]


