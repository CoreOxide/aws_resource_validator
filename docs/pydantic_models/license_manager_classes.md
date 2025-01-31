# License Manager Classes

# AcceptGrantRequestRequestTypeDef

### GrantArn
- **Type**: <class 'str'>
- **Required**: Yes


# AcceptGrantResponseTypeDef

### GrantArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'DISABLED', 'FAILED_WORKFLOW', 'PENDING_ACCEPT', 'PENDING_DELETE', 'PENDING_WORKFLOW', 'REJECTED', 'WORKFLOW_COMPLETED']
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AutomatedDiscoveryInformationTypeDef

### LastRunTime
- **Type**: typing.Optional[datetime.datetime]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BorrowConfigurationTypeDef

### AllowEarlyCheckIn
- **Type**: <class 'bool'>
- **Required**: Yes

### MaxTimeToLiveInMinutes
- **Type**: <class 'int'>
- **Required**: Yes


# CheckInLicenseRequestRequestTypeDef

### LicenseConsumptionToken
- **Type**: <class 'str'>
- **Required**: Yes

### Beneficiary
- **Type**: typing.Optional[str]


# CheckoutBorrowLicenseRequestRequestTypeDef

### LicenseArn
- **Type**: <class 'str'>
- **Required**: Yes

### Entitlements
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.EntitlementDataTypeDef]
- **Required**: Yes

### DigitalSignatureMethod
- **Type**: typing.Literal['JWT_PS384']
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### NodeId
- **Type**: typing.Optional[str]

### CheckoutMetadata
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.MetadataTypeDef]]


# CheckoutBorrowLicenseResponseTypeDef

### LicenseArn
- **Type**: <class 'str'>
- **Required**: Yes

### LicenseConsumptionToken
- **Type**: <class 'str'>
- **Required**: Yes

### EntitlementsAllowed
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.EntitlementDataTypeDef]
- **Required**: Yes

### NodeId
- **Type**: <class 'str'>
- **Required**: Yes

### SignedToken
- **Type**: <class 'str'>
- **Required**: Yes

### IssuedAt
- **Type**: <class 'str'>
- **Required**: Yes

### Expiration
- **Type**: <class 'str'>
- **Required**: Yes

### CheckoutMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.MetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CheckoutLicenseRequestRequestTypeDef

### ProductSKU
- **Type**: <class 'str'>
- **Required**: Yes

### CheckoutType
- **Type**: typing.Literal['PERPETUAL', 'PROVISIONAL']
- **Required**: Yes

### KeyFingerprint
- **Type**: <class 'str'>
- **Required**: Yes

### Entitlements
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.EntitlementDataTypeDef]
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### Beneficiary
- **Type**: typing.Optional[str]

### NodeId
- **Type**: typing.Optional[str]


# CheckoutLicenseResponseTypeDef

### CheckoutType
- **Type**: typing.Literal['PERPETUAL', 'PROVISIONAL']
- **Required**: Yes

### LicenseConsumptionToken
- **Type**: <class 'str'>
- **Required**: Yes

### EntitlementsAllowed
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.EntitlementDataTypeDef]
- **Required**: Yes

### SignedToken
- **Type**: <class 'str'>
- **Required**: Yes

### NodeId
- **Type**: <class 'str'>
- **Required**: Yes

### IssuedAt
- **Type**: <class 'str'>
- **Required**: Yes

### Expiration
- **Type**: <class 'str'>
- **Required**: Yes

### LicenseArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ConsumedLicenseSummaryTypeDef

### ResourceType
- **Type**: typing.Optional[typing.Literal['EC2_AMI', 'EC2_HOST', 'EC2_INSTANCE', 'RDS', 'SYSTEMS_MANAGER_MANAGED_INSTANCE']]

### ConsumedLicenses
- **Type**: typing.Optional[int]


# ConsumptionConfigurationTypeDef

### RenewType
- **Type**: typing.Optional[typing.Literal['Monthly', 'None', 'Weekly']]

### ProvisionalConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.ProvisionalConfigurationTypeDef]

### BorrowConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.BorrowConfigurationTypeDef]


