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
from aws_resource_validator.pydantic_models.budgets_constants import *

class ActionThresholdTypeDef(BaseModel):
    ActionThresholdValue: float
    ActionThresholdType: ThresholdTypeType

class SubscriberTypeDef(BaseModel):
    SubscriptionType: SubscriptionTypeType
    Address: str

class HistoricalOptionsTypeDef(BaseModel):
    BudgetAdjustmentPeriod: int
    LookBackAvailablePeriods: Optional[int] = None

class CostTypesTypeDef(BaseModel):
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

class SpendTypeDef(BaseModel):
    Amount: str
    Unit: str

class TimePeriodExtraOutputTypeDef(BaseModel):
    Start: Optional[datetime] = None
    End: Optional[datetime] = None

class NotificationTypeDef(BaseModel):
    NotificationType: NotificationTypeType
    ComparisonOperator: ComparisonOperatorType
    Threshold: float
    ThresholdType: Optional[ThresholdTypeType] = None
    NotificationState: Optional[NotificationStateType] = None

class TimePeriodOutputTypeDef(BaseModel):
    Start: Optional[datetime] = None
    End: Optional[datetime] = None

class ResourceTagTypeDef(BaseModel):
    Key: str
    Value: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class IamActionDefinitionExtraOutputTypeDef(BaseModel):
    PolicyArn: str
    Roles: Optional[List[str]] = None
    Groups: Optional[List[str]] = None
    Users: Optional[List[str]] = None

class ScpActionDefinitionExtraOutputTypeDef(BaseModel):
    PolicyId: str
    TargetIds: List[str]

class SsmActionDefinitionExtraOutputTypeDef(BaseModel):
    ActionSubType: ActionSubTypeType
    Region: str
    InstanceIds: List[str]

class IamActionDefinitionOutputTypeDef(BaseModel):
    PolicyArn: str
    Roles: Optional[List[str]] = None
    Groups: Optional[List[str]] = None
    Users: Optional[List[str]] = None

class ScpActionDefinitionOutputTypeDef(BaseModel):
    PolicyId: str
    TargetIds: List[str]

class SsmActionDefinitionOutputTypeDef(BaseModel):
    ActionSubType: ActionSubTypeType
    Region: str
    InstanceIds: List[str]

class IamActionDefinitionTypeDef(BaseModel):
    PolicyArn: str
    Roles: Optional[Sequence[str]] = None
    Groups: Optional[Sequence[str]] = None
    Users: Optional[Sequence[str]] = None

class ScpActionDefinitionTypeDef(BaseModel):
    PolicyId: str
    TargetIds: Sequence[str]

class SsmActionDefinitionTypeDef(BaseModel):
    ActionSubType: ActionSubTypeType
    Region: str
    InstanceIds: Sequence[str]

class DeleteBudgetActionRequestRequestTypeDef(BaseModel):
    AccountId: str
    BudgetName: str
    ActionId: str

class DeleteBudgetRequestRequestTypeDef(BaseModel):
    AccountId: str
    BudgetName: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeBudgetActionRequestRequestTypeDef(BaseModel):
    AccountId: str
    BudgetName: str
    ActionId: str

class DescribeBudgetActionsForAccountRequestRequestTypeDef(BaseModel):
    AccountId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeBudgetActionsForBudgetRequestRequestTypeDef(BaseModel):
    AccountId: str
    BudgetName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeBudgetNotificationsForAccountRequestRequestTypeDef(BaseModel):
    AccountId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeBudgetRequestRequestTypeDef(BaseModel):
    AccountId: str
    BudgetName: str

class DescribeBudgetsRequestRequestTypeDef(BaseModel):
    AccountId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeNotificationsForBudgetRequestRequestTypeDef(BaseModel):
    AccountId: str
    BudgetName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ExecuteBudgetActionRequestRequestTypeDef(BaseModel):
    AccountId: str
    BudgetName: str
    ActionId: str
    ExecutionType: ExecutionTypeType

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    ResourceTagKeys: Sequence[str]

class AutoAdjustDataExtraOutputTypeDef(BaseModel):
    AutoAdjustType: AutoAdjustTypeType
    HistoricalOptions: Optional[HistoricalOptionsTypeDef] = None
    LastAutoAdjustTime: Optional[datetime] = None

class AutoAdjustDataOutputTypeDef(BaseModel):
    AutoAdjustType: AutoAdjustTypeType
    HistoricalOptions: Optional[HistoricalOptionsTypeDef] = None
    LastAutoAdjustTime: Optional[datetime] = None

class AutoAdjustDataTypeDef(BaseModel):
    AutoAdjustType: AutoAdjustTypeType
    HistoricalOptions: Optional[HistoricalOptionsTypeDef] = None
    LastAutoAdjustTime: Optional[TimestampTypeDef] = None

class TimePeriodTypeDef(BaseModel):
    Start: Optional[TimestampTypeDef] = None
    End: Optional[TimestampTypeDef] = None

