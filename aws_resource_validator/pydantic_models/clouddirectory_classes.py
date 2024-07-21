from datetime import datetime
from pydantic import BaseModel
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.clouddirectory_constants import *

class ObjectReferenceTypeDef(BaseModel):
    Selector: Optional[str] = None

class SchemaFacetTypeDef(BaseModel):
    SchemaArn: Optional[str] = None
    FacetName: Optional[str] = None

class ApplySchemaRequestRequestTypeDef(BaseModel):
    PublishedSchemaArn: str
    DirectoryArn: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class TypedLinkSchemaAndFacetNameTypeDef(BaseModel):
    SchemaArn: str
    TypedLinkName: str

class AttributeKeyTypeDef(BaseModel):
    SchemaArn: str
    FacetName: str
    Name: str

class TypedAttributeValuePaginatorTypeDef(BaseModel):
    StringValue: Optional[str] = None
    BinaryValue: Optional[bytes] = None
    BooleanValue: Optional[bool] = None
    NumberValue: Optional[str] = None
    DatetimeValue: Optional[datetime] = None

class BatchAttachObjectResponseTypeDef(BaseModel):
    attachedObjectIdentifier: Optional[str] = None

class BatchAttachToIndexResponseTypeDef(BaseModel):
    AttachedObjectIdentifier: Optional[str] = None

class BatchCreateIndexResponseTypeDef(BaseModel):
    ObjectIdentifier: Optional[str] = None

class BatchCreateObjectResponseTypeDef(BaseModel):
    ObjectIdentifier: Optional[str] = None

class BatchDetachFromIndexResponseTypeDef(BaseModel):
    DetachedObjectIdentifier: Optional[str] = None

class BatchDetachObjectResponseTypeDef(BaseModel):
    detachedObjectIdentifier: Optional[str] = None

class BatchListObjectChildrenResponseTypeDef(BaseModel):
    Children: Optional[Dict[str, str]] = None
    NextToken: Optional[str] = None

class PathToObjectIdentifiersTypeDef(BaseModel):
    Path: Optional[str] = None
    ObjectIdentifiers: Optional[List[str]] = None

class ObjectIdentifierAndLinkNameTupleTypeDef(BaseModel):
    ObjectIdentifier: Optional[str] = None
    LinkName: Optional[str] = None

class BatchListObjectPoliciesResponseTypeDef(BaseModel):
    AttachedPolicyIds: Optional[List[str]] = None
    NextToken: Optional[str] = None

class BatchListPolicyAttachmentsResponseTypeDef(BaseModel):
    ObjectIdentifiers: Optional[List[str]] = None
    NextToken: Optional[str] = None

class BatchReadExceptionTypeDef(BaseModel):
    Type: Optional[BatchReadExceptionTypeType] = None
    Message: Optional[str] = None

class BatchUpdateObjectAttributesResponseTypeDef(BaseModel):
    ObjectIdentifier: Optional[str] = None

class CreateDirectoryRequestRequestTypeDef(BaseModel):
    Name: str
    SchemaArn: str

class CreateSchemaRequestRequestTypeDef(BaseModel):
    Name: str

class DeleteDirectoryRequestRequestTypeDef(BaseModel):
    DirectoryArn: str

class DeleteFacetRequestRequestTypeDef(BaseModel):
    SchemaArn: str
    Name: str

class DeleteSchemaRequestRequestTypeDef(BaseModel):
    SchemaArn: str

class DeleteTypedLinkFacetRequestRequestTypeDef(BaseModel):
    SchemaArn: str
    Name: str

class DirectoryTypeDef(BaseModel):
    Name: Optional[str] = None
    DirectoryArn: Optional[str] = None
    State: Optional[DirectoryStateType] = None
    CreationDateTime: Optional[datetime] = None

class DisableDirectoryRequestRequestTypeDef(BaseModel):
    DirectoryArn: str

class EnableDirectoryRequestRequestTypeDef(BaseModel):
    DirectoryArn: str

class RulePaginatorTypeDef(BaseModel):
    Type: Optional[RuleTypeType] = None
    Parameters: Optional[Dict[str, str]] = None

class RuleTypeDef(BaseModel):
    Type: Optional[RuleTypeType] = None
    Parameters: Optional[Mapping[str, str]] = None

class FacetAttributeReferenceTypeDef(BaseModel):
    TargetFacetName: str
    TargetAttributeName: str

class FacetTypeDef(BaseModel):
    Name: Optional[str] = None
    ObjectType: Optional[ObjectTypeType] = None
    FacetStyle: Optional[FacetStyleType] = None

class GetAppliedSchemaVersionRequestRequestTypeDef(BaseModel):
    SchemaArn: str

class GetDirectoryRequestRequestTypeDef(BaseModel):
    DirectoryArn: str

class GetFacetRequestRequestTypeDef(BaseModel):
    SchemaArn: str
    Name: str

class GetSchemaAsJsonRequestRequestTypeDef(BaseModel):
    SchemaArn: str

class GetTypedLinkFacetInformationRequestRequestTypeDef(BaseModel):
    SchemaArn: str
    Name: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAppliedSchemaArnsRequestRequestTypeDef(BaseModel):
    DirectoryArn: str
    SchemaArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDevelopmentSchemaArnsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDirectoriesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    state: Optional[DirectoryStateType] = None

