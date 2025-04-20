# Tnb Tnb Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelSolNetworkOperationInput

### nsLcmOpOccId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateSolFunctionPackageInput

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateSolFunctionPackageOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSolNetworkInstanceInput

### nsName
- **Type**: <class 'str'>
- **Required**: Yes

### nsdInfoId
- **Type**: <class 'str'>
- **Required**: Yes

### nsDescription
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateSolNetworkInstanceOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSolNetworkPackageInput

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateSolNetworkPackageOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteSolFunctionPackageInput

### vnfPkgId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSolNetworkInstanceInput

### nsInstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSolNetworkPackageInput

### nsdInfoId
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ResponseMetadata'>
- **Required**: Yes


# ErrorInfo

### cause
- **Type**: typing.Optional[str]

### details
- **Type**: typing.Optional[str]


# FunctionArtifactMeta

### overrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.tnb.tnb_classes.ToscaOverride]]


# GetSolFunctionInstanceInput

### vnfInstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSolFunctionInstanceMetadata

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# GetSolFunctionInstanceOutput

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### instantiatedVnfInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.GetSolVnfInfo'>
- **Required**: Yes

### instantiationState
- **Type**: typing.Literal['INSTANTIATED', 'NOT_INSTANTIATED']
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.GetSolFunctionInstanceMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ResponseMetadata'>
- **Required**: Yes


# GetSolFunctionPackageContentInput

### accept
- **Type**: typing.Literal['application/zip']
- **Required**: Yes

### vnfPkgId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSolFunctionPackageContentOutput

### contentType
- **Type**: typing.Literal['application/zip']
- **Required**: Yes

### packageContent
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ResponseMetadata'>
- **Required**: Yes


# GetSolFunctionPackageDescriptorInput

### accept
- **Type**: typing.Literal['text/plain']
- **Required**: Yes

### vnfPkgId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSolFunctionPackageDescriptorOutput

### contentType
- **Type**: typing.Literal['text/plain']
- **Required**: Yes

### vnfd
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ResponseMetadata'>
- **Required**: Yes


# GetSolFunctionPackageInput

### vnfPkgId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSolFunctionPackageMetadata

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### vnfd
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb.tnb_classes.FunctionArtifactMeta]


# GetSolFunctionPackageOutput

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.GetSolFunctionPackageMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ResponseMetadata'>
- **Required**: Yes


# GetSolInstantiatedVnfInfo

### vnfState
- **Type**: typing.Optional[typing.Literal['STARTED', 'STOPPED']]


# GetSolNetworkInstanceInput

### nsInstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSolNetworkInstanceMetadata

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# GetSolNetworkInstanceOutput

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lcmOpInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.LcmOperationInfo'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.GetSolNetworkInstanceMetadata'>
- **Required**: Yes

### nsInstanceDescription
- **Type**: <class 'str'>
- **Required**: Yes

### nsInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### nsState
- **Type**: typing.Literal['DELETED', 'IMPAIRED', 'INSTANTIATED', 'INSTANTIATE_IN_PROGRESS', 'INTENT_TO_UPDATE_IN_PROGRESS', 'NOT_INSTANTIATED', 'STOPPED', 'TERMINATE_IN_PROGRESS', 'UPDATED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']
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
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ResponseMetadata'>
- **Required**: Yes


# GetSolNetworkOperationInput

### nsLcmOpOccId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSolNetworkOperationMetadata

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### instantiateMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb.tnb_classes.InstantiateMetadata]

### modifyVnfInfoMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb.tnb_classes.ModifyVnfInfoMetadata]

### updateNsMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb.tnb_classes.UpdateNsMetadata]


# GetSolNetworkOperationOutput

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### error
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ProblemDetails'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lcmOperationType
- **Type**: typing.Literal['INSTANTIATE', 'TERMINATE', 'UPDATE']
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.GetSolNetworkOperationMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.tnb.tnb_classes.GetSolNetworkOperationTaskDetails]
- **Required**: Yes

### updateType
- **Type**: typing.Literal['MODIFY_VNF_INFORMATION', 'UPDATE_NS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ResponseMetadata'>
- **Required**: Yes


# GetSolNetworkOperationTaskDetails

### taskContext
- **Type**: typing.Optional[typing.Dict[str, str]]

### taskEndTime
- **Type**: typing.Optional[datetime.datetime]

### taskErrorDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb.tnb_classes.ErrorInfo]

### taskName
- **Type**: typing.Optional[str]

### taskStartTime
- **Type**: typing.Optional[datetime.datetime]

### taskStatus
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'ERROR', 'IN_PROGRESS', 'SCHEDULED', 'SKIPPED', 'STARTED']]


# GetSolNetworkPackageContentInput

