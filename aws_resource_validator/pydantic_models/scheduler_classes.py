from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class AwsVpcConfigurationTypeDef(BaseValidatorModel):
    Subnets: Sequence[str]
    AssignPublicIp: Optional[AssignPublicIpType] = None
    SecurityGroups: Optional[Sequence[str]] = None

class CapacityProviderStrategyItemTypeDef(BaseValidatorModel):
    capacityProvider: str
    base: Optional[int] = None
    weight: Optional[int] = None

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class FlexibleTimeWindowTypeDef(BaseValidatorModel):
    Mode: FlexibleTimeWindowModeType
    MaximumWindowInMinutes: Optional[int] = None

class DeadLetterConfigTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None

class DeleteScheduleGroupInputRequestTypeDef(BaseValidatorModel):
    Name: str
    ClientToken: Optional[str] = None

class DeleteScheduleInputRequestTypeDef(BaseValidatorModel):
    Name: str
    ClientToken: Optional[str] = None
    GroupName: Optional[str] = None

class PlacementConstraintTypeDef(BaseValidatorModel):
    expression: Optional[str] = None
    type: Optional[PlacementConstraintTypeType] = None

class PlacementStrategyTypeDef(BaseValidatorModel):
    field: Optional[str] = None
    type: Optional[PlacementStrategyTypeType] = None

class EventBridgeParametersTypeDef(BaseValidatorModel):
    DetailType: str
    Source: str

class GetScheduleGroupInputRequestTypeDef(BaseValidatorModel):
    Name: str

class GetScheduleInputRequestTypeDef(BaseValidatorModel):
    Name: str
    GroupName: Optional[str] = None

class KinesisParametersTypeDef(BaseValidatorModel):
    PartitionKey: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListScheduleGroupsInputRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NamePrefix: Optional[str] = None
    NextToken: Optional[str] = None

class ScheduleGroupSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CreationDate: Optional[datetime] = None
    LastModificationDate: Optional[datetime] = None
    Name: Optional[str] = None
    State: Optional[ScheduleGroupStateType] = None

class ListSchedulesInputRequestTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    MaxResults: Optional[int] = None
    NamePrefix: Optional[str] = None
    NextToken: Optional[str] = None
    State: Optional[ScheduleStateType] = None

class ListTagsForResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class RetryPolicyTypeDef(BaseValidatorModel):
    MaximumEventAgeInSeconds: Optional[int] = None
    MaximumRetryAttempts: Optional[int] = None

class SageMakerPipelineParameterTypeDef(BaseValidatorModel):
    Name: str
    Value: str

class TargetSummaryTypeDef(BaseValidatorModel):
    Arn: str

class SqsParametersTypeDef(BaseValidatorModel):
    MessageGroupId: Optional[str] = None

class UntagResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class NetworkConfigurationTypeDef(BaseValidatorModel):
    awsvpcConfiguration: Optional[AwsVpcConfigurationTypeDef] = None

class CreateScheduleGroupInputRequestTypeDef(BaseValidatorModel):
    Name: str
    ClientToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateScheduleGroupOutputTypeDef(BaseValidatorModel):
    ScheduleGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateScheduleOutputTypeDef(BaseValidatorModel):
    ScheduleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetScheduleGroupOutputTypeDef(BaseValidatorModel):
    Arn: str
    CreationDate: datetime
    LastModificationDate: datetime
    Name: str
    State: ScheduleGroupStateType
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateScheduleOutputTypeDef(BaseValidatorModel):
    ScheduleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListScheduleGroupsInputListScheduleGroupsPaginateTypeDef(BaseValidatorModel):
    NamePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSchedulesInputListSchedulesPaginateTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    NamePrefix: Optional[str] = None
    State: Optional[ScheduleStateType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListScheduleGroupsOutputTypeDef(BaseValidatorModel):
    NextToken: str
    ScheduleGroups: List[ScheduleGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SageMakerPipelineParametersTypeDef(BaseValidatorModel):
    PipelineParameterList: Optional[Sequence[SageMakerPipelineParameterTypeDef]] = None

class ScheduleSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CreationDate: Optional[datetime] = None
    GroupName: Optional[str] = None
    LastModificationDate: Optional[datetime] = None
    Name: Optional[str] = None
    State: Optional[ScheduleStateType] = None
    Target: Optional[TargetSummaryTypeDef] = None

class EcsParametersTypeDef(BaseValidatorModel):
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

class ListSchedulesOutputTypeDef(BaseValidatorModel):
    NextToken: str
    Schedules: List[ScheduleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TargetTypeDef(BaseValidatorModel):
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

class CreateScheduleInputRequestTypeDef(BaseValidatorModel):
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

class GetScheduleOutputTypeDef(BaseValidatorModel):
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

class UpdateScheduleInputRequestTypeDef(BaseValidatorModel):
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

