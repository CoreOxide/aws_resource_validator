# License Manager Classes

# AcceptGrantRequest

### GrantArn
- **Type**: <class 'str'>
- **Required**: Yes


# AcceptGrantResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes


# AutomatedDiscoveryInformation

### LastRunTime
- **Type**: typing.Optional[datetime.datetime]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BorrowConfiguration

### AllowEarlyCheckIn
- **Type**: <class 'bool'>
- **Required**: Yes

### MaxTimeToLiveInMinutes
- **Type**: <class 'int'>
- **Required**: Yes


# CheckInLicenseRequest

### LicenseConsumptionToken
- **Type**: <class 'str'>
- **Required**: Yes

### Beneficiary
- **Type**: typing.Optional[str]


# CheckoutBorrowLicenseRequest

### LicenseArn
- **Type**: <class 'str'>
- **Required**: Yes

### Entitlements
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.EntitlementData]
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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.Metadata]]


# CheckoutBorrowLicenseResponse

### LicenseArn
- **Type**: <class 'str'>
- **Required**: Yes

### LicenseConsumptionToken
- **Type**: <class 'str'>
- **Required**: Yes

### EntitlementsAllowed
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.EntitlementData]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.Metadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes


# CheckoutLicenseRequest

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.EntitlementData]
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### Beneficiary
- **Type**: typing.Optional[str]

### NodeId
- **Type**: typing.Optional[str]


# CheckoutLicenseResponse

### CheckoutType
- **Type**: typing.Literal['PERPETUAL', 'PROVISIONAL']
- **Required**: Yes

### LicenseConsumptionToken
- **Type**: <class 'str'>
- **Required**: Yes

### EntitlementsAllowed
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.EntitlementData]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes


# ConsumedLicenseSummary

### ResourceType
- **Type**: typing.Optional[typing.Literal['EC2_AMI', 'EC2_HOST', 'EC2_INSTANCE', 'RDS', 'SYSTEMS_MANAGER_MANAGED_INSTANCE']]

### ConsumedLicenses
- **Type**: typing.Optional[int]


# ConsumptionConfiguration

### RenewType
- **Type**: typing.Optional[typing.Literal['Monthly', 'None', 'Weekly']]

### ProvisionalConfiguration
- **Type**: <class 'NoneType'>

### BorrowConfiguration
- **Type**: <class 'NoneType'>


# CreateGrantRequest

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


# CreateGrantResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes


# CreateGrantVersionRequest

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
- **Type**: <class 'NoneType'>


# CreateGrantVersionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLicenseConfigurationRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.Tag]]

### DisassociateWhenNotFound
- **Type**: typing.Optional[bool]

### ProductInformationList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.ProductInformationUnion]]


# CreateLicenseConfigurationResponse

### LicenseConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLicenseConversionTaskForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceLicenseContext
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.LicenseConversionContext'>
- **Required**: Yes

### DestinationLicenseContext
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.LicenseConversionContext'>
- **Required**: Yes


# CreateLicenseConversionTaskForResourceResponse

### LicenseConversionTaskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLicenseManagerReportGeneratorResponse

### LicenseManagerReportGeneratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLicenseRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.Issuer'>
- **Required**: Yes

### HomeRegion
- **Type**: <class 'str'>
- **Required**: Yes

### Validity
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.DatetimeRange'>
- **Required**: Yes

### Entitlements
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.Entitlement]
- **Required**: Yes

### Beneficiary
- **Type**: <class 'str'>
- **Required**: Yes

### ConsumptionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ConsumptionConfiguration'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### LicenseMetadata
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.Metadata]]


# CreateLicenseResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLicenseVersionRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.Issuer'>
- **Required**: Yes

### HomeRegion
- **Type**: <class 'str'>
- **Required**: Yes

### Validity
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.DatetimeRange'>
- **Required**: Yes

### Entitlements
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.Entitlement]
- **Required**: Yes

### ConsumptionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ConsumptionConfiguration'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['AVAILABLE', 'DEACTIVATED', 'DELETED', 'EXPIRED', 'PENDING_AVAILABLE', 'PENDING_DELETE', 'SUSPENDED']
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### LicenseMetadata
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.Metadata]]

### SourceVersion
- **Type**: typing.Optional[str]


# CreateLicenseVersionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTokenRequest

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


# CreateTokenResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes


# DatetimeRange

### Begin
- **Type**: <class 'str'>
- **Required**: Yes

