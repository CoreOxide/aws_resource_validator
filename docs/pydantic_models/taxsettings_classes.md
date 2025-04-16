# Taxsettings Classes

# AccountDetails

### accountId
- **Type**: typing.Optional[str]

### accountMetaData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.AccountMetaData]

### taxInheritanceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.TaxInheritanceDetails]

### taxRegistration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.TaxRegistrationWithJurisdiction]


# AccountMetaData

### accountName
- **Type**: typing.Optional[str]

### address
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.Address]

### addressRoleMap
- **Type**: typing.Optional[typing.Dict[typing.Literal['BillingAddress', 'ContactAddress', 'TaxAddress'], aws_resource_validator.pydantic_models.taxsettings_classes.Jurisdiction]]

### addressType
- **Type**: typing.Optional[typing.Literal['BillingAddress', 'ContactAddress', 'TaxAddress']]

### seller
- **Type**: typing.Optional[str]


# AdditionalInfoRequest

### canadaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.CanadaAdditionalInfo]

### egyptAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.EgyptAdditionalInfo]

### estoniaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.EstoniaAdditionalInfo]

### georgiaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.GeorgiaAdditionalInfo]

### greeceAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.GreeceAdditionalInfo]

### israelAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.IsraelAdditionalInfo]

### italyAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.ItalyAdditionalInfo]

### kenyaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.KenyaAdditionalInfo]

### malaysiaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.MalaysiaAdditionalInfoUnion]

### polandAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.PolandAdditionalInfo]

### romaniaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.RomaniaAdditionalInfo]

### saudiArabiaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.SaudiArabiaAdditionalInfo]

### southKoreaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.SouthKoreaAdditionalInfo]

### spainAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.SpainAdditionalInfo]

### turkeyAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.TurkeyAdditionalInfo]

### ukraineAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.UkraineAdditionalInfo]

### vietnamAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.VietnamAdditionalInfo]


# AdditionalInfoResponse

### brazilAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.BrazilAdditionalInfo]

### canadaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.CanadaAdditionalInfo]

### egyptAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.EgyptAdditionalInfo]

### estoniaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.EstoniaAdditionalInfo]

### georgiaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.GeorgiaAdditionalInfo]

### greeceAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.GreeceAdditionalInfo]

### indiaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.IndiaAdditionalInfo]

### israelAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.IsraelAdditionalInfo]

### italyAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.ItalyAdditionalInfo]

### kenyaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.KenyaAdditionalInfo]

### malaysiaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.MalaysiaAdditionalInfoOutput]

### polandAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.PolandAdditionalInfo]

### romaniaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.RomaniaAdditionalInfo]

### saudiArabiaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.SaudiArabiaAdditionalInfo]

### southKoreaAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.SouthKoreaAdditionalInfo]

### spainAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.SpainAdditionalInfo]

### turkeyAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.TurkeyAdditionalInfo]

### ukraineAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.UkraineAdditionalInfo]

### vietnamAdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.VietnamAdditionalInfo]


# Address

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


# Authority

### country
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDeleteTaxRegistrationError

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: typing.Optional[str]


# BatchDeleteTaxRegistrationRequest

### accountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchDeleteTaxRegistrationResponse

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.taxsettings_classes.BatchDeleteTaxRegistrationError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetTaxExemptionsRequest

### accountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetTaxExemptionsResponse

### failedAccounts
- **Type**: typing.List[str]
- **Required**: Yes

### taxExemptionDetailsMap
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.taxsettings_classes.TaxExemptionDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.ResponseMetadata'>
- **Required**: Yes


# BatchPutTaxRegistrationError

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: typing.Optional[str]


# BatchPutTaxRegistrationRequest

### accountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### taxRegistrationEntry
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.TaxRegistrationEntry'>
- **Required**: Yes


# BatchPutTaxRegistrationResponse

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.taxsettings_classes.BatchPutTaxRegistrationError]
- **Required**: Yes

### status
- **Type**: typing.Literal['Deleted', 'Pending', 'Rejected', 'Verified']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.ResponseMetadata'>
- **Required**: Yes


# Blob

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BrazilAdditionalInfo

### ccmCode
- **Type**: typing.Optional[str]

### legalNatureCode
- **Type**: typing.Optional[str]


# CanadaAdditionalInfo

### canadaQuebecSalesTaxNumber
- **Type**: typing.Optional[str]

### canadaRetailSalesTaxNumber
- **Type**: typing.Optional[str]

### isResellerAccount
- **Type**: typing.Optional[bool]

### provincialSalesTaxId
- **Type**: typing.Optional[str]


# DeleteSupplementalTaxRegistrationRequest

### authorityId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTaxRegistrationRequest

### accountId
- **Type**: typing.Optional[str]


# DestinationS3Location

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### prefix
- **Type**: typing.Optional[str]


# EgyptAdditionalInfo

### uniqueIdentificationNumber
- **Type**: typing.Optional[str]

### uniqueIdentificationNumberExpirationDate
- **Type**: typing.Optional[str]


# EstoniaAdditionalInfo

