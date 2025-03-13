# Clouddirectory Classes

# AddFacetToObjectRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaFacet
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.SchemaFacetTypeDef'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### ObjectAttributeList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.clouddirectory_classes.AttributeKeyAndValueUnionTypeDef]]


# ApplySchemaRequestTypeDef

### PublishedSchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes


# ApplySchemaResponseTypeDef

### AppliedSchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AttachObjectRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ParentReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### ChildReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### LinkName
- **Type**: <class 'str'>
- **Required**: Yes


# AttachObjectResponseTypeDef

### AttachedObjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AttachPolicyRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes


# AttachToIndexRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### IndexReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### TargetReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes


# AttachToIndexResponseTypeDef

### AttachedObjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AttachTypedLinkRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### TargetObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### TypedLinkFacet
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.TypedLinkSchemaAndFacetNameTypeDef'>
- **Required**: Yes

### Attributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.clouddirectory_classes.AttributeNameAndValueUnionTypeDef]
- **Required**: Yes


# AttachTypedLinkResponseTypeDef

### TypedLinkSpecifier
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.TypedLinkSpecifierOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AttributeKeyAndValueOutputTypeDef

### Key
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.AttributeKeyTypeDef'>
- **Required**: Yes

### Value
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.TypedAttributeValueOutputTypeDef'>
- **Required**: Yes


# AttributeKeyAndValueTypeDef

### Key
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.AttributeKeyTypeDef'>
- **Required**: Yes

### Value
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.TypedAttributeValueUnionTypeDef'>
- **Required**: Yes


# AttributeKeyAndValueUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AttributeKeyTypeDef

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### FacetName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# AttributeNameAndValueOutputTypeDef

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.TypedAttributeValueOutputTypeDef'>
- **Required**: Yes


# AttributeNameAndValueTypeDef

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.TypedAttributeValueUnionTypeDef'>
- **Required**: Yes


# AttributeNameAndValueUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchAddFacetToObjectTypeDef

### SchemaFacet
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.SchemaFacetTypeDef'>
- **Required**: Yes

### ObjectAttributeList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.clouddirectory_classes.AttributeKeyAndValueUnionTypeDef]
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes


# BatchAttachObjectResponseTypeDef

### attachedObjectIdentifier
- **Type**: typing.Optional[str]


# BatchAttachObjectTypeDef

### ParentReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### ChildReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### LinkName
- **Type**: <class 'str'>
- **Required**: Yes


# BatchAttachPolicyTypeDef

### PolicyReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes


# BatchAttachToIndexResponseTypeDef

### AttachedObjectIdentifier
- **Type**: typing.Optional[str]


# BatchAttachToIndexTypeDef

### IndexReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### TargetReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes


# BatchAttachTypedLinkResponseTypeDef

### TypedLinkSpecifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.TypedLinkSpecifierOutputTypeDef]


# BatchAttachTypedLinkTypeDef

### SourceObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### TargetObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### TypedLinkFacet
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.TypedLinkSchemaAndFacetNameTypeDef'>
- **Required**: Yes

### Attributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.clouddirectory_classes.AttributeNameAndValueUnionTypeDef]
- **Required**: Yes


# BatchCreateIndexResponseTypeDef

### ObjectIdentifier
- **Type**: typing.Optional[str]


# BatchCreateIndexTypeDef

### OrderedIndexedAttributeList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.clouddirectory_classes.AttributeKeyTypeDef]
- **Required**: Yes

### IsUnique
- **Type**: <class 'bool'>
- **Required**: Yes

### ParentReference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef]

### LinkName
- **Type**: typing.Optional[str]

### BatchReferenceName
- **Type**: typing.Optional[str]


# BatchCreateObjectResponseTypeDef

### ObjectIdentifier
- **Type**: typing.Optional[str]


# BatchCreateObjectTypeDef

### SchemaFacet
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.clouddirectory_classes.SchemaFacetTypeDef]
- **Required**: Yes

