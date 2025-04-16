# Appstream Classes

# AccessEndpoint

### EndpointType
- **Type**: typing.Literal['STREAMING']
- **Required**: Yes

### VpceId
- **Type**: typing.Optional[str]


# AppBlock

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.S3Location]

### SetupScriptDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.ScriptDetails]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### PostSetupScriptDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.ScriptDetails]

### PackagingType
- **Type**: typing.Optional[typing.Literal['APPSTREAM2', 'CUSTOM']]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### AppBlockErrors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.ErrorDetails]]


# AppBlockBuilder

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
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.VpcConfigOutput'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.ResourceError]]

### StateChangeReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.AppBlockBuilderStateChangeReason]

### AccessEndpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.AccessEndpoint]]


# AppBlockBuilderAppBlockAssociation

### AppBlockArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppBlockBuilderName
- **Type**: <class 'str'>
- **Required**: Yes


# AppBlockBuilderStateChangeReason

### Code
- **Type**: typing.Optional[typing.Literal['INTERNAL_ERROR']]

### Message
- **Type**: typing.Optional[str]


# Application

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.S3Location]

### Platforms
- **Type**: typing.Optional[typing.List[typing.Literal['AMAZON_LINUX2', 'RHEL8', 'ROCKY_LINUX8', 'WINDOWS', 'WINDOWS_SERVER_2016', 'WINDOWS_SERVER_2019', 'WINDOWS_SERVER_2022']]]

### InstanceFamilies
- **Type**: typing.Optional[typing.List[str]]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]


# ApplicationFleetAssociation

### FleetName
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes


# ApplicationSettings

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### SettingsGroup
- **Type**: typing.Optional[str]


# ApplicationSettingsResponse

### Enabled
- **Type**: typing.Optional[bool]

### SettingsGroup
- **Type**: typing.Optional[str]

### S3BucketName
- **Type**: typing.Optional[str]


# AssociateAppBlockBuilderAppBlockRequest

### AppBlockArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppBlockBuilderName
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateAppBlockBuilderAppBlockResult

### AppBlockBuilderAppBlockAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.AppBlockBuilderAppBlockAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateApplicationFleetRequest

### FleetName
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateApplicationFleetResult

### ApplicationFleetAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ApplicationFleetAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateApplicationToEntitlementRequest

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### EntitlementName
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateFleetRequest

### FleetName
- **Type**: <class 'str'>
- **Required**: Yes

### StackName
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchAssociateUserStackRequest

### UserStackAssociations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.appstream_classes.UserStackAssociation]
- **Required**: Yes


# BatchAssociateUserStackResult

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.UserStackAssociationError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDisassociateUserStackRequest

### UserStackAssociations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.appstream_classes.UserStackAssociation]
- **Required**: Yes


# BatchDisassociateUserStackResult

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.UserStackAssociationError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# CertificateBasedAuthProperties

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'ENABLED_NO_DIRECTORY_LOGIN_FALLBACK']]

### CertificateAuthorityArn
- **Type**: typing.Optional[str]


# ComputeCapacity

### DesiredInstances
- **Type**: typing.Optional[int]

### DesiredSessions
- **Type**: typing.Optional[int]


# ComputeCapacityStatus

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


# CopyImageRequest

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


# CopyImageResponse

### DestinationImageName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAppBlockBuilderRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.VpcConfigUnion'>
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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appstream_classes.AccessEndpoint]]


# CreateAppBlockBuilderResult

### AppBlockBuilder
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.AppBlockBuilder'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAppBlockBuilderStreamingURLRequest

### AppBlockBuilderName
- **Type**: <class 'str'>
- **Required**: Yes

### Validity
- **Type**: typing.Optional[int]


# CreateAppBlockBuilderStreamingURLResult

### StreamingURL
- **Type**: <class 'str'>
- **Required**: Yes

### Expires
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAppBlockRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SourceS3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.S3Location'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### SetupScriptDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.ScriptDetails]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### PostSetupScriptDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.ScriptDetails]