### End
- **Type**: typing.Optional[str]


# DeleteGrantRequest

### GrantArn
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### StatusReason
- **Type**: typing.Optional[str]


# DeleteGrantResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteLicenseConfigurationRequest

### LicenseConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLicenseManagerReportGeneratorRequest

### LicenseManagerReportGeneratorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLicenseRequest

### LicenseArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceVersion
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLicenseResponse

### Status
- **Type**: typing.Literal['DELETED', 'PENDING_DELETE']
- **Required**: Yes

### DeletionDate
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteTokenRequest

### TokenId
- **Type**: <class 'str'>
- **Required**: Yes


# Entitlement

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


# EntitlementData

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Unit
- **Type**: typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# EntitlementUsage

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


# ExtendLicenseConsumptionRequest

### LicenseConsumptionToken
- **Type**: <class 'str'>
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# ExtendLicenseConsumptionResponse

### LicenseConsumptionToken
- **Type**: <class 'str'>
- **Required**: Yes

### Expiration
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes


# Filter

### Name
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# GetAccessTokenRequest

### Token
- **Type**: <class 'str'>
- **Required**: Yes

### TokenProperties
- **Type**: typing.Optional[typing.Sequence[str]]


# GetAccessTokenResponse

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes


# GetGrantRequest

### GrantArn
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]


# GetGrantResponse

### Grant
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.Grant'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes


# GetLicenseConfigurationRequest

### LicenseConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetLicenseConfigurationResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.ConsumedLicenseSummary]
- **Required**: Yes

### ManagedResourceSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.ManagedResourceSummary]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.Tag]
- **Required**: Yes

### ProductInformationList
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.ProductInformationOutput]
- **Required**: Yes

### AutomatedDiscoveryInformation
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.AutomatedDiscoveryInformation'>
- **Required**: Yes

### DisassociateWhenNotFound
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes


# GetLicenseConversionTaskRequest

### LicenseConversionTaskId
- **Type**: <class 'str'>
- **Required**: Yes


# GetLicenseConversionTaskResponse

### LicenseConversionTaskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceLicenseContext
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.LicenseConversionContext'>
- **Required**: Yes

### DestinationLicenseContext
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.LicenseConversionContext'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes


# GetLicenseManagerReportGeneratorRequest

### LicenseManagerReportGeneratorArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetLicenseManagerReportGeneratorResponse

### ReportGenerator
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ReportGenerator'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes


# GetLicenseRequest

### LicenseArn
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]


# GetLicenseResponse

### License
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.License'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes


# GetLicenseUsageRequest

### LicenseArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetLicenseUsageResponse

### LicenseUsage
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.LicenseUsage'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes


# GetServiceSettingsResponse

### S3BucketArn
- **Type**: <class 'str'>
- **Required**: Yes

### SnsTopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.OrganizationConfiguration'>
- **Required**: Yes

### EnableCrossAccountsDiscovery
- **Type**: <class 'bool'>
- **Required**: Yes

### LicenseManagerResourceShareArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes


# Grant

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
- **Type**: <class 'NoneType'>


# GrantedLicense

### LicenseArn
- **Type**: typing.Optional[str]

### LicenseName
- **Type**: typing.Optional[str]

### ProductName
- **Type**: typing.Optional[str]

### ProductSKU
- **Type**: typing.Optional[str]

### Issuer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.IssuerDetails]

### HomeRegion
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DEACTIVATED', 'DELETED', 'EXPIRED', 'PENDING_AVAILABLE', 'PENDING_DELETE', 'SUSPENDED']]

### Validity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.DatetimeRange]

### Beneficiary
- **Type**: typing.Optional[str]

### Entitlements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_classes.Entitlement]]

### ConsumptionConfiguration
- **Type**: <class 'NoneType'>

### LicenseMetadata
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_classes.Metadata]]

### CreateTime
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### ReceivedMetadata
- **Type**: <class 'NoneType'>


# InventoryFilter

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Condition
- **Type**: typing.Literal['BEGINS_WITH', 'CONTAINS', 'EQUALS', 'NOT_EQUALS']
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# Issuer

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SignKey
- **Type**: typing.Optional[str]


# IssuerDetails

### Name
- **Type**: typing.Optional[str]

### SignKey
- **Type**: typing.Optional[str]

### KeyFingerprint
- **Type**: typing.Optional[str]


# License

