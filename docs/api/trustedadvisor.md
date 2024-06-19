# Trustedadvisor Service

### AccountId
- **Type**: string
- **Pattern**: `^\d+$`
- **Min Length**: 12
- **Max Length**: 12

### AccountRecommendationArn
- **Type**: string
- **Pattern**: `^arn:[\w-]+:trustedadvisor::\d{12}:recommendation\/[\w-]+$`
- **Min Length**: 20
- **Max Length**: 2048

### AccountRecommendationIdentifier
- **Type**: string
- **Pattern**: `^arn:[\w-]+:trustedadvisor::\d{12}:recommendation\/[\w-]+$`
- **Min Length**: 20
- **Max Length**: 200

### CheckArn
- **Type**: string
- **Pattern**: `^arn:[\w-]+:trustedadvisor:::check\/[\w-]+$`
- **Min Length**: 20
- **Max Length**: 2048

### CheckIdentifier
- **Type**: string
- **Pattern**: `^arn:[\w-]+:trustedadvisor:::check\/[\w-]+$`
- **Min Length**: 20
- **Max Length**: 64

### OrganizationRecommendationArn
- **Type**: string
- **Pattern**: `^arn:[\w-]+:trustedadvisor:::organization-recommendation\/[\w-]+$`
- **Min Length**: 20
- **Max Length**: 2048

### OrganizationRecommendationIdentifier
- **Type**: string
- **Pattern**: `^arn:[\w-]+:trustedadvisor:::organization-recommendation\/[\w-]+$`
- **Min Length**: 20
- **Max Length**: 200

### RecommendationResourceArn
- **Type**: string
- **Pattern**: `^arn:[\w-]+:trustedadvisor::\d{12}:recommendation-resource\/[\w-]+\/[\w-]+$`
- **Min Length**: 20
- **Max Length**: 2048

### RecommendationUpdateReason
- **Type**: string
- **Pattern**: `^[\s\S]*$`
- **Min Length**: 10
- **Max Length**: 4096