### PackagingType
- **Type**: typing.Optional[typing.Literal['APPSTREAM2', 'CUSTOM']]


# CreateAppBlockResult

### AppBlock
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.AppBlock'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# CreateApplicationRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IconS3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.S3Location'>
- **Required**: Yes

### LaunchPath
- **Type**: <class 'str'>
- **Required**: Yes

### Platforms
- **Type**: typing.Sequence[typing.Literal['AMAZON_LINUX2', 'RHEL8', 'ROCKY_LINUX8', 'WINDOWS', 'WINDOWS_SERVER_2016', 'WINDOWS_SERVER_2019', 'WINDOWS_SERVER_2022']]
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


# CreateApplicationResult

### Application
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.Application'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDirectoryConfigRequest

### DirectoryName
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationalUnitDistinguishedNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ServiceAccountCredentials
- **Type**: <class 'NoneType'>

### CertificateBasedAuthProperties
- **Type**: <class 'NoneType'>


# CreateDirectoryConfigResult

### DirectoryConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.DirectoryConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEntitlementRequest

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.appstream_classes.EntitlementAttribute]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# CreateEntitlementResult

### Entitlement
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.Entitlement'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFleetRequest

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
- **Type**: <class 'NoneType'>

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.VpcConfigUnion]

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
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### IdleDisconnectTimeoutInSeconds
- **Type**: typing.Optional[int]

### IamRoleArn
- **Type**: typing.Optional[str]

### StreamView
- **Type**: typing.Optional[typing.Literal['APP', 'DESKTOP']]

### Platform
- **Type**: typing.Optional[typing.Literal['AMAZON_LINUX2', 'RHEL8', 'ROCKY_LINUX8', 'WINDOWS', 'WINDOWS_SERVER_2016', 'WINDOWS_SERVER_2019', 'WINDOWS_SERVER_2022']]

### MaxConcurrentSessions
- **Type**: typing.Optional[int]

### UsbDeviceFilterStrings
- **Type**: typing.Optional[typing.Sequence[str]]

### SessionScriptS3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.S3Location]

### MaxSessionsPerInstance
- **Type**: typing.Optional[int]


# CreateFleetResult

### Fleet
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.Fleet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# CreateImageBuilderRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.VpcConfigUnion]

### IamRoleArn
- **Type**: typing.Optional[str]

### EnableDefaultInternetAccess
- **Type**: typing.Optional[bool]

### DomainJoinInfo
- **Type**: <class 'NoneType'>

### AppstreamAgentVersion
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### AccessEndpoints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appstream_classes.AccessEndpoint]]


# CreateImageBuilderResult

### ImageBuilder
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ImageBuilder'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# CreateImageBuilderStreamingURLRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Validity
- **Type**: typing.Optional[int]


# CreateImageBuilderStreamingURLResult

### StreamingURL
- **Type**: <class 'str'>
- **Required**: Yes

### Expires
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# CreateStackRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### StorageConnectors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appstream_classes.StorageConnectorUnion]]

### RedirectURL
- **Type**: typing.Optional[str]

### FeedbackURL
- **Type**: typing.Optional[str]

### UserSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appstream_classes.UserSetting]]

### ApplicationSettings
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### AccessEndpoints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appstream_classes.AccessEndpoint]]

### EmbedHostDomains
- **Type**: typing.Optional[typing.Sequence[str]]

### StreamingExperienceSettings
- **Type**: <class 'NoneType'>


# CreateStackResult

### Stack
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.Stack'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# CreateStreamingURLRequest

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


# CreateStreamingURLResult

### StreamingURL
- **Type**: <class 'str'>
- **Required**: Yes

### Expires
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# CreateThemeForStackRequest

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### TitleText
- **Type**: <class 'str'>
- **Required**: Yes

### ThemeStyling
- **Type**: typing.Literal['BLUE', 'LIGHT_BLUE', 'PINK', 'RED']
- **Required**: Yes

