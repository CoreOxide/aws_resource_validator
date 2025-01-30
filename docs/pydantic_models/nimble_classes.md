# nimble_classes

# AcceptEulasRequestRequestTypeDef

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### eulaIds
- **Type**: typing.Optional[typing.Sequence[str]]


# AcceptEulasResponseTypeDef

### eulaAcceptances
- **Type**: typing.List[aws_resource_validator.pydantic_models.nimble_classes.EulaAcceptanceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ActiveDirectoryComputerAttributeTypeDef

### name
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# ActiveDirectoryConfigurationPaginatorTypeDef

### computerAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.nimble_classes.ActiveDirectoryComputerAttributeTypeDef]]

### directoryId
- **Type**: typing.Optional[str]

### organizationalUnitDistinguishedName
- **Type**: typing.Optional[str]


# ActiveDirectoryConfigurationTypeDef

### computerAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.nimble_classes.ActiveDirectoryComputerAttributeTypeDef]]

### directoryId
- **Type**: typing.Optional[str]

### organizationalUnitDistinguishedName
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComputeFarmConfigurationTypeDef

### activeDirectoryUser
- **Type**: typing.Optional[str]

### endpoint
- **Type**: typing.Optional[str]


# CreateLaunchProfileRequestRequestTypeDef

### ec2SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### launchProfileProtocolVersions
- **Type**: typing.Sequence[str]
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### streamConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.StreamConfigurationCreateTypeDef'>
- **Required**: Yes

### studioComponentIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateLaunchProfileResponseTypeDef

### launchProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.LaunchProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStreamingImageRequestRequestTypeDef

### ec2ImageId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateStreamingImageResponseTypeDef

### streamingImage
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.StreamingImageTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStreamingSessionRequestRequestTypeDef

### launchProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### ec2InstanceType
- **Type**: typing.Optional[typing.Literal['g3.4xlarge', 'g3s.xlarge', 'g4dn.12xlarge', 'g4dn.16xlarge', 'g4dn.2xlarge', 'g4dn.4xlarge', 'g4dn.8xlarge', 'g4dn.xlarge', 'g5.16xlarge', 'g5.2xlarge', 'g5.4xlarge', 'g5.8xlarge', 'g5.xlarge']]

### ownedBy
- **Type**: typing.Optional[str]

### streamingImageId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateStreamingSessionResponseTypeDef

### session
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.StreamingSessionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStreamingSessionStreamRequestRequestTypeDef

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### expirationInSeconds
- **Type**: typing.Optional[int]


# CreateStreamingSessionStreamResponseTypeDef

### stream
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.StreamingSessionStreamTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStudioComponentRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['ACTIVE_DIRECTORY', 'COMPUTE_FARM', 'CUSTOM', 'LICENSE_SERVICE', 'SHARED_FILE_SYSTEM']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.StudioComponentConfigurationTypeDef]

### description
- **Type**: typing.Optional[str]

### ec2SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### initializationScripts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.nimble_classes.StudioComponentInitializationScriptTypeDef]]

### runtimeRoleArn
- **Type**: typing.Optional[str]

### scriptParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.nimble_classes.ScriptParameterKeyValueTypeDef]]

### secureInitializationRoleArn
- **Type**: typing.Optional[str]

### subtype
- **Type**: typing.Optional[typing.Literal['AMAZON_FSX_FOR_LUSTRE', 'AMAZON_FSX_FOR_WINDOWS', 'AWS_MANAGED_MICROSOFT_AD', 'CUSTOM']]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateStudioComponentResponseTypeDef

### studioComponent
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.StudioComponentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStudioRequestRequestTypeDef

### adminRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### studioName
- **Type**: <class 'str'>
- **Required**: Yes

### userRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### studioEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.StudioEncryptionConfigurationTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateStudioResponseTypeDef

### studio
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.StudioTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteLaunchProfileMemberRequestRequestTypeDef

### launchProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteLaunchProfileRequestRequestTypeDef

### launchProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteLaunchProfileResponseTypeDef

### launchProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.LaunchProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteStreamingImageRequestRequestTypeDef

### streamingImageId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteStreamingImageResponseTypeDef

### streamingImage
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.StreamingImageTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteStreamingSessionRequestRequestTypeDef

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteStreamingSessionResponseTypeDef

### session
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.StreamingSessionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteStudioComponentRequestRequestTypeDef

### studioComponentId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteStudioComponentResponseTypeDef

### studioComponent
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.StudioComponentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteStudioMemberRequestRequestTypeDef

### principalId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteStudioRequestRequestTypeDef

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteStudioResponseTypeDef

### studio
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.StudioTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EulaAcceptanceTypeDef

### acceptedAt
- **Type**: typing.Optional[datetime.datetime]

### acceptedBy
- **Type**: typing.Optional[str]

### accepteeId
- **Type**: typing.Optional[str]

### eulaAcceptanceId
- **Type**: typing.Optional[str]

### eulaId
- **Type**: typing.Optional[str]


# EulaTypeDef

### content
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### eulaId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# GetEulaRequestRequestTypeDef

### eulaId
- **Type**: <class 'str'>
- **Required**: Yes


# GetEulaResponseTypeDef

