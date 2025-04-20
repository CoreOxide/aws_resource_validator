# Clouddirectory Clouddirectory Classes

# AddFacetToObjectRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaFacet
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.SchemaFacet'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### ObjectAttributeList
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.AttributeKeyAndValue, aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.AttributeKeyAndValueOutput]]]


# ApplySchemaRequest

### PublishedSchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes


# ApplySchemaResponse

### AppliedSchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes


# AttachObjectRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ParentReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### ChildReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### LinkName
- **Type**: <class 'str'>
- **Required**: Yes


# AttachObjectResponse

### AttachedObjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes


# AttachPolicyRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes


# AttachToIndexRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### IndexReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### TargetReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes


# AttachToIndexResponse

### AttachedObjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes


# AttachTypedLinkRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### TargetObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### TypedLinkFacet
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkSchemaAndFacetName'>
- **Required**: Yes

### Attributes
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.AttributeNameAndValue, aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.AttributeNameAndValueOutput]]
- **Required**: Yes


# AttachTypedLinkResponse

### TypedLinkSpecifier
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkSpecifierOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes


# AttributeKey

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### FacetName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# AttributeKeyAndValue

### Key
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.AttributeKey'>
- **Required**: Yes

### Value
- **Type**: typing.Union[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedAttributeValue, aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedAttributeValueOutput]
- **Required**: Yes


# AttributeKeyAndValueOutput

### Key
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.AttributeKey'>
- **Required**: Yes

### Value
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedAttributeValueOutput'>
- **Required**: Yes


# AttributeNameAndValue

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Union[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedAttributeValue, aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedAttributeValueOutput]
- **Required**: Yes


# AttributeNameAndValueOutput

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedAttributeValueOutput'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchAddFacetToObject

### SchemaFacet
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.SchemaFacet'>
- **Required**: Yes

### ObjectAttributeList
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.AttributeKeyAndValue, aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.AttributeKeyAndValueOutput]]
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes


# BatchAttachObject

### ParentReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### ChildReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### LinkName
- **Type**: <class 'str'>
- **Required**: Yes


# BatchAttachObjectResponse

### attachedObjectIdentifier
- **Type**: typing.Optional[str]


# BatchAttachPolicy

### PolicyReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes


# BatchAttachToIndex

### IndexReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### TargetReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes


# BatchAttachToIndexResponse

### AttachedObjectIdentifier
- **Type**: typing.Optional[str]


# BatchAttachTypedLink

### SourceObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### TargetObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### TypedLinkFacet
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkSchemaAndFacetName'>
- **Required**: Yes

### Attributes
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.AttributeNameAndValue, aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.AttributeNameAndValueOutput]]
- **Required**: Yes


# BatchAttachTypedLinkResponse

### TypedLinkSpecifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkSpecifierOutput]


# BatchCreateIndex

### OrderedIndexedAttributeList
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.AttributeKey]
- **Required**: Yes

### IsUnique
- **Type**: <class 'bool'>
- **Required**: Yes

### ParentReference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference]

### LinkName
- **Type**: typing.Optional[str]

### BatchReferenceName
- **Type**: typing.Optional[str]


# BatchCreateIndexResponse

### ObjectIdentifier
- **Type**: typing.Optional[str]


# BatchCreateObject

### SchemaFacet
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.SchemaFacet]
- **Required**: Yes

### ObjectAttributeList
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.AttributeKeyAndValue]
- **Required**: Yes

### ParentReference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference]

### LinkName
- **Type**: typing.Optional[str]

### BatchReferenceName
- **Type**: typing.Optional[str]


# BatchCreateObjectResponse

### ObjectIdentifier
- **Type**: typing.Optional[str]


# BatchDeleteObject

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes


# BatchDetachFromIndex

### IndexReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### TargetReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes


# BatchDetachFromIndexResponse

### DetachedObjectIdentifier
- **Type**: typing.Optional[str]


# BatchDetachObject

### ParentReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### LinkName
- **Type**: <class 'str'>
- **Required**: Yes

### BatchReferenceName
- **Type**: typing.Optional[str]


# BatchDetachObjectResponse

### detachedObjectIdentifier
- **Type**: typing.Optional[str]


# BatchDetachPolicy

### PolicyReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes


# BatchDetachTypedLink

### TypedLinkSpecifier
- **Type**: typing.Union[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkSpecifier, aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkSpecifierOutput]
- **Required**: Yes


