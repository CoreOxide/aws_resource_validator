# Networkmonitor Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateMonitorInput

### monitorName
- **Type**: <class 'str'>
- **Required**: Yes

### probes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmonitor.networkmonitor_classes.CreateMonitorProbeInput]]

### aggregationPeriod
- **Type**: typing.Optional[int]

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateMonitorOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmonitor.networkmonitor_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMonitorProbeInput

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
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateProbeInput

### monitorName
- **Type**: <class 'str'>
- **Required**: Yes

### probe
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmonitor.networkmonitor_classes.ProbeInput'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateProbeOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmonitor.networkmonitor_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteMonitorInput

### monitorName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProbeInput

### monitorName
- **Type**: <class 'str'>
- **Required**: Yes

### probeId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMonitorInput

### monitorName
- **Type**: <class 'str'>
- **Required**: Yes


# GetMonitorOutput

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmonitor.networkmonitor_classes.Probe]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### modifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmonitor.networkmonitor_classes.ResponseMetadata'>
- **Required**: Yes


# GetProbeInput

### monitorName
- **Type**: <class 'str'>
- **Required**: Yes

### probeId
- **Type**: <class 'str'>
- **Required**: Yes


# GetProbeOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmonitor.networkmonitor_classes.ResponseMetadata'>
- **Required**: Yes


# ListMonitorsInput

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### state
- **Type**: typing.Optional[str]


# ListMonitorsInputPaginate

### state
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmonitor.networkmonitor_classes.PaginatorConfig]


# ListMonitorsOutput

### monitors
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmonitor.networkmonitor_classes.MonitorSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmonitor.networkmonitor_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutput

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmonitor.networkmonitor_classes.ResponseMetadata'>
- **Required**: Yes


# MonitorSummary

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


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Probe

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


# ProbeInput

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
- **Type**: typing.Optional[typing.Dict[str, str]]


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


# TagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateMonitorInput

### monitorName
- **Type**: <class 'str'>
- **Required**: Yes

### aggregationPeriod
- **Type**: <class 'int'>
- **Required**: Yes


# UpdateMonitorOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmonitor.networkmonitor_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateProbeInput

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


# UpdateProbeOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmonitor.networkmonitor_classes.ResponseMetadata'>
- **Required**: Yes