### ObjectAttributeList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.clouddirectory_classes.AttributeKeyAndValueTypeDef]
- **Required**: Yes

### ParentReference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef]

### LinkName
- **Type**: typing.Optional[str]

### BatchReferenceName
- **Type**: typing.Optional[str]


# BatchDeleteObjectTypeDef

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes


# BatchDetachFromIndexResponseTypeDef

### DetachedObjectIdentifier
- **Type**: typing.Optional[str]


# BatchDetachFromIndexTypeDef

### IndexReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### TargetReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes


# BatchDetachObjectResponseTypeDef

### detachedObjectIdentifier
- **Type**: typing.Optional[str]


# BatchDetachObjectTypeDef

### ParentReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### LinkName
- **Type**: <class 'str'>
- **Required**: Yes

### BatchReferenceName
- **Type**: typing.Optional[str]


# BatchDetachPolicyTypeDef

### PolicyReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes


# BatchDetachTypedLinkTypeDef

### TypedLinkSpecifier
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.TypedLinkSpecifierUnionTypeDef'>
- **Required**: Yes


# BatchGetLinkAttributesResponseTypeDef

### Attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory_classes.AttributeKeyAndValueOutputTypeDef]]


# BatchGetLinkAttributesTypeDef

### TypedLinkSpecifier
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.TypedLinkSpecifierUnionTypeDef'>
- **Required**: Yes

### AttributeNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetObjectAttributesResponseTypeDef

### Attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory_classes.AttributeKeyAndValueOutputTypeDef]]


# BatchGetObjectAttributesTypeDef

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### SchemaFacet
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.SchemaFacetTypeDef'>
- **Required**: Yes

### AttributeNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetObjectInformationResponseTypeDef

### SchemaFacets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory_classes.SchemaFacetTypeDef]]

### ObjectIdentifier
- **Type**: typing.Optional[str]


# BatchGetObjectInformationTypeDef

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes


# BatchListAttachedIndicesResponseTypeDef

### IndexAttachments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory_classes.IndexAttachmentTypeDef]]

### NextToken
- **Type**: typing.Optional[str]


# BatchListAttachedIndicesTypeDef

### TargetReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# BatchListIncomingTypedLinksResponseTypeDef

### LinkSpecifiers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory_classes.TypedLinkSpecifierOutputTypeDef]]

### NextToken
- **Type**: typing.Optional[str]


# BatchListIncomingTypedLinksTypeDef

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### FilterAttributeRanges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.clouddirectory_classes.TypedLinkAttributeRangeTypeDef]]

### FilterTypedLink
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.TypedLinkSchemaAndFacetNameTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# BatchListIndexResponseTypeDef

### IndexAttachments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory_classes.IndexAttachmentTypeDef]]

### NextToken
- **Type**: typing.Optional[str]


# BatchListIndexTypeDef

### IndexReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### RangesOnIndexedValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectAttributeRangeTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# BatchListObjectAttributesResponseTypeDef

### Attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory_classes.AttributeKeyAndValueOutputTypeDef]]

### NextToken
- **Type**: typing.Optional[str]


# BatchListObjectAttributesTypeDef

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### FacetFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.SchemaFacetTypeDef]


# BatchListObjectChildrenResponseTypeDef

### Children
- **Type**: typing.Optional[typing.Dict[str, str]]

### NextToken
- **Type**: typing.Optional[str]


# BatchListObjectChildrenTypeDef

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# BatchListObjectParentPathsResponseTypeDef

### PathToObjectIdentifiersList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory_classes.PathToObjectIdentifiersTypeDef]]

### NextToken
- **Type**: typing.Optional[str]


# BatchListObjectParentPathsTypeDef

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# BatchListObjectParentsResponseTypeDef

### ParentLinks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectIdentifierAndLinkNameTupleTypeDef]]

### NextToken
- **Type**: typing.Optional[str]


# BatchListObjectParentsTypeDef

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# BatchListObjectPoliciesResponseTypeDef

