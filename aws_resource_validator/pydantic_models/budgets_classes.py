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

class TimePeriodExtraOutputTypeDef(BaseValidatorModel):
    Start: Optional[datetime] = None
    End: Optional[datetime] = None

class NotificationTypeDef(BaseValidatorModel):
    NotificationType: NotificationTypeType
    ComparisonOperator: ComparisonOperatorType
    Threshold: float
    ThresholdType: Optional[ThresholdTypeType] = None
    NotificationState: Optional[NotificationStateType] = None

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

class IamActionDefinitionExtraOutputTypeDef(BaseValidatorModel):
    PolicyArn: str
    Roles: Optional[List[str]] = None
    Groups: Optional[List[str]] = None
    Users: Optional[List[str]] = None

class ScpActionDefinitionExtraOutputTypeDef(BaseValidatorModel):
    PolicyId: str
    TargetIds: List[str]

class SsmActionDefinitionExtraOutputTypeDef(BaseValidatorModel):
    ActionSubType: ActionSubTypeType
    Region: str
    InstanceIds: List[str]

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

class DeleteBudgetActionRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    ActionId: str

class DeleteBudgetRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeBudgetActionRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    ActionId: str

class DescribeBudgetActionsForAccountRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeBudgetActionsForBudgetRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeBudgetNotificationsForAccountRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeBudgetRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str

class DescribeBudgetsRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeNotificationsForBudgetRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ExecuteBudgetActionRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    ActionId: str
    ExecutionType: ExecutionTypeType

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    ResourceTagKeys: Sequence[str]

class AutoAdjustDataExtraOutputTypeDef(BaseValidatorModel):
    AutoAdjustType: AutoAdjustTypeType
    HistoricalOptions: Optional[HistoricalOptionsTypeDef] = None
    LastAutoAdjustTime: Optional[datetime] = None

class AutoAdjustDataOutputTypeDef(BaseValidatorModel):
    AutoAdjustType: AutoAdjustTypeType
    HistoricalOptions: Optional[HistoricalOptionsTypeDef] = None
    LastAutoAdjustTime: Optional[datetime] = None

class AutoAdjustDataTypeDef(BaseValidatorModel):
    AutoAdjustType: AutoAdjustTypeType
    HistoricalOptions: Optional[HistoricalOptionsTypeDef] = None
    LastAutoAdjustTime: Optional[TimestampTypeDef] = None

class TimePeriodTypeDef(BaseValidatorModel):
    Start: Optional[TimestampTypeDef] = None
    End: Optional[TimestampTypeDef] = None

class CalculatedSpendTypeDef(BaseValidatorModel):
    ActualSpend: SpendTypeDef
    ForecastedSpend: Optional[SpendTypeDef] = None

class BudgetNotificationsForAccountTypeDef(BaseValidatorModel):
    Notifications: Optional[List[NotificationTypeDef]] = None
    BudgetName: Optional[str] = None

class CreateNotificationRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    Notification: NotificationTypeDef
    Subscribers: Sequence[SubscriberTypeDef]

class CreateSubscriberRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    Notification: NotificationTypeDef
    Subscriber: SubscriberTypeDef

class DeleteNotificationRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    Notification: NotificationTypeDef

class DeleteSubscriberRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    Notification: NotificationTypeDef
    Subscriber: SubscriberTypeDef

class DescribeSubscribersForNotificationRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    Notification: NotificationTypeDef
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class NotificationWithSubscribersTypeDef(BaseValidatorModel):
    Notification: NotificationTypeDef
    Subscribers: Sequence[SubscriberTypeDef]

class UpdateNotificationRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    OldNotification: NotificationTypeDef
    NewNotification: NotificationTypeDef

class UpdateSubscriberRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    Notification: NotificationTypeDef
    OldSubscriber: SubscriberTypeDef
    NewSubscriber: SubscriberTypeDef

