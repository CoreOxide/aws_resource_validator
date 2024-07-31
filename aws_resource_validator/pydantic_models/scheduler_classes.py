from datetime import datetime
from pydantic import BaseModel
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.scheduler_constants import *

class AwsVpcConfigurationTypeDef(BaseModel):
    Subnets: Sequence[str]
    AssignPublicIp: Optional[AssignPublicIpType] = None
    SecurityGroups: Optional[Sequence[str]] = None

class CapacityProviderStrategyItemTypeDef(BaseModel):
    capacityProvider: str
    base: Optional[int] = None
    weight: Optional[int] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class FlexibleTimeWindowTypeDef(BaseModel):
    Mode: FlexibleTimeWindowModeType
    MaximumWindowInMinutes: Optional[int] = None

class DeadLetterConfigTypeDef(BaseModel):
    Arn: Optional[str] = None

class DeleteScheduleGroupInputRequestTypeDef(BaseModel):
    Name: str
    ClientToken: Optional[str] = None

class DeleteScheduleInputRequestTypeDef(BaseModel):
    Name: str
    ClientToken: Optional[str] = None
    GroupName: Optional[str] = None

class PlacementConstraintTypeDef(BaseModel):
    expression: Optional[str] = None
    type: Optional[PlacementConstraintTypeType] = None

class PlacementStrategyTypeDef(BaseModel):
    field: Optional[str] = None
    type: Optional[PlacementStrategyTypeType] = None

class EventBridgeParametersTypeDef(BaseModel):
    DetailType: str
    Source: str

class GetScheduleGroupInputRequestTypeDef(BaseModel):
    Name: str

class GetScheduleInputRequestTypeDef(BaseModel):
    Name: str
    GroupName: Optional[str] = None

class KinesisParametersTypeDef(BaseModel):
    PartitionKey: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListScheduleGroupsInputRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NamePrefix: Optional[str] = None
    NextToken: Optional[str] = None

class ScheduleGroupSummaryTypeDef(BaseModel):
    Arn: Optional[str] = None
    CreationDate: Optional[datetime] = None
    LastModificationDate: Optional[datetime] = None
    Name: Optional[str] = None
    State: Optional[ScheduleGroupStateType] = None

class ListSchedulesInputRequestTypeDef(BaseModel):
    GroupName: Optional[str] = None
    MaxResults: Optional[int] = None
    NamePrefix: Optional[str] = None
    NextToken: Optional[str] = None
    State: Optional[ScheduleStateType] = None

class ListTagsForResourceInputRequestTypeDef(BaseModel):
    ResourceArn: str

class RetryPolicyTypeDef(BaseModel):
    MaximumEventAgeInSeconds: Optional[int] = None
    MaximumRetryAttempts: Optional[int] = None

class SageMakerPipelineParameterTypeDef(BaseModel):
    Name: str
    Value: str

class TargetSummaryTypeDef(BaseModel):
    Arn: str

class SqsParametersTypeDef(BaseModel):
    MessageGroupId: Optional[str] = None

class UntagResourceInputRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class NetworkConfigurationTypeDef(BaseModel):
    awsvpcConfiguration: Optional[AwsVpcConfigurationTypeDef] = None