### OrganizationLogoS3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.S3Location'>
- **Required**: Yes

### FaviconS3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.S3Location'>
- **Required**: Yes

### FooterLinks
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appstream_classes.ThemeFooterLink]]


# CreateThemeForStackResult

### Theme
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.Theme'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUpdatedImageRequest

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


# CreateUpdatedImageResult

### image
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.Image'>
- **Required**: Yes

### canUpdateImage
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUsageReportSubscriptionResult

### S3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### Schedule
- **Type**: typing.Literal['DAILY']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUserRequest

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


# DeleteAppBlockBuilderRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAppBlockRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApplicationRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDirectoryConfigRequest

### DirectoryName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEntitlementRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### StackName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFleetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteImageBuilderRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteImageBuilderResult

### ImageBuilder
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ImageBuilder'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteImagePermissionsRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SharedAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteImageRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteImageResult

### Image
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.Image'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteStackRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteThemeForStackRequest

### StackName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationType
- **Type**: typing.Literal['API', 'AWS_AD', 'SAML', 'USERPOOL']
- **Required**: Yes


# DescribeAppBlockBuilderAppBlockAssociationsRequest

### AppBlockArn
- **Type**: typing.Optional[str]

### AppBlockBuilderName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeAppBlockBuilderAppBlockAssociationsResult

### AppBlockBuilderAppBlockAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.AppBlockBuilderAppBlockAssociation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeAppBlockBuildersRequest

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeAppBlockBuildersResult

### AppBlockBuilders
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.AppBlockBuilder]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeAppBlocksRequest

### Arns
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeAppBlocksResult

### AppBlocks
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.AppBlock]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeApplicationFleetAssociationsRequest

### FleetName
- **Type**: typing.Optional[str]

### ApplicationArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeApplicationFleetAssociationsResult

### ApplicationFleetAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.ApplicationFleetAssociation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeApplicationsRequest

### Arns
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeApplicationsResult

### Applications
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.Application]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeDirectoryConfigsRequest

### DirectoryNames
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeDirectoryConfigsRequestPaginate

### DirectoryNames
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.PaginatorConfig]


# DescribeDirectoryConfigsResult

### DirectoryConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.DirectoryConfig]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeEntitlementsRequest

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeEntitlementsResult

### Entitlements
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.Entitlement]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetsRequest

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetsRequestPaginate

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.PaginatorConfig]


# DescribeFleetsRequestWait

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeFleetsRequestWaitExtra

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeFleetsResult

### Fleets
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.Fleet]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeImageBuildersRequest

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeImageBuildersRequestPaginate

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.PaginatorConfig]


# DescribeImageBuildersResult

### ImageBuilders
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.ImageBuilder]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeImagePermissionsRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### SharedAwsAccountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]


# DescribeImagePermissionsResult

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SharedImagePermissionsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.SharedImagePermissions]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeImagesResult

### Images
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.Image]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeSessionsRequest

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


# DescribeSessionsRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.PaginatorConfig]


# DescribeSessionsResult

### Sessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.Session]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeStacksRequest

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]


# DescribeStacksRequestPaginate

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.PaginatorConfig]


# DescribeStacksResult

### Stacks
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.Stack]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeThemeForStackRequest

### StackName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeThemeForStackResult

### Theme
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.Theme'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeUsageReportSubscriptionsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeUsageReportSubscriptionsResult

### UsageReportSubscriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.UsageReportSubscription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeUserStackAssociationsRequest

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


# DescribeUserStackAssociationsRequestPaginate

### StackName
- **Type**: typing.Optional[str]

### UserName
- **Type**: typing.Optional[str]

### AuthenticationType
- **Type**: typing.Optional[typing.Literal['API', 'AWS_AD', 'SAML', 'USERPOOL']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.PaginatorConfig]


# DescribeUserStackAssociationsResult

### UserStackAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.UserStackAssociation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeUsersRequest

### AuthenticationType
- **Type**: typing.Literal['API', 'AWS_AD', 'SAML', 'USERPOOL']
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeUsersRequestPaginate

