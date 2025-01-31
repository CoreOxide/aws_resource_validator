# Mobile Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BundleDetailsTypeDef

### bundleId
- **Type**: typing.Optional[str]

### title
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### iconUrl
- **Type**: typing.Optional[str]

### availablePlatforms
- **Type**: typing.Optional[typing.List[typing.Literal['ANDROID', 'JAVASCRIPT', 'LINUX', 'OBJC', 'OSX', 'SWIFT', 'WINDOWS']]]


# CreateProjectRequestRequestTypeDef

### name
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[str]

### contents
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]

### snapshotId
- **Type**: typing.Optional[str]


# CreateProjectResultTypeDef

### details
- **Type**: <class 'aws_resource_validator.pydantic_models.mobile_classes.ProjectDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mobile_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteProjectRequestRequestTypeDef

### projectId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProjectResultTypeDef

### deletedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.mobile_classes.ResourceTypeDef]
- **Required**: Yes

### orphanedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.mobile_classes.ResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mobile_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeBundleRequestRequestTypeDef

### bundleId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBundleResultTypeDef

### details
- **Type**: <class 'aws_resource_validator.pydantic_models.mobile_classes.BundleDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mobile_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeProjectRequestRequestTypeDef

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### syncFromResources
- **Type**: typing.Optional[bool]


# DescribeProjectResultTypeDef

### details
- **Type**: <class 'aws_resource_validator.pydantic_models.mobile_classes.ProjectDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mobile_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExportBundleRequestRequestTypeDef

### bundleId
- **Type**: <class 'str'>
- **Required**: Yes

### projectId
- **Type**: typing.Optional[str]

### platform
- **Type**: typing.Optional[typing.Literal['ANDROID', 'JAVASCRIPT', 'LINUX', 'OBJC', 'OSX', 'SWIFT', 'WINDOWS']]


# ExportBundleResultTypeDef

### downloadUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mobile_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExportProjectRequestRequestTypeDef

### projectId
- **Type**: <class 'str'>
- **Required**: Yes


# ExportProjectResultTypeDef

### downloadUrl
- **Type**: <class 'str'>
- **Required**: Yes

### shareUrl
- **Type**: <class 'str'>
- **Required**: Yes

### snapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mobile_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBundlesRequestListBundlesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mobile_classes.PaginatorConfigTypeDef]


# ListBundlesRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListBundlesResultTypeDef

### bundleList
- **Type**: typing.List[aws_resource_validator.pydantic_models.mobile_classes.BundleDetailsTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mobile_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProjectsRequestListProjectsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mobile_classes.PaginatorConfigTypeDef]


# ListProjectsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListProjectsResultTypeDef

### projects
- **Type**: typing.List[aws_resource_validator.pydantic_models.mobile_classes.ProjectSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mobile_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProjectDetailsTypeDef

### name
- **Type**: typing.Optional[str]

### projectId
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['IMPORTING', 'NORMAL', 'SYNCING']]

### createdDate
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDate
- **Type**: typing.Optional[datetime.datetime]

### consoleUrl
- **Type**: typing.Optional[str]

### resources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mobile_classes.ResourceTypeDef]]


# ProjectSummaryTypeDef

### name
- **Type**: typing.Optional[str]

### projectId
- **Type**: typing.Optional[str]


# ResourceTypeDef

### type
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### feature
- **Type**: typing.Optional[str]

### attributes
- **Type**: typing.Optional[typing.Dict[str, str]]


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


# UpdateProjectRequestRequestTypeDef

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### contents
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]


# UpdateProjectResultTypeDef

### details
- **Type**: <class 'aws_resource_validator.pydantic_models.mobile_classes.ProjectDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mobile_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


