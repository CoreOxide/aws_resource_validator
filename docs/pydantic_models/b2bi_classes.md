# Pydantic Models in b2bi_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CapabilityConfigurationTypeDef

### edi
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.EdiConfigurationTypeDef]


# CapabilitySummaryTypeDef

### capabilityId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['edi']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### modifiedAt
- **Type**: typing.Optional[datetime.datetime]


# CreateCapabilityRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['edi']
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.CapabilityConfigurationTypeDef'>
- **Required**: Yes

### instructionsDocuments
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.b2bi_classes.S3LocationTypeDef]]

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.b2bi_classes.TagTypeDef]]


# CreateCapabilityResponseTypeDef

### capabilityId
- **Type**: <class 'str'>
- **Required**: Yes

### capabilityArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['edi']
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.CapabilityConfigurationTypeDef'>
- **Required**: Yes

### instructionsDocuments
- **Type**: typing.List[aws_resource_validator.pydantic_models.b2bi_classes.S3LocationTypeDef]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePartnershipRequestRequestTypeDef

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

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.b2bi_classes.TagTypeDef]]


# CreatePartnershipResponseTypeDef

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

### tradingPartnerId
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProfileRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.b2bi_classes.TagTypeDef]]


# CreateProfileResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTransformerRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### fileFormat
- **Type**: typing.Literal['JSON', 'XML']
- **Required**: Yes

### mappingTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### ediType
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.EdiTypeTypeDef'>
- **Required**: Yes

### sampleDocument
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.b2bi_classes.TagTypeDef]]


# CreateTransformerResponseTypeDef

### transformerId
- **Type**: <class 'str'>
- **Required**: Yes

### transformerArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### fileFormat
- **Type**: typing.Literal['JSON', 'XML']
- **Required**: Yes

### mappingTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['active', 'inactive']
- **Required**: Yes

### ediType
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.EdiTypeTypeDef'>
- **Required**: Yes

### sampleDocument
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteCapabilityRequestRequestTypeDef

### capabilityId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePartnershipRequestRequestTypeDef

### partnershipId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProfileRequestRequestTypeDef

### profileId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTransformerRequestRequestTypeDef

### transformerId
- **Type**: <class 'str'>
- **Required**: Yes


# EdiConfigurationTypeDef

### type
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.EdiTypeTypeDef'>
- **Required**: Yes

### inputLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.S3LocationTypeDef'>
- **Required**: Yes

### outputLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.S3LocationTypeDef'>
- **Required**: Yes

### transformerId
- **Type**: <class 'str'>
- **Required**: Yes


# EdiTypeTypeDef

### x12Details
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.X12DetailsTypeDef]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCapabilityRequestRequestTypeDef

### capabilityId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCapabilityResponseTypeDef

### capabilityId
- **Type**: <class 'str'>
- **Required**: Yes

### capabilityArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['edi']
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.CapabilityConfigurationTypeDef'>
- **Required**: Yes

### instructionsDocuments
- **Type**: typing.List[aws_resource_validator.pydantic_models.b2bi_classes.S3LocationTypeDef]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### modifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPartnershipRequestRequestTypeDef

### partnershipId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPartnershipResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetProfileRequestRequestTypeDef

### profileId
- **Type**: <class 'str'>
- **Required**: Yes


# GetProfileResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTransformerJobRequestRequestTypeDef

### transformerJobId
- **Type**: <class 'str'>
- **Required**: Yes

### transformerId
- **Type**: <class 'str'>
- **Required**: Yes


# GetTransformerJobResponseTypeDef

### status
- **Type**: typing.Literal['failed', 'running', 'succeeded']
- **Required**: Yes

### outputFiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.b2bi_classes.S3LocationTypeDef]
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTransformerRequestRequestTypeDef

### transformerId
- **Type**: <class 'str'>
- **Required**: Yes


# GetTransformerResponseTypeDef

### transformerId
- **Type**: <class 'str'>
- **Required**: Yes

### transformerArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### fileFormat
- **Type**: typing.Literal['JSON', 'XML']
- **Required**: Yes

### mappingTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['active', 'inactive']
- **Required**: Yes

### ediType
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.EdiTypeTypeDef'>
- **Required**: Yes

### sampleDocument
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### modifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCapabilitiesRequestListCapabilitiesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.PaginatorConfigTypeDef]


# ListCapabilitiesRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCapabilitiesResponseTypeDef

### capabilities
- **Type**: typing.List[aws_resource_validator.pydantic_models.b2bi_classes.CapabilitySummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPartnershipsRequestListPartnershipsPaginateTypeDef

### profileId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.PaginatorConfigTypeDef]


# ListPartnershipsRequestRequestTypeDef

### profileId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPartnershipsResponseTypeDef

### partnerships
- **Type**: typing.List[aws_resource_validator.pydantic_models.b2bi_classes.PartnershipSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProfilesRequestListProfilesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.PaginatorConfigTypeDef]


# ListProfilesRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListProfilesResponseTypeDef

### profiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.b2bi_classes.ProfileSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.b2bi_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTransformersRequestListTransformersPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.PaginatorConfigTypeDef]


# ListTransformersRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTransformersResponseTypeDef

### transformers
- **Type**: typing.List[aws_resource_validator.pydantic_models.b2bi_classes.TransformerSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PartnershipSummaryTypeDef

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

### tradingPartnerId
- **Type**: typing.Optional[str]

### modifiedAt
- **Type**: typing.Optional[datetime.datetime]


# ProfileSummaryTypeDef

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


# S3LocationTypeDef

### bucketName
- **Type**: typing.Optional[str]

### key
- **Type**: typing.Optional[str]


# StartTransformerJobRequestRequestTypeDef

### inputFile
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.S3LocationTypeDef'>
- **Required**: Yes

### outputLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.S3LocationTypeDef'>
- **Required**: Yes

### transformerId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# StartTransformerJobResponseTypeDef

### transformerJobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.b2bi_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TestMappingRequestRequestTypeDef

### inputFileContent
- **Type**: <class 'str'>
- **Required**: Yes

### mappingTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### fileFormat
- **Type**: typing.Literal['JSON', 'XML']
- **Required**: Yes


# TestMappingResponseTypeDef

### mappedFileContent
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TestParsingRequestRequestTypeDef

### inputFile
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.S3LocationTypeDef'>
- **Required**: Yes

### fileFormat
- **Type**: typing.Literal['JSON', 'XML']
- **Required**: Yes

### ediType
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.EdiTypeTypeDef'>
- **Required**: Yes


# TestParsingResponseTypeDef

### parsedFileContent
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TransformerSummaryTypeDef

### transformerId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### fileFormat
- **Type**: typing.Literal['JSON', 'XML']
- **Required**: Yes

### mappingTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['active', 'inactive']
- **Required**: Yes

### ediType
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.EdiTypeTypeDef'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### sampleDocument
- **Type**: typing.Optional[str]

### modifiedAt
- **Type**: typing.Optional[datetime.datetime]


# UntagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateCapabilityRequestRequestTypeDef

### capabilityId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.CapabilityConfigurationTypeDef]

### instructionsDocuments
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.b2bi_classes.S3LocationTypeDef]]


# UpdateCapabilityResponseTypeDef

### capabilityId
- **Type**: <class 'str'>
- **Required**: Yes

### capabilityArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['edi']
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.CapabilityConfigurationTypeDef'>
- **Required**: Yes

### instructionsDocuments
- **Type**: typing.List[aws_resource_validator.pydantic_models.b2bi_classes.S3LocationTypeDef]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### modifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePartnershipRequestRequestTypeDef

### partnershipId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### capabilities
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdatePartnershipResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateProfileRequestRequestTypeDef

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


# UpdateProfileResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTransformerRequestRequestTypeDef

### transformerId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### fileFormat
- **Type**: typing.Optional[typing.Literal['JSON', 'XML']]

### mappingTemplate
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['active', 'inactive']]

### ediType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.b2bi_classes.EdiTypeTypeDef]

### sampleDocument
- **Type**: typing.Optional[str]


# UpdateTransformerResponseTypeDef

### transformerId
- **Type**: <class 'str'>
- **Required**: Yes

### transformerArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### fileFormat
- **Type**: typing.Literal['JSON', 'XML']
- **Required**: Yes

### mappingTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['active', 'inactive']
- **Required**: Yes

### ediType
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.EdiTypeTypeDef'>
- **Required**: Yes

### sampleDocument
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### modifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.b2bi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# X12DetailsTypeDef

### transactionSet
- **Type**: typing.Optional[typing.Literal['X12_110', 'X12_180', 'X12_204', 'X12_210', 'X12_211', 'X12_214', 'X12_215', 'X12_259', 'X12_260', 'X12_266', 'X12_269', 'X12_270', 'X12_270_X279', 'X12_271', 'X12_271_X279', 'X12_274', 'X12_275', 'X12_275_X210', 'X12_275_X211', 'X12_276', 'X12_276_X212', 'X12_277', 'X12_277_X212', 'X12_277_X214', 'X12_277_X364', 'X12_278', 'X12_278_X217', 'X12_310', 'X12_315', 'X12_322', 'X12_404', 'X12_410', 'X12_417', 'X12_421', 'X12_426', 'X12_810', 'X12_820', 'X12_820_X218', 'X12_820_X306', 'X12_824', 'X12_824_X186', 'X12_830', 'X12_832', 'X12_834', 'X12_834_X220', 'X12_834_X307', 'X12_834_X318', 'X12_835', 'X12_835_X221', 'X12_837', 'X12_837_X222', 'X12_837_X223', 'X12_837_X224', 'X12_837_X291', 'X12_837_X292', 'X12_837_X298', 'X12_844', 'X12_846', 'X12_849', 'X12_850', 'X12_852', 'X12_855', 'X12_856', 'X12_860', 'X12_861', 'X12_864', 'X12_865', 'X12_869', 'X12_870', 'X12_940', 'X12_945', 'X12_990', 'X12_997', 'X12_999', 'X12_999_X231']]

### version
- **Type**: typing.Optional[typing.Literal['VERSION_4010', 'VERSION_4030', 'VERSION_5010', 'VERSION_5010_HIPAA']]


