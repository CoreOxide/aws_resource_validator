# Bcm Pricing Calculator Classes

# AddReservedInstanceAction

### reservedInstancesOfferingId
- **Type**: typing.Optional[str]

### instanceCount
- **Type**: typing.Optional[int]


# AddSavingsPlanAction

### savingsPlanOfferingId
- **Type**: typing.Optional[str]

### commitment
- **Type**: typing.Optional[float]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchCreateBillScenarioCommitmentModificationEntry

### key
- **Type**: <class 'str'>
- **Required**: Yes

### usageAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### commitmentAction
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BillScenarioCommitmentModificationAction'>
- **Required**: Yes

### group
- **Type**: typing.Optional[str]


# BatchCreateBillScenarioCommitmentModificationError

### key
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[typing.Literal['CONFLICT', 'INTERNAL_SERVER_ERROR', 'INVALID_ACCOUNT']]


# BatchCreateBillScenarioCommitmentModificationItem

### key
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### group
- **Type**: typing.Optional[str]

### usageAccountId
- **Type**: typing.Optional[str]

### commitmentAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BillScenarioCommitmentModificationAction]


# BatchCreateBillScenarioCommitmentModificationRequest

### billScenarioId
- **Type**: <class 'str'>
- **Required**: Yes

### commitmentModifications
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BatchCreateBillScenarioCommitmentModificationEntry]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# BatchCreateBillScenarioCommitmentModificationResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BatchCreateBillScenarioCommitmentModificationItem]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BatchCreateBillScenarioCommitmentModificationError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes


# BatchCreateBillScenarioUsageModificationEntry

### serviceCode
- **Type**: <class 'str'>
- **Required**: Yes

### usageType
- **Type**: <class 'str'>
- **Required**: Yes

### operation
- **Type**: <class 'str'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes

### usageAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### availabilityZone
- **Type**: typing.Optional[str]

### group
- **Type**: typing.Optional[str]

### amounts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.UsageAmount]]

### historicalUsage
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.HistoricalUsageEntity, aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.HistoricalUsageEntityOutput, NoneType]


# BatchCreateBillScenarioUsageModificationError

### key
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[typing.Literal['BAD_REQUEST', 'CONFLICT', 'INTERNAL_SERVER_ERROR', 'NOT_FOUND']]


# BatchCreateBillScenarioUsageModificationItem

### serviceCode
- **Type**: <class 'str'>
- **Required**: Yes

### usageType
- **Type**: <class 'str'>
- **Required**: Yes

### operation
- **Type**: <class 'str'>
- **Required**: Yes

### location
- **Type**: typing.Optional[str]

### availabilityZone
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### group
- **Type**: typing.Optional[str]

### usageAccountId
- **Type**: typing.Optional[str]

### quantities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.UsageQuantity]]

### historicalUsage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.HistoricalUsageEntityOutput]

### key
- **Type**: typing.Optional[str]


# BatchCreateBillScenarioUsageModificationRequest

### billScenarioId
- **Type**: <class 'str'>
- **Required**: Yes

### usageModifications
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BatchCreateBillScenarioUsageModificationEntry]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# BatchCreateBillScenarioUsageModificationResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BatchCreateBillScenarioUsageModificationItem]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BatchCreateBillScenarioUsageModificationError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes


# BatchCreateWorkloadEstimateUsageEntry

### serviceCode
- **Type**: <class 'str'>
- **Required**: Yes

### usageType
- **Type**: <class 'str'>
- **Required**: Yes

### operation
- **Type**: <class 'str'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes

### usageAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### amount
- **Type**: <class 'float'>
- **Required**: Yes

### group
- **Type**: typing.Optional[str]

### historicalUsage
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.HistoricalUsageEntity, aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.HistoricalUsageEntityOutput, NoneType]


# BatchCreateWorkloadEstimateUsageError

### key
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[typing.Literal['BAD_REQUEST', 'CONFLICT', 'INTERNAL_SERVER_ERROR', 'NOT_FOUND']]

### errorMessage
- **Type**: typing.Optional[str]


# BatchCreateWorkloadEstimateUsageItem

### serviceCode
- **Type**: <class 'str'>
- **Required**: Yes

### usageType
- **Type**: <class 'str'>
- **Required**: Yes

### operation
- **Type**: <class 'str'>
- **Required**: Yes

