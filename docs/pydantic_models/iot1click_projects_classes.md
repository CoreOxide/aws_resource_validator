# Pydantic Models in iot1click_projects_classes

# AssociateDeviceWithPlacementRequestRequestTypeDef

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### placementName
- **Type**: <class 'str'>
- **Required**: Yes

### deviceId
- **Type**: <class 'str'>
- **Required**: Yes

### deviceTemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreatePlacementRequestRequestTypeDef

### placementName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateProjectRequestRequestTypeDef

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### placementTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot1click_projects_classes.PlacementTemplateTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# DeletePlacementRequestRequestTypeDef

### placementName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProjectRequestRequestTypeDef

### projectName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePlacementRequestRequestTypeDef

### placementName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePlacementResponseTypeDef

### placement
- **Type**: <class 'aws_resource_validator.pydantic_models.iot1click_projects_classes.PlacementDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot1click_projects_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeProjectRequestRequestTypeDef

### projectName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeProjectResponseTypeDef

### project
- **Type**: <class 'aws_resource_validator.pydantic_models.iot1click_projects_classes.ProjectDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot1click_projects_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeviceTemplateTypeDef

### deviceType
- **Type**: typing.Optional[str]

### callbackOverrides
- **Type**: typing.Optional[typing.Mapping[str, str]]


# DisassociateDeviceFromPlacementRequestRequestTypeDef

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### placementName
- **Type**: <class 'str'>
- **Required**: Yes

### deviceTemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDevicesInPlacementRequestRequestTypeDef

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### placementName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDevicesInPlacementResponseTypeDef

### devices
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot1click_projects_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPlacementsRequestListPlacementsPaginateTypeDef

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot1click_projects_classes.PaginatorConfigTypeDef]


# ListPlacementsRequestRequestTypeDef

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPlacementsResponseTypeDef

### placements
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot1click_projects_classes.PlacementSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot1click_projects_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProjectsRequestListProjectsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot1click_projects_classes.PaginatorConfigTypeDef]


# ListProjectsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListProjectsResponseTypeDef

### projects
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot1click_projects_classes.ProjectSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot1click_projects_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot1click_projects_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PlacementDescriptionTypeDef

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### placementName
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# PlacementSummaryTypeDef

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### placementName
- **Type**: <class 'str'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# PlacementTemplateTypeDef

### defaultAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### deviceTemplates
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iot1click_projects_classes.DeviceTemplateTypeDef]]


# ProjectDescriptionTypeDef

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### arn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### placementTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot1click_projects_classes.PlacementTemplateTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ProjectSummaryTypeDef

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### arn
- **Type**: typing.Optional[str]

### tags
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


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdatePlacementRequestRequestTypeDef

### placementName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]


# UpdateProjectRequestRequestTypeDef

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### placementTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot1click_projects_classes.PlacementTemplateTypeDef]