# BatchGetLinkAttributes

### TypedLinkSpecifier
- **Type**: typing.Union[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkSpecifier, aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkSpecifierOutput]
- **Required**: Yes

### AttributeNames
- **Type**: typing.List[str]
- **Required**: Yes


# BatchGetLinkAttributesResponse

### Attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.AttributeKeyAndValueOutput]]


# BatchGetObjectAttributes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### SchemaFacet
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.SchemaFacet'>
- **Required**: Yes

### AttributeNames
- **Type**: typing.List[str]
- **Required**: Yes


# BatchGetObjectAttributesResponse

### Attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.AttributeKeyAndValueOutput]]


# BatchGetObjectInformation

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes


# BatchGetObjectInformationResponse

### SchemaFacets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.SchemaFacet]]

### ObjectIdentifier
- **Type**: typing.Optional[str]


# BatchListAttachedIndices

### TargetReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# BatchListAttachedIndicesResponse

### IndexAttachments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.IndexAttachment]]

### NextToken
- **Type**: typing.Optional[str]


# BatchListIncomingTypedLinks

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### FilterAttributeRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkAttributeRange]]

### FilterTypedLink
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkSchemaAndFacetName]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# BatchListIncomingTypedLinksResponse

### LinkSpecifiers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkSpecifierOutput]]

### NextToken
- **Type**: typing.Optional[str]


# BatchListIndex

### IndexReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### RangesOnIndexedValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectAttributeRange]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# BatchListIndexResponse

### IndexAttachments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.IndexAttachment]]

### NextToken
- **Type**: typing.Optional[str]


# BatchListObjectAttributes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### FacetFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.SchemaFacet]


# BatchListObjectAttributesResponse

### Attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.AttributeKeyAndValueOutput]]

### NextToken
- **Type**: typing.Optional[str]


# BatchListObjectChildren

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# BatchListObjectChildrenResponse

### Children
- **Type**: typing.Optional[typing.Dict[str, str]]

### NextToken
- **Type**: typing.Optional[str]


# BatchListObjectParentPaths

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# BatchListObjectParentPathsResponse

### PathToObjectIdentifiersList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.PathToObjectIdentifiers]]

### NextToken
- **Type**: typing.Optional[str]


# BatchListObjectParents

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# BatchListObjectParentsResponse

### ParentLinks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectIdentifierAndLinkNameTuple]]

### NextToken
- **Type**: typing.Optional[str]


# BatchListObjectPolicies

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# BatchListObjectPoliciesResponse

### AttachedPolicyIds
- **Type**: typing.Optional[typing.List[str]]

### NextToken
- **Type**: typing.Optional[str]


# BatchListOutgoingTypedLinks

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### FilterAttributeRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkAttributeRange]]

### FilterTypedLink
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkSchemaAndFacetName]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# BatchListOutgoingTypedLinksResponse

### TypedLinkSpecifiers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkSpecifierOutput]]

### NextToken
- **Type**: typing.Optional[str]


# BatchListPolicyAttachments

### PolicyReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# BatchListPolicyAttachmentsResponse

### ObjectIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### NextToken
- **Type**: typing.Optional[str]


# BatchLookupPolicy

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# BatchLookupPolicyResponse

### PolicyToPathList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.PolicyToPath]]

### NextToken
- **Type**: typing.Optional[str]


# BatchReadException

### Type
- **Type**: typing.Optional[typing.Literal['AccessDeniedException', 'CannotListParentOfRootException', 'DirectoryNotEnabledException', 'FacetValidationException', 'InternalServiceException', 'InvalidArnException', 'InvalidNextTokenException', 'LimitExceededException', 'NotIndexException', 'NotNodeException', 'NotPolicyException', 'ResourceNotFoundException', 'ValidationException']]

### Message
- **Type**: typing.Optional[str]


# BatchReadOperation

### ListObjectAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchListObjectAttributes]

### ListObjectChildren
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchListObjectChildren]

### ListAttachedIndices
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchListAttachedIndices]

### ListObjectParentPaths
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchListObjectParentPaths]

### GetObjectInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchGetObjectInformation]

### GetObjectAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchGetObjectAttributes]

### ListObjectParents
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchListObjectParents]

### ListObjectPolicies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchListObjectPolicies]

### ListPolicyAttachments
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchListPolicyAttachments]

### LookupPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchLookupPolicy]

### ListIndex
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchListIndex]