### eula
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.EulaTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLaunchProfileDetailsRequestRequestTypeDef

### launchProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes


# GetLaunchProfileDetailsResponseTypeDef

### launchProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.LaunchProfileTypeDef'>
- **Required**: Yes

### streamingImages
- **Type**: typing.List[aws_resource_validator.pydantic_models.nimble_classes.StreamingImageTypeDef]
- **Required**: Yes

### studioComponentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.nimble_classes.StudioComponentSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLaunchProfileInitializationRequestRequestTypeDef

### launchProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### launchProfileProtocolVersions
- **Type**: typing.Sequence[str]
- **Required**: Yes

### launchPurpose
- **Type**: <class 'str'>
- **Required**: Yes

### platform
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes


# GetLaunchProfileInitializationResponseTypeDef

### launchProfileInitialization
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.LaunchProfileInitializationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLaunchProfileMemberRequestRequestTypeDef

### launchProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes


# GetLaunchProfileMemberResponseTypeDef

### member
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.LaunchProfileMembershipTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLaunchProfileRequestLaunchProfileDeletedWaitTypeDef

### launchProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.WaiterConfigTypeDef]


# GetLaunchProfileRequestLaunchProfileReadyWaitTypeDef

### launchProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.WaiterConfigTypeDef]


# GetLaunchProfileRequestRequestTypeDef

### launchProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes


# GetLaunchProfileResponseTypeDef

### launchProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.LaunchProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetStreamingImageRequestRequestTypeDef

### streamingImageId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes


# GetStreamingImageRequestStreamingImageDeletedWaitTypeDef

### streamingImageId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.WaiterConfigTypeDef]


# GetStreamingImageRequestStreamingImageReadyWaitTypeDef

### streamingImageId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.WaiterConfigTypeDef]


# GetStreamingImageResponseTypeDef

### streamingImage
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.StreamingImageTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetStreamingSessionBackupRequestRequestTypeDef

### backupId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes


# GetStreamingSessionBackupResponseTypeDef

### streamingSessionBackup
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.StreamingSessionBackupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetStreamingSessionRequestRequestTypeDef

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes


# GetStreamingSessionRequestStreamingSessionDeletedWaitTypeDef

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.WaiterConfigTypeDef]


# GetStreamingSessionRequestStreamingSessionReadyWaitTypeDef

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.WaiterConfigTypeDef]


# GetStreamingSessionRequestStreamingSessionStoppedWaitTypeDef

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.WaiterConfigTypeDef]


# GetStreamingSessionResponseTypeDef

### session
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.StreamingSessionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetStreamingSessionStreamRequestRequestTypeDef

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### streamId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes


# GetStreamingSessionStreamRequestStreamingSessionStreamReadyWaitTypeDef

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### streamId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.WaiterConfigTypeDef]


# GetStreamingSessionStreamResponseTypeDef

### stream
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.StreamingSessionStreamTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetStudioComponentRequestRequestTypeDef

### studioComponentId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes


# GetStudioComponentRequestStudioComponentDeletedWaitTypeDef

### studioComponentId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.WaiterConfigTypeDef]


# GetStudioComponentRequestStudioComponentReadyWaitTypeDef

### studioComponentId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.WaiterConfigTypeDef]


# GetStudioComponentResponseTypeDef

### studioComponent
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.StudioComponentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetStudioMemberRequestRequestTypeDef

### principalId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes


# GetStudioMemberResponseTypeDef

### member
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.StudioMembershipTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetStudioRequestRequestTypeDef

### studioId
- **Type**: <class 'str'>
- **Required**: Yes


# GetStudioRequestStudioDeletedWaitTypeDef

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.WaiterConfigTypeDef]


# GetStudioRequestStudioReadyWaitTypeDef

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.WaiterConfigTypeDef]


# GetStudioResponseTypeDef

### studio
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.StudioTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LaunchProfileInitializationActiveDirectoryTypeDef

### computerAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.nimble_classes.ActiveDirectoryComputerAttributeTypeDef]]

### directoryId
- **Type**: typing.Optional[str]

### directoryName
- **Type**: typing.Optional[str]

### dnsIpAddresses
- **Type**: typing.Optional[typing.List[str]]

### organizationalUnitDistinguishedName
- **Type**: typing.Optional[str]

### studioComponentId
- **Type**: typing.Optional[str]

### studioComponentName
- **Type**: typing.Optional[str]


# LaunchProfileInitializationScriptTypeDef

### runtimeRoleArn
- **Type**: typing.Optional[str]

### script
- **Type**: typing.Optional[str]

### secureInitializationRoleArn
- **Type**: typing.Optional[str]

### studioComponentId
- **Type**: typing.Optional[str]

### studioComponentName
- **Type**: typing.Optional[str]


# LaunchProfileInitializationTypeDef

### activeDirectory
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.LaunchProfileInitializationActiveDirectoryTypeDef]

### ec2SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### launchProfileId
- **Type**: typing.Optional[str]

### launchProfileProtocolVersion
- **Type**: typing.Optional[str]

### launchPurpose
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### platform
- **Type**: typing.Optional[typing.Literal['LINUX', 'WINDOWS']]

