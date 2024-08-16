from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class ApplySchemaRequestRequestTypeDef(BaseValidatorModel):
    PublishedSchemaArn: str
    DirectoryArn: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class TypedLinkSchemaAndFacetNameTypeDef(BaseValidatorModel):
    SchemaArn: str
    TypedLinkName: str

class AttributeKeyTypeDef(BaseValidatorModel):
    SchemaArn: str
    FacetName: str
    Name: str

class TypedAttributeValuePaginatorTypeDef(BaseValidatorModel):
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

class BatchReadExceptionTypeDef(BaseValidatorModel):
    Type: Optional[BatchReadExceptionTypeType] = None
    Message: Optional[str] = None

class BatchUpdateObjectAttributesResponseTypeDef(BaseValidatorModel):
    ObjectIdentifier: Optional[str] = None

class CreateDirectoryRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    SchemaArn: str

class CreateSchemaRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteDirectoryRequestRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str

class DeleteFacetRequestRequestTypeDef(BaseValidatorModel):
    SchemaArn: str
    Name: str

class DeleteSchemaRequestRequestTypeDef(BaseValidatorModel):
    SchemaArn: str

class DeleteTypedLinkFacetRequestRequestTypeDef(BaseValidatorModel):
    SchemaArn: str
    Name: str

class DirectoryTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    DirectoryArn: Optional[str] = None
    State: Optional[DirectoryStateType] = None
    CreationDateTime: Optional[datetime] = None

class DisableDirectoryRequestRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str

class EnableDirectoryRequestRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str

class RulePaginatorTypeDef(BaseValidatorModel):
    Type: Optional[RuleTypeType] = None
    Parameters: Optional[Dict[str, str]] = None

class RuleTypeDef(BaseValidatorModel):
    Type: Optional[RuleTypeType] = None
    Parameters: Optional[Mapping[str, str]] = None

class FacetAttributeReferenceTypeDef(BaseValidatorModel):
    TargetFacetName: str
    TargetAttributeName: str

class FacetTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    ObjectType: Optional[ObjectTypeType] = None
    FacetStyle: Optional[FacetStyleType] = None

class GetAppliedSchemaVersionRequestRequestTypeDef(BaseValidatorModel):
    SchemaArn: str

class GetDirectoryRequestRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str

class GetFacetRequestRequestTypeDef(BaseValidatorModel):
    SchemaArn: str
    Name: str

class GetSchemaAsJsonRequestRequestTypeDef(BaseValidatorModel):
    SchemaArn: str

class GetTypedLinkFacetInformationRequestRequestTypeDef(BaseValidatorModel):
    SchemaArn: str
    Name: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAppliedSchemaArnsRequestRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    SchemaArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDevelopmentSchemaArnsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDirectoriesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    state: Optional[DirectoryStateType] = None

class ListFacetAttributesRequestRequestTypeDef(BaseValidatorModel):
    SchemaArn: str
    Name: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListFacetNamesRequestRequestTypeDef(BaseValidatorModel):
    SchemaArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListManagedSchemaArnsRequestRequestTypeDef(BaseValidatorModel):
    SchemaArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListPublishedSchemaArnsRequestRequestTypeDef(BaseValidatorModel):
    SchemaArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class TagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class ListTypedLinkFacetAttributesRequestRequestTypeDef(BaseValidatorModel):
    SchemaArn: str
    Name: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTypedLinkFacetNamesRequestRequestTypeDef(BaseValidatorModel):
    SchemaArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PolicyAttachmentTypeDef(BaseValidatorModel):
    PolicyId: Optional[str] = None
    ObjectIdentifier: Optional[str] = None
    PolicyType: Optional[str] = None

class PublishSchemaRequestRequestTypeDef(BaseValidatorModel):
    DevelopmentSchemaArn: str
    Version: str
    MinorVersion: Optional[str] = None
    Name: Optional[str] = None