### AuthenticationType
- **Type**: typing.Literal['API', 'AWS_AD', 'SAML', 'USERPOOL']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.PaginatorConfig]


# DescribeUsersResult

### Users
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.User]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DirectoryConfig

### DirectoryName
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationalUnitDistinguishedNames
- **Type**: typing.Optional[typing.List[str]]

### ServiceAccountCredentials
- **Type**: <class 'NoneType'>

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### CertificateBasedAuthProperties
- **Type**: <class 'NoneType'>


# DisableUserRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationType
- **Type**: typing.Literal['API', 'AWS_AD', 'SAML', 'USERPOOL']
- **Required**: Yes


# DisassociateAppBlockBuilderAppBlockRequest

### AppBlockArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppBlockBuilderName
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateApplicationFleetRequest

### FleetName
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateApplicationFromEntitlementRequest

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### EntitlementName
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateFleetRequest

### FleetName
- **Type**: <class 'str'>
- **Required**: Yes

### StackName
- **Type**: <class 'str'>
- **Required**: Yes


# DomainJoinInfo

### DirectoryName
- **Type**: typing.Optional[str]

### OrganizationalUnitDistinguishedName
- **Type**: typing.Optional[str]


# EnableUserRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationType
- **Type**: typing.Literal['API', 'AWS_AD', 'SAML', 'USERPOOL']
- **Required**: Yes


# EntitledApplication

### ApplicationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# Entitlement

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.EntitlementAttribute]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# EntitlementAttribute

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ErrorDetails

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# ExpireSessionRequest

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes


# Fleet

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
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ComputeCapacityStatus'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.VpcConfigOutput]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### FleetErrors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.FleetError]]

### EnableDefaultInternetAccess
- **Type**: typing.Optional[bool]

### DomainJoinInfo
- **Type**: <class 'NoneType'>

### IdleDisconnectTimeoutInSeconds
- **Type**: typing.Optional[int]

### IamRoleArn
- **Type**: typing.Optional[str]

### StreamView
- **Type**: typing.Optional[typing.Literal['APP', 'DESKTOP']]

### Platform
- **Type**: typing.Optional[typing.Literal['AMAZON_LINUX2', 'RHEL8', 'ROCKY_LINUX8', 'WINDOWS', 'WINDOWS_SERVER_2016', 'WINDOWS_SERVER_2019', 'WINDOWS_SERVER_2022']]

### MaxConcurrentSessions
- **Type**: typing.Optional[int]

### UsbDeviceFilterStrings
- **Type**: typing.Optional[typing.List[str]]

### SessionScriptS3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.S3Location]

### MaxSessionsPerInstance
- **Type**: typing.Optional[int]


# FleetError