### location
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### usageAccountId
- **Type**: typing.Optional[str]

### group
- **Type**: typing.Optional[str]

### quantity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.WorkloadEstimateUsageQuantity]

### cost
- **Type**: typing.Optional[float]

### currency
- **Type**: typing.Optional[typing.Literal['USD']]

### status
- **Type**: typing.Optional[typing.Literal['INVALID', 'STALE', 'VALID']]

### historicalUsage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.HistoricalUsageEntityOutput]

### key
- **Type**: typing.Optional[str]


# BatchCreateWorkloadEstimateUsageRequest

### workloadEstimateId
- **Type**: <class 'str'>
- **Required**: Yes

### usage
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BatchCreateWorkloadEstimateUsageEntry]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# BatchCreateWorkloadEstimateUsageResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BatchCreateWorkloadEstimateUsageItem]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BatchCreateWorkloadEstimateUsageError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDeleteBillScenarioCommitmentModificationError

### id
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[typing.Literal['BAD_REQUEST', 'CONFLICT', 'INTERNAL_SERVER_ERROR']]

### errorMessage
- **Type**: typing.Optional[str]


# BatchDeleteBillScenarioCommitmentModificationRequest

### billScenarioId
- **Type**: <class 'str'>
- **Required**: Yes

### ids
- **Type**: typing.List[str]
- **Required**: Yes


# BatchDeleteBillScenarioCommitmentModificationResponse

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BatchDeleteBillScenarioCommitmentModificationError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDeleteBillScenarioUsageModificationError

### id
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[typing.Literal['BAD_REQUEST', 'CONFLICT', 'INTERNAL_SERVER_ERROR']]


# BatchDeleteBillScenarioUsageModificationRequest

### billScenarioId
- **Type**: <class 'str'>
- **Required**: Yes

### ids
- **Type**: typing.List[str]
- **Required**: Yes


# BatchDeleteBillScenarioUsageModificationResponse

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BatchDeleteBillScenarioUsageModificationError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDeleteWorkloadEstimateUsageError

### id
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[typing.Literal['BAD_REQUEST', 'CONFLICT', 'INTERNAL_SERVER_ERROR', 'NOT_FOUND']]


# BatchDeleteWorkloadEstimateUsageRequest

### workloadEstimateId
- **Type**: <class 'str'>
- **Required**: Yes

### ids
- **Type**: typing.List[str]
- **Required**: Yes


# BatchDeleteWorkloadEstimateUsageResponse

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BatchDeleteWorkloadEstimateUsageError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes


# BatchUpdateBillScenarioCommitmentModificationEntry

### id
- **Type**: <class 'str'>
- **Required**: Yes

### group
- **Type**: typing.Optional[str]


# BatchUpdateBillScenarioCommitmentModificationError

### id
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[typing.Literal['BAD_REQUEST', 'CONFLICT', 'INTERNAL_SERVER_ERROR', 'NOT_FOUND']]

### errorMessage
- **Type**: typing.Optional[str]


# BatchUpdateBillScenarioCommitmentModificationRequest

### billScenarioId
- **Type**: <class 'str'>
- **Required**: Yes

### commitmentModifications
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BatchUpdateBillScenarioCommitmentModificationEntry]
- **Required**: Yes


# BatchUpdateBillScenarioCommitmentModificationResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BillScenarioCommitmentModificationItem]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BatchUpdateBillScenarioCommitmentModificationError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes


# BatchUpdateBillScenarioUsageModificationEntry

### id
- **Type**: <class 'str'>
- **Required**: Yes

### group
- **Type**: typing.Optional[str]

### amounts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.UsageAmount]]


# BatchUpdateBillScenarioUsageModificationError

### id
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[typing.Literal['BAD_REQUEST', 'CONFLICT', 'INTERNAL_SERVER_ERROR', 'NOT_FOUND']]


# BatchUpdateBillScenarioUsageModificationRequest

### billScenarioId
- **Type**: <class 'str'>
- **Required**: Yes

### usageModifications
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BatchUpdateBillScenarioUsageModificationEntry]
- **Required**: Yes


# BatchUpdateBillScenarioUsageModificationResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BillScenarioUsageModificationItem]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BatchUpdateBillScenarioUsageModificationError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes


# BatchUpdateWorkloadEstimateUsageEntry

