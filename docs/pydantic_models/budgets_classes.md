# Budgets Classes

# Action

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
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ActionThreshold'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.DefinitionOutput'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.budgets_classes.Subscriber]
- **Required**: Yes


# ActionHistory

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
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ActionHistoryDetails'>
- **Required**: Yes


# ActionHistoryDetails

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.Action'>
- **Required**: Yes


# ActionThreshold

### ActionThresholdValue
- **Type**: <class 'float'>
- **Required**: Yes

### ActionThresholdType
- **Type**: typing.Literal['ABSOLUTE_VALUE', 'PERCENTAGE']
- **Required**: Yes


# AutoAdjustData

### AutoAdjustType
- **Type**: typing.Literal['FORECAST', 'HISTORICAL']
- **Required**: Yes

### HistoricalOptions
- **Type**: <class 'NoneType'>

### LastAutoAdjustTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.Timestamp]


# AutoAdjustDataOutput

### AutoAdjustType
- **Type**: typing.Literal['FORECAST', 'HISTORICAL']
- **Required**: Yes

### HistoricalOptions
- **Type**: <class 'NoneType'>

### LastAutoAdjustTime
- **Type**: typing.Optional[datetime.datetime]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Budget

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.Spend]

### PlannedBudgetLimits
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.budgets_classes.Spend]]

### CostFilters
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### CostTypes
- **Type**: <class 'NoneType'>

### TimePeriod
- **Type**: <class 'NoneType'>

### CalculatedSpend
- **Type**: <class 'NoneType'>

### LastUpdatedTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.Timestamp]

### AutoAdjustData
- **Type**: <class 'NoneType'>


# BudgetNotificationsForAccount

### Notifications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.budgets_classes.Notification]]

### BudgetName
- **Type**: typing.Optional[str]


# BudgetOutput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.Spend]

### PlannedBudgetLimits
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.budgets_classes.Spend]]

### CostFilters
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### CostTypes
- **Type**: <class 'NoneType'>

### TimePeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.TimePeriodOutput]

### CalculatedSpend
- **Type**: <class 'NoneType'>

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### AutoAdjustData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.AutoAdjustDataOutput]


# BudgetPerformanceHistory

### BudgetName
- **Type**: typing.Optional[str]

### BudgetType
- **Type**: typing.Optional[typing.Literal['COST', 'RI_COVERAGE', 'RI_UTILIZATION', 'SAVINGS_PLANS_COVERAGE', 'SAVINGS_PLANS_UTILIZATION', 'USAGE']]

### CostFilters
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### CostTypes
- **Type**: <class 'NoneType'>

### TimeUnit
- **Type**: typing.Optional[typing.Literal['ANNUALLY', 'DAILY', 'MONTHLY', 'QUARTERLY']]

### BudgetedAndActualAmountsList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.budgets_classes.BudgetedAndActualAmounts]]


# BudgetUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BudgetedAndActualAmounts

### BudgetedAmount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.Spend]

### ActualAmount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.Spend]

### TimePeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.TimePeriodOutput]


# CalculatedSpend

### ActualSpend
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.Spend'>
- **Required**: Yes

### ForecastedSpend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.Spend]


# CostTypes

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


# CreateBudgetActionRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ActionThreshold'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.DefinitionUnion'>
- **Required**: Yes

### ExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ApprovalModel
- **Type**: typing.Literal['AUTOMATIC', 'MANUAL']
- **Required**: Yes

### Subscribers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.budgets_classes.Subscriber]
- **Required**: Yes

### ResourceTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.budgets_classes.ResourceTag]]


# CreateBudgetActionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ResponseMetadata'>
- **Required**: Yes


# CreateBudgetRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Budget
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.BudgetUnion'>
- **Required**: Yes

### NotificationsWithSubscribers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.budgets_classes.NotificationWithSubscribers]]

### ResourceTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.budgets_classes.ResourceTag]]


# CreateNotificationRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### Notification
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.Notification'>
- **Required**: Yes

### Subscribers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.budgets_classes.Subscriber]
- **Required**: Yes


# CreateSubscriberRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### Notification
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.Notification'>
- **Required**: Yes

### Subscriber
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.Subscriber'>
- **Required**: Yes


# Definition

### IamActionDefinition
- **Type**: <class 'NoneType'>

### ScpActionDefinition
- **Type**: <class 'NoneType'>

### SsmActionDefinition
- **Type**: <class 'NoneType'>


# DefinitionOutput

### IamActionDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.IamActionDefinitionOutput]

### ScpActionDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.ScpActionDefinitionOutput]

### SsmActionDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.SsmActionDefinitionOutput]


# DefinitionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteBudgetActionRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### ActionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBudgetActionResponse

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.Action'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteBudgetRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNotificationRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### Notification
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.Notification'>
- **Required**: Yes


# DeleteSubscriberRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### Notification
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.Notification'>
- **Required**: Yes

### Subscriber
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.Subscriber'>
- **Required**: Yes


# DescribeBudgetActionHistoriesRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.TimePeriodUnion]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeBudgetActionHistoriesRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.TimePeriodUnion]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.PaginatorConfig]


# DescribeBudgetActionHistoriesResponse

### ActionHistories
- **Type**: typing.List[aws_resource_validator.pydantic_models.budgets_classes.ActionHistory]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeBudgetActionRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### ActionId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBudgetActionResponse

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.Action'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeBudgetActionsForAccountRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeBudgetActionsForAccountRequestPaginate

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.PaginatorConfig]


