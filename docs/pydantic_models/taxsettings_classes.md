# Taxsettings Classes

# AccountDetailsTypeDef

### accountId
- **Type**: typing.Optional[str]

### accountMetaData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.AccountMetaDataTypeDef]

### taxInheritanceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.TaxInheritanceDetailsTypeDef]

### taxRegistration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.TaxRegistrationWithJurisdictionTypeDef]


# AccountMetaDataTypeDef

### accountName
- **Type**: typing.Optional[str]

### address
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.AddressTypeDef]

### addressRoleMap
- **Type**: typing.Optional[typing.Dict[typing.Literal['BillingAddress', 'ContactAddress', 'TaxAddress'], aws_resource_validator.pydantic_models.taxsettings_classes.JurisdictionTypeDef]]

### addressType
- **Type**: typing.Optional[typing.Literal['BillingAddress', 'ContactAddress', 'TaxAddress']]

### seller
- **Type**: typing.Optional[str]


# AdditionalInfoRequestTypeDef

### canadaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.CanadaAdditionalInfoTypeDef]

### egyptAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.EgyptAdditionalInfoTypeDef]

### estoniaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.EstoniaAdditionalInfoTypeDef]

### georgiaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.GeorgiaAdditionalInfoTypeDef]

### greeceAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.GreeceAdditionalInfoTypeDef]

### israelAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.IsraelAdditionalInfoTypeDef]

### italyAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.ItalyAdditionalInfoTypeDef]

### kenyaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.KenyaAdditionalInfoTypeDef]

### malaysiaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.MalaysiaAdditionalInfoUnionTypeDef]

### polandAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.PolandAdditionalInfoTypeDef]

### romaniaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.RomaniaAdditionalInfoTypeDef]

### saudiArabiaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.SaudiArabiaAdditionalInfoTypeDef]

### southKoreaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.SouthKoreaAdditionalInfoTypeDef]

### spainAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.SpainAdditionalInfoTypeDef]

### turkeyAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.TurkeyAdditionalInfoTypeDef]

### ukraineAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.UkraineAdditionalInfoTypeDef]

### vietnamAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.VietnamAdditionalInfoTypeDef]


# AdditionalInfoResponseTypeDef

### brazilAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.BrazilAdditionalInfoTypeDef]

### canadaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.CanadaAdditionalInfoTypeDef]

### egyptAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.EgyptAdditionalInfoTypeDef]

### estoniaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.EstoniaAdditionalInfoTypeDef]

### georgiaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.GeorgiaAdditionalInfoTypeDef]

### greeceAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.GreeceAdditionalInfoTypeDef]

### indiaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.IndiaAdditionalInfoTypeDef]

### israelAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.IsraelAdditionalInfoTypeDef]

### italyAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.ItalyAdditionalInfoTypeDef]

### kenyaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.KenyaAdditionalInfoTypeDef]

### malaysiaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.MalaysiaAdditionalInfoOutputTypeDef]

### polandAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.PolandAdditionalInfoTypeDef]

### romaniaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.RomaniaAdditionalInfoTypeDef]

### saudiArabiaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.SaudiArabiaAdditionalInfoTypeDef]

### southKoreaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.SouthKoreaAdditionalInfoTypeDef]

### spainAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.SpainAdditionalInfoTypeDef]

### turkeyAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.TurkeyAdditionalInfoTypeDef]

### ukraineAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.UkraineAdditionalInfoTypeDef]

### vietnamAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.VietnamAdditionalInfoTypeDef]


# AddressTypeDef

### addressLine1
- **Type**: <class 'str'>
- **Required**: Yes

### city
- **Type**: <class 'str'>
- **Required**: Yes

### countryCode
- **Type**: <class 'str'>
- **Required**: Yes

### postalCode
- **Type**: <class 'str'>
- **Required**: Yes

### addressLine2
- **Type**: typing.Optional[str]

### addressLine3
- **Type**: typing.Optional[str]

### districtOrCounty
- **Type**: typing.Optional[str]

### stateOrRegion
- **Type**: typing.Optional[str]


# AuthorityTypeDef

### country
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDeleteTaxRegistrationErrorTypeDef

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: typing.Optional[str]


# BatchDeleteTaxRegistrationRequestTypeDef

### accountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchDeleteTaxRegistrationResponseTypeDef

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.taxsettings_classes.BatchDeleteTaxRegistrationErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetTaxExemptionsRequestTypeDef

### accountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetTaxExemptionsResponseTypeDef

### failedAccounts
- **Type**: typing.List[str]
- **Required**: Yes

### taxExemptionDetailsMap
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.taxsettings_classes.TaxExemptionDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchPutTaxRegistrationErrorTypeDef

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: typing.Optional[str]