class ListFacetAttributesRequestRequestTypeDef(BaseModel):
    SchemaArn: str
    Name: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListFacetNamesRequestRequestTypeDef(BaseModel):
    SchemaArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListManagedSchemaArnsRequestRequestTypeDef(BaseModel):
    SchemaArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListPublishedSchemaArnsRequestRequestTypeDef(BaseModel):
    SchemaArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class TagTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class ListTypedLinkFacetAttributesRequestRequestTypeDef(BaseModel):
    SchemaArn: str
    Name: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTypedLinkFacetNamesRequestRequestTypeDef(BaseModel):
    SchemaArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PolicyAttachmentTypeDef(BaseModel):
    PolicyId: Optional[str] = None
    ObjectIdentifier: Optional[str] = None
    PolicyType: Optional[str] = None

class PublishSchemaRequestRequestTypeDef(BaseModel):
    DevelopmentSchemaArn: str
    Version: str
    MinorVersion: Optional[str] = None
    Name: Optional[str] = None

class PutSchemaFromJsonRequestRequestTypeDef(BaseModel):
    SchemaArn: str
    Document: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateSchemaRequestRequestTypeDef(BaseModel):
    SchemaArn: str
    Name: str

class UpgradeAppliedSchemaRequestRequestTypeDef(BaseModel):
    PublishedSchemaArn: str
    DirectoryArn: str
    DryRun: Optional[bool] = None

class UpgradePublishedSchemaRequestRequestTypeDef(BaseModel):
    DevelopmentSchemaArn: str
    PublishedSchemaArn: str
    MinorVersion: str
    DryRun: Optional[bool] = None

class AttachObjectRequestRequestTypeDef(BaseModel):
    DirectoryArn: str
    ParentReference: ObjectReferenceTypeDef
    ChildReference: ObjectReferenceTypeDef
    LinkName: str

class AttachPolicyRequestRequestTypeDef(BaseModel):
    DirectoryArn: str
    PolicyReference: ObjectReferenceTypeDef
    ObjectReference: ObjectReferenceTypeDef

class AttachToIndexRequestRequestTypeDef(BaseModel):
    DirectoryArn: str
    IndexReference: ObjectReferenceTypeDef
    TargetReference: ObjectReferenceTypeDef

class BatchAttachObjectTypeDef(BaseModel):
    ParentReference: ObjectReferenceTypeDef
    ChildReference: ObjectReferenceTypeDef
    LinkName: str

class BatchAttachPolicyTypeDef(BaseModel):
    PolicyReference: ObjectReferenceTypeDef
    ObjectReference: ObjectReferenceTypeDef

class BatchAttachToIndexTypeDef(BaseModel):
    IndexReference: ObjectReferenceTypeDef
    TargetReference: ObjectReferenceTypeDef

class BatchDeleteObjectTypeDef(BaseModel):
    ObjectReference: ObjectReferenceTypeDef

class BatchDetachFromIndexTypeDef(BaseModel):
    IndexReference: ObjectReferenceTypeDef
    TargetReference: ObjectReferenceTypeDef

class BatchDetachObjectTypeDef(BaseModel):
    ParentReference: ObjectReferenceTypeDef
    LinkName: str
    BatchReferenceName: Optional[str] = None

class BatchDetachPolicyTypeDef(BaseModel):
    PolicyReference: ObjectReferenceTypeDef
    ObjectReference: ObjectReferenceTypeDef

class BatchGetObjectInformationTypeDef(BaseModel):
    ObjectReference: ObjectReferenceTypeDef