# CreateGrantRequestRequestTypeDef

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### GrantName
- **Type**: <class 'str'>
- **Required**: Yes

### LicenseArn
- **Type**: <class 'str'>
- **Required**: Yes

### Principals
- **Type**: typing.Sequence[str]
- **Required**: Yes

### HomeRegion
- **Type**: <class 'str'>
- **Required**: Yes

### AllowedOperations
- **Type**: typing.Sequence[typing.Literal['CheckInLicense', 'CheckoutBorrowLicense', 'CheckoutLicense', 'CreateGrant', 'CreateToken', 'ExtendConsumptionLicense', 'ListPurchasedLicenses']]
- **Required**: Yes


# CreateGrantResponseTypeDef

### GrantArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'DISABLED', 'FAILED_WORKFLOW', 'PENDING_ACCEPT', 'PENDING_DELETE', 'PENDING_WORKFLOW', 'REJECTED', 'WORKFLOW_COMPLETED']
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGrantVersionRequestRequestTypeDef

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### GrantArn
- **Type**: <class 'str'>
- **Required**: Yes

### GrantName
- **Type**: typing.Optional[str]

### AllowedOperations
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CheckInLicense', 'CheckoutBorrowLicense', 'CheckoutLicense', 'CreateGrant', 'CreateToken', 'ExtendConsumptionLicense', 'ListPurchasedLicenses']]]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED', 'DISABLED', 'FAILED_WORKFLOW', 'PENDING_ACCEPT', 'PENDING_DELETE', 'PENDING_WORKFLOW', 'REJECTED', 'WORKFLOW_COMPLETED']]

### StatusReason
- **Type**: typing.Optional[str]

### SourceVersion
- **Type**: typing.Optional[str]

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.OptionsTypeDef]


# CreateGrantVersionResponseTypeDef

### GrantArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'DISABLED', 'FAILED_WORKFLOW', 'PENDING_ACCEPT', 'PENDING_DELETE', 'PENDING_WORKFLOW', 'REJECTED', 'WORKFLOW_COMPLETED']
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLicenseConfigurationRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### LicenseCountingType
- **Type**: typing.Literal['Core', 'Instance', 'Socket', 'vCPU']
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### LicenseCount
- **Type**: typing.Optional[int]

### LicenseCountHardLimit
- **Type**: typing.Optional[bool]

### LicenseRules
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.TagTypeDef]]

### DisassociateWhenNotFound
- **Type**: typing.Optional[bool]

### ProductInformationList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.ProductInformationTypeDef]]


# CreateLicenseConfigurationResponseTypeDef

### LicenseConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLicenseConversionTaskForResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceLicenseContext
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.LicenseConversionContextTypeDef'>
- **Required**: Yes

### DestinationLicenseContext
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.LicenseConversionContextTypeDef'>
- **Required**: Yes


# CreateLicenseConversionTaskForResourceResponseTypeDef

### LicenseConversionTaskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLicenseManagerReportGeneratorRequestRequestTypeDef

### ReportGeneratorName
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Sequence[typing.Literal['LicenseConfigurationSummaryReport', 'LicenseConfigurationUsageReport']]
- **Required**: Yes

### ReportContext
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ReportContextTypeDef'>
- **Required**: Yes

### ReportFrequency
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ReportFrequencyTypeDef'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.TagTypeDef]]


# CreateLicenseManagerReportGeneratorResponseTypeDef

### LicenseManagerReportGeneratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLicenseRequestRequestTypeDef

### LicenseName
- **Type**: <class 'str'>
- **Required**: Yes

### ProductName
- **Type**: <class 'str'>
- **Required**: Yes

### ProductSKU
- **Type**: <class 'str'>
- **Required**: Yes

### Issuer
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.IssuerTypeDef'>
- **Required**: Yes

### HomeRegion
- **Type**: <class 'str'>
- **Required**: Yes

### Validity
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.DatetimeRangeTypeDef'>
- **Required**: Yes

### Entitlements
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.EntitlementTypeDef]
- **Required**: Yes

### Beneficiary
- **Type**: <class 'str'>
- **Required**: Yes

### ConsumptionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ConsumptionConfigurationTypeDef'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### LicenseMetadata
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.MetadataTypeDef]]


# CreateLicenseResponseTypeDef

### LicenseArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['AVAILABLE', 'DEACTIVATED', 'DELETED', 'EXPIRED', 'PENDING_AVAILABLE', 'PENDING_DELETE', 'SUSPENDED']
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLicenseVersionRequestRequestTypeDef

### LicenseArn
- **Type**: <class 'str'>
- **Required**: Yes

### LicenseName
- **Type**: <class 'str'>
- **Required**: Yes

### ProductName
- **Type**: <class 'str'>
- **Required**: Yes

### Issuer
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.IssuerTypeDef'>
- **Required**: Yes

### HomeRegion
- **Type**: <class 'str'>
- **Required**: Yes

### Validity
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.DatetimeRangeTypeDef'>
- **Required**: Yes

### Entitlements
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.EntitlementTypeDef]
- **Required**: Yes

### ConsumptionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ConsumptionConfigurationTypeDef'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['AVAILABLE', 'DEACTIVATED', 'DELETED', 'EXPIRED', 'PENDING_AVAILABLE', 'PENDING_DELETE', 'SUSPENDED']
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### LicenseMetadata
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.MetadataTypeDef]]

### SourceVersion
- **Type**: typing.Optional[str]


# CreateLicenseVersionResponseTypeDef

### LicenseArn
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['AVAILABLE', 'DEACTIVATED', 'DELETED', 'EXPIRED', 'PENDING_AVAILABLE', 'PENDING_DELETE', 'SUSPENDED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTokenRequestRequestTypeDef

### LicenseArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArns
- **Type**: typing.Optional[typing.Sequence[str]]

### ExpirationInDays
- **Type**: typing.Optional[int]

### TokenProperties
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateTokenResponseTypeDef

### TokenId
- **Type**: <class 'str'>
- **Required**: Yes

### TokenType
- **Type**: typing.Literal['REFRESH_TOKEN']
- **Required**: Yes

### Token
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DatetimeRangeTypeDef

### Begin
- **Type**: <class 'str'>
- **Required**: Yes

### End
- **Type**: typing.Optional[str]


# DeleteGrantRequestRequestTypeDef

### GrantArn
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### StatusReason
- **Type**: typing.Optional[str]


# DeleteGrantResponseTypeDef

### GrantArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'DISABLED', 'FAILED_WORKFLOW', 'PENDING_ACCEPT', 'PENDING_DELETE', 'PENDING_WORKFLOW', 'REJECTED', 'WORKFLOW_COMPLETED']
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteLicenseConfigurationRequestRequestTypeDef

### LicenseConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLicenseManagerReportGeneratorRequestRequestTypeDef

### LicenseManagerReportGeneratorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLicenseRequestRequestTypeDef

### LicenseArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceVersion
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLicenseResponseTypeDef

### Status
- **Type**: typing.Literal['DELETED', 'PENDING_DELETE']
- **Required**: Yes

### DeletionDate
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteTokenRequestRequestTypeDef

### TokenId
- **Type**: <class 'str'>
- **Required**: Yes


# EntitlementDataTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Unit
- **Type**: typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# EntitlementTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Unit
- **Type**: typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]

### MaxCount
- **Type**: typing.Optional[int]

### Overage
- **Type**: typing.Optional[bool]

### AllowCheckIn
- **Type**: typing.Optional[bool]


# EntitlementUsageTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ConsumedValue
- **Type**: <class 'str'>
- **Required**: Yes

### Unit
- **Type**: typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']
- **Required**: Yes

### MaxCount
- **Type**: typing.Optional[str]


# ExtendLicenseConsumptionRequestRequestTypeDef

### LicenseConsumptionToken
- **Type**: <class 'str'>
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# ExtendLicenseConsumptionResponseTypeDef

### LicenseConsumptionToken
- **Type**: <class 'str'>
- **Required**: Yes

### Expiration
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FilterTypeDef

### Name
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# GetAccessTokenRequestRequestTypeDef

### Token
- **Type**: <class 'str'>
- **Required**: Yes