# BatchPutTaxRegistrationRequestTypeDef

### accountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### taxRegistrationEntry
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.TaxRegistrationEntryTypeDef'>
- **Required**: Yes


# BatchPutTaxRegistrationResponseTypeDef

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.taxsettings_classes.BatchPutTaxRegistrationErrorTypeDef]
- **Required**: Yes

### status
- **Type**: typing.Literal['Deleted', 'Pending', 'Rejected', 'Verified']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BrazilAdditionalInfoTypeDef

### ccmCode
- **Type**: typing.Optional[str]

### legalNatureCode
- **Type**: typing.Optional[str]


# CanadaAdditionalInfoTypeDef

### canadaQuebecSalesTaxNumber
- **Type**: typing.Optional[str]

### canadaRetailSalesTaxNumber
- **Type**: typing.Optional[str]

### isResellerAccount
- **Type**: typing.Optional[bool]

### provincialSalesTaxId
- **Type**: typing.Optional[str]


# DeleteSupplementalTaxRegistrationRequestTypeDef

### authorityId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTaxRegistrationRequestTypeDef

### accountId
- **Type**: typing.Optional[str]


# DestinationS3LocationTypeDef

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### prefix
- **Type**: typing.Optional[str]


# EgyptAdditionalInfoTypeDef

### uniqueIdentificationNumber
- **Type**: typing.Optional[str]

### uniqueIdentificationNumberExpirationDate
- **Type**: typing.Optional[str]


# EstoniaAdditionalInfoTypeDef

### registryCommercialCode
- **Type**: <class 'str'>
- **Required**: Yes


# ExemptionCertificateTypeDef

### documentFile
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.BlobTypeDef'>
- **Required**: Yes

### documentName
- **Type**: <class 'str'>
- **Required**: Yes


# GeorgiaAdditionalInfoTypeDef

### personType
- **Type**: typing.Literal['Business', 'Legal Person', 'Physical Person']
- **Required**: Yes


# GetTaxExemptionTypesResponseTypeDef

### taxExemptionTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.taxsettings_classes.TaxExemptionTypeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTaxInheritanceResponseTypeDef

### heritageStatus
- **Type**: typing.Literal['OptIn', 'OptOut']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTaxRegistrationDocumentRequestTypeDef

### taxDocumentMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.TaxDocumentMetadataTypeDef'>
- **Required**: Yes

### destinationS3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.DestinationS3LocationTypeDef]


# GetTaxRegistrationDocumentResponseTypeDef

### destinationFilePath
- **Type**: <class 'str'>
- **Required**: Yes

### presignedS3Url
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTaxRegistrationRequestTypeDef

### accountId
- **Type**: typing.Optional[str]


# GetTaxRegistrationResponseTypeDef

### taxRegistration
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.TaxRegistrationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GreeceAdditionalInfoTypeDef

### contractingAuthorityCode
- **Type**: typing.Optional[str]


# IndiaAdditionalInfoTypeDef

### pan
- **Type**: typing.Optional[str]


# IsraelAdditionalInfoTypeDef

### customerType
- **Type**: typing.Literal['Business', 'Individual']
- **Required**: Yes

### dealerType
- **Type**: typing.Literal['Authorized', 'Non-authorized']
- **Required**: Yes


# ItalyAdditionalInfoTypeDef

### cigNumber
- **Type**: typing.Optional[str]

### cupNumber
- **Type**: typing.Optional[str]

### sdiAccountId
- **Type**: typing.Optional[str]

### taxCode
- **Type**: typing.Optional[str]


# JurisdictionTypeDef

### countryCode
- **Type**: <class 'str'>
- **Required**: Yes

### stateOrRegion
- **Type**: typing.Optional[str]


# KenyaAdditionalInfoTypeDef

### personType
- **Type**: typing.Literal['Business', 'Legal Person', 'Physical Person']
- **Required**: Yes


# ListSupplementalTaxRegistrationsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.PaginatorConfigTypeDef]


# ListSupplementalTaxRegistrationsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSupplementalTaxRegistrationsResponseTypeDef

### taxRegistrations
- **Type**: typing.List[aws_resource_validator.pydantic_models.taxsettings_classes.SupplementalTaxRegistrationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTaxExemptionsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.PaginatorConfigTypeDef]


# ListTaxExemptionsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTaxExemptionsResponseTypeDef

### taxExemptionDetailsMap
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.taxsettings_classes.TaxExemptionDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTaxRegistrationsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.PaginatorConfigTypeDef]


# ListTaxRegistrationsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTaxRegistrationsResponseTypeDef

### accountDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.taxsettings_classes.AccountDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# MalaysiaAdditionalInfoOutputTypeDef

