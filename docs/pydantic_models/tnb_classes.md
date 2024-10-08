# Pydantic Models in tnb_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelSolNetworkOperationInputRequestTypeDef

### nsLcmOpOccId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateSolFunctionPackageInputRequestTypeDef

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateSolFunctionPackageOutputTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### onboardingState
- **Type**: typing.Literal['CREATED', 'ERROR', 'ONBOARDED']
- **Required**: Yes

### operationalState
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### usageState
- **Type**: typing.Literal['IN_USE', 'NOT_IN_USE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSolNetworkInstanceInputRequestTypeDef

### nsName
- **Type**: <class 'str'>
- **Required**: Yes

### nsdInfoId
- **Type**: <class 'str'>
- **Required**: Yes

### nsDescription
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateSolNetworkInstanceOutputTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### nsInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### nsdInfoId
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSolNetworkPackageInputRequestTypeDef

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateSolNetworkPackageOutputTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### nsdOnboardingState
- **Type**: typing.Literal['CREATED', 'ERROR', 'ONBOARDED']
- **Required**: Yes

### nsdOperationalState
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### nsdUsageState
- **Type**: typing.Literal['IN_USE', 'NOT_IN_USE']
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteSolFunctionPackageInputRequestTypeDef

### vnfPkgId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSolNetworkInstanceInputRequestTypeDef

### nsInstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSolNetworkPackageInputRequestTypeDef

### nsdInfoId
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ErrorInfoTypeDef

### cause
- **Type**: typing.Optional[str]

### details
- **Type**: typing.Optional[str]


# FunctionArtifactMetaTypeDef

### overrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.tnb_classes.ToscaOverrideTypeDef]]


# GetSolFunctionInstanceInputRequestTypeDef

### vnfInstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSolFunctionInstanceMetadataTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# GetSolFunctionInstanceOutputTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### instantiatedVnfInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.GetSolVnfInfoTypeDef'>
- **Required**: Yes

### instantiationState
- **Type**: typing.Literal['INSTANTIATED', 'NOT_INSTANTIATED']
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.GetSolFunctionInstanceMetadataTypeDef'>
- **Required**: Yes

### nsInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### vnfPkgId
- **Type**: <class 'str'>
- **Required**: Yes

### vnfProductName
- **Type**: <class 'str'>
- **Required**: Yes

### vnfProvider
- **Type**: <class 'str'>
- **Required**: Yes

### vnfdId
- **Type**: <class 'str'>
- **Required**: Yes

### vnfdVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSolFunctionPackageContentInputRequestTypeDef

### accept
- **Type**: typing.Literal['application/zip']
- **Required**: Yes

### vnfPkgId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSolFunctionPackageContentOutputTypeDef

### contentType
- **Type**: typing.Literal['application/zip']
- **Required**: Yes

### packageContent
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSolFunctionPackageDescriptorInputRequestTypeDef

### accept
- **Type**: typing.Literal['text/plain']
- **Required**: Yes

### vnfPkgId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSolFunctionPackageDescriptorOutputTypeDef

### contentType
- **Type**: typing.Literal['text/plain']
- **Required**: Yes

### vnfd
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSolFunctionPackageInputRequestTypeDef

### vnfPkgId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSolFunctionPackageMetadataTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### vnfd
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.FunctionArtifactMetaTypeDef]


# GetSolFunctionPackageOutputTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.GetSolFunctionPackageMetadataTypeDef'>
- **Required**: Yes

### onboardingState
- **Type**: typing.Literal['CREATED', 'ERROR', 'ONBOARDED']
- **Required**: Yes

### operationalState
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### usageState
- **Type**: typing.Literal['IN_USE', 'NOT_IN_USE']
- **Required**: Yes

### vnfProductName
- **Type**: <class 'str'>
- **Required**: Yes

### vnfProvider
- **Type**: <class 'str'>
- **Required**: Yes

### vnfdId
- **Type**: <class 'str'>
- **Required**: Yes

### vnfdVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSolInstantiatedVnfInfoTypeDef

### vnfState
- **Type**: typing.Optional[typing.Literal['STARTED', 'STOPPED']]


# GetSolNetworkInstanceInputRequestTypeDef

### nsInstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSolNetworkInstanceMetadataTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# GetSolNetworkInstanceOutputTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lcmOpInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.LcmOperationInfoTypeDef'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.GetSolNetworkInstanceMetadataTypeDef'>
- **Required**: Yes