class CalculatedSpendTypeDef(BaseModel):
    ActualSpend: SpendTypeDef
    ForecastedSpend: Optional[SpendTypeDef] = None

class BudgetNotificationsForAccountTypeDef(BaseModel):
    Notifications: Optional[List[NotificationTypeDef]] = None
    BudgetName: Optional[str] = None

class CreateNotificationRequestRequestTypeDef(BaseModel):
    AccountId: str
    BudgetName: str
    Notification: NotificationTypeDef
    Subscribers: Sequence[SubscriberTypeDef]

class CreateSubscriberRequestRequestTypeDef(BaseModel):
    AccountId: str
    BudgetName: str
    Notification: NotificationTypeDef
    Subscriber: SubscriberTypeDef

class DeleteNotificationRequestRequestTypeDef(BaseModel):
    AccountId: str
    BudgetName: str
    Notification: NotificationTypeDef

class DeleteSubscriberRequestRequestTypeDef(BaseModel):
    AccountId: str
    BudgetName: str
    Notification: NotificationTypeDef
    Subscriber: SubscriberTypeDef

class DescribeSubscribersForNotificationRequestRequestTypeDef(BaseModel):
    AccountId: str
    BudgetName: str
    Notification: NotificationTypeDef
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class NotificationWithSubscribersTypeDef(BaseModel):
    Notification: NotificationTypeDef
    Subscribers: Sequence[SubscriberTypeDef]

class UpdateNotificationRequestRequestTypeDef(BaseModel):
    AccountId: str
    BudgetName: str
    OldNotification: NotificationTypeDef
    NewNotification: NotificationTypeDef

class UpdateSubscriberRequestRequestTypeDef(BaseModel):
    AccountId: str
    BudgetName: str
    Notification: NotificationTypeDef
    OldSubscriber: SubscriberTypeDef
    NewSubscriber: SubscriberTypeDef

class BudgetedAndActualAmountsTypeDef(BaseModel):
    BudgetedAmount: Optional[SpendTypeDef] = None
    ActualAmount: Optional[SpendTypeDef] = None
    TimePeriod: Optional[TimePeriodOutputTypeDef] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    ResourceTags: Sequence[ResourceTagTypeDef]

