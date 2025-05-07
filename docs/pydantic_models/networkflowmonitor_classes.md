# Networkflowmonitor Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateMonitorInput

### monitorName
- **Type**: <class 'str'>
- **Required**: Yes

### localResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.MonitorLocalResource]
- **Required**: Yes

### scopeArn
- **Type**: <class 'str'>
- **Required**: Yes

### remoteResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.MonitorRemoteResource]]

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

### monitorStatus
- **Type**: typing.Literal['ACTIVE', 'DELETING', 'ERROR', 'INACTIVE', 'PENDING']
- **Required**: Yes

### localResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.MonitorLocalResource]
- **Required**: Yes

### remoteResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.MonitorRemoteResource]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.ResponseMetadata'>
- **Required**: Yes


# CreateScopeInput

### targets
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.TargetResource]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateScopeOutput

### scopeId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### scopeArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteMonitorInput

### monitorName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteScopeInput

### scopeId
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

### monitorStatus
- **Type**: typing.Literal['ACTIVE', 'DELETING', 'ERROR', 'INACTIVE', 'PENDING']
- **Required**: Yes

### localResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.MonitorLocalResource]
- **Required**: Yes

### remoteResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.MonitorRemoteResource]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.ResponseMetadata'>
- **Required**: Yes


# GetQueryResultsMonitorTopContributorsInput

### monitorName
- **Type**: <class 'str'>
- **Required**: Yes

### queryId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetQueryResultsMonitorTopContributorsInputPaginate

### monitorName
- **Type**: <class 'str'>
- **Required**: Yes

### queryId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.PaginatorConfig]


# GetQueryResultsMonitorTopContributorsOutput

### unit
- **Type**: typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']
- **Required**: Yes

### topContributors
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.MonitorTopContributorsRow]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetQueryResultsWorkloadInsightsTopContributorsDataInput

### scopeId
- **Type**: <class 'str'>
- **Required**: Yes

### queryId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetQueryResultsWorkloadInsightsTopContributorsDataInputPaginate

### scopeId
- **Type**: <class 'str'>
- **Required**: Yes

### queryId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.PaginatorConfig]


# GetQueryResultsWorkloadInsightsTopContributorsDataOutput

### unit
- **Type**: typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']
- **Required**: Yes

### datapoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.WorkloadInsightsTopContributorsDataPoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetQueryResultsWorkloadInsightsTopContributorsInput

### scopeId
- **Type**: <class 'str'>
- **Required**: Yes

### queryId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetQueryResultsWorkloadInsightsTopContributorsInputPaginate

### scopeId
- **Type**: <class 'str'>
- **Required**: Yes

### queryId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.PaginatorConfig]


# GetQueryResultsWorkloadInsightsTopContributorsOutput

### topContributors
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.WorkloadInsightsTopContributorsRow]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetQueryStatusMonitorTopContributorsInput

### monitorName
- **Type**: <class 'str'>
- **Required**: Yes

### queryId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueryStatusMonitorTopContributorsOutput

### status
- **Type**: typing.Literal['CANCELED', 'FAILED', 'QUEUED', 'RUNNING', 'SUCCEEDED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.ResponseMetadata'>
- **Required**: Yes


# GetQueryStatusWorkloadInsightsTopContributorsDataInput

### scopeId
- **Type**: <class 'str'>
- **Required**: Yes

### queryId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueryStatusWorkloadInsightsTopContributorsDataOutput

### status
- **Type**: typing.Literal['CANCELED', 'FAILED', 'QUEUED', 'RUNNING', 'SUCCEEDED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.ResponseMetadata'>
- **Required**: Yes


# GetQueryStatusWorkloadInsightsTopContributorsInput

### scopeId
- **Type**: <class 'str'>
- **Required**: Yes

### queryId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueryStatusWorkloadInsightsTopContributorsOutput

### status
- **Type**: typing.Literal['CANCELED', 'FAILED', 'QUEUED', 'RUNNING', 'SUCCEEDED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.ResponseMetadata'>
- **Required**: Yes


# GetScopeInput

### scopeId
- **Type**: <class 'str'>
- **Required**: Yes


# GetScopeOutput

### scopeId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### scopeArn
- **Type**: <class 'str'>
- **Required**: Yes

### targets
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.TargetResource]
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.ResponseMetadata'>
- **Required**: Yes


# KubernetesMetadata

### localServiceName
- **Type**: typing.Optional[str]

### localPodName
- **Type**: typing.Optional[str]

### localPodNamespace
- **Type**: typing.Optional[str]

### remoteServiceName
- **Type**: typing.Optional[str]

### remotePodName
- **Type**: typing.Optional[str]

### remotePodNamespace
- **Type**: typing.Optional[str]


# ListMonitorsInput

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### monitorStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'ERROR', 'INACTIVE', 'PENDING']]


# ListMonitorsInputPaginate

### monitorStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'ERROR', 'INACTIVE', 'PENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.PaginatorConfig]


# ListMonitorsOutput

### monitors
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.MonitorSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListScopesInput

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListScopesInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.PaginatorConfig]


# ListScopesOutput

### scopes
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.ScopeSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.ResponseMetadata'>
- **Required**: Yes


# MonitorLocalResource

### type
- **Type**: typing.Literal['AWS::AvailabilityZone', 'AWS::EC2::Subnet', 'AWS::EC2::VPC']
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# MonitorRemoteResource

### type
- **Type**: typing.Literal['AWS::AWSService', 'AWS::AvailabilityZone', 'AWS::EC2::Subnet', 'AWS::EC2::VPC']
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# MonitorSummary

### monitorArn
- **Type**: <class 'str'>
- **Required**: Yes

### monitorName
- **Type**: <class 'str'>
- **Required**: Yes

### monitorStatus
- **Type**: typing.Literal['ACTIVE', 'DELETING', 'ERROR', 'INACTIVE', 'PENDING']
- **Required**: Yes


# MonitorTopContributorsRow

### localIp
- **Type**: typing.Optional[str]

### snatIp
- **Type**: typing.Optional[str]

### localInstanceId
- **Type**: typing.Optional[str]

### localVpcId
- **Type**: typing.Optional[str]

### localRegion
- **Type**: typing.Optional[str]

### localAz
- **Type**: typing.Optional[str]

### localSubnetId
- **Type**: typing.Optional[str]

### targetPort
- **Type**: typing.Optional[int]

### destinationCategory
- **Type**: typing.Optional[typing.Literal['AMAZON_DYNAMODB', 'AMAZON_S3', 'INTER_AZ', 'INTER_VPC', 'INTRA_AZ', 'UNCLASSIFIED']]

### remoteVpcId
- **Type**: typing.Optional[str]

### remoteRegion
- **Type**: typing.Optional[str]

### remoteAz
- **Type**: typing.Optional[str]

### remoteSubnetId
- **Type**: typing.Optional[str]

### remoteInstanceId
- **Type**: typing.Optional[str]

### remoteIp
- **Type**: typing.Optional[str]

### dnatIp
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[int]

### traversedConstructs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.TraversedComponent]]

### kubernetesMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.KubernetesMetadata]

### localInstanceArn
- **Type**: typing.Optional[str]

### localSubnetArn
- **Type**: typing.Optional[str]

### localVpcArn
- **Type**: typing.Optional[str]

### remoteInstanceArn
- **Type**: typing.Optional[str]

### remoteSubnetArn
- **Type**: typing.Optional[str]

### remoteVpcArn
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


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


# ScopeSummary

### scopeId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### scopeArn
- **Type**: <class 'str'>
- **Required**: Yes


# StartQueryMonitorTopContributorsInput

### monitorName
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### metricName
- **Type**: typing.Literal['DATA_TRANSFERRED', 'RETRANSMISSIONS', 'ROUND_TRIP_TIME', 'TIMEOUTS']
- **Required**: Yes

### destinationCategory
- **Type**: typing.Literal['AMAZON_DYNAMODB', 'AMAZON_S3', 'INTER_AZ', 'INTER_VPC', 'INTRA_AZ', 'UNCLASSIFIED']
- **Required**: Yes

### limit
- **Type**: typing.Optional[int]


# StartQueryMonitorTopContributorsOutput

### queryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.ResponseMetadata'>
- **Required**: Yes


# StartQueryWorkloadInsightsTopContributorsDataInput

### scopeId
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### metricName
- **Type**: typing.Literal['DATA_TRANSFERRED', 'RETRANSMISSIONS', 'TIMEOUTS']
- **Required**: Yes

### destinationCategory
- **Type**: typing.Literal['AMAZON_DYNAMODB', 'AMAZON_S3', 'INTER_AZ', 'INTER_VPC', 'INTRA_AZ', 'UNCLASSIFIED']
- **Required**: Yes


# StartQueryWorkloadInsightsTopContributorsDataOutput

### queryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.ResponseMetadata'>
- **Required**: Yes


# StartQueryWorkloadInsightsTopContributorsInput

### scopeId
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### metricName
- **Type**: typing.Literal['DATA_TRANSFERRED', 'RETRANSMISSIONS', 'TIMEOUTS']
- **Required**: Yes

### destinationCategory
- **Type**: typing.Literal['AMAZON_DYNAMODB', 'AMAZON_S3', 'INTER_AZ', 'INTER_VPC', 'INTRA_AZ', 'UNCLASSIFIED']
- **Required**: Yes

### limit
- **Type**: typing.Optional[int]


# StartQueryWorkloadInsightsTopContributorsOutput

### queryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.ResponseMetadata'>
- **Required**: Yes


# StopQueryMonitorTopContributorsInput

### monitorName
- **Type**: <class 'str'>
- **Required**: Yes

### queryId
- **Type**: <class 'str'>
- **Required**: Yes


# StopQueryWorkloadInsightsTopContributorsDataInput

### scopeId
- **Type**: <class 'str'>
- **Required**: Yes

### queryId
- **Type**: <class 'str'>
- **Required**: Yes


# StopQueryWorkloadInsightsTopContributorsInput

### scopeId
- **Type**: <class 'str'>
- **Required**: Yes

### queryId
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TargetId

### accountId
- **Type**: typing.Optional[str]


# TargetIdentifier

### targetId
- **Type**: <class 'aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.TargetId'>
- **Required**: Yes

### targetType
- **Type**: typing.Literal['ACCOUNT']
- **Required**: Yes


# TargetResource

### targetIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.TargetIdentifier'>
- **Required**: Yes

### region
- **Type**: <class 'str'>
- **Required**: Yes


# TraversedComponent

### componentId
- **Type**: typing.Optional[str]

### componentType
- **Type**: typing.Optional[str]

### componentArn
- **Type**: typing.Optional[str]

### serviceName
- **Type**: typing.Optional[str]


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

### localResourcesToAdd
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.MonitorLocalResource]]