### TokenProperties
- **Type**: typing.Optional[typing.Sequence[str]]


# GetAccessTokenResponseTypeDef

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGrantRequestRequestTypeDef

### GrantArn
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]


# GetGrantResponseTypeDef

### Grant
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.GrantTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLicenseConfigurationRequestRequestTypeDef

### LicenseConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetLicenseConfigurationResponseTypeDef

### LicenseConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### LicenseConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### LicenseCountingType
- **Type**: typing.Literal['Core', 'Instance', 'Socket', 'vCPU']
- **Required**: Yes

### LicenseRules
- **Type**: typing.List[str]
- **Required**: Yes

### LicenseCount
- **Type**: <class 'int'>
- **Required**: Yes

### LicenseCountHardLimit
- **Type**: <class 'bool'>
- **Required**: Yes

### ConsumedLicenses
- **Type**: <class 'int'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### OwnerAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ConsumedLicenseSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.ConsumedLicenseSummaryTypeDef]
- **Required**: Yes

### ManagedResourceSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.ManagedResourceSummaryTypeDef]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.TagTypeDef]
- **Required**: Yes

### ProductInformationList
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.ProductInformationTypeDef]
- **Required**: Yes

### AutomatedDiscoveryInformation
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.AutomatedDiscoveryInformationTypeDef'>
- **Required**: Yes

### DisassociateWhenNotFound
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLicenseConversionTaskRequestRequestTypeDef

### LicenseConversionTaskId
- **Type**: <class 'str'>
- **Required**: Yes


# GetLicenseConversionTaskResponseTypeDef

### LicenseConversionTaskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceLicenseContext
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.LicenseConversionContextTypeDef'>
- **Required**: Yes

### DestinationLicenseContext
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.LicenseConversionContextTypeDef'>
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LicenseConversionTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLicenseManagerReportGeneratorRequestRequestTypeDef

### LicenseManagerReportGeneratorArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetLicenseManagerReportGeneratorResponseTypeDef

### ReportGenerator
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ReportGeneratorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLicenseRequestRequestTypeDef

### LicenseArn
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]


# GetLicenseResponseTypeDef

### License
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.LicenseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLicenseUsageRequestRequestTypeDef

### LicenseArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetLicenseUsageResponseTypeDef

### LicenseUsage
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.LicenseUsageTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetServiceSettingsResponseTypeDef

### S3BucketArn
- **Type**: <class 'str'>
- **Required**: Yes

### SnsTopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.OrganizationConfigurationTypeDef'>
- **Required**: Yes

### EnableCrossAccountsDiscovery
- **Type**: <class 'bool'>
- **Required**: Yes

### LicenseManagerResourceShareArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GrantTypeDef

### GrantArn
- **Type**: <class 'str'>
- **Required**: Yes

### GrantName
- **Type**: <class 'str'>
- **Required**: Yes

### ParentArn
- **Type**: <class 'str'>
- **Required**: Yes

### LicenseArn
- **Type**: <class 'str'>
- **Required**: Yes

### GranteePrincipalArn
- **Type**: <class 'str'>
- **Required**: Yes

### HomeRegion
- **Type**: <class 'str'>
- **Required**: Yes

### GrantStatus
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'DISABLED', 'FAILED_WORKFLOW', 'PENDING_ACCEPT', 'PENDING_DELETE', 'PENDING_WORKFLOW', 'REJECTED', 'WORKFLOW_COMPLETED']
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### GrantedOperations
- **Type**: typing.List[typing.Literal['CheckInLicense', 'CheckoutBorrowLicense', 'CheckoutLicense', 'CreateGrant', 'CreateToken', 'ExtendConsumptionLicense', 'ListPurchasedLicenses']]
- **Required**: Yes

### StatusReason
- **Type**: typing.Optional[str]

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.OptionsTypeDef]


# GrantedLicenseTypeDef

### LicenseArn
- **Type**: typing.Optional[str]

### LicenseName
- **Type**: typing.Optional[str]

### ProductName
- **Type**: typing.Optional[str]

### ProductSKU
- **Type**: typing.Optional[str]

### Issuer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.IssuerDetailsTypeDef]