### nsInstanceDescription
- **Type**: <class 'str'>
- **Required**: Yes

### nsInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### nsState
- **Type**: typing.Literal['DELETED', 'IMPAIRED', 'INSTANTIATED', 'INSTANTIATE_IN_PROGRESS', 'NOT_INSTANTIATED', 'STOPPED', 'TERMINATE_IN_PROGRESS', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### nsdId
- **Type**: <class 'str'>
- **Required**: Yes

### nsdInfoId
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSolNetworkOperationInputRequestTypeDef

### nsLcmOpOccId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSolNetworkOperationMetadataTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# GetSolNetworkOperationOutputTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### error
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ProblemDetailsTypeDef'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lcmOperationType
- **Type**: typing.Literal['INSTANTIATE', 'TERMINATE', 'UPDATE']
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.GetSolNetworkOperationMetadataTypeDef'>
- **Required**: Yes

### nsInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### operationState
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'FAILED', 'PROCESSING']
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.tnb_classes.GetSolNetworkOperationTaskDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSolNetworkOperationTaskDetailsTypeDef

### taskContext
- **Type**: typing.Optional[typing.Dict[str, str]]

### taskEndTime
- **Type**: typing.Optional[datetime.datetime]

### taskErrorDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.ErrorInfoTypeDef]

### taskName
- **Type**: typing.Optional[str]

### taskStartTime
- **Type**: typing.Optional[datetime.datetime]

### taskStatus
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'ERROR', 'IN_PROGRESS', 'SCHEDULED', 'SKIPPED', 'STARTED']]


# GetSolNetworkPackageContentInputRequestTypeDef

### accept
- **Type**: typing.Literal['application/zip']
- **Required**: Yes

### nsdInfoId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSolNetworkPackageContentOutputTypeDef

### contentType
- **Type**: typing.Literal['application/zip']
- **Required**: Yes

### nsdContent
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSolNetworkPackageDescriptorInputRequestTypeDef

### nsdInfoId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSolNetworkPackageDescriptorOutputTypeDef

### contentType
- **Type**: typing.Literal['text/plain']
- **Required**: Yes

### nsd
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSolNetworkPackageInputRequestTypeDef

### nsdInfoId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSolNetworkPackageMetadataTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### nsd
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.NetworkArtifactMetaTypeDef]


# GetSolNetworkPackageOutputTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.GetSolNetworkPackageMetadataTypeDef'>
- **Required**: Yes

### nsdId
- **Type**: <class 'str'>
- **Required**: Yes

### nsdName
- **Type**: <class 'str'>
- **Required**: Yes

### nsdOnboardingState
- **Type**: typing.Literal['CREATED', 'ERROR', 'ONBOARDED']
- **Required**: Yes

### nsdOperationalState
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### nsdUsageState
- **Type**: typing.Literal['IN_USE', 'NOT_IN_USE']
- **Required**: Yes

### nsdVersion
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### vnfPkgIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSolVnfInfoTypeDef

### vnfState
- **Type**: typing.Optional[typing.Literal['STARTED', 'STOPPED']]

### vnfcResourceInfo
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.tnb_classes.GetSolVnfcResourceInfoTypeDef]]


# GetSolVnfcResourceInfoMetadataTypeDef

### cluster
- **Type**: typing.Optional[str]

### helmChart
- **Type**: typing.Optional[str]

### nodeGroup
- **Type**: typing.Optional[str]


# GetSolVnfcResourceInfoTypeDef

### metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.GetSolVnfcResourceInfoMetadataTypeDef]


# InstantiateSolNetworkInstanceInputRequestTypeDef

### nsInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### additionalParamsForNs
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### dryRun
- **Type**: typing.Optional[bool]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# InstantiateSolNetworkInstanceOutputTypeDef

### nsLcmOpOccId
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LcmOperationInfoTypeDef

### nsLcmOpOccId
- **Type**: <class 'str'>
- **Required**: Yes


# ListSolFunctionInstanceInfoTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### instantiationState
- **Type**: typing.Literal['INSTANTIATED', 'NOT_INSTANTIATED']
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ListSolFunctionInstanceMetadataTypeDef'>
- **Required**: Yes

### nsInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### vnfPkgId
- **Type**: <class 'str'>
- **Required**: Yes

### instantiatedVnfInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.GetSolInstantiatedVnfInfoTypeDef]

