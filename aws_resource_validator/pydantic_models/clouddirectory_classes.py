from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from botocore.response import StreamingBody
from datetime import datetime
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

class ObjectReferenceTypeDef(BaseValidatorModel):
    Selector: Optional[str] = None


class SchemaFacetTypeDef(BaseValidatorModel):
    SchemaArn: Optional[str] = None
    FacetName: Optional[str] = None


class ApplySchemaRequestTypeDef(BaseValidatorModel):
    PublishedSchemaArn: str
    DirectoryArn: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class TypedLinkSchemaAndFacetNameTypeDef(BaseValidatorModel):
    SchemaArn: str
    TypedLinkName: str


class AttributeKeyTypeDef(BaseValidatorModel):
    SchemaArn: str
    FacetName: str
    Name: str


class TypedAttributeValueOutputTypeDef(BaseValidatorModel):
    StringValue: Optional[str] = None
    BinaryValue: Optional[bytes] = None
    BooleanValue: Optional[bool] = None
    NumberValue: Optional[str] = None
    DatetimeValue: Optional[datetime] = None


class BatchAttachObjectResponseTypeDef(BaseValidatorModel):
    attachedObjectIdentifier: Optional[str] = None


class BatchAttachToIndexResponseTypeDef(BaseValidatorModel):
    AttachedObjectIdentifier: Optional[str] = None


class BatchCreateIndexResponseTypeDef(BaseValidatorModel):
    ObjectIdentifier: Optional[str] = None


class BatchCreateObjectResponseTypeDef(BaseValidatorModel):
    ObjectIdentifier: Optional[str] = None


class BatchDetachFromIndexResponseTypeDef(BaseValidatorModel):
    DetachedObjectIdentifier: Optional[str] = None


class BatchDetachObjectResponseTypeDef(BaseValidatorModel):
    detachedObjectIdentifier: Optional[str] = None


class BatchListObjectChildrenResponseTypeDef(BaseValidatorModel):
    Children: Optional[Dict[str, str]] = None
    NextToken: Optional[str] = None


class PathToObjectIdentifiersTypeDef(BaseValidatorModel):
    Path: Optional[str] = None
    ObjectIdentifiers: Optional[List[str]] = None


class ObjectIdentifierAndLinkNameTupleTypeDef(BaseValidatorModel):
    ObjectIdentifier: Optional[str] = None
    LinkName: Optional[str] = None


class BatchListObjectPoliciesResponseTypeDef(BaseValidatorModel):
    AttachedPolicyIds: Optional[List[str]] = None
    NextToken: Optional[str] = None


class BatchListPolicyAttachmentsResponseTypeDef(BaseValidatorModel):
    ObjectIdentifiers: Optional[List[str]] = None
    NextToken: Optional[str] = None


class BatchUpdateObjectAttributesResponseTypeDef(BaseValidatorModel):
    ObjectIdentifier: Optional[str] = None


class CreateDirectoryRequestTypeDef(BaseValidatorModel):
    Name: str
    SchemaArn: str


class CreateSchemaRequestTypeDef(BaseValidatorModel):
    Name: str


class DeleteDirectoryRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str


class DeleteFacetRequestTypeDef(BaseValidatorModel):
    SchemaArn: str
    Name: str


class DeleteSchemaRequestTypeDef(BaseValidatorModel):
    SchemaArn: str


class DeleteTypedLinkFacetRequestTypeDef(BaseValidatorModel):
    SchemaArn: str
    Name: str


class DirectoryTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    DirectoryArn: Optional[str] = None
    State: Optional[DirectoryStateType] = None
    CreationDateTime: Optional[datetime] = None


class DisableDirectoryRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str


class EnableDirectoryRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str


class FacetAttributeReferenceTypeDef(BaseValidatorModel):
    TargetFacetName: str
    TargetAttributeName: str


class FacetTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    ObjectType: Optional[ObjectTypeType] = None
    FacetStyle: Optional[FacetStyleType] = None


class GetAppliedSchemaVersionRequestTypeDef(BaseValidatorModel):
    SchemaArn: str


class GetDirectoryRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str


class GetFacetRequestTypeDef(BaseValidatorModel):
    SchemaArn: str
    Name: str


class GetSchemaAsJsonRequestTypeDef(BaseValidatorModel):
    SchemaArn: str