### HomeRegion
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DEACTIVATED', 'DELETED', 'EXPIRED', 'PENDING_AVAILABLE', 'PENDING_DELETE', 'SUSPENDED']]

### Validity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.DatetimeRangeTypeDef]

### Beneficiary
- **Type**: typing.Optional[str]

### Entitlements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_classes.EntitlementTypeDef]]

### ConsumptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.ConsumptionConfigurationTypeDef]

### LicenseMetadata
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_classes.MetadataTypeDef]]

### CreateTime
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### ReceivedMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.ReceivedMetadataTypeDef]


# InventoryFilterTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Condition
- **Type**: typing.Literal['BEGINS_WITH', 'CONTAINS', 'EQUALS', 'NOT_EQUALS']
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# IssuerDetailsTypeDef

### Name
- **Type**: typing.Optional[str]

### SignKey
- **Type**: typing.Optional[str]

### KeyFingerprint
- **Type**: typing.Optional[str]


# IssuerTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SignKey
- **Type**: typing.Optional[str]


# LicenseConfigurationAssociationTypeDef

### ResourceArn
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[typing.Literal['EC2_AMI', 'EC2_HOST', 'EC2_INSTANCE', 'RDS', 'SYSTEMS_MANAGER_MANAGED_INSTANCE']]

### ResourceOwnerId
- **Type**: typing.Optional[str]

### AssociationTime
- **Type**: typing.Optional[datetime.datetime]

### AmiAssociationScope
- **Type**: typing.Optional[str]


# LicenseConfigurationPaginatorTypeDef

### LicenseConfigurationId
- **Type**: typing.Optional[str]

### LicenseConfigurationArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### LicenseCountingType
- **Type**: typing.Optional[typing.Literal['Core', 'Instance', 'Socket', 'vCPU']]

### LicenseRules
- **Type**: typing.Optional[typing.List[str]]

### LicenseCount
- **Type**: typing.Optional[int]

### LicenseCountHardLimit
- **Type**: typing.Optional[bool]

### DisassociateWhenNotFound
- **Type**: typing.Optional[bool]

### ConsumedLicenses
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[str]

### OwnerAccountId
- **Type**: typing.Optional[str]

### ConsumedLicenseSummaryList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_classes.ConsumedLicenseSummaryTypeDef]]

### ManagedResourceSummaryList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_classes.ManagedResourceSummaryTypeDef]]

### ProductInformationList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_classes.ProductInformationPaginatorTypeDef]]

### AutomatedDiscoveryInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.AutomatedDiscoveryInformationTypeDef]


# LicenseConfigurationTypeDef

### LicenseConfigurationId
- **Type**: typing.Optional[str]

### LicenseConfigurationArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### LicenseCountingType
- **Type**: typing.Optional[typing.Literal['Core', 'Instance', 'Socket', 'vCPU']]

### LicenseRules
- **Type**: typing.Optional[typing.List[str]]

### LicenseCount
- **Type**: typing.Optional[int]

### LicenseCountHardLimit
- **Type**: typing.Optional[bool]

### DisassociateWhenNotFound
- **Type**: typing.Optional[bool]

### ConsumedLicenses
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[str]

### OwnerAccountId
- **Type**: typing.Optional[str]

### ConsumedLicenseSummaryList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_classes.ConsumedLicenseSummaryTypeDef]]

### ManagedResourceSummaryList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_classes.ManagedResourceSummaryTypeDef]]

### ProductInformationList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_classes.ProductInformationTypeDef]]

### AutomatedDiscoveryInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.AutomatedDiscoveryInformationTypeDef]


# LicenseConfigurationUsageTypeDef

### ResourceArn
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[typing.Literal['EC2_AMI', 'EC2_HOST', 'EC2_INSTANCE', 'RDS', 'SYSTEMS_MANAGER_MANAGED_INSTANCE']]

### ResourceStatus
- **Type**: typing.Optional[str]

### ResourceOwnerId
- **Type**: typing.Optional[str]

### AssociationTime
- **Type**: typing.Optional[datetime.datetime]

### ConsumedLicenses
- **Type**: typing.Optional[int]