class CreateScheduleGroupInputRequestTypeDef(BaseModel):
    Name: str
    ClientToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceInputRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateScheduleGroupOutputTypeDef(BaseModel):
    ScheduleGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateScheduleOutputTypeDef(BaseModel):
    ScheduleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetScheduleGroupOutputTypeDef(BaseModel):
    Arn: str
    CreationDate: datetime
    LastModificationDate: datetime
    Name: str
    State: ScheduleGroupStateType
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateScheduleOutputTypeDef(BaseModel):
    ScheduleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListScheduleGroupsInputListScheduleGroupsPaginateTypeDef(BaseModel):
    NamePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSchedulesInputListSchedulesPaginateTypeDef(BaseModel):
    GroupName: Optional[str] = None
    NamePrefix: Optional[str] = None
    State: Optional[ScheduleStateType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListScheduleGroupsOutputTypeDef(BaseModel):
    NextToken: str
    ScheduleGroups: List[ScheduleGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SageMakerPipelineParametersTypeDef(BaseModel):
    PipelineParameterList: Optional[Sequence[SageMakerPipelineParameterTypeDef]] = None

class ScheduleSummaryTypeDef(BaseModel):
    Arn: Optional[str] = None
    CreationDate: Optional[datetime] = None
    GroupName: Optional[str] = None
    LastModificationDate: Optional[datetime] = None
    Name: Optional[str] = None
    State: Optional[ScheduleStateType] = None
    Target: Optional[TargetSummaryTypeDef] = None

class EcsParametersTypeDef(BaseModel):
    TaskDefinitionArn: str
    CapacityProviderStrategy: Optional[Sequence[CapacityProviderStrategyItemTypeDef]] = None
    EnableECSManagedTags: Optional[bool] = None
    EnableExecuteCommand: Optional[bool] = None
    Group: Optional[str] = None
    LaunchType: Optional[LaunchTypeType] = None
    NetworkConfiguration: Optional[NetworkConfigurationTypeDef] = None
    PlacementConstraints: Optional[Sequence[PlacementConstraintTypeDef]] = None
    PlacementStrategy: Optional[Sequence[PlacementStrategyTypeDef]] = None
    PlatformVersion: Optional[str] = None
    PropagateTags: Optional[Literal["TASK_DEFINITION"]] = None
    ReferenceId: Optional[str] = None
    Tags: Optional[Sequence[Mapping[str, str]]] = None
    TaskCount: Optional[int] = None

class ListSchedulesOutputTypeDef(BaseModel):
    NextToken: str
    Schedules: List[ScheduleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TargetTypeDef(BaseModel):
    Arn: str
    RoleArn: str
    DeadLetterConfig: Optional[DeadLetterConfigTypeDef] = None
    EcsParameters: Optional[EcsParametersTypeDef] = None
    EventBridgeParameters: Optional[EventBridgeParametersTypeDef] = None
    Input: Optional[str] = None
    KinesisParameters: Optional[KinesisParametersTypeDef] = None
    RetryPolicy: Optional[RetryPolicyTypeDef] = None
    SageMakerPipelineParameters: Optional[SageMakerPipelineParametersTypeDef] = None
    SqsParameters: Optional[SqsParametersTypeDef] = None

class CreateScheduleInputRequestTypeDef(BaseModel):
    FlexibleTimeWindow: FlexibleTimeWindowTypeDef
    Name: str
    ScheduleExpression: str
    Target: TargetTypeDef
    ActionAfterCompletion: Optional[ActionAfterCompletionType] = None
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    EndDate: Optional[TimestampTypeDef] = None
    GroupName: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    ScheduleExpressionTimezone: Optional[str] = None
    StartDate: Optional[TimestampTypeDef] = None
    State: Optional[ScheduleStateType] = None

class GetScheduleOutputTypeDef(BaseModel):
    ActionAfterCompletion: ActionAfterCompletionType
    Arn: str
    CreationDate: datetime
    Description: str
    EndDate: datetime
    FlexibleTimeWindow: FlexibleTimeWindowTypeDef
    GroupName: str
    KmsKeyArn: str
    LastModificationDate: datetime
    Name: str
    ScheduleExpression: str
    ScheduleExpressionTimezone: str
    StartDate: datetime
    State: ScheduleStateType
    Target: TargetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateScheduleInputRequestTypeDef(BaseModel):
    FlexibleTimeWindow: FlexibleTimeWindowTypeDef
    Name: str
    ScheduleExpression: str
    Target: TargetTypeDef
    ActionAfterCompletion: Optional[ActionAfterCompletionType] = None
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    EndDate: Optional[TimestampTypeDef] = None
    GroupName: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    ScheduleExpressionTimezone: Optional[str] = None
    StartDate: Optional[TimestampTypeDef] = None
    State: Optional[ScheduleStateType] = None