### id
- **Type**: <class 'str'>
- **Required**: Yes

### group
- **Type**: typing.Optional[str]

### amount
- **Type**: typing.Optional[float]


# BatchUpdateWorkloadEstimateUsageError

### id
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[typing.Literal['BAD_REQUEST', 'CONFLICT', 'INTERNAL_SERVER_ERROR', 'NOT_FOUND']]


# BatchUpdateWorkloadEstimateUsageRequest

### workloadEstimateId
- **Type**: <class 'str'>
- **Required**: Yes

### usage
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BatchUpdateWorkloadEstimateUsageEntry]
- **Required**: Yes


# BatchUpdateWorkloadEstimateUsageResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.WorkloadEstimateUsageItem]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BatchUpdateWorkloadEstimateUsageError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes


# BillEstimateCommitmentSummary

### id
- **Type**: typing.Optional[str]

### purchaseAgreementType
- **Type**: typing.Optional[typing.Literal['RESERVED_INSTANCE', 'SAVINGS_PLANS']]

### offeringId
- **Type**: typing.Optional[str]

### usageAccountId
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[str]

### termLength
- **Type**: typing.Optional[str]

### paymentOption
- **Type**: typing.Optional[str]

### upfrontPayment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.CostAmount]

### monthlyPayment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.CostAmount]


# BillEstimateCostSummary

### totalCostDifference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.CostDifference]

### serviceCostDifferences
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.CostDifference]]


# BillEstimateInputCommitmentModificationSummary

### id
- **Type**: typing.Optional[str]

### group
- **Type**: typing.Optional[str]

### usageAccountId
- **Type**: typing.Optional[str]

### commitmentAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BillScenarioCommitmentModificationAction]


# BillEstimateInputUsageModificationSummary

### serviceCode
- **Type**: <class 'str'>
- **Required**: Yes

### usageType
- **Type**: <class 'str'>
- **Required**: Yes

### operation
- **Type**: <class 'str'>
- **Required**: Yes

### location
- **Type**: typing.Optional[str]

### availabilityZone
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### group
- **Type**: typing.Optional[str]

### usageAccountId
- **Type**: typing.Optional[str]

### quantities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.UsageQuantity]]

### historicalUsage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.HistoricalUsageEntityOutput]


# BillEstimateInputUsageModificationSummaryPaginator

### serviceCode
- **Type**: <class 'str'>
- **Required**: Yes

### usageType
- **Type**: <class 'str'>
- **Required**: Yes

### operation
- **Type**: <class 'str'>
- **Required**: Yes

### location
- **Type**: typing.Optional[str]

### availabilityZone
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### group
- **Type**: typing.Optional[str]

### usageAccountId
- **Type**: typing.Optional[str]

### quantities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.UsageQuantity]]

### historicalUsage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.HistoricalUsageEntityPaginator]


# BillEstimateLineItemSummary

### serviceCode
- **Type**: <class 'str'>
- **Required**: Yes

### usageType
- **Type**: <class 'str'>
- **Required**: Yes

### operation
- **Type**: <class 'str'>
- **Required**: Yes

### location
- **Type**: typing.Optional[str]

### availabilityZone
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### lineItemId
- **Type**: typing.Optional[str]

### lineItemType
- **Type**: typing.Optional[str]

### payerAccountId
- **Type**: typing.Optional[str]

### usageAccountId
- **Type**: typing.Optional[str]

### estimatedUsageQuantity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.UsageQuantityResult]

### estimatedCost
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.CostAmount]

### historicalUsageQuantity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.UsageQuantityResult]

### historicalCost
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.CostAmount]

### savingsPlanArns
- **Type**: typing.Optional[typing.List[str]]


# BillEstimateSummary

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'FAILED', 'IN_PROGRESS']]

### billInterval
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BillIntervalOutput]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### expiresAt
- **Type**: typing.Optional[datetime.datetime]


# BillInterval

### start
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### end
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# BillIntervalOutput

### start
- **Type**: typing.Optional[datetime.datetime]

### end
- **Type**: typing.Optional[datetime.datetime]


# BillScenarioCommitmentModificationAction

### addReservedInstanceAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.AddReservedInstanceAction]

### addSavingsPlanAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.AddSavingsPlanAction]

### negateReservedInstanceAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.NegateReservedInstanceAction]

### negateSavingsPlanAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.NegateSavingsPlanAction]


# BillScenarioCommitmentModificationItem

### id
- **Type**: typing.Optional[str]

### usageAccountId
- **Type**: typing.Optional[str]

### group
- **Type**: typing.Optional[str]

### commitmentAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BillScenarioCommitmentModificationAction]


# BillScenarioSummary

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### billInterval
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BillIntervalOutput]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'LOCKED', 'READY']]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### expiresAt
- **Type**: typing.Optional[datetime.datetime]

### failureMessage
- **Type**: typing.Optional[str]


# BillScenarioUsageModificationItem

### serviceCode
- **Type**: <class 'str'>
- **Required**: Yes

### usageType
- **Type**: <class 'str'>
- **Required**: Yes

### operation
- **Type**: <class 'str'>
- **Required**: Yes

### location
- **Type**: typing.Optional[str]

### availabilityZone
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### group
- **Type**: typing.Optional[str]

### usageAccountId
- **Type**: typing.Optional[str]

### quantities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.UsageQuantity]]

### historicalUsage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.HistoricalUsageEntityOutput]


# BillScenarioUsageModificationItemPaginator

### serviceCode
- **Type**: <class 'str'>
- **Required**: Yes

### usageType
- **Type**: <class 'str'>
- **Required**: Yes

### operation
- **Type**: <class 'str'>
- **Required**: Yes

### location
- **Type**: typing.Optional[str]

### availabilityZone
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### group
- **Type**: typing.Optional[str]

### usageAccountId
- **Type**: typing.Optional[str]

### quantities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.UsageQuantity]]

### historicalUsage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.HistoricalUsageEntityPaginator]


# CostAmount

### amount
- **Type**: typing.Optional[float]

### currency
- **Type**: typing.Optional[typing.Literal['USD']]


# CostDifference

### historicalCost
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.CostAmount]

### estimatedCost
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.CostAmount]


# CreateBillEstimateRequest

### billScenarioId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateBillEstimateResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['COMPLETE', 'FAILED', 'IN_PROGRESS']
- **Required**: Yes

### failureMessage
- **Type**: <class 'str'>
- **Required**: Yes

### billInterval
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BillIntervalOutput'>
- **Required**: Yes

### costSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BillEstimateCostSummary'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### expiresAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes


# CreateBillScenarioRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateBillScenarioResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### billInterval
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BillIntervalOutput'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'LOCKED', 'READY']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### expiresAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### failureMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWorkloadEstimateRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### rateType
- **Type**: typing.Optional[typing.Literal['AFTER_DISCOUNTS', 'BEFORE_DISCOUNTS']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateWorkloadEstimateResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### expiresAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### rateType
- **Type**: typing.Literal['AFTER_DISCOUNTS', 'BEFORE_DISCOUNTS']
- **Required**: Yes

### rateTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTION_NEEDED', 'INVALID', 'UPDATING', 'VALID']
- **Required**: Yes

### totalCost
- **Type**: <class 'float'>
- **Required**: Yes

### costCurrency
- **Type**: typing.Literal['USD']
- **Required**: Yes

### failureMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteBillEstimateRequest

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBillScenarioRequest

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkloadEstimateRequest

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# Expression

### and_
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### or_
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### not_
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### costCategories
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ExpressionFilter, aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ExpressionFilterOutput, NoneType]

### dimensions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ExpressionFilter, aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ExpressionFilterOutput, NoneType]

### tags
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ExpressionFilter, aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ExpressionFilterOutput, NoneType]


# ExpressionFilter

### key
- **Type**: typing.Optional[str]

### matchOptions
- **Type**: typing.Optional[typing.List[str]]

### values
- **Type**: typing.Optional[typing.List[str]]


# ExpressionFilterOutput

### key
- **Type**: typing.Optional[str]

### matchOptions
- **Type**: typing.Optional[typing.List[str]]

### values
- **Type**: typing.Optional[typing.List[str]]


# ExpressionOutput

### and_
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### or_
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### not_
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### costCategories
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ExpressionFilterOutput]

### dimensions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ExpressionFilterOutput]

### tags
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ExpressionFilterOutput]


# ExpressionPaginator

### and_
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### or_
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### not_
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### costCategories
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ExpressionFilterOutput]