### ErrorCode
- **Type**: typing.Optional[typing.Literal['DOMAIN_JOIN_ERROR_ACCESS_DENIED', 'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED', 'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND', 'DOMAIN_JOIN_ERROR_INVALID_PARAMETER', 'DOMAIN_JOIN_ERROR_LOGON_FAILURE', 'DOMAIN_JOIN_ERROR_MORE_DATA', 'DOMAIN_JOIN_ERROR_NOT_SUPPORTED', 'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN', 'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR', 'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME', 'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED', 'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED', 'FLEET_INSTANCE_PROVISIONING_FAILURE', 'FLEET_STOPPED', 'IAM_SERVICE_ROLE_IS_MISSING', 'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION', 'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION', 'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION', 'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION', 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION', 'IGW_NOT_ATTACHED', 'IMAGE_NOT_FOUND', 'INTERNAL_SERVICE_ERROR', 'INVALID_SUBNET_CONFIGURATION', 'MACHINE_ROLE_IS_MISSING', 'NETWORK_INTERFACE_LIMIT_EXCEEDED', 'SECURITY_GROUPS_NOT_FOUND', 'STS_DISABLED_IN_REGION', 'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES', 'SUBNET_NOT_FOUND']]

### ErrorMessage
- **Type**: typing.Optional[str]


# Image

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
- **Type**: typing.Optional[typing.Literal['AMAZON_LINUX2', 'RHEL8', 'ROCKY_LINUX8', 'WINDOWS', 'WINDOWS_SERVER_2016', 'WINDOWS_SERVER_2019', 'WINDOWS_SERVER_2022']]

### Description
- **Type**: typing.Optional[str]

### StateChangeReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.ImageStateChangeReason]

### Applications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.Application]]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### PublicBaseImageReleasedDate
- **Type**: typing.Optional[datetime.datetime]

### AppstreamAgentVersion
- **Type**: typing.Optional[str]

### ImagePermissions
- **Type**: <class 'NoneType'>

### ImageErrors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.ResourceError]]

### LatestAppstreamAgentVersion
- **Type**: typing.Optional[typing.Literal['FALSE', 'TRUE']]

### SupportedInstanceFamilies
- **Type**: typing.Optional[typing.List[str]]

### DynamicAppProvidersEnabled
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### ImageSharedWithOthers
- **Type**: typing.Optional[typing.Literal['FALSE', 'TRUE']]


# ImageBuilder

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.VpcConfigOutput]

### InstanceType
- **Type**: typing.Optional[str]

### Platform
- **Type**: typing.Optional[typing.Literal['AMAZON_LINUX2', 'RHEL8', 'ROCKY_LINUX8', 'WINDOWS', 'WINDOWS_SERVER_2016', 'WINDOWS_SERVER_2019', 'WINDOWS_SERVER_2022']]

### IamRoleArn
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['DELETING', 'FAILED', 'PENDING', 'PENDING_QUALIFICATION', 'REBOOTING', 'RUNNING', 'SNAPSHOTTING', 'STOPPED', 'STOPPING', 'UPDATING', 'UPDATING_AGENT']]

### StateChangeReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.ImageBuilderStateChangeReason]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### EnableDefaultInternetAccess
- **Type**: typing.Optional[bool]

### DomainJoinInfo
- **Type**: <class 'NoneType'>

### NetworkAccessConfiguration
- **Type**: <class 'NoneType'>

### ImageBuilderErrors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.ResourceError]]

### AppstreamAgentVersion
- **Type**: typing.Optional[str]

### AccessEndpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.AccessEndpoint]]

### LatestAppstreamAgentVersion
- **Type**: typing.Optional[typing.Literal['FALSE', 'TRUE']]


# ImageBuilderStateChangeReason

### Code
- **Type**: typing.Optional[typing.Literal['IMAGE_UNAVAILABLE', 'INTERNAL_ERROR']]

### Message
- **Type**: typing.Optional[str]


# ImagePermissions

### allowFleet
- **Type**: typing.Optional[bool]

### allowImageBuilder
- **Type**: typing.Optional[bool]


# ImageStateChangeReason

### Code
- **Type**: typing.Optional[typing.Literal['IMAGE_BUILDER_NOT_AVAILABLE', 'IMAGE_COPY_FAILURE', 'INTERNAL_ERROR']]

### Message
- **Type**: typing.Optional[str]


# LastReportGenerationExecutionError

### ErrorCode
- **Type**: typing.Optional[typing.Literal['ACCESS_DENIED', 'INTERNAL_SERVICE_ERROR', 'RESOURCE_NOT_FOUND']]

### ErrorMessage
- **Type**: typing.Optional[str]


# ListAssociatedFleetsRequest

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAssociatedFleetsRequestPaginate

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.PaginatorConfig]


# ListAssociatedFleetsResult

### Names
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAssociatedStacksRequest

### FleetName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAssociatedStacksRequestPaginate

### FleetName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.PaginatorConfig]


# ListAssociatedStacksResult

### Names
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEntitledApplicationsRequest

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


# ListEntitledApplicationsResult

### EntitledApplications
- **Type**: typing.List[aws_resource_validator.pydantic_models.appstream_classes.EntitledApplication]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# NetworkAccessConfiguration