class PutSchemaFromJsonRequestRequestTypeDef(BaseValidatorModel):
    SchemaArn: str
    Document: str

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateSchemaRequestRequestTypeDef(BaseValidatorModel):
    SchemaArn: str
    Name: str

class UpgradeAppliedSchemaRequestRequestTypeDef(BaseValidatorModel):
    PublishedSchemaArn: str
    DirectoryArn: str
    DryRun: Optional[bool] = None

class UpgradePublishedSchemaRequestRequestTypeDef(BaseValidatorModel):
    DevelopmentSchemaArn: str
    PublishedSchemaArn: str
    MinorVersion: str
    DryRun: Optional[bool] = None

class AttachObjectRequestRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ParentReference: ObjectReferenceTypeDef
    ChildReference: ObjectReferenceTypeDef
    LinkName: str

class AttachPolicyRequestRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    PolicyReference: ObjectReferenceTypeDef
    ObjectReference: ObjectReferenceTypeDef

class AttachToIndexRequestRequestTypeDef(BaseValidatorModel):
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

class DeleteObjectRequestRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef

class DetachFromIndexRequestRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    IndexReference: ObjectReferenceTypeDef
    TargetReference: ObjectReferenceTypeDef

class DetachObjectRequestRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ParentReference: ObjectReferenceTypeDef
    LinkName: str

class DetachPolicyRequestRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    PolicyReference: ObjectReferenceTypeDef
    ObjectReference: ObjectReferenceTypeDef

class GetObjectInformationRequestRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    ConsistencyLevel: Optional[ConsistencyLevelType] = None

class ListAttachedIndicesRequestRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    TargetReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None

class ListObjectChildrenRequestRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None

class ListObjectParentPathsRequestRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListObjectParentsRequestRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    IncludeAllLinksToEachParent: Optional[bool] = None

class ListObjectPoliciesRequestRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None

class ListPolicyAttachmentsRequestRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    PolicyReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None

class LookupPolicyRequestRequestTypeDef(BaseValidatorModel):
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

class GetObjectAttributesRequestRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    SchemaFacet: SchemaFacetTypeDef
    AttributeNames: Sequence[str]
    ConsistencyLevel: Optional[ConsistencyLevelType] = None

class ListObjectAttributesRequestRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    FacetFilter: Optional[SchemaFacetTypeDef] = None

