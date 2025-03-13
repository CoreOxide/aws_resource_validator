# Cognitoidp Service

### AWSAccountIdType
- **Type**: string
- **Pattern**: `[0-9]+`
- **Max Length**: 12

### ArnType
- **Type**: string
- **Pattern**: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
- **Min Length**: 20
- **Max Length**: 2048

### AttributeNameType
- **Type**: string
- **Pattern**: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
- **Min Length**: 1
- **Max Length**: 32

### ClientIdType
- **Type**: string
- **Pattern**: `[\w+]+`
- **Min Length**: 1
- **Max Length**: 128

### ClientNameType
- **Type**: string
- **Pattern**: `[\w\s+=,.@-]+`
- **Min Length**: 1
- **Max Length**: 128

### ClientSecretType
- **Type**: string
- **Pattern**: `[\w+]+`
- **Min Length**: 1
- **Max Length**: 64

### CompletionMessageType
- **Type**: string
- **Pattern**: `[\w]+`
- **Min Length**: 1
- **Max Length**: 128

### ConfirmationCodeType
- **Type**: string
- **Pattern**: `[\S]+`
- **Min Length**: 1
- **Max Length**: 2048

### CustomAttributeNameType
- **Type**: string
- **Pattern**: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
- **Min Length**: 1
- **Max Length**: 20

### DeviceKeyType
- **Type**: string
- **Pattern**: `[\w-]+_[0-9a-f-]+`
- **Min Length**: 1
- **Max Length**: 55

### DomainType
- **Type**: string
- **Pattern**: `^[a-z0-9](?:[a-z0-9\-]{0,61}[a-z0-9])?$`
- **Min Length**: 1
- **Max Length**: 63