### systemInitializationScripts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.nimble_classes.LaunchProfileInitializationScriptTypeDef]]

### userInitializationScripts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.nimble_classes.LaunchProfileInitializationScriptTypeDef]]


# LaunchProfileMembershipTypeDef

### identityStoreId
- **Type**: typing.Optional[str]

### persona
- **Type**: typing.Optional[typing.Literal['USER']]

### principalId
- **Type**: typing.Optional[str]

### sid
- **Type**: typing.Optional[str]


# LaunchProfilePaginatorTypeDef

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### ec2SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### launchProfileId
- **Type**: typing.Optional[str]

### launchProfileProtocolVersions
- **Type**: typing.Optional[typing.List[str]]

### name
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'READY', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']]

### statusCode
- **Type**: typing.Optional[typing.Literal['ENCRYPTION_KEY_ACCESS_DENIED', 'ENCRYPTION_KEY_NOT_FOUND', 'INTERNAL_ERROR', 'INVALID_INSTANCE_TYPES_PROVIDED', 'INVALID_SUBNETS_COMBINATION', 'INVALID_SUBNETS_PROVIDED', 'LAUNCH_PROFILE_CREATED', 'LAUNCH_PROFILE_CREATE_IN_PROGRESS', 'LAUNCH_PROFILE_DELETED', 'LAUNCH_PROFILE_DELETE_IN_PROGRESS', 'LAUNCH_PROFILE_UPDATED', 'LAUNCH_PROFILE_UPDATE_IN_PROGRESS', 'LAUNCH_PROFILE_WITH_STREAM_SESSIONS_NOT_DELETED', 'STREAMING_IMAGE_NOT_FOUND', 'STREAMING_IMAGE_NOT_READY']]

### statusMessage
- **Type**: typing.Optional[str]

### streamConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.StreamConfigurationPaginatorTypeDef]

### studioComponentIds
- **Type**: typing.Optional[typing.List[str]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]

### validationResults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.nimble_classes.ValidationResultTypeDef]]


# LaunchProfileTypeDef

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### ec2SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### launchProfileId
- **Type**: typing.Optional[str]

### launchProfileProtocolVersions
- **Type**: typing.Optional[typing.List[str]]

### name
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'READY', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']]

### statusCode
- **Type**: typing.Optional[typing.Literal['ENCRYPTION_KEY_ACCESS_DENIED', 'ENCRYPTION_KEY_NOT_FOUND', 'INTERNAL_ERROR', 'INVALID_INSTANCE_TYPES_PROVIDED', 'INVALID_SUBNETS_COMBINATION', 'INVALID_SUBNETS_PROVIDED', 'LAUNCH_PROFILE_CREATED', 'LAUNCH_PROFILE_CREATE_IN_PROGRESS', 'LAUNCH_PROFILE_DELETED', 'LAUNCH_PROFILE_DELETE_IN_PROGRESS', 'LAUNCH_PROFILE_UPDATED', 'LAUNCH_PROFILE_UPDATE_IN_PROGRESS', 'LAUNCH_PROFILE_WITH_STREAM_SESSIONS_NOT_DELETED', 'STREAMING_IMAGE_NOT_FOUND', 'STREAMING_IMAGE_NOT_READY']]

### statusMessage
- **Type**: typing.Optional[str]

### streamConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.StreamConfigurationTypeDef]

### studioComponentIds
- **Type**: typing.Optional[typing.List[str]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]

### validationResults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.nimble_classes.ValidationResultTypeDef]]


# LicenseServiceConfigurationTypeDef

### endpoint
- **Type**: typing.Optional[str]


# ListEulaAcceptancesRequestListEulaAcceptancesPaginateTypeDef

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### eulaIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.PaginatorConfigTypeDef]


# ListEulaAcceptancesRequestRequestTypeDef

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### eulaIds
- **Type**: typing.Optional[typing.Sequence[str]]

### nextToken
- **Type**: typing.Optional[str]


# ListEulaAcceptancesResponseTypeDef