# DescribeBudgetActionsForAccountResponse

### Actions
- **Type**: typing.List[aws_resource_validator.pydantic_models.budgets_classes.Action]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeBudgetActionsForBudgetRequest

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


# DescribeBudgetActionsForBudgetRequestPaginate

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.PaginatorConfig]


# DescribeBudgetActionsForBudgetResponse

### Actions
- **Type**: typing.List[aws_resource_validator.pydantic_models.budgets_classes.Action]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeBudgetNotificationsForAccountRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeBudgetNotificationsForAccountRequestPaginate

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.PaginatorConfig]


# DescribeBudgetNotificationsForAccountResponse

### BudgetNotificationsForAccount
- **Type**: typing.List[aws_resource_validator.pydantic_models.budgets_classes.BudgetNotificationsForAccount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeBudgetPerformanceHistoryRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### TimePeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.TimePeriodUnion]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeBudgetPerformanceHistoryRequestPaginate

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### TimePeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.TimePeriodUnion]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.PaginatorConfig]


# DescribeBudgetPerformanceHistoryResponse

### BudgetPerformanceHistory
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.BudgetPerformanceHistory'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeBudgetRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBudgetResponse

### Budget
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.BudgetOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeBudgetsRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeBudgetsRequestPaginate

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.PaginatorConfig]


# DescribeBudgetsResponse

### Budgets
- **Type**: typing.List[aws_resource_validator.pydantic_models.budgets_classes.BudgetOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeNotificationsForBudgetRequest

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


# DescribeNotificationsForBudgetRequestPaginate

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.PaginatorConfig]


# DescribeNotificationsForBudgetResponse

### Notifications
- **Type**: typing.List[aws_resource_validator.pydantic_models.budgets_classes.Notification]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeSubscribersForNotificationRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### Notification
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.Notification'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeSubscribersForNotificationRequestPaginate

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### Notification
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.Notification'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.PaginatorConfig]


# DescribeSubscribersForNotificationResponse

### Subscribers
- **Type**: typing.List[aws_resource_validator.pydantic_models.budgets_classes.Subscriber]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ExecuteBudgetActionRequest

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


# ExecuteBudgetActionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ResponseMetadata'>
- **Required**: Yes


# HistoricalOptions

### BudgetAdjustmentPeriod
- **Type**: <class 'int'>
- **Required**: Yes

### LookBackAvailablePeriods
- **Type**: typing.Optional[int]


# IamActionDefinition

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### Roles
- **Type**: typing.Optional[typing.Sequence[str]]

### Groups
- **Type**: typing.Optional[typing.Sequence[str]]

### Users
- **Type**: typing.Optional[typing.Sequence[str]]


# IamActionDefinitionOutput

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### Roles
- **Type**: typing.Optional[typing.List[str]]

### Groups
- **Type**: typing.Optional[typing.List[str]]

### Users
- **Type**: typing.Optional[typing.List[str]]


# ListTagsForResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### ResourceTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.budgets_classes.ResourceTag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ResponseMetadata'>
- **Required**: Yes


# Notification

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


# NotificationWithSubscribers

### Notification
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.Notification'>
- **Required**: Yes

### Subscribers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.budgets_classes.Subscriber]
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ResourceTag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


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


# ScpActionDefinition

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ScpActionDefinitionOutput

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetIds
- **Type**: typing.List[str]
- **Required**: Yes


# Spend

### Amount
- **Type**: <class 'str'>
- **Required**: Yes

### Unit
- **Type**: <class 'str'>
- **Required**: Yes


# SsmActionDefinition

### ActionSubType
- **Type**: typing.Literal['STOP_EC2_INSTANCES', 'STOP_RDS_INSTANCES']
- **Required**: Yes

### Region
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# SsmActionDefinitionOutput

### ActionSubType
- **Type**: typing.Literal['STOP_EC2_INSTANCES', 'STOP_RDS_INSTANCES']
- **Required**: Yes

### Region
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceIds
- **Type**: typing.List[str]
- **Required**: Yes


# Subscriber

### SubscriptionType
- **Type**: typing.Literal['EMAIL', 'SNS']
- **Required**: Yes

### Address
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.budgets_classes.ResourceTag]
- **Required**: Yes


# TimePeriod

### Start
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.Timestamp]

### End
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.Timestamp]


# TimePeriodOutput

### Start
- **Type**: typing.Optional[datetime.datetime]

### End
- **Type**: typing.Optional[datetime.datetime]


# TimePeriodUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateBudgetActionRequest

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
- **Type**: <class 'NoneType'>

### Definition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.budgets_classes.DefinitionUnion]

### ExecutionRoleArn
- **Type**: typing.Optional[str]

### ApprovalModel
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'MANUAL']]

### Subscribers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.budgets_classes.Subscriber]]


# UpdateBudgetActionResponse

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### OldAction
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.Action'>
- **Required**: Yes

### NewAction
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.Action'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateBudgetRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NewBudget
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.BudgetUnion'>
- **Required**: Yes


# UpdateNotificationRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### OldNotification
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.Notification'>
- **Required**: Yes

### NewNotification
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.Notification'>
- **Required**: Yes


# UpdateSubscriberRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### Notification
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.Notification'>
- **Required**: Yes

### OldSubscriber
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.Subscriber'>
- **Required**: Yes

### NewSubscriber
- **Type**: <class 'aws_resource_validator.pydantic_models.budgets_classes.Subscriber'>
- **Required**: Yes