class GetTypedLinkFacetInformationRequestTypeDef(BaseValidatorModel):
    SchemaArn: str
    Name: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAppliedSchemaArnsRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    SchemaArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDevelopmentSchemaArnsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDirectoriesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    state: Optional[DirectoryStateType] = None


class ListFacetAttributesRequestTypeDef(BaseValidatorModel):
    SchemaArn: str
    Name: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListFacetNamesRequestTypeDef(BaseValidatorModel):
    SchemaArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListManagedSchemaArnsRequestTypeDef(BaseValidatorModel):
    SchemaArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListPublishedSchemaArnsRequestTypeDef(BaseValidatorModel):
    SchemaArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class TagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class ListTypedLinkFacetAttributesRequestTypeDef(BaseValidatorModel):
    SchemaArn: str
    Name: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTypedLinkFacetNamesRequestTypeDef(BaseValidatorModel):
    SchemaArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PolicyAttachmentTypeDef(BaseValidatorModel):
    PolicyId: Optional[str] = None
    ObjectIdentifier: Optional[str] = None
    PolicyType: Optional[str] = None


class PublishSchemaRequestTypeDef(BaseValidatorModel):
    DevelopmentSchemaArn: str
    Version: str
    MinorVersion: Optional[str] = None
    Name: Optional[str] = None


class PutSchemaFromJsonRequestTypeDef(BaseValidatorModel):
    SchemaArn: str
    Document: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateSchemaRequestTypeDef(BaseValidatorModel):
    SchemaArn: str
    Name: str


class UpgradeAppliedSchemaRequestTypeDef(BaseValidatorModel):
    PublishedSchemaArn: str
    DirectoryArn: str
    DryRun: Optional[bool] = None


class UpgradePublishedSchemaRequestTypeDef(BaseValidatorModel):
    DevelopmentSchemaArn: str
    PublishedSchemaArn: str
    MinorVersion: str
    DryRun: Optional[bool] = None


class AttachObjectRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ParentReference: ObjectReferenceTypeDef
    ChildReference: ObjectReferenceTypeDef
    LinkName: str


class AttachPolicyRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    PolicyReference: ObjectReferenceTypeDef
    ObjectReference: ObjectReferenceTypeDef


class AttachToIndexRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    IndexReference: ObjectReferenceTypeDef
    TargetReference: ObjectReferenceTypeDef


class BatchAttachObjectTypeDef(BaseValidatorModel):
    ParentReference: ObjectReferenceTypeDef
    ChildReference: ObjectReferenceTypeDef
    LinkName: str


class BatchAttachPolicyTypeDef(BaseValidatorModel):
    PolicyReference: ObjectReferenceTypeDef
    ObjectReference: ObjectReferenceTypeDef


class BatchAttachToIndexTypeDef(BaseValidatorModel):
    IndexReference: ObjectReferenceTypeDef
    TargetReference: ObjectReferenceTypeDef


class BatchDeleteObjectTypeDef(BaseValidatorModel):
    ObjectReference: ObjectReferenceTypeDef


class BatchDetachFromIndexTypeDef(BaseValidatorModel):
    IndexReference: ObjectReferenceTypeDef
    TargetReference: ObjectReferenceTypeDef


class BatchDetachObjectTypeDef(BaseValidatorModel):
    ParentReference: ObjectReferenceTypeDef
    LinkName: str
    BatchReferenceName: Optional[str] = None


class BatchDetachPolicyTypeDef(BaseValidatorModel):
    PolicyReference: ObjectReferenceTypeDef
    ObjectReference: ObjectReferenceTypeDef


class BatchGetObjectInformationTypeDef(BaseValidatorModel):
    ObjectReference: ObjectReferenceTypeDef


class BatchListAttachedIndicesTypeDef(BaseValidatorModel):
    TargetReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class BatchListObjectChildrenTypeDef(BaseValidatorModel):
    ObjectReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class BatchListObjectParentPathsTypeDef(BaseValidatorModel):
    ObjectReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class BatchListObjectParentsTypeDef(BaseValidatorModel):
    ObjectReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class BatchListObjectPoliciesTypeDef(BaseValidatorModel):
    ObjectReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class BatchListPolicyAttachmentsTypeDef(BaseValidatorModel):
    PolicyReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class BatchLookupPolicyTypeDef(BaseValidatorModel):
    ObjectReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DeleteObjectRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef


class DetachFromIndexRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    IndexReference: ObjectReferenceTypeDef
    TargetReference: ObjectReferenceTypeDef


class DetachObjectRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ParentReference: ObjectReferenceTypeDef
    LinkName: str


class DetachPolicyRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    PolicyReference: ObjectReferenceTypeDef
    ObjectReference: ObjectReferenceTypeDef


class GetObjectInformationRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    ConsistencyLevel: Optional[ConsistencyLevelType] = None


class ListAttachedIndicesRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    TargetReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None


class ListObjectChildrenRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None


class ListObjectParentPathsRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListObjectParentsRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    IncludeAllLinksToEachParent: Optional[bool] = None


class ListObjectPoliciesRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None


class ListPolicyAttachmentsRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    PolicyReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None


class LookupPolicyRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class BatchGetObjectAttributesTypeDef(BaseValidatorModel):
    ObjectReference: ObjectReferenceTypeDef
    SchemaFacet: SchemaFacetTypeDef
    AttributeNames: Sequence[str]


class BatchGetObjectInformationResponseTypeDef(BaseValidatorModel):
    SchemaFacets: Optional[List[SchemaFacetTypeDef]] = None
    ObjectIdentifier: Optional[str] = None


class BatchListObjectAttributesTypeDef(BaseValidatorModel):
    ObjectReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    FacetFilter: Optional[SchemaFacetTypeDef] = None


class BatchRemoveFacetFromObjectTypeDef(BaseValidatorModel):
    SchemaFacet: SchemaFacetTypeDef
    ObjectReference: ObjectReferenceTypeDef


class GetObjectAttributesRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    SchemaFacet: SchemaFacetTypeDef
    AttributeNames: Sequence[str]
    ConsistencyLevel: Optional[ConsistencyLevelType] = None


class ListObjectAttributesRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    FacetFilter: Optional[SchemaFacetTypeDef] = None


class RemoveFacetFromObjectRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    SchemaFacet: SchemaFacetTypeDef
    ObjectReference: ObjectReferenceTypeDef


class ApplySchemaResponseTypeDef(BaseValidatorModel):
    AppliedSchemaArn: str
    DirectoryArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class AttachObjectResponseTypeDef(BaseValidatorModel):
    AttachedObjectIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef


class AttachToIndexResponseTypeDef(BaseValidatorModel):
    AttachedObjectIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDirectoryResponseTypeDef(BaseValidatorModel):
    DirectoryArn: str
    Name: str
    ObjectIdentifier: str
    AppliedSchemaArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateIndexResponseTypeDef(BaseValidatorModel):
    ObjectIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateObjectResponseTypeDef(BaseValidatorModel):
    ObjectIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateSchemaResponseTypeDef(BaseValidatorModel):
    SchemaArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDirectoryResponseTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteSchemaResponseTypeDef(BaseValidatorModel):
    SchemaArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DetachFromIndexResponseTypeDef(BaseValidatorModel):
    DetachedObjectIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef


class DetachObjectResponseTypeDef(BaseValidatorModel):
    DetachedObjectIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef


class DisableDirectoryResponseTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class EnableDirectoryResponseTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetAppliedSchemaVersionResponseTypeDef(BaseValidatorModel):
    AppliedSchemaArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetObjectInformationResponseTypeDef(BaseValidatorModel):
    SchemaFacets: List[SchemaFacetTypeDef]
    ObjectIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetSchemaAsJsonResponseTypeDef(BaseValidatorModel):
    Name: str
    Document: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetTypedLinkFacetInformationResponseTypeDef(BaseValidatorModel):
    IdentityAttributeOrder: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class ListAppliedSchemaArnsResponseTypeDef(BaseValidatorModel):
    SchemaArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListDevelopmentSchemaArnsResponseTypeDef(BaseValidatorModel):
    SchemaArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListFacetNamesResponseTypeDef(BaseValidatorModel):
    FacetNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListManagedSchemaArnsResponseTypeDef(BaseValidatorModel):
    SchemaArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListObjectChildrenResponseTypeDef(BaseValidatorModel):
    Children: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListObjectPoliciesResponseTypeDef(BaseValidatorModel):
    AttachedPolicyIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListPolicyAttachmentsResponseTypeDef(BaseValidatorModel):
    ObjectIdentifiers: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListPublishedSchemaArnsResponseTypeDef(BaseValidatorModel):
    SchemaArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTypedLinkFacetNamesResponseTypeDef(BaseValidatorModel):
    FacetNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PublishSchemaResponseTypeDef(BaseValidatorModel):
    PublishedSchemaArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class PutSchemaFromJsonResponseTypeDef(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateObjectAttributesResponseTypeDef(BaseValidatorModel):
    ObjectIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateSchemaResponseTypeDef(BaseValidatorModel):
    SchemaArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpgradeAppliedSchemaResponseTypeDef(BaseValidatorModel):
    UpgradedSchemaArn: str
    DirectoryArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpgradePublishedSchemaResponseTypeDef(BaseValidatorModel):
    UpgradedSchemaArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class BatchCreateIndexTypeDef(BaseValidatorModel):
    OrderedIndexedAttributeList: Sequence[AttributeKeyTypeDef]
    IsUnique: bool
    ParentReference: Optional[ObjectReferenceTypeDef] = None
    LinkName: Optional[str] = None
    BatchReferenceName: Optional[str] = None


class CreateIndexRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    OrderedIndexedAttributeList: Sequence[AttributeKeyTypeDef]
    IsUnique: bool
    ParentReference: Optional[ObjectReferenceTypeDef] = None
    LinkName: Optional[str] = None


class AttributeKeyAndValueOutputTypeDef(BaseValidatorModel):
    Key: AttributeKeyTypeDef
    Value: TypedAttributeValueOutputTypeDef


class AttributeNameAndValueOutputTypeDef(BaseValidatorModel):
    AttributeName: str
    Value: TypedAttributeValueOutputTypeDef


class BatchListObjectParentPathsResponseTypeDef(BaseValidatorModel):
    PathToObjectIdentifiersList: Optional[List[PathToObjectIdentifiersTypeDef]] = None
    NextToken: Optional[str] = None


class ListObjectParentPathsResponseTypeDef(BaseValidatorModel):
    PathToObjectIdentifiersList: List[PathToObjectIdentifiersTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class BatchListObjectParentsResponseTypeDef(BaseValidatorModel):
    ParentLinks: Optional[List[ObjectIdentifierAndLinkNameTupleTypeDef]] = None
    NextToken: Optional[str] = None


class ListObjectParentsResponseTypeDef(BaseValidatorModel):
    Parents: Dict[str, str]
    ParentLinks: List[ObjectIdentifierAndLinkNameTupleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetDirectoryResponseTypeDef(BaseValidatorModel):
    Directory: DirectoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListDirectoriesResponseTypeDef(BaseValidatorModel):
    Directories: List[DirectoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetFacetResponseTypeDef(BaseValidatorModel):
    Facet: FacetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListAppliedSchemaArnsRequestPaginateTypeDef(BaseValidatorModel):
    DirectoryArn: str
    SchemaArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAttachedIndicesRequestPaginateTypeDef(BaseValidatorModel):
    DirectoryArn: str
    TargetReference: ObjectReferenceTypeDef
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDevelopmentSchemaArnsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDirectoriesRequestPaginateTypeDef(BaseValidatorModel):
    state: Optional[DirectoryStateType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFacetAttributesRequestPaginateTypeDef(BaseValidatorModel):
    SchemaArn: str
    Name: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFacetNamesRequestPaginateTypeDef(BaseValidatorModel):
    SchemaArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListManagedSchemaArnsRequestPaginateTypeDef(BaseValidatorModel):
    SchemaArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListObjectAttributesRequestPaginateTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    FacetFilter: Optional[SchemaFacetTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListObjectParentPathsRequestPaginateTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListObjectPoliciesRequestPaginateTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPolicyAttachmentsRequestPaginateTypeDef(BaseValidatorModel):
    DirectoryArn: str
    PolicyReference: ObjectReferenceTypeDef
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPublishedSchemaArnsRequestPaginateTypeDef(BaseValidatorModel):
    SchemaArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTagsForResourceRequestPaginateTypeDef(BaseValidatorModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTypedLinkFacetAttributesRequestPaginateTypeDef(BaseValidatorModel):
    SchemaArn: str
    Name: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTypedLinkFacetNamesRequestPaginateTypeDef(BaseValidatorModel):
    SchemaArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class LookupPolicyRequestPaginateTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]


class PolicyToPathTypeDef(BaseValidatorModel):
    Path: Optional[str] = None
    Policies: Optional[List[PolicyAttachmentTypeDef]] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class BlobTypeDef(BaseValidatorModel):
    pass


class TypedAttributeValueTypeDef(BaseValidatorModel):
    StringValue: Optional[str] = None
    BinaryValue: Optional[BlobTypeDef] = None
    BooleanValue: Optional[bool] = None
    NumberValue: Optional[str] = None
    DatetimeValue: Optional[TimestampTypeDef] = None


class BatchGetLinkAttributesResponseTypeDef(BaseValidatorModel):
    Attributes: Optional[List[AttributeKeyAndValueOutputTypeDef]] = None


class BatchGetObjectAttributesResponseTypeDef(BaseValidatorModel):
    Attributes: Optional[List[AttributeKeyAndValueOutputTypeDef]] = None


class BatchListObjectAttributesResponseTypeDef(BaseValidatorModel):
    Attributes: Optional[List[AttributeKeyAndValueOutputTypeDef]] = None
    NextToken: Optional[str] = None


class GetLinkAttributesResponseTypeDef(BaseValidatorModel):
    Attributes: List[AttributeKeyAndValueOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetObjectAttributesResponseTypeDef(BaseValidatorModel):
    Attributes: List[AttributeKeyAndValueOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class IndexAttachmentTypeDef(BaseValidatorModel):
    IndexedAttributes: Optional[List[AttributeKeyAndValueOutputTypeDef]] = None
    ObjectIdentifier: Optional[str] = None


class ListObjectAttributesResponseTypeDef(BaseValidatorModel):
    Attributes: List[AttributeKeyAndValueOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TypedLinkSpecifierOutputTypeDef(BaseValidatorModel):
    TypedLinkFacet: TypedLinkSchemaAndFacetNameTypeDef
    SourceObjectReference: ObjectReferenceTypeDef
    TargetObjectReference: ObjectReferenceTypeDef
    IdentityAttributeValues: List[AttributeNameAndValueOutputTypeDef]


class FacetAttributeDefinitionOutputTypeDef(BaseValidatorModel):
    pass


class FacetAttributeOutputTypeDef(BaseValidatorModel):
    Name: str
    AttributeDefinition: Optional[FacetAttributeDefinitionOutputTypeDef] = None
    AttributeReference: Optional[FacetAttributeReferenceTypeDef] = None
    RequiredBehavior: Optional[RequiredAttributeBehaviorType] = None


class TypedLinkAttributeDefinitionOutputTypeDef(BaseValidatorModel):
    pass


class ListTypedLinkFacetAttributesResponseTypeDef(BaseValidatorModel):
    Attributes: List[TypedLinkAttributeDefinitionOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class BatchLookupPolicyResponseTypeDef(BaseValidatorModel):
    PolicyToPathList: Optional[List[PolicyToPathTypeDef]] = None
    NextToken: Optional[str] = None


class LookupPolicyResponseTypeDef(BaseValidatorModel):
    PolicyToPathList: List[PolicyToPathTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class BatchListAttachedIndicesResponseTypeDef(BaseValidatorModel):
    IndexAttachments: Optional[List[IndexAttachmentTypeDef]] = None
    NextToken: Optional[str] = None


class BatchListIndexResponseTypeDef(BaseValidatorModel):
    IndexAttachments: Optional[List[IndexAttachmentTypeDef]] = None
    NextToken: Optional[str] = None


class ListAttachedIndicesResponseTypeDef(BaseValidatorModel):
    IndexAttachments: List[IndexAttachmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListIndexResponseTypeDef(BaseValidatorModel):
    IndexAttachments: List[IndexAttachmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class AttachTypedLinkResponseTypeDef(BaseValidatorModel):
    TypedLinkSpecifier: TypedLinkSpecifierOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class BatchAttachTypedLinkResponseTypeDef(BaseValidatorModel):
    TypedLinkSpecifier: Optional[TypedLinkSpecifierOutputTypeDef] = None


class BatchListIncomingTypedLinksResponseTypeDef(BaseValidatorModel):
    LinkSpecifiers: Optional[List[TypedLinkSpecifierOutputTypeDef]] = None
    NextToken: Optional[str] = None


class BatchListOutgoingTypedLinksResponseTypeDef(BaseValidatorModel):
    TypedLinkSpecifiers: Optional[List[TypedLinkSpecifierOutputTypeDef]] = None
    NextToken: Optional[str] = None


class ListIncomingTypedLinksResponseTypeDef(BaseValidatorModel):
    LinkSpecifiers: List[TypedLinkSpecifierOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListOutgoingTypedLinksResponseTypeDef(BaseValidatorModel):
    TypedLinkSpecifiers: List[TypedLinkSpecifierOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListFacetAttributesResponseTypeDef(BaseValidatorModel):
    Attributes: List[FacetAttributeOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TypedAttributeValueUnionTypeDef(BaseValidatorModel):
    pass


class AttributeKeyAndValueTypeDef(BaseValidatorModel):
    Key: AttributeKeyTypeDef
    Value: TypedAttributeValueUnionTypeDef


class AttributeNameAndValueTypeDef(BaseValidatorModel):
    AttributeName: str
    Value: TypedAttributeValueUnionTypeDef


class LinkAttributeActionTypeDef(BaseValidatorModel):
    AttributeActionType: Optional[UpdateActionTypeType] = None
    AttributeUpdateValue: Optional[TypedAttributeValueUnionTypeDef] = None


class ObjectAttributeActionTypeDef(BaseValidatorModel):
    ObjectAttributeActionType: Optional[UpdateActionTypeType] = None
    ObjectAttributeUpdateValue: Optional[TypedAttributeValueUnionTypeDef] = None


class TypedAttributeValueRangeTypeDef(BaseValidatorModel):
    StartMode: RangeModeType
    EndMode: RangeModeType
    StartValue: Optional[TypedAttributeValueUnionTypeDef] = None
    EndValue: Optional[TypedAttributeValueUnionTypeDef] = None


class BatchWriteOperationResponseTypeDef(BaseValidatorModel):
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


class BatchReadSuccessfulResponseTypeDef(BaseValidatorModel):
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


class BatchCreateObjectTypeDef(BaseValidatorModel):
    SchemaFacet: Sequence[SchemaFacetTypeDef]
    ObjectAttributeList: Sequence[AttributeKeyAndValueTypeDef]
    ParentReference: Optional[ObjectReferenceTypeDef] = None
    LinkName: Optional[str] = None
    BatchReferenceName: Optional[str] = None


class LinkAttributeUpdateTypeDef(BaseValidatorModel):
    AttributeKey: Optional[AttributeKeyTypeDef] = None
    AttributeAction: Optional[LinkAttributeActionTypeDef] = None


class ObjectAttributeUpdateTypeDef(BaseValidatorModel):
    ObjectAttributeKey: Optional[AttributeKeyTypeDef] = None
    ObjectAttributeAction: Optional[ObjectAttributeActionTypeDef] = None


class ObjectAttributeRangeTypeDef(BaseValidatorModel):
    AttributeKey: Optional[AttributeKeyTypeDef] = None
    Range: Optional[TypedAttributeValueRangeTypeDef] = None


class TypedLinkAttributeRangeTypeDef(BaseValidatorModel):
    Range: TypedAttributeValueRangeTypeDef
    AttributeName: Optional[str] = None


class BatchWriteResponseTypeDef(BaseValidatorModel):
    Responses: List[BatchWriteOperationResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchReadExceptionTypeDef(BaseValidatorModel):
    pass


class BatchReadOperationResponseTypeDef(BaseValidatorModel):
    SuccessfulResponse: Optional[BatchReadSuccessfulResponseTypeDef] = None
    ExceptionResponse: Optional[BatchReadExceptionTypeDef] = None


class AttributeKeyAndValueUnionTypeDef(BaseValidatorModel):
    pass


class AddFacetToObjectRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    SchemaFacet: SchemaFacetTypeDef
    ObjectReference: ObjectReferenceTypeDef
    ObjectAttributeList: Optional[Sequence[AttributeKeyAndValueUnionTypeDef]] = None


class BatchAddFacetToObjectTypeDef(BaseValidatorModel):
    SchemaFacet: SchemaFacetTypeDef
    ObjectAttributeList: Sequence[AttributeKeyAndValueUnionTypeDef]
    ObjectReference: ObjectReferenceTypeDef


class CreateObjectRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    SchemaFacets: Sequence[SchemaFacetTypeDef]
    ObjectAttributeList: Optional[Sequence[AttributeKeyAndValueUnionTypeDef]] = None
    ParentReference: Optional[ObjectReferenceTypeDef] = None
    LinkName: Optional[str] = None


class AttributeNameAndValueUnionTypeDef(BaseValidatorModel):
    pass


class AttachTypedLinkRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    SourceObjectReference: ObjectReferenceTypeDef
    TargetObjectReference: ObjectReferenceTypeDef
    TypedLinkFacet: TypedLinkSchemaAndFacetNameTypeDef
    Attributes: Sequence[AttributeNameAndValueUnionTypeDef]


class BatchAttachTypedLinkTypeDef(BaseValidatorModel):
    SourceObjectReference: ObjectReferenceTypeDef
    TargetObjectReference: ObjectReferenceTypeDef
    TypedLinkFacet: TypedLinkSchemaAndFacetNameTypeDef
    Attributes: Sequence[AttributeNameAndValueUnionTypeDef]


class TypedLinkSpecifierTypeDef(BaseValidatorModel):
    TypedLinkFacet: TypedLinkSchemaAndFacetNameTypeDef
    SourceObjectReference: ObjectReferenceTypeDef
    TargetObjectReference: ObjectReferenceTypeDef
    IdentityAttributeValues: Sequence[AttributeNameAndValueUnionTypeDef]


class FacetAttributeDefinitionUnionTypeDef(BaseValidatorModel):
    pass


class FacetAttributeTypeDef(BaseValidatorModel):
    Name: str
    AttributeDefinition: Optional[FacetAttributeDefinitionUnionTypeDef] = None
    AttributeReference: Optional[FacetAttributeReferenceTypeDef] = None
    RequiredBehavior: Optional[RequiredAttributeBehaviorType] = None


class BatchUpdateObjectAttributesTypeDef(BaseValidatorModel):
    ObjectReference: ObjectReferenceTypeDef
    AttributeUpdates: Sequence[ObjectAttributeUpdateTypeDef]


class UpdateObjectAttributesRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    AttributeUpdates: Sequence[ObjectAttributeUpdateTypeDef]


class BatchListIndexTypeDef(BaseValidatorModel):
    IndexReference: ObjectReferenceTypeDef
    RangesOnIndexedValues: Optional[Sequence[ObjectAttributeRangeTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListIndexRequestPaginateTypeDef(BaseValidatorModel):
    DirectoryArn: str
    IndexReference: ObjectReferenceTypeDef
    RangesOnIndexedValues: Optional[Sequence[ObjectAttributeRangeTypeDef]] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListIndexRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    IndexReference: ObjectReferenceTypeDef
    RangesOnIndexedValues: Optional[Sequence[ObjectAttributeRangeTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None


class BatchListIncomingTypedLinksTypeDef(BaseValidatorModel):
    ObjectReference: ObjectReferenceTypeDef
    FilterAttributeRanges: Optional[Sequence[TypedLinkAttributeRangeTypeDef]] = None
    FilterTypedLink: Optional[TypedLinkSchemaAndFacetNameTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class BatchListOutgoingTypedLinksTypeDef(BaseValidatorModel):
    ObjectReference: ObjectReferenceTypeDef
    FilterAttributeRanges: Optional[Sequence[TypedLinkAttributeRangeTypeDef]] = None
    FilterTypedLink: Optional[TypedLinkSchemaAndFacetNameTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListIncomingTypedLinksRequestPaginateTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    FilterAttributeRanges: Optional[Sequence[TypedLinkAttributeRangeTypeDef]] = None
    FilterTypedLink: Optional[TypedLinkSchemaAndFacetNameTypeDef] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListIncomingTypedLinksRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    FilterAttributeRanges: Optional[Sequence[TypedLinkAttributeRangeTypeDef]] = None
    FilterTypedLink: Optional[TypedLinkSchemaAndFacetNameTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None


class ListOutgoingTypedLinksRequestPaginateTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    FilterAttributeRanges: Optional[Sequence[TypedLinkAttributeRangeTypeDef]] = None
    FilterTypedLink: Optional[TypedLinkSchemaAndFacetNameTypeDef] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListOutgoingTypedLinksRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    FilterAttributeRanges: Optional[Sequence[TypedLinkAttributeRangeTypeDef]] = None
    FilterTypedLink: Optional[TypedLinkSchemaAndFacetNameTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None


class TypedLinkAttributeDefinitionUnionTypeDef(BaseValidatorModel):
    pass


class TypedLinkFacetAttributeUpdateTypeDef(BaseValidatorModel):
    Attribute: TypedLinkAttributeDefinitionUnionTypeDef
    Action: UpdateActionTypeType


class TypedLinkFacetTypeDef(BaseValidatorModel):
    Name: str
    Attributes: Sequence[TypedLinkAttributeDefinitionUnionTypeDef]
    IdentityAttributeOrder: Sequence[str]


class BatchReadResponseTypeDef(BaseValidatorModel):
    Responses: List[BatchReadOperationResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateTypedLinkFacetRequestTypeDef(BaseValidatorModel):
    SchemaArn: str
    Name: str
    AttributeUpdates: Sequence[TypedLinkFacetAttributeUpdateTypeDef]
    IdentityAttributeOrder: Sequence[str]


class CreateTypedLinkFacetRequestTypeDef(BaseValidatorModel):
    SchemaArn: str
    Facet: TypedLinkFacetTypeDef


class TypedLinkSpecifierUnionTypeDef(BaseValidatorModel):
    pass


class BatchDetachTypedLinkTypeDef(BaseValidatorModel):
    TypedLinkSpecifier: TypedLinkSpecifierUnionTypeDef


class BatchGetLinkAttributesTypeDef(BaseValidatorModel):
    TypedLinkSpecifier: TypedLinkSpecifierUnionTypeDef
    AttributeNames: Sequence[str]


class BatchUpdateLinkAttributesTypeDef(BaseValidatorModel):
    TypedLinkSpecifier: TypedLinkSpecifierUnionTypeDef
    AttributeUpdates: Sequence[LinkAttributeUpdateTypeDef]


class DetachTypedLinkRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    TypedLinkSpecifier: TypedLinkSpecifierUnionTypeDef


class GetLinkAttributesRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    TypedLinkSpecifier: TypedLinkSpecifierUnionTypeDef
    AttributeNames: Sequence[str]
    ConsistencyLevel: Optional[ConsistencyLevelType] = None


class UpdateLinkAttributesRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    TypedLinkSpecifier: TypedLinkSpecifierUnionTypeDef
    AttributeUpdates: Sequence[LinkAttributeUpdateTypeDef]


class FacetAttributeUnionTypeDef(BaseValidatorModel):
    pass


class CreateFacetRequestTypeDef(BaseValidatorModel):
    SchemaArn: str
    Name: str
    Attributes: Optional[Sequence[FacetAttributeUnionTypeDef]] = None
    ObjectType: Optional[ObjectTypeType] = None
    FacetStyle: Optional[FacetStyleType] = None


class FacetAttributeUpdateTypeDef(BaseValidatorModel):
    Attribute: Optional[FacetAttributeUnionTypeDef] = None
    Action: Optional[UpdateActionTypeType] = None


class BatchReadOperationTypeDef(BaseValidatorModel):
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


class BatchWriteOperationTypeDef(BaseValidatorModel):
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


class UpdateFacetRequestTypeDef(BaseValidatorModel):
    SchemaArn: str
    Name: str
    AttributeUpdates: Optional[Sequence[FacetAttributeUpdateTypeDef]] = None
    ObjectType: Optional[ObjectTypeType] = None


class BatchReadRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    Operations: Sequence[BatchReadOperationTypeDef]
    ConsistencyLevel: Optional[ConsistencyLevelType] = None


class BatchWriteRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    Operations: Sequence[BatchWriteOperationTypeDef]


