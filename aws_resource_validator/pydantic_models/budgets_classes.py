from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from botocore.response import StreamingBody
from datetime import datetime
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.budgets_constants import *

class ActionThreshold(BaseValidatorModel):
    ActionThresholdValue: float
    ActionThresholdType: ThresholdTypeType


class Subscriber(BaseValidatorModel):
    SubscriptionType: SubscriptionTypeType
    Address: str


class HistoricalOptions(BaseValidatorModel):
    BudgetAdjustmentPeriod: int
    LookBackAvailablePeriods: Optional[int] = None


class Notification(BaseValidatorModel):
    NotificationType: NotificationTypeType
    ComparisonOperator: ComparisonOperatorType
    Threshold: float
    ThresholdType: Optional[ThresholdTypeType] = None
    NotificationState: Optional[NotificationStateType] = None


class CostTypes(BaseValidatorModel):
    IncludeTax: Optional[bool] = None
    IncludeSubscription: Optional[bool] = None
    UseBlended: Optional[bool] = None
    IncludeRefund: Optional[bool] = None
    IncludeCredit: Optional[bool] = None
    IncludeUpfront: Optional[bool] = None
    IncludeRecurring: Optional[bool] = None
    IncludeOtherSubscription: Optional[bool] = None
    IncludeSupport: Optional[bool] = None
    IncludeDiscount: Optional[bool] = None
    UseAmortized: Optional[bool] = None


class Spend(BaseValidatorModel):
    Amount: str
    Unit: str


class TimePeriodOutput(BaseValidatorModel):
    Start: Optional[datetime] = None
    End: Optional[datetime] = None