### EmailAddressType
- **Type**: string
- **Pattern**: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+@[\p{L}\p{M}\p{S}\p{N}\p{P}]+`

### EmailInviteMessageType
- **Type**: string
- **Pattern**: `[\p{L}\p{M}\p{S}\p{N}\p{P}\s*]*`
- **Min Length**: 6
- **Max Length**: 20000

### EmailMfaMessageType
- **Type**: string
- **Pattern**: `[\p{L}\p{M}\p{S}\p{N}\p{P}\s*]*\{####\}[\p{L}\p{M}\p{S}\p{N}\p{P}\s*]*`
- **Min Length**: 6
- **Max Length**: 20000

### EmailMfaSubjectType
- **Type**: string
- **Pattern**: `[\p{L}\p{M}\p{S}\p{N}\p{P}\s]+`

### EmailNotificationBodyType
- **Type**: string
- **Pattern**: `[\p{L}\p{M}\p{S}\p{N}\p{P}\s*]+`
- **Min Length**: 6
- **Max Length**: 20000

### EmailNotificationSubjectType
- **Type**: string
- **Pattern**: `[\p{L}\p{M}\p{S}\p{N}\p{P}\s]+`
- **Min Length**: 1
- **Max Length**: 140

### EmailVerificationMessageByLinkType
- **Type**: string
- **Pattern**: `[\p{L}\p{M}\p{S}\p{N}\p{P}\s*]*\{##[\p{L}\p{M}\p{S}\p{N}\p{P}\s*]*##\}[\p{L}\p{M}\p{S}\p{N}\p{P}\s*]*`
- **Min Length**: 6
- **Max Length**: 20000

### EmailVerificationMessageType
- **Type**: string
- **Pattern**: `[\p{L}\p{M}\p{S}\p{N}\p{P}\s*]*\{####\}[\p{L}\p{M}\p{S}\p{N}\p{P}\s*]*`
- **Min Length**: 6
- **Max Length**: 20000

### EmailVerificationSubjectByLinkType
- **Type**: string
- **Pattern**: `[\p{L}\p{M}\p{S}\p{N}\p{P}\s]+`
- **Min Length**: 1
- **Max Length**: 140

### EmailVerificationSubjectType
- **Type**: string
- **Pattern**: `[\p{L}\p{M}\p{S}\p{N}\p{P}\s]+`
- **Min Length**: 1
- **Max Length**: 140

### EventIdType
- **Type**: string
- **Pattern**: `[\w+-]+`
- **Min Length**: 1
- **Max Length**: 50

### GroupNameType
- **Type**: string
- **Pattern**: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
- **Min Length**: 1
- **Max Length**: 128

### HexStringType
- **Type**: string
- **Pattern**: `^[0-9a-fA-F]+$`

### IdpIdentifierType
- **Type**: string
- **Pattern**: `[\w\s+=.@-]+`
- **Min Length**: 1
- **Max Length**: 40

### ManagedLoginBrandingIdType
- **Type**: string
- **Pattern**: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[4][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$`

### PaginationKey
- **Type**: string
- **Pattern**: `[\S]+`
- **Min Length**: 1
- **Max Length**: 131072

### PaginationKeyType
- **Type**: string
- **Pattern**: `[\S]+`
- **Min Length**: 1

### PasswordType
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 256

### ProviderNameType
- **Type**: string
- **Pattern**: `[\p{L}\p{M}\p{S}\p{N}\p{P}\p{Z}]+`
- **Min Length**: 1
- **Max Length**: 32

### ProviderNameTypeV2
- **Type**: string
- **Pattern**: `[^_\p{Z}][\p{L}\p{M}\p{S}\p{N}\p{P}][^_\p{Z}]+`
- **Min Length**: 1
- **Max Length**: 32

### RedirectUrlType
- **Type**: string
- **Pattern**: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
- **Min Length**: 1
- **Max Length**: 1024

### ResourceIdType
- **Type**: string
- **Pattern**: `^[\w\- ]+$`
- **Min Length**: 1
- **Max Length**: 40

### ResourceServerIdentifierType
- **Type**: string
- **Pattern**: `[\x21\x23-\x5B\x5D-\x7E]+`
- **Min Length**: 1
- **Max Length**: 256

### ResourceServerNameType
- **Type**: string
- **Pattern**: `[\w\s+=,.@-]+`
- **Min Length**: 1
- **Max Length**: 256

### ResourceServerScopeNameType
- **Type**: string
- **Pattern**: `[\x21\x23-\x2E\x30-\x5B\x5D-\x7E]+`
- **Min Length**: 1
- **Max Length**: 256

### S3ArnType
- **Type**: string
- **Pattern**: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:::[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
- **Min Length**: 3
- **Max Length**: 1024

### S3BucketType
- **Type**: string
- **Pattern**: `^[0-9A-Za-z\.\-_]*(?<!\.)$`
- **Min Length**: 3
- **Max Length**: 1024

### SESConfigurationSet
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_-]+$`
- **Min Length**: 1
- **Max Length**: 64

### ScopeType
- **Type**: string
- **Pattern**: `[\x21\x23-\x5B\x5D-\x7E]+`
- **Min Length**: 1
- **Max Length**: 256

### SearchPaginationTokenType
- **Type**: string
- **Pattern**: `[\S]+`
- **Min Length**: 1

### SecretCodeType
- **Type**: string
- **Pattern**: `[A-Za-z0-9]+`
- **Min Length**: 16

### SecretHashType
- **Type**: string
- **Pattern**: `[\w+=/]+`
- **Min Length**: 1
- **Max Length**: 128

### SmsInviteMessageType
- **Type**: string
- **Pattern**: `(?s).*`
- **Min Length**: 6
- **Max Length**: 140

### SmsVerificationMessageType
- **Type**: string
- **Pattern**: `.*\{####\}.*`
- **Min Length**: 6
- **Max Length**: 140

### SoftwareTokenMFAUserCodeType
- **Type**: string
- **Pattern**: `[0-9]+`
- **Min Length**: 6
- **Max Length**: 6

### TokenModelType
- **Type**: string
- **Pattern**: `[A-Za-z0-9-_=.]+`

### UserImportJobIdType
- **Type**: string
- **Pattern**: `import-[0-9a-zA-Z-]+`
- **Min Length**: 1
- **Max Length**: 55

### UserImportJobNameType
- **Type**: string
- **Pattern**: `[\w\s+=,.@-]+`
- **Min Length**: 1
- **Max Length**: 128

### UserPoolIdType
- **Type**: string
- **Pattern**: `[\w-]+_[0-9a-zA-Z]+`
- **Min Length**: 1
- **Max Length**: 55

### UserPoolNameType
- **Type**: string
- **Pattern**: `[\w\s+=,.@-]+`
- **Min Length**: 1
- **Max Length**: 128

### UsernameType
- **Type**: string
- **Pattern**: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
- **Min Length**: 1
- **Max Length**: 128

