# Pydantic Models in appstream_classes

# AccessEndpointTypeDef

### EndpointType
- **Type**: typing.Literal['STREAMING']
- **Required**: Yes

### VpceId
- **Type**: typing.Optional[str]


# AppBlockBuilderAppBlockAssociationTypeDef

### AppBlockArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppBlockBuilderName
- **Type**: <class 'str'>
- **Required**: Yes


# AppBlockBuilderStateChangeReasonTypeDef

### Code
- **Type**: typing.Optional[typing.Literal['INTERNAL_ERROR']]

### Message
- **Type**: typing.Optional[str]


# AppBlockBuilderTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Platform
- **Type**: typing.Literal['WINDOWS_SERVER_2019']
- **Required**: Yes

### InstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### VpcConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.VpcConfigTypeDef'>
- **Required**: Yes

### State
- **Type**: typing.Literal['RUNNING', 'STARTING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EnableDefaultInternetAccess
- **Type**: typing.Optional[bool]

### IamRoleArn
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### AppBlockBuilderErrors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.ResourceErrorTypeDef]]

### StateChangeReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.AppBlockBuilderStateChangeReasonTypeDef]

### AccessEndpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.AccessEndpointTypeDef]]


# AppBlockTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### SourceS3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.S3LocationTypeDef]

### SetupScriptDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.ScriptDetailsTypeDef]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### PostSetupScriptDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.ScriptDetailsTypeDef]

### PackagingType
- **Type**: typing.Optional[typing.Literal['APPSTREAM2', 'CUSTOM']]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### AppBlockErrors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.ErrorDetailsTypeDef]]


# ApplicationFleetAssociationTypeDef

### FleetName
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes


# ApplicationSettingsResponseTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### SettingsGroup
- **Type**: typing.Optional[str]

### S3BucketName
- **Type**: typing.Optional[str]


# ApplicationSettingsTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### SettingsGroup
- **Type**: typing.Optional[str]


# ApplicationTypeDef

### Name
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### IconURL
- **Type**: typing.Optional[str]

### LaunchPath
- **Type**: typing.Optional[str]

### LaunchParameters
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### Metadata
- **Type**: typing.Optional[typing.Dict[str, str]]

### WorkingDirectory
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### AppBlockArn
- **Type**: typing.Optional[str]

### IconS3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.S3LocationTypeDef]

### Platforms
- **Type**: typing.Optional[typing.List[typing.Literal['AMAZON_LINUX2', 'WINDOWS', 'WINDOWS_SERVER_2016', 'WINDOWS_SERVER_2019', 'WINDOWS_SERVER_2022']]]

### InstanceFamilies
- **Type**: typing.Optional[typing.List[str]]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]


# AssociateAppBlockBuilderAppBlockRequestRequestTypeDef

### AppBlockArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppBlockBuilderName
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateAppBlockBuilderAppBlockResultTypeDef

### AppBlockBuilderAppBlockAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.AppBlockBuilderAppBlockAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateApplicationFleetRequestRequestTypeDef

### FleetName
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateApplicationFleetResultTypeDef

### ApplicationFleetAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ApplicationFleetAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateApplicationToEntitlementRequestRequestTypeDef

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### EntitlementName
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateFleetRequestRequestTypeDef

### FleetName
- **Type**: <class 'str'>
- **Required**: Yes

### StackName
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchAssociateUserStackRequestRequestTypeDef

### UserStackAssociations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.appstream_classes.UserStackAssociationTypeDef]
- **Required**: Yes


# BatchAssociateUserStackResultTypeDef

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.UserStackAssociationErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDisassociateUserStackRequestRequestTypeDef

### UserStackAssociations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.appstream_classes.UserStackAssociationTypeDef]
- **Required**: Yes


# BatchDisassociateUserStackResultTypeDef

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.UserStackAssociationErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CertificateBasedAuthPropertiesTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'ENABLED_NO_DIRECTORY_LOGIN_FALLBACK']]

### CertificateAuthorityArn
- **Type**: typing.Optional[str]


# ComputeCapacityStatusTypeDef

### Desired
- **Type**: <class 'int'>
- **Required**: Yes

### Running
- **Type**: typing.Optional[int]

### InUse
- **Type**: typing.Optional[int]

### Available
- **Type**: typing.Optional[int]

### DesiredUserSessions
- **Type**: typing.Optional[int]

### AvailableUserSessions
- **Type**: typing.Optional[int]

### ActiveUserSessions
- **Type**: typing.Optional[int]

### ActualUserSessions
- **Type**: typing.Optional[int]


# ComputeCapacityTypeDef

### DesiredInstances
- **Type**: typing.Optional[int]

### DesiredSessions
- **Type**: typing.Optional[int]


# CopyImageRequestRequestTypeDef

### SourceImageName
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationImageName
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationRegion
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationImageDescription
- **Type**: typing.Optional[str]


# CopyImageResponseTypeDef

### DestinationImageName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAppBlockBuilderRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Platform
- **Type**: typing.Literal['WINDOWS_SERVER_2019']
- **Required**: Yes

### InstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### VpcConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.VpcConfigTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### EnableDefaultInternetAccess
- **Type**: typing.Optional[bool]

### IamRoleArn
- **Type**: typing.Optional[str]

### AccessEndpoints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appstream_classes.AccessEndpointTypeDef]]