### registryCommercialCode
- **Type**: <class 'str'>
- **Required**: Yes


# ExemptionCertificate

### documentFile
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.Blob'>
- **Required**: Yes

### documentName
- **Type**: <class 'str'>
- **Required**: Yes


# GeorgiaAdditionalInfo

### personType
- **Type**: typing.Literal['Business', 'Legal Person', 'Physical Person']
- **Required**: Yes


# GetTaxExemptionTypesResponse

### taxExemptionTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.taxsettings_classes.TaxExemptionType]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.ResponseMetadata'>
- **Required**: Yes


# GetTaxInheritanceResponse

### heritageStatus
- **Type**: typing.Literal['OptIn', 'OptOut']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.ResponseMetadata'>
- **Required**: Yes


# GetTaxRegistrationDocumentRequest

### taxDocumentMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.TaxDocumentMetadata'>
- **Required**: Yes

### destinationS3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.DestinationS3Location]


# GetTaxRegistrationDocumentResponse

### destinationFilePath
- **Type**: <class 'str'>
- **Required**: Yes

### presignedS3Url
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.ResponseMetadata'>
- **Required**: Yes


# GetTaxRegistrationRequest

### accountId
- **Type**: typing.Optional[str]


# GetTaxRegistrationResponse

### taxRegistration
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.TaxRegistration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.ResponseMetadata'>
- **Required**: Yes


# GreeceAdditionalInfo

### contractingAuthorityCode
- **Type**: typing.Optional[str]


# IndiaAdditionalInfo

### pan
- **Type**: typing.Optional[str]


# IsraelAdditionalInfo

### customerType
- **Type**: typing.Literal['Business', 'Individual']
- **Required**: Yes

### dealerType
- **Type**: typing.Literal['Authorized', 'Non-authorized']
- **Required**: Yes


# ItalyAdditionalInfo

### cigNumber
- **Type**: typing.Optional[str]

### cupNumber
- **Type**: typing.Optional[str]

### sdiAccountId
- **Type**: typing.Optional[str]

### taxCode
- **Type**: typing.Optional[str]


# Jurisdiction

### countryCode
- **Type**: <class 'str'>
- **Required**: Yes

### stateOrRegion
- **Type**: typing.Optional[str]


# KenyaAdditionalInfo

### personType
- **Type**: typing.Literal['Business', 'Legal Person', 'Physical Person']
- **Required**: Yes


# ListSupplementalTaxRegistrationsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSupplementalTaxRegistrationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.PaginatorConfig]


# ListSupplementalTaxRegistrationsResponse

### taxRegistrations
- **Type**: typing.List[aws_resource_validator.pydantic_models.taxsettings_classes.SupplementalTaxRegistration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTaxExemptionsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTaxExemptionsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.PaginatorConfig]


# ListTaxExemptionsResponse

### taxExemptionDetailsMap
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.taxsettings_classes.TaxExemptionDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTaxRegistrationsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTaxRegistrationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.PaginatorConfig]


# ListTaxRegistrationsResponse

### accountDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.taxsettings_classes.AccountDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# MalaysiaAdditionalInfo

### businessRegistrationNumber
- **Type**: typing.Optional[str]

### serviceTaxCodes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Consultancy', 'Digital Service And Electronic Medium', 'IT Services', 'Training Or Coaching']]]

### taxInformationNumber
- **Type**: typing.Optional[str]


# MalaysiaAdditionalInfoOutput

### businessRegistrationNumber
- **Type**: typing.Optional[str]

### serviceTaxCodes
- **Type**: typing.Optional[typing.List[typing.Literal['Consultancy', 'Digital Service And Electronic Medium', 'IT Services', 'Training Or Coaching']]]

### taxInformationNumber
- **Type**: typing.Optional[str]


# MalaysiaAdditionalInfoUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PolandAdditionalInfo

### individualRegistrationNumber
- **Type**: typing.Optional[str]

### isGroupVatEnabled
- **Type**: typing.Optional[bool]


# PutSupplementalTaxRegistrationRequest

### taxRegistrationEntry
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.SupplementalTaxRegistrationEntry'>
- **Required**: Yes


# PutSupplementalTaxRegistrationResponse

### authorityId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Deleted', 'Pending', 'Rejected', 'Verified']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.ResponseMetadata'>
- **Required**: Yes


# PutTaxExemptionRequest

### accountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### authority
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.Authority'>
- **Required**: Yes

### exemptionCertificate
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.ExemptionCertificate'>
- **Required**: Yes

### exemptionType
- **Type**: <class 'str'>
- **Required**: Yes


# PutTaxExemptionResponse

### caseId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.ResponseMetadata'>
- **Required**: Yes


# PutTaxInheritanceRequest

### heritageStatus
- **Type**: typing.Optional[typing.Literal['OptIn', 'OptOut']]


# PutTaxRegistrationRequest

### taxRegistrationEntry
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.TaxRegistrationEntry'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]


# PutTaxRegistrationResponse

### status
- **Type**: typing.Literal['Deleted', 'Pending', 'Rejected', 'Verified']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.ResponseMetadata'>
- **Required**: Yes


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


