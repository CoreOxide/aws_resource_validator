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

class ActionThresholdTypeDef(BaseValidatorModel):
    ActionThresholdValue: float
    ActionThresholdType: ThresholdTypeType


class SubscriberTypeDef(BaseValidatorModel):
    SubscriptionType: SubscriptionTypeType
    Address: str


class HistoricalOptionsTypeDef(BaseValidatorModel):
    BudgetAdjustmentPeriod: int
    LookBackAvailablePeriods: Optional[int] = None


class NotificationTypeDef(BaseValidatorModel):
    NotificationType: NotificationTypeType
    ComparisonOperator: ComparisonOperatorType
    Threshold: float
    ThresholdType: Optional[ThresholdTypeType] = None
    NotificationState: Optional[NotificationStateType] = None


class CostTypesTypeDef(BaseValidatorModel):
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


class SpendTypeDef(BaseValidatorModel):
    Amount: str
    Unit: str


class TimePeriodOutputTypeDef(BaseValidatorModel):
    Start: Optional[datetime] = None
    End: Optional[datetime] = None


class ResourceTagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class IamActionDefinitionOutputTypeDef(BaseValidatorModel):
    PolicyArn: str
    Roles: Optional[List[str]] = None
    Groups: Optional[List[str]] = None
    Users: Optional[List[str]] = None


class ScpActionDefinitionOutputTypeDef(BaseValidatorModel):
    PolicyId: str
    TargetIds: List[str]


class SsmActionDefinitionOutputTypeDef(BaseValidatorModel):
    ActionSubType: ActionSubTypeType
    Region: str
    InstanceIds: List[str]


class IamActionDefinitionTypeDef(BaseValidatorModel):
    PolicyArn: str
    Roles: Optional[Sequence[str]] = None
    Groups: Optional[Sequence[str]] = None
    Users: Optional[Sequence[str]] = None


class ScpActionDefinitionTypeDef(BaseValidatorModel):
    PolicyId: str
    TargetIds: Sequence[str]


class SsmActionDefinitionTypeDef(BaseValidatorModel):
    ActionSubType: ActionSubTypeType
    Region: str
    InstanceIds: Sequence[str]


class DeleteBudgetActionRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    ActionId: str


class DeleteBudgetRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeBudgetActionRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    ActionId: str


class DescribeBudgetActionsForAccountRequestTypeDef(BaseValidatorModel):
    AccountId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeBudgetActionsForBudgetRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeBudgetNotificationsForAccountRequestTypeDef(BaseValidatorModel):
    AccountId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeBudgetRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str


class DescribeBudgetsRequestTypeDef(BaseValidatorModel):
    AccountId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeNotificationsForBudgetRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ExecuteBudgetActionRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    ActionId: str
    ExecutionType: ExecutionTypeType


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    ResourceTagKeys: Sequence[str]


class AutoAdjustDataOutputTypeDef(BaseValidatorModel):
    AutoAdjustType: AutoAdjustTypeType
    HistoricalOptions: Optional[HistoricalOptionsTypeDef] = None
    LastAutoAdjustTime: Optional[datetime] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class AutoAdjustDataTypeDef(BaseValidatorModel):
    AutoAdjustType: AutoAdjustTypeType
    HistoricalOptions: Optional[HistoricalOptionsTypeDef] = None
    LastAutoAdjustTime: Optional[TimestampTypeDef] = None


class TimePeriodTypeDef(BaseValidatorModel):
    Start: Optional[TimestampTypeDef] = None
    End: Optional[TimestampTypeDef] = None


class BudgetNotificationsForAccountTypeDef(BaseValidatorModel):
    Notifications: Optional[List[NotificationTypeDef]] = None
    BudgetName: Optional[str] = None


class CreateNotificationRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    Notification: NotificationTypeDef
    Subscribers: Sequence[SubscriberTypeDef]


class CreateSubscriberRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    Notification: NotificationTypeDef
    Subscriber: SubscriberTypeDef


class DeleteNotificationRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    Notification: NotificationTypeDef


class DeleteSubscriberRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    Notification: NotificationTypeDef
    Subscriber: SubscriberTypeDef


class DescribeSubscribersForNotificationRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    Notification: NotificationTypeDef
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class NotificationWithSubscribersTypeDef(BaseValidatorModel):
    Notification: NotificationTypeDef
    Subscribers: Sequence[SubscriberTypeDef]


class UpdateNotificationRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    OldNotification: NotificationTypeDef
    NewNotification: NotificationTypeDef


class UpdateSubscriberRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    Notification: NotificationTypeDef
    OldSubscriber: SubscriberTypeDef
    NewSubscriber: SubscriberTypeDef


class CalculatedSpendTypeDef(BaseValidatorModel):
    ActualSpend: SpendTypeDef
    ForecastedSpend: Optional[SpendTypeDef] = None


class BudgetedAndActualAmountsTypeDef(BaseValidatorModel):
    BudgetedAmount: Optional[SpendTypeDef] = None
    ActualAmount: Optional[SpendTypeDef] = None
    TimePeriod: Optional[TimePeriodOutputTypeDef] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    ResourceTags: Sequence[ResourceTagTypeDef]


class CreateBudgetActionResponseTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    ActionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeNotificationsForBudgetResponseTypeDef(BaseValidatorModel):
    Notifications: List[NotificationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeSubscribersForNotificationResponseTypeDef(BaseValidatorModel):
    Subscribers: List[SubscriberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ExecuteBudgetActionResponseTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    ActionId: str
    ExecutionType: ExecutionTypeType
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    ResourceTags: List[ResourceTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DefinitionOutputTypeDef(BaseValidatorModel):
    IamActionDefinition: Optional[IamActionDefinitionOutputTypeDef] = None
    ScpActionDefinition: Optional[ScpActionDefinitionOutputTypeDef] = None
    SsmActionDefinition: Optional[SsmActionDefinitionOutputTypeDef] = None


class DefinitionTypeDef(BaseValidatorModel):
    IamActionDefinition: Optional[IamActionDefinitionTypeDef] = None
    ScpActionDefinition: Optional[ScpActionDefinitionTypeDef] = None
    SsmActionDefinition: Optional[SsmActionDefinitionTypeDef] = None


class DescribeBudgetActionsForAccountRequestPaginateTypeDef(BaseValidatorModel):
    AccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeBudgetActionsForBudgetRequestPaginateTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeBudgetNotificationsForAccountRequestPaginateTypeDef(BaseValidatorModel):
    AccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeBudgetsRequestPaginateTypeDef(BaseValidatorModel):
    AccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeNotificationsForBudgetRequestPaginateTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeSubscribersForNotificationRequestPaginateTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    Notification: NotificationTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeBudgetNotificationsForAccountResponseTypeDef(BaseValidatorModel):
    BudgetNotificationsForAccount: List[BudgetNotificationsForAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class BudgetOutputTypeDef(BaseValidatorModel):
    BudgetName: str
    TimeUnit: TimeUnitType
    BudgetType: BudgetTypeType
    BudgetLimit: Optional[SpendTypeDef] = None
    PlannedBudgetLimits: Optional[Dict[str, SpendTypeDef]] = None
    CostFilters: Optional[Dict[str, List[str]]] = None
    CostTypes: Optional[CostTypesTypeDef] = None
    TimePeriod: Optional[TimePeriodOutputTypeDef] = None
    CalculatedSpend: Optional[CalculatedSpendTypeDef] = None
    LastUpdatedTime: Optional[datetime] = None
    AutoAdjustData: Optional[AutoAdjustDataOutputTypeDef] = None


class BudgetTypeDef(BaseValidatorModel):
    BudgetName: str
    TimeUnit: TimeUnitType
    BudgetType: BudgetTypeType
    BudgetLimit: Optional[SpendTypeDef] = None
    PlannedBudgetLimits: Optional[Mapping[str, SpendTypeDef]] = None
    CostFilters: Optional[Mapping[str, Sequence[str]]] = None
    CostTypes: Optional[CostTypesTypeDef] = None
    TimePeriod: Optional[TimePeriodTypeDef] = None
    CalculatedSpend: Optional[CalculatedSpendTypeDef] = None
    LastUpdatedTime: Optional[TimestampTypeDef] = None
    AutoAdjustData: Optional[AutoAdjustDataTypeDef] = None


class BudgetPerformanceHistoryTypeDef(BaseValidatorModel):
    BudgetName: Optional[str] = None
    BudgetType: Optional[BudgetTypeType] = None
    CostFilters: Optional[Dict[str, List[str]]] = None
    CostTypes: Optional[CostTypesTypeDef] = None
    TimeUnit: Optional[TimeUnitType] = None
    BudgetedAndActualAmountsList: Optional[List[BudgetedAndActualAmountsTypeDef]] = None


class ActionTypeDef(BaseValidatorModel):
    ActionId: str
    BudgetName: str
    NotificationType: NotificationTypeType
    ActionType: ActionTypeType
    ActionThreshold: ActionThresholdTypeDef
    Definition: DefinitionOutputTypeDef
    ExecutionRoleArn: str
    ApprovalModel: ApprovalModelType
    Status: ActionStatusType
    Subscribers: List[SubscriberTypeDef]


class TimePeriodUnionTypeDef(BaseValidatorModel):
    pass


class DescribeBudgetActionHistoriesRequestPaginateTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    ActionId: str
    TimePeriod: Optional[TimePeriodUnionTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeBudgetActionHistoriesRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    ActionId: str
    TimePeriod: Optional[TimePeriodUnionTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeBudgetPerformanceHistoryRequestPaginateTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    TimePeriod: Optional[TimePeriodUnionTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeBudgetPerformanceHistoryRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    TimePeriod: Optional[TimePeriodUnionTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeBudgetResponseTypeDef(BaseValidatorModel):
    Budget: BudgetOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeBudgetsResponseTypeDef(BaseValidatorModel):
    Budgets: List[BudgetOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeBudgetPerformanceHistoryResponseTypeDef(BaseValidatorModel):
    BudgetPerformanceHistory: BudgetPerformanceHistoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ActionHistoryDetailsTypeDef(BaseValidatorModel):
    Message: str
    Action: ActionTypeDef


class DeleteBudgetActionResponseTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    Action: ActionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeBudgetActionResponseTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    Action: ActionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeBudgetActionsForAccountResponseTypeDef(BaseValidatorModel):
    Actions: List[ActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeBudgetActionsForBudgetResponseTypeDef(BaseValidatorModel):
    Actions: List[ActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateBudgetActionResponseTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    OldAction: ActionTypeDef
    NewAction: ActionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DefinitionUnionTypeDef(BaseValidatorModel):
    pass


class CreateBudgetActionRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    NotificationType: NotificationTypeType
    ActionType: ActionTypeType
    ActionThreshold: ActionThresholdTypeDef
    Definition: DefinitionUnionTypeDef
    ExecutionRoleArn: str
    ApprovalModel: ApprovalModelType
    Subscribers: Sequence[SubscriberTypeDef]
    ResourceTags: Optional[Sequence[ResourceTagTypeDef]] = None


class UpdateBudgetActionRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    ActionId: str
    NotificationType: Optional[NotificationTypeType] = None
    ActionThreshold: Optional[ActionThresholdTypeDef] = None
    Definition: Optional[DefinitionUnionTypeDef] = None
    ExecutionRoleArn: Optional[str] = None
    ApprovalModel: Optional[ApprovalModelType] = None
    Subscribers: Optional[Sequence[SubscriberTypeDef]] = None


class BudgetUnionTypeDef(BaseValidatorModel):
    pass


class CreateBudgetRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Budget: BudgetUnionTypeDef
    NotificationsWithSubscribers: Optional[Sequence[NotificationWithSubscribersTypeDef]] = None
    ResourceTags: Optional[Sequence[ResourceTagTypeDef]] = None


class UpdateBudgetRequestTypeDef(BaseValidatorModel):
    AccountId: str
    NewBudget: BudgetUnionTypeDef


class ActionHistoryTypeDef(BaseValidatorModel):
    Timestamp: datetime
    Status: ActionStatusType
    EventType: EventTypeType
    ActionHistoryDetails: ActionHistoryDetailsTypeDef


class DescribeBudgetActionHistoriesResponseTypeDef(BaseValidatorModel):
    ActionHistories: List[ActionHistoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