# CreateAppBlockBuilderResultTypeDef

### AppBlockBuilder
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.AppBlockBuilderTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAppBlockBuilderStreamingURLRequestRequestTypeDef

### AppBlockBuilderName
- **Type**: <class 'str'>
- **Required**: Yes

### Validity
- **Type**: typing.Optional[int]


# CreateAppBlockBuilderStreamingURLResultTypeDef

### StreamingURL
- **Type**: <class 'str'>
- **Required**: Yes

### Expires
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAppBlockRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SourceS3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.S3LocationTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### SetupScriptDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.ScriptDetailsTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### PostSetupScriptDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.ScriptDetailsTypeDef]

### PackagingType
- **Type**: typing.Optional[typing.Literal['APPSTREAM2', 'CUSTOM']]


# CreateAppBlockResultTypeDef

### AppBlock
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.AppBlockTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateApplicationRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IconS3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.S3LocationTypeDef'>
- **Required**: Yes

### LaunchPath
- **Type**: <class 'str'>
- **Required**: Yes

### Platforms
- **Type**: typing.Sequence[typing.Literal['AMAZON_LINUX2', 'WINDOWS', 'WINDOWS_SERVER_2016', 'WINDOWS_SERVER_2019', 'WINDOWS_SERVER_2022']]
- **Required**: Yes

### InstanceFamilies
- **Type**: typing.Sequence[str]
- **Required**: Yes

### AppBlockArn
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### WorkingDirectory
- **Type**: typing.Optional[str]

### LaunchParameters
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateApplicationResultTypeDef

### Application
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ApplicationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDirectoryConfigRequestRequestTypeDef

### DirectoryName
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationalUnitDistinguishedNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ServiceAccountCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.ServiceAccountCredentialsTypeDef]

### CertificateBasedAuthProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.CertificateBasedAuthPropertiesTypeDef]


# CreateDirectoryConfigResultTypeDef

### DirectoryConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.DirectoryConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEntitlementRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### AppVisibility
- **Type**: typing.Literal['ALL', 'ASSOCIATED']
- **Required**: Yes

### Attributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.appstream_classes.EntitlementAttributeTypeDef]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# CreateEntitlementResultTypeDef

### Entitlement
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.EntitlementTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFleetRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### ImageName
- **Type**: typing.Optional[str]

### ImageArn
- **Type**: typing.Optional[str]

### FleetType
- **Type**: typing.Optional[typing.Literal['ALWAYS_ON', 'ELASTIC', 'ON_DEMAND']]

### ComputeCapacity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.ComputeCapacityTypeDef]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.VpcConfigTypeDef]

### MaxUserDurationInSeconds
- **Type**: typing.Optional[int]

### DisconnectTimeoutInSeconds
- **Type**: typing.Optional[int]

### Description
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### EnableDefaultInternetAccess
- **Type**: typing.Optional[bool]

### DomainJoinInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.DomainJoinInfoTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### IdleDisconnectTimeoutInSeconds
- **Type**: typing.Optional[int]

### IamRoleArn
- **Type**: typing.Optional[str]

### StreamView
- **Type**: typing.Optional[typing.Literal['APP', 'DESKTOP']]

### Platform
- **Type**: typing.Optional[typing.Literal['AMAZON_LINUX2', 'WINDOWS', 'WINDOWS_SERVER_2016', 'WINDOWS_SERVER_2019', 'WINDOWS_SERVER_2022']]

### MaxConcurrentSessions
- **Type**: typing.Optional[int]

### UsbDeviceFilterStrings
- **Type**: typing.Optional[typing.Sequence[str]]

### SessionScriptS3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.S3LocationTypeDef]

### MaxSessionsPerInstance
- **Type**: typing.Optional[int]


# CreateFleetResultTypeDef

### Fleet
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.FleetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateImageBuilderRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### ImageName
- **Type**: typing.Optional[str]

### ImageArn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.VpcConfigTypeDef]

### IamRoleArn
- **Type**: typing.Optional[str]

### EnableDefaultInternetAccess
- **Type**: typing.Optional[bool]

### DomainJoinInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.DomainJoinInfoTypeDef]

### AppstreamAgentVersion
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### AccessEndpoints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appstream_classes.AccessEndpointTypeDef]]


# CreateImageBuilderResultTypeDef

### ImageBuilder
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ImageBuilderTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateImageBuilderStreamingURLRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Validity
- **Type**: typing.Optional[int]


# CreateImageBuilderStreamingURLResultTypeDef

### StreamingURL
- **Type**: <class 'str'>
- **Required**: Yes

### Expires
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStackRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### StorageConnectors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appstream_classes.StorageConnectorTypeDef]]

### RedirectURL
- **Type**: typing.Optional[str]

### FeedbackURL
- **Type**: typing.Optional[str]

### UserSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appstream_classes.UserSettingTypeDef]]

### ApplicationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.ApplicationSettingsTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### AccessEndpoints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appstream_classes.AccessEndpointTypeDef]]

### EmbedHostDomains
- **Type**: typing.Optional[typing.Sequence[str]]

### StreamingExperienceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.StreamingExperienceSettingsTypeDef]


# CreateStackResultTypeDef

### Stack
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.StackTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStreamingURLRequestRequestTypeDef

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### FleetName
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationId
- **Type**: typing.Optional[str]

