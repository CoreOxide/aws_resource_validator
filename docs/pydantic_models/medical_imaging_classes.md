# Medical Imaging Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CopyDestinationImageSetPropertiesTypeDef

### imageSetId
- **Type**: <class 'str'>
- **Required**: Yes

### latestVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### imageSetState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED', 'LOCKED']]

### imageSetWorkflowStatus
- **Type**: typing.Optional[typing.Literal['COPIED', 'COPYING', 'COPYING_WITH_READ_ONLY_ACCESS', 'COPY_FAILED', 'CREATED', 'DELETED', 'DELETING', 'UPDATED', 'UPDATE_FAILED', 'UPDATING']]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### imageSetArn
- **Type**: typing.Optional[str]


# CopyDestinationImageSetTypeDef

### imageSetId
- **Type**: <class 'str'>
- **Required**: Yes

### latestVersionId
- **Type**: <class 'str'>
- **Required**: Yes


# CopyImageSetInformationTypeDef

### sourceImageSet
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging_classes.CopySourceImageSetInformationTypeDef'>
- **Required**: Yes

### destinationImageSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medical_imaging_classes.CopyDestinationImageSetTypeDef]


# CopyImageSetRequestRequestTypeDef

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### sourceImageSetId
- **Type**: <class 'str'>
- **Required**: Yes

### copyImageSetInformation
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging_classes.CopyImageSetInformationTypeDef'>
- **Required**: Yes


# CopyImageSetResponseTypeDef

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### sourceImageSetProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging_classes.CopySourceImageSetPropertiesTypeDef'>
- **Required**: Yes

### destinationImageSetProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging_classes.CopyDestinationImageSetPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CopySourceImageSetInformationTypeDef

### latestVersionId
- **Type**: <class 'str'>
- **Required**: Yes


# CopySourceImageSetPropertiesTypeDef

### imageSetId
- **Type**: <class 'str'>
- **Required**: Yes

### latestVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### imageSetState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED', 'LOCKED']]

### imageSetWorkflowStatus
- **Type**: typing.Optional[typing.Literal['COPIED', 'COPYING', 'COPYING_WITH_READ_ONLY_ACCESS', 'COPY_FAILED', 'CREATED', 'DELETED', 'DELETING', 'UPDATED', 'UPDATE_FAILED', 'UPDATING']]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### imageSetArn
- **Type**: typing.Optional[str]


# CreateDatastoreRequestRequestTypeDef

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### datastoreName
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### kmsKeyArn
- **Type**: typing.Optional[str]


# CreateDatastoreResponseTypeDef

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### datastoreStatus
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DICOMImportJobPropertiesTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### jobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']
- **Required**: Yes

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### dataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### inputS3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### outputS3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### endedAt
- **Type**: typing.Optional[datetime.datetime]

### submittedAt
- **Type**: typing.Optional[datetime.datetime]

### message
- **Type**: typing.Optional[str]


# DICOMImportJobSummaryTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### jobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']
- **Required**: Yes

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### dataAccessRoleArn
- **Type**: typing.Optional[str]

### endedAt
- **Type**: typing.Optional[datetime.datetime]

### submittedAt
- **Type**: typing.Optional[datetime.datetime]

### message
- **Type**: typing.Optional[str]


# DICOMStudyDateAndTimeTypeDef

### DICOMStudyDate
- **Type**: <class 'str'>
- **Required**: Yes

### DICOMStudyTime
- **Type**: typing.Optional[str]


# DICOMTagsTypeDef

### DICOMPatientId
- **Type**: typing.Optional[str]

### DICOMPatientName
- **Type**: typing.Optional[str]

### DICOMPatientBirthDate
- **Type**: typing.Optional[str]

### DICOMPatientSex
- **Type**: typing.Optional[str]

### DICOMStudyInstanceUID
- **Type**: typing.Optional[str]

### DICOMStudyId
- **Type**: typing.Optional[str]

### DICOMStudyDescription
- **Type**: typing.Optional[str]

### DICOMNumberOfStudyRelatedSeries
- **Type**: typing.Optional[int]

### DICOMNumberOfStudyRelatedInstances
- **Type**: typing.Optional[int]