### eulaAcceptances
- **Type**: typing.List[aws_resource_validator.pydantic_models.nimble_classes.EulaAcceptanceTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEulasRequestListEulasPaginateTypeDef

### eulaIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.PaginatorConfigTypeDef]


# ListEulasRequestRequestTypeDef

### eulaIds
- **Type**: typing.Optional[typing.Sequence[str]]

### nextToken
- **Type**: typing.Optional[str]


# ListEulasResponseTypeDef

### eulas
- **Type**: typing.List[aws_resource_validator.pydantic_models.nimble_classes.EulaTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLaunchProfileMembersRequestListLaunchProfileMembersPaginateTypeDef

### launchProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.PaginatorConfigTypeDef]


# ListLaunchProfileMembersRequestRequestTypeDef

### launchProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListLaunchProfileMembersResponseTypeDef

### members
- **Type**: typing.List[aws_resource_validator.pydantic_models.nimble_classes.LaunchProfileMembershipTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLaunchProfilesRequestListLaunchProfilesPaginateTypeDef

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### principalId
- **Type**: typing.Optional[str]

### states
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'READY', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.PaginatorConfigTypeDef]


# ListLaunchProfilesRequestRequestTypeDef

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### principalId
- **Type**: typing.Optional[str]

### states
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'READY', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']]]


# ListLaunchProfilesResponsePaginatorTypeDef

### launchProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.nimble_classes.LaunchProfilePaginatorTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLaunchProfilesResponseTypeDef

### launchProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.nimble_classes.LaunchProfileTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListStreamingImagesRequestListStreamingImagesPaginateTypeDef

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### owner
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.PaginatorConfigTypeDef]


# ListStreamingImagesRequestRequestTypeDef

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### owner
- **Type**: typing.Optional[str]


# ListStreamingImagesResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### streamingImages
- **Type**: typing.List[aws_resource_validator.pydantic_models.nimble_classes.StreamingImageTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListStreamingSessionBackupsRequestListStreamingSessionBackupsPaginateTypeDef

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### ownedBy
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.PaginatorConfigTypeDef]


# ListStreamingSessionBackupsRequestRequestTypeDef

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### ownedBy
- **Type**: typing.Optional[str]


# ListStreamingSessionBackupsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### streamingSessionBackups
- **Type**: typing.List[aws_resource_validator.pydantic_models.nimble_classes.StreamingSessionBackupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListStreamingSessionsRequestListStreamingSessionsPaginateTypeDef

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### createdBy
- **Type**: typing.Optional[str]

### ownedBy
- **Type**: typing.Optional[str]

### sessionIds
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.PaginatorConfigTypeDef]


# ListStreamingSessionsRequestRequestTypeDef

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### createdBy
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### ownedBy
- **Type**: typing.Optional[str]

### sessionIds
- **Type**: typing.Optional[str]


# ListStreamingSessionsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### sessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.nimble_classes.StreamingSessionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListStudioComponentsRequestListStudioComponentsPaginateTypeDef

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### states
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'READY', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']]]

### types
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ACTIVE_DIRECTORY', 'COMPUTE_FARM', 'CUSTOM', 'LICENSE_SERVICE', 'SHARED_FILE_SYSTEM']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.PaginatorConfigTypeDef]


# ListStudioComponentsRequestRequestTypeDef

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### states
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'READY', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']]]

### types
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ACTIVE_DIRECTORY', 'COMPUTE_FARM', 'CUSTOM', 'LICENSE_SERVICE', 'SHARED_FILE_SYSTEM']]]


# ListStudioComponentsResponsePaginatorTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### studioComponents
- **Type**: typing.List[aws_resource_validator.pydantic_models.nimble_classes.StudioComponentPaginatorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListStudioComponentsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### studioComponents
- **Type**: typing.List[aws_resource_validator.pydantic_models.nimble_classes.StudioComponentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListStudioMembersRequestListStudioMembersPaginateTypeDef

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.PaginatorConfigTypeDef]


# ListStudioMembersRequestRequestTypeDef

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListStudioMembersResponseTypeDef

### members
- **Type**: typing.List[aws_resource_validator.pydantic_models.nimble_classes.StudioMembershipTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListStudiosRequestListStudiosPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.PaginatorConfigTypeDef]


# ListStudiosRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]


# ListStudiosResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### studios
- **Type**: typing.List[aws_resource_validator.pydantic_models.nimble_classes.StudioTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# NewLaunchProfileMemberTypeDef

### persona
- **Type**: typing.Literal['USER']
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes


# NewStudioMemberTypeDef

### persona
- **Type**: typing.Literal['ADMINISTRATOR']
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutLaunchProfileMembersRequestRequestTypeDef

### identityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### launchProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### members
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.nimble_classes.NewLaunchProfileMemberTypeDef]
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# PutStudioMembersRequestRequestTypeDef

### identityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### members
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.nimble_classes.NewStudioMemberTypeDef]
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


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


# ScriptParameterKeyValueTypeDef

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# SharedFileSystemConfigurationTypeDef

### endpoint
- **Type**: typing.Optional[str]

### fileSystemId
- **Type**: typing.Optional[str]

### linuxMountPoint
- **Type**: typing.Optional[str]

### shareName
- **Type**: typing.Optional[str]

### windowsMountDrive
- **Type**: typing.Optional[str]


# StartStreamingSessionRequestRequestTypeDef

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### backupId
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


# StartStreamingSessionResponseTypeDef

### session
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.StreamingSessionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartStudioSSOConfigurationRepairRequestRequestTypeDef

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# StartStudioSSOConfigurationRepairResponseTypeDef

### studio
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.StudioTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopStreamingSessionRequestRequestTypeDef

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### volumeRetentionMode
- **Type**: typing.Optional[typing.Literal['DELETE', 'RETAIN']]


# StopStreamingSessionResponseTypeDef

### session
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.StreamingSessionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StreamConfigurationCreateTypeDef

### clipboardMode
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ec2InstanceTypes
- **Type**: typing.Sequence[typing.Literal['g3.4xlarge', 'g3s.xlarge', 'g4dn.12xlarge', 'g4dn.16xlarge', 'g4dn.2xlarge', 'g4dn.4xlarge', 'g4dn.8xlarge', 'g4dn.xlarge', 'g5.16xlarge', 'g5.2xlarge', 'g5.4xlarge', 'g5.8xlarge', 'g5.xlarge']]
- **Required**: Yes

### streamingImageIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### automaticTerminationMode
- **Type**: typing.Optional[typing.Literal['ACTIVATED', 'DEACTIVATED']]

### maxSessionLengthInMinutes
- **Type**: typing.Optional[int]

### maxStoppedSessionLengthInMinutes
- **Type**: typing.Optional[int]

### sessionBackup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.StreamConfigurationSessionBackupTypeDef]

### sessionPersistenceMode
- **Type**: typing.Optional[typing.Literal['ACTIVATED', 'DEACTIVATED']]

### sessionStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.StreamConfigurationSessionStorageTypeDef]

### volumeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.VolumeConfigurationTypeDef]


# StreamConfigurationPaginatorTypeDef

### clipboardMode
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ec2InstanceTypes
- **Type**: typing.List[typing.Literal['g3.4xlarge', 'g3s.xlarge', 'g4dn.12xlarge', 'g4dn.16xlarge', 'g4dn.2xlarge', 'g4dn.4xlarge', 'g4dn.8xlarge', 'g4dn.xlarge', 'g5.16xlarge', 'g5.2xlarge', 'g5.4xlarge', 'g5.8xlarge', 'g5.xlarge']]
- **Required**: Yes

### streamingImageIds
- **Type**: typing.List[str]
- **Required**: Yes

### automaticTerminationMode
- **Type**: typing.Optional[typing.Literal['ACTIVATED', 'DEACTIVATED']]

### maxSessionLengthInMinutes
- **Type**: typing.Optional[int]

### maxStoppedSessionLengthInMinutes
- **Type**: typing.Optional[int]

### sessionBackup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.StreamConfigurationSessionBackupTypeDef]

### sessionPersistenceMode
- **Type**: typing.Optional[typing.Literal['ACTIVATED', 'DEACTIVATED']]

### sessionStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.StreamConfigurationSessionStoragePaginatorTypeDef]

### volumeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.VolumeConfigurationTypeDef]


# StreamConfigurationSessionBackupTypeDef

### maxBackupsToRetain
- **Type**: typing.Optional[int]

### mode
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'DEACTIVATED']]