# LicenseConversionContextTypeDef

### UsageOperation
- **Type**: typing.Optional[str]


# LicenseConversionTaskTypeDef

### LicenseConversionTaskId
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### SourceLicenseContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.LicenseConversionContextTypeDef]

### DestinationLicenseContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.LicenseConversionContextTypeDef]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']]

### StatusMessage
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### LicenseConversionTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]


# LicenseOperationFailureTypeDef

### ResourceArn
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[typing.Literal['EC2_AMI', 'EC2_HOST', 'EC2_INSTANCE', 'RDS', 'SYSTEMS_MANAGER_MANAGED_INSTANCE']]

### ErrorMessage
- **Type**: typing.Optional[str]

### FailureTime
- **Type**: typing.Optional[datetime.datetime]

### OperationName
- **Type**: typing.Optional[str]

### ResourceOwnerId
- **Type**: typing.Optional[str]

### OperationRequestedBy
- **Type**: typing.Optional[str]

### MetadataList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_classes.MetadataTypeDef]]


# LicenseSpecificationTypeDef

### LicenseConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### AmiAssociationScope
- **Type**: typing.Optional[str]


# LicenseTypeDef

### LicenseArn
- **Type**: typing.Optional[str]

### LicenseName
- **Type**: typing.Optional[str]

### ProductName
- **Type**: typing.Optional[str]

### ProductSKU
- **Type**: typing.Optional[str]

### Issuer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.IssuerDetailsTypeDef]

### HomeRegion
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DEACTIVATED', 'DELETED', 'EXPIRED', 'PENDING_AVAILABLE', 'PENDING_DELETE', 'SUSPENDED']]

### Validity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.DatetimeRangeTypeDef]

### Beneficiary
- **Type**: typing.Optional[str]

### Entitlements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_classes.EntitlementTypeDef]]

### ConsumptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.ConsumptionConfigurationTypeDef]

### LicenseMetadata
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_classes.MetadataTypeDef]]

### CreateTime
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# LicenseUsageTypeDef

### EntitlementUsages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_classes.EntitlementUsageTypeDef]]


# ListAssociationsForLicenseConfigurationRequestListAssociationsForLicenseConfigurationPaginateTypeDef

### LicenseConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.PaginatorConfigTypeDef]


# ListAssociationsForLicenseConfigurationRequestRequestTypeDef

### LicenseConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAssociationsForLicenseConfigurationResponseTypeDef

### LicenseConfigurationAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.LicenseConfigurationAssociationTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDistributedGrantsRequestRequestTypeDef

### GrantArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.FilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDistributedGrantsResponseTypeDef

### Grants
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.GrantTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFailuresForLicenseConfigurationOperationsRequestRequestTypeDef

### LicenseConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListFailuresForLicenseConfigurationOperationsResponseTypeDef

### LicenseOperationFailureList
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.LicenseOperationFailureTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLicenseConfigurationsRequestListLicenseConfigurationsPaginateTypeDef

### LicenseConfigurationArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.PaginatorConfigTypeDef]


# ListLicenseConfigurationsRequestRequestTypeDef

### LicenseConfigurationArns
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.FilterTypeDef]]


# ListLicenseConfigurationsResponsePaginatorTypeDef

### LicenseConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.LicenseConfigurationPaginatorTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLicenseConfigurationsResponseTypeDef

### LicenseConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.LicenseConfigurationTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLicenseConversionTasksRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.FilterTypeDef]]


# ListLicenseConversionTasksResponseTypeDef

### LicenseConversionTasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.LicenseConversionTaskTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLicenseManagerReportGeneratorsRequestRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.FilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListLicenseManagerReportGeneratorsResponseTypeDef

### ReportGenerators
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.ReportGeneratorTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLicenseSpecificationsForResourceRequestListLicenseSpecificationsForResourcePaginateTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.PaginatorConfigTypeDef]


# ListLicenseSpecificationsForResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListLicenseSpecificationsForResourceResponseTypeDef

### LicenseSpecifications
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.LicenseSpecificationTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLicenseVersionsRequestRequestTypeDef

### LicenseArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListLicenseVersionsResponseTypeDef

### Licenses
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.LicenseTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLicensesRequestRequestTypeDef

### LicenseArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.FilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListLicensesResponseTypeDef

### Licenses
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.LicenseTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListReceivedGrantsForOrganizationRequestRequestTypeDef

### LicenseArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.FilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListReceivedGrantsForOrganizationResponseTypeDef

### Grants
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.GrantTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListReceivedGrantsRequestRequestTypeDef

### GrantArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.FilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListReceivedGrantsResponseTypeDef

### Grants
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.GrantTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListReceivedLicensesForOrganizationRequestRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.FilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListReceivedLicensesForOrganizationResponseTypeDef

### Licenses
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.GrantedLicenseTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListReceivedLicensesRequestRequestTypeDef

### LicenseArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.FilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListReceivedLicensesResponseTypeDef

### Licenses
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.GrantedLicenseTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListResourceInventoryRequestListResourceInventoryPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.InventoryFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.PaginatorConfigTypeDef]


# ListResourceInventoryRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.InventoryFilterTypeDef]]


# ListResourceInventoryResponseTypeDef

### ResourceInventoryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.ResourceInventoryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTokensRequestRequestTypeDef

### TokenIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.FilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTokensResponseTypeDef

### Tokens
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.TokenDataTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListUsageForLicenseConfigurationRequestListUsageForLicenseConfigurationPaginateTypeDef

### LicenseConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.PaginatorConfigTypeDef]


# ListUsageForLicenseConfigurationRequestRequestTypeDef

### LicenseConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.FilterTypeDef]]


# ListUsageForLicenseConfigurationResponseTypeDef

### LicenseConfigurationUsageList
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.LicenseConfigurationUsageTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ManagedResourceSummaryTypeDef

### ResourceType
- **Type**: typing.Optional[typing.Literal['EC2_AMI', 'EC2_HOST', 'EC2_INSTANCE', 'RDS', 'SYSTEMS_MANAGER_MANAGED_INSTANCE']]

### AssociationCount
- **Type**: typing.Optional[int]


# MetadataTypeDef

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# OptionsTypeDef

### ActivationOverrideBehavior
- **Type**: typing.Optional[typing.Literal['ALL_GRANTS_PERMITTED_BY_ISSUER', 'DISTRIBUTED_GRANTS_ONLY']]


# OrganizationConfigurationTypeDef

### EnableIntegration
- **Type**: <class 'bool'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProductInformationFilterPaginatorTypeDef

### ProductInformationFilterName
- **Type**: <class 'str'>
- **Required**: Yes

### ProductInformationFilterComparator
- **Type**: <class 'str'>
- **Required**: Yes

### ProductInformationFilterValue
- **Type**: typing.Optional[typing.List[str]]


# ProductInformationFilterTypeDef

### ProductInformationFilterName
- **Type**: <class 'str'>
- **Required**: Yes

### ProductInformationFilterComparator
- **Type**: <class 'str'>
- **Required**: Yes

### ProductInformationFilterValue
- **Type**: typing.Optional[typing.Sequence[str]]


# ProductInformationPaginatorTypeDef

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### ProductInformationFilterList
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.ProductInformationFilterPaginatorTypeDef]
- **Required**: Yes


# ProductInformationTypeDef

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### ProductInformationFilterList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.ProductInformationFilterTypeDef]
- **Required**: Yes


# ProvisionalConfigurationTypeDef

### MaxTimeToLiveInMinutes
- **Type**: <class 'int'>
- **Required**: Yes


# ReceivedMetadataTypeDef

### ReceivedStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED', 'DISABLED', 'FAILED_WORKFLOW', 'PENDING_ACCEPT', 'PENDING_WORKFLOW', 'REJECTED', 'WORKFLOW_COMPLETED']]

### ReceivedStatusReason
- **Type**: typing.Optional[str]

### AllowedOperations
- **Type**: typing.Optional[typing.List[typing.Literal['CheckInLicense', 'CheckoutBorrowLicense', 'CheckoutLicense', 'CreateGrant', 'CreateToken', 'ExtendConsumptionLicense', 'ListPurchasedLicenses']]]


