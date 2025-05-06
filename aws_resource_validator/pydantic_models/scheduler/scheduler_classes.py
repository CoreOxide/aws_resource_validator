from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.scheduler.scheduler_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AwsVpcConfigurationOutput(BaseValidatorModel):
    Subnets: List[str]
    AssignPublicIp: Optional[AssignPublicIpType] = None
    SecurityGroups: Optional[List[str]] = None


class AwsVpcConfiguration(BaseValidatorModel):
    Subnets: List[str]
    AssignPublicIp: Optional[AssignPublicIpType] = None
    SecurityGroups: Optional[List[str]] = None


class CapacityProviderStrategyItem(BaseValidatorModel):
    capacityProvider: str
    base: Optional[int] = None
    weight: Optional[int] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class FlexibleTimeWindow(BaseValidatorModel):
    Mode: FlexibleTimeWindowModeType
    MaximumWindowInMinutes: Optional[int] = None

Timestamp = Union[datetime, str]


class DeadLetterConfig(BaseValidatorModel):
    Arn: Optional[str] = None


class DeleteScheduleGroupInput(BaseValidatorModel):
    Name: str
    ClientToken: Optional[str] = None


class DeleteScheduleInput(BaseValidatorModel):
    Name: str
    ClientToken: Optional[str] = None
    GroupName: Optional[str] = None


class PlacementConstraint(BaseValidatorModel):
    expression: Optional[str] = None
    type: Optional[PlacementConstraintTypeType] = None


class PlacementStrategy(BaseValidatorModel):
    field: Optional[str] = None
    type: Optional[PlacementStrategyTypeType] = None


class EventBridgeParameters(BaseValidatorModel):
    DetailType: str
    Source: str


class GetScheduleGroupInput(BaseValidatorModel):
    Name: str


class GetScheduleInput(BaseValidatorModel):
    Name: str
    GroupName: Optional[str] = None


class KinesisParameters(BaseValidatorModel):
    PartitionKey: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListScheduleGroupsInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NamePrefix: Optional[str] = None
    NextToken: Optional[str] = None


class ScheduleGroupSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    CreationDate: Optional[datetime] = None
    LastModificationDate: Optional[datetime] = None
    Name: Optional[str] = None
    State: Optional[ScheduleGroupStateType] = None


class ListSchedulesInput(BaseValidatorModel):
    GroupName: Optional[str] = None
    MaxResults: Optional[int] = None
    NamePrefix: Optional[str] = None
    NextToken: Optional[str] = None
    State: Optional[ScheduleStateType] = None


class ListTagsForResourceInput(BaseValidatorModel):
    ResourceArn: str


class RetryPolicy(BaseValidatorModel):
    MaximumEventAgeInSeconds: Optional[int] = None
    MaximumRetryAttempts: Optional[int] = None


class SageMakerPipelineParameter(BaseValidatorModel):
    Name: str
    Value: str


class TargetSummary(BaseValidatorModel):
    Arn: str


class SqsParameters(BaseValidatorModel):
    MessageGroupId: Optional[str] = None


