# Tnb Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelSolNetworkOperationInputTypeDef

### nsLcmOpOccId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateSolFunctionPackageInputTypeDef

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateSolNetworkInstanceInputTypeDef

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


# CreateSolNetworkPackageInputTypeDef

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# DeleteSolFunctionPackageInputTypeDef

### vnfPkgId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSolNetworkInstanceInputTypeDef

### nsInstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSolNetworkPackageInputTypeDef

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


# GetSolFunctionInstanceInputTypeDef

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


# GetSolFunctionPackageContentInputTypeDef

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


# GetSolFunctionPackageDescriptorInputTypeDef

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


# GetSolFunctionPackageInputTypeDef

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


# GetSolInstantiatedVnfInfoTypeDef

### vnfState
- **Type**: typing.Optional[typing.Literal['STARTED', 'STOPPED']]


# GetSolNetworkInstanceInputTypeDef

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


# GetSolNetworkOperationInputTypeDef

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

### instantiateMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.InstantiateMetadataTypeDef]

### modifyVnfInfoMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.ModifyVnfInfoMetadataTypeDef]

### updateNsMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.UpdateNsMetadataTypeDef]


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


# GetSolNetworkPackageContentInputTypeDef

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


# GetSolNetworkPackageDescriptorInputTypeDef

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


# GetSolNetworkPackageInputTypeDef

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


# InstantiateMetadataTypeDef

### nsdInfoId
- **Type**: <class 'str'>
- **Required**: Yes

### additionalParamsForNs
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# InstantiateSolNetworkInstanceInputTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListSolFunctionInstanceMetadataTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ListSolFunctionInstancesInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.PaginatorConfigTypeDef]


# ListSolFunctionInstancesInputTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSolFunctionInstancesOutputTypeDef

### functionInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.tnb_classes.ListSolFunctionInstanceInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSolFunctionPackageInfoTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListSolFunctionPackageMetadataTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ListSolFunctionPackagesInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.PaginatorConfigTypeDef]


# ListSolFunctionPackagesInputTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSolFunctionPackagesOutputTypeDef

### functionPackages
- **Type**: typing.List[aws_resource_validator.pydantic_models.tnb_classes.ListSolFunctionPackageInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSolNetworkInstanceInfoTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListSolNetworkInstanceMetadataTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ListSolNetworkInstancesInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.PaginatorConfigTypeDef]


# ListSolNetworkInstancesInputTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSolNetworkInstancesOutputTypeDef

### networkInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.tnb_classes.ListSolNetworkInstanceInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSolNetworkOperationsInfoTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListSolNetworkOperationsInputPaginateTypeDef

### nsInstanceId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.PaginatorConfigTypeDef]


# ListSolNetworkOperationsInputTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### nsInstanceId
- **Type**: typing.Optional[str]


# ListSolNetworkOperationsMetadataTypeDef

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


# ListSolNetworkOperationsOutputTypeDef

### networkOperations
- **Type**: typing.List[aws_resource_validator.pydantic_models.tnb_classes.ListSolNetworkOperationsInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSolNetworkPackageInfoTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListSolNetworkPackageMetadataTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ListSolNetworkPackagesInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.PaginatorConfigTypeDef]


# ListSolNetworkPackagesInputTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSolNetworkPackagesOutputTypeDef

### networkPackages
- **Type**: typing.List[aws_resource_validator.pydantic_models.tnb_classes.ListSolNetworkPackageInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInputTypeDef

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


# ModifyVnfInfoMetadataTypeDef

### vnfConfigurableProperties
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### vnfInstanceId
- **Type**: <class 'str'>
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


# PutSolFunctionPackageContentInputTypeDef

### file
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.BlobTypeDef'>
- **Required**: Yes

### vnfPkgId
- **Type**: <class 'str'>
- **Required**: Yes

### contentType
- **Type**: typing.Optional[typing.Literal['application/zip']]


# PutSolFunctionPackageContentMetadataTypeDef

### vnfd
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.FunctionArtifactMetaTypeDef]


# PutSolNetworkPackageContentInputTypeDef

### file
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.BlobTypeDef'>
- **Required**: Yes

### nsdInfoId
- **Type**: <class 'str'>
- **Required**: Yes

### contentType
- **Type**: typing.Optional[typing.Literal['application/zip']]


# PutSolNetworkPackageContentMetadataTypeDef

### nsd
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.NetworkArtifactMetaTypeDef]


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


# TagResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TerminateSolNetworkInstanceInputTypeDef

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


# UntagResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateNsMetadataTypeDef

### nsdInfoId
- **Type**: <class 'str'>
- **Required**: Yes

### additionalParamsForNs
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# UpdateSolFunctionPackageInputTypeDef

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


# UpdateSolNetworkInstanceInputTypeDef

### nsInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### updateType
- **Type**: typing.Literal['MODIFY_VNF_INFORMATION', 'UPDATE_NS']
- **Required**: Yes

### modifyVnfInfoData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.UpdateSolNetworkModifyTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### updateNs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.UpdateSolNetworkServiceDataTypeDef]


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


# UpdateSolNetworkPackageInputTypeDef

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


# UpdateSolNetworkServiceDataTypeDef

### nsdInfoId
- **Type**: <class 'str'>
- **Required**: Yes

### additionalParamsForNs
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# ValidateSolFunctionPackageContentInputTypeDef

### file
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.BlobTypeDef'>
- **Required**: Yes

### vnfPkgId
- **Type**: <class 'str'>
- **Required**: Yes

### contentType
- **Type**: typing.Optional[typing.Literal['application/zip']]


# ValidateSolFunctionPackageContentMetadataTypeDef

### vnfd
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.FunctionArtifactMetaTypeDef]


# ValidateSolNetworkPackageContentInputTypeDef

### file
- **Type**: <class 'aws_resource_validator.pydantic_models.tnb_classes.BlobTypeDef'>
- **Required**: Yes

### nsdInfoId
- **Type**: <class 'str'>
- **Required**: Yes

### contentType
- **Type**: typing.Optional[typing.Literal['application/zip']]


# ValidateSolNetworkPackageContentMetadataTypeDef

### nsd
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.tnb_classes.NetworkArtifactMetaTypeDef]


