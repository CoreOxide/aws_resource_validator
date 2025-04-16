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

class ObjectReference(BaseValidatorModel):
    Selector: Optional[str] = None


class SchemaFacet(BaseValidatorModel):
    SchemaArn: Optional[str] = None
    FacetName: Optional[str] = None


class ApplySchemaRequest(BaseValidatorModel):
    PublishedSchemaArn: str
    DirectoryArn: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class TypedLinkSchemaAndFacetName(BaseValidatorModel):
    SchemaArn: str
    TypedLinkName: str


class AttributeKey(BaseValidatorModel):
    SchemaArn: str
    FacetName: str
    Name: str


class TypedAttributeValueOutput(BaseValidatorModel):
    StringValue: Optional[str] = None
    BinaryValue: Optional[bytes] = None
    BooleanValue: Optional[bool] = None
    NumberValue: Optional[str] = None
    DatetimeValue: Optional[datetime] = None


class BatchAttachObjectResponse(BaseValidatorModel):
    attachedObjectIdentifier: Optional[str] = None


class BatchAttachToIndexResponse(BaseValidatorModel):
    AttachedObjectIdentifier: Optional[str] = None


class BatchCreateIndexResponse(BaseValidatorModel):
    ObjectIdentifier: Optional[str] = None


class BatchCreateObjectResponse(BaseValidatorModel):
    ObjectIdentifier: Optional[str] = None


class BatchDetachFromIndexResponse(BaseValidatorModel):
    DetachedObjectIdentifier: Optional[str] = None


class BatchDetachObjectResponse(BaseValidatorModel):
    detachedObjectIdentifier: Optional[str] = None


class BatchListObjectChildrenResponse(BaseValidatorModel):
    Children: Optional[Dict[str, str]] = None
    NextToken: Optional[str] = None


class PathToObjectIdentifiers(BaseValidatorModel):
    Path: Optional[str] = None
    ObjectIdentifiers: Optional[List[str]] = None


class ObjectIdentifierAndLinkNameTuple(BaseValidatorModel):
    ObjectIdentifier: Optional[str] = None
    LinkName: Optional[str] = None


class BatchListObjectPoliciesResponse(BaseValidatorModel):
    AttachedPolicyIds: Optional[List[str]] = None
    NextToken: Optional[str] = None


class BatchListPolicyAttachmentsResponse(BaseValidatorModel):
    ObjectIdentifiers: Optional[List[str]] = None
    NextToken: Optional[str] = None


class BatchUpdateObjectAttributesResponse(BaseValidatorModel):
    ObjectIdentifier: Optional[str] = None


class CreateDirectoryRequest(BaseValidatorModel):
    Name: str
    SchemaArn: str


class CreateSchemaRequest(BaseValidatorModel):
    Name: str


class DeleteDirectoryRequest(BaseValidatorModel):
    DirectoryArn: str


class DeleteFacetRequest(BaseValidatorModel):
    SchemaArn: str
    Name: str


class DeleteSchemaRequest(BaseValidatorModel):
    SchemaArn: str


class DeleteTypedLinkFacetRequest(BaseValidatorModel):
    SchemaArn: str
    Name: str


class Directory(BaseValidatorModel):
    Name: Optional[str] = None
    DirectoryArn: Optional[str] = None
    State: Optional[DirectoryStateType] = None
    CreationDateTime: Optional[datetime] = None


class DisableDirectoryRequest(BaseValidatorModel):
    DirectoryArn: str


class EnableDirectoryRequest(BaseValidatorModel):
    DirectoryArn: str


class FacetAttributeReference(BaseValidatorModel):
    TargetFacetName: str
    TargetAttributeName: str


class Facet(BaseValidatorModel):
    Name: Optional[str] = None
    ObjectType: Optional[ObjectTypeType] = None
    FacetStyle: Optional[FacetStyleType] = None


class GetAppliedSchemaVersionRequest(BaseValidatorModel):
    SchemaArn: str


class GetDirectoryRequest(BaseValidatorModel):
    DirectoryArn: str


class GetFacetRequest(BaseValidatorModel):
    SchemaArn: str
    Name: str


class GetSchemaAsJsonRequest(BaseValidatorModel):
    SchemaArn: str


class GetTypedLinkFacetInformationRequest(BaseValidatorModel):
    SchemaArn: str
    Name: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAppliedSchemaArnsRequest(BaseValidatorModel):
    DirectoryArn: str
    SchemaArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDevelopmentSchemaArnsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDirectoriesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    state: Optional[DirectoryStateType] = None


