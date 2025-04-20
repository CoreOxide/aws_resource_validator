# Taxsettings Service

### AccountId
- **Type**: string
- **Pattern**: `^\d+$`
- **Min Length**: 12
- **Max Length**: 12

### AccountName
- **Type**: string
- **Pattern**: `^[\s\S]*$`

### AddressLine1
- **Type**: string
- **Pattern**: `^(?!\s*$)[\s\S]+$`
- **Min Length**: 1
- **Max Length**: 180

### AddressLine2
- **Type**: string
- **Pattern**: `^(?!\s*$)[\s\S]+$`
- **Min Length**: 1
- **Max Length**: 60

### AddressLine3
- **Type**: string
- **Pattern**: `^(?!\s*$)[\s\S]+$`
- **Min Length**: 1
- **Max Length**: 60

### BusinessRegistrationNumber
- **Type**: string
- **Pattern**: `^[0-9]{12}$`

### BusinessRepresentativeName
- **Type**: string
- **Pattern**: `^[0-9\u3130-\u318F\uAC00-\uD7AF,.( )-\\s]*$`
- **Min Length**: 1
- **Max Length**: 200

### CanadaProvincialSalesTaxIdString
- **Type**: string
- **Pattern**: `^([0-9A-Z/-]+)$`
- **Min Length**: 7
- **Max Length**: 16

### CanadaQuebecSalesTaxNumberString
- **Type**: string
- **Pattern**: `^([0-9]{10})(TQ[0-9]{4})?$`

### CanadaRetailSalesTaxNumberString
- **Type**: string
- **Pattern**: `^([0-9]{6}-[0-9]{1})$`

### CcmCode
- **Type**: string
- **Pattern**: `^\d+$`
- **Min Length**: 0
- **Max Length**: 1024

### CertifiedEmailId
- **Type**: string
- **Pattern**: `^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,20}$`

### CigNumber
- **Type**: string
- **Pattern**: `^([0-9A-Z]{1,15})$`

### City
- **Type**: string
- **Pattern**: `^(?!\s*$)[\s\S]+$`
- **Min Length**: 1
- **Max Length**: 50

### ContractingAuthorityCode
- **Type**: string
- **Pattern**: `^\d{4}\.[A-Z]\d{5}\.\d{4}$`

### CountryCode
- **Type**: string
- **Pattern**: `^[a-zA-Z]+$`
- **Min Length**: 2
- **Max Length**: 2

### CupNumber
- **Type**: string
- **Pattern**: `^([0-9A-Z]{1,15})$`

### DateOfBirth
- **Type**: string
- **Pattern**: `^(\d{4}-(0[0-9]|1[0-2])-([0-2][0-9]|3[0-1]))$`
- **Min Length**: 10
- **Max Length**: 10

### DateString
- **Type**: string
- **Pattern**: `^(\d{4}-(0[0-9]|1[0-2])-([0-2][0-9]|3[0-1]))$`

### DestinationFilePath
- **Type**: string
- **Pattern**: `^[\s\S]*$`

### DisplayName
- **Type**: string
- **Pattern**: `^[\s\S]*$`
- **Min Length**: 0
- **Max Length**: 50

### District
- **Type**: string
- **Pattern**: `^(?!\s*$)[\s\S]+$`
- **Min Length**: 1
- **Max Length**: 50

### ElectronicTransactionCodeNumber
- **Type**: string
- **Pattern**: `^\d{17}$`

### EnterpriseIdentificationNumber
- **Type**: string
- **Pattern**: `^(\d{10}|(\d{10}-\d{3}))$`

### ErrorCode
- **Type**: string
- **Pattern**: `^[\s\S]*$`
- **Min Length**: 0
- **Max Length**: 50

### ErrorMessage
- **Type**: string
- **Pattern**: `^[\s\S]*$`
- **Min Length**: 0
- **Max Length**: 1024

### ExemptionDocumentName
- **Type**: string
- **Pattern**: `^([A-Za-z0-9-_.]+).(pdf|jpg|png)$`
- **Min Length**: 0
- **Max Length**: 128