class UntagResourceInput(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class NetworkConfigurationOutput(BaseValidatorModel):
    awsvpcConfiguration: Optional[AwsVpcConfigurationOutput] = None


class NetworkConfiguration(BaseValidatorModel):
    awsvpcConfiguration: Optional[AwsVpcConfiguration] = None


class CreateScheduleGroupInput(BaseValidatorModel):
    Name: str
    ClientToken: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class TagResourceInput(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


class CreateScheduleGroupOutput(BaseValidatorModel):
    ScheduleGroupArn: str
    ResponseMetadata: ResponseMetadata


class CreateScheduleOutput(BaseValidatorModel):
    ScheduleArn: str
    ResponseMetadata: ResponseMetadata


class GetScheduleGroupOutput(BaseValidatorModel):
    Arn: str
    CreationDate: datetime
    LastModificationDate: datetime
    Name: str
    State: ScheduleGroupStateType
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceOutput(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class UpdateScheduleOutput(BaseValidatorModel):
    ScheduleArn: str
    ResponseMetadata: ResponseMetadata


class ListScheduleGroupsInputPaginate(BaseValidatorModel):
    NamePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSchedulesInputPaginate(BaseValidatorModel):
    GroupName: Optional[str] = None
    NamePrefix: Optional[str] = None
    State: Optional[ScheduleStateType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListScheduleGroupsOutput(BaseValidatorModel):
    ScheduleGroups: List[ScheduleGroupSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SageMakerPipelineParametersOutput(BaseValidatorModel):
    PipelineParameterList: Optional[List[SageMakerPipelineParameter]] = None


class SageMakerPipelineParameters(BaseValidatorModel):
    PipelineParameterList: Optional[List[SageMakerPipelineParameter]] = None


class ScheduleSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    CreationDate: Optional[datetime] = None
    GroupName: Optional[str] = None
    LastModificationDate: Optional[datetime] = None
    Name: Optional[str] = None
    State: Optional[ScheduleStateType] = None
    Target: Optional[TargetSummary] = None


class EcsParametersOutput(BaseValidatorModel):
    TaskDefinitionArn: str
    CapacityProviderStrategy: Optional[List[CapacityProviderStrategyItem]] = None
    EnableECSManagedTags: Optional[bool] = None
    EnableExecuteCommand: Optional[bool] = None
    Group: Optional[str] = None
    LaunchType: Optional[LaunchTypeType] = None
    NetworkConfiguration: Optional[NetworkConfigurationOutput] = None
    PlacementConstraints: Optional[List[PlacementConstraint]] = None
    PlacementStrategy: Optional[List[PlacementStrategy]] = None
    PlatformVersion: Optional[str] = None
    PropagateTags: Optional[Literal['TASK_DEFINITION']] = None
    ReferenceId: Optional[str] = None
    Tags: Optional[List[Dict[str, str]]] = None
    TaskCount: Optional[int] = None


class EcsParameters(BaseValidatorModel):
    TaskDefinitionArn: str
    CapacityProviderStrategy: Optional[List[CapacityProviderStrategyItem]] = None
    EnableECSManagedTags: Optional[bool] = None
    EnableExecuteCommand: Optional[bool] = None
    Group: Optional[str] = None
    LaunchType: Optional[LaunchTypeType] = None
    NetworkConfiguration: Optional[NetworkConfiguration] = None
    PlacementConstraints: Optional[List[PlacementConstraint]] = None
    PlacementStrategy: Optional[List[PlacementStrategy]] = None
    PlatformVersion: Optional[str] = None
    PropagateTags: Optional[Literal['TASK_DEFINITION']] = None
    ReferenceId: Optional[str] = None
    Tags: Optional[List[Dict[str, str]]] = None
    TaskCount: Optional[int] = None


class ListSchedulesOutput(BaseValidatorModel):
    Schedules: List[ScheduleSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TargetOutput(BaseValidatorModel):
    Arn: str
    RoleArn: str
    DeadLetterConfig: Optional[DeadLetterConfig] = None
    EcsParameters: Optional[EcsParametersOutput] = None
    EventBridgeParameters: Optional[EventBridgeParameters] = None
    Input: Optional[str] = None
    KinesisParameters: Optional[KinesisParameters] = None
    RetryPolicy: Optional[RetryPolicy] = None
    SageMakerPipelineParameters: Optional[SageMakerPipelineParametersOutput] = None
    SqsParameters: Optional[SqsParameters] = None


class Target(BaseValidatorModel):
    Arn: str
    RoleArn: str
    DeadLetterConfig: Optional[DeadLetterConfig] = None
    EcsParameters: Optional[EcsParameters] = None
    EventBridgeParameters: Optional[EventBridgeParameters] = None
    Input: Optional[str] = None
    KinesisParameters: Optional[KinesisParameters] = None
    RetryPolicy: Optional[RetryPolicy] = None
    SageMakerPipelineParameters: Optional[SageMakerPipelineParameters] = None
    SqsParameters: Optional[SqsParameters] = None


class GetScheduleOutput(BaseValidatorModel):
    ActionAfterCompletion: ActionAfterCompletionType
    Arn: str
    CreationDate: datetime
    Description: str
    EndDate: datetime
    FlexibleTimeWindow: FlexibleTimeWindow
    GroupName: str
    KmsKeyArn: str
    LastModificationDate: datetime
    Name: str
    ScheduleExpression: str
    ScheduleExpressionTimezone: str
    StartDate: datetime
    State: ScheduleStateType
    Target: TargetOutput
    ResponseMetadata: ResponseMetadata

TargetUnion = Union[Target, TargetOutput]


class CreateScheduleInput(BaseValidatorModel):
    FlexibleTimeWindow: FlexibleTimeWindow
    Name: str
    ScheduleExpression: str
    Target: TargetUnion
    ActionAfterCompletion: Optional[ActionAfterCompletionType] = None
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    EndDate: Optional[Timestamp] = None
    GroupName: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    ScheduleExpressionTimezone: Optional[str] = None
    StartDate: Optional[Timestamp] = None
    State: Optional[ScheduleStateType] = None


class UpdateScheduleInput(BaseValidatorModel):
    FlexibleTimeWindow: FlexibleTimeWindow
    Name: str
    ScheduleExpression: str
    Target: TargetUnion
    ActionAfterCompletion: Optional[ActionAfterCompletionType] = None
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    EndDate: Optional[Timestamp] = None
    GroupName: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    ScheduleExpressionTimezone: Optional[str] = None
    StartDate: Optional[Timestamp] = None
    State: Optional[ScheduleStateType] = None