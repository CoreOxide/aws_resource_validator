# B2Bi Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CapabilityConfiguration

### edi
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.EdiConfiguration]


# CapabilityOptions

### outboundEdi
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.OutboundEdiOptions]


# CapabilitySummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConversionSource

### fileFormat
- **Type**: typing.Literal['JSON', 'XML']
- **Required**: Yes

### inputFile
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.InputFileSource'>
- **Required**: Yes


# ConversionTarget

### fileFormat
- **Type**: typing.Literal['X12']
- **Required**: Yes

### formatDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.ConversionTargetFormatDetails]

### outputSampleFile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.OutputSampleFileSource]


# ConversionTargetFormatDetails

### x12
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.X12Details]


# CreatePartnershipRequest

### profileId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### email
- **Type**: <class 'str'>
- **Required**: Yes

### capabilities
- **Type**: typing.Sequence[str]
- **Required**: Yes

### phone
- **Type**: typing.Optional[str]

### capabilityOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.CapabilityOptions]

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.b2bi_classes.Tag]]


# CreatePartnershipResponse

### profileId
- **Type**: <class 'str'>
- **Required**: Yes

### partnershipId
- **Type**: <class 'str'>
- **Required**: Yes

### partnershipArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### email
- **Type**: <class 'str'>
- **Required**: Yes

### phone
- **Type**: <class 'str'>
- **Required**: Yes

### capabilities
- **Type**: typing.List[str]
- **Required**: Yes

### capabilityOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.CapabilityOptions'>
- **Required**: Yes

### tradingPartnerId
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProfileRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### phone
- **Type**: <class 'str'>
- **Required**: Yes

### businessName
- **Type**: <class 'str'>
- **Required**: Yes

### logging
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### email
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.b2bi_classes.Tag]]


# CreateProfileResponse

### profileId
- **Type**: <class 'str'>
- **Required**: Yes

### profileArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### businessName
- **Type**: <class 'str'>
- **Required**: Yes

### phone
- **Type**: <class 'str'>
- **Required**: Yes

### email
- **Type**: <class 'str'>
- **Required**: Yes

### logging
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadata'>
- **Required**: Yes


# CreateStarterMappingTemplateRequest

### mappingType
- **Type**: typing.Literal['JSONATA', 'XSLT']
- **Required**: Yes

### templateDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.TemplateDetails'>
- **Required**: Yes

### outputSampleLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.S3Location]


# CreateStarterMappingTemplateResponse

### mappingTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTransformerRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.b2bi_classes.Tag]]

### fileFormat
- **Type**: typing.Optional[typing.Literal['JSON', 'NOT_USED', 'XML']]

### mappingTemplate
- **Type**: typing.Optional[str]

### ediType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.EdiType]

### sampleDocument
- **Type**: typing.Optional[str]

### inputConversion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.InputConversion]

### mapping
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.MappingType]

### outputConversion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.OutputConversion]

### sampleDocuments
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.SampleDocumentsUnion]


# CreateTransformerResponse

### transformerId
- **Type**: <class 'str'>
- **Required**: Yes

### transformerArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['active', 'inactive']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### fileFormat
- **Type**: typing.Literal['JSON', 'NOT_USED', 'XML']
- **Required**: Yes

### mappingTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### ediType
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.EdiType'>
- **Required**: Yes

### sampleDocument
- **Type**: <class 'str'>
- **Required**: Yes

### inputConversion
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.InputConversion'>
- **Required**: Yes

### mapping
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.MappingType'>
- **Required**: Yes

### outputConversion
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.OutputConversion'>
- **Required**: Yes

### sampleDocuments
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.SampleDocumentsOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteCapabilityRequest

### capabilityId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePartnershipRequest

### partnershipId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProfileRequest

### profileId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTransformerRequest

### transformerId
- **Type**: <class 'str'>
- **Required**: Yes


# EdiConfiguration

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EdiType

### x12Details
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.X12Details]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadata'>
- **Required**: Yes


# FormatOptions

### x12
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.X12Details]


# GenerateMappingRequest

### inputFileContent
- **Type**: <class 'str'>
- **Required**: Yes

### outputFileContent
- **Type**: <class 'str'>
- **Required**: Yes

### mappingType
- **Type**: typing.Literal['JSONATA', 'XSLT']
- **Required**: Yes


# GenerateMappingResponse

### mappingTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### mappingAccuracy
- **Type**: <class 'float'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadata'>
- **Required**: Yes


# GetCapabilityRequest

### capabilityId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPartnershipRequest

### partnershipId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPartnershipResponse

### profileId
- **Type**: <class 'str'>
- **Required**: Yes

### partnershipId
- **Type**: <class 'str'>
- **Required**: Yes

### partnershipArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### email
- **Type**: <class 'str'>
- **Required**: Yes

### phone
- **Type**: <class 'str'>
- **Required**: Yes

### capabilities
- **Type**: typing.List[str]
- **Required**: Yes

### capabilityOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.CapabilityOptions'>
- **Required**: Yes

### tradingPartnerId
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### modifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadata'>
- **Required**: Yes


# GetProfileRequest

### profileId
- **Type**: <class 'str'>
- **Required**: Yes


# GetProfileResponse

### profileId
- **Type**: <class 'str'>
- **Required**: Yes

### profileArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### email
- **Type**: <class 'str'>
- **Required**: Yes

### phone
- **Type**: <class 'str'>
- **Required**: Yes

### businessName
- **Type**: <class 'str'>
- **Required**: Yes

### logging
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### modifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadata'>
- **Required**: Yes


# GetTransformerJobRequest

### transformerJobId
- **Type**: <class 'str'>
- **Required**: Yes

### transformerId
- **Type**: <class 'str'>
- **Required**: Yes


# GetTransformerJobResponse

### status
- **Type**: typing.Literal['failed', 'running', 'succeeded']
- **Required**: Yes

### outputFiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.b2bi_classes.S3Location]
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadata'>
- **Required**: Yes


# GetTransformerRequest

### transformerId
- **Type**: <class 'str'>
- **Required**: Yes


# GetTransformerResponse

### transformerId
- **Type**: <class 'str'>
- **Required**: Yes

### transformerArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['active', 'inactive']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### modifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### fileFormat
- **Type**: typing.Literal['JSON', 'NOT_USED', 'XML']
- **Required**: Yes

### mappingTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### ediType
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.EdiType'>
- **Required**: Yes

### sampleDocument
- **Type**: <class 'str'>
- **Required**: Yes

### inputConversion
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.InputConversion'>
- **Required**: Yes

### mapping
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.MappingType'>
- **Required**: Yes

### outputConversion
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.OutputConversion'>
- **Required**: Yes

### sampleDocuments
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.SampleDocumentsOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadata'>
- **Required**: Yes


# InputConversion

### fromFormat
- **Type**: typing.Literal['X12']
- **Required**: Yes

### formatOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.FormatOptions]


# InputFileSource

### fileContent
- **Type**: typing.Optional[str]


# ListCapabilitiesRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCapabilitiesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.PaginatorConfig]


# ListCapabilitiesResponse

### capabilities
- **Type**: typing.List[aws_resource_validator.pydantic_models.b2bi_classes.CapabilitySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPartnershipsRequest

### profileId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPartnershipsRequestPaginate

### profileId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.PaginatorConfig]


# ListPartnershipsResponse

### partnerships
- **Type**: typing.List[aws_resource_validator.pydantic_models.b2bi_classes.PartnershipSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProfilesRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListProfilesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.PaginatorConfig]


# ListProfilesResponse

### profiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.b2bi_classes.ProfileSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.b2bi_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadata'>
- **Required**: Yes


# ListTransformersRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTransformersRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.PaginatorConfig]


# ListTransformersResponse

### transformers
- **Type**: typing.List[aws_resource_validator.pydantic_models.b2bi_classes.TransformerSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# MappingType

### templateLanguage
- **Type**: typing.Literal['JSONATA', 'XSLT']
- **Required**: Yes

### template
- **Type**: typing.Optional[str]


# OutboundEdiOptions

### x12
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.X12Envelope]


# OutputConversion

### toFormat
- **Type**: typing.Literal['X12']
- **Required**: Yes

### formatOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.FormatOptions]


# OutputSampleFileSource

### fileLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.S3Location]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PartnershipSummary

### profileId
- **Type**: <class 'str'>
- **Required**: Yes

### partnershipId
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### capabilities
- **Type**: typing.Optional[typing.List[str]]

### capabilityOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.CapabilityOptions]

### tradingPartnerId
- **Type**: typing.Optional[str]

### modifiedAt
- **Type**: typing.Optional[datetime.datetime]


# ProfileSummary

### profileId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### businessName
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### logging
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### logGroupName
- **Type**: typing.Optional[str]

### modifiedAt
- **Type**: typing.Optional[datetime.datetime]


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

### bucketName
- **Type**: typing.Optional[str]

### key
- **Type**: typing.Optional[str]


# SampleDocumentKeys

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SampleDocuments

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### keys
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.b2bi_classes.SampleDocumentKeys]
- **Required**: Yes