### DICOMAccessionNumber
- **Type**: typing.Optional[str]

### DICOMSeriesInstanceUID
- **Type**: typing.Optional[str]

### DICOMSeriesModality
- **Type**: typing.Optional[str]

### DICOMSeriesBodyPart
- **Type**: typing.Optional[str]

### DICOMSeriesNumber
- **Type**: typing.Optional[int]

### DICOMStudyDate
- **Type**: typing.Optional[str]

### DICOMStudyTime
- **Type**: typing.Optional[str]


# DICOMUpdatesTypeDef

### removableAttributes
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]

### updatableAttributes
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]


# DatastorePropertiesTypeDef

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### datastoreName
- **Type**: <class 'str'>
- **Required**: Yes

### datastoreStatus
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING']
- **Required**: Yes

### kmsKeyArn
- **Type**: typing.Optional[str]

### datastoreArn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# DatastoreSummaryTypeDef

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### datastoreName
- **Type**: <class 'str'>
- **Required**: Yes

### datastoreStatus
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING']
- **Required**: Yes

### datastoreArn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# DeleteDatastoreRequestRequestTypeDef

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDatastoreResponseTypeDef

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### datastoreStatus
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteImageSetRequestRequestTypeDef

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### imageSetId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteImageSetResponseTypeDef

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### imageSetId
- **Type**: <class 'str'>
- **Required**: Yes

### imageSetState
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'LOCKED']
- **Required**: Yes

### imageSetWorkflowStatus
- **Type**: typing.Literal['COPIED', 'COPYING', 'COPYING_WITH_READ_ONLY_ACCESS', 'COPY_FAILED', 'CREATED', 'DELETED', 'DELETING', 'UPDATED', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDICOMImportJobRequestRequestTypeDef

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDICOMImportJobResponseTypeDef

### jobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging_classes.DICOMImportJobPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDatastoreRequestRequestTypeDef

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDatastoreResponseTypeDef

### datastoreProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging_classes.DatastorePropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetImageFrameRequestRequestTypeDef

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### imageSetId
- **Type**: <class 'str'>
- **Required**: Yes

### imageFrameInformation
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging_classes.ImageFrameInformationTypeDef'>
- **Required**: Yes


# GetImageFrameResponseTypeDef

### imageFrameBlob
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetImageSetMetadataRequestRequestTypeDef

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### imageSetId
- **Type**: <class 'str'>
- **Required**: Yes

### versionId
- **Type**: typing.Optional[str]


# GetImageSetMetadataResponseTypeDef

### imageSetMetadataBlob
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### contentEncoding
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetImageSetRequestRequestTypeDef

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### imageSetId
- **Type**: <class 'str'>
- **Required**: Yes

### versionId
- **Type**: typing.Optional[str]


# GetImageSetResponseTypeDef

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### imageSetId
- **Type**: <class 'str'>
- **Required**: Yes

### versionId
- **Type**: <class 'str'>
- **Required**: Yes

### imageSetState
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'LOCKED']
- **Required**: Yes

### imageSetWorkflowStatus
- **Type**: typing.Literal['COPIED', 'COPYING', 'COPYING_WITH_READ_ONLY_ACCESS', 'COPY_FAILED', 'CREATED', 'DELETED', 'DELETING', 'UPDATED', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### deletedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### imageSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImageFrameInformationTypeDef

### imageFrameId
- **Type**: <class 'str'>
- **Required**: Yes


# ImageSetPropertiesTypeDef

### imageSetId
- **Type**: <class 'str'>
- **Required**: Yes

### versionId
- **Type**: <class 'str'>
- **Required**: Yes

### imageSetState
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'LOCKED']
- **Required**: Yes

### ImageSetWorkflowStatus
- **Type**: typing.Optional[typing.Literal['COPIED', 'COPYING', 'COPYING_WITH_READ_ONLY_ACCESS', 'COPY_FAILED', 'CREATED', 'DELETED', 'DELETING', 'UPDATED', 'UPDATE_FAILED', 'UPDATING']]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### deletedAt
- **Type**: typing.Optional[datetime.datetime]

### message
- **Type**: typing.Optional[str]