### dimensions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ExpressionFilterOutput]

### tags
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ExpressionFilterOutput]


# FilterTimestamp

### afterTimestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### beforeTimestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# GetBillEstimateRequest

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetBillEstimateResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['COMPLETE', 'FAILED', 'IN_PROGRESS']
- **Required**: Yes

### failureMessage
- **Type**: <class 'str'>
- **Required**: Yes

### billInterval
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BillIntervalOutput'>
- **Required**: Yes

### costSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BillEstimateCostSummary'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### expiresAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes


# GetBillScenarioRequest

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetBillScenarioResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### billInterval
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BillIntervalOutput'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'LOCKED', 'READY']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### expiresAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### failureMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes


# GetPreferencesResponse

### managementAccountRateTypeSelections
- **Type**: typing.List[typing.Literal['AFTER_DISCOUNTS', 'BEFORE_DISCOUNTS']]
- **Required**: Yes

### memberAccountRateTypeSelections
- **Type**: typing.List[typing.Literal['AFTER_DISCOUNTS', 'BEFORE_DISCOUNTS']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes


# GetWorkloadEstimateRequest

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkloadEstimateResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### expiresAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### rateType
- **Type**: typing.Literal['AFTER_DISCOUNTS', 'BEFORE_DISCOUNTS']
- **Required**: Yes

### rateTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTION_NEEDED', 'INVALID', 'UPDATING', 'VALID']
- **Required**: Yes

### totalCost
- **Type**: <class 'float'>
- **Required**: Yes

### costCurrency
- **Type**: typing.Literal['USD']
- **Required**: Yes

### failureMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes


# HistoricalUsageEntity

### serviceCode
- **Type**: <class 'str'>
- **Required**: Yes

### usageType
- **Type**: <class 'str'>
- **Required**: Yes

### operation
- **Type**: <class 'str'>
- **Required**: Yes

### usageAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### billInterval
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BillInterval, aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BillIntervalOutput]
- **Required**: Yes

### filterExpression
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.Expression, aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ExpressionOutput]
- **Required**: Yes

### location
- **Type**: typing.Optional[str]


# HistoricalUsageEntityOutput

### serviceCode
- **Type**: <class 'str'>
- **Required**: Yes

### usageType
- **Type**: <class 'str'>
- **Required**: Yes

### operation
- **Type**: <class 'str'>
- **Required**: Yes

### usageAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### billInterval
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BillIntervalOutput'>
- **Required**: Yes

### filterExpression
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ExpressionOutput'>
- **Required**: Yes

### location
- **Type**: typing.Optional[str]


# HistoricalUsageEntityPaginator

### serviceCode
- **Type**: <class 'str'>
- **Required**: Yes

### usageType
- **Type**: <class 'str'>
- **Required**: Yes

### operation
- **Type**: <class 'str'>
- **Required**: Yes

### usageAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### billInterval
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BillIntervalOutput'>
- **Required**: Yes

### filterExpression
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ExpressionPaginator'>
- **Required**: Yes

### location
- **Type**: typing.Optional[str]


# ListBillEstimateCommitmentsRequest

### billEstimateId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListBillEstimateCommitmentsRequestPaginate

### billEstimateId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.PaginatorConfig]


# ListBillEstimateCommitmentsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BillEstimateCommitmentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBillEstimateInputCommitmentModificationsRequest

### billEstimateId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListBillEstimateInputCommitmentModificationsRequestPaginate

### billEstimateId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.PaginatorConfig]


# ListBillEstimateInputCommitmentModificationsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BillEstimateInputCommitmentModificationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBillEstimateInputUsageModificationsRequest

### billEstimateId
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ListUsageFilter]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListBillEstimateInputUsageModificationsRequestPaginate

### billEstimateId
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ListUsageFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.PaginatorConfig]


# ListBillEstimateInputUsageModificationsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BillEstimateInputUsageModificationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBillEstimateInputUsageModificationsResponsePaginator

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BillEstimateInputUsageModificationSummaryPaginator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBillEstimateLineItemsFilter

### name
- **Type**: typing.Literal['LINE_ITEM_TYPE', 'LOCATION', 'OPERATION', 'SERVICE_CODE', 'USAGE_ACCOUNT_ID', 'USAGE_TYPE']
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes

### matchOption
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EQUALS', 'STARTS_WITH']]