# StreamConfigurationSessionStoragePaginatorTypeDef

### mode
- **Type**: typing.List[typing.Literal['UPLOAD']]
- **Required**: Yes

### root
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.StreamingSessionStorageRootTypeDef]


# StreamConfigurationSessionStorageTypeDef

### mode
- **Type**: typing.Sequence[typing.Literal['UPLOAD']]
- **Required**: Yes

### root
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.StreamingSessionStorageRootTypeDef]


# StreamConfigurationTypeDef

### clipboardMode
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ec2InstanceTypes
- **Type**: typing.List[typing.Literal['g3.4xlarge', 'g3s.xlarge', 'g4dn.12xlarge', 'g4dn.16xlarge', 'g4dn.2xlarge', 'g4dn.4xlarge', 'g4dn.8xlarge', 'g4dn.xlarge', 'g5.16xlarge', 'g5.2xlarge', 'g5.4xlarge', 'g5.8xlarge', 'g5.xlarge']]
- **Required**: Yes

### streamingImageIds
- **Type**: typing.List[str]
- **Required**: Yes

### automaticTerminationMode
- **Type**: typing.Optional[typing.Literal['ACTIVATED', 'DEACTIVATED']]

### maxSessionLengthInMinutes
- **Type**: typing.Optional[int]

### maxStoppedSessionLengthInMinutes
- **Type**: typing.Optional[int]

### sessionBackup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.StreamConfigurationSessionBackupTypeDef]

### sessionPersistenceMode
- **Type**: typing.Optional[typing.Literal['ACTIVATED', 'DEACTIVATED']]

### sessionStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.StreamConfigurationSessionStorageTypeDef]

### volumeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.VolumeConfigurationTypeDef]


# StreamingImageEncryptionConfigurationTypeDef

### keyType
- **Type**: typing.Literal['CUSTOMER_MANAGED_KEY']
- **Required**: Yes

### keyArn
- **Type**: typing.Optional[str]


# StreamingImageTypeDef

### arn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### ec2ImageId
- **Type**: typing.Optional[str]

### encryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.StreamingImageEncryptionConfigurationTypeDef]

### eulaIds
- **Type**: typing.Optional[typing.List[str]]

### name
- **Type**: typing.Optional[str]

### owner
- **Type**: typing.Optional[str]

### platform
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'READY', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']]

### statusCode
- **Type**: typing.Optional[typing.Literal['ACCESS_DENIED', 'INTERNAL_ERROR', 'STREAMING_IMAGE_CREATE_IN_PROGRESS', 'STREAMING_IMAGE_DELETED', 'STREAMING_IMAGE_DELETE_IN_PROGRESS', 'STREAMING_IMAGE_READY', 'STREAMING_IMAGE_UPDATE_IN_PROGRESS']]

### statusMessage
- **Type**: typing.Optional[str]

### streamingImageId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# StreamingSessionBackupTypeDef

### arn
- **Type**: typing.Optional[str]

### backupId
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### launchProfileId
- **Type**: typing.Optional[str]

### ownedBy
- **Type**: typing.Optional[str]