### accept
- **Type**: typing.Literal['application/zip']
- **Required**: Yes

### nsdInfoId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSolNetworkPackageContentOutput

### contentType
- **Type**: typing.Literal['application/zip']
- **Required**: Yes

### nsdContent
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ResponseMetadata'>
- **Required**: Yes


# GetSolNetworkPackageDescriptorInput

### nsdInfoId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSolNetworkPackageDescriptorOutput

### contentType
- **Type**: typing.Literal['text/plain']
- **Required**: Yes

### nsd
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ResponseMetadata'>
- **Required**: Yes


# GetSolNetworkPackageInput

### nsdInfoId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSolNetworkPackageMetadata

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### nsd
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb.tnb_classes.NetworkArtifactMeta]


# GetSolNetworkPackageOutput

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.GetSolNetworkPackageMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ResponseMetadata'>
- **Required**: Yes


# GetSolVnfInfo

### vnfState
- **Type**: typing.Optional[typing.Literal['STARTED', 'STOPPED']]

### vnfcResourceInfo
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.tnb.tnb_classes.GetSolVnfcResourceInfo]]


# GetSolVnfcResourceInfo

### metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb.tnb_classes.GetSolVnfcResourceInfoMetadata]


# GetSolVnfcResourceInfoMetadata

### cluster
- **Type**: typing.Optional[str]

### helmChart
- **Type**: typing.Optional[str]

### nodeGroup
- **Type**: typing.Optional[str]


# InstantiateMetadata

### nsdInfoId
- **Type**: <class 'str'>
- **Required**: Yes

### additionalParamsForNs
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# InstantiateSolNetworkInstanceInput

### nsInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### additionalParamsForNs
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### dryRun
- **Type**: typing.Optional[bool]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# InstantiateSolNetworkInstanceOutput

### nsLcmOpOccId
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ResponseMetadata'>
- **Required**: Yes


# LcmOperationInfo

### nsLcmOpOccId
- **Type**: <class 'str'>
- **Required**: Yes


# ListSolFunctionInstanceInfo

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
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ListSolFunctionInstanceMetadata'>
- **Required**: Yes

### nsInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### vnfPkgId
- **Type**: <class 'str'>
- **Required**: Yes

### instantiatedVnfInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb.tnb_classes.GetSolInstantiatedVnfInfo]

### vnfPkgName
- **Type**: typing.Optional[str]


# ListSolFunctionInstanceMetadata

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ListSolFunctionInstancesInput

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSolFunctionInstancesInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb.tnb_classes.PaginatorConfig]


# ListSolFunctionInstancesOutput

### functionInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.tnb.tnb_classes.ListSolFunctionInstanceInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSolFunctionPackageInfo

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb.tnb_classes.ListSolFunctionPackageMetadata]

### vnfProductName
- **Type**: typing.Optional[str]

### vnfProvider
- **Type**: typing.Optional[str]

### vnfdId
- **Type**: typing.Optional[str]

### vnfdVersion
- **Type**: typing.Optional[str]


# ListSolFunctionPackageMetadata

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ListSolFunctionPackagesInput

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSolFunctionPackagesInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb.tnb_classes.PaginatorConfig]


# ListSolFunctionPackagesOutput

### functionPackages
- **Type**: typing.List[aws_resource_validator.pydantic_models.tnb.tnb_classes.ListSolFunctionPackageInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSolNetworkInstanceInfo

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ListSolNetworkInstanceMetadata'>
- **Required**: Yes

### nsInstanceDescription
- **Type**: <class 'str'>
- **Required**: Yes

### nsInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### nsState
- **Type**: typing.Literal['DELETED', 'IMPAIRED', 'INSTANTIATED', 'INSTANTIATE_IN_PROGRESS', 'INTENT_TO_UPDATE_IN_PROGRESS', 'NOT_INSTANTIATED', 'STOPPED', 'TERMINATE_IN_PROGRESS', 'UPDATED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### nsdId
- **Type**: <class 'str'>
- **Required**: Yes

### nsdInfoId
- **Type**: <class 'str'>
- **Required**: Yes


# ListSolNetworkInstanceMetadata

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ListSolNetworkInstancesInput

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSolNetworkInstancesInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb.tnb_classes.PaginatorConfig]


# ListSolNetworkInstancesOutput

### networkInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.tnb.tnb_classes.ListSolNetworkInstanceInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSolNetworkOperationsInfo

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb.tnb_classes.ProblemDetails]

### metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb.tnb_classes.ListSolNetworkOperationsMetadata]

### updateType
- **Type**: typing.Optional[typing.Literal['MODIFY_VNF_INFORMATION', 'UPDATE_NS']]