# RomaniaAdditionalInfo

### taxRegistrationNumberType
- **Type**: typing.Literal['LocalRegistrationNumber', 'TaxRegistrationNumber']
- **Required**: Yes


# SaudiArabiaAdditionalInfo

### taxRegistrationNumberType
- **Type**: typing.Optional[typing.Literal['CommercialRegistrationNumber', 'TaxIdentificationNumber', 'TaxRegistrationNumber']]


# SourceS3Location

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes


# SouthKoreaAdditionalInfo

### businessRepresentativeName
- **Type**: <class 'str'>
- **Required**: Yes

### itemOfBusiness
- **Type**: <class 'str'>
- **Required**: Yes

### lineOfBusiness
- **Type**: <class 'str'>
- **Required**: Yes


# SpainAdditionalInfo

### registrationType
- **Type**: typing.Literal['Intra-EU', 'Local']
- **Required**: Yes


# SupplementalTaxRegistration

### address
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.Address'>
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


# SupplementalTaxRegistrationEntry

### address
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.Address'>
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


# TaxDocumentMetadata

### taxDocumentAccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### taxDocumentName
- **Type**: <class 'str'>
- **Required**: Yes


# TaxExemption

### authority
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.Authority'>
- **Required**: Yes

### taxExemptionType
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.TaxExemptionType'>
- **Required**: Yes

### effectiveDate
- **Type**: typing.Optional[datetime.datetime]

### expirationDate
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['Expired', 'None', 'Pending', 'Valid']]

### systemEffectiveDate
- **Type**: typing.Optional[datetime.datetime]


# TaxExemptionDetails

### heritageObtainedDetails
- **Type**: typing.Optional[bool]

### heritageObtainedParentEntity
- **Type**: typing.Optional[str]

### heritageObtainedReason
- **Type**: typing.Optional[str]

### taxExemptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.taxsettings_classes.TaxExemption]]


# TaxExemptionType

### applicableJurisdictions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.taxsettings_classes.Authority]]

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]


# TaxInheritanceDetails

### inheritanceObtainedReason
- **Type**: typing.Optional[str]

### parentEntityId
- **Type**: typing.Optional[str]


# TaxRegistration

### legalAddress
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.Address'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.AdditionalInfoResponse]

### certifiedEmailId
- **Type**: typing.Optional[str]

### sector
- **Type**: typing.Optional[typing.Literal['Business', 'Government', 'Individual']]

### taxDocumentMetadatas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.taxsettings_classes.TaxDocumentMetadata]]


# TaxRegistrationDocFile

### fileContent
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.Blob'>
- **Required**: Yes

### fileName
- **Type**: <class 'str'>
- **Required**: Yes


# TaxRegistrationDocument

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.TaxRegistrationDocFile]

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.SourceS3Location]


# TaxRegistrationEntry

### registrationId
- **Type**: <class 'str'>
- **Required**: Yes

### registrationType
- **Type**: typing.Literal['CNPJ', 'CPF', 'GST', 'NRIC', 'SST', 'TIN', 'VAT']
- **Required**: Yes

### additionalTaxInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.AdditionalInfoRequest]

### certifiedEmailId
- **Type**: typing.Optional[str]

### legalAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.Address]

### legalName
- **Type**: typing.Optional[str]

### sector
- **Type**: typing.Optional[typing.Literal['Business', 'Government', 'Individual']]

### verificationDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.VerificationDetails]


# TaxRegistrationWithJurisdiction

### jurisdiction
- **Type**: <class 'aws_resource_validator.pydantic_models.taxsettings_classes.Jurisdiction'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.taxsettings_classes.AdditionalInfoResponse]

### certifiedEmailId
- **Type**: typing.Optional[str]

### sector
- **Type**: typing.Optional[typing.Literal['Business', 'Government', 'Individual']]

### taxDocumentMetadatas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.taxsettings_classes.TaxDocumentMetadata]]


# TurkeyAdditionalInfo

### industries
- **Type**: typing.Optional[typing.Literal['Banks', 'CirculatingOrg', 'DevelopmentAgencies', 'Insurance', 'PensionAndBenefitFunds', 'ProfessionalOrg']]

### kepEmailId
- **Type**: typing.Optional[str]

### secondaryTaxId
- **Type**: typing.Optional[str]

### taxOffice
- **Type**: typing.Optional[str]


# UkraineAdditionalInfo

### ukraineTrnType
- **Type**: typing.Literal['Business', 'Individual']
- **Required**: Yes


# VerificationDetails

### dateOfBirth
- **Type**: typing.Optional[str]

### taxRegistrationDocuments
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.taxsettings_classes.TaxRegistrationDocument]]


# VietnamAdditionalInfo

### electronicTransactionCodeNumber
- **Type**: typing.Optional[str]

### enterpriseIdentificationNumber
- **Type**: typing.Optional[str]

### paymentVoucherNumber
- **Type**: typing.Optional[str]

### paymentVoucherNumberDate
- **Type**: typing.Optional[str]