### Validity
- **Type**: typing.Optional[int]

### SessionContext
- **Type**: typing.Optional[str]


# CreateStreamingURLResultTypeDef

### StreamingURL
- **Type**: <class 'str'>
- **Required**: Yes

### Expires
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUpdatedImageRequestRequestTypeDef

### existingImageName
- **Type**: <class 'str'>
- **Required**: Yes

### newImageName
- **Type**: <class 'str'>
- **Required**: Yes

### newImageDescription
- **Type**: typing.Optional[str]

### newImageDisplayName
- **Type**: typing.Optional[str]

### newImageTags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### dryRun
- **Type**: typing.Optional[bool]


# CreateUpdatedImageResultTypeDef

### image
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ImageTypeDef'>
- **Required**: Yes

### canUpdateImage
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUsageReportSubscriptionResultTypeDef

### S3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### Schedule
- **Type**: typing.Literal['DAILY']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUserRequestRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationType
- **Type**: typing.Literal['API', 'AWS_AD', 'SAML', 'USERPOOL']
- **Required**: Yes

### MessageAction
- **Type**: typing.Optional[typing.Literal['RESEND', 'SUPPRESS']]

### FirstName
- **Type**: typing.Optional[str]

### LastName
- **Type**: typing.Optional[str]


# DeleteAppBlockBuilderRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAppBlockRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApplicationRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDirectoryConfigRequestRequestTypeDef

### DirectoryName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEntitlementRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### StackName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFleetRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteImageBuilderRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteImageBuilderResultTypeDef

### ImageBuilder
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ImageBuilderTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteImagePermissionsRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SharedAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteImageRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteImageResultTypeDef

### Image
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ImageTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteStackRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserRequestRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationType
- **Type**: typing.Literal['API', 'AWS_AD', 'SAML', 'USERPOOL']
- **Required**: Yes


# DescribeAppBlockBuilderAppBlockAssociationsRequestRequestTypeDef

### AppBlockArn
- **Type**: typing.Optional[str]

### AppBlockBuilderName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeAppBlockBuilderAppBlockAssociationsResultTypeDef

### AppBlockBuilderAppBlockAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.AppBlockBuilderAppBlockAssociationTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAppBlockBuildersRequestRequestTypeDef

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeAppBlockBuildersResultTypeDef

### AppBlockBuilders
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.AppBlockBuilderTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAppBlocksRequestRequestTypeDef

### Arns
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeAppBlocksResultTypeDef

### AppBlocks
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.AppBlockTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeApplicationFleetAssociationsRequestRequestTypeDef

### FleetName
- **Type**: typing.Optional[str]

### ApplicationArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeApplicationFleetAssociationsResultTypeDef

### ApplicationFleetAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.ApplicationFleetAssociationTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeApplicationsRequestRequestTypeDef

### Arns
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeApplicationsResultTypeDef

### Applications
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.ApplicationTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDirectoryConfigsRequestDescribeDirectoryConfigsPaginateTypeDef

### DirectoryNames
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.PaginatorConfigTypeDef]


# DescribeDirectoryConfigsRequestRequestTypeDef

### DirectoryNames
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeDirectoryConfigsResultTypeDef

### DirectoryConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.DirectoryConfigTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEntitlementsRequestRequestTypeDef

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeEntitlementsResultTypeDef

### Entitlements
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.EntitlementTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFleetsRequestDescribeFleetsPaginateTypeDef

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.PaginatorConfigTypeDef]


# DescribeFleetsRequestFleetStartedWaitTypeDef

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.WaiterConfigTypeDef]


# DescribeFleetsRequestFleetStoppedWaitTypeDef

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.WaiterConfigTypeDef]


# DescribeFleetsRequestRequestTypeDef

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetsResultPaginatorTypeDef

### Fleets
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.FleetPaginatorTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFleetsResultTypeDef

### Fleets
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.FleetTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeImageBuildersRequestDescribeImageBuildersPaginateTypeDef

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.PaginatorConfigTypeDef]


# DescribeImageBuildersRequestRequestTypeDef

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeImageBuildersResultPaginatorTypeDef

### ImageBuilders
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.ImageBuilderPaginatorTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeImageBuildersResultTypeDef

### ImageBuilders
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.ImageBuilderTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeImagePermissionsRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### SharedAwsAccountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]


# DescribeImagePermissionsResultTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SharedImagePermissionsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.SharedImagePermissionsTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeImagesRequestDescribeImagesPaginateTypeDef

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### Arns
- **Type**: typing.Optional[typing.Sequence[str]]

### Type
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'PUBLIC', 'SHARED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.PaginatorConfigTypeDef]


# DescribeImagesRequestRequestTypeDef

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### Arns
- **Type**: typing.Optional[typing.Sequence[str]]

### Type
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'PUBLIC', 'SHARED']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeImagesResultTypeDef

### Images
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.ImageTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSessionsRequestDescribeSessionsPaginateTypeDef

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### FleetName
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: typing.Optional[str]

### AuthenticationType
- **Type**: typing.Optional[typing.Literal['API', 'AWS_AD', 'SAML', 'USERPOOL']]

### InstanceId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.PaginatorConfigTypeDef]


# DescribeSessionsRequestRequestTypeDef

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### FleetName
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### AuthenticationType
- **Type**: typing.Optional[typing.Literal['API', 'AWS_AD', 'SAML', 'USERPOOL']]