class BatchListAttachedIndicesTypeDef(BaseModel):
    TargetReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class BatchListObjectChildrenTypeDef(BaseModel):
    ObjectReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class BatchListObjectParentPathsTypeDef(BaseModel):
    ObjectReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class BatchListObjectParentsTypeDef(BaseModel):
    ObjectReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class BatchListObjectPoliciesTypeDef(BaseModel):
    ObjectReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class BatchListPolicyAttachmentsTypeDef(BaseModel):
    PolicyReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class BatchLookupPolicyTypeDef(BaseModel):
    ObjectReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DeleteObjectRequestRequestTypeDef(BaseModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef

class DetachFromIndexRequestRequestTypeDef(BaseModel):
    DirectoryArn: str
    IndexReference: ObjectReferenceTypeDef
    TargetReference: ObjectReferenceTypeDef

class DetachObjectRequestRequestTypeDef(BaseModel):
    DirectoryArn: str
    ParentReference: ObjectReferenceTypeDef
    LinkName: str

class DetachPolicyRequestRequestTypeDef(BaseModel):
    DirectoryArn: str
    PolicyReference: ObjectReferenceTypeDef
    ObjectReference: ObjectReferenceTypeDef

class GetObjectInformationRequestRequestTypeDef(BaseModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    ConsistencyLevel: Optional[ConsistencyLevelType] = None

class ListAttachedIndicesRequestRequestTypeDef(BaseModel):
    DirectoryArn: str
    TargetReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None

class ListObjectChildrenRequestRequestTypeDef(BaseModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None

class ListObjectParentPathsRequestRequestTypeDef(BaseModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListObjectParentsRequestRequestTypeDef(BaseModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    IncludeAllLinksToEachParent: Optional[bool] = None

class ListObjectPoliciesRequestRequestTypeDef(BaseModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None

class ListPolicyAttachmentsRequestRequestTypeDef(BaseModel):
    DirectoryArn: str
    PolicyReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None

class LookupPolicyRequestRequestTypeDef(BaseModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class BatchGetObjectAttributesTypeDef(BaseModel):
    ObjectReference: ObjectReferenceTypeDef
    SchemaFacet: SchemaFacetTypeDef
    AttributeNames: Sequence[str]

class BatchGetObjectInformationResponseTypeDef(BaseModel):
    SchemaFacets: Optional[List[SchemaFacetTypeDef]] = None
    ObjectIdentifier: Optional[str] = None

class BatchListObjectAttributesTypeDef(BaseModel):
    ObjectReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    FacetFilter: Optional[SchemaFacetTypeDef] = None

class BatchRemoveFacetFromObjectTypeDef(BaseModel):
    SchemaFacet: SchemaFacetTypeDef
    ObjectReference: ObjectReferenceTypeDef

class GetObjectAttributesRequestRequestTypeDef(BaseModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    SchemaFacet: SchemaFacetTypeDef
    AttributeNames: Sequence[str]
    ConsistencyLevel: Optional[ConsistencyLevelType] = None

class ListObjectAttributesRequestRequestTypeDef(BaseModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    FacetFilter: Optional[SchemaFacetTypeDef] = None

class RemoveFacetFromObjectRequestRequestTypeDef(BaseModel):
    DirectoryArn: str
    SchemaFacet: SchemaFacetTypeDef
    ObjectReference: ObjectReferenceTypeDef

class ApplySchemaResponseTypeDef(BaseModel):
    AppliedSchemaArn: str
    DirectoryArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AttachObjectResponseTypeDef(BaseModel):
    AttachedObjectIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class AttachToIndexResponseTypeDef(BaseModel):
    AttachedObjectIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDirectoryResponseTypeDef(BaseModel):
    DirectoryArn: str
    Name: str
    ObjectIdentifier: str
    AppliedSchemaArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIndexResponseTypeDef(BaseModel):
    ObjectIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateObjectResponseTypeDef(BaseModel):
    ObjectIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSchemaResponseTypeDef(BaseModel):
    SchemaArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDirectoryResponseTypeDef(BaseModel):
    DirectoryArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSchemaResponseTypeDef(BaseModel):
    SchemaArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DetachFromIndexResponseTypeDef(BaseModel):
    DetachedObjectIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class DetachObjectResponseTypeDef(BaseModel):
    DetachedObjectIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisableDirectoryResponseTypeDef(BaseModel):
    DirectoryArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class EnableDirectoryResponseTypeDef(BaseModel):
    DirectoryArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAppliedSchemaVersionResponseTypeDef(BaseModel):
    AppliedSchemaArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetObjectInformationResponseTypeDef(BaseModel):
    SchemaFacets: List[SchemaFacetTypeDef]
    ObjectIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSchemaAsJsonResponseTypeDef(BaseModel):
    Name: str
    Document: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTypedLinkFacetInformationResponseTypeDef(BaseModel):
    IdentityAttributeOrder: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppliedSchemaArnsResponseTypeDef(BaseModel):
    SchemaArns: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDevelopmentSchemaArnsResponseTypeDef(BaseModel):
    SchemaArns: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFacetNamesResponseTypeDef(BaseModel):
    FacetNames: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListManagedSchemaArnsResponseTypeDef(BaseModel):
    SchemaArns: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListObjectChildrenResponseTypeDef(BaseModel):
    Children: Dict[str, str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListObjectPoliciesResponseTypeDef(BaseModel):
    AttachedPolicyIds: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPolicyAttachmentsResponseTypeDef(BaseModel):
    ObjectIdentifiers: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPublishedSchemaArnsResponseTypeDef(BaseModel):
    SchemaArns: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTypedLinkFacetNamesResponseTypeDef(BaseModel):
    FacetNames: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PublishSchemaResponseTypeDef(BaseModel):
    PublishedSchemaArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutSchemaFromJsonResponseTypeDef(BaseModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateObjectAttributesResponseTypeDef(BaseModel):
    ObjectIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSchemaResponseTypeDef(BaseModel):
    SchemaArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpgradeAppliedSchemaResponseTypeDef(BaseModel):
    UpgradedSchemaArn: str
    DirectoryArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpgradePublishedSchemaResponseTypeDef(BaseModel):
    UpgradedSchemaArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchCreateIndexTypeDef(BaseModel):
    OrderedIndexedAttributeList: Sequence[AttributeKeyTypeDef]
    IsUnique: bool
    ParentReference: Optional[ObjectReferenceTypeDef] = None
    LinkName: Optional[str] = None
    BatchReferenceName: Optional[str] = None

class CreateIndexRequestRequestTypeDef(BaseModel):
    DirectoryArn: str
    OrderedIndexedAttributeList: Sequence[AttributeKeyTypeDef]
    IsUnique: bool
    ParentReference: Optional[ObjectReferenceTypeDef] = None
    LinkName: Optional[str] = None

class AttributeKeyAndValuePaginatorTypeDef(BaseModel):
    Key: AttributeKeyTypeDef
    Value: TypedAttributeValuePaginatorTypeDef

class AttributeNameAndValuePaginatorTypeDef(BaseModel):
    AttributeName: str
    Value: TypedAttributeValuePaginatorTypeDef

class TypedAttributeValueRangePaginatorTypeDef(BaseModel):
    StartMode: RangeModeType
    EndMode: RangeModeType
    StartValue: Optional[TypedAttributeValuePaginatorTypeDef] = None
    EndValue: Optional[TypedAttributeValuePaginatorTypeDef] = None

class BatchListObjectParentPathsResponseTypeDef(BaseModel):
    PathToObjectIdentifiersList: Optional[List[PathToObjectIdentifiersTypeDef]] = None
    NextToken: Optional[str] = None

class ListObjectParentPathsResponseTypeDef(BaseModel):
    PathToObjectIdentifiersList: List[PathToObjectIdentifiersTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchListObjectParentsResponseTypeDef(BaseModel):
    ParentLinks: Optional[List[ObjectIdentifierAndLinkNameTupleTypeDef]] = None
    NextToken: Optional[str] = None

class ListObjectParentsResponseTypeDef(BaseModel):
    Parents: Dict[str, str]
    NextToken: str
    ParentLinks: List[ObjectIdentifierAndLinkNameTupleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDirectoryResponseTypeDef(BaseModel):
    Directory: DirectoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDirectoriesResponseTypeDef(BaseModel):
    Directories: List[DirectoryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class FacetAttributeDefinitionPaginatorTypeDef(BaseModel):
    Type: FacetAttributeTypeType
    DefaultValue: Optional[TypedAttributeValuePaginatorTypeDef] = None
    IsImmutable: Optional[bool] = None
    Rules: Optional[Dict[str, RulePaginatorTypeDef]] = None

class TypedLinkAttributeDefinitionPaginatorTypeDef(BaseModel):
    Name: str
    Type: FacetAttributeTypeType
    RequiredBehavior: RequiredAttributeBehaviorType
    DefaultValue: Optional[TypedAttributeValuePaginatorTypeDef] = None
    IsImmutable: Optional[bool] = None
    Rules: Optional[Dict[str, RulePaginatorTypeDef]] = None

class GetFacetResponseTypeDef(BaseModel):
    Facet: FacetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppliedSchemaArnsRequestListAppliedSchemaArnsPaginateTypeDef(BaseModel):
    DirectoryArn: str
    SchemaArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAttachedIndicesRequestListAttachedIndicesPaginateTypeDef(BaseModel):
    DirectoryArn: str
    TargetReference: ObjectReferenceTypeDef
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDevelopmentSchemaArnsRequestListDevelopmentSchemaArnsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDirectoriesRequestListDirectoriesPaginateTypeDef(BaseModel):
    state: Optional[DirectoryStateType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFacetAttributesRequestListFacetAttributesPaginateTypeDef(BaseModel):
    SchemaArn: str
    Name: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFacetNamesRequestListFacetNamesPaginateTypeDef(BaseModel):
    SchemaArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListManagedSchemaArnsRequestListManagedSchemaArnsPaginateTypeDef(BaseModel):
    SchemaArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListObjectAttributesRequestListObjectAttributesPaginateTypeDef(BaseModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    FacetFilter: Optional[SchemaFacetTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListObjectParentPathsRequestListObjectParentPathsPaginateTypeDef(BaseModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListObjectPoliciesRequestListObjectPoliciesPaginateTypeDef(BaseModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPolicyAttachmentsRequestListPolicyAttachmentsPaginateTypeDef(BaseModel):
    DirectoryArn: str
    PolicyReference: ObjectReferenceTypeDef
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPublishedSchemaArnsRequestListPublishedSchemaArnsPaginateTypeDef(BaseModel):
    SchemaArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(BaseModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTypedLinkFacetAttributesRequestListTypedLinkFacetAttributesPaginateTypeDef(BaseModel):
    SchemaArn: str
    Name: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTypedLinkFacetNamesRequestListTypedLinkFacetNamesPaginateTypeDef(BaseModel):
    SchemaArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class LookupPolicyRequestLookupPolicyPaginateTypeDef(BaseModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class PolicyToPathTypeDef(BaseModel):
    Path: Optional[str] = None
    Policies: Optional[List[PolicyAttachmentTypeDef]] = None

class TypedAttributeValueTypeDef(BaseModel):
    StringValue: Optional[str] = None
    BinaryValue: Optional[BlobTypeDef] = None
    BooleanValue: Optional[bool] = None
    NumberValue: Optional[str] = None
    DatetimeValue: Optional[TimestampTypeDef] = None

class IndexAttachmentPaginatorTypeDef(BaseModel):
    IndexedAttributes: Optional[List[AttributeKeyAndValuePaginatorTypeDef]] = None
    ObjectIdentifier: Optional[str] = None

class ListObjectAttributesResponsePaginatorTypeDef(BaseModel):
    Attributes: List[AttributeKeyAndValuePaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TypedLinkSpecifierPaginatorTypeDef(BaseModel):
    TypedLinkFacet: TypedLinkSchemaAndFacetNameTypeDef
    SourceObjectReference: ObjectReferenceTypeDef
    TargetObjectReference: ObjectReferenceTypeDef
    IdentityAttributeValues: List[AttributeNameAndValuePaginatorTypeDef]

class ObjectAttributeRangePaginatorTypeDef(BaseModel):
    AttributeKey: Optional[AttributeKeyTypeDef] = None
    Range: Optional[TypedAttributeValueRangePaginatorTypeDef] = None

class TypedLinkAttributeRangePaginatorTypeDef(BaseModel):
    Range: TypedAttributeValueRangePaginatorTypeDef
    AttributeName: Optional[str] = None

class FacetAttributePaginatorTypeDef(BaseModel):
    Name: str
    AttributeDefinition: Optional[FacetAttributeDefinitionPaginatorTypeDef] = None
    AttributeReference: Optional[FacetAttributeReferenceTypeDef] = None
    RequiredBehavior: Optional[RequiredAttributeBehaviorType] = None

class ListTypedLinkFacetAttributesResponsePaginatorTypeDef(BaseModel):
    Attributes: List[TypedLinkAttributeDefinitionPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchLookupPolicyResponseTypeDef(BaseModel):
    PolicyToPathList: Optional[List[PolicyToPathTypeDef]] = None
    NextToken: Optional[str] = None

class LookupPolicyResponseTypeDef(BaseModel):
    PolicyToPathList: List[PolicyToPathTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AttributeKeyAndValueTypeDef(BaseModel):
    Key: AttributeKeyTypeDef
    Value: TypedAttributeValueTypeDef

class AttributeNameAndValueTypeDef(BaseModel):
    AttributeName: str
    Value: TypedAttributeValueTypeDef

class FacetAttributeDefinitionTypeDef(BaseModel):
    Type: FacetAttributeTypeType
    DefaultValue: Optional[TypedAttributeValueTypeDef] = None
    IsImmutable: Optional[bool] = None
    Rules: Optional[Mapping[str, RuleTypeDef]] = None

class LinkAttributeActionTypeDef(BaseModel):
    AttributeActionType: Optional[UpdateActionTypeType] = None
    AttributeUpdateValue: Optional[TypedAttributeValueTypeDef] = None

class ObjectAttributeActionTypeDef(BaseModel):
    ObjectAttributeActionType: Optional[UpdateActionTypeType] = None
    ObjectAttributeUpdateValue: Optional[TypedAttributeValueTypeDef] = None

class TypedAttributeValueRangeTypeDef(BaseModel):
    StartMode: RangeModeType
    EndMode: RangeModeType
    StartValue: Optional[TypedAttributeValueTypeDef] = None
    EndValue: Optional[TypedAttributeValueTypeDef] = None

class TypedLinkAttributeDefinitionTypeDef(BaseModel):
    Name: str
    Type: FacetAttributeTypeType
    RequiredBehavior: RequiredAttributeBehaviorType
    DefaultValue: Optional[TypedAttributeValueTypeDef] = None
    IsImmutable: Optional[bool] = None
    Rules: Optional[Mapping[str, RuleTypeDef]] = None

class ListAttachedIndicesResponsePaginatorTypeDef(BaseModel):
    IndexAttachments: List[IndexAttachmentPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListIndexResponsePaginatorTypeDef(BaseModel):
    IndexAttachments: List[IndexAttachmentPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListIncomingTypedLinksResponsePaginatorTypeDef(BaseModel):
    LinkSpecifiers: List[TypedLinkSpecifierPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListOutgoingTypedLinksResponsePaginatorTypeDef(BaseModel):
    TypedLinkSpecifiers: List[TypedLinkSpecifierPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListIndexRequestListIndexPaginateTypeDef(BaseModel):
    DirectoryArn: str
    IndexReference: ObjectReferenceTypeDef
    RangesOnIndexedValues: Optional[Sequence[ObjectAttributeRangePaginatorTypeDef]] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIncomingTypedLinksRequestListIncomingTypedLinksPaginateTypeDef(BaseModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    FilterAttributeRanges: Optional[Sequence[TypedLinkAttributeRangePaginatorTypeDef]] = None
    FilterTypedLink: Optional[TypedLinkSchemaAndFacetNameTypeDef] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOutgoingTypedLinksRequestListOutgoingTypedLinksPaginateTypeDef(BaseModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    FilterAttributeRanges: Optional[Sequence[TypedLinkAttributeRangePaginatorTypeDef]] = None
    FilterTypedLink: Optional[TypedLinkSchemaAndFacetNameTypeDef] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFacetAttributesResponsePaginatorTypeDef(BaseModel):
    Attributes: List[FacetAttributePaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AddFacetToObjectRequestRequestTypeDef(BaseModel):
    DirectoryArn: str
    SchemaFacet: SchemaFacetTypeDef
    ObjectReference: ObjectReferenceTypeDef
    ObjectAttributeList: Optional[Sequence[AttributeKeyAndValueTypeDef]] = None

class BatchAddFacetToObjectTypeDef(BaseModel):
    SchemaFacet: SchemaFacetTypeDef
    ObjectAttributeList: Sequence[AttributeKeyAndValueTypeDef]
    ObjectReference: ObjectReferenceTypeDef

class BatchCreateObjectTypeDef(BaseModel):
    SchemaFacet: Sequence[SchemaFacetTypeDef]
    ObjectAttributeList: Sequence[AttributeKeyAndValueTypeDef]
    ParentReference: Optional[ObjectReferenceTypeDef] = None
    LinkName: Optional[str] = None
    BatchReferenceName: Optional[str] = None

class BatchGetLinkAttributesResponseTypeDef(BaseModel):
    Attributes: Optional[List[AttributeKeyAndValueTypeDef]] = None

class BatchGetObjectAttributesResponseTypeDef(BaseModel):
    Attributes: Optional[List[AttributeKeyAndValueTypeDef]] = None

class BatchListObjectAttributesResponseTypeDef(BaseModel):
    Attributes: Optional[List[AttributeKeyAndValueTypeDef]] = None
    NextToken: Optional[str] = None

class CreateObjectRequestRequestTypeDef(BaseModel):
    DirectoryArn: str
    SchemaFacets: Sequence[SchemaFacetTypeDef]
    ObjectAttributeList: Optional[Sequence[AttributeKeyAndValueTypeDef]] = None
    ParentReference: Optional[ObjectReferenceTypeDef] = None
    LinkName: Optional[str] = None

class GetLinkAttributesResponseTypeDef(BaseModel):
    Attributes: List[AttributeKeyAndValueTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetObjectAttributesResponseTypeDef(BaseModel):
    Attributes: List[AttributeKeyAndValueTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class IndexAttachmentTypeDef(BaseModel):
    IndexedAttributes: Optional[List[AttributeKeyAndValueTypeDef]] = None
    ObjectIdentifier: Optional[str] = None

class ListObjectAttributesResponseTypeDef(BaseModel):
    Attributes: List[AttributeKeyAndValueTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AttachTypedLinkRequestRequestTypeDef(BaseModel):
    DirectoryArn: str
    SourceObjectReference: ObjectReferenceTypeDef
    TargetObjectReference: ObjectReferenceTypeDef
    TypedLinkFacet: TypedLinkSchemaAndFacetNameTypeDef
    Attributes: Sequence[AttributeNameAndValueTypeDef]

class BatchAttachTypedLinkTypeDef(BaseModel):
    SourceObjectReference: ObjectReferenceTypeDef
    TargetObjectReference: ObjectReferenceTypeDef
    TypedLinkFacet: TypedLinkSchemaAndFacetNameTypeDef
    Attributes: Sequence[AttributeNameAndValueTypeDef]

class TypedLinkSpecifierTypeDef(BaseModel):
    TypedLinkFacet: TypedLinkSchemaAndFacetNameTypeDef
    SourceObjectReference: ObjectReferenceTypeDef
    TargetObjectReference: ObjectReferenceTypeDef
    IdentityAttributeValues: List[AttributeNameAndValueTypeDef]

class FacetAttributeTypeDef(BaseModel):
    Name: str
    AttributeDefinition: Optional[FacetAttributeDefinitionTypeDef] = None
    AttributeReference: Optional[FacetAttributeReferenceTypeDef] = None
    RequiredBehavior: Optional[RequiredAttributeBehaviorType] = None

class LinkAttributeUpdateTypeDef(BaseModel):
    AttributeKey: Optional[AttributeKeyTypeDef] = None
    AttributeAction: Optional[LinkAttributeActionTypeDef] = None

class ObjectAttributeUpdateTypeDef(BaseModel):
    ObjectAttributeKey: Optional[AttributeKeyTypeDef] = None
    ObjectAttributeAction: Optional[ObjectAttributeActionTypeDef] = None

class ObjectAttributeRangeTypeDef(BaseModel):
    AttributeKey: Optional[AttributeKeyTypeDef] = None
    Range: Optional[TypedAttributeValueRangeTypeDef] = None

class TypedLinkAttributeRangeTypeDef(BaseModel):
    Range: TypedAttributeValueRangeTypeDef
    AttributeName: Optional[str] = None

class ListTypedLinkFacetAttributesResponseTypeDef(BaseModel):
    Attributes: List[TypedLinkAttributeDefinitionTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TypedLinkFacetAttributeUpdateTypeDef(BaseModel):
    Attribute: TypedLinkAttributeDefinitionTypeDef
    Action: UpdateActionTypeType

class TypedLinkFacetTypeDef(BaseModel):
    Name: str
    Attributes: Sequence[TypedLinkAttributeDefinitionTypeDef]
    IdentityAttributeOrder: Sequence[str]

class BatchListAttachedIndicesResponseTypeDef(BaseModel):
    IndexAttachments: Optional[List[IndexAttachmentTypeDef]] = None
    NextToken: Optional[str] = None

class BatchListIndexResponseTypeDef(BaseModel):
    IndexAttachments: Optional[List[IndexAttachmentTypeDef]] = None
    NextToken: Optional[str] = None

class ListAttachedIndicesResponseTypeDef(BaseModel):
    IndexAttachments: List[IndexAttachmentTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListIndexResponseTypeDef(BaseModel):
    IndexAttachments: List[IndexAttachmentTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AttachTypedLinkResponseTypeDef(BaseModel):
    TypedLinkSpecifier: TypedLinkSpecifierTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchAttachTypedLinkResponseTypeDef(BaseModel):
    TypedLinkSpecifier: Optional[TypedLinkSpecifierTypeDef] = None

class BatchDetachTypedLinkTypeDef(BaseModel):
    TypedLinkSpecifier: TypedLinkSpecifierTypeDef

class BatchGetLinkAttributesTypeDef(BaseModel):
    TypedLinkSpecifier: TypedLinkSpecifierTypeDef
    AttributeNames: Sequence[str]

class BatchListIncomingTypedLinksResponseTypeDef(BaseModel):
    LinkSpecifiers: Optional[List[TypedLinkSpecifierTypeDef]] = None
    NextToken: Optional[str] = None

class BatchListOutgoingTypedLinksResponseTypeDef(BaseModel):
    TypedLinkSpecifiers: Optional[List[TypedLinkSpecifierTypeDef]] = None
    NextToken: Optional[str] = None

class DetachTypedLinkRequestRequestTypeDef(BaseModel):
    DirectoryArn: str
    TypedLinkSpecifier: TypedLinkSpecifierTypeDef

class GetLinkAttributesRequestRequestTypeDef(BaseModel):
    DirectoryArn: str
    TypedLinkSpecifier: TypedLinkSpecifierTypeDef
    AttributeNames: Sequence[str]
    ConsistencyLevel: Optional[ConsistencyLevelType] = None

class ListIncomingTypedLinksResponseTypeDef(BaseModel):
    LinkSpecifiers: List[TypedLinkSpecifierTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListOutgoingTypedLinksResponseTypeDef(BaseModel):
    TypedLinkSpecifiers: List[TypedLinkSpecifierTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFacetRequestRequestTypeDef(BaseModel):
    SchemaArn: str
    Name: str
    Attributes: Optional[Sequence[FacetAttributeTypeDef]] = None
    ObjectType: Optional[ObjectTypeType] = None
    FacetStyle: Optional[FacetStyleType] = None

class FacetAttributeUpdateTypeDef(BaseModel):
    Attribute: Optional[FacetAttributeTypeDef] = None
    Action: Optional[UpdateActionTypeType] = None

class ListFacetAttributesResponseTypeDef(BaseModel):
    Attributes: List[FacetAttributeTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateLinkAttributesTypeDef(BaseModel):
    TypedLinkSpecifier: TypedLinkSpecifierTypeDef
    AttributeUpdates: Sequence[LinkAttributeUpdateTypeDef]

class UpdateLinkAttributesRequestRequestTypeDef(BaseModel):
    DirectoryArn: str
    TypedLinkSpecifier: TypedLinkSpecifierTypeDef
    AttributeUpdates: Sequence[LinkAttributeUpdateTypeDef]

class BatchUpdateObjectAttributesTypeDef(BaseModel):
    ObjectReference: ObjectReferenceTypeDef
    AttributeUpdates: Sequence[ObjectAttributeUpdateTypeDef]

class UpdateObjectAttributesRequestRequestTypeDef(BaseModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    AttributeUpdates: Sequence[ObjectAttributeUpdateTypeDef]

class BatchListIndexTypeDef(BaseModel):
    IndexReference: ObjectReferenceTypeDef
    RangesOnIndexedValues: Optional[Sequence[ObjectAttributeRangeTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListIndexRequestRequestTypeDef(BaseModel):
    DirectoryArn: str
    IndexReference: ObjectReferenceTypeDef
    RangesOnIndexedValues: Optional[Sequence[ObjectAttributeRangeTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None

class BatchListIncomingTypedLinksTypeDef(BaseModel):
    ObjectReference: ObjectReferenceTypeDef
    FilterAttributeRanges: Optional[Sequence[TypedLinkAttributeRangeTypeDef]] = None
    FilterTypedLink: Optional[TypedLinkSchemaAndFacetNameTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class BatchListOutgoingTypedLinksTypeDef(BaseModel):
    ObjectReference: ObjectReferenceTypeDef
    FilterAttributeRanges: Optional[Sequence[TypedLinkAttributeRangeTypeDef]] = None
    FilterTypedLink: Optional[TypedLinkSchemaAndFacetNameTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListIncomingTypedLinksRequestRequestTypeDef(BaseModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    FilterAttributeRanges: Optional[Sequence[TypedLinkAttributeRangeTypeDef]] = None
    FilterTypedLink: Optional[TypedLinkSchemaAndFacetNameTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None

class ListOutgoingTypedLinksRequestRequestTypeDef(BaseModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    FilterAttributeRanges: Optional[Sequence[TypedLinkAttributeRangeTypeDef]] = None
    FilterTypedLink: Optional[TypedLinkSchemaAndFacetNameTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None

class UpdateTypedLinkFacetRequestRequestTypeDef(BaseModel):
    SchemaArn: str
    Name: str
    AttributeUpdates: Sequence[TypedLinkFacetAttributeUpdateTypeDef]
    IdentityAttributeOrder: Sequence[str]

class CreateTypedLinkFacetRequestRequestTypeDef(BaseModel):
    SchemaArn: str
    Facet: TypedLinkFacetTypeDef

class BatchWriteOperationResponseTypeDef(BaseModel):
    CreateObject: Optional[BatchCreateObjectResponseTypeDef] = None
    AttachObject: Optional[BatchAttachObjectResponseTypeDef] = None
    DetachObject: Optional[BatchDetachObjectResponseTypeDef] = None
    UpdateObjectAttributes: Optional[BatchUpdateObjectAttributesResponseTypeDef] = None
    DeleteObject: Optional[Dict[str, Any]] = None
    AddFacetToObject: Optional[Dict[str, Any]] = None
    RemoveFacetFromObject: Optional[Dict[str, Any]] = None
    AttachPolicy: Optional[Dict[str, Any]] = None
    DetachPolicy: Optional[Dict[str, Any]] = None
    CreateIndex: Optional[BatchCreateIndexResponseTypeDef] = None
    AttachToIndex: Optional[BatchAttachToIndexResponseTypeDef] = None
    DetachFromIndex: Optional[BatchDetachFromIndexResponseTypeDef] = None
    AttachTypedLink: Optional[BatchAttachTypedLinkResponseTypeDef] = None
    DetachTypedLink: Optional[Dict[str, Any]] = None
    UpdateLinkAttributes: Optional[Dict[str, Any]] = None

class BatchReadSuccessfulResponseTypeDef(BaseModel):
    ListObjectAttributes: Optional[BatchListObjectAttributesResponseTypeDef] = None
    ListObjectChildren: Optional[BatchListObjectChildrenResponseTypeDef] = None
    GetObjectInformation: Optional[BatchGetObjectInformationResponseTypeDef] = None
    GetObjectAttributes: Optional[BatchGetObjectAttributesResponseTypeDef] = None
    ListAttachedIndices: Optional[BatchListAttachedIndicesResponseTypeDef] = None
    ListObjectParentPaths: Optional[BatchListObjectParentPathsResponseTypeDef] = None
    ListObjectPolicies: Optional[BatchListObjectPoliciesResponseTypeDef] = None
    ListPolicyAttachments: Optional[BatchListPolicyAttachmentsResponseTypeDef] = None
    LookupPolicy: Optional[BatchLookupPolicyResponseTypeDef] = None
    ListIndex: Optional[BatchListIndexResponseTypeDef] = None
    ListOutgoingTypedLinks: Optional[BatchListOutgoingTypedLinksResponseTypeDef] = None
    ListIncomingTypedLinks: Optional[BatchListIncomingTypedLinksResponseTypeDef] = None
    GetLinkAttributes: Optional[BatchGetLinkAttributesResponseTypeDef] = None
    ListObjectParents: Optional[BatchListObjectParentsResponseTypeDef] = None

class UpdateFacetRequestRequestTypeDef(BaseModel):
    SchemaArn: str
    Name: str
    AttributeUpdates: Optional[Sequence[FacetAttributeUpdateTypeDef]] = None
    ObjectType: Optional[ObjectTypeType] = None

class BatchWriteOperationTypeDef(BaseModel):
    CreateObject: Optional[BatchCreateObjectTypeDef] = None
    AttachObject: Optional[BatchAttachObjectTypeDef] = None
    DetachObject: Optional[BatchDetachObjectTypeDef] = None
    UpdateObjectAttributes: Optional[BatchUpdateObjectAttributesTypeDef] = None
    DeleteObject: Optional[BatchDeleteObjectTypeDef] = None
    AddFacetToObject: Optional[BatchAddFacetToObjectTypeDef] = None
    RemoveFacetFromObject: Optional[BatchRemoveFacetFromObjectTypeDef] = None
    AttachPolicy: Optional[BatchAttachPolicyTypeDef] = None
    DetachPolicy: Optional[BatchDetachPolicyTypeDef] = None
    CreateIndex: Optional[BatchCreateIndexTypeDef] = None
    AttachToIndex: Optional[BatchAttachToIndexTypeDef] = None
    DetachFromIndex: Optional[BatchDetachFromIndexTypeDef] = None
    AttachTypedLink: Optional[BatchAttachTypedLinkTypeDef] = None
    DetachTypedLink: Optional[BatchDetachTypedLinkTypeDef] = None
    UpdateLinkAttributes: Optional[BatchUpdateLinkAttributesTypeDef] = None

class BatchReadOperationTypeDef(BaseModel):
    ListObjectAttributes: Optional[BatchListObjectAttributesTypeDef] = None
    ListObjectChildren: Optional[BatchListObjectChildrenTypeDef] = None
    ListAttachedIndices: Optional[BatchListAttachedIndicesTypeDef] = None
    ListObjectParentPaths: Optional[BatchListObjectParentPathsTypeDef] = None
    GetObjectInformation: Optional[BatchGetObjectInformationTypeDef] = None
    GetObjectAttributes: Optional[BatchGetObjectAttributesTypeDef] = None
    ListObjectParents: Optional[BatchListObjectParentsTypeDef] = None
    ListObjectPolicies: Optional[BatchListObjectPoliciesTypeDef] = None
    ListPolicyAttachments: Optional[BatchListPolicyAttachmentsTypeDef] = None
    LookupPolicy: Optional[BatchLookupPolicyTypeDef] = None
    ListIndex: Optional[BatchListIndexTypeDef] = None
    ListOutgoingTypedLinks: Optional[BatchListOutgoingTypedLinksTypeDef] = None
    ListIncomingTypedLinks: Optional[BatchListIncomingTypedLinksTypeDef] = None
    GetLinkAttributes: Optional[BatchGetLinkAttributesTypeDef] = None

class BatchWriteResponseTypeDef(BaseModel):
    Responses: List[BatchWriteOperationResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchReadOperationResponseTypeDef(BaseModel):
    SuccessfulResponse: Optional[BatchReadSuccessfulResponseTypeDef] = None
    ExceptionResponse: Optional[BatchReadExceptionTypeDef] = None

class BatchWriteRequestRequestTypeDef(BaseModel):
    DirectoryArn: str
    Operations: Sequence[BatchWriteOperationTypeDef]

class BatchReadRequestRequestTypeDef(BaseModel):
    DirectoryArn: str
    Operations: Sequence[BatchReadOperationTypeDef]
    ConsistencyLevel: Optional[ConsistencyLevelType] = None

class BatchReadResponseTypeDef(BaseModel):
    Responses: List[BatchReadOperationResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