### businessRegistrationNumber
- **Type**: typing.Optional[str]

### serviceTaxCodes
- **Type**: typing.Optional[typing.List[typing.Literal['Consultancy', 'Digital Service And Electronic Medium', 'IT Services', 'Training Or Coaching']]]

### taxInformationNumber
- **Type**: typing.Optional[str]


# MalaysiaAdditionalInfoTypeDef

### businessRegistrationNumber
- **Type**: typing.Optional[str]

### serviceTaxCodes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Consultancy', 'Digital Service And Electronic Medium', 'IT Services', 'Training Or Coaching']]]

### taxInformationNumber
- **Type**: typing.Optional[str]


# MalaysiaAdditionalInfoUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PolandAdditionalInfoTypeDef

### individualRegistrationNumber
- **Type**: typing.Optional[str]

### isGroupVatEnabled
- **Type**: typing.Optional[bool]


# PutSupplementalTaxRegistrationRequestTypeDef

### taxRegistrationEntry
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.SupplementalTaxRegistrationEntryTypeDef'>
- **Required**: Yes


# PutSupplementalTaxRegistrationResponseTypeDef

### authorityId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Deleted', 'Pending', 'Rejected', 'Verified']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutTaxExemptionRequestTypeDef

### accountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### authority
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.AuthorityTypeDef'>
- **Required**: Yes

### exemptionCertificate
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.ExemptionCertificateTypeDef'>
- **Required**: Yes

### exemptionType
- **Type**: <class 'str'>
- **Required**: Yes


# PutTaxExemptionResponseTypeDef

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutTaxInheritanceRequestTypeDef

### heritageStatus
- **Type**: typing.Optional[typing.Literal['OptIn', 'OptOut']]


# PutTaxRegistrationRequestTypeDef

### taxRegistrationEntry
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.TaxRegistrationEntryTypeDef'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]


# PutTaxRegistrationResponseTypeDef

### status
- **Type**: typing.Literal['Deleted', 'Pending', 'Rejected', 'Verified']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResponseMetadataTypeDef

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


# RomaniaAdditionalInfoTypeDef

### taxRegistrationNumberType
- **Type**: typing.Literal['LocalRegistrationNumber', 'TaxRegistrationNumber']
- **Required**: Yes


# SaudiArabiaAdditionalInfoTypeDef

### taxRegistrationNumberType
- **Type**: typing.Optional[typing.Literal['CommercialRegistrationNumber', 'TaxIdentificationNumber', 'TaxRegistrationNumber']]


# SourceS3LocationTypeDef

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes


# SouthKoreaAdditionalInfoTypeDef

### businessRepresentativeName
- **Type**: <class 'str'>
- **Required**: Yes

### itemOfBusiness
- **Type**: <class 'str'>
- **Required**: Yes

### lineOfBusiness
- **Type**: <class 'str'>
- **Required**: Yes


# SpainAdditionalInfoTypeDef

### registrationType
- **Type**: typing.Literal['Intra-EU', 'Local']
- **Required**: Yes


# SupplementalTaxRegistrationEntryTypeDef

### address
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.AddressTypeDef'>
- **Required**: Yes

### legalName
- **Type**: <class 'str'>
- **Required**: Yes

### registrationId
- **Type**: <class 'str'>
- **Required**: Yes

### registrationType
- **Type**: typing.Literal['VAT']
- **Required**: Yes


# SupplementalTaxRegistrationTypeDef

### address
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.AddressTypeDef'>
- **Required**: Yes

### authorityId
- **Type**: <class 'str'>
- **Required**: Yes

### legalName
- **Type**: <class 'str'>
- **Required**: Yes

### registrationId
- **Type**: <class 'str'>
- **Required**: Yes

### registrationType
- **Type**: typing.Literal['VAT']
- **Required**: Yes

### status
- **Type**: typing.Literal['Deleted', 'Pending', 'Rejected', 'Verified']
- **Required**: Yes


# TaxDocumentMetadataTypeDef

### taxDocumentAccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### taxDocumentName
- **Type**: <class 'str'>
- **Required**: Yes


# TaxExemptionDetailsTypeDef

### heritageObtainedDetails
- **Type**: typing.Optional[bool]

### heritageObtainedParentEntity
- **Type**: typing.Optional[str]

### heritageObtainedReason
- **Type**: typing.Optional[str]

### taxExemptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.taxsettings_classes.TaxExemptionTypeDef]]


# TaxExemptionTypeDef

### authority
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.AuthorityTypeDef'>
- **Required**: Yes

### taxExemptionType
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.TaxExemptionTypeTypeDef'>
- **Required**: Yes