### InstanceId
- **Type**: typing.Optional[str]


# DescribeSessionsResultTypeDef

### Sessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.SessionTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeStacksRequestDescribeStacksPaginateTypeDef

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.PaginatorConfigTypeDef]


# DescribeStacksRequestRequestTypeDef

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]


# DescribeStacksResultPaginatorTypeDef

### Stacks
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.StackPaginatorTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeStacksResultTypeDef

### Stacks
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.StackTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeUsageReportSubscriptionsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeUsageReportSubscriptionsResultTypeDef

### UsageReportSubscriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.UsageReportSubscriptionTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeUserStackAssociationsRequestDescribeUserStackAssociationsPaginateTypeDef

### StackName
- **Type**: typing.Optional[str]

### UserName
- **Type**: typing.Optional[str]

### AuthenticationType
- **Type**: typing.Optional[typing.Literal['API', 'AWS_AD', 'SAML', 'USERPOOL']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.PaginatorConfigTypeDef]


# DescribeUserStackAssociationsRequestRequestTypeDef

### StackName
- **Type**: typing.Optional[str]

### UserName
- **Type**: typing.Optional[str]

### AuthenticationType
- **Type**: typing.Optional[typing.Literal['API', 'AWS_AD', 'SAML', 'USERPOOL']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeUserStackAssociationsResultTypeDef

### UserStackAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.UserStackAssociationTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeUsersRequestDescribeUsersPaginateTypeDef

### AuthenticationType
- **Type**: typing.Literal['API', 'AWS_AD', 'SAML', 'USERPOOL']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.PaginatorConfigTypeDef]


# DescribeUsersRequestRequestTypeDef

### AuthenticationType
- **Type**: typing.Literal['API', 'AWS_AD', 'SAML', 'USERPOOL']
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeUsersResultTypeDef

### Users
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.UserTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DirectoryConfigTypeDef

### DirectoryName
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationalUnitDistinguishedNames
- **Type**: typing.Optional[typing.List[str]]

### ServiceAccountCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.ServiceAccountCredentialsTypeDef]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### CertificateBasedAuthProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.CertificateBasedAuthPropertiesTypeDef]


# DisableUserRequestRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationType
- **Type**: typing.Literal['API', 'AWS_AD', 'SAML', 'USERPOOL']
- **Required**: Yes


# DisassociateAppBlockBuilderAppBlockRequestRequestTypeDef

### AppBlockArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppBlockBuilderName
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateApplicationFleetRequestRequestTypeDef

### FleetName
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateApplicationFromEntitlementRequestRequestTypeDef

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### EntitlementName
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateFleetRequestRequestTypeDef

### FleetName
- **Type**: <class 'str'>
- **Required**: Yes

### StackName
- **Type**: <class 'str'>
- **Required**: Yes


# DomainJoinInfoTypeDef

### DirectoryName
- **Type**: typing.Optional[str]

### OrganizationalUnitDistinguishedName
- **Type**: typing.Optional[str]


# EnableUserRequestRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationType
- **Type**: typing.Literal['API', 'AWS_AD', 'SAML', 'USERPOOL']
- **Required**: Yes


# EntitledApplicationTypeDef

### ApplicationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# EntitlementAttributeTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# EntitlementTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### AppVisibility
- **Type**: typing.Literal['ALL', 'ASSOCIATED']
- **Required**: Yes

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.EntitlementAttributeTypeDef]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# ErrorDetailsTypeDef

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# ExpireSessionRequestRequestTypeDef

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes


# FleetErrorTypeDef