class CreateBudgetActionResponseTypeDef(BaseModel):
    AccountId: str
    BudgetName: str
    ActionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNotificationsForBudgetResponseTypeDef(BaseModel):
    Notifications: List[NotificationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeSubscribersForNotificationResponseTypeDef(BaseModel):
    Subscribers: List[SubscriberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ExecuteBudgetActionResponseTypeDef(BaseModel):
    AccountId: str
    BudgetName: str
    ActionId: str
    ExecutionType: ExecutionTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    ResourceTags: List[ResourceTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DefinitionExtraOutputTypeDef(BaseModel):
    IamActionDefinition: Optional[IamActionDefinitionExtraOutputTypeDef] = None
    ScpActionDefinition: Optional[ScpActionDefinitionExtraOutputTypeDef] = None
    SsmActionDefinition: Optional[SsmActionDefinitionExtraOutputTypeDef] = None

class DefinitionOutputTypeDef(BaseModel):
    IamActionDefinition: Optional[IamActionDefinitionOutputTypeDef] = None
    ScpActionDefinition: Optional[ScpActionDefinitionOutputTypeDef] = None
    SsmActionDefinition: Optional[SsmActionDefinitionOutputTypeDef] = None

class DefinitionTypeDef(BaseModel):
    IamActionDefinition: Optional[IamActionDefinitionTypeDef] = None
    ScpActionDefinition: Optional[ScpActionDefinitionTypeDef] = None
    SsmActionDefinition: Optional[SsmActionDefinitionTypeDef] = None

class DescribeBudgetActionsForAccountRequestDescribeBudgetActionsForAccountPaginateTypeDef(BaseModel):
    AccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeBudgetActionsForBudgetRequestDescribeBudgetActionsForBudgetPaginateTypeDef(BaseModel):
    AccountId: str
    BudgetName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeBudgetNotificationsForAccountRequestDescribeBudgetNotificationsForAccountPaginateTypeDef(BaseModel):
    AccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeBudgetsRequestDescribeBudgetsPaginateTypeDef(BaseModel):
    AccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeNotificationsForBudgetRequestDescribeNotificationsForBudgetPaginateTypeDef(BaseModel):
    AccountId: str
    BudgetName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSubscribersForNotificationRequestDescribeSubscribersForNotificationPaginateTypeDef(BaseModel):
    AccountId: str
    BudgetName: str
    Notification: NotificationTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeBudgetActionHistoriesRequestDescribeBudgetActionHistoriesPaginateTypeDef(BaseModel):
    AccountId: str
    BudgetName: str
    ActionId: str
    TimePeriod: Optional[TimePeriodTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeBudgetActionHistoriesRequestRequestTypeDef(BaseModel):
    AccountId: str
    BudgetName: str
    ActionId: str
    TimePeriod: Optional[TimePeriodTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeBudgetPerformanceHistoryRequestDescribeBudgetPerformanceHistoryPaginateTypeDef(BaseModel):
    AccountId: str
    BudgetName: str
    TimePeriod: Optional[TimePeriodTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeBudgetPerformanceHistoryRequestRequestTypeDef(BaseModel):
    AccountId: str
    BudgetName: str
    TimePeriod: Optional[TimePeriodTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class BudgetExtraOutputTypeDef(BaseModel):
    BudgetName: str
    TimeUnit: TimeUnitType
    BudgetType: BudgetTypeType
    BudgetLimit: Optional[SpendTypeDef] = None
    PlannedBudgetLimits: Optional[Dict[str, SpendTypeDef]] = None
    CostFilters: Optional[Dict[str, List[str]]] = None
    CostTypes: Optional[CostTypesTypeDef] = None
    TimePeriod: Optional[TimePeriodExtraOutputTypeDef] = None
    CalculatedSpend: Optional[CalculatedSpendTypeDef] = None
    LastUpdatedTime: Optional[datetime] = None
    AutoAdjustData: Optional[AutoAdjustDataExtraOutputTypeDef] = None

class BudgetOutputTypeDef(BaseModel):
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

class BudgetTypeDef(BaseModel):
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

class DescribeBudgetNotificationsForAccountResponseTypeDef(BaseModel):
    BudgetNotificationsForAccount: List[BudgetNotificationsForAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BudgetPerformanceHistoryTypeDef(BaseModel):
    BudgetName: Optional[str] = None
    BudgetType: Optional[BudgetTypeType] = None
    CostFilters: Optional[Dict[str, List[str]]] = None
    CostTypes: Optional[CostTypesTypeDef] = None
    TimeUnit: Optional[TimeUnitType] = None
    BudgetedAndActualAmountsList: Optional[List[BudgetedAndActualAmountsTypeDef]] = None

class ActionTypeDef(BaseModel):
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

class CreateBudgetActionRequestRequestTypeDef(BaseModel):
    AccountId: str
    BudgetName: str
    NotificationType: NotificationTypeType
    ActionType: ActionTypeType
    ActionThreshold: ActionThresholdTypeDef
    Definition: DefinitionTypeDef
    ExecutionRoleArn: str
    ApprovalModel: ApprovalModelType
    Subscribers: Sequence[SubscriberTypeDef]
    ResourceTags: Optional[Sequence[ResourceTagTypeDef]] = None

class UpdateBudgetActionRequestRequestTypeDef(BaseModel):
    AccountId: str
    BudgetName: str
    ActionId: str
    NotificationType: Optional[NotificationTypeType] = None
    ActionThreshold: Optional[ActionThresholdTypeDef] = None
    Definition: Optional[DefinitionTypeDef] = None
    ExecutionRoleArn: Optional[str] = None
    ApprovalModel: Optional[ApprovalModelType] = None
    Subscribers: Optional[Sequence[SubscriberTypeDef]] = None

class DescribeBudgetsResponseTypeDef(BaseModel):
    Budgets: List[BudgetExtraOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeBudgetResponseTypeDef(BaseModel):
    Budget: BudgetOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBudgetRequestRequestTypeDef(BaseModel):
    AccountId: str
    Budget: BudgetTypeDef
    NotificationsWithSubscribers: Optional[Sequence[NotificationWithSubscribersTypeDef]] = None
    ResourceTags: Optional[Sequence[ResourceTagTypeDef]] = None

class UpdateBudgetRequestRequestTypeDef(BaseModel):
    AccountId: str
    NewBudget: BudgetTypeDef

class DescribeBudgetPerformanceHistoryResponseTypeDef(BaseModel):
    BudgetPerformanceHistory: BudgetPerformanceHistoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ActionHistoryDetailsTypeDef(BaseModel):
    Message: str
    Action: ActionTypeDef

class DeleteBudgetActionResponseTypeDef(BaseModel):
    AccountId: str
    BudgetName: str
    Action: ActionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBudgetActionResponseTypeDef(BaseModel):
    AccountId: str
    BudgetName: str
    Action: ActionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBudgetActionsForAccountResponseTypeDef(BaseModel):
    Actions: List[ActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeBudgetActionsForBudgetResponseTypeDef(BaseModel):
    Actions: List[ActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateBudgetActionResponseTypeDef(BaseModel):
    AccountId: str
    BudgetName: str
    OldAction: ActionTypeDef
    NewAction: ActionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ActionHistoryTypeDef(BaseModel):
    Timestamp: datetime
    Status: ActionStatusType
    EventType: EventTypeType
    ActionHistoryDetails: ActionHistoryDetailsTypeDef

class DescribeBudgetActionHistoriesResponseTypeDef(BaseModel):
    ActionHistories: List[ActionHistoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

