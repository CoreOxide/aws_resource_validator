# Pcaconnectorad Service

### CertificateAuthorityArn
- **Type**: string
- **Pattern**: `^arn:[\w-]+:acm-pca:[\w-]+:[0-9]+:certificate-authority\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}$`
- **Min Length**: 5
- **Max Length**: 200

### ClientToken
- **Type**: string
- **Pattern**: `^[!-~]+$`
- **Min Length**: 1
- **Max Length**: 64

### ConnectorArn
- **Type**: string
- **Pattern**: `^arn:[\w-]+:pca-connector-ad:[\w-]+:[0-9]+:connector\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}$`
- **Min Length**: 5
- **Max Length**: 200

### CustomObjectIdentifier
- **Type**: string
- **Pattern**: `^([0-2])\.([0-9]|([0-3][0-9]))(\.([0-9]+)){0,126}$`
- **Min Length**: 1
- **Max Length**: 64

### DirectoryId
- **Type**: string
- **Pattern**: `^d-[0-9a-f]{10}$`

### DirectoryRegistrationArn
- **Type**: string
- **Pattern**: `^arn:[\w-]+:pca-connector-ad:[\w-]+:[0-9]+:directory-registration\/d-[0-9a-f]{10}$`
- **Min Length**: 5
- **Max Length**: 200

### DisplayName
- **Type**: string
- **Pattern**: `^[\x20-\x7E]+$`
- **Min Length**: 0
- **Max Length**: 256

### GroupSecurityIdentifier
- **Type**: string
- **Pattern**: `^S-[0-9]-([0-9]+-){1,14}[0-9]+$`
- **Min Length**: 7
- **Max Length**: 256

### NextToken
- **Type**: string
- **Pattern**: `^(?:[A-Za-z0-9_-]{4})*(?:[A-Za-z0-9_-]{2}==|[A-Za-z0-9_-]{3}=)?$`
- **Min Length**: 1
- **Max Length**: 1000

### SecurityGroupId
- **Type**: string
- **Pattern**: `^(?:sg-[0-9a-f]{8}|sg-[0-9a-f]{17})$`
- **Min Length**: 11
- **Max Length**: 20

### TemplateArn
- **Type**: string
- **Pattern**: `^arn:[\w-]+:pca-connector-ad:[\w-]+:[0-9]+:connector\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}\/template\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}$`
- **Min Length**: 5
- **Max Length**: 200

### TemplateName
- **Type**: string
- **Pattern**: `^(?!^\s+$)((?![\x5c\'\x2b,;<=>#\x22])([\x20-\x7E]))+$`
- **Min Length**: 1
- **Max Length**: 64