### AttachedPolicyIds
- **Type**: typing.Optional[typing.List[str]]

### NextToken
- **Type**: typing.Optional[str]


# BatchListObjectPoliciesTypeDef

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# BatchListOutgoingTypedLinksResponseTypeDef

### TypedLinkSpecifiers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory_classes.TypedLinkSpecifierOutputTypeDef]]

### NextToken
- **Type**: typing.Optional[str]


# BatchListOutgoingTypedLinksTypeDef

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### FilterAttributeRanges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.clouddirectory_classes.TypedLinkAttributeRangeTypeDef]]

### FilterTypedLink
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.TypedLinkSchemaAndFacetNameTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# BatchListPolicyAttachmentsResponseTypeDef

### ObjectIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### NextToken
- **Type**: typing.Optional[str]


# BatchListPolicyAttachmentsTypeDef

### PolicyReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# BatchLookupPolicyResponseTypeDef

### PolicyToPathList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory_classes.PolicyToPathTypeDef]]

### NextToken
- **Type**: typing.Optional[str]


# BatchLookupPolicyTypeDef

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# BatchReadExceptionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchReadOperationResponseTypeDef

### SuccessfulResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchReadSuccessfulResponseTypeDef]

### ExceptionResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchReadExceptionTypeDef]


# BatchReadOperationTypeDef

### ListObjectAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchListObjectAttributesTypeDef]

### ListObjectChildren
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchListObjectChildrenTypeDef]

### ListAttachedIndices
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchListAttachedIndicesTypeDef]

### ListObjectParentPaths
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchListObjectParentPathsTypeDef]

### GetObjectInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchGetObjectInformationTypeDef]

### GetObjectAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchGetObjectAttributesTypeDef]

### ListObjectParents
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchListObjectParentsTypeDef]

### ListObjectPolicies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchListObjectPoliciesTypeDef]

### ListPolicyAttachments
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchListPolicyAttachmentsTypeDef]

### LookupPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchLookupPolicyTypeDef]

### ListIndex
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchListIndexTypeDef]

### ListOutgoingTypedLinks
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchListOutgoingTypedLinksTypeDef]

### ListIncomingTypedLinks
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchListIncomingTypedLinksTypeDef]

### GetLinkAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchGetLinkAttributesTypeDef]


# BatchReadRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### Operations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchReadOperationTypeDef]
- **Required**: Yes

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]


# BatchReadResponseTypeDef

### Responses
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchReadOperationResponseTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchReadSuccessfulResponseTypeDef

### ListObjectAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchListObjectAttributesResponseTypeDef]

### ListObjectChildren
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchListObjectChildrenResponseTypeDef]

### GetObjectInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchGetObjectInformationResponseTypeDef]

### GetObjectAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchGetObjectAttributesResponseTypeDef]

### ListAttachedIndices
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchListAttachedIndicesResponseTypeDef]

### ListObjectParentPaths
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchListObjectParentPathsResponseTypeDef]

### ListObjectPolicies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchListObjectPoliciesResponseTypeDef]

### ListPolicyAttachments
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchListPolicyAttachmentsResponseTypeDef]

### LookupPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchLookupPolicyResponseTypeDef]

### ListIndex
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchListIndexResponseTypeDef]

### ListOutgoingTypedLinks
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchListOutgoingTypedLinksResponseTypeDef]

### ListIncomingTypedLinks
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchListIncomingTypedLinksResponseTypeDef]

### GetLinkAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchGetLinkAttributesResponseTypeDef]

### ListObjectParents
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchListObjectParentsResponseTypeDef]


# BatchRemoveFacetFromObjectTypeDef

### SchemaFacet
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.SchemaFacetTypeDef'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes


# BatchUpdateLinkAttributesTypeDef

### TypedLinkSpecifier
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.TypedLinkSpecifierUnionTypeDef'>
- **Required**: Yes

### AttributeUpdates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.clouddirectory_classes.LinkAttributeUpdateTypeDef]
- **Required**: Yes