### ErrorCode
- **Type**: typing.Optional[typing.Literal['DOMAIN_JOIN_ERROR_ACCESS_DENIED', 'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED', 'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND', 'DOMAIN_JOIN_ERROR_INVALID_PARAMETER', 'DOMAIN_JOIN_ERROR_LOGON_FAILURE', 'DOMAIN_JOIN_ERROR_MORE_DATA', 'DOMAIN_JOIN_ERROR_NOT_SUPPORTED', 'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN', 'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR', 'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME', 'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED', 'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED', 'FLEET_INSTANCE_PROVISIONING_FAILURE', 'FLEET_STOPPED', 'IAM_SERVICE_ROLE_IS_MISSING', 'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION', 'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION', 'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION', 'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION', 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION', 'IGW_NOT_ATTACHED', 'IMAGE_NOT_FOUND', 'INTERNAL_SERVICE_ERROR', 'INVALID_SUBNET_CONFIGURATION', 'MACHINE_ROLE_IS_MISSING', 'NETWORK_INTERFACE_LIMIT_EXCEEDED', 'SECURITY_GROUPS_NOT_FOUND', 'STS_DISABLED_IN_REGION', 'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES', 'SUBNET_NOT_FOUND']]

### ErrorMessage
- **Type**: typing.Optional[str]


# FleetPaginatorTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeCapacityStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ComputeCapacityStatusTypeDef'>
- **Required**: Yes

### State
- **Type**: typing.Literal['RUNNING', 'STARTING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ImageName
- **Type**: typing.Optional[str]

### ImageArn
- **Type**: typing.Optional[str]

### FleetType
- **Type**: typing.Optional[typing.Literal['ALWAYS_ON', 'ELASTIC', 'ON_DEMAND']]

### MaxUserDurationInSeconds
- **Type**: typing.Optional[int]

### DisconnectTimeoutInSeconds
- **Type**: typing.Optional[int]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.VpcConfigPaginatorTypeDef]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### FleetErrors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.FleetErrorTypeDef]]

### EnableDefaultInternetAccess
- **Type**: typing.Optional[bool]

### DomainJoinInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.DomainJoinInfoTypeDef]

### IdleDisconnectTimeoutInSeconds
- **Type**: typing.Optional[int]

### IamRoleArn
- **Type**: typing.Optional[str]

### StreamView
- **Type**: typing.Optional[typing.Literal['APP', 'DESKTOP']]

### Platform
- **Type**: typing.Optional[typing.Literal['AMAZON_LINUX2', 'WINDOWS', 'WINDOWS_SERVER_2016', 'WINDOWS_SERVER_2019', 'WINDOWS_SERVER_2022']]

### MaxConcurrentSessions
- **Type**: typing.Optional[int]

### UsbDeviceFilterStrings
- **Type**: typing.Optional[typing.List[str]]

### SessionScriptS3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.S3LocationTypeDef]

### MaxSessionsPerInstance
- **Type**: typing.Optional[int]


# FleetTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeCapacityStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ComputeCapacityStatusTypeDef'>
- **Required**: Yes

### State
- **Type**: typing.Literal['RUNNING', 'STARTING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ImageName
- **Type**: typing.Optional[str]

### ImageArn
- **Type**: typing.Optional[str]

### FleetType
- **Type**: typing.Optional[typing.Literal['ALWAYS_ON', 'ELASTIC', 'ON_DEMAND']]

### MaxUserDurationInSeconds
- **Type**: typing.Optional[int]

### DisconnectTimeoutInSeconds
- **Type**: typing.Optional[int]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.VpcConfigTypeDef]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### FleetErrors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.FleetErrorTypeDef]]

### EnableDefaultInternetAccess
- **Type**: typing.Optional[bool]

### DomainJoinInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.DomainJoinInfoTypeDef]

### IdleDisconnectTimeoutInSeconds
- **Type**: typing.Optional[int]

### IamRoleArn
- **Type**: typing.Optional[str]

### StreamView
- **Type**: typing.Optional[typing.Literal['APP', 'DESKTOP']]

### Platform
- **Type**: typing.Optional[typing.Literal['AMAZON_LINUX2', 'WINDOWS', 'WINDOWS_SERVER_2016', 'WINDOWS_SERVER_2019', 'WINDOWS_SERVER_2022']]

### MaxConcurrentSessions
- **Type**: typing.Optional[int]

### UsbDeviceFilterStrings
- **Type**: typing.Optional[typing.List[str]]

### SessionScriptS3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.S3LocationTypeDef]

### MaxSessionsPerInstance
- **Type**: typing.Optional[int]


# ImageBuilderPaginatorTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: typing.Optional[str]

### ImageArn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.VpcConfigPaginatorTypeDef]

### InstanceType
- **Type**: typing.Optional[str]

### Platform
- **Type**: typing.Optional[typing.Literal['AMAZON_LINUX2', 'WINDOWS', 'WINDOWS_SERVER_2016', 'WINDOWS_SERVER_2019', 'WINDOWS_SERVER_2022']]

### IamRoleArn
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['DELETING', 'FAILED', 'PENDING', 'PENDING_QUALIFICATION', 'REBOOTING', 'RUNNING', 'SNAPSHOTTING', 'STOPPED', 'STOPPING', 'UPDATING', 'UPDATING_AGENT']]

### StateChangeReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.ImageBuilderStateChangeReasonTypeDef]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### EnableDefaultInternetAccess
- **Type**: typing.Optional[bool]

### DomainJoinInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.DomainJoinInfoTypeDef]

### NetworkAccessConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.NetworkAccessConfigurationTypeDef]

### ImageBuilderErrors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.ResourceErrorTypeDef]]

### AppstreamAgentVersion
- **Type**: typing.Optional[str]

### AccessEndpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.AccessEndpointTypeDef]]


# ImageBuilderStateChangeReasonTypeDef

### Code
- **Type**: typing.Optional[typing.Literal['IMAGE_UNAVAILABLE', 'INTERNAL_ERROR']]

### Message
- **Type**: typing.Optional[str]


# ImageBuilderTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: typing.Optional[str]

### ImageArn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.VpcConfigTypeDef]

### InstanceType
- **Type**: typing.Optional[str]

### Platform
- **Type**: typing.Optional[typing.Literal['AMAZON_LINUX2', 'WINDOWS', 'WINDOWS_SERVER_2016', 'WINDOWS_SERVER_2019', 'WINDOWS_SERVER_2022']]

### IamRoleArn
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['DELETING', 'FAILED', 'PENDING', 'PENDING_QUALIFICATION', 'REBOOTING', 'RUNNING', 'SNAPSHOTTING', 'STOPPED', 'STOPPING', 'UPDATING', 'UPDATING_AGENT']]

### StateChangeReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.ImageBuilderStateChangeReasonTypeDef]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### EnableDefaultInternetAccess
- **Type**: typing.Optional[bool]

### DomainJoinInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.DomainJoinInfoTypeDef]

### NetworkAccessConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.NetworkAccessConfigurationTypeDef]

