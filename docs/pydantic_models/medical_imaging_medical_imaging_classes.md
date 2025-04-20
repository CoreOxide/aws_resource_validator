# Medical Imaging Medical Imaging Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CopyDestinationImageSet

### imageSetId
- **Type**: <class 'str'>
- **Required**: Yes

### latestVersionId
- **Type**: <class 'str'>
- **Required**: Yes


# CopyDestinationImageSetProperties

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


# CopyImageSetInformation

### sourceImageSet
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.CopySourceImageSetInformation'>
- **Required**: Yes

### destinationImageSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.CopyDestinationImageSet]


# CopyImageSetRequest

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### sourceImageSetId
- **Type**: <class 'str'>
- **Required**: Yes

### copyImageSetInformation
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.CopyImageSetInformation'>
- **Required**: Yes

### force
- **Type**: typing.Optional[bool]


# CopyImageSetResponse

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### sourceImageSetProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.CopySourceImageSetProperties'>
- **Required**: Yes

### destinationImageSetProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.CopyDestinationImageSetProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.ResponseMetadata'>
- **Required**: Yes


# CopySourceImageSetInformation

### latestVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### DICOMCopies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.MetadataCopies]


# CopySourceImageSetProperties

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


# CreateDatastoreRequest

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### datastoreName
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### kmsKeyArn
- **Type**: typing.Optional[str]


# CreateDatastoreResponse

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### datastoreStatus
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.ResponseMetadata'>
- **Required**: Yes


# DICOMImportJobProperties

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


# DICOMImportJobSummary

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


# DICOMStudyDateAndTime

### DICOMStudyDate
- **Type**: <class 'str'>
- **Required**: Yes

### DICOMStudyTime
- **Type**: typing.Optional[str]


# DICOMTags

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


# DICOMUpdates

### removableAttributes
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]

### updatableAttributes
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]


# DatastoreProperties

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


# DatastoreSummary

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


# DeleteDatastoreRequest

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDatastoreResponse

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### datastoreStatus
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteImageSetRequest

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### imageSetId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteImageSetResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.ResponseMetadata'>
- **Required**: Yes


# GetDICOMImportJobRequest

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDICOMImportJobResponse

### jobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.DICOMImportJobProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.ResponseMetadata'>
- **Required**: Yes


# GetDatastoreRequest

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDatastoreResponse

### datastoreProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.DatastoreProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.ResponseMetadata'>
- **Required**: Yes


# GetImageFrameRequest

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### imageSetId
- **Type**: <class 'str'>
- **Required**: Yes

### imageFrameInformation
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.ImageFrameInformation'>
- **Required**: Yes


# GetImageFrameResponse

### imageFrameBlob
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.ResponseMetadata'>
- **Required**: Yes


# GetImageSetMetadataRequest

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### imageSetId
- **Type**: <class 'str'>
- **Required**: Yes

### versionId
- **Type**: typing.Optional[str]


# GetImageSetMetadataResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.ResponseMetadata'>
- **Required**: Yes


# GetImageSetRequest

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### imageSetId
- **Type**: <class 'str'>
- **Required**: Yes

### versionId
- **Type**: typing.Optional[str]


# GetImageSetResponse

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

### overrides
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.Overrides'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.ResponseMetadata'>
- **Required**: Yes


# ImageFrameInformation

### imageFrameId
- **Type**: <class 'str'>
- **Required**: Yes


# ImageSetProperties

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

### overrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.Overrides]


# ImageSetsMetadataSummary

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
- **Type**: <class 'NoneType'>


# ListDICOMImportJobsRequest

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### jobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDICOMImportJobsRequestPaginate

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### jobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.PaginatorConfig]


# ListDICOMImportJobsResponse

### jobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.DICOMImportJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDatastoresRequest

### datastoreStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDatastoresRequestPaginate

### datastoreStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.PaginatorConfig]


# ListDatastoresResponse

### datastoreSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.DatastoreSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListImageSetVersionsRequest

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


# ListImageSetVersionsRequestPaginate

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### imageSetId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.PaginatorConfig]


# ListImageSetVersionsResponse

### imageSetPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.ImageSetProperties]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.ResponseMetadata'>
- **Required**: Yes


# MetadataCopies

### copiableAttributes
- **Type**: <class 'str'>
- **Required**: Yes


# MetadataUpdates

### DICOMUpdates
- **Type**: <class 'NoneType'>

### revertToVersionId
- **Type**: typing.Optional[str]


# Overrides

### forced
- **Type**: typing.Optional[bool]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


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


# SearchByAttributeValue

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
- **Type**: <class 'NoneType'>


# SearchCriteria

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.SearchFilter]]

### sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.Sort]


# SearchFilter

### values
- **Type**: typing.List[aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.SearchByAttributeValue]
- **Required**: Yes

### operator
- **Type**: typing.Literal['BETWEEN', 'EQUAL']
- **Required**: Yes


# SearchImageSetsRequest

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### searchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.SearchCriteria]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# SearchImageSetsRequestPaginate

### datastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### searchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.SearchCriteria]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.PaginatorConfig]


# SearchImageSetsResponse

### imageSetsMetadataSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.ImageSetsMetadataSummary]
- **Required**: Yes

### sort
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.Sort'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# Sort

### sortOrder
- **Type**: typing.Literal['ASC', 'DESC']
- **Required**: Yes

### sortField
- **Type**: typing.Literal['DICOMStudyDateAndTime', 'createdAt', 'updatedAt']
- **Required**: Yes


# StartDICOMImportJobRequest

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


# StartDICOMImportJobResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.ResponseMetadata'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateImageSetMetadataRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.MetadataUpdates'>
- **Required**: Yes

### force
- **Type**: typing.Optional[bool]


# UpdateImageSetMetadataResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.medical_imaging.medical_imaging_classes.ResponseMetadata'>
- **Required**: Yes


