# Budgets Classes

# ActionHistoryDetailsTypeDef

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ActionTypeDef'>
- **Required**: Yes


# ActionHistoryTypeDef

### Timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['EXECUTION_FAILURE', 'EXECUTION_IN_PROGRESS', 'EXECUTION_SUCCESS', 'PENDING', 'RESET_FAILURE', 'RESET_IN_PROGRESS', 'REVERSE_FAILURE', 'REVERSE_IN_PROGRESS', 'REVERSE_SUCCESS', 'STANDBY']
- **Required**: Yes

### EventType
- **Type**: typing.Literal['CREATE_ACTION', 'DELETE_ACTION', 'EXECUTE_ACTION', 'SYSTEM', 'UPDATE_ACTION']
- **Required**: Yes

### ActionHistoryDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ActionHistoryDetailsTypeDef'>
- **Required**: Yes


# ActionThresholdTypeDef

### ActionThresholdValue
- **Type**: <class 'float'>
- **Required**: Yes

### ActionThresholdType
- **Type**: typing.Literal['ABSOLUTE_VALUE', 'PERCENTAGE']
- **Required**: Yes


# ActionTypeDef

### ActionId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### NotificationType
- **Type**: typing.Literal['ACTUAL', 'FORECASTED']
- **Required**: Yes

### ActionType
- **Type**: typing.Literal['APPLY_IAM_POLICY', 'APPLY_SCP_POLICY', 'RUN_SSM_DOCUMENTS']
- **Required**: Yes

### ActionThreshold
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ActionThresholdTypeDef'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.DefinitionOutputTypeDef'>
- **Required**: Yes

### ExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ApprovalModel
- **Type**: typing.Literal['AUTOMATIC', 'MANUAL']
- **Required**: Yes

### Status
- **Type**: typing.Literal['EXECUTION_FAILURE', 'EXECUTION_IN_PROGRESS', 'EXECUTION_SUCCESS', 'PENDING', 'RESET_FAILURE', 'RESET_IN_PROGRESS', 'REVERSE_FAILURE', 'REVERSE_IN_PROGRESS', 'REVERSE_SUCCESS', 'STANDBY']
- **Required**: Yes

### Subscribers
- **Type**: typing.List[aws_resource_validator.pydantic_models.budgets_classes.SubscriberTypeDef]
- **Required**: Yes


# AutoAdjustDataExtraOutputTypeDef

### AutoAdjustType
- **Type**: typing.Literal['FORECAST', 'HISTORICAL']
- **Required**: Yes

### HistoricalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.HistoricalOptionsTypeDef]

### LastAutoAdjustTime
- **Type**: typing.Optional[datetime.datetime]


# AutoAdjustDataOutputTypeDef

### AutoAdjustType
- **Type**: typing.Literal['FORECAST', 'HISTORICAL']
- **Required**: Yes

### HistoricalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.HistoricalOptionsTypeDef]

### LastAutoAdjustTime
- **Type**: typing.Optional[datetime.datetime]


# AutoAdjustDataTypeDef

### AutoAdjustType
- **Type**: typing.Literal['FORECAST', 'HISTORICAL']
- **Required**: Yes

### HistoricalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.HistoricalOptionsTypeDef]

### LastAutoAdjustTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BudgetExtraOutputTypeDef

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### TimeUnit
- **Type**: typing.Literal['ANNUALLY', 'DAILY', 'MONTHLY', 'QUARTERLY']
- **Required**: Yes

### BudgetType
- **Type**: typing.Literal['COST', 'RI_COVERAGE', 'RI_UTILIZATION', 'SAVINGS_PLANS_COVERAGE', 'SAVINGS_PLANS_UTILIZATION', 'USAGE']
- **Required**: Yes

### BudgetLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.SpendTypeDef]

### PlannedBudgetLimits
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.budgets_classes.SpendTypeDef]]

### CostFilters
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### CostTypes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.CostTypesTypeDef]

### TimePeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.TimePeriodExtraOutputTypeDef]

### CalculatedSpend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.CalculatedSpendTypeDef]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### AutoAdjustData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.AutoAdjustDataExtraOutputTypeDef]


# BudgetNotificationsForAccountTypeDef

### Notifications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.budgets_classes.NotificationTypeDef]]

### BudgetName
- **Type**: typing.Optional[str]


# BudgetOutputTypeDef

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### TimeUnit
- **Type**: typing.Literal['ANNUALLY', 'DAILY', 'MONTHLY', 'QUARTERLY']
- **Required**: Yes

### BudgetType
- **Type**: typing.Literal['COST', 'RI_COVERAGE', 'RI_UTILIZATION', 'SAVINGS_PLANS_COVERAGE', 'SAVINGS_PLANS_UTILIZATION', 'USAGE']
- **Required**: Yes

### BudgetLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.SpendTypeDef]

### PlannedBudgetLimits
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.budgets_classes.SpendTypeDef]]

### CostFilters
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### CostTypes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.CostTypesTypeDef]

### TimePeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.TimePeriodOutputTypeDef]

### CalculatedSpend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.CalculatedSpendTypeDef]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### AutoAdjustData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.AutoAdjustDataOutputTypeDef]


# BudgetPerformanceHistoryTypeDef

### BudgetName
- **Type**: typing.Optional[str]

### BudgetType
- **Type**: typing.Optional[typing.Literal['COST', 'RI_COVERAGE', 'RI_UTILIZATION', 'SAVINGS_PLANS_COVERAGE', 'SAVINGS_PLANS_UTILIZATION', 'USAGE']]

### CostFilters
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### CostTypes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.CostTypesTypeDef]

### TimeUnit
- **Type**: typing.Optional[typing.Literal['ANNUALLY', 'DAILY', 'MONTHLY', 'QUARTERLY']]

### BudgetedAndActualAmountsList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.budgets_classes.BudgetedAndActualAmountsTypeDef]]


# BudgetTypeDef

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### TimeUnit
- **Type**: typing.Literal['ANNUALLY', 'DAILY', 'MONTHLY', 'QUARTERLY']
- **Required**: Yes

### BudgetType
- **Type**: typing.Literal['COST', 'RI_COVERAGE', 'RI_UTILIZATION', 'SAVINGS_PLANS_COVERAGE', 'SAVINGS_PLANS_UTILIZATION', 'USAGE']
- **Required**: Yes

### BudgetLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.SpendTypeDef]

### PlannedBudgetLimits
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.budgets_classes.SpendTypeDef]]

### CostFilters
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### CostTypes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.CostTypesTypeDef]

### TimePeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.TimePeriodTypeDef]

### CalculatedSpend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.CalculatedSpendTypeDef]

### LastUpdatedTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### AutoAdjustData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.AutoAdjustDataTypeDef]


# BudgetedAndActualAmountsTypeDef

### BudgetedAmount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.SpendTypeDef]

### ActualAmount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.SpendTypeDef]

### TimePeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.TimePeriodOutputTypeDef]


# CalculatedSpendTypeDef

### ActualSpend
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.SpendTypeDef'>
- **Required**: Yes

### ForecastedSpend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.SpendTypeDef]


# CostTypesTypeDef

### IncludeTax
- **Type**: typing.Optional[bool]

### IncludeSubscription
- **Type**: typing.Optional[bool]

### UseBlended
- **Type**: typing.Optional[bool]

### IncludeRefund
- **Type**: typing.Optional[bool]

### IncludeCredit
- **Type**: typing.Optional[bool]

### IncludeUpfront
- **Type**: typing.Optional[bool]

### IncludeRecurring
- **Type**: typing.Optional[bool]

### IncludeOtherSubscription
- **Type**: typing.Optional[bool]

### IncludeSupport
- **Type**: typing.Optional[bool]