### ListOutgoingTypedLinks
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchListOutgoingTypedLinks]

### ListIncomingTypedLinks
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchListIncomingTypedLinks]

### GetLinkAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchGetLinkAttributes]


# BatchReadOperationResponse

### SuccessfulResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchReadSuccessfulResponse]

### ExceptionResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchReadException]


# BatchReadRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### Operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchReadOperation]
- **Required**: Yes

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]


# BatchReadResponse

### Responses
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchReadOperationResponse]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes


# BatchReadSuccessfulResponse

### ListObjectAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchListObjectAttributesResponse]

### ListObjectChildren
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchListObjectChildrenResponse]

### GetObjectInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchGetObjectInformationResponse]

### GetObjectAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchGetObjectAttributesResponse]

### ListAttachedIndices
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchListAttachedIndicesResponse]

### ListObjectParentPaths
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchListObjectParentPathsResponse]

### ListObjectPolicies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchListObjectPoliciesResponse]

### ListPolicyAttachments
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchListPolicyAttachmentsResponse]

### LookupPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchLookupPolicyResponse]

### ListIndex
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchListIndexResponse]

### ListOutgoingTypedLinks
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchListOutgoingTypedLinksResponse]

### ListIncomingTypedLinks
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchListIncomingTypedLinksResponse]

### GetLinkAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchGetLinkAttributesResponse]

### ListObjectParents
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchListObjectParentsResponse]


# BatchRemoveFacetFromObject

### SchemaFacet
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.SchemaFacet'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes


# BatchUpdateLinkAttributes

### TypedLinkSpecifier
- **Type**: typing.Union[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkSpecifier, aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkSpecifierOutput]
- **Required**: Yes

### AttributeUpdates
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.LinkAttributeUpdate]
- **Required**: Yes


# BatchUpdateObjectAttributes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### AttributeUpdates
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectAttributeUpdate]
- **Required**: Yes


# BatchUpdateObjectAttributesResponse

### ObjectIdentifier
- **Type**: typing.Optional[str]


# BatchWriteOperation

### CreateObject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchCreateObject]

### AttachObject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchAttachObject]

### DetachObject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchDetachObject]

### UpdateObjectAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchUpdateObjectAttributes]

### DeleteObject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchDeleteObject]

### AddFacetToObject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchAddFacetToObject]

### RemoveFacetFromObject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchRemoveFacetFromObject]

### AttachPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchAttachPolicy]

### DetachPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchDetachPolicy]

### CreateIndex
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchCreateIndex]

### AttachToIndex
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchAttachToIndex]

### DetachFromIndex
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchDetachFromIndex]

### AttachTypedLink
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchAttachTypedLink]

### DetachTypedLink
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchDetachTypedLink]

### UpdateLinkAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchUpdateLinkAttributes]


# BatchWriteOperationResponse

### CreateObject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchCreateObjectResponse]

### AttachObject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchAttachObjectResponse]

### DetachObject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchDetachObjectResponse]

### UpdateObjectAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchUpdateObjectAttributesResponse]

### DeleteObject
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### AddFacetToObject
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### RemoveFacetFromObject
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### AttachPolicy
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### DetachPolicy
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### CreateIndex
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchCreateIndexResponse]

### AttachToIndex
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchAttachToIndexResponse]

### DetachFromIndex
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchDetachFromIndexResponse]

### AttachTypedLink
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchAttachTypedLinkResponse]

### DetachTypedLink
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### UpdateLinkAttributes
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# BatchWriteRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### Operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchWriteOperation]
- **Required**: Yes


# BatchWriteResponse

### Responses
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.BatchWriteOperationResponse]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDirectoryRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes


# CreateDirectoryResponse

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### AppliedSchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFacetRequest

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.FacetAttribute, aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.FacetAttributeOutput]]]

### ObjectType
- **Type**: typing.Optional[typing.Literal['INDEX', 'LEAF_NODE', 'NODE', 'POLICY']]

### FacetStyle
- **Type**: typing.Optional[typing.Literal['DYNAMIC', 'STATIC']]


# CreateIndexRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### OrderedIndexedAttributeList
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.AttributeKey]
- **Required**: Yes

### IsUnique
- **Type**: <class 'bool'>
- **Required**: Yes

### ParentReference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference]

### LinkName
- **Type**: typing.Optional[str]


# CreateIndexResponse

### ObjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes


# CreateObjectRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaFacets
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.SchemaFacet]
- **Required**: Yes

### ObjectAttributeList
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.AttributeKeyAndValue, aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.AttributeKeyAndValueOutput]]]

### ParentReference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference]

### LinkName
- **Type**: typing.Optional[str]


# CreateObjectResponse

### ObjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSchemaRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# CreateSchemaResponse

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTypedLinkFacetRequest

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### Facet
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkFacet'>
- **Required**: Yes


# DeleteDirectoryRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDirectoryResponse

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteFacetRequest

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteObjectRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes


# DeleteSchemaRequest

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSchemaResponse

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteTypedLinkFacetRequest

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DetachFromIndexRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### IndexReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### TargetReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes


# DetachFromIndexResponse

### DetachedObjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes


# DetachObjectRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ParentReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### LinkName
- **Type**: <class 'str'>
- **Required**: Yes


# DetachObjectResponse

### DetachedObjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes


# DetachPolicyRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes


# DetachTypedLinkRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### TypedLinkSpecifier
- **Type**: typing.Union[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkSpecifier, aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkSpecifierOutput]
- **Required**: Yes


# Directory

### Name
- **Type**: typing.Optional[str]

### DirectoryArn
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['DELETED', 'DISABLED', 'ENABLED']]

### CreationDateTime
- **Type**: typing.Optional[datetime.datetime]


# DisableDirectoryRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisableDirectoryResponse

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes


# EnableDirectoryRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes


# EnableDirectoryResponse

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes


# Facet

### Name
- **Type**: typing.Optional[str]

### ObjectType
- **Type**: typing.Optional[typing.Literal['INDEX', 'LEAF_NODE', 'NODE', 'POLICY']]

### FacetStyle
- **Type**: typing.Optional[typing.Literal['DYNAMIC', 'STATIC']]


# FacetAttribute

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeDefinition
- **Type**: typing.Union[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.FacetAttributeDefinition, aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.FacetAttributeDefinitionOutput, NoneType]

### AttributeReference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.FacetAttributeReference]

### RequiredBehavior
- **Type**: typing.Optional[typing.Literal['NOT_REQUIRED', 'REQUIRED_ALWAYS']]


# FacetAttributeDefinition

### Type
- **Type**: typing.Literal['BINARY', 'BOOLEAN', 'DATETIME', 'NUMBER', 'STRING', 'VARIANT']
- **Required**: Yes

### DefaultValue
- **Type**: typing.Union[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedAttributeValue, aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedAttributeValueOutput, NoneType]

### IsImmutable
- **Type**: typing.Optional[bool]

### Rules
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.Rule, aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.RuleOutput]]]


# FacetAttributeDefinitionOutput

### Type
- **Type**: typing.Literal['BINARY', 'BOOLEAN', 'DATETIME', 'NUMBER', 'STRING', 'VARIANT']
- **Required**: Yes

### DefaultValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedAttributeValueOutput]

### IsImmutable
- **Type**: typing.Optional[bool]

### Rules
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.RuleOutput]]


# FacetAttributeOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.FacetAttributeDefinitionOutput]

### AttributeReference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.FacetAttributeReference]

### RequiredBehavior
- **Type**: typing.Optional[typing.Literal['NOT_REQUIRED', 'REQUIRED_ALWAYS']]


# FacetAttributeReference

### TargetFacetName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetAttributeName
- **Type**: <class 'str'>
- **Required**: Yes


# FacetAttributeUpdate

### Attribute
- **Type**: typing.Union[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.FacetAttribute, aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.FacetAttributeOutput, NoneType]

### Action
- **Type**: typing.Optional[typing.Literal['CREATE_OR_UPDATE', 'DELETE']]


# GetAppliedSchemaVersionRequest

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetAppliedSchemaVersionResponse

### AppliedSchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes


# GetDirectoryRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetDirectoryResponse

### Directory
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.Directory'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes


# GetFacetRequest

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetFacetResponse

### Facet
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.Facet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes


# GetLinkAttributesRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### TypedLinkSpecifier
- **Type**: typing.Union[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkSpecifier, aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkSpecifierOutput]
- **Required**: Yes

### AttributeNames
- **Type**: typing.List[str]
- **Required**: Yes

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]


# GetLinkAttributesResponse

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.AttributeKeyAndValueOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes


# GetObjectAttributesRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### SchemaFacet
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.SchemaFacet'>
- **Required**: Yes