### ImageBuilderErrors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.ResourceErrorTypeDef]]

### AppstreamAgentVersion
- **Type**: typing.Optional[str]

### AccessEndpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.AccessEndpointTypeDef]]


# ImagePermissionsTypeDef

### allowFleet
- **Type**: typing.Optional[bool]

### allowImageBuilder
- **Type**: typing.Optional[bool]


# ImageStateChangeReasonTypeDef

### Code
- **Type**: typing.Optional[typing.Literal['IMAGE_BUILDER_NOT_AVAILABLE', 'IMAGE_COPY_FAILURE', 'INTERNAL_ERROR']]

### Message
- **Type**: typing.Optional[str]


# ImageTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: typing.Optional[str]

### BaseImageArn
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'COPYING', 'CREATING', 'DELETING', 'FAILED', 'IMPORTING', 'PENDING']]

### Visibility
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'PUBLIC', 'SHARED']]

### ImageBuilderSupported
- **Type**: typing.Optional[bool]

### ImageBuilderName
- **Type**: typing.Optional[str]

### Platform
- **Type**: typing.Optional[typing.Literal['AMAZON_LINUX2', 'WINDOWS', 'WINDOWS_SERVER_2016', 'WINDOWS_SERVER_2019', 'WINDOWS_SERVER_2022']]

### Description
- **Type**: typing.Optional[str]

### StateChangeReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.ImageStateChangeReasonTypeDef]

### Applications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.ApplicationTypeDef]]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### PublicBaseImageReleasedDate
- **Type**: typing.Optional[datetime.datetime]

### AppstreamAgentVersion
- **Type**: typing.Optional[str]

### ImagePermissions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.ImagePermissionsTypeDef]

### ImageErrors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.ResourceErrorTypeDef]]


# LastReportGenerationExecutionErrorTypeDef

### ErrorCode
- **Type**: typing.Optional[typing.Literal['ACCESS_DENIED', 'INTERNAL_SERVICE_ERROR', 'RESOURCE_NOT_FOUND']]

### ErrorMessage
- **Type**: typing.Optional[str]


# ListAssociatedFleetsRequestListAssociatedFleetsPaginateTypeDef

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.PaginatorConfigTypeDef]


# ListAssociatedFleetsRequestRequestTypeDef

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAssociatedFleetsResultTypeDef

### Names
- **Type**: typing.List[str]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAssociatedStacksRequestListAssociatedStacksPaginateTypeDef

### FleetName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.PaginatorConfigTypeDef]


# ListAssociatedStacksRequestRequestTypeDef

### FleetName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAssociatedStacksResultTypeDef

### Names
- **Type**: typing.List[str]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEntitledApplicationsRequestRequestTypeDef

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### EntitlementName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEntitledApplicationsResultTypeDef

### EntitledApplications
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.EntitledApplicationTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# NetworkAccessConfigurationTypeDef

### EniPrivateIpAddress
- **Type**: typing.Optional[str]

### EniId
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ResourceErrorTypeDef