### sessionId
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'READY', 'START_FAILED', 'START_IN_PROGRESS', 'STOPPED', 'STOP_FAILED', 'STOP_IN_PROGRESS']]

### statusCode
- **Type**: typing.Optional[typing.Literal['ACTIVE_DIRECTORY_DOMAIN_JOIN_ERROR', 'AMI_VALIDATION_ERROR', 'DECRYPT_STREAMING_IMAGE_ERROR', 'INITIALIZATION_SCRIPT_ERROR', 'INSUFFICIENT_CAPACITY', 'INTERNAL_ERROR', 'NETWORK_CONNECTION_ERROR', 'NETWORK_INTERFACE_ERROR', 'STREAMING_SESSION_CREATE_IN_PROGRESS', 'STREAMING_SESSION_DELETED', 'STREAMING_SESSION_DELETE_IN_PROGRESS', 'STREAMING_SESSION_READY', 'STREAMING_SESSION_STARTED', 'STREAMING_SESSION_START_IN_PROGRESS', 'STREAMING_SESSION_STOPPED', 'STREAMING_SESSION_STOP_IN_PROGRESS']]

### statusMessage
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# StreamingSessionStorageRootTypeDef

### linux
- **Type**: typing.Optional[str]

### windows
- **Type**: typing.Optional[str]


# StreamingSessionStreamTypeDef

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### expiresAt
- **Type**: typing.Optional[datetime.datetime]

### ownedBy
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'READY']]

### statusCode
- **Type**: typing.Optional[typing.Literal['INTERNAL_ERROR', 'NETWORK_CONNECTION_ERROR', 'STREAM_CREATE_IN_PROGRESS', 'STREAM_DELETED', 'STREAM_DELETE_IN_PROGRESS', 'STREAM_READY']]

### streamId
- **Type**: typing.Optional[str]

### url
- **Type**: typing.Optional[str]


# StreamingSessionTypeDef

### arn
- **Type**: typing.Optional[str]

### automaticTerminationMode
- **Type**: typing.Optional[typing.Literal['ACTIVATED', 'DEACTIVATED']]

### backupMode
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'DEACTIVATED']]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### ec2InstanceType
- **Type**: typing.Optional[str]

### launchProfileId
- **Type**: typing.Optional[str]

### maxBackupsToRetain
- **Type**: typing.Optional[int]

### ownedBy
- **Type**: typing.Optional[str]

### sessionId
- **Type**: typing.Optional[str]

### sessionPersistenceMode
- **Type**: typing.Optional[typing.Literal['ACTIVATED', 'DEACTIVATED']]

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### startedBy
- **Type**: typing.Optional[str]

### startedFromBackupId
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'READY', 'START_FAILED', 'START_IN_PROGRESS', 'STOPPED', 'STOP_FAILED', 'STOP_IN_PROGRESS']]

### statusCode
- **Type**: typing.Optional[typing.Literal['ACTIVE_DIRECTORY_DOMAIN_JOIN_ERROR', 'AMI_VALIDATION_ERROR', 'DECRYPT_STREAMING_IMAGE_ERROR', 'INITIALIZATION_SCRIPT_ERROR', 'INSUFFICIENT_CAPACITY', 'INTERNAL_ERROR', 'NETWORK_CONNECTION_ERROR', 'NETWORK_INTERFACE_ERROR', 'STREAMING_SESSION_CREATE_IN_PROGRESS', 'STREAMING_SESSION_DELETED', 'STREAMING_SESSION_DELETE_IN_PROGRESS', 'STREAMING_SESSION_READY', 'STREAMING_SESSION_STARTED', 'STREAMING_SESSION_START_IN_PROGRESS', 'STREAMING_SESSION_STOPPED', 'STREAMING_SESSION_STOP_IN_PROGRESS']]

### statusMessage
- **Type**: typing.Optional[str]

### stopAt
- **Type**: typing.Optional[datetime.datetime]

### stoppedAt
- **Type**: typing.Optional[datetime.datetime]

### stoppedBy
- **Type**: typing.Optional[str]

### streamingImageId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### terminateAt
- **Type**: typing.Optional[datetime.datetime]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]

### volumeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.VolumeConfigurationTypeDef]

### volumeRetentionMode
- **Type**: typing.Optional[typing.Literal['DELETE', 'RETAIN']]


# StudioComponentConfigurationPaginatorTypeDef

### activeDirectoryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.ActiveDirectoryConfigurationPaginatorTypeDef]

### computeFarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.ComputeFarmConfigurationTypeDef]

### licenseServiceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.LicenseServiceConfigurationTypeDef]

### sharedFileSystemConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.SharedFileSystemConfigurationTypeDef]


# StudioComponentConfigurationTypeDef

### activeDirectoryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.ActiveDirectoryConfigurationTypeDef]

### computeFarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.ComputeFarmConfigurationTypeDef]

### licenseServiceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.LicenseServiceConfigurationTypeDef]

### sharedFileSystemConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.SharedFileSystemConfigurationTypeDef]


# StudioComponentInitializationScriptTypeDef

### launchProfileProtocolVersion
- **Type**: typing.Optional[str]

### platform
- **Type**: typing.Optional[typing.Literal['LINUX', 'WINDOWS']]

### runContext
- **Type**: typing.Optional[typing.Literal['SYSTEM_INITIALIZATION', 'USER_INITIALIZATION']]