class ResourceTag(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class IamActionDefinitionOutput(BaseValidatorModel):
    PolicyArn: str
    Roles: Optional[List[str]] = None
    Groups: Optional[List[str]] = None
    Users: Optional[List[str]] = None


class ScpActionDefinitionOutput(BaseValidatorModel):
    PolicyId: str
    TargetIds: List[str]


class SsmActionDefinitionOutput(BaseValidatorModel):
    ActionSubType: ActionSubTypeType
    Region: str
    InstanceIds: List[str]


class IamActionDefinition(BaseValidatorModel):
    PolicyArn: str
    Roles: Optional[Sequence[str]] = None
    Groups: Optional[Sequence[str]] = None
    Users: Optional[Sequence[str]] = None


class ScpActionDefinition(BaseValidatorModel):
    PolicyId: str
    TargetIds: Sequence[str]


class SsmActionDefinition(BaseValidatorModel):
    ActionSubType: ActionSubTypeType
    Region: str
    InstanceIds: Sequence[str]


class DeleteBudgetActionRequest(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    ActionId: str


class DeleteBudgetRequest(BaseValidatorModel):
    AccountId: str
    BudgetName: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeBudgetActionRequest(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    ActionId: str


class DescribeBudgetActionsForAccountRequest(BaseValidatorModel):
    AccountId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeBudgetActionsForBudgetRequest(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeBudgetNotificationsForAccountRequest(BaseValidatorModel):
    AccountId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeBudgetRequest(BaseValidatorModel):
    AccountId: str
    BudgetName: str


class DescribeBudgetsRequest(BaseValidatorModel):
    AccountId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeNotificationsForBudgetRequest(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ExecuteBudgetActionRequest(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    ActionId: str
    ExecutionType: ExecutionTypeType


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    ResourceTagKeys: Sequence[str]


class AutoAdjustDataOutput(BaseValidatorModel):
    AutoAdjustType: AutoAdjustTypeType
    HistoricalOptions: Optional[HistoricalOptions] = None
    LastAutoAdjustTime: Optional[datetime] = None


class Timestamp(BaseValidatorModel):
    pass


class AutoAdjustData(BaseValidatorModel):
    AutoAdjustType: AutoAdjustTypeType
    HistoricalOptions: Optional[HistoricalOptions] = None
    LastAutoAdjustTime: Optional[Timestamp] = None


class TimePeriod(BaseValidatorModel):
    Start: Optional[Timestamp] = None
    End: Optional[Timestamp] = None


class BudgetNotificationsForAccount(BaseValidatorModel):
    Notifications: Optional[List[Notification]] = None
    BudgetName: Optional[str] = None


class CreateNotificationRequest(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    Notification: Notification
    Subscribers: Sequence[Subscriber]


class CreateSubscriberRequest(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    Notification: Notification
    Subscriber: Subscriber


class DeleteNotificationRequest(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    Notification: Notification


class DeleteSubscriberRequest(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    Notification: Notification
    Subscriber: Subscriber


class DescribeSubscribersForNotificationRequest(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    Notification: Notification
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class NotificationWithSubscribers(BaseValidatorModel):
    Notification: Notification
    Subscribers: Sequence[Subscriber]


class UpdateNotificationRequest(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    OldNotification: Notification
    NewNotification: Notification


class UpdateSubscriberRequest(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    Notification: Notification
    OldSubscriber: Subscriber
    NewSubscriber: Subscriber


class CalculatedSpend(BaseValidatorModel):
    ActualSpend: Spend
    ForecastedSpend: Optional[Spend] = None


class BudgetedAndActualAmounts(BaseValidatorModel):
    BudgetedAmount: Optional[Spend] = None
    ActualAmount: Optional[Spend] = None
    TimePeriod: Optional[TimePeriodOutput] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    ResourceTags: Sequence[ResourceTag]


class CreateBudgetActionResponse(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    ActionId: str
    ResponseMetadata: ResponseMetadata


class DescribeNotificationsForBudgetResponse(BaseValidatorModel):
    Notifications: List[Notification]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeSubscribersForNotificationResponse(BaseValidatorModel):
    Subscribers: List[Subscriber]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ExecuteBudgetActionResponse(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    ActionId: str
    ExecutionType: ExecutionTypeType
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    ResourceTags: List[ResourceTag]
    ResponseMetadata: ResponseMetadata


class DefinitionOutput(BaseValidatorModel):
    IamActionDefinition: Optional[IamActionDefinitionOutput] = None
    ScpActionDefinition: Optional[ScpActionDefinitionOutput] = None
    SsmActionDefinition: Optional[SsmActionDefinitionOutput] = None


class Definition(BaseValidatorModel):
    IamActionDefinition: Optional[IamActionDefinition] = None
    ScpActionDefinition: Optional[ScpActionDefinition] = None
    SsmActionDefinition: Optional[SsmActionDefinition] = None


class DescribeBudgetActionsForAccountRequestPaginate(BaseValidatorModel):
    AccountId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeBudgetActionsForBudgetRequestPaginate(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeBudgetNotificationsForAccountRequestPaginate(BaseValidatorModel):
    AccountId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeBudgetsRequestPaginate(BaseValidatorModel):
    AccountId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeNotificationsForBudgetRequestPaginate(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeSubscribersForNotificationRequestPaginate(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    Notification: Notification
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeBudgetNotificationsForAccountResponse(BaseValidatorModel):
    BudgetNotificationsForAccount: List[BudgetNotificationsForAccount]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class BudgetOutput(BaseValidatorModel):
    BudgetName: str
    TimeUnit: TimeUnitType
    BudgetType: BudgetTypeType
    BudgetLimit: Optional[Spend] = None
    PlannedBudgetLimits: Optional[Dict[str, Spend]] = None
    CostFilters: Optional[Dict[str, List[str]]] = None
    CostTypes: Optional[CostTypes] = None
    TimePeriod: Optional[TimePeriodOutput] = None
    CalculatedSpend: Optional[CalculatedSpend] = None
    LastUpdatedTime: Optional[datetime] = None
    AutoAdjustData: Optional[AutoAdjustDataOutput] = None


class Budget(BaseValidatorModel):
    BudgetName: str
    TimeUnit: TimeUnitType
    BudgetType: BudgetTypeType
    BudgetLimit: Optional[Spend] = None
    PlannedBudgetLimits: Optional[Mapping[str, Spend]] = None
    CostFilters: Optional[Mapping[str, Sequence[str]]] = None
    CostTypes: Optional[CostTypes] = None
    TimePeriod: Optional[TimePeriod] = None
    CalculatedSpend: Optional[CalculatedSpend] = None
    LastUpdatedTime: Optional[Timestamp] = None
    AutoAdjustData: Optional[AutoAdjustData] = None


class BudgetPerformanceHistory(BaseValidatorModel):
    BudgetName: Optional[str] = None
    BudgetType: Optional[BudgetTypeType] = None
    CostFilters: Optional[Dict[str, List[str]]] = None
    CostTypes: Optional[CostTypes] = None
    TimeUnit: Optional[TimeUnitType] = None
    BudgetedAndActualAmountsList: Optional[List[BudgetedAndActualAmounts]] = None


class Action(BaseValidatorModel):
    ActionId: str
    BudgetName: str
    NotificationType: NotificationTypeType
    ActionType: ActionTypeType
    ActionThreshold: ActionThreshold
    Definition: DefinitionOutput
    ExecutionRoleArn: str
    ApprovalModel: ApprovalModelType
    Status: ActionStatusType
    Subscribers: List[Subscriber]


class TimePeriodUnion(BaseValidatorModel):
    pass


class DescribeBudgetActionHistoriesRequestPaginate(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    ActionId: str
    TimePeriod: Optional[TimePeriodUnion] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeBudgetActionHistoriesRequest(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    ActionId: str
    TimePeriod: Optional[TimePeriodUnion] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeBudgetPerformanceHistoryRequestPaginate(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    TimePeriod: Optional[TimePeriodUnion] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeBudgetPerformanceHistoryRequest(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    TimePeriod: Optional[TimePeriodUnion] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeBudgetResponse(BaseValidatorModel):
    Budget: BudgetOutput
    ResponseMetadata: ResponseMetadata


class DescribeBudgetsResponse(BaseValidatorModel):
    Budgets: List[BudgetOutput]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeBudgetPerformanceHistoryResponse(BaseValidatorModel):
    BudgetPerformanceHistory: BudgetPerformanceHistory
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ActionHistoryDetails(BaseValidatorModel):
    Message: str
    Action: Action


class DeleteBudgetActionResponse(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    Action: Action
    ResponseMetadata: ResponseMetadata


class DescribeBudgetActionResponse(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    Action: Action
    ResponseMetadata: ResponseMetadata


class DescribeBudgetActionsForAccountResponse(BaseValidatorModel):
    Actions: List[Action]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeBudgetActionsForBudgetResponse(BaseValidatorModel):
    Actions: List[Action]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateBudgetActionResponse(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    OldAction: Action
    NewAction: Action
    ResponseMetadata: ResponseMetadata


class DefinitionUnion(BaseValidatorModel):
    pass


class CreateBudgetActionRequest(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    NotificationType: NotificationTypeType
    ActionType: ActionTypeType
    ActionThreshold: ActionThreshold
    Definition: DefinitionUnion
    ExecutionRoleArn: str
    ApprovalModel: ApprovalModelType
    Subscribers: Sequence[Subscriber]
    ResourceTags: Optional[Sequence[ResourceTag]] = None


class UpdateBudgetActionRequest(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    ActionId: str
    NotificationType: Optional[NotificationTypeType] = None
    ActionThreshold: Optional[ActionThreshold] = None
    Definition: Optional[DefinitionUnion] = None
    ExecutionRoleArn: Optional[str] = None
    ApprovalModel: Optional[ApprovalModelType] = None
    Subscribers: Optional[Sequence[Subscriber]] = None


class BudgetUnion(BaseValidatorModel):
    pass


class CreateBudgetRequest(BaseValidatorModel):
    AccountId: str
    Budget: BudgetUnion
    NotificationsWithSubscribers: Optional[Sequence[NotificationWithSubscribers]] = None
    ResourceTags: Optional[Sequence[ResourceTag]] = None


class UpdateBudgetRequest(BaseValidatorModel):
    AccountId: str
    NewBudget: BudgetUnion


class ActionHistory(BaseValidatorModel):
    Timestamp: datetime
    Status: ActionStatusType
    EventType: EventTypeType
    ActionHistoryDetails: ActionHistoryDetails


class DescribeBudgetActionHistoriesResponse(BaseValidatorModel):
    ActionHistories: List[ActionHistory]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


