# Auditmanager Service

### AWSServiceName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-\s().]+$`
- **Min Length**: 1
- **Max Length**: 40

### AccountId
- **Type**: string
- **Pattern**: `^[0-9]{12}$`
- **Min Length**: 12
- **Max Length**: 12

### AccountName
- **Type**: string
- **Pattern**: `^[\u0020-\u007E]+$`
- **Min Length**: 1
- **Max Length**: 50

### ActionPlanInstructions
- **Type**: string
- **Pattern**: `^[\w\W\s\S]*$`
- **Max Length**: 1000

### ActionPlanTitle
- **Type**: string
- **Pattern**: `^[\w\W\s\S]*$`
- **Max Length**: 300

### AssessmentDescription
- **Type**: string
- **Pattern**: `^[\w\W\s\S]*$`
- **Max Length**: 1000

### AssessmentEvidenceFolderName
- **Type**: string
- **Pattern**: `^[\w\W\s\S]*$`
- **Min Length**: 1
- **Max Length**: 300

### AssessmentFrameworkDescription
- **Type**: string
- **Pattern**: `^[\w\W\s\S]*$`
- **Min Length**: 1
- **Max Length**: 200

### AssessmentName
- **Type**: string
- **Pattern**: `^[^\\]*$`
- **Min Length**: 1
- **Max Length**: 300

### AssessmentReportDescription
- **Type**: string
- **Pattern**: `^[\w\W\s\S]*$`
- **Max Length**: 1000

### AssessmentReportName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_\.]+$`
- **Min Length**: 1
- **Max Length**: 300

### AuditManagerArn
- **Type**: string
- **Pattern**: `^arn:.*:auditmanager:.*`
- **Min Length**: 20
- **Max Length**: 2048

### CloudTrailArn
- **Type**: string
- **Pattern**: `^arn:.*:cloudtrail:.*`
- **Min Length**: 20
- **Max Length**: 2048

### ComplianceType
- **Type**: string
- **Pattern**: `^[\w\W\s\S]*$`
- **Max Length**: 100

### ControlCommentBody
- **Type**: string
- **Pattern**: `^[\w\W\s\S]*$`
- **Max Length**: 500

### ControlDescription
- **Type**: string
- **Pattern**: `^[\w\W\s\S]*$`
- **Max Length**: 1000

### ControlName
- **Type**: string
- **Pattern**: `^[^\\]*$`
- **Min Length**: 1
- **Max Length**: 300

### ControlSetId
- **Type**: string
- **Pattern**: `^[\w\W\s\S]*$`
- **Min Length**: 1
- **Max Length**: 300

### ControlSetName
- **Type**: string
- **Pattern**: `^[^\\\_]*$`
- **Min Length**: 1
- **Max Length**: 300

### ControlSources
- **Type**: string
- **Pattern**: `^[a-zA-Z_0-9-\s.,]+$`
- **Min Length**: 1
- **Max Length**: 100