### LicenseArn
- **Type**: typing.Optional[str]

### LicenseName
- **Type**: typing.Optional[str]

### ProductName
- **Type**: typing.Optional[str]

### ProductSKU
- **Type**: typing.Optional[str]

### Issuer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.IssuerDetails]

### HomeRegion
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DEACTIVATED', 'DELETED', 'EXPIRED', 'PENDING_AVAILABLE', 'PENDING_DELETE', 'SUSPENDED']]

### Validity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.DatetimeRange]

### Beneficiary
- **Type**: typing.Optional[str]

### Entitlements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_classes.Entitlement]]

### ConsumptionConfiguration
- **Type**: <class 'NoneType'>

### LicenseMetadata
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_classes.Metadata]]

### CreateTime
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# LicenseConfiguration

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_classes.ConsumedLicenseSummary]]

### ManagedResourceSummaryList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_classes.ManagedResourceSummary]]

### ProductInformationList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_classes.ProductInformationOutput]]

### AutomatedDiscoveryInformation
- **Type**: <class 'NoneType'>


# LicenseConfigurationAssociation

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


# LicenseConfigurationUsage

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


# LicenseConversionContext

### UsageOperation
- **Type**: typing.Optional[str]


# LicenseConversionTask

### LicenseConversionTaskId
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### SourceLicenseContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.LicenseConversionContext]

### DestinationLicenseContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.LicenseConversionContext]

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


# LicenseOperationFailure

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_classes.Metadata]]


# LicenseSpecification

### LicenseConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### AmiAssociationScope
- **Type**: typing.Optional[str]


# LicenseUsage

### EntitlementUsages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_classes.EntitlementUsage]]


# ListAssociationsForLicenseConfigurationRequest

### LicenseConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAssociationsForLicenseConfigurationRequestPaginate

### LicenseConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.PaginatorConfig]


# ListAssociationsForLicenseConfigurationResponse

### LicenseConfigurationAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.LicenseConfigurationAssociation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDistributedGrantsRequest

### GrantArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.Filter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDistributedGrantsResponse

### Grants
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.Grant]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFailuresForLicenseConfigurationOperationsRequest

### LicenseConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListFailuresForLicenseConfigurationOperationsResponse

### LicenseOperationFailureList
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.LicenseOperationFailure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLicenseConfigurationsRequest

### LicenseConfigurationArns
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.Filter]]


# ListLicenseConfigurationsRequestPaginate

### LicenseConfigurationArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.PaginatorConfig]


# ListLicenseConfigurationsResponse

### LicenseConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.LicenseConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLicenseConversionTasksRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.Filter]]


# ListLicenseConversionTasksResponse

### LicenseConversionTasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.LicenseConversionTask]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLicenseManagerReportGeneratorsRequest

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.Filter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListLicenseManagerReportGeneratorsResponse

### ReportGenerators
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.ReportGenerator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLicenseSpecificationsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListLicenseSpecificationsForResourceRequestPaginate

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.PaginatorConfig]


# ListLicenseSpecificationsForResourceResponse

### LicenseSpecifications
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.LicenseSpecification]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLicenseVersionsRequest

### LicenseArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListLicenseVersionsResponse

### Licenses
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.License]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLicensesRequest

### LicenseArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.Filter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListLicensesResponse

### Licenses
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.License]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListReceivedGrantsForOrganizationRequest

### LicenseArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.Filter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListReceivedGrantsForOrganizationResponse

### Grants
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.Grant]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListReceivedGrantsRequest

### GrantArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.Filter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListReceivedGrantsResponse

### Grants
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.Grant]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListReceivedLicensesForOrganizationRequest

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.Filter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListReceivedLicensesForOrganizationResponse

### Licenses
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.GrantedLicense]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListReceivedLicensesRequest

### LicenseArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.Filter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListReceivedLicensesResponse

### Licenses
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.GrantedLicense]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourceInventoryRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.InventoryFilter]]


# ListResourceInventoryRequestPaginate

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.InventoryFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.PaginatorConfig]


# ListResourceInventoryResponse

### ResourceInventoryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.ResourceInventory]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes


# ListTokensRequest

### TokenIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.Filter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTokensResponse

### Tokens
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.TokenData]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListUsageForLicenseConfigurationRequest

### LicenseConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.Filter]]


# ListUsageForLicenseConfigurationRequestPaginate

### LicenseConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.PaginatorConfig]


# ListUsageForLicenseConfigurationResponse

### LicenseConfigurationUsageList
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.LicenseConfigurationUsage]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ManagedResourceSummary

### ResourceType
- **Type**: typing.Optional[typing.Literal['EC2_AMI', 'EC2_HOST', 'EC2_INSTANCE', 'RDS', 'SYSTEMS_MANAGER_MANAGED_INSTANCE']]

### AssociationCount
- **Type**: typing.Optional[int]


# Metadata

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# Options

### ActivationOverrideBehavior
- **Type**: typing.Optional[typing.Literal['ALL_GRANTS_PERMITTED_BY_ISSUER', 'DISTRIBUTED_GRANTS_ONLY']]


# OrganizationConfiguration

### EnableIntegration
- **Type**: <class 'bool'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProductInformation

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### ProductInformationFilterList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.ProductInformationFilterUnion]
- **Required**: Yes


# ProductInformationFilter

### ProductInformationFilterName
- **Type**: <class 'str'>
- **Required**: Yes

### ProductInformationFilterComparator
- **Type**: <class 'str'>
- **Required**: Yes

### ProductInformationFilterValue
- **Type**: typing.Optional[typing.Sequence[str]]


# ProductInformationFilterOutput

### ProductInformationFilterName
- **Type**: <class 'str'>
- **Required**: Yes

### ProductInformationFilterComparator
- **Type**: <class 'str'>
- **Required**: Yes

### ProductInformationFilterValue
- **Type**: typing.Optional[typing.List[str]]


# ProductInformationFilterUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProductInformationOutput

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### ProductInformationFilterList
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_classes.ProductInformationFilterOutput]
- **Required**: Yes


# ProductInformationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProvisionalConfiguration

### MaxTimeToLiveInMinutes
- **Type**: <class 'int'>
- **Required**: Yes


# ReceivedMetadata

### ReceivedStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED', 'DISABLED', 'FAILED_WORKFLOW', 'PENDING_ACCEPT', 'PENDING_WORKFLOW', 'REJECTED', 'WORKFLOW_COMPLETED']]

### ReceivedStatusReason
- **Type**: typing.Optional[str]

### AllowedOperations
- **Type**: typing.Optional[typing.List[typing.Literal['CheckInLicense', 'CheckoutBorrowLicense', 'CheckoutLicense', 'CreateGrant', 'CreateToken', 'ExtendConsumptionLicense', 'ListPurchasedLicenses']]]


# RejectGrantRequest

### GrantArn
- **Type**: <class 'str'>
- **Required**: Yes


# RejectGrantResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_classes.ResponseMetadata'>
- **Required**: Yes


# ReportContext

### licenseConfigurationArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ReportContextOutput

### licenseConfigurationArns
- **Type**: typing.List[str]
- **Required**: Yes


# ReportFrequency

### value
- **Type**: typing.Optional[int]

### period
- **Type**: typing.Optional[typing.Literal['DAY', 'MONTH', 'WEEK']]


# ReportGenerator

### ReportGeneratorName
- **Type**: typing.Optional[str]

### ReportType
- **Type**: typing.Optional[typing.List[typing.Literal['LicenseConfigurationSummaryReport', 'LicenseConfigurationUsageReport']]]

### ReportContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_classes.ReportContextOutput]

### ReportFrequency
- **Type**: <class 'NoneType'>

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
- **Type**: <class 'NoneType'>

### CreateTime
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_classes.Tag]]


# ResourceInventory

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


# S3Location

### bucket
- **Type**: typing.Optional[str]

### keyPrefix
- **Type**: typing.Optional[str]


# Tag

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.Tag]
- **Required**: Yes


# TokenData

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


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateLicenseConfigurationRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.ProductInformationUnion]]

### DisassociateWhenNotFound
- **Type**: typing.Optional[bool]


# UpdateLicenseSpecificationsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### AddLicenseSpecifications
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.LicenseSpecification]]

### RemoveLicenseSpecifications
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_classes.LicenseSpecification]]


# UpdateServiceSettingsRequest

### S3BucketArn
- **Type**: typing.Optional[str]

### SnsTopicArn
- **Type**: typing.Optional[str]

### OrganizationConfiguration
- **Type**: <class 'NoneType'>

### EnableCrossAccountsDiscovery
- **Type**: typing.Optional[bool]