### EniPrivateIpAddress
- **Type**: typing.Optional[str]

### EniId
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ResourceError

### ErrorCode
- **Type**: typing.Optional[typing.Literal['DOMAIN_JOIN_ERROR_ACCESS_DENIED', 'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED', 'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND', 'DOMAIN_JOIN_ERROR_INVALID_PARAMETER', 'DOMAIN_JOIN_ERROR_LOGON_FAILURE', 'DOMAIN_JOIN_ERROR_MORE_DATA', 'DOMAIN_JOIN_ERROR_NOT_SUPPORTED', 'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN', 'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR', 'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME', 'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED', 'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED', 'FLEET_INSTANCE_PROVISIONING_FAILURE', 'FLEET_STOPPED', 'IAM_SERVICE_ROLE_IS_MISSING', 'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION', 'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION', 'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION', 'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION', 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION', 'IGW_NOT_ATTACHED', 'IMAGE_NOT_FOUND', 'INTERNAL_SERVICE_ERROR', 'INVALID_SUBNET_CONFIGURATION', 'MACHINE_ROLE_IS_MISSING', 'NETWORK_INTERFACE_LIMIT_EXCEEDED', 'SECURITY_GROUPS_NOT_FOUND', 'STS_DISABLED_IN_REGION', 'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES', 'SUBNET_NOT_FOUND']]

### ErrorMessage
- **Type**: typing.Optional[str]

### ErrorTimestamp
- **Type**: typing.Optional[datetime.datetime]


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


# S3Location

### S3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### S3Key
- **Type**: typing.Optional[str]


# ScriptDetails

### ScriptS3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.S3Location'>
- **Required**: Yes

### ExecutablePath
- **Type**: <class 'str'>
- **Required**: Yes

### TimeoutInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### ExecutableParameters
- **Type**: typing.Optional[str]


# ServiceAccountCredentials

### AccountName
- **Type**: <class 'str'>
- **Required**: Yes

### AccountPassword
- **Type**: <class 'str'>
- **Required**: Yes


# Session

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
- **Type**: <class 'NoneType'>

### InstanceId
- **Type**: typing.Optional[str]


# SharedImagePermissions

### sharedAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### imagePermissions
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ImagePermissions'>
- **Required**: Yes


# Stack

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.StorageConnectorOutput]]

### RedirectURL
- **Type**: typing.Optional[str]

### FeedbackURL
- **Type**: typing.Optional[str]

### StackErrors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.StackError]]

### UserSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.UserSetting]]

### ApplicationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.ApplicationSettingsResponse]

### AccessEndpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.AccessEndpoint]]

### EmbedHostDomains
- **Type**: typing.Optional[typing.List[str]]

### StreamingExperienceSettings
- **Type**: <class 'NoneType'>


# StackError

### ErrorCode
- **Type**: typing.Optional[typing.Literal['INTERNAL_SERVICE_ERROR', 'STORAGE_CONNECTOR_ERROR']]

### ErrorMessage
- **Type**: typing.Optional[str]


# StartAppBlockBuilderRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# StartAppBlockBuilderResult

### AppBlockBuilder
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.AppBlockBuilder'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# StartFleetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# StartImageBuilderRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AppstreamAgentVersion
- **Type**: typing.Optional[str]


# StartImageBuilderResult

### ImageBuilder
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ImageBuilder'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# StopAppBlockBuilderRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# StopAppBlockBuilderResult

### AppBlockBuilder
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.AppBlockBuilder'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# StopFleetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# StopImageBuilderRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# StopImageBuilderResult

### ImageBuilder
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ImageBuilder'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# StorageConnector

### ConnectorType
- **Type**: typing.Literal['GOOGLE_DRIVE', 'HOMEFOLDERS', 'ONE_DRIVE']
- **Required**: Yes

### ResourceIdentifier
- **Type**: typing.Optional[str]

### Domains
- **Type**: typing.Optional[typing.Sequence[str]]

