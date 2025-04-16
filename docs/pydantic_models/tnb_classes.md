# Tnb Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Blob

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelSolNetworkOperationInput

### nsLcmOpOccId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateSolFunctionPackageInput

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


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
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateSolNetworkPackageInput

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadata'>
- **Required**: Yes


# ErrorInfo

### cause
- **Type**: typing.Optional[str]

### details
- **Type**: typing.Optional[str]


# FunctionArtifactMeta

### overrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.tnb_classes.ToscaOverride]]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.FunctionArtifactMeta]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.InstantiateMetadata]

### modifyVnfInfoMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.ModifyVnfInfoMetadata]

### updateNsMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.UpdateNsMetadata]


# GetSolNetworkOperationTaskDetails

### taskContext
- **Type**: typing.Optional[typing.Dict[str, str]]

### taskEndTime
- **Type**: typing.Optional[datetime.datetime]

### taskErrorDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.ErrorInfo]

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
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.NetworkArtifactMeta]


# GetSolVnfInfo

### vnfState
- **Type**: typing.Optional[typing.Literal['STARTED', 'STOPPED']]

### vnfcResourceInfo
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.tnb_classes.GetSolVnfcResourceInfo]]


# GetSolVnfcResourceInfo

### metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.GetSolVnfcResourceInfoMetadata]


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
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### dryRun
- **Type**: typing.Optional[bool]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# InstantiateSolNetworkInstanceOutput

### nsLcmOpOccId
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadata'>
- **Required**: Yes


# LcmOperationInfo

### nsLcmOpOccId
- **Type**: <class 'str'>
- **Required**: Yes


# ListSolFunctionInstanceInfo

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.PaginatorConfig]


# ListSolFunctionInstancesOutput

### functionInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.tnb_classes.ListSolFunctionInstanceInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSolFunctionPackageInfo

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.PaginatorConfig]


# ListSolFunctionPackagesOutput

### functionPackages
- **Type**: typing.List[aws_resource_validator.pydantic_models.tnb_classes.ListSolFunctionPackageInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSolNetworkInstanceInfo

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.PaginatorConfig]


# ListSolNetworkInstancesOutput

### networkInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.tnb_classes.ListSolNetworkInstanceInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSolNetworkOperationsInfo

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.PaginatorConfig]


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
- **Type**: typing.List[aws_resource_validator.pydantic_models.tnb_classes.ListSolNetworkOperationsInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSolNetworkPackageInfo

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.PaginatorConfig]


# ListSolNetworkPackagesOutput

### networkPackages
- **Type**: typing.List[aws_resource_validator.pydantic_models.tnb_classes.ListSolNetworkPackageInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.tnb_classes.ToscaOverride]]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.Blob'>
- **Required**: Yes

### vnfPkgId
- **Type**: <class 'str'>
- **Required**: Yes

### contentType
- **Type**: typing.Optional[typing.Literal['application/zip']]


# PutSolFunctionPackageContentMetadata

### vnfd
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.FunctionArtifactMeta]


# PutSolNetworkPackageContentInput

### file
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.Blob'>
- **Required**: Yes

### nsdInfoId
- **Type**: <class 'str'>
- **Required**: Yes

### contentType
- **Type**: typing.Optional[typing.Literal['application/zip']]


# PutSolNetworkPackageContentMetadata

### nsd
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.NetworkArtifactMeta]


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
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TerminateSolNetworkInstanceInput

### nsInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# TerminateSolNetworkInstanceOutput

### nsLcmOpOccId
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadata'>
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
- **Type**: typing.Sequence[str]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSolNetworkInstanceInput

### nsInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### updateType
- **Type**: typing.Literal['MODIFY_VNF_INFORMATION', 'UPDATE_NS']
- **Required**: Yes

### modifyVnfInfoData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.UpdateSolNetworkModify]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### updateNs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.UpdateSolNetworkServiceData]


# UpdateSolNetworkInstanceOutput

### nsLcmOpOccId
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSolNetworkModify

### vnfConfigurableProperties
- **Type**: typing.Mapping[str, typing.Any]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSolNetworkServiceData

### nsdInfoId
- **Type**: <class 'str'>
- **Required**: Yes

### additionalParamsForNs
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# ValidateSolFunctionPackageContentInput

### file
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.Blob'>
- **Required**: Yes

### vnfPkgId
- **Type**: <class 'str'>
- **Required**: Yes

### contentType
- **Type**: typing.Optional[typing.Literal['application/zip']]


# ValidateSolFunctionPackageContentMetadata

### vnfd
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.FunctionArtifactMeta]


# ValidateSolNetworkPackageContentInput

### file
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.Blob'>
- **Required**: Yes

### nsdInfoId
- **Type**: <class 'str'>
- **Required**: Yes

### contentType
- **Type**: typing.Optional[typing.Literal['application/zip']]


# ValidateSolNetworkPackageContentMetadata

### nsd
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.NetworkArtifactMeta]