# ListBillEstimateLineItemsRequest

### billEstimateId
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ListBillEstimateLineItemsFilter]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListBillEstimateLineItemsRequestPaginate

### billEstimateId
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ListBillEstimateLineItemsFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.PaginatorConfig]


# ListBillEstimateLineItemsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BillEstimateLineItemSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBillEstimatesFilter

### name
- **Type**: typing.Literal['NAME', 'STATUS']
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes

### matchOption
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EQUALS', 'STARTS_WITH']]


# ListBillEstimatesRequest

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ListBillEstimatesFilter]]

### createdAtFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.FilterTimestamp]

### expiresAtFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.FilterTimestamp]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListBillEstimatesRequestPaginate

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ListBillEstimatesFilter]]

### createdAtFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.FilterTimestamp]

### expiresAtFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.FilterTimestamp]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.PaginatorConfig]


# ListBillEstimatesResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BillEstimateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBillScenarioCommitmentModificationsRequest

### billScenarioId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListBillScenarioCommitmentModificationsRequestPaginate

### billScenarioId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.PaginatorConfig]


# ListBillScenarioCommitmentModificationsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BillScenarioCommitmentModificationItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBillScenarioUsageModificationsRequest

### billScenarioId
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ListUsageFilter]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListBillScenarioUsageModificationsRequestPaginate

### billScenarioId
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ListUsageFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.PaginatorConfig]


# ListBillScenarioUsageModificationsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BillScenarioUsageModificationItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBillScenarioUsageModificationsResponsePaginator

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BillScenarioUsageModificationItemPaginator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBillScenariosFilter

### name
- **Type**: typing.Literal['NAME', 'STATUS']
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes

### matchOption
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EQUALS', 'STARTS_WITH']]


# ListBillScenariosRequest

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ListBillScenariosFilter]]

### createdAtFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.FilterTimestamp]

### expiresAtFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.FilterTimestamp]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListBillScenariosRequestPaginate

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ListBillScenariosFilter]]

### createdAtFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.FilterTimestamp]

### expiresAtFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.FilterTimestamp]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.PaginatorConfig]


# ListBillScenariosResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BillScenarioSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes


# ListUsageFilter

### name
- **Type**: typing.Literal['HISTORICAL_LOCATION', 'HISTORICAL_OPERATION', 'HISTORICAL_SERVICE_CODE', 'HISTORICAL_USAGE_ACCOUNT_ID', 'HISTORICAL_USAGE_TYPE', 'LOCATION', 'OPERATION', 'SERVICE_CODE', 'USAGE_ACCOUNT_ID', 'USAGE_GROUP', 'USAGE_TYPE']
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes

### matchOption
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EQUALS', 'STARTS_WITH']]


# ListWorkloadEstimateUsageRequest

### workloadEstimateId
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ListUsageFilter]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListWorkloadEstimateUsageRequestPaginate

### workloadEstimateId
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ListUsageFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.PaginatorConfig]


# ListWorkloadEstimateUsageResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.WorkloadEstimateUsageItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkloadEstimateUsageResponsePaginator

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.WorkloadEstimateUsageItemPaginator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkloadEstimatesFilter

### name
- **Type**: typing.Literal['NAME', 'STATUS']
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes

### matchOption
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EQUALS', 'STARTS_WITH']]


# ListWorkloadEstimatesRequest

### createdAtFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.FilterTimestamp]

### expiresAtFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.FilterTimestamp]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ListWorkloadEstimatesFilter]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListWorkloadEstimatesRequestPaginate

### createdAtFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.FilterTimestamp]

### expiresAtFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.FilterTimestamp]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ListWorkloadEstimatesFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.PaginatorConfig]


# ListWorkloadEstimatesResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.WorkloadEstimateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# NegateReservedInstanceAction

### reservedInstancesId
- **Type**: typing.Optional[str]


# NegateSavingsPlanAction

### savingsPlanId
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


# TagResourceRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateBillEstimateRequest

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### expiresAt
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# UpdateBillEstimateResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['COMPLETE', 'FAILED', 'IN_PROGRESS']
- **Required**: Yes

### failureMessage
- **Type**: <class 'str'>
- **Required**: Yes

### billInterval
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BillIntervalOutput'>
- **Required**: Yes

### costSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BillEstimateCostSummary'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### expiresAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateBillScenarioRequest

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### expiresAt
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# UpdateBillScenarioResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### billInterval
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.BillIntervalOutput'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'LOCKED', 'READY']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### expiresAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### failureMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePreferencesRequest

### managementAccountRateTypeSelections
- **Type**: typing.Optional[typing.List[typing.Literal['AFTER_DISCOUNTS', 'BEFORE_DISCOUNTS']]]

### memberAccountRateTypeSelections
- **Type**: typing.Optional[typing.List[typing.Literal['AFTER_DISCOUNTS', 'BEFORE_DISCOUNTS']]]


# UpdatePreferencesResponse

### managementAccountRateTypeSelections
- **Type**: typing.List[typing.Literal['AFTER_DISCOUNTS', 'BEFORE_DISCOUNTS']]
- **Required**: Yes

### memberAccountRateTypeSelections
- **Type**: typing.List[typing.Literal['AFTER_DISCOUNTS', 'BEFORE_DISCOUNTS']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateWorkloadEstimateRequest

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### expiresAt
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# UpdateWorkloadEstimateResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### expiresAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### rateType
- **Type**: typing.Literal['AFTER_DISCOUNTS', 'BEFORE_DISCOUNTS']
- **Required**: Yes

### rateTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTION_NEEDED', 'INVALID', 'UPDATING', 'VALID']
- **Required**: Yes

### totalCost
- **Type**: <class 'float'>
- **Required**: Yes

### costCurrency
- **Type**: typing.Literal['USD']
- **Required**: Yes

### failureMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.ResponseMetadata'>
- **Required**: Yes


# UsageAmount

### startHour
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### amount
- **Type**: <class 'float'>
- **Required**: Yes


# UsageQuantity

### startHour
- **Type**: typing.Optional[datetime.datetime]

### unit
- **Type**: typing.Optional[str]

### amount
- **Type**: typing.Optional[float]


# UsageQuantityResult

### amount
- **Type**: typing.Optional[float]

### unit
- **Type**: typing.Optional[str]


# WorkloadEstimateSummary

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### expiresAt
- **Type**: typing.Optional[datetime.datetime]

### rateType
- **Type**: typing.Optional[typing.Literal['AFTER_DISCOUNTS', 'BEFORE_DISCOUNTS']]

### rateTimestamp
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['ACTION_NEEDED', 'INVALID', 'UPDATING', 'VALID']]

### totalCost
- **Type**: typing.Optional[float]

### costCurrency
- **Type**: typing.Optional[typing.Literal['USD']]

### failureMessage
- **Type**: typing.Optional[str]


# WorkloadEstimateUsageItem

### serviceCode
- **Type**: <class 'str'>
- **Required**: Yes

### usageType
- **Type**: <class 'str'>
- **Required**: Yes

### operation
- **Type**: <class 'str'>
- **Required**: Yes

### location
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### usageAccountId
- **Type**: typing.Optional[str]

### group
- **Type**: typing.Optional[str]

### quantity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.WorkloadEstimateUsageQuantity]

### cost
- **Type**: typing.Optional[float]

### currency
- **Type**: typing.Optional[typing.Literal['USD']]

### status
- **Type**: typing.Optional[typing.Literal['INVALID', 'STALE', 'VALID']]

### historicalUsage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.HistoricalUsageEntityOutput]


# WorkloadEstimateUsageItemPaginator

### serviceCode
- **Type**: <class 'str'>
- **Required**: Yes

### usageType
- **Type**: <class 'str'>
- **Required**: Yes

### operation
- **Type**: <class 'str'>
- **Required**: Yes

### location
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### usageAccountId
- **Type**: typing.Optional[str]

### group
- **Type**: typing.Optional[str]

### quantity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.WorkloadEstimateUsageQuantity]

### cost
- **Type**: typing.Optional[float]

### currency
- **Type**: typing.Optional[typing.Literal['USD']]

### status
- **Type**: typing.Optional[typing.Literal['INVALID', 'STALE', 'VALID']]

### historicalUsage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bcm_pricing_calculator.bcm_pricing_calculator_classes.HistoricalUsageEntityPaginator]


# WorkloadEstimateUsageQuantity

### unit
- **Type**: typing.Optional[str]

### amount
- **Type**: typing.Optional[float]


