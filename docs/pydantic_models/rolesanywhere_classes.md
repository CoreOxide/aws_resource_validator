# Rolesanywhere Classes

# AttributeMapping

### certificateField
- **Type**: typing.Optional[typing.Literal['x509Issuer', 'x509SAN', 'x509Subject']]

### mappingRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.MappingRule]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateProfileRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### roleArns
- **Type**: typing.List[str]
- **Required**: Yes

### acceptRoleSessionName
- **Type**: typing.Optional[bool]

### durationSeconds
- **Type**: typing.Optional[int]

### enabled
- **Type**: typing.Optional[bool]

### managedPolicyArns
- **Type**: typing.Optional[typing.List[str]]

### requireInstanceProperties
- **Type**: typing.Optional[bool]

### sessionPolicy
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.Tag]]


# CreateTrustAnchorRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.Source'>
- **Required**: Yes

### enabled
- **Type**: typing.Optional[bool]

### notificationSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.NotificationSetting]]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.Tag]]


# CredentialSummary

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


# CrlDetail

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


# CrlDetailResponse

### crl
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.CrlDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAttributeMappingRequest

### certificateField
- **Type**: typing.Literal['x509Issuer', 'x509SAN', 'x509Subject']
- **Required**: Yes

### profileId
- **Type**: <class 'str'>
- **Required**: Yes

### specifiers
- **Type**: typing.Optional[typing.List[str]]


# DeleteAttributeMappingResponse

### profile
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.ProfileDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.ResponseMetadata'>
- **Required**: Yes


# ImportCrlRequest

### crlData
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.Tag]]


# InstanceProperty

### failed
- **Type**: typing.Optional[bool]

### properties
- **Type**: typing.Optional[typing.Dict[str, str]]

### seenAt
- **Type**: typing.Optional[datetime.datetime]


# ListCrlsResponse

### crls
- **Type**: typing.List[aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.CrlDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProfilesResponse

### profiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.ProfileDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRequest

### nextToken
- **Type**: typing.Optional[str]

### pageSize
- **Type**: typing.Optional[int]


# ListRequestPaginate

### pageSize
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.PaginatorConfig]


# ListRequestPaginateExtra

### pageSize
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.PaginatorConfig]


# ListRequestPaginateExtraExtra

### pageSize
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.PaginatorConfig]


# ListRequestPaginateExtraExtraExtra

### pageSize
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.PaginatorConfig]


# ListRequestRequest

### nextToken
- **Type**: typing.Optional[str]

### pageSize
- **Type**: typing.Optional[int]


# ListRequestRequestExtra

### nextToken
- **Type**: typing.Optional[str]

### pageSize
- **Type**: typing.Optional[int]


# ListRequestRequestExtraExtra

### nextToken
- **Type**: typing.Optional[str]

### pageSize
- **Type**: typing.Optional[int]


# ListSubjectsResponse