# SampleDocumentsOutput

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### keys
- **Type**: typing.List[aws_resource_validator.pydantic_models.b2bi_classes.SampleDocumentKeys]
- **Required**: Yes


# SampleDocumentsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StartTransformerJobRequest

### inputFile
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.S3Location'>
- **Required**: Yes

### outputLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.S3Location'>
- **Required**: Yes

### transformerId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# StartTransformerJobResponse

### transformerJobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.b2bi_classes.Tag]
- **Required**: Yes


# TemplateDetails

### x12
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.X12Details]


# TestConversionRequest

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ConversionSource'>
- **Required**: Yes

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ConversionTarget'>
- **Required**: Yes


# TestConversionResponse

### convertedFileContent
- **Type**: <class 'str'>
- **Required**: Yes

### validationMessages
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadata'>
- **Required**: Yes


# TestMappingRequest

### inputFileContent
- **Type**: <class 'str'>
- **Required**: Yes

### mappingTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### fileFormat
- **Type**: typing.Literal['JSON', 'NOT_USED', 'XML']
- **Required**: Yes


# TestMappingResponse

### mappedFileContent
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadata'>
- **Required**: Yes


# TestParsingRequest

### inputFile
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.S3Location'>
- **Required**: Yes

### fileFormat
- **Type**: typing.Literal['JSON', 'NOT_USED', 'XML']
- **Required**: Yes

### ediType
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.EdiType'>
- **Required**: Yes


# TestParsingResponse

### parsedFileContent
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadata'>
- **Required**: Yes


# TransformerSummary

### transformerId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['active', 'inactive']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### modifiedAt
- **Type**: typing.Optional[datetime.datetime]

### fileFormat
- **Type**: typing.Optional[typing.Literal['JSON', 'NOT_USED', 'XML']]

### mappingTemplate
- **Type**: typing.Optional[str]

### ediType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.EdiType]

### sampleDocument
- **Type**: typing.Optional[str]

### inputConversion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.InputConversion]

### mapping
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.MappingType]

### outputConversion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.OutputConversion]

### sampleDocuments
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.SampleDocumentsOutput]


# UntagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateCapabilityRequest

### capabilityId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.CapabilityConfiguration]

### instructionsDocuments
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.b2bi_classes.S3Location]]


# UpdatePartnershipRequest

### partnershipId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### capabilities
- **Type**: typing.Optional[typing.Sequence[str]]

### capabilityOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.CapabilityOptions]


# UpdatePartnershipResponse

### profileId
- **Type**: <class 'str'>
- **Required**: Yes

### partnershipId
- **Type**: <class 'str'>
- **Required**: Yes

### partnershipArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### email
- **Type**: <class 'str'>
- **Required**: Yes

### phone
- **Type**: <class 'str'>
- **Required**: Yes

### capabilities
- **Type**: typing.List[str]
- **Required**: Yes

### capabilityOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.CapabilityOptions'>
- **Required**: Yes

### tradingPartnerId
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### modifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateProfileRequest

### profileId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### email
- **Type**: typing.Optional[str]

### phone
- **Type**: typing.Optional[str]

### businessName
- **Type**: typing.Optional[str]


# UpdateProfileResponse

### profileId
- **Type**: <class 'str'>
- **Required**: Yes

### profileArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### email
- **Type**: <class 'str'>
- **Required**: Yes

### phone
- **Type**: <class 'str'>
- **Required**: Yes

### businessName
- **Type**: <class 'str'>
- **Required**: Yes

### logging
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### modifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTransformerRequest

### transformerId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['active', 'inactive']]

### fileFormat
- **Type**: typing.Optional[typing.Literal['JSON', 'NOT_USED', 'XML']]

### mappingTemplate
- **Type**: typing.Optional[str]

### ediType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.EdiType]

### sampleDocument
- **Type**: typing.Optional[str]