### ErrorCode
- **Type**: typing.Optional[typing.Literal['DOMAIN_JOIN_ERROR_ACCESS_DENIED', 'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED', 'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND', 'DOMAIN_JOIN_ERROR_INVALID_PARAMETER', 'DOMAIN_JOIN_ERROR_LOGON_FAILURE', 'DOMAIN_JOIN_ERROR_MORE_DATA', 'DOMAIN_JOIN_ERROR_NOT_SUPPORTED', 'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN', 'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR', 'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME', 'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED', 'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED', 'FLEET_INSTANCE_PROVISIONING_FAILURE', 'FLEET_STOPPED', 'IAM_SERVICE_ROLE_IS_MISSING', 'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION', 'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION', 'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION', 'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION', 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION', 'IGW_NOT_ATTACHED', 'IMAGE_NOT_FOUND', 'INTERNAL_SERVICE_ERROR', 'INVALID_SUBNET_CONFIGURATION', 'MACHINE_ROLE_IS_MISSING', 'NETWORK_INTERFACE_LIMIT_EXCEEDED', 'SECURITY_GROUPS_NOT_FOUND', 'STS_DISABLED_IN_REGION', 'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES', 'SUBNET_NOT_FOUND']]

### ErrorMessage
- **Type**: typing.Optional[str]

### ErrorTimestamp
- **Type**: typing.Optional[datetime.datetime]


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


# S3LocationTypeDef

### S3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### S3Key
- **Type**: typing.Optional[str]


# ScriptDetailsTypeDef

### ScriptS3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.S3LocationTypeDef'>
- **Required**: Yes

### ExecutablePath
- **Type**: <class 'str'>
- **Required**: Yes

### TimeoutInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### ExecutableParameters
- **Type**: typing.Optional[str]


# ServiceAccountCredentialsTypeDef

### AccountName
- **Type**: <class 'str'>
- **Required**: Yes

### AccountPassword
- **Type**: <class 'str'>
- **Required**: Yes


# SessionTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### FleetName
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'EXPIRED', 'PENDING']
- **Required**: Yes

### ConnectionState
- **Type**: typing.Optional[typing.Literal['CONNECTED', 'NOT_CONNECTED']]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### MaxExpirationTime
- **Type**: typing.Optional[datetime.datetime]

### AuthenticationType
- **Type**: typing.Optional[typing.Literal['API', 'AWS_AD', 'SAML', 'USERPOOL']]

### NetworkAccessConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.NetworkAccessConfigurationTypeDef]

### InstanceId
- **Type**: typing.Optional[str]


# SharedImagePermissionsTypeDef

### sharedAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### imagePermissions
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ImagePermissionsTypeDef'>
- **Required**: Yes


# StackErrorTypeDef

### ErrorCode
- **Type**: typing.Optional[typing.Literal['INTERNAL_SERVICE_ERROR', 'STORAGE_CONNECTOR_ERROR']]

### ErrorMessage
- **Type**: typing.Optional[str]


# StackPaginatorTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### StorageConnectors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.StorageConnectorPaginatorTypeDef]]

### RedirectURL
- **Type**: typing.Optional[str]

### FeedbackURL
- **Type**: typing.Optional[str]

### StackErrors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.StackErrorTypeDef]]

### UserSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.UserSettingTypeDef]]

### ApplicationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.ApplicationSettingsResponseTypeDef]

### AccessEndpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.AccessEndpointTypeDef]]

### EmbedHostDomains
- **Type**: typing.Optional[typing.List[str]]

### StreamingExperienceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.StreamingExperienceSettingsTypeDef]


# StackTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### StorageConnectors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.StorageConnectorTypeDef]]

### RedirectURL
- **Type**: typing.Optional[str]

### FeedbackURL
- **Type**: typing.Optional[str]

### StackErrors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.StackErrorTypeDef]]

### UserSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.UserSettingTypeDef]]

### ApplicationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.ApplicationSettingsResponseTypeDef]

### AccessEndpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.AccessEndpointTypeDef]]

### EmbedHostDomains
- **Type**: typing.Optional[typing.List[str]]

### StreamingExperienceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.StreamingExperienceSettingsTypeDef]


# StartAppBlockBuilderRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# StartAppBlockBuilderResultTypeDef

### AppBlockBuilder
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.AppBlockBuilderTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartFleetRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# StartImageBuilderRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AppstreamAgentVersion
- **Type**: typing.Optional[str]


# StartImageBuilderResultTypeDef

### ImageBuilder
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ImageBuilderTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopAppBlockBuilderRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# StopAppBlockBuilderResultTypeDef

### AppBlockBuilder
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.AppBlockBuilderTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopFleetRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# StopImageBuilderRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# StopImageBuilderResultTypeDef

### ImageBuilder
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ImageBuilderTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StorageConnectorPaginatorTypeDef

### ConnectorType
- **Type**: typing.Literal['GOOGLE_DRIVE', 'HOMEFOLDERS', 'ONE_DRIVE']
- **Required**: Yes

### ResourceIdentifier
- **Type**: typing.Optional[str]

### Domains
- **Type**: typing.Optional[typing.List[str]]


# StorageConnectorTypeDef

### ConnectorType
- **Type**: typing.Literal['GOOGLE_DRIVE', 'HOMEFOLDERS', 'ONE_DRIVE']
- **Required**: Yes

### ResourceIdentifier
- **Type**: typing.Optional[str]

### Domains
- **Type**: typing.Optional[typing.Sequence[str]]


# StreamingExperienceSettingsTypeDef

### PreferredProtocol
- **Type**: typing.Optional[typing.Literal['TCP', 'UDP']]


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


# UpdateAppBlockBuilderRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### Platform
- **Type**: typing.Optional[typing.Literal['AMAZON_LINUX2', 'WINDOWS', 'WINDOWS_SERVER_2016', 'WINDOWS_SERVER_2019', 'WINDOWS_SERVER_2022']]

### InstanceType
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.VpcConfigTypeDef]

### EnableDefaultInternetAccess
- **Type**: typing.Optional[bool]

### IamRoleArn
- **Type**: typing.Optional[str]

### AccessEndpoints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appstream_classes.AccessEndpointTypeDef]]

### AttributesToDelete
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ACCESS_ENDPOINTS', 'IAM_ROLE_ARN', 'VPC_CONFIGURATION_SECURITY_GROUP_IDS']]]


# UpdateAppBlockBuilderResultTypeDef

### AppBlockBuilder
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.AppBlockBuilderTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateApplicationRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### IconS3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.S3LocationTypeDef]

### LaunchPath
- **Type**: typing.Optional[str]

### WorkingDirectory
- **Type**: typing.Optional[str]

### LaunchParameters
- **Type**: typing.Optional[str]

### AppBlockArn
- **Type**: typing.Optional[str]

### AttributesToDelete
- **Type**: typing.Optional[typing.Sequence[typing.Literal['LAUNCH_PARAMETERS', 'WORKING_DIRECTORY']]]


# UpdateApplicationResultTypeDef

### Application
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ApplicationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDirectoryConfigRequestRequestTypeDef

### DirectoryName
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationalUnitDistinguishedNames
- **Type**: typing.Optional[typing.Sequence[str]]

### ServiceAccountCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.ServiceAccountCredentialsTypeDef]

### CertificateBasedAuthProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.CertificateBasedAuthPropertiesTypeDef]


# UpdateDirectoryConfigResultTypeDef

### DirectoryConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.DirectoryConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEntitlementRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### AppVisibility
- **Type**: typing.Optional[typing.Literal['ALL', 'ASSOCIATED']]

### Attributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appstream_classes.EntitlementAttributeTypeDef]]


# UpdateEntitlementResultTypeDef

