# Gameliftstreams Classes

# AddStreamGroupLocationsInput

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### LocationConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.LocationConfiguration]
- **Required**: Yes


# AddStreamGroupLocationsOutput

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### Locations
- **Type**: typing.List[aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.LocationState]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.ResponseMetadata'>
- **Required**: Yes


# ApplicationSummary

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### LastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### RuntimeEnvironment
- **Type**: <class 'NoneType'>

### Status
- **Type**: typing.Optional[typing.Literal['DELETING', 'ERROR', 'INITIALIZED', 'PROCESSING', 'READY']]


# AssociateApplicationsInput

### ApplicationIdentifiers
- **Type**: typing.List[str]
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateApplicationsOutput

### ApplicationArns
- **Type**: typing.List[str]
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.ResponseMetadata'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateApplicationInput

### ApplicationSourceUri
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutablePath
- **Type**: <class 'str'>
- **Required**: Yes

### RuntimeEnvironment
- **Type**: <class 'aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.RuntimeEnvironment'>
- **Required**: Yes

### ApplicationLogOutputUri
- **Type**: typing.Optional[str]

### ApplicationLogPaths
- **Type**: typing.Optional[typing.List[str]]

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateApplicationOutput

### ApplicationLogOutputUri
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationLogPaths
- **Type**: typing.List[str]
- **Required**: Yes

### ApplicationSourceUri
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AssociatedStreamGroups
- **Type**: typing.List[str]
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutablePath
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ReplicationStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.ReplicationStatus]
- **Required**: Yes

### RuntimeEnvironment
- **Type**: <class 'aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.RuntimeEnvironment'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['DELETING', 'ERROR', 'INITIALIZED', 'PROCESSING', 'READY']
- **Required**: Yes

### StatusReason
- **Type**: typing.Literal['accessDenied', 'internalError']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.ResponseMetadata'>
- **Required**: Yes


# CreateStreamGroupInput

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### StreamClass
- **Type**: typing.Literal['gen4n_high', 'gen4n_ultra', 'gen4n_win2022', 'gen5n_high', 'gen5n_ultra', 'gen5n_win2022']
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### DefaultApplicationIdentifier
- **Type**: typing.Optional[str]

### LocationConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.LocationConfiguration]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateStreamGroupOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AssociatedApplications
- **Type**: typing.List[str]
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DefaultApplication
- **Type**: <class 'aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.DefaultApplication'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LocationStates
- **Type**: typing.List[aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.LocationState]
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVATING', 'ACTIVE', 'ACTIVE_WITH_ERRORS', 'DELETING', 'ERROR', 'UPDATING_LOCATIONS']
- **Required**: Yes

### StatusReason
- **Type**: typing.Literal['internalError', 'noAvailableInstances']
- **Required**: Yes

### StreamClass
- **Type**: typing.Literal['gen4n_high', 'gen4n_ultra', 'gen4n_win2022', 'gen5n_high', 'gen5n_ultra', 'gen5n_win2022']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.ResponseMetadata'>
- **Required**: Yes


# CreateStreamSessionConnectionInput

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### SignalRequest
- **Type**: <class 'str'>
- **Required**: Yes

### StreamSessionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# CreateStreamSessionConnectionOutput

### SignalResponse
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.ResponseMetadata'>
- **Required**: Yes


# DefaultApplication

### Arn
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]


# DeleteApplicationInput

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStreamGroupInput

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateApplicationsInput

### ApplicationIdentifiers
- **Type**: typing.List[str]
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateApplicationsOutput

### ApplicationArns
- **Type**: typing.List[str]
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.ResponseMetadata'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.ResponseMetadata'>
- **Required**: Yes


# ExportFilesMetadata

### OutputUri
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'SUCCEEDED']]

### StatusReason
- **Type**: typing.Optional[str]


# ExportStreamSessionFilesInput

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### OutputUri
- **Type**: <class 'str'>
- **Required**: Yes

### StreamSessionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetApplicationInput

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetApplicationInputWait

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetApplicationInputWaitExtra

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetApplicationOutput

### ApplicationLogOutputUri
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationLogPaths
- **Type**: typing.List[str]
- **Required**: Yes

### ApplicationSourceUri
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AssociatedStreamGroups
- **Type**: typing.List[str]
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutablePath
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ReplicationStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.ReplicationStatus]
- **Required**: Yes

### RuntimeEnvironment
- **Type**: <class 'aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.RuntimeEnvironment'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['DELETING', 'ERROR', 'INITIALIZED', 'PROCESSING', 'READY']
- **Required**: Yes

### StatusReason
- **Type**: typing.Literal['accessDenied', 'internalError']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.ResponseMetadata'>
- **Required**: Yes