### inputConversion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.InputConversion]

### mapping
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.MappingType]

### outputConversion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.OutputConversion]

### sampleDocuments
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.SampleDocumentsUnion]


# UpdateTransformerResponse

### transformerId
- **Type**: <class 'str'>
- **Required**: Yes

### transformerArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['active', 'inactive']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### modifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### fileFormat
- **Type**: typing.Literal['JSON', 'NOT_USED', 'XML']
- **Required**: Yes

### mappingTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### ediType
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.EdiType'>
- **Required**: Yes

### sampleDocument
- **Type**: <class 'str'>
- **Required**: Yes

### inputConversion
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.InputConversion'>
- **Required**: Yes

### mapping
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.MappingType'>
- **Required**: Yes

### outputConversion
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.OutputConversion'>
- **Required**: Yes

### sampleDocuments
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.SampleDocumentsOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadata'>
- **Required**: Yes


# X12Delimiters

### componentSeparator
- **Type**: typing.Optional[str]

### dataElementSeparator
- **Type**: typing.Optional[str]

### segmentTerminator
- **Type**: typing.Optional[str]


# X12Details

### transactionSet
- **Type**: typing.Optional[typing.Literal['X12_100', 'X12_101', 'X12_102', 'X12_103', 'X12_104', 'X12_105', 'X12_106', 'X12_107', 'X12_108', 'X12_109', 'X12_110', 'X12_111', 'X12_112', 'X12_113', 'X12_120', 'X12_121', 'X12_124', 'X12_125', 'X12_126', 'X12_127', 'X12_128', 'X12_129', 'X12_130', 'X12_131', 'X12_132', 'X12_133', 'X12_135', 'X12_138', 'X12_139', 'X12_140', 'X12_141', 'X12_142', 'X12_143', 'X12_144', 'X12_146', 'X12_147', 'X12_148', 'X12_149', 'X12_150', 'X12_151', 'X12_152', 'X12_153', 'X12_154', 'X12_155', 'X12_157', 'X12_158', 'X12_159', 'X12_160', 'X12_161', 'X12_163', 'X12_170', 'X12_175', 'X12_176', 'X12_179', 'X12_180', 'X12_185', 'X12_186', 'X12_187', 'X12_188', 'X12_189', 'X12_190', 'X12_191', 'X12_194', 'X12_195', 'X12_196', 'X12_197', 'X12_198', 'X12_199', 'X12_200', 'X12_201', 'X12_202', 'X12_203', 'X12_204', 'X12_205', 'X12_206', 'X12_210', 'X12_211', 'X12_212', 'X12_213', 'X12_214', 'X12_215', 'X12_216', 'X12_217', 'X12_218', 'X12_219', 'X12_220', 'X12_222', 'X12_223', 'X12_224', 'X12_225', 'X12_227', 'X12_228', 'X12_240', 'X12_242', 'X12_244', 'X12_245', 'X12_248', 'X12_249', 'X12_250', 'X12_251', 'X12_252', 'X12_255', 'X12_256', 'X12_259', 'X12_260', 'X12_261', 'X12_262', 'X12_263', 'X12_264', 'X12_265', 'X12_266', 'X12_267', 'X12_268', 'X12_269', 'X12_270', 'X12_270_X279', 'X12_271', 'X12_271_X279', 'X12_272', 'X12_273', 'X12_274', 'X12_275', 'X12_275_X210', 'X12_275_X211', 'X12_276', 'X12_276_X212', 'X12_277', 'X12_277_X212', 'X12_277_X214', 'X12_277_X364', 'X12_278', 'X12_278_X217', 'X12_280', 'X12_283', 'X12_284', 'X12_285', 'X12_286', 'X12_288', 'X12_290', 'X12_300', 'X12_301', 'X12_303', 'X12_304', 'X12_309', 'X12_310', 'X12_311', 'X12_312', 'X12_313', 'X12_315', 'X12_317', 'X12_319', 'X12_322', 'X12_323', 'X12_324', 'X12_325', 'X12_326', 'X12_350', 'X12_352', 'X12_353', 'X12_354', 'X12_355', 'X12_356', 'X12_357', 'X12_358', 'X12_361', 'X12_362', 'X12_404', 'X12_410', 'X12_412', 'X12_414', 'X12_417', 'X12_418', 'X12_419', 'X12_420', 'X12_421', 'X12_422', 'X12_423', 'X12_424', 'X12_425', 'X12_426', 'X12_429', 'X12_431', 'X12_432', 'X12_433', 'X12_434', 'X12_435', 'X12_436', 'X12_437', 'X12_440', 'X12_451', 'X12_452', 'X12_453', 'X12_455', 'X12_456', 'X12_460', 'X12_463', 'X12_466', 'X12_468', 'X12_470', 'X12_475', 'X12_485', 'X12_486', 'X12_490', 'X12_492', 'X12_494', 'X12_500', 'X12_501', 'X12_503', 'X12_504', 'X12_511', 'X12_517', 'X12_521', 'X12_527', 'X12_536', 'X12_540', 'X12_561', 'X12_567', 'X12_568', 'X12_601', 'X12_602', 'X12_620', 'X12_625', 'X12_650', 'X12_715', 'X12_753', 'X12_754', 'X12_805', 'X12_806', 'X12_810', 'X12_811', 'X12_812', 'X12_813', 'X12_814', 'X12_815', 'X12_816', 'X12_818', 'X12_819', 'X12_820', 'X12_820_X218', 'X12_820_X306', 'X12_821', 'X12_822', 'X12_823', 'X12_824', 'X12_824_X186', 'X12_826', 'X12_827', 'X12_828', 'X12_829', 'X12_830', 'X12_831', 'X12_832', 'X12_833', 'X12_834', 'X12_834_X220', 'X12_834_X307', 'X12_834_X318', 'X12_835', 'X12_835_X221', 'X12_836', 'X12_837', 'X12_837_X222', 'X12_837_X223', 'X12_837_X224', 'X12_837_X291', 'X12_837_X292', 'X12_837_X298', 'X12_838', 'X12_839', 'X12_840', 'X12_841', 'X12_842', 'X12_843', 'X12_844', 'X12_845', 'X12_846', 'X12_847', 'X12_848', 'X12_849', 'X12_850', 'X12_851', 'X12_852', 'X12_853', 'X12_854', 'X12_855', 'X12_856', 'X12_857', 'X12_858', 'X12_859', 'X12_860', 'X12_861', 'X12_862', 'X12_863', 'X12_864', 'X12_865', 'X12_866', 'X12_867', 'X12_868', 'X12_869', 'X12_870', 'X12_871', 'X12_872', 'X12_873', 'X12_874', 'X12_875', 'X12_876', 'X12_877', 'X12_878', 'X12_879', 'X12_880', 'X12_881', 'X12_882', 'X12_883', 'X12_884', 'X12_885', 'X12_886', 'X12_887', 'X12_888', 'X12_889', 'X12_891', 'X12_893', 'X12_894', 'X12_895', 'X12_896', 'X12_920', 'X12_924', 'X12_925', 'X12_926', 'X12_928', 'X12_940', 'X12_943', 'X12_944', 'X12_945', 'X12_947', 'X12_980', 'X12_990', 'X12_993', 'X12_996', 'X12_997', 'X12_998', 'X12_999', 'X12_999_X231']]