### AttributeNames
- **Type**: typing.List[str]
- **Required**: Yes

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]


# GetObjectAttributesResponse

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.AttributeKeyAndValueOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes


# GetObjectInformationRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]


# GetObjectInformationResponse

### SchemaFacets
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.SchemaFacet]
- **Required**: Yes

### ObjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes


# GetSchemaAsJsonRequest

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetSchemaAsJsonResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Document
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes


# GetTypedLinkFacetInformationRequest

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetTypedLinkFacetInformationResponse

### IdentityAttributeOrder
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes


# IndexAttachment

### IndexedAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.AttributeKeyAndValueOutput]]

### ObjectIdentifier
- **Type**: typing.Optional[str]


# LinkAttributeAction

### AttributeActionType
- **Type**: typing.Optional[typing.Literal['CREATE_OR_UPDATE', 'DELETE']]

### AttributeUpdateValue
- **Type**: typing.Union[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedAttributeValue, aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedAttributeValueOutput, NoneType]


# LinkAttributeUpdate

### AttributeKey
- **Type**: <class 'NoneType'>

### AttributeAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.LinkAttributeAction]


# ListAppliedSchemaArnsRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaArn
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAppliedSchemaArnsRequestPaginate

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.PaginatorConfig]


# ListAppliedSchemaArnsResponse

### SchemaArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAttachedIndicesRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### TargetReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]


# ListAttachedIndicesRequestPaginate

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### TargetReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.PaginatorConfig]


# ListAttachedIndicesResponse

### IndexAttachments
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.IndexAttachment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDevelopmentSchemaArnsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDevelopmentSchemaArnsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.PaginatorConfig]


# ListDevelopmentSchemaArnsResponse

### SchemaArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDirectoriesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### state
- **Type**: typing.Optional[typing.Literal['DELETED', 'DISABLED', 'ENABLED']]


# ListDirectoriesRequestPaginate

### state
- **Type**: typing.Optional[typing.Literal['DELETED', 'DISABLED', 'ENABLED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.PaginatorConfig]


# ListDirectoriesResponse

### Directories
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.Directory]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFacetAttributesRequest

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListFacetAttributesRequestPaginate

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.PaginatorConfig]


# ListFacetAttributesResponse

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.FacetAttributeOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFacetNamesRequest

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListFacetNamesRequestPaginate

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.PaginatorConfig]


# ListFacetNamesResponse

### FacetNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIncomingTypedLinksRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### FilterAttributeRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkAttributeRange]]

### FilterTypedLink
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkSchemaAndFacetName]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]


# ListIncomingTypedLinksRequestPaginate

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### FilterAttributeRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkAttributeRange]]

### FilterTypedLink
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkSchemaAndFacetName]

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.PaginatorConfig]


# ListIncomingTypedLinksResponse

### LinkSpecifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkSpecifierOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIndexRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### IndexReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### RangesOnIndexedValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectAttributeRange]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]


# ListIndexRequestPaginate

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### IndexReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### RangesOnIndexedValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectAttributeRange]]

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.PaginatorConfig]


# ListIndexResponse

### IndexAttachments
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.IndexAttachment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListManagedSchemaArnsRequest

### SchemaArn
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListManagedSchemaArnsRequestPaginate

### SchemaArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.PaginatorConfig]


# ListManagedSchemaArnsResponse

### SchemaArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListObjectAttributesRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]

### FacetFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.SchemaFacet]


# ListObjectAttributesRequestPaginate

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]

### FacetFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.SchemaFacet]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.PaginatorConfig]


# ListObjectAttributesResponse

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.AttributeKeyAndValueOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListObjectChildrenRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]


# ListObjectChildrenResponse

### Children
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListObjectParentPathsRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListObjectParentPathsRequestPaginate

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.PaginatorConfig]


# ListObjectParentPathsResponse

### PathToObjectIdentifiersList
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.PathToObjectIdentifiers]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListObjectParentsRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]

### IncludeAllLinksToEachParent
- **Type**: typing.Optional[bool]


# ListObjectParentsResponse

### Parents
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ParentLinks
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectIdentifierAndLinkNameTuple]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListObjectPoliciesRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]


# ListObjectPoliciesRequestPaginate

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.PaginatorConfig]


# ListObjectPoliciesResponse

### AttachedPolicyIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOutgoingTypedLinksRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### FilterAttributeRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkAttributeRange]]