### vnfPkgName
- **Type**: typing.Optional[str]


# ListSolFunctionInstanceMetadataTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ListSolFunctionInstancesInputListSolFunctionInstancesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.PaginatorConfigTypeDef]


# ListSolFunctionInstancesInputRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSolFunctionInstancesOutputTypeDef

### functionInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.tnb_classes.ListSolFunctionInstanceInfoTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSolFunctionPackageInfoTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### onboardingState
- **Type**: typing.Literal['CREATED', 'ERROR', 'ONBOARDED']
- **Required**: Yes

### operationalState
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### usageState
- **Type**: typing.Literal['IN_USE', 'NOT_IN_USE']
- **Required**: Yes

### metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.ListSolFunctionPackageMetadataTypeDef]

### vnfProductName
- **Type**: typing.Optional[str]

### vnfProvider
- **Type**: typing.Optional[str]

### vnfdId
- **Type**: typing.Optional[str]

### vnfdVersion
- **Type**: typing.Optional[str]


# ListSolFunctionPackageMetadataTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ListSolFunctionPackagesInputListSolFunctionPackagesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.PaginatorConfigTypeDef]


# ListSolFunctionPackagesInputRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSolFunctionPackagesOutputTypeDef

### functionPackages
- **Type**: typing.List[aws_resource_validator.pydantic_models.tnb_classes.ListSolFunctionPackageInfoTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSolNetworkInstanceInfoTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ListSolNetworkInstanceMetadataTypeDef'>
- **Required**: Yes

### nsInstanceDescription
- **Type**: <class 'str'>
- **Required**: Yes

### nsInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### nsState
- **Type**: typing.Literal['DELETED', 'IMPAIRED', 'INSTANTIATED', 'INSTANTIATE_IN_PROGRESS', 'NOT_INSTANTIATED', 'STOPPED', 'TERMINATE_IN_PROGRESS', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### nsdId
- **Type**: <class 'str'>
- **Required**: Yes

### nsdInfoId
- **Type**: <class 'str'>
- **Required**: Yes


# ListSolNetworkInstanceMetadataTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ListSolNetworkInstancesInputListSolNetworkInstancesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.PaginatorConfigTypeDef]


# ListSolNetworkInstancesInputRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSolNetworkInstancesOutputTypeDef

### networkInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.tnb_classes.ListSolNetworkInstanceInfoTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSolNetworkOperationsInfoTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lcmOperationType
- **Type**: typing.Literal['INSTANTIATE', 'TERMINATE', 'UPDATE']
- **Required**: Yes

### nsInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### operationState
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'FAILED', 'PROCESSING']
- **Required**: Yes

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.ProblemDetailsTypeDef]

### metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.ListSolNetworkOperationsMetadataTypeDef]


# ListSolNetworkOperationsInputListSolNetworkOperationsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.PaginatorConfigTypeDef]


# ListSolNetworkOperationsInputRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSolNetworkOperationsMetadataTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ListSolNetworkOperationsOutputTypeDef

### networkOperations
- **Type**: typing.List[aws_resource_validator.pydantic_models.tnb_classes.ListSolNetworkOperationsInfoTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSolNetworkPackageInfoTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ListSolNetworkPackageMetadataTypeDef'>
- **Required**: Yes

### nsdOnboardingState
- **Type**: typing.Literal['CREATED', 'ERROR', 'ONBOARDED']
- **Required**: Yes

### nsdOperationalState
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### nsdUsageState
- **Type**: typing.Literal['IN_USE', 'NOT_IN_USE']
- **Required**: Yes

### nsdDesigner
- **Type**: typing.Optional[str]

### nsdId
- **Type**: typing.Optional[str]

### nsdInvariantId
- **Type**: typing.Optional[str]

### nsdName
- **Type**: typing.Optional[str]

### nsdVersion
- **Type**: typing.Optional[str]

### vnfPkgIds
- **Type**: typing.Optional[typing.List[str]]


# ListSolNetworkPackageMetadataTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ListSolNetworkPackagesInputListSolNetworkPackagesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.PaginatorConfigTypeDef]


# ListSolNetworkPackagesInputRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSolNetworkPackagesOutputTypeDef

### networkPackages
- **Type**: typing.List[aws_resource_validator.pydantic_models.tnb_classes.ListSolNetworkPackageInfoTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceInputRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutputTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# NetworkArtifactMetaTypeDef

### overrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.tnb_classes.ToscaOverrideTypeDef]]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProblemDetailsTypeDef

### detail
- **Type**: <class 'str'>
- **Required**: Yes

### title
- **Type**: typing.Optional[str]


# PutSolFunctionPackageContentInputRequestTypeDef

### file
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### vnfPkgId
- **Type**: <class 'str'>
- **Required**: Yes

### contentType
- **Type**: typing.Optional[typing.Literal['application/zip']]


# PutSolFunctionPackageContentMetadataTypeDef

### vnfd
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.FunctionArtifactMetaTypeDef]


# PutSolFunctionPackageContentOutputTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.PutSolFunctionPackageContentMetadataTypeDef'>
- **Required**: Yes

### vnfProductName
- **Type**: <class 'str'>
- **Required**: Yes

### vnfProvider
- **Type**: <class 'str'>
- **Required**: Yes

### vnfdId
- **Type**: <class 'str'>
- **Required**: Yes

### vnfdVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutSolNetworkPackageContentInputRequestTypeDef

### file
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### nsdInfoId
- **Type**: <class 'str'>
- **Required**: Yes

### contentType
- **Type**: typing.Optional[typing.Literal['application/zip']]


# PutSolNetworkPackageContentMetadataTypeDef

### nsd
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.NetworkArtifactMetaTypeDef]


# PutSolNetworkPackageContentOutputTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.PutSolNetworkPackageContentMetadataTypeDef'>
- **Required**: Yes

### nsdId
- **Type**: <class 'str'>
- **Required**: Yes

### nsdName
- **Type**: <class 'str'>
- **Required**: Yes

### nsdVersion
- **Type**: <class 'str'>
- **Required**: Yes

### vnfPkgIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# TagResourceInputRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TerminateSolNetworkInstanceInputRequestTypeDef

### nsInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# TerminateSolNetworkInstanceOutputTypeDef

### nsLcmOpOccId
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ToscaOverrideTypeDef

### defaultValue
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# UntagResourceInputRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateSolFunctionPackageInputRequestTypeDef

### operationalState
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### vnfPkgId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateSolFunctionPackageOutputTypeDef

### operationalState
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSolNetworkInstanceInputRequestTypeDef

### nsInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### updateType
- **Type**: typing.Literal['MODIFY_VNF_INFORMATION']
- **Required**: Yes

### modifyVnfInfoData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.UpdateSolNetworkModifyTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# UpdateSolNetworkInstanceOutputTypeDef

### nsLcmOpOccId
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSolNetworkModifyTypeDef

### vnfConfigurableProperties
- **Type**: typing.Mapping[str, typing.Any]
- **Required**: Yes

### vnfInstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateSolNetworkPackageInputRequestTypeDef

### nsdInfoId
- **Type**: <class 'str'>
- **Required**: Yes

### nsdOperationalState
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# UpdateSolNetworkPackageOutputTypeDef

### nsdOperationalState
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ValidateSolFunctionPackageContentInputRequestTypeDef

### file
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### vnfPkgId
- **Type**: <class 'str'>
- **Required**: Yes

### contentType
- **Type**: typing.Optional[typing.Literal['application/zip']]


# ValidateSolFunctionPackageContentMetadataTypeDef

### vnfd
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.FunctionArtifactMetaTypeDef]


# ValidateSolFunctionPackageContentOutputTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ValidateSolFunctionPackageContentMetadataTypeDef'>
- **Required**: Yes

### vnfProductName
- **Type**: <class 'str'>
- **Required**: Yes

### vnfProvider
- **Type**: <class 'str'>
- **Required**: Yes

### vnfdId
- **Type**: <class 'str'>
- **Required**: Yes

### vnfdVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ValidateSolNetworkPackageContentInputRequestTypeDef

### file
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### nsdInfoId
- **Type**: <class 'str'>
- **Required**: Yes

### contentType
- **Type**: typing.Optional[typing.Literal['application/zip']]


# ValidateSolNetworkPackageContentMetadataTypeDef

### nsd
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.NetworkArtifactMetaTypeDef]


# ValidateSolNetworkPackageContentOutputTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ValidateSolNetworkPackageContentMetadataTypeDef'>
- **Required**: Yes

### nsdId
- **Type**: <class 'str'>
- **Required**: Yes

### nsdName
- **Type**: <class 'str'>
- **Required**: Yes

### nsdVersion
- **Type**: <class 'str'>
- **Required**: Yes

### vnfPkgIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