### localResourcesToRemove
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.MonitorLocalResource]]

### remoteResourcesToAdd
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.MonitorRemoteResource]]

### remoteResourcesToRemove
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.MonitorRemoteResource]]

### clientToken
- **Type**: typing.Optional[str]


# UpdateMonitorOutput

### monitorArn
- **Type**: <class 'str'>
- **Required**: Yes

### monitorName
- **Type**: <class 'str'>
- **Required**: Yes

### monitorStatus
- **Type**: typing.Literal['ACTIVE', 'DELETING', 'ERROR', 'INACTIVE', 'PENDING']
- **Required**: Yes

### localResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.MonitorLocalResource]
- **Required**: Yes

### remoteResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.MonitorRemoteResource]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateScopeInput

### scopeId
- **Type**: <class 'str'>
- **Required**: Yes

### resourcesToAdd
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.TargetResource]]

### resourcesToDelete
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.TargetResource]]


# UpdateScopeOutput

### scopeId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### scopeArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_classes.ResponseMetadata'>
- **Required**: Yes


# WorkloadInsightsTopContributorsDataPoint

### timestamps
- **Type**: typing.List[datetime.datetime]
- **Required**: Yes

### values
- **Type**: typing.List[float]
- **Required**: Yes

### label
- **Type**: <class 'str'>
- **Required**: Yes


# WorkloadInsightsTopContributorsRow

### accountId
- **Type**: typing.Optional[str]

### localSubnetId
- **Type**: typing.Optional[str]

### localAz
- **Type**: typing.Optional[str]

### localVpcId
- **Type**: typing.Optional[str]

### localRegion
- **Type**: typing.Optional[str]

### remoteIdentifier
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[int]

### localSubnetArn
- **Type**: typing.Optional[str]

### localVpcArn
- **Type**: typing.Optional[str]