### subjects
- **Type**: typing.List[aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.SubjectSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.ResponseMetadata'>
- **Required**: Yes


# ListTrustAnchorsResponse

### trustAnchors
- **Type**: typing.List[aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.TrustAnchorDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# MappingRule

### specifier
- **Type**: <class 'str'>
- **Required**: Yes


# NotificationSetting

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


# NotificationSettingDetail

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


# NotificationSettingKey

### event
- **Type**: typing.Literal['CA_CERTIFICATE_EXPIRY', 'END_ENTITY_CERTIFICATE_EXPIRY']
- **Required**: Yes

### channel
- **Type**: typing.Optional[typing.Literal['ALL']]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProfileDetail

### acceptRoleSessionName
- **Type**: typing.Optional[bool]

### attributeMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.AttributeMapping]]

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


# ProfileDetailResponse

### profile
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.ProfileDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.ResponseMetadata'>
- **Required**: Yes


# PutAttributeMappingRequest

### certificateField
- **Type**: typing.Literal['x509Issuer', 'x509SAN', 'x509Subject']
- **Required**: Yes

### mappingRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.MappingRule]
- **Required**: Yes

### profileId
- **Type**: <class 'str'>
- **Required**: Yes


# PutAttributeMappingResponse

### profile
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.ProfileDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.ResponseMetadata'>
- **Required**: Yes


# PutNotificationSettingsRequest

### notificationSettings
- **Type**: typing.List[aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.NotificationSetting]
- **Required**: Yes

### trustAnchorId
- **Type**: <class 'str'>
- **Required**: Yes


# PutNotificationSettingsResponse

### trustAnchor
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.TrustAnchorDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.ResponseMetadata'>
- **Required**: Yes


# ResetNotificationSettingsRequest

### notificationSettingKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.NotificationSettingKey]
- **Required**: Yes

### trustAnchorId
- **Type**: <class 'str'>
- **Required**: Yes


# ResetNotificationSettingsResponse

### trustAnchor
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.TrustAnchorDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.ResponseMetadata'>
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


# ScalarCrlRequest

### crlId
- **Type**: <class 'str'>
- **Required**: Yes


# ScalarCrlRequestRequest

### crlId
- **Type**: <class 'str'>
- **Required**: Yes


# ScalarCrlRequestRequestExtra

### crlId
- **Type**: <class 'str'>
- **Required**: Yes


# ScalarCrlRequestRequestExtraExtra

### crlId
- **Type**: <class 'str'>
- **Required**: Yes


# ScalarProfileRequest

### profileId
- **Type**: <class 'str'>
- **Required**: Yes


# ScalarProfileRequestRequest

### profileId
- **Type**: <class 'str'>
- **Required**: Yes


# ScalarProfileRequestRequestExtra

### profileId
- **Type**: <class 'str'>
- **Required**: Yes


# ScalarProfileRequestRequestExtraExtra

### profileId
- **Type**: <class 'str'>
- **Required**: Yes


# ScalarSubjectRequest

### subjectId
- **Type**: <class 'str'>
- **Required**: Yes


# ScalarTrustAnchorRequest

### trustAnchorId
- **Type**: <class 'str'>
- **Required**: Yes


# ScalarTrustAnchorRequestRequest

### trustAnchorId
- **Type**: <class 'str'>
- **Required**: Yes


# ScalarTrustAnchorRequestRequestExtra

### trustAnchorId
- **Type**: <class 'str'>
- **Required**: Yes


# ScalarTrustAnchorRequestRequestExtraExtra

### trustAnchorId
- **Type**: <class 'str'>
- **Required**: Yes


# Source

### sourceData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.SourceData]

### sourceType
- **Type**: typing.Optional[typing.Literal['AWS_ACM_PCA', 'CERTIFICATE_BUNDLE', 'SELF_SIGNED_REPOSITORY']]


# SourceData

### acmPcaArn
- **Type**: typing.Optional[str]

### x509CertificateData
- **Type**: typing.Optional[str]


# SubjectDetail

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### credentials
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.CredentialSummary]]

### enabled
- **Type**: typing.Optional[bool]

### instanceProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.InstanceProperty]]

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


# SubjectDetailResponse

### subject
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.SubjectDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.ResponseMetadata'>
- **Required**: Yes


# SubjectSummary

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


# Tag

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.Tag]
- **Required**: Yes


# TrustAnchorDetail

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### enabled
- **Type**: typing.Optional[bool]

### name
- **Type**: typing.Optional[str]

### notificationSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.NotificationSettingDetail]]

### source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.Source]

### trustAnchorArn
- **Type**: typing.Optional[str]

### trustAnchorId
- **Type**: typing.Optional[str]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# TrustAnchorDetailResponse

### trustAnchor
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.TrustAnchorDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.ResponseMetadata'>
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateCrlRequest

### crlId
- **Type**: <class 'str'>
- **Required**: Yes

### crlData
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]

### name
- **Type**: typing.Optional[str]


# UpdateProfileRequest

### profileId
- **Type**: <class 'str'>
- **Required**: Yes

### acceptRoleSessionName
- **Type**: typing.Optional[bool]

### durationSeconds
- **Type**: typing.Optional[int]

### managedPolicyArns
- **Type**: typing.Optional[typing.List[str]]

### name
- **Type**: typing.Optional[str]

### roleArns
- **Type**: typing.Optional[typing.List[str]]

### sessionPolicy
- **Type**: typing.Optional[str]


# UpdateTrustAnchorRequest

### trustAnchorId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_classes.Source]