### effectiveDate
- **Type**: typing.Optional[datetime.datetime]

### expirationDate
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['Expired', 'None', 'Pending', 'Valid']]

### systemEffectiveDate
- **Type**: typing.Optional[datetime.datetime]


# TaxExemptionTypeTypeDef

### applicableJurisdictions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.taxsettings_classes.AuthorityTypeDef]]

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]


# TaxInheritanceDetailsTypeDef

### inheritanceObtainedReason
- **Type**: typing.Optional[str]

### parentEntityId
- **Type**: typing.Optional[str]


# TaxRegistrationDocFileTypeDef

### fileContent
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.BlobTypeDef'>
- **Required**: Yes

### fileName
- **Type**: <class 'str'>
- **Required**: Yes


# TaxRegistrationDocumentTypeDef

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.TaxRegistrationDocFileTypeDef]

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.SourceS3LocationTypeDef]


# TaxRegistrationEntryTypeDef

### registrationId
- **Type**: <class 'str'>
- **Required**: Yes

### registrationType
- **Type**: typing.Literal['CNPJ', 'CPF', 'GST', 'NRIC', 'SST', 'TIN', 'VAT']
- **Required**: Yes

### additionalTaxInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.AdditionalInfoRequestTypeDef]

### certifiedEmailId
- **Type**: typing.Optional[str]

### legalAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.AddressTypeDef]

### legalName
- **Type**: typing.Optional[str]

### sector
- **Type**: typing.Optional[typing.Literal['Business', 'Government', 'Individual']]

### verificationDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.VerificationDetailsTypeDef]


# TaxRegistrationTypeDef

### legalAddress
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.AddressTypeDef'>
- **Required**: Yes

### legalName
- **Type**: <class 'str'>
- **Required**: Yes

### registrationId
- **Type**: <class 'str'>
- **Required**: Yes

### registrationType
- **Type**: typing.Literal['CNPJ', 'CPF', 'GST', 'NRIC', 'SST', 'TIN', 'VAT']
- **Required**: Yes

### status
- **Type**: typing.Literal['Deleted', 'Pending', 'Rejected', 'Verified']
- **Required**: Yes

### additionalTaxInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.AdditionalInfoResponseTypeDef]

### certifiedEmailId
- **Type**: typing.Optional[str]

### sector
- **Type**: typing.Optional[typing.Literal['Business', 'Government', 'Individual']]

### taxDocumentMetadatas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.taxsettings_classes.TaxDocumentMetadataTypeDef]]


# TaxRegistrationWithJurisdictionTypeDef

### jurisdiction
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.JurisdictionTypeDef'>
- **Required**: Yes

### legalName
- **Type**: <class 'str'>
- **Required**: Yes

### registrationId
- **Type**: <class 'str'>
- **Required**: Yes

### registrationType
- **Type**: typing.Literal['CNPJ', 'CPF', 'GST', 'NRIC', 'SST', 'TIN', 'VAT']
- **Required**: Yes

### status
- **Type**: typing.Literal['Deleted', 'Pending', 'Rejected', 'Verified']
- **Required**: Yes

### additionalTaxInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.AdditionalInfoResponseTypeDef]

### certifiedEmailId
- **Type**: typing.Optional[str]

### sector
- **Type**: typing.Optional[typing.Literal['Business', 'Government', 'Individual']]

### taxDocumentMetadatas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.taxsettings_classes.TaxDocumentMetadataTypeDef]]


# TurkeyAdditionalInfoTypeDef

### industries
- **Type**: typing.Optional[typing.Literal['Banks', 'CirculatingOrg', 'DevelopmentAgencies', 'Insurance', 'PensionAndBenefitFunds', 'ProfessionalOrg']]

### kepEmailId
- **Type**: typing.Optional[str]

### secondaryTaxId
- **Type**: typing.Optional[str]

### taxOffice
- **Type**: typing.Optional[str]


# UkraineAdditionalInfoTypeDef

### ukraineTrnType
- **Type**: typing.Literal['Business', 'Individual']
- **Required**: Yes


# VerificationDetailsTypeDef

### dateOfBirth
- **Type**: typing.Optional[str]

### taxRegistrationDocuments
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.taxsettings_classes.TaxRegistrationDocumentTypeDef]]


# VietnamAdditionalInfoTypeDef

### electronicTransactionCodeNumber
- **Type**: typing.Optional[str]

### enterpriseIdentificationNumber
- **Type**: typing.Optional[str]

### paymentVoucherNumber
- **Type**: typing.Optional[str]

### paymentVoucherNumberDate
- **Type**: typing.Optional[str]