### Entitlement
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.EntitlementTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFleetRequestRequestTypeDef

### ImageName
- **Type**: typing.Optional[str]

### ImageArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[str]

### ComputeCapacity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.ComputeCapacityTypeDef]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.VpcConfigTypeDef]

### MaxUserDurationInSeconds
- **Type**: typing.Optional[int]

### DisconnectTimeoutInSeconds
- **Type**: typing.Optional[int]

### DeleteVpcConfig
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### EnableDefaultInternetAccess
- **Type**: typing.Optional[bool]

### DomainJoinInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.DomainJoinInfoTypeDef]

### IdleDisconnectTimeoutInSeconds
- **Type**: typing.Optional[int]

### AttributesToDelete
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DOMAIN_JOIN_INFO', 'IAM_ROLE_ARN', 'MAX_SESSIONS_PER_INSTANCE', 'SESSION_SCRIPT_S3_LOCATION', 'USB_DEVICE_FILTER_STRINGS', 'VPC_CONFIGURATION', 'VPC_CONFIGURATION_SECURITY_GROUP_IDS']]]

### IamRoleArn
- **Type**: typing.Optional[str]

### StreamView
- **Type**: typing.Optional[typing.Literal['APP', 'DESKTOP']]

### Platform
- **Type**: typing.Optional[typing.Literal['AMAZON_LINUX2', 'WINDOWS', 'WINDOWS_SERVER_2016', 'WINDOWS_SERVER_2019', 'WINDOWS_SERVER_2022']]

### MaxConcurrentSessions
- **Type**: typing.Optional[int]

### UsbDeviceFilterStrings
- **Type**: typing.Optional[typing.Sequence[str]]

### SessionScriptS3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.S3LocationTypeDef]

### MaxSessionsPerInstance
- **Type**: typing.Optional[int]


# UpdateFleetResultTypeDef

### Fleet
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.FleetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateImagePermissionsRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SharedAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ImagePermissions
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ImagePermissionsTypeDef'>
- **Required**: Yes


# UpdateStackRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### StorageConnectors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appstream_classes.StorageConnectorTypeDef]]

### DeleteStorageConnectors
- **Type**: typing.Optional[bool]

### RedirectURL
- **Type**: typing.Optional[str]

### FeedbackURL
- **Type**: typing.Optional[str]

### AttributesToDelete
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ACCESS_ENDPOINTS', 'EMBED_HOST_DOMAINS', 'FEEDBACK_URL', 'IAM_ROLE_ARN', 'REDIRECT_URL', 'STORAGE_CONNECTORS', 'STORAGE_CONNECTOR_GOOGLE_DRIVE', 'STORAGE_CONNECTOR_HOMEFOLDERS', 'STORAGE_CONNECTOR_ONE_DRIVE', 'STREAMING_EXPERIENCE_SETTINGS', 'THEME_NAME', 'USER_SETTINGS']]]

### UserSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appstream_classes.UserSettingTypeDef]]

### ApplicationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.ApplicationSettingsTypeDef]

### AccessEndpoints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appstream_classes.AccessEndpointTypeDef]]

### EmbedHostDomains
- **Type**: typing.Optional[typing.Sequence[str]]

### StreamingExperienceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.StreamingExperienceSettingsTypeDef]


# UpdateStackResultTypeDef

### Stack
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.StackTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UsageReportSubscriptionTypeDef

### S3BucketName
- **Type**: typing.Optional[str]

### Schedule
- **Type**: typing.Optional[typing.Literal['DAILY']]

### LastGeneratedReportDate
- **Type**: typing.Optional[datetime.datetime]

### SubscriptionErrors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.LastReportGenerationExecutionErrorTypeDef]]


# UserSettingTypeDef

### Action
- **Type**: typing.Literal['CLIPBOARD_COPY_FROM_LOCAL_DEVICE', 'CLIPBOARD_COPY_TO_LOCAL_DEVICE', 'DOMAIN_PASSWORD_SIGNIN', 'DOMAIN_SMART_CARD_SIGNIN', 'FILE_DOWNLOAD', 'FILE_UPLOAD', 'PRINTING_TO_LOCAL_DEVICE']
- **Required**: Yes

### Permission
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### MaximumLength
- **Type**: typing.Optional[int]


# UserStackAssociationErrorTypeDef

### UserStackAssociation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.UserStackAssociationTypeDef]

### ErrorCode
- **Type**: typing.Optional[typing.Literal['DIRECTORY_NOT_FOUND', 'INTERNAL_ERROR', 'STACK_NOT_FOUND', 'USER_NAME_NOT_FOUND']]

### ErrorMessage
- **Type**: typing.Optional[str]


# UserStackAssociationTypeDef

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationType
- **Type**: typing.Literal['API', 'AWS_AD', 'SAML', 'USERPOOL']
- **Required**: Yes

### SendEmailNotification
- **Type**: typing.Optional[bool]


# UserTypeDef

### AuthenticationType
- **Type**: typing.Literal['API', 'AWS_AD', 'SAML', 'USERPOOL']
- **Required**: Yes

### Arn
- **Type**: typing.Optional[str]

### UserName
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### Status
- **Type**: typing.Optional[str]

### FirstName
- **Type**: typing.Optional[str]

### LastName
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]


# VpcConfigPaginatorTypeDef

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# VpcConfigTypeDef

### SubnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