### IncludeDiscount
- **Type**: typing.Optional[bool]

### UseAmortized
- **Type**: typing.Optional[bool]


# CreateBudgetActionRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### NotificationType
- **Type**: typing.Literal['ACTUAL', 'FORECASTED']
- **Required**: Yes

### ActionType
- **Type**: typing.Literal['APPLY_IAM_POLICY', 'APPLY_SCP_POLICY', 'RUN_SSM_DOCUMENTS']
- **Required**: Yes

### ActionThreshold
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ActionThresholdTypeDef'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.DefinitionTypeDef'>
- **Required**: Yes

### ExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ApprovalModel
- **Type**: typing.Literal['AUTOMATIC', 'MANUAL']
- **Required**: Yes

### Subscribers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.budgets_classes.SubscriberTypeDef]
- **Required**: Yes

### ResourceTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.budgets_classes.ResourceTagTypeDef]]


# CreateBudgetActionResponseTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### ActionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateBudgetRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Budget
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.BudgetTypeDef'>
- **Required**: Yes

### NotificationsWithSubscribers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.budgets_classes.NotificationWithSubscribersTypeDef]]

### ResourceTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.budgets_classes.ResourceTagTypeDef]]


# CreateNotificationRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### Notification
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.NotificationTypeDef'>
- **Required**: Yes

### Subscribers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.budgets_classes.SubscriberTypeDef]
- **Required**: Yes


# CreateSubscriberRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### Notification
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.NotificationTypeDef'>
- **Required**: Yes

### Subscriber
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.SubscriberTypeDef'>
- **Required**: Yes


# DefinitionExtraOutputTypeDef

### IamActionDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.IamActionDefinitionExtraOutputTypeDef]

### ScpActionDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.ScpActionDefinitionExtraOutputTypeDef]

### SsmActionDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.SsmActionDefinitionExtraOutputTypeDef]


# DefinitionOutputTypeDef

### IamActionDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.IamActionDefinitionOutputTypeDef]

### ScpActionDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.ScpActionDefinitionOutputTypeDef]

### SsmActionDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.SsmActionDefinitionOutputTypeDef]


# DefinitionTypeDef

### IamActionDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.IamActionDefinitionTypeDef]

### ScpActionDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.ScpActionDefinitionTypeDef]

### SsmActionDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.SsmActionDefinitionTypeDef]


# DeleteBudgetActionRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### ActionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBudgetActionResponseTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ActionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteBudgetRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNotificationRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### Notification
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.NotificationTypeDef'>
- **Required**: Yes


# DeleteSubscriberRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### Notification
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.NotificationTypeDef'>
- **Required**: Yes

### Subscriber
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.SubscriberTypeDef'>
- **Required**: Yes


# DescribeBudgetActionHistoriesRequestDescribeBudgetActionHistoriesPaginateTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### ActionId
- **Type**: <class 'str'>
- **Required**: Yes

### TimePeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.TimePeriodTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.PaginatorConfigTypeDef]


# DescribeBudgetActionHistoriesRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### ActionId
- **Type**: <class 'str'>
- **Required**: Yes

### TimePeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.TimePeriodTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeBudgetActionHistoriesResponseTypeDef