class ListFacetAttributesRequest(BaseValidatorModel):
    SchemaArn: str
    Name: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListFacetNamesRequest(BaseValidatorModel):
    SchemaArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListManagedSchemaArnsRequest(BaseValidatorModel):
    SchemaArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListPublishedSchemaArnsRequest(BaseValidatorModel):
    SchemaArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class Tag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class ListTypedLinkFacetAttributesRequest(BaseValidatorModel):
    SchemaArn: str
    Name: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTypedLinkFacetNamesRequest(BaseValidatorModel):
    SchemaArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PolicyAttachment(BaseValidatorModel):
    PolicyId: Optional[str] = None
    ObjectIdentifier: Optional[str] = None
    PolicyType: Optional[str] = None


class PublishSchemaRequest(BaseValidatorModel):
    DevelopmentSchemaArn: str
    Version: str
    MinorVersion: Optional[str] = None
    Name: Optional[str] = None


class PutSchemaFromJsonRequest(BaseValidatorModel):
    SchemaArn: str
    Document: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateSchemaRequest(BaseValidatorModel):
    SchemaArn: str
    Name: str


class UpgradeAppliedSchemaRequest(BaseValidatorModel):
    PublishedSchemaArn: str
    DirectoryArn: str
    DryRun: Optional[bool] = None


class UpgradePublishedSchemaRequest(BaseValidatorModel):
    DevelopmentSchemaArn: str
    PublishedSchemaArn: str
    MinorVersion: str
    DryRun: Optional[bool] = None


class AttachObjectRequest(BaseValidatorModel):
    DirectoryArn: str
    ParentReference: ObjectReference
    ChildReference: ObjectReference
    LinkName: str


class AttachPolicyRequest(BaseValidatorModel):
    DirectoryArn: str
    PolicyReference: ObjectReference
    ObjectReference: ObjectReference


class AttachToIndexRequest(BaseValidatorModel):
    DirectoryArn: str
    IndexReference: ObjectReference
    TargetReference: ObjectReference


class BatchAttachObject(BaseValidatorModel):
    ParentReference: ObjectReference
    ChildReference: ObjectReference
    LinkName: str


class BatchAttachPolicy(BaseValidatorModel):
    PolicyReference: ObjectReference
    ObjectReference: ObjectReference


class BatchAttachToIndex(BaseValidatorModel):
    IndexReference: ObjectReference
    TargetReference: ObjectReference


class BatchDeleteObject(BaseValidatorModel):
    ObjectReference: ObjectReference


class BatchDetachFromIndex(BaseValidatorModel):
    IndexReference: ObjectReference
    TargetReference: ObjectReference


class BatchDetachObject(BaseValidatorModel):
    ParentReference: ObjectReference
    LinkName: str
    BatchReferenceName: Optional[str] = None


class BatchDetachPolicy(BaseValidatorModel):
    PolicyReference: ObjectReference
    ObjectReference: ObjectReference


class BatchGetObjectInformation(BaseValidatorModel):
    ObjectReference: ObjectReference