# BatchUpdateObjectAttributesResponseTypeDef

### ObjectIdentifier
- **Type**: typing.Optional[str]


# BatchUpdateObjectAttributesTypeDef

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### AttributeUpdates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectAttributeUpdateTypeDef]
- **Required**: Yes


# BatchWriteOperationResponseTypeDef

### CreateObject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchCreateObjectResponseTypeDef]

### AttachObject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchAttachObjectResponseTypeDef]

### DetachObject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchDetachObjectResponseTypeDef]

### UpdateObjectAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchUpdateObjectAttributesResponseTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchCreateIndexResponseTypeDef]

### AttachToIndex
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchAttachToIndexResponseTypeDef]

### DetachFromIndex
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchDetachFromIndexResponseTypeDef]

### AttachTypedLink
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchAttachTypedLinkResponseTypeDef]

### DetachTypedLink
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### UpdateLinkAttributes
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# BatchWriteOperationTypeDef

### CreateObject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchCreateObjectTypeDef]

### AttachObject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchAttachObjectTypeDef]

### DetachObject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchDetachObjectTypeDef]

### UpdateObjectAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchUpdateObjectAttributesTypeDef]

### DeleteObject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchDeleteObjectTypeDef]

### AddFacetToObject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchAddFacetToObjectTypeDef]

### RemoveFacetFromObject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchRemoveFacetFromObjectTypeDef]

### AttachPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchAttachPolicyTypeDef]

### DetachPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchDetachPolicyTypeDef]

### CreateIndex
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchCreateIndexTypeDef]

### AttachToIndex
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchAttachToIndexTypeDef]

### DetachFromIndex
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchDetachFromIndexTypeDef]

### AttachTypedLink
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchAttachTypedLinkTypeDef]

### DetachTypedLink
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchDetachTypedLinkTypeDef]

### UpdateLinkAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchUpdateLinkAttributesTypeDef]


# BatchWriteRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### Operations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchWriteOperationTypeDef]
- **Required**: Yes


# BatchWriteResponseTypeDef

### Responses
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory_classes.BatchWriteOperationResponseTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateDirectoryRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes


# CreateDirectoryResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFacetRequestTypeDef

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.clouddirectory_classes.FacetAttributeUnionTypeDef]]

### ObjectType
- **Type**: typing.Optional[typing.Literal['INDEX', 'LEAF_NODE', 'NODE', 'POLICY']]

### FacetStyle
- **Type**: typing.Optional[typing.Literal['DYNAMIC', 'STATIC']]


# CreateIndexRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### OrderedIndexedAttributeList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.clouddirectory_classes.AttributeKeyTypeDef]
- **Required**: Yes

### IsUnique
- **Type**: <class 'bool'>
- **Required**: Yes

### ParentReference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef]

### LinkName
- **Type**: typing.Optional[str]


# CreateIndexResponseTypeDef

### ObjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateObjectRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaFacets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.clouddirectory_classes.SchemaFacetTypeDef]
- **Required**: Yes

### ObjectAttributeList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.clouddirectory_classes.AttributeKeyAndValueUnionTypeDef]]

### ParentReference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef]

### LinkName
- **Type**: typing.Optional[str]


# CreateObjectResponseTypeDef

### ObjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSchemaRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# CreateSchemaResponseTypeDef

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTypedLinkFacetRequestTypeDef

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### Facet
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.TypedLinkFacetTypeDef'>
- **Required**: Yes


# DeleteDirectoryRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDirectoryResponseTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteFacetRequestTypeDef

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteObjectRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes


# DeleteSchemaRequestTypeDef

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSchemaResponseTypeDef

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteTypedLinkFacetRequestTypeDef

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DetachFromIndexRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### IndexReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### TargetReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes


# DetachFromIndexResponseTypeDef

### DetachedObjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetachObjectRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ParentReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### LinkName
- **Type**: <class 'str'>
- **Required**: Yes


# DetachObjectResponseTypeDef

### DetachedObjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetachPolicyRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes


# DetachTypedLinkRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### TypedLinkSpecifier
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.TypedLinkSpecifierUnionTypeDef'>
- **Required**: Yes


# DirectoryTypeDef

### Name
- **Type**: typing.Optional[str]

### DirectoryArn
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['DELETED', 'DISABLED', 'ENABLED']]

### CreationDateTime
- **Type**: typing.Optional[datetime.datetime]


# DisableDirectoryRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisableDirectoryResponseTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnableDirectoryRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes


# EnableDirectoryResponseTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FacetAttributeDefinitionOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FacetAttributeDefinitionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FacetAttributeOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.FacetAttributeDefinitionOutputTypeDef]

### AttributeReference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.FacetAttributeReferenceTypeDef]

### RequiredBehavior
- **Type**: typing.Optional[typing.Literal['NOT_REQUIRED', 'REQUIRED_ALWAYS']]


# FacetAttributeReferenceTypeDef

### TargetFacetName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetAttributeName
- **Type**: <class 'str'>
- **Required**: Yes


# FacetAttributeTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.FacetAttributeDefinitionUnionTypeDef]

### AttributeReference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.FacetAttributeReferenceTypeDef]

### RequiredBehavior
- **Type**: typing.Optional[typing.Literal['NOT_REQUIRED', 'REQUIRED_ALWAYS']]


# FacetAttributeUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FacetAttributeUpdateTypeDef

### Attribute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.FacetAttributeUnionTypeDef]

### Action
- **Type**: typing.Optional[typing.Literal['CREATE_OR_UPDATE', 'DELETE']]


# FacetTypeDef

### Name
- **Type**: typing.Optional[str]

### ObjectType
- **Type**: typing.Optional[typing.Literal['INDEX', 'LEAF_NODE', 'NODE', 'POLICY']]

### FacetStyle
- **Type**: typing.Optional[typing.Literal['DYNAMIC', 'STATIC']]


# GetAppliedSchemaVersionRequestTypeDef

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetAppliedSchemaVersionResponseTypeDef

### AppliedSchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDirectoryRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetDirectoryResponseTypeDef

### Directory
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.DirectoryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFacetRequestTypeDef

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetFacetResponseTypeDef

### Facet
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.FacetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLinkAttributesRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### TypedLinkSpecifier
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.TypedLinkSpecifierUnionTypeDef'>
- **Required**: Yes

### AttributeNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]


# GetLinkAttributesResponseTypeDef

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory_classes.AttributeKeyAndValueOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetObjectAttributesRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### SchemaFacet
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.SchemaFacetTypeDef'>
- **Required**: Yes

### AttributeNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]


# GetObjectAttributesResponseTypeDef

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory_classes.AttributeKeyAndValueOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetObjectInformationRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]


# GetObjectInformationResponseTypeDef

### SchemaFacets
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory_classes.SchemaFacetTypeDef]
- **Required**: Yes

### ObjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSchemaAsJsonRequestTypeDef

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetSchemaAsJsonResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Document
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTypedLinkFacetInformationRequestTypeDef

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetTypedLinkFacetInformationResponseTypeDef

### IdentityAttributeOrder
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IndexAttachmentTypeDef

### IndexedAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory_classes.AttributeKeyAndValueOutputTypeDef]]

### ObjectIdentifier
- **Type**: typing.Optional[str]


# LinkAttributeActionTypeDef

### AttributeActionType
- **Type**: typing.Optional[typing.Literal['CREATE_OR_UPDATE', 'DELETE']]

### AttributeUpdateValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.TypedAttributeValueUnionTypeDef]


# LinkAttributeUpdateTypeDef

### AttributeKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.AttributeKeyTypeDef]

### AttributeAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.LinkAttributeActionTypeDef]


# ListAppliedSchemaArnsRequestPaginateTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.PaginatorConfigTypeDef]


# ListAppliedSchemaArnsRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaArn
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAppliedSchemaArnsResponseTypeDef

### SchemaArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAttachedIndicesRequestPaginateTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### TargetReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.PaginatorConfigTypeDef]


# ListAttachedIndicesRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### TargetReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]


# ListAttachedIndicesResponseTypeDef

### IndexAttachments
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory_classes.IndexAttachmentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDevelopmentSchemaArnsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.PaginatorConfigTypeDef]


# ListDevelopmentSchemaArnsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDevelopmentSchemaArnsResponseTypeDef

### SchemaArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDirectoriesRequestPaginateTypeDef

### state
- **Type**: typing.Optional[typing.Literal['DELETED', 'DISABLED', 'ENABLED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.PaginatorConfigTypeDef]


# ListDirectoriesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### state
- **Type**: typing.Optional[typing.Literal['DELETED', 'DISABLED', 'ENABLED']]


# ListDirectoriesResponseTypeDef

### Directories
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory_classes.DirectoryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFacetAttributesRequestPaginateTypeDef

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.PaginatorConfigTypeDef]


# ListFacetAttributesRequestTypeDef

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


# ListFacetAttributesResponseTypeDef

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory_classes.FacetAttributeOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFacetNamesRequestPaginateTypeDef

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.PaginatorConfigTypeDef]


# ListFacetNamesRequestTypeDef

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListFacetNamesResponseTypeDef

### FacetNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIncomingTypedLinksRequestPaginateTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### FilterAttributeRanges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.clouddirectory_classes.TypedLinkAttributeRangeTypeDef]]

### FilterTypedLink
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.TypedLinkSchemaAndFacetNameTypeDef]

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.PaginatorConfigTypeDef]


# ListIncomingTypedLinksRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### FilterAttributeRanges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.clouddirectory_classes.TypedLinkAttributeRangeTypeDef]]

### FilterTypedLink
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.TypedLinkSchemaAndFacetNameTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]


# ListIncomingTypedLinksResponseTypeDef

### LinkSpecifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory_classes.TypedLinkSpecifierOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIndexRequestPaginateTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### IndexReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### RangesOnIndexedValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectAttributeRangeTypeDef]]

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.PaginatorConfigTypeDef]


# ListIndexRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### IndexReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### RangesOnIndexedValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectAttributeRangeTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]


# ListIndexResponseTypeDef

### IndexAttachments
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory_classes.IndexAttachmentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListManagedSchemaArnsRequestPaginateTypeDef

### SchemaArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.PaginatorConfigTypeDef]


# ListManagedSchemaArnsRequestTypeDef

### SchemaArn
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListManagedSchemaArnsResponseTypeDef

### SchemaArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListObjectAttributesRequestPaginateTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]

### FacetFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.SchemaFacetTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.PaginatorConfigTypeDef]


# ListObjectAttributesRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]

### FacetFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.SchemaFacetTypeDef]


# ListObjectAttributesResponseTypeDef

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory_classes.AttributeKeyAndValueOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListObjectChildrenRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]


# ListObjectChildrenResponseTypeDef

### Children
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListObjectParentPathsRequestPaginateTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.PaginatorConfigTypeDef]


# ListObjectParentPathsRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListObjectParentPathsResponseTypeDef

### PathToObjectIdentifiersList
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory_classes.PathToObjectIdentifiersTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListObjectParentsRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]

### IncludeAllLinksToEachParent
- **Type**: typing.Optional[bool]


# ListObjectParentsResponseTypeDef

### Parents
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ParentLinks
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectIdentifierAndLinkNameTupleTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListObjectPoliciesRequestPaginateTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.PaginatorConfigTypeDef]


# ListObjectPoliciesRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]


# ListObjectPoliciesResponseTypeDef

### AttachedPolicyIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOutgoingTypedLinksRequestPaginateTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### FilterAttributeRanges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.clouddirectory_classes.TypedLinkAttributeRangeTypeDef]]

### FilterTypedLink
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.TypedLinkSchemaAndFacetNameTypeDef]

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.PaginatorConfigTypeDef]


# ListOutgoingTypedLinksRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### FilterAttributeRanges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.clouddirectory_classes.TypedLinkAttributeRangeTypeDef]]

### FilterTypedLink
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.TypedLinkSchemaAndFacetNameTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]


# ListOutgoingTypedLinksResponseTypeDef

### TypedLinkSpecifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory_classes.TypedLinkSpecifierOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPolicyAttachmentsRequestPaginateTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.PaginatorConfigTypeDef]


# ListPolicyAttachmentsRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ConsistencyLevel
- **Type**: typing.Optional[typing.Literal['EVENTUAL', 'SERIALIZABLE']]


# ListPolicyAttachmentsResponseTypeDef

### ObjectIdentifiers
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPublishedSchemaArnsRequestPaginateTypeDef

### SchemaArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.PaginatorConfigTypeDef]


# ListPublishedSchemaArnsRequestTypeDef

### SchemaArn
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPublishedSchemaArnsResponseTypeDef

### SchemaArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestPaginateTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.PaginatorConfigTypeDef]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTypedLinkFacetAttributesRequestPaginateTypeDef

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.PaginatorConfigTypeDef]


# ListTypedLinkFacetAttributesRequestTypeDef

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


# ListTypedLinkFacetAttributesResponseTypeDef

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory_classes.TypedLinkAttributeDefinitionOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTypedLinkFacetNamesRequestPaginateTypeDef

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.PaginatorConfigTypeDef]


# ListTypedLinkFacetNamesRequestTypeDef

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTypedLinkFacetNamesResponseTypeDef

### FacetNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LookupPolicyRequestPaginateTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.PaginatorConfigTypeDef]


# LookupPolicyRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# LookupPolicyResponseTypeDef

### PolicyToPathList
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory_classes.PolicyToPathTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ObjectAttributeActionTypeDef

### ObjectAttributeActionType
- **Type**: typing.Optional[typing.Literal['CREATE_OR_UPDATE', 'DELETE']]

### ObjectAttributeUpdateValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.TypedAttributeValueUnionTypeDef]


# ObjectAttributeRangeTypeDef

### AttributeKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.AttributeKeyTypeDef]

### Range
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.TypedAttributeValueRangeTypeDef]


# ObjectAttributeUpdateTypeDef

### ObjectAttributeKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.AttributeKeyTypeDef]

### ObjectAttributeAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectAttributeActionTypeDef]


# ObjectIdentifierAndLinkNameTupleTypeDef

### ObjectIdentifier
- **Type**: typing.Optional[str]

### LinkName
- **Type**: typing.Optional[str]


# ObjectReferenceTypeDef

### Selector
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PathToObjectIdentifiersTypeDef

### Path
- **Type**: typing.Optional[str]

### ObjectIdentifiers
- **Type**: typing.Optional[typing.List[str]]


# PolicyAttachmentTypeDef

### PolicyId
- **Type**: typing.Optional[str]

### ObjectIdentifier
- **Type**: typing.Optional[str]

### PolicyType
- **Type**: typing.Optional[str]


# PolicyToPathTypeDef

### Path
- **Type**: typing.Optional[str]

### Policies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.clouddirectory_classes.PolicyAttachmentTypeDef]]


# PublishSchemaRequestTypeDef

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


# PublishSchemaResponseTypeDef

### PublishedSchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutSchemaFromJsonRequestTypeDef

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### Document
- **Type**: <class 'str'>
- **Required**: Yes


# PutSchemaFromJsonResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RemoveFacetFromObjectRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaFacet
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.SchemaFacetTypeDef'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes


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


# SchemaFacetTypeDef

### SchemaArn
- **Type**: typing.Optional[str]

### FacetName
- **Type**: typing.Optional[str]


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.clouddirectory_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TypedAttributeValueOutputTypeDef

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


# TypedAttributeValueRangeTypeDef

### StartMode
- **Type**: typing.Literal['EXCLUSIVE', 'FIRST', 'INCLUSIVE', 'LAST', 'LAST_BEFORE_MISSING_VALUES']
- **Required**: Yes

