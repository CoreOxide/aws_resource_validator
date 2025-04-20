# Marketplacereporting Service

### DashboardIdentifier
- **Type**: string
- **Pattern**: `arn:aws:aws-marketplace::[0-9]{12}:AWSMarketplace/ReportingData/(Agreement_V1/Dashboard/AgreementSummary_V1|BillingEvent_V1/Dashboard/CostAnalysis_V1)`
- **Min Length**: 1
- **Max Length**: 1023

### EmbeddingDomain
- **Type**: string
- **Pattern**: `(https://[a-zA-Z\.\*0-9\-_]+[\.]{1}[a-zA-Z]{1,}[a-zA-Z0-9&?/-_=]*[a-zA-Z\*0-9/]+|http[s]*://localhost(:[0-9]{1,5})?)`
- **Min Length**: 1
- **Max Length**: 2000