### DomainsRequireAdminConsent
- **Type**: typing.Optional[typing.Sequence[str]]


# StorageConnectorOutput

### ConnectorType
- **Type**: typing.Literal['GOOGLE_DRIVE', 'HOMEFOLDERS', 'ONE_DRIVE']
- **Required**: Yes

### ResourceIdentifier
- **Type**: typing.Optional[str]

### Domains
- **Type**: typing.Optional[typing.List[str]]

### DomainsRequireAdminConsent
- **Type**: typing.Optional[typing.List[str]]


# StorageConnectorUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StreamingExperienceSettings

### PreferredProtocol
- **Type**: typing.Optional[typing.Literal['TCP', 'UDP']]


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# Theme

### StackName
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### ThemeTitleText
- **Type**: typing.Optional[str]

### ThemeStyling
- **Type**: typing.Optional[typing.Literal['BLUE', 'LIGHT_BLUE', 'PINK', 'RED']]

### ThemeFooterLinks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.ThemeFooterLink]]

### ThemeOrganizationLogoURL
- **Type**: typing.Optional[str]

### ThemeFaviconURL
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]


# ThemeFooterLink

### DisplayName
- **Type**: typing.Optional[str]

### FooterLinkURL
- **Type**: typing.Optional[str]


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAppBlockBuilderRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### Platform
- **Type**: typing.Optional[typing.Literal['AMAZON_LINUX2', 'RHEL8', 'ROCKY_LINUX8', 'WINDOWS', 'WINDOWS_SERVER_2016', 'WINDOWS_SERVER_2019', 'WINDOWS_SERVER_2022']]

### InstanceType
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.VpcConfigUnion]

### EnableDefaultInternetAccess
- **Type**: typing.Optional[bool]

### IamRoleArn
- **Type**: typing.Optional[str]

### AccessEndpoints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appstream_classes.AccessEndpoint]]

### AttributesToDelete
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ACCESS_ENDPOINTS', 'IAM_ROLE_ARN', 'VPC_CONFIGURATION_SECURITY_GROUP_IDS']]]


# UpdateAppBlockBuilderResult

### AppBlockBuilder
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.AppBlockBuilder'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateApplicationRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### IconS3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.S3Location]

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


# UpdateApplicationResult

### Application
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.Application'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDirectoryConfigRequest

### DirectoryName
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationalUnitDistinguishedNames
- **Type**: typing.Optional[typing.Sequence[str]]

### ServiceAccountCredentials
- **Type**: <class 'NoneType'>

### CertificateBasedAuthProperties
- **Type**: <class 'NoneType'>


# UpdateDirectoryConfigResult

### DirectoryConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.DirectoryConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEntitlementRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appstream_classes.EntitlementAttribute]]


# UpdateEntitlementResult

### Entitlement
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.Entitlement'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFleetRequest

### ImageName
- **Type**: typing.Optional[str]

### ImageArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[str]

### ComputeCapacity
- **Type**: <class 'NoneType'>

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.VpcConfigUnion]

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
- **Type**: <class 'NoneType'>

### IdleDisconnectTimeoutInSeconds
- **Type**: typing.Optional[int]

### AttributesToDelete
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DOMAIN_JOIN_INFO', 'IAM_ROLE_ARN', 'MAX_SESSIONS_PER_INSTANCE', 'SESSION_SCRIPT_S3_LOCATION', 'USB_DEVICE_FILTER_STRINGS', 'VPC_CONFIGURATION', 'VPC_CONFIGURATION_SECURITY_GROUP_IDS']]]

### IamRoleArn
- **Type**: typing.Optional[str]

### StreamView
- **Type**: typing.Optional[typing.Literal['APP', 'DESKTOP']]

### Platform
- **Type**: typing.Optional[typing.Literal['AMAZON_LINUX2', 'RHEL8', 'ROCKY_LINUX8', 'WINDOWS', 'WINDOWS_SERVER_2016', 'WINDOWS_SERVER_2019', 'WINDOWS_SERVER_2022']]