# GetStreamGroupInput

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetStreamGroupInputWait

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetStreamGroupInputWaitExtra

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetStreamGroupOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AssociatedApplications
- **Type**: typing.List[str]
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DefaultApplication
- **Type**: <class 'aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.DefaultApplication'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LocationStates
- **Type**: typing.List[aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.LocationState]
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVATING', 'ACTIVE', 'ACTIVE_WITH_ERRORS', 'DELETING', 'ERROR', 'UPDATING_LOCATIONS']
- **Required**: Yes

### StatusReason
- **Type**: typing.Literal['internalError', 'noAvailableInstances']
- **Required**: Yes

### StreamClass
- **Type**: typing.Literal['gen4n_high', 'gen4n_ultra', 'gen4n_win2022', 'gen5n_high', 'gen5n_ultra', 'gen5n_win2022']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.ResponseMetadata'>
- **Required**: Yes


# GetStreamSessionInput

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### StreamSessionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetStreamSessionInputWait

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### StreamSessionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetStreamSessionOutput

### AdditionalEnvironmentVariables
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### AdditionalLaunchArgs
- **Type**: typing.List[str]
- **Required**: Yes

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionTimeoutSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ExportFilesMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.ExportFilesMetadata'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### LogFileLocationUri
- **Type**: <class 'str'>
- **Required**: Yes

### Protocol
- **Type**: typing.Literal['WebRTC']
- **Required**: Yes

### SessionLengthSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### SignalRequest
- **Type**: <class 'str'>
- **Required**: Yes

### SignalResponse
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVATING', 'ACTIVE', 'CONNECTED', 'ERROR', 'PENDING_CLIENT_RECONNECTION', 'RECONNECTING', 'TERMINATED', 'TERMINATING']
- **Required**: Yes

### StatusReason
- **Type**: typing.Literal['applicationLogS3DestinationError', 'internalError', 'invalidSignalRequest', 'placementTimeout']
- **Required**: Yes

### StreamGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### WebSdkProtocolUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.ResponseMetadata'>
- **Required**: Yes


# ListApplicationsInput

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationsInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.PaginatorConfig]


# ListApplicationsOutput

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.ApplicationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStreamGroupsInput

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListStreamGroupsInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.PaginatorConfig]


# ListStreamGroupsOutput

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.StreamGroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStreamSessionsByAccountInput

### ExportFilesStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'SUCCEEDED']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVATING', 'ACTIVE', 'CONNECTED', 'ERROR', 'PENDING_CLIENT_RECONNECTION', 'RECONNECTING', 'TERMINATED', 'TERMINATING']]


# ListStreamSessionsByAccountInputPaginate

### ExportFilesStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'SUCCEEDED']]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVATING', 'ACTIVE', 'CONNECTED', 'ERROR', 'PENDING_CLIENT_RECONNECTION', 'RECONNECTING', 'TERMINATED', 'TERMINATING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.PaginatorConfig]


# ListStreamSessionsByAccountOutput

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.StreamSessionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStreamSessionsInput

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### ExportFilesStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'SUCCEEDED']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVATING', 'ACTIVE', 'CONNECTED', 'ERROR', 'PENDING_CLIENT_RECONNECTION', 'RECONNECTING', 'TERMINATED', 'TERMINATING']]


# ListStreamSessionsInputPaginate

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### ExportFilesStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'SUCCEEDED']]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVATING', 'ACTIVE', 'CONNECTED', 'ERROR', 'PENDING_CLIENT_RECONNECTION', 'RECONNECTING', 'TERMINATED', 'TERMINATING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.PaginatorConfig]


# ListStreamSessionsOutput

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.StreamSessionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.ResponseMetadata'>
- **Required**: Yes


# LocationConfiguration

### LocationName
- **Type**: <class 'str'>
- **Required**: Yes

### AlwaysOnCapacity
- **Type**: typing.Optional[int]

### OnDemandCapacity
- **Type**: typing.Optional[int]


# LocationState

### AllocatedCapacity
- **Type**: typing.Optional[int]

### AlwaysOnCapacity
- **Type**: typing.Optional[int]

### IdleCapacity
- **Type**: typing.Optional[int]

### LocationName
- **Type**: typing.Optional[str]

### OnDemandCapacity
- **Type**: typing.Optional[int]

### RequestedCapacity
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVATING', 'ACTIVE', 'ERROR', 'REMOVING']]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RemoveStreamGroupLocationsInput

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### Locations
- **Type**: typing.List[str]
- **Required**: Yes


# ReplicationStatus

### Location
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'REPLICATING']]


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


# RuntimeEnvironment

