# Billingconductor Service

### AccountId
- **Type**: string
- **Pattern**: `[0-9]{12}`

### Arn
- **Type**: string
- **Pattern**: `arn:aws(-cn)?:billingconductor::[0-9]{12}:billinggroup/?[0-9]{12}$|^arn:aws(-cn)?:billingconductor::[0-9]{12}:pricingplan/[a-zA-Z0-9]{10}$|^arn:aws(-cn)?:billingconductor::[0-9]{12}:pricingrule/[a-zA-Z0-9]{10}$|^(arn:aws(-cn)?:billingconductor::[0-9]{12}:customlineitem/)?[a-zA-Z0-9]{10}`
- **Min Length**: 0
- **Max Length**: 100

### Association
- **Type**: string
- **Pattern**: `((arn:aws(-cn)?:billingconductor::[0-9]{12}:billinggroup/)?[0-9]{12}|MONITORED|UNMONITORED)`

### BillingEntity
- **Type**: string
- **Pattern**: `[a-zA-Z0-9 ]+`

### BillingGroupArn
- **Type**: string
- **Pattern**: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:billinggroup/)?[0-9]{12}`

### BillingGroupFullArn
- **Type**: string
- **Pattern**: `arn:aws(-cn)?:billingconductor::[0-9]{12}:billinggroup/[0-9]{12}`

### BillingGroupName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_\+=\.\-@]+`
- **Min Length**: 1
- **Max Length**: 128

### BillingPeriod
- **Type**: string
- **Pattern**: `\d{4}-(0?[1-9]|1[012])`

### ClientToken
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-]+`
- **Min Length**: 1
- **Max Length**: 64

### CustomLineItemArn
- **Type**: string
- **Pattern**: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:customlineitem/)?[a-zA-Z0-9]{10}`

### CustomLineItemAssociationElement
- **Type**: string
- **Pattern**: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:(customlineitem|billinggroup)/)?[a-zA-Z0-9]{10,12}`

### CustomLineItemName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_\+=\.\-@]+`
- **Min Length**: 1
- **Max Length**: 128

### Operation
- **Type**: string
- **Pattern**: `\S+`
- **Min Length**: 1
- **Max Length**: 256

### PricingPlanArn
- **Type**: string
- **Pattern**: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:pricingplan/)?[a-zA-Z0-9]{10}`

### PricingPlanFullArn
- **Type**: string
- **Pattern**: `arn:aws(-cn)?:billingconductor::[0-9]{12}:pricingplan/[a-zA-Z0-9]{10}`

### PricingPlanName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_\+=\.\-@]+`
- **Min Length**: 1
- **Max Length**: 128

### PricingRuleArn
- **Type**: string
- **Pattern**: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:pricingrule/)?[a-zA-Z0-9]{10}`

### PricingRuleName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_\+=\.\-@]+`
- **Min Length**: 1
- **Max Length**: 128

### Service
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]+`
- **Min Length**: 1
- **Max Length**: 128

### UsageType
- **Type**: string
- **Pattern**: `\S+`
- **Min Length**: 1
- **Max Length**: 256