class BudgetedAndActualAmountsTypeDef(BaseValidatorModel):
    BudgetedAmount: Optional[SpendTypeDef] = None
    ActualAmount: Optional[SpendTypeDef] = None
    TimePeriod: Optional[TimePeriodOutputTypeDef] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
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

class DefinitionExtraOutputTypeDef(BaseValidatorModel):
    IamActionDefinition: Optional[IamActionDefinitionExtraOutputTypeDef] = None
    ScpActionDefinition: Optional[ScpActionDefinitionExtraOutputTypeDef] = None
    SsmActionDefinition: Optional[SsmActionDefinitionExtraOutputTypeDef] = None

class DefinitionOutputTypeDef(BaseValidatorModel):
    IamActionDefinition: Optional[IamActionDefinitionOutputTypeDef] = None
    ScpActionDefinition: Optional[ScpActionDefinitionOutputTypeDef] = None
    SsmActionDefinition: Optional[SsmActionDefinitionOutputTypeDef] = None

class DefinitionTypeDef(BaseValidatorModel):
    IamActionDefinition: Optional[IamActionDefinitionTypeDef] = None
    ScpActionDefinition: Optional[ScpActionDefinitionTypeDef] = None
    SsmActionDefinition: Optional[SsmActionDefinitionTypeDef] = None

class DescribeBudgetActionsForAccountRequestDescribeBudgetActionsForAccountPaginateTypeDef(BaseValidatorModel):
    AccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeBudgetActionsForBudgetRequestDescribeBudgetActionsForBudgetPaginateTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeBudgetNotificationsForAccountRequestDescribeBudgetNotificationsForAccountPaginateTypeDef(BaseValidatorModel):
    AccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeBudgetsRequestDescribeBudgetsPaginateTypeDef(BaseValidatorModel):
    AccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeNotificationsForBudgetRequestDescribeNotificationsForBudgetPaginateTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSubscribersForNotificationRequestDescribeSubscribersForNotificationPaginateTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    Notification: NotificationTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeBudgetActionHistoriesRequestDescribeBudgetActionHistoriesPaginateTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    ActionId: str
    TimePeriod: Optional[TimePeriodTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeBudgetActionHistoriesRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    ActionId: str
    TimePeriod: Optional[TimePeriodTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeBudgetPerformanceHistoryRequestDescribeBudgetPerformanceHistoryPaginateTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    TimePeriod: Optional[TimePeriodTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeBudgetPerformanceHistoryRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    TimePeriod: Optional[TimePeriodTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class BudgetExtraOutputTypeDef(BaseValidatorModel):
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

class DescribeBudgetNotificationsForAccountResponseTypeDef(BaseValidatorModel):
    BudgetNotificationsForAccount: List[BudgetNotificationsForAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

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

class CreateBudgetActionRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateBudgetActionRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BudgetName: str
    ActionId: str
    NotificationType: Optional[NotificationTypeType] = None
    ActionThreshold: Optional[ActionThresholdTypeDef] = None
    Definition: Optional[DefinitionTypeDef] = None
    ExecutionRoleArn: Optional[str] = None
    ApprovalModel: Optional[ApprovalModelType] = None
    Subscribers: Optional[Sequence[SubscriberTypeDef]] = None

class DescribeBudgetsResponseTypeDef(BaseValidatorModel):
    Budgets: List[BudgetExtraOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeBudgetResponseTypeDef(BaseValidatorModel):
    Budget: BudgetOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBudgetRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Budget: BudgetTypeDef
    NotificationsWithSubscribers: Optional[Sequence[NotificationWithSubscribersTypeDef]] = None
    ResourceTags: Optional[Sequence[ResourceTagTypeDef]] = None

class UpdateBudgetRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    NewBudget: BudgetTypeDef

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

class ActionHistoryTypeDef(BaseValidatorModel):
    Timestamp: datetime
    Status: ActionStatusType
    EventType: EventTypeType
    ActionHistoryDetails: ActionHistoryDetailsTypeDef

class DescribeBudgetActionHistoriesResponseTypeDef(BaseValidatorModel):
    ActionHistories: List[ActionHistoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