### FilterTypedLink
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkSchemaAndFacetName]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]


# ListOutgoingTypedLinksRequestPaginate

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### FilterAttributeRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkAttributeRange]]

### FilterTypedLink
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkSchemaAndFacetName]

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.PaginatorConfig]


# ListOutgoingTypedLinksResponse

### TypedLinkSpecifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkSpecifierOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPolicyAttachmentsRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]


# ListPolicyAttachmentsRequestPaginate

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.PaginatorConfig]


# ListPolicyAttachmentsResponse

### ObjectIdentifiers
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPublishedSchemaArnsRequest

### SchemaArn
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPublishedSchemaArnsRequestPaginate

### SchemaArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.PaginatorConfig]


# ListPublishedSchemaArnsResponse

### SchemaArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTagsForResourceRequestPaginate

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.PaginatorConfig]


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTypedLinkFacetAttributesRequest

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTypedLinkFacetAttributesRequestPaginate

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.PaginatorConfig]


# ListTypedLinkFacetAttributesResponse

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkAttributeDefinitionOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTypedLinkFacetNamesRequest

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTypedLinkFacetNamesRequestPaginate

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.PaginatorConfig]


# ListTypedLinkFacetNamesResponse

### FacetNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LookupPolicyRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# LookupPolicyRequestPaginate

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.PaginatorConfig]


# LookupPolicyResponse

### PolicyToPathList
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.PolicyToPath]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ObjectAttributeAction

### ObjectAttributeActionType
- **Type**: typing.Optional[typing.Literal['CREATE_OR_UPDATE', 'DELETE']]

### ObjectAttributeUpdateValue
- **Type**: typing.Union[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedAttributeValue, aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedAttributeValueOutput, NoneType]


# ObjectAttributeRange

### AttributeKey
- **Type**: <class 'NoneType'>

### Range
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedAttributeValueRange]


# ObjectAttributeUpdate

### ObjectAttributeKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.AttributeKey]

### ObjectAttributeAction
- **Type**: <class 'NoneType'>


# ObjectIdentifierAndLinkNameTuple

### ObjectIdentifier
- **Type**: typing.Optional[str]

### LinkName
- **Type**: typing.Optional[str]


# ObjectReference

### Selector
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PathToObjectIdentifiers

### Path
- **Type**: typing.Optional[str]

### ObjectIdentifiers
- **Type**: typing.Optional[typing.List[str]]


# PolicyAttachment

### PolicyId
- **Type**: typing.Optional[str]

### ObjectIdentifier
- **Type**: typing.Optional[str]

### PolicyType
- **Type**: typing.Optional[str]


# PolicyToPath

### Path
- **Type**: typing.Optional[str]

### Policies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.PolicyAttachment]]


# PublishSchemaRequest

### DevelopmentSchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### MinorVersion
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# PublishSchemaResponse

### PublishedSchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes


# PutSchemaFromJsonRequest

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### Document
- **Type**: <class 'str'>
- **Required**: Yes


# PutSchemaFromJsonResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes


# RemoveFacetFromObjectRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaFacet
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.SchemaFacet'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
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


# Rule

### Type
- **Type**: typing.Optional[typing.Literal['BINARY_LENGTH', 'NUMBER_COMPARISON', 'STRING_FROM_SET', 'STRING_LENGTH']]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# RuleOutput

### Type
- **Type**: typing.Optional[typing.Literal['BINARY_LENGTH', 'NUMBER_COMPARISON', 'STRING_FROM_SET', 'STRING_LENGTH']]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# SchemaFacet

### SchemaArn
- **Type**: typing.Optional[str]

### FacetName
- **Type**: typing.Optional[str]


# Tag

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.Tag]
- **Required**: Yes


# TypedAttributeValue

### StringValue
- **Type**: typing.Optional[str]

### BinaryValue
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]

### BooleanValue
- **Type**: typing.Optional[bool]

### NumberValue
- **Type**: typing.Optional[str]

### DatetimeValue
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# TypedAttributeValueOutput

### StringValue
- **Type**: typing.Optional[str]

### BinaryValue
- **Type**: typing.Optional[bytes]

### BooleanValue
- **Type**: typing.Optional[bool]

### NumberValue
- **Type**: typing.Optional[str]

### DatetimeValue
- **Type**: typing.Optional[datetime.datetime]


# TypedAttributeValueRange

