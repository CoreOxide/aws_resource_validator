# Pcaconnectorscep Service

### AzureApplicationId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]{2,15}-[a-zA-Z0-9]{2,15}-[a-zA-Z0-9]{2,15}-[a-zA-Z0-9]{2,15}-[a-zA-Z0-9]{2,15}`
- **Min Length**: 15
- **Max Length**: 100

### AzureDomain
- **Type**: string
- **Pattern**: `[a-zA-Z0-9._-]+`
- **Min Length**: 1
- **Max Length**: 256

### CertificateAuthorityArn
- **Type**: string
- **Pattern**: `arn:aws(-[a-z]+)*:acm-pca:[a-z]+(-[a-z]+)+-[1-9]\d*:\d{12}:certificate-authority\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}`
- **Min Length**: 5
- **Max Length**: 200

### ChallengeArn
- **Type**: string
- **Pattern**: `arn:aws(-[a-z]+)*:pca-connector-scep:[a-z]+(-[a-z]+)+-[1-9]\d*:\d{12}:connector\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}\/challenge\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}`
- **Min Length**: 5
- **Max Length**: 200

### ClientToken
- **Type**: string
- **Pattern**: `[!-~]+`
- **Min Length**: 1
- **Max Length**: 64

### ConnectorArn
- **Type**: string
- **Pattern**: `arn:aws(-[a-z]+)*:pca-connector-scep:[a-z]+(-[a-z]+)+-[1-9]\d*:\d{12}:connector\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}`
- **Min Length**: 5
- **Max Length**: 200

### NextToken
- **Type**: string
- **Pattern**: `(?:[A-Za-z0-9_-]{4})*(?:[A-Za-z0-9_-]{2}==|[A-Za-z0-9_-]{3}=)?`
- **Min Length**: 1
- **Max Length**: 1000