### MaxConcurrentSessions
- **Type**: typing.Optional[int]

### UsbDeviceFilterStrings
- **Type**: typing.Optional[typing.Sequence[str]]

### SessionScriptS3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.S3Location]

### MaxSessionsPerInstance
- **Type**: typing.Optional[int]


# UpdateFleetResult

### Fleet
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.Fleet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateImagePermissionsRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SharedAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ImagePermissions
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ImagePermissions'>
- **Required**: Yes


# UpdateStackRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### StorageConnectors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appstream_classes.StorageConnectorUnion]]

### DeleteStorageConnectors
- **Type**: typing.Optional[bool]

### RedirectURL
- **Type**: typing.Optional[str]

### FeedbackURL
- **Type**: typing.Optional[str]

### AttributesToDelete
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ACCESS_ENDPOINTS', 'EMBED_HOST_DOMAINS', 'FEEDBACK_URL', 'IAM_ROLE_ARN', 'REDIRECT_URL', 'STORAGE_CONNECTORS', 'STORAGE_CONNECTOR_GOOGLE_DRIVE', 'STORAGE_CONNECTOR_HOMEFOLDERS', 'STORAGE_CONNECTOR_ONE_DRIVE', 'STREAMING_EXPERIENCE_SETTINGS', 'THEME_NAME', 'USER_SETTINGS']]]

### UserSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appstream_classes.UserSetting]]

### ApplicationSettings
- **Type**: <class 'NoneType'>

### AccessEndpoints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appstream_classes.AccessEndpoint]]

### EmbedHostDomains
- **Type**: typing.Optional[typing.Sequence[str]]

### StreamingExperienceSettings
- **Type**: <class 'NoneType'>


# UpdateStackResult

### Stack
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.Stack'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateThemeForStackRequest

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### FooterLinks
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appstream_classes.ThemeFooterLink]]

### TitleText
- **Type**: typing.Optional[str]

### ThemeStyling
- **Type**: typing.Optional[typing.Literal['BLUE', 'LIGHT_BLUE', 'PINK', 'RED']]

### OrganizationLogoS3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.S3Location]

### FaviconS3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appstream_classes.S3Location]

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### AttributesToDelete
- **Type**: typing.Optional[typing.Sequence[typing.Literal['FOOTER_LINKS']]]


# UpdateThemeForStackResult

### Theme
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.Theme'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appstream_classes.ResponseMetadata'>
- **Required**: Yes


# UsageReportSubscription

### S3BucketName
- **Type**: typing.Optional[str]

### Schedule
- **Type**: typing.Optional[typing.Literal['DAILY']]

### LastGeneratedReportDate
- **Type**: typing.Optional[datetime.datetime]

### SubscriptionErrors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appstream_classes.LastReportGenerationExecutionError]]


# User

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


# UserSetting

### Action
- **Type**: typing.Literal['AUTO_TIME_ZONE_REDIRECTION', 'CLIPBOARD_COPY_FROM_LOCAL_DEVICE', 'CLIPBOARD_COPY_TO_LOCAL_DEVICE', 'DOMAIN_PASSWORD_SIGNIN', 'DOMAIN_SMART_CARD_SIGNIN', 'FILE_DOWNLOAD', 'FILE_UPLOAD', 'PRINTING_TO_LOCAL_DEVICE']
- **Required**: Yes

### Permission
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### MaximumLength
- **Type**: typing.Optional[int]


# UserStackAssociation

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


# UserStackAssociationError

### UserStackAssociation
- **Type**: <class 'NoneType'>

### ErrorCode
- **Type**: typing.Optional[typing.Literal['DIRECTORY_NOT_FOUND', 'INTERNAL_ERROR', 'STACK_NOT_FOUND', 'USER_NAME_NOT_FOUND']]

### ErrorMessage
- **Type**: typing.Optional[str]


# VpcConfig

### SubnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]


# VpcConfigOutput

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# VpcConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