# RejectGrantRequestRequestTypeDef

### GrantArn
- **Type**: <class 'str'>
- **Required**: Yes


# RejectGrantResponseTypeDef

### GrantArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'DISABLED', 'FAILED_WORKFLOW', 'PENDING_ACCEPT', 'PENDING_DELETE', 'PENDING_WORKFLOW', 'REJECTED', 'WORKFLOW_COMPLETED']
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReportContextTypeDef

### licenseConfigurationArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ReportFrequencyTypeDef

### value
- **Type**: typing.Optional[int]

### period
- **Type**: typing.Optional[typing.Literal['DAY', 'MONTH', 'WEEK']]


# ReportGeneratorTypeDef

### ReportGeneratorName
- **Type**: typing.Optional[str]

### ReportType
- **Type**: typing.Optional[typing.List[typing.Literal['LicenseConfigurationSummaryReport', 'LicenseConfigurationUsageReport']]]

### ReportContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.ReportContextTypeDef]

### ReportFrequency
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.ReportFrequencyTypeDef]

### LicenseManagerReportGeneratorArn
- **Type**: typing.Optional[str]

### LastRunStatus
- **Type**: typing.Optional[str]

### LastRunFailureReason
- **Type**: typing.Optional[str]

### LastReportGenerationTime
- **Type**: typing.Optional[str]

### ReportCreatorAccount
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### S3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.S3LocationTypeDef]

### CreateTime
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_classes.TagTypeDef]]


# ResourceInventoryTypeDef

### ResourceId
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[typing.Literal['EC2_AMI', 'EC2_HOST', 'EC2_INSTANCE', 'RDS', 'SYSTEMS_MANAGER_MANAGED_INSTANCE']]

### ResourceArn
- **Type**: typing.Optional[str]

### Platform
- **Type**: typing.Optional[str]

### PlatformVersion
- **Type**: typing.Optional[str]

### ResourceOwningAccountId
- **Type**: typing.Optional[str]


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HostId
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


# S3LocationTypeDef

### bucket
- **Type**: typing.Optional[str]

### keyPrefix
- **Type**: typing.Optional[str]


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TokenDataTypeDef

### TokenId
- **Type**: typing.Optional[str]

### TokenType
- **Type**: typing.Optional[str]

### LicenseArn
- **Type**: typing.Optional[str]

### ExpirationTime
- **Type**: typing.Optional[str]

### TokenProperties
- **Type**: typing.Optional[typing.List[str]]

### RoleArns
- **Type**: typing.Optional[typing.List[str]]

### Status
- **Type**: typing.Optional[str]


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateLicenseConfigurationRequestRequestTypeDef

### LicenseConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### LicenseConfigurationStatus
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DISABLED']]

### LicenseRules
- **Type**: typing.Optional[typing.Sequence[str]]

### LicenseCount
- **Type**: typing.Optional[int]

### LicenseCountHardLimit
- **Type**: typing.Optional[bool]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ProductInformationList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.ProductInformationTypeDef]]

### DisassociateWhenNotFound
- **Type**: typing.Optional[bool]


# UpdateLicenseManagerReportGeneratorRequestRequestTypeDef

### LicenseManagerReportGeneratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ReportGeneratorName
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Sequence[typing.Literal['LicenseConfigurationSummaryReport', 'LicenseConfigurationUsageReport']]
- **Required**: Yes

### ReportContext
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ReportContextTypeDef'>
- **Required**: Yes

### ReportFrequency
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ReportFrequencyTypeDef'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateLicenseSpecificationsForResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### AddLicenseSpecifications
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.LicenseSpecificationTypeDef]]

### RemoveLicenseSpecifications
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.LicenseSpecificationTypeDef]]


# UpdateServiceSettingsRequestRequestTypeDef

### S3BucketArn
- **Type**: typing.Optional[str]

### SnsTopicArn
- **Type**: typing.Optional[str]

### OrganizationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.OrganizationConfigurationTypeDef]

### EnableCrossAccountsDiscovery
- **Type**: typing.Optional[bool]