### CreatedBy
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\s-_()\[\]]+$`
- **Min Length**: 1
- **Max Length**: 100

### DelegationComment
- **Type**: string
- **Pattern**: `^[\w\W\s\S]*$`
- **Max Length**: 350

### EmailAddress
- **Type**: string
- **Pattern**: `^.*@.*$`
- **Min Length**: 1
- **Max Length**: 320

### ErrorCode
- **Type**: string
- **Pattern**: `[0-9]{3}`
- **Min Length**: 3
- **Max Length**: 3

### ErrorMessage
- **Type**: string
- **Pattern**: `^[\w\W\s\S]*$`
- **Max Length**: 300

### EventName
- **Type**: string
- **Pattern**: `^[\w\W\s\S]*$`
- **Max Length**: 100

### EvidenceAttributeKey
- **Type**: string
- **Pattern**: `^[\w\W\s\S]*$`
- **Max Length**: 100

### EvidenceAttributeValue
- **Type**: string
- **Pattern**: `^[\w\W\s\S]*$`
- **Max Length**: 200

### Filename
- **Type**: string
- **Pattern**: `^[\w,\s-]+\.[A-Za-z]+$`
- **Min Length**: 1
- **Max Length**: 255

### FrameworkDescription
- **Type**: string
- **Pattern**: `^[\w\W\s\S]*$`
- **Min Length**: 1
- **Max Length**: 1000

### FrameworkName
- **Type**: string
- **Pattern**: `^[^\\]*$`
- **Min Length**: 1
- **Max Length**: 300

### GenericArn
- **Type**: string
- **Pattern**: `^arn:.*`
- **Min Length**: 20
- **Max Length**: 2048

### HyperlinkName
- **Type**: string
- **Pattern**: `^[\w\W\s\S]*$`
- **Min Length**: 1
- **Max Length**: 200

### IamArn
- **Type**: string
- **Pattern**: `^arn:.*:iam:.*`
- **Min Length**: 20
- **Max Length**: 2048

### KeywordValue
- **Type**: string
- **Pattern**: `^[a-zA-Z_0-9-\s().]+$`
- **Min Length**: 1
- **Max Length**: 100

### KmsKey
- **Type**: string
- **Pattern**: `^arn:.*:kms:.*|DEFAULT`
- **Min Length**: 7
- **Max Length**: 2048

### LastUpdatedBy
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\s-_()\[\]]+$`
- **Min Length**: 1
- **Max Length**: 100

### ManualEvidenceLocalFileName
- **Type**: string
- **Pattern**: `[^\/]*`
- **Min Length**: 1
- **Max Length**: 300

### ManualEvidenceTextResponse
- **Type**: string
- **Pattern**: `^[\w\W\s\S]*$`
- **Min Length**: 1
- **Max Length**: 1000

### NonEmptyString
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 2048

### QueryStatement
- **Type**: string
- **Pattern**: `(?s).*`
- **Min Length**: 1
- **Max Length**: 10000

### Region
- **Type**: string
- **Pattern**: `^[a-z]{2}-[a-z]+-[0-9]{1}$`

### S3Url
- **Type**: string
- **Pattern**: `^(S|s)3:\/\/[a-zA-Z0-9\-\.\(\)\\'\*\_\!\/]+$`
- **Min Length**: 1
- **Max Length**: 1024

### SNSTopic
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_\(\)\[\]]+$`
- **Min Length**: 1
- **Max Length**: 255

### ShareRequestComment
- **Type**: string
- **Pattern**: `^[\w\W\s\S]*$`
- **Max Length**: 500

### SnsArn
- **Type**: string
- **Pattern**: `^arn:.*:sns:.*|NONE`
- **Min Length**: 4
- **Max Length**: 2048

### SourceDescription
- **Type**: string
- **Pattern**: `^[\w\W\s\S]*$`
- **Max Length**: 1000

### String
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 2048

### TagKey
- **Type**: string
- **Pattern**: `^(?!aws:)[a-zA-Z+-=._:/]+$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `.{0,255}`
- **Min Length**: 0
- **Max Length**: 256

### TestingInformation
- **Type**: string
- **Pattern**: `^[\w\W\s\S]*$`
- **Max Length**: 1000

### TimestampUUID
- **Type**: string
- **Pattern**: `^[0-9]{10,13}_[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
- **Min Length**: 47
- **Max Length**: 50

### Token
- **Type**: string
- **Pattern**: `^[A-Za-z0-9+\/=]*$`
- **Min Length**: 1
- **Max Length**: 1000

### TroubleshootingText
- **Type**: string
- **Pattern**: `^[\w\W\s\S]*$`
- **Max Length**: 1000

### UUID
- **Type**: string
- **Pattern**: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
- **Min Length**: 36
- **Max Length**: 36

### UrlLink
- **Type**: string
- **Pattern**: `^(https?:\/\/)?(www\.)?[a-zA-Z0-9-_]+([\.]+[a-zA-Z]+)+[\/\w]*$`
- **Min Length**: 1
- **Max Length**: 8192

### Username
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_()\s\+=,.@]+$`
- **Min Length**: 1
- **Max Length**: 128

### organizationId
- **Type**: string
- **Pattern**: `o-[a-z0-9]{10,32}`
- **Min Length**: 12
- **Max Length**: 34