### version
- **Type**: typing.Optional[typing.Literal['VERSION_4010', 'VERSION_4030', 'VERSION_4050', 'VERSION_4060', 'VERSION_5010', 'VERSION_5010_HIPAA']]


# X12Envelope

### common
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.X12OutboundEdiHeaders]


# X12FunctionalGroupHeaders

### applicationSenderCode
- **Type**: typing.Optional[str]

### applicationReceiverCode
- **Type**: typing.Optional[str]

### responsibleAgencyCode
- **Type**: typing.Optional[str]


# X12InterchangeControlHeaders

### senderIdQualifier
- **Type**: typing.Optional[str]

### senderId
- **Type**: typing.Optional[str]

### receiverIdQualifier
- **Type**: typing.Optional[str]

### receiverId
- **Type**: typing.Optional[str]

### repetitionSeparator
- **Type**: typing.Optional[str]

### acknowledgmentRequestedCode
- **Type**: typing.Optional[str]

### usageIndicatorCode
- **Type**: typing.Optional[str]


# X12OutboundEdiHeaders

### interchangeControlHeaders
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.X12InterchangeControlHeaders]

### functionalGroupHeaders
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.X12FunctionalGroupHeaders]

### delimiters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.X12Delimiters]

### validateEdi
- **Type**: typing.Optional[bool]


