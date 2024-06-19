# Iam Service

### CertificationKeyType
- **Type**: string
- **Pattern**: `[\u0020-\u00FF]+`
- **Min Length**: 1
- **Max Length**: 128

### CertificationValueType
- **Type**: string
- **Pattern**: `[\u0020-\u00FF]+`
- **Min Length**: 1
- **Max Length**: 32

### SAMLProviderNameType
- **Type**: string
- **Pattern**: `[\w._-]+`
- **Min Length**: 1
- **Max Length**: 128

### accessKeyIdType
- **Type**: string
- **Pattern**: `[\w]+`
- **Min Length**: 16
- **Max Length**: 128

### accountAliasType
- **Type**: string
- **Pattern**: `^[a-z0-9]([a-z0-9]|-(?!-)){1,61}[a-z0-9]$`
- **Min Length**: 3
- **Max Length**: 63

### authenticationCodeType
- **Type**: string
- **Pattern**: `[\d]+`
- **Min Length**: 6
- **Max Length**: 6

### certificateBodyType
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u00FF]+`
- **Min Length**: 1
- **Max Length**: 16384

### certificateChainType
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u00FF]+`
- **Min Length**: 1
- **Max Length**: 2097152

### certificateIdType
- **Type**: string
- **Pattern**: `[\w]+`
- **Min Length**: 24
- **Max Length**: 128

### customSuffixType
- **Type**: string
- **Pattern**: `[\w+=,.@-]+`
- **Min Length**: 1
- **Max Length**: 64

### entityNameType
- **Type**: string
- **Pattern**: `[\w+=,.@-]+`
- **Min Length**: 1
- **Max Length**: 128

### existingUserNameType
- **Type**: string
- **Pattern**: `[\w+=,.@-]+`
- **Min Length**: 1
- **Max Length**: 128

### groupNameType
- **Type**: string
- **Pattern**: `[\w+=,.@-]+`
- **Min Length**: 1
- **Max Length**: 128

### idType
- **Type**: string
- **Pattern**: `[\w]+`
- **Min Length**: 16
- **Max Length**: 128

### instanceProfileNameType
- **Type**: string
- **Pattern**: `[\w+=,.@-]+`
- **Min Length**: 1
- **Max Length**: 128

### markerType
- **Type**: string
- **Pattern**: `[\u0020-\u00FF]+`
- **Min Length**: 1
- **Max Length**: 320

### organizationsEntityPathType
- **Type**: string
- **Pattern**: `^o-[0-9a-z]{10,32}\/r-[0-9a-z]{4,32}[0-9a-z-\/]*`
- **Min Length**: 19
- **Max Length**: 427

### organizationsPolicyIdType
- **Type**: string
- **Pattern**: `^p-[0-9a-zA-Z_]{8,128}$`

### passwordType
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u00FF]+`
- **Min Length**: 1
- **Max Length**: 128

### pathPrefixType
- **Type**: string
- **Pattern**: `\u002F[\u0021-\u007F]*`
- **Min Length**: 1
- **Max Length**: 512

### pathType
- **Type**: string
- **Pattern**: `(\u002F)|(\u002F[\u0021-\u007E]+\u002F)`
- **Min Length**: 1
- **Max Length**: 512

### policyDocumentType
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u00FF]+`
- **Min Length**: 1
- **Max Length**: 131072

### policyNameType
- **Type**: string
- **Pattern**: `[\w+=,.@-]+`
- **Min Length**: 1
- **Max Length**: 128

### policyPathType
- **Type**: string
- **Pattern**: `((/[A-Za-z0-9\.,\+@=_-]+)*)/`
- **Min Length**: 1
- **Max Length**: 512

### policyVersionIdType
- **Type**: string
- **Pattern**: `v[1-9][0-9]*(\.[A-Za-z0-9-]*)?`

### privateKeyType
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u00FF]+`
- **Min Length**: 1
- **Max Length**: 16384

### publicKeyFingerprintType
- **Type**: string
- **Pattern**: `[:\w]+`
- **Min Length**: 48
- **Max Length**: 48

### publicKeyIdType
- **Type**: string
- **Pattern**: `[\w]+`
- **Min Length**: 20
- **Max Length**: 128

### publicKeyMaterialType
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u00FF]+`
- **Min Length**: 1
- **Max Length**: 16384

### roleDescriptionType
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u007E\u00A1-\u00FF]*`
- **Max Length**: 1000

### roleNameType
- **Type**: string
- **Pattern**: `[\w+=,.@-]+`
- **Min Length**: 1
- **Max Length**: 64

### serialNumberType
- **Type**: string
- **Pattern**: `[\w+=/:,.@-]+`
- **Min Length**: 9
- **Max Length**: 256

### serverCertificateNameType
- **Type**: string
- **Pattern**: `[\w+=,.@-]+`
- **Min Length**: 1
- **Max Length**: 128

### serviceNamespaceType
- **Type**: string
- **Pattern**: `[\w-]*`
- **Min Length**: 1
- **Max Length**: 64

### serviceSpecificCredentialId
- **Type**: string
- **Pattern**: `[\w]+`
- **Min Length**: 20
- **Max Length**: 128

### serviceUserName
- **Type**: string
- **Pattern**: `[\w+=,.@-]+`
- **Min Length**: 17
- **Max Length**: 200

### tagKeyType
- **Type**: string
- **Pattern**: `[\p{L}\p{Z}\p{N}_.:/=+\-@]+`
- **Min Length**: 1
- **Max Length**: 128

### tagValueType
- **Type**: string
- **Pattern**: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
- **Min Length**: 0
- **Max Length**: 256

### userNameType
- **Type**: string
- **Pattern**: `[\w+=,.@-]+`
- **Min Length**: 1
- **Max Length**: 64

### virtualMFADeviceName
- **Type**: string
- **Pattern**: `[\w+=,.@-]+`
- **Min Length**: 1