### Type
- **Type**: typing.Literal['PROTON', 'UBUNTU', 'WINDOWS']
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes


# StartStreamSessionInput

### ApplicationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### Protocol
- **Type**: typing.Literal['WebRTC']
- **Required**: Yes

### SignalRequest
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalEnvironmentVariables
- **Type**: typing.Optional[typing.Dict[str, str]]

### AdditionalLaunchArgs
- **Type**: typing.Optional[typing.List[str]]

### ClientToken
- **Type**: typing.Optional[str]

### ConnectionTimeoutSeconds
- **Type**: typing.Optional[int]

### Description
- **Type**: typing.Optional[str]

### Locations
- **Type**: typing.Optional[typing.List[str]]

### SessionLengthSeconds
- **Type**: typing.Optional[int]

### UserId
- **Type**: typing.Optional[str]


# StartStreamSessionOutput

### AdditionalEnvironmentVariables
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### AdditionalLaunchArgs
- **Type**: typing.List[str]
- **Required**: Yes

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionTimeoutSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ExportFilesMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.ExportFilesMetadata'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### LogFileLocationUri
- **Type**: <class 'str'>
- **Required**: Yes

### Protocol
- **Type**: typing.Literal['WebRTC']
- **Required**: Yes

### SessionLengthSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### SignalRequest
- **Type**: <class 'str'>
- **Required**: Yes

### SignalResponse
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVATING', 'ACTIVE', 'CONNECTED', 'ERROR', 'PENDING_CLIENT_RECONNECTION', 'RECONNECTING', 'TERMINATED', 'TERMINATING']
- **Required**: Yes

### StatusReason
- **Type**: typing.Literal['applicationLogS3DestinationError', 'internalError', 'invalidSignalRequest', 'placementTimeout']
- **Required**: Yes

### StreamGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### WebSdkProtocolUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.ResponseMetadata'>
- **Required**: Yes


# StreamGroupSummary

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### DefaultApplication
- **Type**: <class 'NoneType'>

### Description
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### LastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVATING', 'ACTIVE', 'ACTIVE_WITH_ERRORS', 'DELETING', 'ERROR', 'UPDATING_LOCATIONS']]

### StreamClass
- **Type**: typing.Optional[typing.Literal['gen4n_high', 'gen4n_ultra', 'gen4n_win2022', 'gen5n_high', 'gen5n_ultra', 'gen5n_win2022']]


# StreamSessionSummary

### ApplicationArn
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### ExportFilesMetadata
- **Type**: <class 'NoneType'>

### LastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### Location
- **Type**: typing.Optional[str]

### Protocol
- **Type**: typing.Optional[typing.Literal['WebRTC']]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVATING', 'ACTIVE', 'CONNECTED', 'ERROR', 'PENDING_CLIENT_RECONNECTION', 'RECONNECTING', 'TERMINATED', 'TERMINATING']]

### UserId
- **Type**: typing.Optional[str]


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TerminateStreamSessionInput

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### StreamSessionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateApplicationInput

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationLogOutputUri
- **Type**: typing.Optional[str]

### ApplicationLogPaths
- **Type**: typing.Optional[typing.List[str]]

### Description
- **Type**: typing.Optional[str]


# UpdateApplicationOutput

### ApplicationLogOutputUri
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationLogPaths
- **Type**: typing.List[str]
- **Required**: Yes

### ApplicationSourceUri
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AssociatedStreamGroups
- **Type**: typing.List[str]
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutablePath
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ReplicationStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.ReplicationStatus]
- **Required**: Yes

### RuntimeEnvironment
- **Type**: <class 'aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.RuntimeEnvironment'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['DELETING', 'ERROR', 'INITIALIZED', 'PROCESSING', 'READY']
- **Required**: Yes

### StatusReason
- **Type**: typing.Literal['accessDenied', 'internalError']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateStreamGroupInput

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### LocationConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.LocationConfiguration]]


# UpdateStreamGroupOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AssociatedApplications
- **Type**: typing.List[str]
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DefaultApplication
- **Type**: <class 'aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.DefaultApplication'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LocationStates
- **Type**: typing.List[aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.LocationState]
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVATING', 'ACTIVE', 'ACTIVE_WITH_ERRORS', 'DELETING', 'ERROR', 'UPDATING_LOCATIONS']
- **Required**: Yes

### StatusReason
- **Type**: typing.Literal['internalError', 'noAvailableInstances']
- **Required**: Yes

### StreamClass
- **Type**: typing.Literal['gen4n_high', 'gen4n_ultra', 'gen4n_win2022', 'gen5n_high', 'gen5n_ultra', 'gen5n_win2022']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_classes.ResponseMetadata'>
- **Required**: Yes


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