### EndMode
- **Type**: typing.Literal['EXCLUSIVE', 'FIRST', 'INCLUSIVE', 'LAST', 'LAST_BEFORE_MISSING_VALUES']
- **Required**: Yes

### StartValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.TypedAttributeValueUnionTypeDef]

### EndValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.TypedAttributeValueUnionTypeDef]


# TypedAttributeValueTypeDef

### StringValue
- **Type**: typing.Optional[str]

### BinaryValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.BlobTypeDef]

### BooleanValue
- **Type**: typing.Optional[bool]

### NumberValue
- **Type**: typing.Optional[str]

### DatetimeValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.clouddirectory_classes.TimestampTypeDef]


# TypedAttributeValueUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TypedLinkAttributeDefinitionOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TypedLinkAttributeDefinitionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TypedLinkAttributeRangeTypeDef

### Range
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.TypedAttributeValueRangeTypeDef'>
- **Required**: Yes

### AttributeName
- **Type**: typing.Optional[str]


# TypedLinkFacetAttributeUpdateTypeDef

### Attribute
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.TypedLinkAttributeDefinitionUnionTypeDef'>
- **Required**: Yes

### Action
- **Type**: typing.Literal['CREATE_OR_UPDATE', 'DELETE']
- **Required**: Yes


# TypedLinkFacetTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.clouddirectory_classes.TypedLinkAttributeDefinitionUnionTypeDef]
- **Required**: Yes

### IdentityAttributeOrder
- **Type**: typing.Sequence[str]
- **Required**: Yes


# TypedLinkSchemaAndFacetNameTypeDef

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### TypedLinkName
- **Type**: <class 'str'>
- **Required**: Yes


# TypedLinkSpecifierOutputTypeDef

### TypedLinkFacet
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.TypedLinkSchemaAndFacetNameTypeDef'>
- **Required**: Yes

### SourceObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### TargetObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### IdentityAttributeValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.clouddirectory_classes.AttributeNameAndValueOutputTypeDef]
- **Required**: Yes


# TypedLinkSpecifierTypeDef

### TypedLinkFacet
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.TypedLinkSchemaAndFacetNameTypeDef'>
- **Required**: Yes

### SourceObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### TargetObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### IdentityAttributeValues
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.clouddirectory_classes.AttributeNameAndValueUnionTypeDef]
- **Required**: Yes


# TypedLinkSpecifierUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateFacetRequestTypeDef

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeUpdates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.clouddirectory_classes.FacetAttributeUpdateTypeDef]]

### ObjectType
- **Type**: typing.Optional[typing.Literal['INDEX', 'LEAF_NODE', 'NODE', 'POLICY']]


# UpdateLinkAttributesRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### TypedLinkSpecifier
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.TypedLinkSpecifierUnionTypeDef'>
- **Required**: Yes

### AttributeUpdates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.clouddirectory_classes.LinkAttributeUpdateTypeDef]
- **Required**: Yes


# UpdateObjectAttributesRequestTypeDef

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectReference
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectReferenceTypeDef'>
- **Required**: Yes

### AttributeUpdates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.clouddirectory_classes.ObjectAttributeUpdateTypeDef]
- **Required**: Yes


# UpdateObjectAttributesResponseTypeDef

### ObjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSchemaRequestTypeDef

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateSchemaResponseTypeDef

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTypedLinkFacetRequestTypeDef

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeUpdates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.clouddirectory_classes.TypedLinkFacetAttributeUpdateTypeDef]
- **Required**: Yes

### IdentityAttributeOrder
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpgradeAppliedSchemaRequestTypeDef

### PublishedSchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# UpgradeAppliedSchemaResponseTypeDef

### UpgradedSchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### DirectoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpgradePublishedSchemaRequestTypeDef

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


# UpgradePublishedSchemaResponseTypeDef

### UpgradedSchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.clouddirectory_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