class BatchListAttachedIndices(BaseValidatorModel):
    TargetReference: ObjectReference
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class BatchListObjectChildren(BaseValidatorModel):
    ObjectReference: ObjectReference
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class BatchListObjectParentPaths(BaseValidatorModel):
    ObjectReference: ObjectReference
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class BatchListObjectParents(BaseValidatorModel):
    ObjectReference: ObjectReference
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class BatchListObjectPolicies(BaseValidatorModel):
    ObjectReference: ObjectReference
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class BatchListPolicyAttachments(BaseValidatorModel):
    PolicyReference: ObjectReference
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class BatchLookupPolicy(BaseValidatorModel):
    ObjectReference: ObjectReference
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DeleteObjectRequest(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReference


class DetachFromIndexRequest(BaseValidatorModel):
    DirectoryArn: str
    IndexReference: ObjectReference
    TargetReference: ObjectReference


class DetachObjectRequest(BaseValidatorModel):
    DirectoryArn: str
    ParentReference: ObjectReference
    LinkName: str


class DetachPolicyRequest(BaseValidatorModel):
    DirectoryArn: str
    PolicyReference: ObjectReference
    ObjectReference: ObjectReference


class GetObjectInformationRequest(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReference
    ConsistencyLevel: Optional[ConsistencyLevelType] = None


class ListAttachedIndicesRequest(BaseValidatorModel):
    DirectoryArn: str
    TargetReference: ObjectReference
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None


class ListObjectChildrenRequest(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReference
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None


class ListObjectParentPathsRequest(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReference
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListObjectParentsRequest(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReference
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    IncludeAllLinksToEachParent: Optional[bool] = None


class ListObjectPoliciesRequest(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReference
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None


class ListPolicyAttachmentsRequest(BaseValidatorModel):
    DirectoryArn: str
    PolicyReference: ObjectReference
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None


class LookupPolicyRequest(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReference
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class BatchGetObjectAttributes(BaseValidatorModel):
    ObjectReference: ObjectReference
    SchemaFacet: SchemaFacet
    AttributeNames: Sequence[str]


class BatchGetObjectInformationResponse(BaseValidatorModel):
    SchemaFacets: Optional[List[SchemaFacet]] = None
    ObjectIdentifier: Optional[str] = None


class BatchListObjectAttributes(BaseValidatorModel):
    ObjectReference: ObjectReference
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    FacetFilter: Optional[SchemaFacet] = None


class BatchRemoveFacetFromObject(BaseValidatorModel):
    SchemaFacet: SchemaFacet
    ObjectReference: ObjectReference


class GetObjectAttributesRequest(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReference
    SchemaFacet: SchemaFacet
    AttributeNames: Sequence[str]
    ConsistencyLevel: Optional[ConsistencyLevelType] = None


class ListObjectAttributesRequest(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReference
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    FacetFilter: Optional[SchemaFacet] = None


class RemoveFacetFromObjectRequest(BaseValidatorModel):
    DirectoryArn: str
    SchemaFacet: SchemaFacet
    ObjectReference: ObjectReference


class ApplySchemaResponse(BaseValidatorModel):
    AppliedSchemaArn: str
    DirectoryArn: str
    ResponseMetadata: ResponseMetadata


class AttachObjectResponse(BaseValidatorModel):
    AttachedObjectIdentifier: str
    ResponseMetadata: ResponseMetadata


class AttachToIndexResponse(BaseValidatorModel):
    AttachedObjectIdentifier: str
    ResponseMetadata: ResponseMetadata


class CreateDirectoryResponse(BaseValidatorModel):
    DirectoryArn: str
    Name: str
    ObjectIdentifier: str
    AppliedSchemaArn: str
    ResponseMetadata: ResponseMetadata


class CreateIndexResponse(BaseValidatorModel):
    ObjectIdentifier: str
    ResponseMetadata: ResponseMetadata


class CreateObjectResponse(BaseValidatorModel):
    ObjectIdentifier: str
    ResponseMetadata: ResponseMetadata


class CreateSchemaResponse(BaseValidatorModel):
    SchemaArn: str
    ResponseMetadata: ResponseMetadata


class DeleteDirectoryResponse(BaseValidatorModel):
    DirectoryArn: str
    ResponseMetadata: ResponseMetadata


class DeleteSchemaResponse(BaseValidatorModel):
    SchemaArn: str
    ResponseMetadata: ResponseMetadata


class DetachFromIndexResponse(BaseValidatorModel):
    DetachedObjectIdentifier: str
    ResponseMetadata: ResponseMetadata


class DetachObjectResponse(BaseValidatorModel):
    DetachedObjectIdentifier: str
    ResponseMetadata: ResponseMetadata


class DisableDirectoryResponse(BaseValidatorModel):
    DirectoryArn: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class EnableDirectoryResponse(BaseValidatorModel):
    DirectoryArn: str
    ResponseMetadata: ResponseMetadata


class GetAppliedSchemaVersionResponse(BaseValidatorModel):
    AppliedSchemaArn: str
    ResponseMetadata: ResponseMetadata


class GetObjectInformationResponse(BaseValidatorModel):
    SchemaFacets: List[SchemaFacet]
    ObjectIdentifier: str
    ResponseMetadata: ResponseMetadata


class GetSchemaAsJsonResponse(BaseValidatorModel):
    Name: str
    Document: str
    ResponseMetadata: ResponseMetadata


class GetTypedLinkFacetInformationResponse(BaseValidatorModel):
    IdentityAttributeOrder: List[str]
    ResponseMetadata: ResponseMetadata


class ListAppliedSchemaArnsResponse(BaseValidatorModel):
    SchemaArns: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListDevelopmentSchemaArnsResponse(BaseValidatorModel):
    SchemaArns: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListFacetNamesResponse(BaseValidatorModel):
    FacetNames: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListManagedSchemaArnsResponse(BaseValidatorModel):
    SchemaArns: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListObjectChildrenResponse(BaseValidatorModel):
    Children: Dict[str, str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListObjectPoliciesResponse(BaseValidatorModel):
    AttachedPolicyIds: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListPolicyAttachmentsResponse(BaseValidatorModel):
    ObjectIdentifiers: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListPublishedSchemaArnsResponse(BaseValidatorModel):
    SchemaArns: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTypedLinkFacetNamesResponse(BaseValidatorModel):
    FacetNames: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PublishSchemaResponse(BaseValidatorModel):
    PublishedSchemaArn: str
    ResponseMetadata: ResponseMetadata


class PutSchemaFromJsonResponse(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


class UpdateObjectAttributesResponse(BaseValidatorModel):
    ObjectIdentifier: str
    ResponseMetadata: ResponseMetadata


class UpdateSchemaResponse(BaseValidatorModel):
    SchemaArn: str
    ResponseMetadata: ResponseMetadata


class UpgradeAppliedSchemaResponse(BaseValidatorModel):
    UpgradedSchemaArn: str
    DirectoryArn: str
    ResponseMetadata: ResponseMetadata


class UpgradePublishedSchemaResponse(BaseValidatorModel):
    UpgradedSchemaArn: str
    ResponseMetadata: ResponseMetadata


class BatchCreateIndex(BaseValidatorModel):
    OrderedIndexedAttributeList: Sequence[AttributeKey]
    IsUnique: bool
    ParentReference: Optional[ObjectReference] = None
    LinkName: Optional[str] = None
    BatchReferenceName: Optional[str] = None


class CreateIndexRequest(BaseValidatorModel):
    DirectoryArn: str
    OrderedIndexedAttributeList: Sequence[AttributeKey]
    IsUnique: bool
    ParentReference: Optional[ObjectReference] = None
    LinkName: Optional[str] = None


class AttributeKeyAndValueOutput(BaseValidatorModel):
    Key: AttributeKey
    Value: TypedAttributeValueOutput


class AttributeNameAndValueOutput(BaseValidatorModel):
    AttributeName: str
    Value: TypedAttributeValueOutput


class BatchListObjectParentPathsResponse(BaseValidatorModel):
    PathToObjectIdentifiersList: Optional[List[PathToObjectIdentifiers]] = None
    NextToken: Optional[str] = None


class ListObjectParentPathsResponse(BaseValidatorModel):
    PathToObjectIdentifiersList: List[PathToObjectIdentifiers]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class BatchListObjectParentsResponse(BaseValidatorModel):
    ParentLinks: Optional[List[ObjectIdentifierAndLinkNameTuple]] = None
    NextToken: Optional[str] = None


class ListObjectParentsResponse(BaseValidatorModel):
    Parents: Dict[str, str]
    ParentLinks: List[ObjectIdentifierAndLinkNameTuple]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetDirectoryResponse(BaseValidatorModel):
    Directory: Directory
    ResponseMetadata: ResponseMetadata


class ListDirectoriesResponse(BaseValidatorModel):
    Directories: List[Directory]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetFacetResponse(BaseValidatorModel):
    Facet: Facet
    ResponseMetadata: ResponseMetadata


class ListAppliedSchemaArnsRequestPaginate(BaseValidatorModel):
    DirectoryArn: str
    SchemaArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAttachedIndicesRequestPaginate(BaseValidatorModel):
    DirectoryArn: str
    TargetReference: ObjectReference
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDevelopmentSchemaArnsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDirectoriesRequestPaginate(BaseValidatorModel):
    state: Optional[DirectoryStateType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFacetAttributesRequestPaginate(BaseValidatorModel):
    SchemaArn: str
    Name: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFacetNamesRequestPaginate(BaseValidatorModel):
    SchemaArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListManagedSchemaArnsRequestPaginate(BaseValidatorModel):
    SchemaArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListObjectAttributesRequestPaginate(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReference
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    FacetFilter: Optional[SchemaFacet] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListObjectParentPathsRequestPaginate(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReference
    PaginationConfig: Optional[PaginatorConfig] = None


class ListObjectPoliciesRequestPaginate(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReference
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPolicyAttachmentsRequestPaginate(BaseValidatorModel):
    DirectoryArn: str
    PolicyReference: ObjectReference
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPublishedSchemaArnsRequestPaginate(BaseValidatorModel):
    SchemaArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsForResourceRequestPaginate(BaseValidatorModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTypedLinkFacetAttributesRequestPaginate(BaseValidatorModel):
    SchemaArn: str
    Name: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTypedLinkFacetNamesRequestPaginate(BaseValidatorModel):
    SchemaArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class LookupPolicyRequestPaginate(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReference
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[Tag]


class PolicyToPath(BaseValidatorModel):
    Path: Optional[str] = None
    Policies: Optional[List[PolicyAttachment]] = None


class Timestamp(BaseValidatorModel):
    pass


class Blob(BaseValidatorModel):
    pass


class TypedAttributeValue(BaseValidatorModel):
    StringValue: Optional[str] = None
    BinaryValue: Optional[Blob] = None
    BooleanValue: Optional[bool] = None
    NumberValue: Optional[str] = None
    DatetimeValue: Optional[Timestamp] = None


class BatchGetLinkAttributesResponse(BaseValidatorModel):
    Attributes: Optional[List[AttributeKeyAndValueOutput]] = None


class BatchGetObjectAttributesResponse(BaseValidatorModel):
    Attributes: Optional[List[AttributeKeyAndValueOutput]] = None


class BatchListObjectAttributesResponse(BaseValidatorModel):
    Attributes: Optional[List[AttributeKeyAndValueOutput]] = None
    NextToken: Optional[str] = None


class GetLinkAttributesResponse(BaseValidatorModel):
    Attributes: List[AttributeKeyAndValueOutput]
    ResponseMetadata: ResponseMetadata


class GetObjectAttributesResponse(BaseValidatorModel):
    Attributes: List[AttributeKeyAndValueOutput]
    ResponseMetadata: ResponseMetadata


class IndexAttachment(BaseValidatorModel):
    IndexedAttributes: Optional[List[AttributeKeyAndValueOutput]] = None
    ObjectIdentifier: Optional[str] = None


class ListObjectAttributesResponse(BaseValidatorModel):
    Attributes: List[AttributeKeyAndValueOutput]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TypedLinkSpecifierOutput(BaseValidatorModel):
    TypedLinkFacet: TypedLinkSchemaAndFacetName
    SourceObjectReference: ObjectReference
    TargetObjectReference: ObjectReference
    IdentityAttributeValues: List[AttributeNameAndValueOutput]


class FacetAttributeDefinitionOutput(BaseValidatorModel):
    pass


class FacetAttributeOutput(BaseValidatorModel):
    Name: str
    AttributeDefinition: Optional[FacetAttributeDefinitionOutput] = None
    AttributeReference: Optional[FacetAttributeReference] = None
    RequiredBehavior: Optional[RequiredAttributeBehaviorType] = None


class TypedLinkAttributeDefinitionOutput(BaseValidatorModel):
    pass


class ListTypedLinkFacetAttributesResponse(BaseValidatorModel):
    Attributes: List[TypedLinkAttributeDefinitionOutput]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class BatchLookupPolicyResponse(BaseValidatorModel):
    PolicyToPathList: Optional[List[PolicyToPath]] = None
    NextToken: Optional[str] = None


class LookupPolicyResponse(BaseValidatorModel):
    PolicyToPathList: List[PolicyToPath]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class BatchListAttachedIndicesResponse(BaseValidatorModel):
    IndexAttachments: Optional[List[IndexAttachment]] = None
    NextToken: Optional[str] = None


class BatchListIndexResponse(BaseValidatorModel):
    IndexAttachments: Optional[List[IndexAttachment]] = None
    NextToken: Optional[str] = None


class ListAttachedIndicesResponse(BaseValidatorModel):
    IndexAttachments: List[IndexAttachment]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListIndexResponse(BaseValidatorModel):
    IndexAttachments: List[IndexAttachment]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AttachTypedLinkResponse(BaseValidatorModel):
    TypedLinkSpecifier: TypedLinkSpecifierOutput
    ResponseMetadata: ResponseMetadata


class BatchAttachTypedLinkResponse(BaseValidatorModel):
    TypedLinkSpecifier: Optional[TypedLinkSpecifierOutput] = None


class BatchListIncomingTypedLinksResponse(BaseValidatorModel):
    LinkSpecifiers: Optional[List[TypedLinkSpecifierOutput]] = None
    NextToken: Optional[str] = None


class BatchListOutgoingTypedLinksResponse(BaseValidatorModel):
    TypedLinkSpecifiers: Optional[List[TypedLinkSpecifierOutput]] = None
    NextToken: Optional[str] = None


class ListIncomingTypedLinksResponse(BaseValidatorModel):
    LinkSpecifiers: List[TypedLinkSpecifierOutput]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListOutgoingTypedLinksResponse(BaseValidatorModel):
    TypedLinkSpecifiers: List[TypedLinkSpecifierOutput]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListFacetAttributesResponse(BaseValidatorModel):
    Attributes: List[FacetAttributeOutput]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TypedAttributeValueUnion(BaseValidatorModel):
    pass


class AttributeKeyAndValue(BaseValidatorModel):
    Key: AttributeKey
    Value: TypedAttributeValueUnion


class AttributeNameAndValue(BaseValidatorModel):
    AttributeName: str
    Value: TypedAttributeValueUnion


class LinkAttributeAction(BaseValidatorModel):
    AttributeActionType: Optional[UpdateActionTypeType] = None
    AttributeUpdateValue: Optional[TypedAttributeValueUnion] = None


class ObjectAttributeAction(BaseValidatorModel):
    ObjectAttributeActionType: Optional[UpdateActionTypeType] = None
    ObjectAttributeUpdateValue: Optional[TypedAttributeValueUnion] = None


class TypedAttributeValueRange(BaseValidatorModel):
    StartMode: RangeModeType
    EndMode: RangeModeType
    StartValue: Optional[TypedAttributeValueUnion] = None
    EndValue: Optional[TypedAttributeValueUnion] = None


class BatchWriteOperationResponse(BaseValidatorModel):
    CreateObject: Optional[BatchCreateObjectResponse] = None
    AttachObject: Optional[BatchAttachObjectResponse] = None
    DetachObject: Optional[BatchDetachObjectResponse] = None
    UpdateObjectAttributes: Optional[BatchUpdateObjectAttributesResponse] = None
    DeleteObject: Optional[Dict[str, Any]] = None
    AddFacetToObject: Optional[Dict[str, Any]] = None
    RemoveFacetFromObject: Optional[Dict[str, Any]] = None
    AttachPolicy: Optional[Dict[str, Any]] = None
    DetachPolicy: Optional[Dict[str, Any]] = None
    CreateIndex: Optional[BatchCreateIndexResponse] = None
    AttachToIndex: Optional[BatchAttachToIndexResponse] = None
    DetachFromIndex: Optional[BatchDetachFromIndexResponse] = None
    AttachTypedLink: Optional[BatchAttachTypedLinkResponse] = None
    DetachTypedLink: Optional[Dict[str, Any]] = None
    UpdateLinkAttributes: Optional[Dict[str, Any]] = None


class BatchReadSuccessfulResponse(BaseValidatorModel):
    ListObjectAttributes: Optional[BatchListObjectAttributesResponse] = None
    ListObjectChildren: Optional[BatchListObjectChildrenResponse] = None
    GetObjectInformation: Optional[BatchGetObjectInformationResponse] = None
    GetObjectAttributes: Optional[BatchGetObjectAttributesResponse] = None
    ListAttachedIndices: Optional[BatchListAttachedIndicesResponse] = None
    ListObjectParentPaths: Optional[BatchListObjectParentPathsResponse] = None
    ListObjectPolicies: Optional[BatchListObjectPoliciesResponse] = None
    ListPolicyAttachments: Optional[BatchListPolicyAttachmentsResponse] = None
    LookupPolicy: Optional[BatchLookupPolicyResponse] = None
    ListIndex: Optional[BatchListIndexResponse] = None
    ListOutgoingTypedLinks: Optional[BatchListOutgoingTypedLinksResponse] = None
    ListIncomingTypedLinks: Optional[BatchListIncomingTypedLinksResponse] = None
    GetLinkAttributes: Optional[BatchGetLinkAttributesResponse] = None
    ListObjectParents: Optional[BatchListObjectParentsResponse] = None


class BatchCreateObject(BaseValidatorModel):
    SchemaFacet: Sequence[SchemaFacet]
    ObjectAttributeList: Sequence[AttributeKeyAndValue]
    ParentReference: Optional[ObjectReference] = None
    LinkName: Optional[str] = None
    BatchReferenceName: Optional[str] = None


class LinkAttributeUpdate(BaseValidatorModel):
    AttributeKey: Optional[AttributeKey] = None
    AttributeAction: Optional[LinkAttributeAction] = None


class ObjectAttributeUpdate(BaseValidatorModel):
    ObjectAttributeKey: Optional[AttributeKey] = None
    ObjectAttributeAction: Optional[ObjectAttributeAction] = None


class ObjectAttributeRange(BaseValidatorModel):
    AttributeKey: Optional[AttributeKey] = None
    Range: Optional[TypedAttributeValueRange] = None


class TypedLinkAttributeRange(BaseValidatorModel):
    Range: TypedAttributeValueRange
    AttributeName: Optional[str] = None


class BatchWriteResponse(BaseValidatorModel):
    Responses: List[BatchWriteOperationResponse]
    ResponseMetadata: ResponseMetadata


class BatchReadException(BaseValidatorModel):
    pass


class BatchReadOperationResponse(BaseValidatorModel):
    SuccessfulResponse: Optional[BatchReadSuccessfulResponse] = None
    ExceptionResponse: Optional[BatchReadException] = None


class AttributeKeyAndValueUnion(BaseValidatorModel):
    pass


class AddFacetToObjectRequest(BaseValidatorModel):
    DirectoryArn: str
    SchemaFacet: SchemaFacet
    ObjectReference: ObjectReference
    ObjectAttributeList: Optional[Sequence[AttributeKeyAndValueUnion]] = None


class BatchAddFacetToObject(BaseValidatorModel):
    SchemaFacet: SchemaFacet
    ObjectAttributeList: Sequence[AttributeKeyAndValueUnion]
    ObjectReference: ObjectReference


class CreateObjectRequest(BaseValidatorModel):
    DirectoryArn: str
    SchemaFacets: Sequence[SchemaFacet]
    ObjectAttributeList: Optional[Sequence[AttributeKeyAndValueUnion]] = None
    ParentReference: Optional[ObjectReference] = None
    LinkName: Optional[str] = None


class AttributeNameAndValueUnion(BaseValidatorModel):
    pass


class AttachTypedLinkRequest(BaseValidatorModel):
    DirectoryArn: str
    SourceObjectReference: ObjectReference
    TargetObjectReference: ObjectReference
    TypedLinkFacet: TypedLinkSchemaAndFacetName
    Attributes: Sequence[AttributeNameAndValueUnion]


class BatchAttachTypedLink(BaseValidatorModel):
    SourceObjectReference: ObjectReference
    TargetObjectReference: ObjectReference
    TypedLinkFacet: TypedLinkSchemaAndFacetName
    Attributes: Sequence[AttributeNameAndValueUnion]


class TypedLinkSpecifier(BaseValidatorModel):
    TypedLinkFacet: TypedLinkSchemaAndFacetName
    SourceObjectReference: ObjectReference
    TargetObjectReference: ObjectReference
    IdentityAttributeValues: Sequence[AttributeNameAndValueUnion]


class FacetAttributeDefinitionUnion(BaseValidatorModel):
    pass


class FacetAttribute(BaseValidatorModel):
    Name: str
    AttributeDefinition: Optional[FacetAttributeDefinitionUnion] = None
    AttributeReference: Optional[FacetAttributeReference] = None
    RequiredBehavior: Optional[RequiredAttributeBehaviorType] = None


class BatchUpdateObjectAttributes(BaseValidatorModel):
    ObjectReference: ObjectReference
    AttributeUpdates: Sequence[ObjectAttributeUpdate]


class UpdateObjectAttributesRequest(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReference
    AttributeUpdates: Sequence[ObjectAttributeUpdate]


class BatchListIndex(BaseValidatorModel):
    IndexReference: ObjectReference
    RangesOnIndexedValues: Optional[Sequence[ObjectAttributeRange]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListIndexRequestPaginate(BaseValidatorModel):
    DirectoryArn: str
    IndexReference: ObjectReference
    RangesOnIndexedValues: Optional[Sequence[ObjectAttributeRange]] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListIndexRequest(BaseValidatorModel):
    DirectoryArn: str
    IndexReference: ObjectReference
    RangesOnIndexedValues: Optional[Sequence[ObjectAttributeRange]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None


class BatchListIncomingTypedLinks(BaseValidatorModel):
    ObjectReference: ObjectReference
    FilterAttributeRanges: Optional[Sequence[TypedLinkAttributeRange]] = None
    FilterTypedLink: Optional[TypedLinkSchemaAndFacetName] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class BatchListOutgoingTypedLinks(BaseValidatorModel):
    ObjectReference: ObjectReference
    FilterAttributeRanges: Optional[Sequence[TypedLinkAttributeRange]] = None
    FilterTypedLink: Optional[TypedLinkSchemaAndFacetName] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListIncomingTypedLinksRequestPaginate(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReference
    FilterAttributeRanges: Optional[Sequence[TypedLinkAttributeRange]] = None
    FilterTypedLink: Optional[TypedLinkSchemaAndFacetName] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListIncomingTypedLinksRequest(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReference
    FilterAttributeRanges: Optional[Sequence[TypedLinkAttributeRange]] = None
    FilterTypedLink: Optional[TypedLinkSchemaAndFacetName] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None


class ListOutgoingTypedLinksRequestPaginate(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReference
    FilterAttributeRanges: Optional[Sequence[TypedLinkAttributeRange]] = None
    FilterTypedLink: Optional[TypedLinkSchemaAndFacetName] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOutgoingTypedLinksRequest(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReference
    FilterAttributeRanges: Optional[Sequence[TypedLinkAttributeRange]] = None
    FilterTypedLink: Optional[TypedLinkSchemaAndFacetName] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None


class TypedLinkAttributeDefinitionUnion(BaseValidatorModel):
    pass


class TypedLinkFacetAttributeUpdate(BaseValidatorModel):
    Attribute: TypedLinkAttributeDefinitionUnion
    Action: UpdateActionTypeType


class TypedLinkFacet(BaseValidatorModel):
    Name: str
    Attributes: Sequence[TypedLinkAttributeDefinitionUnion]
    IdentityAttributeOrder: Sequence[str]


class BatchReadResponse(BaseValidatorModel):
    Responses: List[BatchReadOperationResponse]
    ResponseMetadata: ResponseMetadata


class UpdateTypedLinkFacetRequest(BaseValidatorModel):
    SchemaArn: str
    Name: str
    AttributeUpdates: Sequence[TypedLinkFacetAttributeUpdate]
    IdentityAttributeOrder: Sequence[str]


class CreateTypedLinkFacetRequest(BaseValidatorModel):
    SchemaArn: str
    Facet: TypedLinkFacet


class TypedLinkSpecifierUnion(BaseValidatorModel):
    pass


class BatchDetachTypedLink(BaseValidatorModel):
    TypedLinkSpecifier: TypedLinkSpecifierUnion


class BatchGetLinkAttributes(BaseValidatorModel):
    TypedLinkSpecifier: TypedLinkSpecifierUnion
    AttributeNames: Sequence[str]


class BatchUpdateLinkAttributes(BaseValidatorModel):
    TypedLinkSpecifier: TypedLinkSpecifierUnion
    AttributeUpdates: Sequence[LinkAttributeUpdate]


class DetachTypedLinkRequest(BaseValidatorModel):
    DirectoryArn: str
    TypedLinkSpecifier: TypedLinkSpecifierUnion


class GetLinkAttributesRequest(BaseValidatorModel):
    DirectoryArn: str
    TypedLinkSpecifier: TypedLinkSpecifierUnion
    AttributeNames: Sequence[str]
    ConsistencyLevel: Optional[ConsistencyLevelType] = None


class UpdateLinkAttributesRequest(BaseValidatorModel):
    DirectoryArn: str
    TypedLinkSpecifier: TypedLinkSpecifierUnion
    AttributeUpdates: Sequence[LinkAttributeUpdate]


class FacetAttributeUnion(BaseValidatorModel):
    pass


class CreateFacetRequest(BaseValidatorModel):
    SchemaArn: str
    Name: str
    Attributes: Optional[Sequence[FacetAttributeUnion]] = None
    ObjectType: Optional[ObjectTypeType] = None
    FacetStyle: Optional[FacetStyleType] = None


class FacetAttributeUpdate(BaseValidatorModel):
    Attribute: Optional[FacetAttributeUnion] = None
    Action: Optional[UpdateActionTypeType] = None


class BatchReadOperation(BaseValidatorModel):
    ListObjectAttributes: Optional[BatchListObjectAttributes] = None
    ListObjectChildren: Optional[BatchListObjectChildren] = None
    ListAttachedIndices: Optional[BatchListAttachedIndices] = None
    ListObjectParentPaths: Optional[BatchListObjectParentPaths] = None
    GetObjectInformation: Optional[BatchGetObjectInformation] = None
    GetObjectAttributes: Optional[BatchGetObjectAttributes] = None
    ListObjectParents: Optional[BatchListObjectParents] = None
    ListObjectPolicies: Optional[BatchListObjectPolicies] = None
    ListPolicyAttachments: Optional[BatchListPolicyAttachments] = None
    LookupPolicy: Optional[BatchLookupPolicy] = None
    ListIndex: Optional[BatchListIndex] = None
    ListOutgoingTypedLinks: Optional[BatchListOutgoingTypedLinks] = None
    ListIncomingTypedLinks: Optional[BatchListIncomingTypedLinks] = None
    GetLinkAttributes: Optional[BatchGetLinkAttributes] = None


class BatchWriteOperation(BaseValidatorModel):
    CreateObject: Optional[BatchCreateObject] = None
    AttachObject: Optional[BatchAttachObject] = None
    DetachObject: Optional[BatchDetachObject] = None
    UpdateObjectAttributes: Optional[BatchUpdateObjectAttributes] = None
    DeleteObject: Optional[BatchDeleteObject] = None
    AddFacetToObject: Optional[BatchAddFacetToObject] = None
    RemoveFacetFromObject: Optional[BatchRemoveFacetFromObject] = None
    AttachPolicy: Optional[BatchAttachPolicy] = None
    DetachPolicy: Optional[BatchDetachPolicy] = None
    CreateIndex: Optional[BatchCreateIndex] = None
    AttachToIndex: Optional[BatchAttachToIndex] = None
    DetachFromIndex: Optional[BatchDetachFromIndex] = None
    AttachTypedLink: Optional[BatchAttachTypedLink] = None
    DetachTypedLink: Optional[BatchDetachTypedLink] = None
    UpdateLinkAttributes: Optional[BatchUpdateLinkAttributes] = None


class UpdateFacetRequest(BaseValidatorModel):
    SchemaArn: str
    Name: str
    AttributeUpdates: Optional[Sequence[FacetAttributeUpdate]] = None
    ObjectType: Optional[ObjectTypeType] = None


class BatchReadRequest(BaseValidatorModel):
    DirectoryArn: str
    Operations: Sequence[BatchReadOperation]
    ConsistencyLevel: Optional[ConsistencyLevelType] = None


class BatchWriteRequest(BaseValidatorModel):
    DirectoryArn: str
    Operations: Sequence[BatchWriteOperation]