# ListSolNetworkOperationsInput

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### nsInstanceId
- **Type**: typing.Optional[str]


# ListSolNetworkOperationsInputPaginate

### nsInstanceId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb.tnb_classes.PaginatorConfig]


# ListSolNetworkOperationsMetadata

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### nsdInfoId
- **Type**: typing.Optional[str]

### vnfInstanceId
- **Type**: typing.Optional[str]


# ListSolNetworkOperationsOutput

### networkOperations
- **Type**: typing.List[aws_resource_validator.pydantic_models.tnb.tnb_classes.ListSolNetworkOperationsInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSolNetworkPackageInfo

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ListSolNetworkPackageMetadata'>
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


# ListSolNetworkPackageMetadata

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ListSolNetworkPackagesInput

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSolNetworkPackagesInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb.tnb_classes.PaginatorConfig]


# ListSolNetworkPackagesOutput

### networkPackages
- **Type**: typing.List[aws_resource_validator.pydantic_models.tnb.tnb_classes.ListSolNetworkPackageInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutput

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyVnfInfoMetadata

### vnfConfigurableProperties
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### vnfInstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# NetworkArtifactMeta

### overrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.tnb.tnb_classes.ToscaOverride]]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProblemDetails

### detail
- **Type**: <class 'str'>
- **Required**: Yes

### title
- **Type**: typing.Optional[str]


# PutSolFunctionPackageContentInput

### file
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### vnfPkgId
- **Type**: <class 'str'>
- **Required**: Yes

### contentType
- **Type**: typing.Optional[typing.Literal['application/zip']]


# PutSolFunctionPackageContentMetadata

### vnfd
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb.tnb_classes.FunctionArtifactMeta]


# PutSolFunctionPackageContentOutput

### id
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.PutSolFunctionPackageContentMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ResponseMetadata'>
- **Required**: Yes


# PutSolNetworkPackageContentInput

### file
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### nsdInfoId
- **Type**: <class 'str'>
- **Required**: Yes

### contentType
- **Type**: typing.Optional[typing.Literal['application/zip']]


# PutSolNetworkPackageContentMetadata

### nsd
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb.tnb_classes.NetworkArtifactMeta]


# PutSolNetworkPackageContentOutput

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.PutSolNetworkPackageContentMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ResponseMetadata'>
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


# TagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TerminateSolNetworkInstanceInput

### nsInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# TerminateSolNetworkInstanceOutput

### nsLcmOpOccId
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ResponseMetadata'>
- **Required**: Yes


# ToscaOverride

### defaultValue
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# UntagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateNsMetadata

### nsdInfoId
- **Type**: <class 'str'>
- **Required**: Yes

### additionalParamsForNs
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# UpdateSolFunctionPackageInput

### operationalState
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### vnfPkgId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateSolFunctionPackageOutput

### operationalState
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSolNetworkInstanceInput

### nsInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### updateType
- **Type**: typing.Literal['MODIFY_VNF_INFORMATION', 'UPDATE_NS']
- **Required**: Yes

### modifyVnfInfoData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb.tnb_classes.UpdateSolNetworkModify]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### updateNs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb.tnb_classes.UpdateSolNetworkServiceData]


# UpdateSolNetworkInstanceOutput

### nsLcmOpOccId
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSolNetworkModify

### vnfConfigurableProperties
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### vnfInstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateSolNetworkPackageInput

### nsdInfoId
- **Type**: <class 'str'>
- **Required**: Yes

### nsdOperationalState
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# UpdateSolNetworkPackageOutput

### nsdOperationalState
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSolNetworkServiceData

### nsdInfoId
- **Type**: <class 'str'>
- **Required**: Yes

### additionalParamsForNs
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# ValidateSolFunctionPackageContentInput

### file
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### vnfPkgId
- **Type**: <class 'str'>
- **Required**: Yes

### contentType
- **Type**: typing.Optional[typing.Literal['application/zip']]


# ValidateSolFunctionPackageContentMetadata

### vnfd
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb.tnb_classes.FunctionArtifactMeta]


# ValidateSolFunctionPackageContentOutput

### id
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ValidateSolFunctionPackageContentMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ResponseMetadata'>
- **Required**: Yes


# ValidateSolNetworkPackageContentInput

### file
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### nsdInfoId
- **Type**: <class 'str'>
- **Required**: Yes

### contentType
- **Type**: typing.Optional[typing.Literal['application/zip']]


# ValidateSolNetworkPackageContentMetadata

### nsd
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb.tnb_classes.NetworkArtifactMeta]


# ValidateSolNetworkPackageContentOutput

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ValidateSolNetworkPackageContentMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb.tnb_classes.ResponseMetadata'>
- **Required**: Yes


