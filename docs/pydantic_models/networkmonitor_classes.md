# Networkmonitor Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateMonitorInputTypeDef

### monitorName
- **Type**: <class 'str'>
- **Required**: Yes

### probes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.networkmonitor_classes.CreateMonitorProbeInputTypeDef]]

### aggregationPeriod
- **Type**: typing.Optional[int]

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateMonitorOutputTypeDef

### monitorArn
- **Type**: <class 'str'>
- **Required**: Yes

### monitorName
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Literal['ACTIVE', 'DELETING', 'ERROR', 'INACTIVE', 'PENDING']
- **Required**: Yes

### aggregationPeriod
- **Type**: <class 'int'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmonitor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMonitorProbeInputTypeDef

### sourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### destination
- **Type**: <class 'str'>
- **Required**: Yes

### protocol
- **Type**: typing.Literal['ICMP', 'TCP']
- **Required**: Yes

### destinationPort
- **Type**: typing.Optional[int]

### packetSize
- **Type**: typing.Optional[int]

### probeTags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateProbeInputTypeDef

### monitorName
- **Type**: <class 'str'>
- **Required**: Yes

### probe
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmonitor_classes.ProbeInputTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateProbeOutputTypeDef

### probeId
- **Type**: <class 'str'>
- **Required**: Yes

### probeArn
- **Type**: <class 'str'>
- **Required**: Yes

### sourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### destination
- **Type**: <class 'str'>
- **Required**: Yes

### destinationPort
- **Type**: <class 'int'>
- **Required**: Yes

### protocol
- **Type**: typing.Literal['ICMP', 'TCP']
- **Required**: Yes

### packetSize
- **Type**: <class 'int'>
- **Required**: Yes

### addressFamily
- **Type**: typing.Literal['IPV4', 'IPV6']
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'DELETING', 'ERROR', 'INACTIVE', 'PENDING']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### modifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmonitor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteMonitorInputTypeDef

### monitorName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProbeInputTypeDef

### monitorName
- **Type**: <class 'str'>
- **Required**: Yes

### probeId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMonitorInputTypeDef

### monitorName
- **Type**: <class 'str'>
- **Required**: Yes


# GetMonitorOutputTypeDef

### monitorArn
- **Type**: <class 'str'>
- **Required**: Yes

### monitorName
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Literal['ACTIVE', 'DELETING', 'ERROR', 'INACTIVE', 'PENDING']
- **Required**: Yes

### aggregationPeriod
- **Type**: <class 'int'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### probes
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmonitor_classes.ProbeTypeDef]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### modifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmonitor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetProbeInputTypeDef

### monitorName
- **Type**: <class 'str'>
- **Required**: Yes

### probeId
- **Type**: <class 'str'>
- **Required**: Yes


# GetProbeOutputTypeDef

### probeId
- **Type**: <class 'str'>
- **Required**: Yes

### probeArn
- **Type**: <class 'str'>
- **Required**: Yes

### sourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### destination
- **Type**: <class 'str'>
- **Required**: Yes

### destinationPort
- **Type**: <class 'int'>
- **Required**: Yes

### protocol
- **Type**: typing.Literal['ICMP', 'TCP']
- **Required**: Yes

### packetSize
- **Type**: <class 'int'>
- **Required**: Yes

### addressFamily
- **Type**: typing.Literal['IPV4', 'IPV6']
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'DELETING', 'ERROR', 'INACTIVE', 'PENDING']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### modifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmonitor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMonitorsInputPaginateTypeDef

### state
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmonitor_classes.PaginatorConfigTypeDef]


# ListMonitorsInputTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### state
- **Type**: typing.Optional[str]


# ListMonitorsOutputTypeDef

### monitors
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmonitor_classes.MonitorSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmonitor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutputTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmonitor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MonitorSummaryTypeDef

### monitorArn
- **Type**: <class 'str'>
- **Required**: Yes

### monitorName
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Literal['ACTIVE', 'DELETING', 'ERROR', 'INACTIVE', 'PENDING']
- **Required**: Yes

### aggregationPeriod
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProbeInputTypeDef

### sourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### destination
- **Type**: <class 'str'>
- **Required**: Yes

### protocol
- **Type**: typing.Literal['ICMP', 'TCP']
- **Required**: Yes

### destinationPort
- **Type**: typing.Optional[int]

### packetSize
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ProbeTypeDef

### sourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### destination
- **Type**: <class 'str'>
- **Required**: Yes

### protocol
- **Type**: typing.Literal['ICMP', 'TCP']
- **Required**: Yes

### probeId
- **Type**: typing.Optional[str]

### probeArn
- **Type**: typing.Optional[str]

### destinationPort
- **Type**: typing.Optional[int]

### packetSize
- **Type**: typing.Optional[int]

### addressFamily
- **Type**: typing.Optional[typing.Literal['IPV4', 'IPV6']]

### vpcId
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED', 'DELETING', 'ERROR', 'INACTIVE', 'PENDING']]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### modifiedAt
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


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


# TagResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateMonitorInputTypeDef

### monitorName
- **Type**: <class 'str'>
- **Required**: Yes

### aggregationPeriod
- **Type**: <class 'int'>
- **Required**: Yes


# UpdateMonitorOutputTypeDef

### monitorArn
- **Type**: <class 'str'>
- **Required**: Yes

### monitorName
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Literal['ACTIVE', 'DELETING', 'ERROR', 'INACTIVE', 'PENDING']
- **Required**: Yes

### aggregationPeriod
- **Type**: <class 'int'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmonitor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateProbeInputTypeDef

### monitorName
- **Type**: <class 'str'>
- **Required**: Yes

### probeId
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED', 'DELETING', 'ERROR', 'INACTIVE', 'PENDING']]

### destination
- **Type**: typing.Optional[str]

### destinationPort
- **Type**: typing.Optional[int]

### protocol
- **Type**: typing.Optional[typing.Literal['ICMP', 'TCP']]

### packetSize
- **Type**: typing.Optional[int]


# UpdateProbeOutputTypeDef

### probeId
- **Type**: <class 'str'>
- **Required**: Yes

### probeArn
- **Type**: <class 'str'>
- **Required**: Yes

### sourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### destination
- **Type**: <class 'str'>
- **Required**: Yes

### destinationPort
- **Type**: <class 'int'>
- **Required**: Yes

### protocol
- **Type**: typing.Literal['ICMP', 'TCP']
- **Required**: Yes

### packetSize
- **Type**: <class 'int'>
- **Required**: Yes

### addressFamily
- **Type**: typing.Literal['IPV4', 'IPV6']
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'DELETING', 'ERROR', 'INACTIVE', 'PENDING']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### modifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmonitor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


