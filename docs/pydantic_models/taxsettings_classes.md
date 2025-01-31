# taxsettings_classes

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

### estoniaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.EstoniaAdditionalInfoTypeDef]

### georgiaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.GeorgiaAdditionalInfoTypeDef]

### israelAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.IsraelAdditionalInfoTypeDef]

### italyAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.ItalyAdditionalInfoTypeDef]

### kenyaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.KenyaAdditionalInfoTypeDef]

### malaysiaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.MalaysiaAdditionalInfoTypeDef]

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


# AdditionalInfoResponseTypeDef

### brazilAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.BrazilAdditionalInfoTypeDef]

### canadaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.CanadaAdditionalInfoTypeDef]

### estoniaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.EstoniaAdditionalInfoTypeDef]

### georgiaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.GeorgiaAdditionalInfoTypeDef]

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


# BatchDeleteTaxRegistrationRequestRequestTypeDef

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


# BatchPutTaxRegistrationErrorTypeDef

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: typing.Optional[str]


# BatchPutTaxRegistrationRequestRequestTypeDef

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


# DeleteTaxRegistrationRequestRequestTypeDef

### accountId
- **Type**: typing.Optional[str]


# DestinationS3LocationTypeDef

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### prefix
- **Type**: typing.Optional[str]


# EstoniaAdditionalInfoTypeDef

### registryCommercialCode
- **Type**: <class 'str'>
- **Required**: Yes


# GeorgiaAdditionalInfoTypeDef

### personType
- **Type**: typing.Literal['Business', 'Legal Person', 'Physical Person']
- **Required**: Yes


# GetTaxRegistrationDocumentRequestRequestTypeDef

### destinationS3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.DestinationS3LocationTypeDef'>
- **Required**: Yes

### taxDocumentMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.TaxDocumentMetadataTypeDef'>
- **Required**: Yes


# GetTaxRegistrationDocumentResponseTypeDef

### destinationFilePath
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTaxRegistrationRequestRequestTypeDef

### accountId
- **Type**: typing.Optional[str]


# GetTaxRegistrationResponseTypeDef

### taxRegistration
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.TaxRegistrationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# ListTaxRegistrationsRequestListTaxRegistrationsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.PaginatorConfigTypeDef]


# ListTaxRegistrationsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTaxRegistrationsResponseTypeDef

### accountDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.taxsettings_classes.AccountDetailsTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MalaysiaAdditionalInfoOutputTypeDef

### serviceTaxCodes
- **Type**: typing.List[typing.Literal['Consultancy', 'Digital Service And Electronic Medium', 'IT Services', 'Training Or Coaching']]
- **Required**: Yes


# MalaysiaAdditionalInfoTypeDef

### serviceTaxCodes
- **Type**: typing.Sequence[typing.Literal['Consultancy', 'Digital Service And Electronic Medium', 'IT Services', 'Training Or Coaching']]
- **Required**: Yes


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


# PutTaxRegistrationRequestRequestTypeDef

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


# TaxDocumentMetadataTypeDef

### taxDocumentAccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### taxDocumentName
- **Type**: <class 'str'>
- **Required**: Yes


# TaxInheritanceDetailsTypeDef

### inheritanceObtainedReason
- **Type**: typing.Optional[str]

### parentEntityId
- **Type**: typing.Optional[str]


# TaxRegistrationDocumentTypeDef

### s3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.SourceS3LocationTypeDef'>
- **Required**: Yes


# TaxRegistrationEntryTypeDef

### registrationId
- **Type**: <class 'str'>
- **Required**: Yes

### registrationType
- **Type**: typing.Literal['CNPJ', 'CPF', 'GST', 'SST', 'VAT']
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
- **Type**: typing.Literal['CNPJ', 'CPF', 'GST', 'SST', 'VAT']
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
- **Type**: typing.Literal['CNPJ', 'CPF', 'GST', 'SST', 'VAT']
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