class RemoveFacetFromObjectRequestRequestTypeDef(BaseValidatorModel):
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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDevelopmentSchemaArnsResponseTypeDef(BaseValidatorModel):
    SchemaArns: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFacetNamesResponseTypeDef(BaseValidatorModel):
    FacetNames: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListManagedSchemaArnsResponseTypeDef(BaseValidatorModel):
    SchemaArns: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListObjectChildrenResponseTypeDef(BaseValidatorModel):
    Children: Dict[str, str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListObjectPoliciesResponseTypeDef(BaseValidatorModel):
    AttachedPolicyIds: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPolicyAttachmentsResponseTypeDef(BaseValidatorModel):
    ObjectIdentifiers: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPublishedSchemaArnsResponseTypeDef(BaseValidatorModel):
    SchemaArns: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTypedLinkFacetNamesResponseTypeDef(BaseValidatorModel):
    FacetNames: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class CreateIndexRequestRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    OrderedIndexedAttributeList: Sequence[AttributeKeyTypeDef]
    IsUnique: bool
    ParentReference: Optional[ObjectReferenceTypeDef] = None
    LinkName: Optional[str] = None

class AttributeKeyAndValuePaginatorTypeDef(BaseValidatorModel):
    Key: AttributeKeyTypeDef
    Value: TypedAttributeValuePaginatorTypeDef

class AttributeNameAndValuePaginatorTypeDef(BaseValidatorModel):
    AttributeName: str
    Value: TypedAttributeValuePaginatorTypeDef

class TypedAttributeValueRangePaginatorTypeDef(BaseValidatorModel):
    StartMode: RangeModeType
    EndMode: RangeModeType
    StartValue: Optional[TypedAttributeValuePaginatorTypeDef] = None
    EndValue: Optional[TypedAttributeValuePaginatorTypeDef] = None

class BatchListObjectParentPathsResponseTypeDef(BaseValidatorModel):
    PathToObjectIdentifiersList: Optional[List[PathToObjectIdentifiersTypeDef]] = None
    NextToken: Optional[str] = None

class ListObjectParentPathsResponseTypeDef(BaseValidatorModel):
    PathToObjectIdentifiersList: List[PathToObjectIdentifiersTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchListObjectParentsResponseTypeDef(BaseValidatorModel):
    ParentLinks: Optional[List[ObjectIdentifierAndLinkNameTupleTypeDef]] = None
    NextToken: Optional[str] = None

class ListObjectParentsResponseTypeDef(BaseValidatorModel):
    Parents: Dict[str, str]
    NextToken: str
    ParentLinks: List[ObjectIdentifierAndLinkNameTupleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDirectoryResponseTypeDef(BaseValidatorModel):
    Directory: DirectoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDirectoriesResponseTypeDef(BaseValidatorModel):
    Directories: List[DirectoryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class FacetAttributeDefinitionPaginatorTypeDef(BaseValidatorModel):
    Type: FacetAttributeTypeType
    DefaultValue: Optional[TypedAttributeValuePaginatorTypeDef] = None
    IsImmutable: Optional[bool] = None
    Rules: Optional[Dict[str, RulePaginatorTypeDef]] = None

class TypedLinkAttributeDefinitionPaginatorTypeDef(BaseValidatorModel):
    Name: str
    Type: FacetAttributeTypeType
    RequiredBehavior: RequiredAttributeBehaviorType
    DefaultValue: Optional[TypedAttributeValuePaginatorTypeDef] = None
    IsImmutable: Optional[bool] = None
    Rules: Optional[Dict[str, RulePaginatorTypeDef]] = None

class GetFacetResponseTypeDef(BaseValidatorModel):
    Facet: FacetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppliedSchemaArnsRequestListAppliedSchemaArnsPaginateTypeDef(BaseValidatorModel):
    DirectoryArn: str
    SchemaArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAttachedIndicesRequestListAttachedIndicesPaginateTypeDef(BaseValidatorModel):
    DirectoryArn: str
    TargetReference: ObjectReferenceTypeDef
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDevelopmentSchemaArnsRequestListDevelopmentSchemaArnsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDirectoriesRequestListDirectoriesPaginateTypeDef(BaseValidatorModel):
    state: Optional[DirectoryStateType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFacetAttributesRequestListFacetAttributesPaginateTypeDef(BaseValidatorModel):
    SchemaArn: str
    Name: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFacetNamesRequestListFacetNamesPaginateTypeDef(BaseValidatorModel):
    SchemaArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListManagedSchemaArnsRequestListManagedSchemaArnsPaginateTypeDef(BaseValidatorModel):
    SchemaArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListObjectAttributesRequestListObjectAttributesPaginateTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    FacetFilter: Optional[SchemaFacetTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListObjectParentPathsRequestListObjectParentPathsPaginateTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListObjectPoliciesRequestListObjectPoliciesPaginateTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPolicyAttachmentsRequestListPolicyAttachmentsPaginateTypeDef(BaseValidatorModel):
    DirectoryArn: str
    PolicyReference: ObjectReferenceTypeDef
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPublishedSchemaArnsRequestListPublishedSchemaArnsPaginateTypeDef(BaseValidatorModel):
    SchemaArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(BaseValidatorModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTypedLinkFacetAttributesRequestListTypedLinkFacetAttributesPaginateTypeDef(BaseValidatorModel):
    SchemaArn: str
    Name: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTypedLinkFacetNamesRequestListTypedLinkFacetNamesPaginateTypeDef(BaseValidatorModel):
    SchemaArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class LookupPolicyRequestLookupPolicyPaginateTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class PolicyToPathTypeDef(BaseValidatorModel):
    Path: Optional[str] = None
    Policies: Optional[List[PolicyAttachmentTypeDef]] = None

class TypedAttributeValueTypeDef(BaseValidatorModel):
    StringValue: Optional[str] = None
    BinaryValue: Optional[BlobTypeDef] = None
    BooleanValue: Optional[bool] = None
    NumberValue: Optional[str] = None
    DatetimeValue: Optional[TimestampTypeDef] = None

class IndexAttachmentPaginatorTypeDef(BaseValidatorModel):
    IndexedAttributes: Optional[List[AttributeKeyAndValuePaginatorTypeDef]] = None
    ObjectIdentifier: Optional[str] = None

class ListObjectAttributesResponsePaginatorTypeDef(BaseValidatorModel):
    Attributes: List[AttributeKeyAndValuePaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TypedLinkSpecifierPaginatorTypeDef(BaseValidatorModel):
    TypedLinkFacet: TypedLinkSchemaAndFacetNameTypeDef
    SourceObjectReference: ObjectReferenceTypeDef
    TargetObjectReference: ObjectReferenceTypeDef
    IdentityAttributeValues: List[AttributeNameAndValuePaginatorTypeDef]

class ObjectAttributeRangePaginatorTypeDef(BaseValidatorModel):
    AttributeKey: Optional[AttributeKeyTypeDef] = None
    Range: Optional[TypedAttributeValueRangePaginatorTypeDef] = None

class TypedLinkAttributeRangePaginatorTypeDef(BaseValidatorModel):
    Range: TypedAttributeValueRangePaginatorTypeDef
    AttributeName: Optional[str] = None

class FacetAttributePaginatorTypeDef(BaseValidatorModel):
    Name: str
    AttributeDefinition: Optional[FacetAttributeDefinitionPaginatorTypeDef] = None
    AttributeReference: Optional[FacetAttributeReferenceTypeDef] = None
    RequiredBehavior: Optional[RequiredAttributeBehaviorType] = None

class ListTypedLinkFacetAttributesResponsePaginatorTypeDef(BaseValidatorModel):
    Attributes: List[TypedLinkAttributeDefinitionPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchLookupPolicyResponseTypeDef(BaseValidatorModel):
    PolicyToPathList: Optional[List[PolicyToPathTypeDef]] = None
    NextToken: Optional[str] = None

class LookupPolicyResponseTypeDef(BaseValidatorModel):
    PolicyToPathList: List[PolicyToPathTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AttributeKeyAndValueTypeDef(BaseValidatorModel):
    Key: AttributeKeyTypeDef
    Value: TypedAttributeValueTypeDef

class AttributeNameAndValueTypeDef(BaseValidatorModel):
    AttributeName: str
    Value: TypedAttributeValueTypeDef

class FacetAttributeDefinitionTypeDef(BaseValidatorModel):
    Type: FacetAttributeTypeType
    DefaultValue: Optional[TypedAttributeValueTypeDef] = None
    IsImmutable: Optional[bool] = None
    Rules: Optional[Mapping[str, RuleTypeDef]] = None

class LinkAttributeActionTypeDef(BaseValidatorModel):
    AttributeActionType: Optional[UpdateActionTypeType] = None
    AttributeUpdateValue: Optional[TypedAttributeValueTypeDef] = None

class ObjectAttributeActionTypeDef(BaseValidatorModel):
    ObjectAttributeActionType: Optional[UpdateActionTypeType] = None
    ObjectAttributeUpdateValue: Optional[TypedAttributeValueTypeDef] = None

class TypedAttributeValueRangeTypeDef(BaseValidatorModel):
    StartMode: RangeModeType
    EndMode: RangeModeType
    StartValue: Optional[TypedAttributeValueTypeDef] = None
    EndValue: Optional[TypedAttributeValueTypeDef] = None

class TypedLinkAttributeDefinitionTypeDef(BaseValidatorModel):
    Name: str
    Type: FacetAttributeTypeType
    RequiredBehavior: RequiredAttributeBehaviorType
    DefaultValue: Optional[TypedAttributeValueTypeDef] = None
    IsImmutable: Optional[bool] = None
    Rules: Optional[Mapping[str, RuleTypeDef]] = None

class ListAttachedIndicesResponsePaginatorTypeDef(BaseValidatorModel):
    IndexAttachments: List[IndexAttachmentPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListIndexResponsePaginatorTypeDef(BaseValidatorModel):
    IndexAttachments: List[IndexAttachmentPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListIncomingTypedLinksResponsePaginatorTypeDef(BaseValidatorModel):
    LinkSpecifiers: List[TypedLinkSpecifierPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListOutgoingTypedLinksResponsePaginatorTypeDef(BaseValidatorModel):
    TypedLinkSpecifiers: List[TypedLinkSpecifierPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListIndexRequestListIndexPaginateTypeDef(BaseValidatorModel):
    DirectoryArn: str
    IndexReference: ObjectReferenceTypeDef
    RangesOnIndexedValues: Optional[Sequence[ObjectAttributeRangePaginatorTypeDef]] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIncomingTypedLinksRequestListIncomingTypedLinksPaginateTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    FilterAttributeRanges: Optional[Sequence[TypedLinkAttributeRangePaginatorTypeDef]] = None
    FilterTypedLink: Optional[TypedLinkSchemaAndFacetNameTypeDef] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOutgoingTypedLinksRequestListOutgoingTypedLinksPaginateTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    FilterAttributeRanges: Optional[Sequence[TypedLinkAttributeRangePaginatorTypeDef]] = None
    FilterTypedLink: Optional[TypedLinkSchemaAndFacetNameTypeDef] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFacetAttributesResponsePaginatorTypeDef(BaseValidatorModel):
    Attributes: List[FacetAttributePaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AddFacetToObjectRequestRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    SchemaFacet: SchemaFacetTypeDef
    ObjectReference: ObjectReferenceTypeDef
    ObjectAttributeList: Optional[Sequence[AttributeKeyAndValueTypeDef]] = None

class BatchAddFacetToObjectTypeDef(BaseValidatorModel):
    SchemaFacet: SchemaFacetTypeDef
    ObjectAttributeList: Sequence[AttributeKeyAndValueTypeDef]
    ObjectReference: ObjectReferenceTypeDef

class BatchCreateObjectTypeDef(BaseValidatorModel):
    SchemaFacet: Sequence[SchemaFacetTypeDef]
    ObjectAttributeList: Sequence[AttributeKeyAndValueTypeDef]
    ParentReference: Optional[ObjectReferenceTypeDef] = None
    LinkName: Optional[str] = None
    BatchReferenceName: Optional[str] = None

class BatchGetLinkAttributesResponseTypeDef(BaseValidatorModel):
    Attributes: Optional[List[AttributeKeyAndValueTypeDef]] = None

class BatchGetObjectAttributesResponseTypeDef(BaseValidatorModel):
    Attributes: Optional[List[AttributeKeyAndValueTypeDef]] = None

class BatchListObjectAttributesResponseTypeDef(BaseValidatorModel):
    Attributes: Optional[List[AttributeKeyAndValueTypeDef]] = None
    NextToken: Optional[str] = None

class CreateObjectRequestRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    SchemaFacets: Sequence[SchemaFacetTypeDef]
    ObjectAttributeList: Optional[Sequence[AttributeKeyAndValueTypeDef]] = None
    ParentReference: Optional[ObjectReferenceTypeDef] = None
    LinkName: Optional[str] = None

class GetLinkAttributesResponseTypeDef(BaseValidatorModel):
    Attributes: List[AttributeKeyAndValueTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetObjectAttributesResponseTypeDef(BaseValidatorModel):
    Attributes: List[AttributeKeyAndValueTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class IndexAttachmentTypeDef(BaseValidatorModel):
    IndexedAttributes: Optional[List[AttributeKeyAndValueTypeDef]] = None
    ObjectIdentifier: Optional[str] = None

class ListObjectAttributesResponseTypeDef(BaseValidatorModel):
    Attributes: List[AttributeKeyAndValueTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AttachTypedLinkRequestRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    SourceObjectReference: ObjectReferenceTypeDef
    TargetObjectReference: ObjectReferenceTypeDef
    TypedLinkFacet: TypedLinkSchemaAndFacetNameTypeDef
    Attributes: Sequence[AttributeNameAndValueTypeDef]

class BatchAttachTypedLinkTypeDef(BaseValidatorModel):
    SourceObjectReference: ObjectReferenceTypeDef
    TargetObjectReference: ObjectReferenceTypeDef
    TypedLinkFacet: TypedLinkSchemaAndFacetNameTypeDef
    Attributes: Sequence[AttributeNameAndValueTypeDef]

class TypedLinkSpecifierTypeDef(BaseValidatorModel):
    TypedLinkFacet: TypedLinkSchemaAndFacetNameTypeDef
    SourceObjectReference: ObjectReferenceTypeDef
    TargetObjectReference: ObjectReferenceTypeDef
    IdentityAttributeValues: List[AttributeNameAndValueTypeDef]

class FacetAttributeTypeDef(BaseValidatorModel):
    Name: str
    AttributeDefinition: Optional[FacetAttributeDefinitionTypeDef] = None
    AttributeReference: Optional[FacetAttributeReferenceTypeDef] = None
    RequiredBehavior: Optional[RequiredAttributeBehaviorType] = None

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

class ListTypedLinkFacetAttributesResponseTypeDef(BaseValidatorModel):
    Attributes: List[TypedLinkAttributeDefinitionTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TypedLinkFacetAttributeUpdateTypeDef(BaseValidatorModel):
    Attribute: TypedLinkAttributeDefinitionTypeDef
    Action: UpdateActionTypeType

class TypedLinkFacetTypeDef(BaseValidatorModel):
    Name: str
    Attributes: Sequence[TypedLinkAttributeDefinitionTypeDef]
    IdentityAttributeOrder: Sequence[str]

class BatchListAttachedIndicesResponseTypeDef(BaseValidatorModel):
    IndexAttachments: Optional[List[IndexAttachmentTypeDef]] = None
    NextToken: Optional[str] = None

class BatchListIndexResponseTypeDef(BaseValidatorModel):
    IndexAttachments: Optional[List[IndexAttachmentTypeDef]] = None
    NextToken: Optional[str] = None

class ListAttachedIndicesResponseTypeDef(BaseValidatorModel):
    IndexAttachments: List[IndexAttachmentTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListIndexResponseTypeDef(BaseValidatorModel):
    IndexAttachments: List[IndexAttachmentTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AttachTypedLinkResponseTypeDef(BaseValidatorModel):
    TypedLinkSpecifier: TypedLinkSpecifierTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchAttachTypedLinkResponseTypeDef(BaseValidatorModel):
    TypedLinkSpecifier: Optional[TypedLinkSpecifierTypeDef] = None

class BatchDetachTypedLinkTypeDef(BaseValidatorModel):
    TypedLinkSpecifier: TypedLinkSpecifierTypeDef

class BatchGetLinkAttributesTypeDef(BaseValidatorModel):
    TypedLinkSpecifier: TypedLinkSpecifierTypeDef
    AttributeNames: Sequence[str]

class BatchListIncomingTypedLinksResponseTypeDef(BaseValidatorModel):
    LinkSpecifiers: Optional[List[TypedLinkSpecifierTypeDef]] = None
    NextToken: Optional[str] = None

class BatchListOutgoingTypedLinksResponseTypeDef(BaseValidatorModel):
    TypedLinkSpecifiers: Optional[List[TypedLinkSpecifierTypeDef]] = None
    NextToken: Optional[str] = None

class DetachTypedLinkRequestRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    TypedLinkSpecifier: TypedLinkSpecifierTypeDef

class GetLinkAttributesRequestRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    TypedLinkSpecifier: TypedLinkSpecifierTypeDef
    AttributeNames: Sequence[str]
    ConsistencyLevel: Optional[ConsistencyLevelType] = None

class ListIncomingTypedLinksResponseTypeDef(BaseValidatorModel):
    LinkSpecifiers: List[TypedLinkSpecifierTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListOutgoingTypedLinksResponseTypeDef(BaseValidatorModel):
    TypedLinkSpecifiers: List[TypedLinkSpecifierTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFacetRequestRequestTypeDef(BaseValidatorModel):
    SchemaArn: str
    Name: str
    Attributes: Optional[Sequence[FacetAttributeTypeDef]] = None
    ObjectType: Optional[ObjectTypeType] = None
    FacetStyle: Optional[FacetStyleType] = None

class FacetAttributeUpdateTypeDef(BaseValidatorModel):
    Attribute: Optional[FacetAttributeTypeDef] = None
    Action: Optional[UpdateActionTypeType] = None

class ListFacetAttributesResponseTypeDef(BaseValidatorModel):
    Attributes: List[FacetAttributeTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateLinkAttributesTypeDef(BaseValidatorModel):
    TypedLinkSpecifier: TypedLinkSpecifierTypeDef
    AttributeUpdates: Sequence[LinkAttributeUpdateTypeDef]

class UpdateLinkAttributesRequestRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    TypedLinkSpecifier: TypedLinkSpecifierTypeDef
    AttributeUpdates: Sequence[LinkAttributeUpdateTypeDef]

class BatchUpdateObjectAttributesTypeDef(BaseValidatorModel):
    ObjectReference: ObjectReferenceTypeDef
    AttributeUpdates: Sequence[ObjectAttributeUpdateTypeDef]

class UpdateObjectAttributesRequestRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    AttributeUpdates: Sequence[ObjectAttributeUpdateTypeDef]

class BatchListIndexTypeDef(BaseValidatorModel):
    IndexReference: ObjectReferenceTypeDef
    RangesOnIndexedValues: Optional[Sequence[ObjectAttributeRangeTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListIndexRequestRequestTypeDef(BaseValidatorModel):
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

class ListIncomingTypedLinksRequestRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    FilterAttributeRanges: Optional[Sequence[TypedLinkAttributeRangeTypeDef]] = None
    FilterTypedLink: Optional[TypedLinkSchemaAndFacetNameTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None

class ListOutgoingTypedLinksRequestRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    FilterAttributeRanges: Optional[Sequence[TypedLinkAttributeRangeTypeDef]] = None
    FilterTypedLink: Optional[TypedLinkSchemaAndFacetNameTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None

class UpdateTypedLinkFacetRequestRequestTypeDef(BaseValidatorModel):
    SchemaArn: str
    Name: str
    AttributeUpdates: Sequence[TypedLinkFacetAttributeUpdateTypeDef]
    IdentityAttributeOrder: Sequence[str]

class CreateTypedLinkFacetRequestRequestTypeDef(BaseValidatorModel):
    SchemaArn: str
    Facet: TypedLinkFacetTypeDef

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

class UpdateFacetRequestRequestTypeDef(BaseValidatorModel):
    SchemaArn: str
    Name: str
    AttributeUpdates: Optional[Sequence[FacetAttributeUpdateTypeDef]] = None
    ObjectType: Optional[ObjectTypeType] = None

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

class BatchWriteResponseTypeDef(BaseValidatorModel):
    Responses: List[BatchWriteOperationResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchReadOperationResponseTypeDef(BaseValidatorModel):
    SuccessfulResponse: Optional[BatchReadSuccessfulResponseTypeDef] = None
    ExceptionResponse: Optional[BatchReadExceptionTypeDef] = None

class BatchWriteRequestRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    Operations: Sequence[BatchWriteOperationTypeDef]

class BatchReadRequestRequestTypeDef(BaseValidatorModel):
    DirectoryArn: str
    Operations: Sequence[BatchReadOperationTypeDef]
    ConsistencyLevel: Optional[ConsistencyLevelType] = None

class BatchReadResponseTypeDef(BaseValidatorModel):
    Responses: List[BatchReadOperationResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