# ImageSetsMetadataSummaryTypeDef

### imageSetId
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: typing.Optional[int]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### DICOMTags
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medical_imaging_classes.DICOMTagsTypeDef]


# ListDICOMImportJobsRequestListDICOMImportJobsPaginateTypeDef

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### jobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medical_imaging_classes.PaginatorConfigTypeDef]


# ListDICOMImportJobsRequestRequestTypeDef

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### jobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDICOMImportJobsResponseTypeDef

### jobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.medical_imaging_classes.DICOMImportJobSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDatastoresRequestListDatastoresPaginateTypeDef

### datastoreStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medical_imaging_classes.PaginatorConfigTypeDef]


# ListDatastoresRequestRequestTypeDef

### datastoreStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDatastoresResponseTypeDef

### datastoreSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.medical_imaging_classes.DatastoreSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListImageSetVersionsRequestListImageSetVersionsPaginateTypeDef

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### imageSetId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medical_imaging_classes.PaginatorConfigTypeDef]


# ListImageSetVersionsRequestRequestTypeDef

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### imageSetId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListImageSetVersionsResponseTypeDef

### imageSetPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.medical_imaging_classes.ImageSetPropertiesTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MetadataUpdatesTypeDef

### DICOMUpdates
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medical_imaging_classes.DICOMUpdatesTypeDef]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


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


# SearchByAttributeValueTypeDef

### DICOMPatientId
- **Type**: typing.Optional[str]

### DICOMAccessionNumber
- **Type**: typing.Optional[str]

### DICOMStudyId
- **Type**: typing.Optional[str]

### DICOMStudyInstanceUID
- **Type**: typing.Optional[str]

### DICOMSeriesInstanceUID
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### updatedAt
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### DICOMStudyDateAndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medical_imaging_classes.DICOMStudyDateAndTimeTypeDef]


# SearchCriteriaTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medical_imaging_classes.SearchFilterTypeDef]]

### sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medical_imaging_classes.SortTypeDef]


# SearchFilterTypeDef

### values
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.medical_imaging_classes.SearchByAttributeValueTypeDef]
- **Required**: Yes

### operator
- **Type**: typing.Literal['BETWEEN', 'EQUAL']
- **Required**: Yes


# SearchImageSetsRequestRequestTypeDef

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### searchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medical_imaging_classes.SearchCriteriaTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# SearchImageSetsRequestSearchImageSetsPaginateTypeDef

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### searchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medical_imaging_classes.SearchCriteriaTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medical_imaging_classes.PaginatorConfigTypeDef]


# SearchImageSetsResponseTypeDef

### imageSetsMetadataSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.medical_imaging_classes.ImageSetsMetadataSummaryTypeDef]
- **Required**: Yes

### sort
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging_classes.SortTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SortTypeDef

### sortOrder
- **Type**: typing.Literal['ASC', 'DESC']
- **Required**: Yes

### sortField
- **Type**: typing.Literal['DICOMStudyDateAndTime', 'createdAt', 'updatedAt']
- **Required**: Yes


# StartDICOMImportJobRequestRequestTypeDef

### dataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### inputS3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### outputS3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### jobName
- **Type**: typing.Optional[str]

### inputOwnerAccountId
- **Type**: typing.Optional[str]


# StartDICOMImportJobResponseTypeDef

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### jobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']
- **Required**: Yes

### submittedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging_classes.ResponseMetadataTypeDef'>
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


# UpdateImageSetMetadataRequestRequestTypeDef

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### imageSetId
- **Type**: <class 'str'>
- **Required**: Yes

### latestVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### updateImageSetMetadataUpdates
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging_classes.MetadataUpdatesTypeDef'>
- **Required**: Yes


# UpdateImageSetMetadataResponseTypeDef

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### imageSetId
- **Type**: <class 'str'>
- **Required**: Yes

### latestVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### imageSetState
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'LOCKED']
- **Required**: Yes

### imageSetWorkflowStatus
- **Type**: typing.Literal['COPIED', 'COPYING', 'COPYING_WITH_READ_ONLY_ACCESS', 'COPY_FAILED', 'CREATED', 'DELETED', 'DELETING', 'UPDATED', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