### FieldName
- **Type**: string
- **Pattern**: `^(?!\s*$)[\s\S]+$`

### GenericString
- **Type**: string
- **Pattern**: `^[\s\S]*$`
- **Min Length**: 1
- **Max Length**: 200

### IndividualRegistrationNumber
- **Type**: string
- **Pattern**: `^([0-9]{10})$`

### InheritanceObtainedReason
- **Type**: string
- **Pattern**: `^[\s\S]*$`

### ItemOfBusiness
- **Type**: string
- **Pattern**: `^[0-9\u3130-\u318F\uAC00-\uD7AF,.( )-\\s]*$`
- **Min Length**: 1
- **Max Length**: 100

### KepEmailId
- **Type**: string
- **Pattern**: `^[\s\S]*$`

### LegalName
- **Type**: string
- **Pattern**: `^(?!\s*$)[\s\S]+$`
- **Min Length**: 1
- **Max Length**: 200

### LegalNatureCode
- **Type**: string
- **Pattern**: `^\d+$`
- **Min Length**: 0
- **Max Length**: 1024

### LineOfBusiness
- **Type**: string
- **Pattern**: `^[0-9\u3130-\u318F\uAC00-\uD7AF,.( )-\\s]*$`
- **Min Length**: 1
- **Max Length**: 100

### PaginationTokenString
- **Type**: string
- **Pattern**: `^[-A-Za-z0-9_+\=\/]+$`
- **Min Length**: 1
- **Max Length**: 2000

### Pan
- **Type**: string
- **Pattern**: `^[A-Z]{5}[0-9]{4}[A-Z]{1}$`

### PaymentVoucherNumber
- **Type**: string
- **Pattern**: `^\d{17}$`

### PostalCode
- **Type**: string
- **Pattern**: `^(?!\s*$)[\s\S]+$`
- **Min Length**: 1
- **Max Length**: 20

### RegistrationId
- **Type**: string
- **Pattern**: `^(?!\s*$)[\s\S]+$`
- **Min Length**: 1
- **Max Length**: 200

### RegistryCommercialCode
- **Type**: string
- **Pattern**: `^\d+$`
- **Min Length**: 8
- **Max Length**: 8

### S3BucketName
- **Type**: string
- **Pattern**: `^(?=^.{3,63}$)(?!^(\d+\.)+\d+$)(^(([a-z0-9]|[a-z0-9][a-z0-9\-]*[a-z0-9])\.)*([a-z0-9]|[a-z0-9][a-z0-9\-]*[a-z0-9])$)$`
- **Min Length**: 3
- **Max Length**: 63

### S3Key
- **Type**: string
- **Pattern**: `^.*\S.*$`
- **Min Length**: 1
- **Max Length**: 1024

### S3Prefix
- **Type**: string
- **Pattern**: `^.*\S.*$`
- **Min Length**: 0
- **Max Length**: 512

### SdiAccountId
- **Type**: string
- **Pattern**: `^[0-9A-Z]{6,7}$`

### SecondaryTaxId
- **Type**: string
- **Pattern**: `^([0-9]{10})$`

### Seller
- **Type**: string
- **Pattern**: `^[\s\S]*$`

### State
- **Type**: string
- **Pattern**: `^(?!\s*$)[\s\S]+$`
- **Min Length**: 1
- **Max Length**: 50

### TaxCode
- **Type**: string
- **Pattern**: `^([0-9]{11}|[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z])$`

### TaxDocumentAccessToken
- **Type**: string
- **Pattern**: `^[\s\S]*$`

### TaxDocumentName
- **Type**: string
- **Pattern**: `^[\s\S]*$`

### TaxInformationNumber
- **Type**: string
- **Pattern**: `^[A-Z]{1,2}[0-9]{1,11}$`

### TaxOffice
- **Type**: string
- **Pattern**: `^[\s\S]*$`

### UniqueIdentificationNumber
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]{39}$`

### Url
- **Type**: string
- **Pattern**: `^https.*\S.*$`
- **Min Length**: 1
- **Max Length**: 200