### ActionHistories
- **Type**: typing.List[aws_resource_validator.pydantic_models.budgets_classes.ActionHistoryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeBudgetActionRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### ActionId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBudgetActionResponseTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ActionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeBudgetActionsForAccountRequestDescribeBudgetActionsForAccountPaginateTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.PaginatorConfigTypeDef]


# DescribeBudgetActionsForAccountRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeBudgetActionsForAccountResponseTypeDef

### Actions
- **Type**: typing.List[aws_resource_validator.pydantic_models.budgets_classes.ActionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeBudgetActionsForBudgetRequestDescribeBudgetActionsForBudgetPaginateTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.PaginatorConfigTypeDef]


# DescribeBudgetActionsForBudgetRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeBudgetActionsForBudgetResponseTypeDef

### Actions
- **Type**: typing.List[aws_resource_validator.pydantic_models.budgets_classes.ActionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeBudgetNotificationsForAccountRequestDescribeBudgetNotificationsForAccountPaginateTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.PaginatorConfigTypeDef]


# DescribeBudgetNotificationsForAccountRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeBudgetNotificationsForAccountResponseTypeDef

### BudgetNotificationsForAccount
- **Type**: typing.List[aws_resource_validator.pydantic_models.budgets_classes.BudgetNotificationsForAccountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeBudgetPerformanceHistoryRequestDescribeBudgetPerformanceHistoryPaginateTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### TimePeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.TimePeriodTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.PaginatorConfigTypeDef]


# DescribeBudgetPerformanceHistoryRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### TimePeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.TimePeriodTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeBudgetPerformanceHistoryResponseTypeDef

### BudgetPerformanceHistory
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.BudgetPerformanceHistoryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeBudgetRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBudgetResponseTypeDef

### Budget
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.BudgetOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeBudgetsRequestDescribeBudgetsPaginateTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.PaginatorConfigTypeDef]


# DescribeBudgetsRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeBudgetsResponseTypeDef

### Budgets
- **Type**: typing.List[aws_resource_validator.pydantic_models.budgets_classes.BudgetExtraOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeNotificationsForBudgetRequestDescribeNotificationsForBudgetPaginateTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.PaginatorConfigTypeDef]


# DescribeNotificationsForBudgetRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeNotificationsForBudgetResponseTypeDef

### Notifications
- **Type**: typing.List[aws_resource_validator.pydantic_models.budgets_classes.NotificationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeSubscribersForNotificationRequestDescribeSubscribersForNotificationPaginateTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### Notification
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.NotificationTypeDef'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.PaginatorConfigTypeDef]


# DescribeSubscribersForNotificationRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### Notification
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.NotificationTypeDef'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeSubscribersForNotificationResponseTypeDef

### Subscribers
- **Type**: typing.List[aws_resource_validator.pydantic_models.budgets_classes.SubscriberTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ExecuteBudgetActionRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### ActionId
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionType
- **Type**: typing.Literal['APPROVE_BUDGET_ACTION', 'RESET_BUDGET_ACTION', 'RETRY_BUDGET_ACTION', 'REVERSE_BUDGET_ACTION']
- **Required**: Yes


# ExecuteBudgetActionResponseTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### ActionId
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionType
- **Type**: typing.Literal['APPROVE_BUDGET_ACTION', 'RESET_BUDGET_ACTION', 'RETRY_BUDGET_ACTION', 'REVERSE_BUDGET_ACTION']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HistoricalOptionsTypeDef

### BudgetAdjustmentPeriod
- **Type**: <class 'int'>
- **Required**: Yes

### LookBackAvailablePeriods
- **Type**: typing.Optional[int]


# IamActionDefinitionExtraOutputTypeDef

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### Roles
- **Type**: typing.Optional[typing.List[str]]

### Groups
- **Type**: typing.Optional[typing.List[str]]

### Users
- **Type**: typing.Optional[typing.List[str]]


# IamActionDefinitionOutputTypeDef

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### Roles
- **Type**: typing.Optional[typing.List[str]]

### Groups
- **Type**: typing.Optional[typing.List[str]]

### Users
- **Type**: typing.Optional[typing.List[str]]


# IamActionDefinitionTypeDef

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### Roles
- **Type**: typing.Optional[typing.Sequence[str]]

### Groups
- **Type**: typing.Optional[typing.Sequence[str]]

### Users
- **Type**: typing.Optional[typing.Sequence[str]]


# ListTagsForResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### ResourceTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.budgets_classes.ResourceTagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# NotificationTypeDef

### NotificationType
- **Type**: typing.Literal['ACTUAL', 'FORECASTED']
- **Required**: Yes

### ComparisonOperator
- **Type**: typing.Literal['EQUAL_TO', 'GREATER_THAN', 'LESS_THAN']
- **Required**: Yes

### Threshold
- **Type**: <class 'float'>
- **Required**: Yes

### ThresholdType
- **Type**: typing.Optional[typing.Literal['ABSOLUTE_VALUE', 'PERCENTAGE']]

### NotificationState
- **Type**: typing.Optional[typing.Literal['ALARM', 'OK']]


# NotificationWithSubscribersTypeDef

### Notification
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.NotificationTypeDef'>
- **Required**: Yes

### Subscribers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.budgets_classes.SubscriberTypeDef]
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ResourceTagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


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


# ScpActionDefinitionExtraOutputTypeDef

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetIds
- **Type**: typing.List[str]
- **Required**: Yes


# ScpActionDefinitionOutputTypeDef

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetIds
- **Type**: typing.List[str]
- **Required**: Yes


# ScpActionDefinitionTypeDef

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# SpendTypeDef

### Amount
- **Type**: <class 'str'>
- **Required**: Yes

### Unit
- **Type**: <class 'str'>
- **Required**: Yes


# SsmActionDefinitionExtraOutputTypeDef

### ActionSubType
- **Type**: typing.Literal['STOP_EC2_INSTANCES', 'STOP_RDS_INSTANCES']
- **Required**: Yes

### Region
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceIds
- **Type**: typing.List[str]
- **Required**: Yes


# SsmActionDefinitionOutputTypeDef

### ActionSubType
- **Type**: typing.Literal['STOP_EC2_INSTANCES', 'STOP_RDS_INSTANCES']
- **Required**: Yes

### Region
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceIds
- **Type**: typing.List[str]
- **Required**: Yes


# SsmActionDefinitionTypeDef

### ActionSubType
- **Type**: typing.Literal['STOP_EC2_INSTANCES', 'STOP_RDS_INSTANCES']
- **Required**: Yes

### Region
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# SubscriberTypeDef

### SubscriptionType
- **Type**: typing.Literal['EMAIL', 'SNS']
- **Required**: Yes

### Address
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.budgets_classes.ResourceTagTypeDef]
- **Required**: Yes


# TimePeriodExtraOutputTypeDef

### Start
- **Type**: typing.Optional[datetime.datetime]

### End
- **Type**: typing.Optional[datetime.datetime]


# TimePeriodOutputTypeDef

### Start
- **Type**: typing.Optional[datetime.datetime]

### End
- **Type**: typing.Optional[datetime.datetime]


# TimePeriodTypeDef

### Start
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### End
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# UntagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateBudgetActionRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### ActionId
- **Type**: <class 'str'>
- **Required**: Yes

### NotificationType
- **Type**: typing.Optional[typing.Literal['ACTUAL', 'FORECASTED']]

### ActionThreshold
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.ActionThresholdTypeDef]

### Definition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.DefinitionTypeDef]

### ExecutionRoleArn
- **Type**: typing.Optional[str]

### ApprovalModel
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'MANUAL']]

### Subscribers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.budgets_classes.SubscriberTypeDef]]


# UpdateBudgetActionResponseTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### OldAction
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ActionTypeDef'>
- **Required**: Yes

### NewAction
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ActionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateBudgetRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NewBudget
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.BudgetTypeDef'>
- **Required**: Yes


# UpdateNotificationRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### OldNotification
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.NotificationTypeDef'>
- **Required**: Yes

### NewNotification
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.NotificationTypeDef'>
- **Required**: Yes


# UpdateSubscriberRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### Notification
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.NotificationTypeDef'>
- **Required**: Yes

### OldSubscriber
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.SubscriberTypeDef'>
- **Required**: Yes

### NewSubscriber
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.SubscriberTypeDef'>
- **Required**: Yes