### script
- **Type**: typing.Optional[str]


# StudioComponentPaginatorTypeDef

### arn
- **Type**: typing.Optional[str]

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.StudioComponentConfigurationPaginatorTypeDef]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### ec2SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### initializationScripts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.nimble_classes.StudioComponentInitializationScriptTypeDef]]

### name
- **Type**: typing.Optional[str]

### runtimeRoleArn
- **Type**: typing.Optional[str]

### scriptParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.nimble_classes.ScriptParameterKeyValueTypeDef]]

### secureInitializationRoleArn
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'READY', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']]

### statusCode
- **Type**: typing.Optional[typing.Literal['ACTIVE_DIRECTORY_ALREADY_EXISTS', 'ENCRYPTION_KEY_ACCESS_DENIED', 'ENCRYPTION_KEY_NOT_FOUND', 'INTERNAL_ERROR', 'STUDIO_COMPONENT_CREATED', 'STUDIO_COMPONENT_CREATE_IN_PROGRESS', 'STUDIO_COMPONENT_DELETED', 'STUDIO_COMPONENT_DELETE_IN_PROGRESS', 'STUDIO_COMPONENT_UPDATED', 'STUDIO_COMPONENT_UPDATE_IN_PROGRESS']]

### statusMessage
- **Type**: typing.Optional[str]

### studioComponentId
- **Type**: typing.Optional[str]

### subtype
- **Type**: typing.Optional[typing.Literal['AMAZON_FSX_FOR_LUSTRE', 'AMAZON_FSX_FOR_WINDOWS', 'AWS_MANAGED_MICROSOFT_AD', 'CUSTOM']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### type
- **Type**: typing.Optional[typing.Literal['ACTIVE_DIRECTORY', 'COMPUTE_FARM', 'CUSTOM', 'LICENSE_SERVICE', 'SHARED_FILE_SYSTEM']]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]


# StudioComponentSummaryTypeDef

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### studioComponentId
- **Type**: typing.Optional[str]

### subtype
- **Type**: typing.Optional[typing.Literal['AMAZON_FSX_FOR_LUSTRE', 'AMAZON_FSX_FOR_WINDOWS', 'AWS_MANAGED_MICROSOFT_AD', 'CUSTOM']]

### type
- **Type**: typing.Optional[typing.Literal['ACTIVE_DIRECTORY', 'COMPUTE_FARM', 'CUSTOM', 'LICENSE_SERVICE', 'SHARED_FILE_SYSTEM']]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]


# StudioComponentTypeDef

### arn
- **Type**: typing.Optional[str]

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.StudioComponentConfigurationTypeDef]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### ec2SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### initializationScripts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.nimble_classes.StudioComponentInitializationScriptTypeDef]]

### name
- **Type**: typing.Optional[str]

### runtimeRoleArn
- **Type**: typing.Optional[str]

### scriptParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.nimble_classes.ScriptParameterKeyValueTypeDef]]

### secureInitializationRoleArn
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'READY', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']]

### statusCode
- **Type**: typing.Optional[typing.Literal['ACTIVE_DIRECTORY_ALREADY_EXISTS', 'ENCRYPTION_KEY_ACCESS_DENIED', 'ENCRYPTION_KEY_NOT_FOUND', 'INTERNAL_ERROR', 'STUDIO_COMPONENT_CREATED', 'STUDIO_COMPONENT_CREATE_IN_PROGRESS', 'STUDIO_COMPONENT_DELETED', 'STUDIO_COMPONENT_DELETE_IN_PROGRESS', 'STUDIO_COMPONENT_UPDATED', 'STUDIO_COMPONENT_UPDATE_IN_PROGRESS']]

### statusMessage
- **Type**: typing.Optional[str]

### studioComponentId
- **Type**: typing.Optional[str]

### subtype
- **Type**: typing.Optional[typing.Literal['AMAZON_FSX_FOR_LUSTRE', 'AMAZON_FSX_FOR_WINDOWS', 'AWS_MANAGED_MICROSOFT_AD', 'CUSTOM']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### type
- **Type**: typing.Optional[typing.Literal['ACTIVE_DIRECTORY', 'COMPUTE_FARM', 'CUSTOM', 'LICENSE_SERVICE', 'SHARED_FILE_SYSTEM']]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]


# StudioEncryptionConfigurationTypeDef

### keyType
- **Type**: typing.Literal['AWS_OWNED_KEY', 'CUSTOMER_MANAGED_KEY']
- **Required**: Yes

### keyArn
- **Type**: typing.Optional[str]


# StudioMembershipTypeDef

### identityStoreId
- **Type**: typing.Optional[str]

### persona
- **Type**: typing.Optional[typing.Literal['ADMINISTRATOR']]

### principalId
- **Type**: typing.Optional[str]

### sid
- **Type**: typing.Optional[str]


# StudioTypeDef

### adminRoleArn
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### displayName
- **Type**: typing.Optional[str]

### homeRegion
- **Type**: typing.Optional[str]

### ssoClientId
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'READY', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']]