### StartMode
- **Type**: typing.Literal['EXCLUSIVE', 'FIRST', 'INCLUSIVE', 'LAST', 'LAST_BEFORE_MISSING_VALUES']
- **Required**: Yes

### EndMode
- **Type**: typing.Literal['EXCLUSIVE', 'FIRST', 'INCLUSIVE', 'LAST', 'LAST_BEFORE_MISSING_VALUES']
- **Required**: Yes

### StartValue
- **Type**: typing.Union[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedAttributeValue, aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedAttributeValueOutput, NoneType]

### EndValue
- **Type**: typing.Union[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedAttributeValue, aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedAttributeValueOutput, NoneType]


# TypedLinkAttributeDefinition

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['BINARY', 'BOOLEAN', 'DATETIME', 'NUMBER', 'STRING', 'VARIANT']
- **Required**: Yes

### RequiredBehavior
- **Type**: typing.Literal['NOT_REQUIRED', 'REQUIRED_ALWAYS']
- **Required**: Yes

### DefaultValue
- **Type**: typing.Union[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedAttributeValue, aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedAttributeValueOutput, NoneType]

### IsImmutable
- **Type**: typing.Optional[bool]

### Rules
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.Rule, aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.RuleOutput]]]


# TypedLinkAttributeDefinitionOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['BINARY', 'BOOLEAN', 'DATETIME', 'NUMBER', 'STRING', 'VARIANT']
- **Required**: Yes

### RequiredBehavior
- **Type**: typing.Literal['NOT_REQUIRED', 'REQUIRED_ALWAYS']
- **Required**: Yes

### DefaultValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedAttributeValueOutput]

### IsImmutable
- **Type**: typing.Optional[bool]

### Rules
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.RuleOutput]]


# TypedLinkAttributeRange

### Range
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedAttributeValueRange'>
- **Required**: Yes

### AttributeName
- **Type**: typing.Optional[str]


# TypedLinkFacet

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkAttributeDefinition, aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkAttributeDefinitionOutput]]
- **Required**: Yes

### IdentityAttributeOrder
- **Type**: typing.List[str]
- **Required**: Yes


# TypedLinkFacetAttributeUpdate

### Attribute
- **Type**: typing.Union[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkAttributeDefinition, aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkAttributeDefinitionOutput]
- **Required**: Yes

### Action
- **Type**: typing.Literal['CREATE_OR_UPDATE', 'DELETE']
- **Required**: Yes


# TypedLinkSchemaAndFacetName

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### TypedLinkName
- **Type**: <class 'str'>
- **Required**: Yes


# TypedLinkSpecifier

### TypedLinkFacet
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkSchemaAndFacetName'>
- **Required**: Yes

### SourceObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### TargetObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### IdentityAttributeValues
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.AttributeNameAndValue, aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.AttributeNameAndValueOutput]]
- **Required**: Yes


# TypedLinkSpecifierOutput

### TypedLinkFacet
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkSchemaAndFacetName'>
- **Required**: Yes

### SourceObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### TargetObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### IdentityAttributeValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.AttributeNameAndValueOutput]
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateFacetRequest

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeUpdates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.FacetAttributeUpdate]]

### ObjectType
- **Type**: typing.Optional[typing.Literal['INDEX', 'LEAF_NODE', 'NODE', 'POLICY']]


# UpdateLinkAttributesRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### TypedLinkSpecifier
- **Type**: typing.Union[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkSpecifier, aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkSpecifierOutput]
- **Required**: Yes

### AttributeUpdates
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.LinkAttributeUpdate]
- **Required**: Yes


# UpdateObjectAttributesRequest

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectReference'>
- **Required**: Yes

### AttributeUpdates
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ObjectAttributeUpdate]
- **Required**: Yes


# UpdateObjectAttributesResponse

### ObjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSchemaRequest

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateSchemaResponse

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTypedLinkFacetRequest

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeUpdates
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.TypedLinkFacetAttributeUpdate]
- **Required**: Yes

### IdentityAttributeOrder
- **Type**: typing.List[str]
- **Required**: Yes


# UpgradeAppliedSchemaRequest

### PublishedSchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# UpgradeAppliedSchemaResponse

### UpgradedSchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes


# UpgradePublishedSchemaRequest

### DevelopmentSchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### PublishedSchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### MinorVersion
- **Type**: <class 'str'>
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# UpgradePublishedSchemaResponse

### UpgradedSchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_classes.ResponseMetadata'>
- **Required**: Yes