### statusCode
- **Type**: typing.Optional[typing.Literal['AWS_SSO_ACCESS_DENIED', 'AWS_SSO_CONFIGURATION_REPAIRED', 'AWS_SSO_CONFIGURATION_REPAIR_IN_PROGRESS', 'AWS_SSO_NOT_ENABLED', 'AWS_STS_REGION_DISABLED', 'ENCRYPTION_KEY_ACCESS_DENIED', 'ENCRYPTION_KEY_NOT_FOUND', 'INTERNAL_ERROR', 'ROLE_COULD_NOT_BE_ASSUMED', 'ROLE_NOT_OWNED_BY_STUDIO_OWNER', 'STUDIO_CREATED', 'STUDIO_CREATE_IN_PROGRESS', 'STUDIO_DELETED', 'STUDIO_DELETE_IN_PROGRESS', 'STUDIO_UPDATED', 'STUDIO_UPDATE_IN_PROGRESS', 'STUDIO_WITH_LAUNCH_PROFILES_NOT_DELETED', 'STUDIO_WITH_STREAMING_IMAGES_NOT_DELETED', 'STUDIO_WITH_STUDIO_COMPONENTS_NOT_DELETED']]

### statusMessage
- **Type**: typing.Optional[str]

### studioEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.StudioEncryptionConfigurationTypeDef]

### studioId
- **Type**: typing.Optional[str]

### studioName
- **Type**: typing.Optional[str]

### studioUrl
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### userRoleArn
- **Type**: typing.Optional[str]


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateLaunchProfileMemberRequestRequestTypeDef

### launchProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### persona
- **Type**: typing.Literal['USER']
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# UpdateLaunchProfileMemberResponseTypeDef

### member
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.LaunchProfileMembershipTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateLaunchProfileRequestRequestTypeDef

### launchProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### launchProfileProtocolVersions
- **Type**: typing.Optional[typing.Sequence[str]]

### name
- **Type**: typing.Optional[str]

### streamConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.StreamConfigurationCreateTypeDef]

### studioComponentIds
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateLaunchProfileResponseTypeDef

### launchProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.LaunchProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateStreamingImageRequestRequestTypeDef

### streamingImageId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# UpdateStreamingImageResponseTypeDef

### streamingImage
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.StreamingImageTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateStudioComponentRequestRequestTypeDef

### studioComponentId
- **Type**: <class 'str'>
- **Required**: Yes

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.nimble_classes.StudioComponentConfigurationTypeDef]

### description
- **Type**: typing.Optional[str]

### ec2SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### initializationScripts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.nimble_classes.StudioComponentInitializationScriptTypeDef]]

### name
- **Type**: typing.Optional[str]

### runtimeRoleArn
- **Type**: typing.Optional[str]

### scriptParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.nimble_classes.ScriptParameterKeyValueTypeDef]]

### secureInitializationRoleArn
- **Type**: typing.Optional[str]

### subtype
- **Type**: typing.Optional[typing.Literal['AMAZON_FSX_FOR_LUSTRE', 'AMAZON_FSX_FOR_WINDOWS', 'AWS_MANAGED_MICROSOFT_AD', 'CUSTOM']]

### type
- **Type**: typing.Optional[typing.Literal['ACTIVE_DIRECTORY', 'COMPUTE_FARM', 'CUSTOM', 'LICENSE_SERVICE', 'SHARED_FILE_SYSTEM']]


# UpdateStudioComponentResponseTypeDef

### studioComponent
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.StudioComponentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateStudioRequestRequestTypeDef

### studioId
- **Type**: <class 'str'>
- **Required**: Yes

### adminRoleArn
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### userRoleArn
- **Type**: typing.Optional[str]


# UpdateStudioResponseTypeDef

### studio
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.StudioTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.nimble_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ValidationResultTypeDef

### state
- **Type**: typing.Literal['VALIDATION_FAILED', 'VALIDATION_FAILED_INTERNAL_SERVER_ERROR', 'VALIDATION_IN_PROGRESS', 'VALIDATION_NOT_STARTED', 'VALIDATION_SUCCESS']
- **Required**: Yes

### statusCode
- **Type**: typing.Literal['VALIDATION_FAILED_INTERNAL_SERVER_ERROR', 'VALIDATION_FAILED_INVALID_ACTIVE_DIRECTORY', 'VALIDATION_FAILED_INVALID_SECURITY_GROUP_ASSOCIATION', 'VALIDATION_FAILED_INVALID_SUBNET_ROUTE_TABLE_ASSOCIATION', 'VALIDATION_FAILED_SUBNET_NOT_FOUND', 'VALIDATION_FAILED_UNAUTHORIZED', 'VALIDATION_IN_PROGRESS', 'VALIDATION_NOT_STARTED', 'VALIDATION_SUCCESS']
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['VALIDATE_ACTIVE_DIRECTORY_STUDIO_COMPONENT', 'VALIDATE_NETWORK_ACL_ASSOCIATION', 'VALIDATE_SECURITY_GROUP_ASSOCIATION', 'VALIDATE_SUBNET_ASSOCIATION']
- **Required**: Yes


# VolumeConfigurationTypeDef

### iops
- **Type**: typing.Optional[int]

### size
- **Type**: typing.Optional[int]

### throughput
- **Type**: typing.Optional[int]


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


