from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.clouddirectory.clouddirectory_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ObjectReference(BaseValidatorModel):
    Selector: Optional[str] = None


class SchemaFacet(BaseValidatorModel):
    SchemaArn: Optional[str] = None
    FacetName: Optional[str] = None


# This class is the input for the 'apply_schema' function.
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


class BatchReadException(BaseValidatorModel):
    Type: Optional[BatchReadExceptionTypeType] = None
    Message: Optional[str] = None


class BatchUpdateObjectAttributesResponse(BaseValidatorModel):
    ObjectIdentifier: Optional[str] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


# This class is the input for the 'create_directory' function.
class CreateDirectoryRequest(BaseValidatorModel):
    Name: str
    SchemaArn: str


# This class is the input for the 'create_schema' function.
class CreateSchemaRequest(BaseValidatorModel):
    Name: str


# This class is the input for the 'delete_directory' function.
class DeleteDirectoryRequest(BaseValidatorModel):
    DirectoryArn: str


class DeleteFacetRequest(BaseValidatorModel):
    SchemaArn: str
    Name: str


# This class is the input for the 'delete_schema' function.
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


# This class is the input for the 'disable_directory' function.
class DisableDirectoryRequest(BaseValidatorModel):
    DirectoryArn: str


# This class is the input for the 'enable_directory' function.
class EnableDirectoryRequest(BaseValidatorModel):
    DirectoryArn: str


class RuleOutput(BaseValidatorModel):
    Type: Optional[RuleTypeType] = None
    Parameters: Optional[Dict[str, str]] = None


class FacetAttributeReference(BaseValidatorModel):
    TargetFacetName: str
    TargetAttributeName: str


class Facet(BaseValidatorModel):
    Name: Optional[str] = None
    ObjectType: Optional[ObjectTypeType] = None
    FacetStyle: Optional[FacetStyleType] = None


# This class is the input for the 'get_applied_schema_version' function.
class GetAppliedSchemaVersionRequest(BaseValidatorModel):
    SchemaArn: str


# This class is the input for the 'get_directory' function.
class GetDirectoryRequest(BaseValidatorModel):
    DirectoryArn: str


# This class is the input for the 'get_facet' function.
class GetFacetRequest(BaseValidatorModel):
    SchemaArn: str
    Name: str


# This class is the input for the 'get_schema_as_json' function.
class GetSchemaAsJsonRequest(BaseValidatorModel):
    SchemaArn: str


# This class is the input for the 'get_typed_link_facet_information' function.
class GetTypedLinkFacetInformationRequest(BaseValidatorModel):
    SchemaArn: str
    Name: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_applied_schema_arns' function.
class ListAppliedSchemaArnsRequest(BaseValidatorModel):
    DirectoryArn: str
    SchemaArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_development_schema_arns' function.
class ListDevelopmentSchemaArnsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_directories' function.
class ListDirectoriesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    state: Optional[DirectoryStateType] = None


# This class is the input for the 'list_facet_attributes' function.
class ListFacetAttributesRequest(BaseValidatorModel):
    SchemaArn: str
    Name: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_facet_names' function.
class ListFacetNamesRequest(BaseValidatorModel):
    SchemaArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_managed_schema_arns' function.
class ListManagedSchemaArnsRequest(BaseValidatorModel):
    SchemaArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_published_schema_arns' function.
class ListPublishedSchemaArnsRequest(BaseValidatorModel):
    SchemaArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class Tag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


# This class is the input for the 'list_typed_link_facet_attributes' function.
class ListTypedLinkFacetAttributesRequest(BaseValidatorModel):
    SchemaArn: str
    Name: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_typed_link_facet_names' function.
class ListTypedLinkFacetNamesRequest(BaseValidatorModel):
    SchemaArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PolicyAttachment(BaseValidatorModel):
    PolicyId: Optional[str] = None
    ObjectIdentifier: Optional[str] = None
    PolicyType: Optional[str] = None


# This class is the input for the 'publish_schema' function.
class PublishSchemaRequest(BaseValidatorModel):
    DevelopmentSchemaArn: str
    Version: str
    MinorVersion: Optional[str] = None
    Name: Optional[str] = None


# This class is the input for the 'put_schema_from_json' function.
class PutSchemaFromJsonRequest(BaseValidatorModel):
    SchemaArn: str
    Document: str


class Rule(BaseValidatorModel):
    Type: Optional[RuleTypeType] = None
    Parameters: Optional[Dict[str, str]] = None

Timestamp = Union[datetime, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


# This class is the input for the 'update_schema' function.
class UpdateSchemaRequest(BaseValidatorModel):
    SchemaArn: str
    Name: str


# This class is the input for the 'upgrade_applied_schema' function.
class UpgradeAppliedSchemaRequest(BaseValidatorModel):
    PublishedSchemaArn: str
    DirectoryArn: str
    DryRun: Optional[bool] = None


# This class is the input for the 'upgrade_published_schema' function.
class UpgradePublishedSchemaRequest(BaseValidatorModel):
    DevelopmentSchemaArn: str
    PublishedSchemaArn: str
    MinorVersion: str
    DryRun: Optional[bool] = None


# This class is the input for the 'attach_object' function.
class AttachObjectRequest(BaseValidatorModel):
    DirectoryArn: str
    ParentReference: ObjectReference
    ChildReference: ObjectReference
    LinkName: str


class AttachPolicyRequest(BaseValidatorModel):
    DirectoryArn: str
    PolicyReference: ObjectReference
    ObjectReference: ObjectReference


# This class is the input for the 'attach_to_index' function.
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


# This class is the input for the 'detach_from_index' function.
class DetachFromIndexRequest(BaseValidatorModel):
    DirectoryArn: str
    IndexReference: ObjectReference
    TargetReference: ObjectReference


# This class is the input for the 'detach_object' function.
class DetachObjectRequest(BaseValidatorModel):
    DirectoryArn: str
    ParentReference: ObjectReference
    LinkName: str


class DetachPolicyRequest(BaseValidatorModel):
    DirectoryArn: str
    PolicyReference: ObjectReference
    ObjectReference: ObjectReference


# This class is the input for the 'get_object_information' function.
class GetObjectInformationRequest(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReference
    ConsistencyLevel: Optional[ConsistencyLevelType] = None


# This class is the input for the 'list_attached_indices' function.
class ListAttachedIndicesRequest(BaseValidatorModel):
    DirectoryArn: str
    TargetReference: ObjectReference
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None


# This class is the input for the 'list_object_children' function.
class ListObjectChildrenRequest(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReference
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None


# This class is the input for the 'list_object_parent_paths' function.
class ListObjectParentPathsRequest(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReference
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_object_parents' function.
class ListObjectParentsRequest(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReference
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    IncludeAllLinksToEachParent: Optional[bool] = None


# This class is the input for the 'list_object_policies' function.
class ListObjectPoliciesRequest(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReference
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None


# This class is the input for the 'list_policy_attachments' function.
class ListPolicyAttachmentsRequest(BaseValidatorModel):
    DirectoryArn: str
    PolicyReference: ObjectReference
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None


# This class is the input for the 'lookup_policy' function.
class LookupPolicyRequest(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReference
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class BatchGetObjectAttributes(BaseValidatorModel):
    ObjectReference: ObjectReference
    SchemaFacet: SchemaFacet
    AttributeNames: List[str]


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


# This class is the input for the 'get_object_attributes' function.
class GetObjectAttributesRequest(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReference
    SchemaFacet: SchemaFacet
    AttributeNames: List[str]
    ConsistencyLevel: Optional[ConsistencyLevelType] = None


# This class is the input for the 'list_object_attributes' function.
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


# This class is the output for the 'apply_schema' function.
class ApplySchemaResponse(BaseValidatorModel):
    AppliedSchemaArn: str
    DirectoryArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'attach_object' function.
class AttachObjectResponse(BaseValidatorModel):
    AttachedObjectIdentifier: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'attach_to_index' function.
class AttachToIndexResponse(BaseValidatorModel):
    AttachedObjectIdentifier: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_directory' function.
class CreateDirectoryResponse(BaseValidatorModel):
    DirectoryArn: str
    Name: str
    ObjectIdentifier: str
    AppliedSchemaArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_index' function.
class CreateIndexResponse(BaseValidatorModel):
    ObjectIdentifier: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_object' function.
class CreateObjectResponse(BaseValidatorModel):
    ObjectIdentifier: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_schema' function.
class CreateSchemaResponse(BaseValidatorModel):
    SchemaArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_directory' function.
class DeleteDirectoryResponse(BaseValidatorModel):
    DirectoryArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_schema' function.
class DeleteSchemaResponse(BaseValidatorModel):
    SchemaArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'detach_from_index' function.
class DetachFromIndexResponse(BaseValidatorModel):
    DetachedObjectIdentifier: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'detach_object' function.
class DetachObjectResponse(BaseValidatorModel):
    DetachedObjectIdentifier: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disable_directory' function.
class DisableDirectoryResponse(BaseValidatorModel):
    DirectoryArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'detach_typed_link' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'enable_directory' function.
class EnableDirectoryResponse(BaseValidatorModel):
    DirectoryArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_applied_schema_version' function.
class GetAppliedSchemaVersionResponse(BaseValidatorModel):
    AppliedSchemaArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_object_information' function.
class GetObjectInformationResponse(BaseValidatorModel):
    SchemaFacets: List[SchemaFacet]
    ObjectIdentifier: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_schema_as_json' function.
class GetSchemaAsJsonResponse(BaseValidatorModel):
    Name: str
    Document: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_typed_link_facet_information' function.
class GetTypedLinkFacetInformationResponse(BaseValidatorModel):
    IdentityAttributeOrder: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_applied_schema_arns' function.
class ListAppliedSchemaArnsResponse(BaseValidatorModel):
    SchemaArns: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_development_schema_arns' function.
class ListDevelopmentSchemaArnsResponse(BaseValidatorModel):
    SchemaArns: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_facet_names' function.
class ListFacetNamesResponse(BaseValidatorModel):
    FacetNames: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_managed_schema_arns' function.
class ListManagedSchemaArnsResponse(BaseValidatorModel):
    SchemaArns: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_object_children' function.
class ListObjectChildrenResponse(BaseValidatorModel):
    Children: Dict[str, str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_object_policies' function.
class ListObjectPoliciesResponse(BaseValidatorModel):
    AttachedPolicyIds: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_policy_attachments' function.
class ListPolicyAttachmentsResponse(BaseValidatorModel):
    ObjectIdentifiers: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_published_schema_arns' function.
class ListPublishedSchemaArnsResponse(BaseValidatorModel):
    SchemaArns: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_typed_link_facet_names' function.
class ListTypedLinkFacetNamesResponse(BaseValidatorModel):
    FacetNames: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'publish_schema' function.
class PublishSchemaResponse(BaseValidatorModel):
    PublishedSchemaArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_schema_from_json' function.
class PutSchemaFromJsonResponse(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_object_attributes' function.
class UpdateObjectAttributesResponse(BaseValidatorModel):
    ObjectIdentifier: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_schema' function.
class UpdateSchemaResponse(BaseValidatorModel):
    SchemaArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'upgrade_applied_schema' function.
class UpgradeAppliedSchemaResponse(BaseValidatorModel):
    UpgradedSchemaArn: str
    DirectoryArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'upgrade_published_schema' function.
class UpgradePublishedSchemaResponse(BaseValidatorModel):
    UpgradedSchemaArn: str
    ResponseMetadata: ResponseMetadata


class BatchCreateIndex(BaseValidatorModel):
    OrderedIndexedAttributeList: List[AttributeKey]
    IsUnique: bool
    ParentReference: Optional[ObjectReference] = None
    LinkName: Optional[str] = None
    BatchReferenceName: Optional[str] = None


# This class is the input for the 'create_index' function.
class CreateIndexRequest(BaseValidatorModel):
    DirectoryArn: str
    OrderedIndexedAttributeList: List[AttributeKey]
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


# This class is the output for the 'list_object_parent_paths' function.
class ListObjectParentPathsResponse(BaseValidatorModel):
    PathToObjectIdentifiersList: List[PathToObjectIdentifiers]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class BatchListObjectParentsResponse(BaseValidatorModel):
    ParentLinks: Optional[List[ObjectIdentifierAndLinkNameTuple]] = None
    NextToken: Optional[str] = None


# This class is the output for the 'list_object_parents' function.
class ListObjectParentsResponse(BaseValidatorModel):
    Parents: Dict[str, str]
    ParentLinks: List[ObjectIdentifierAndLinkNameTuple]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_directory' function.
class GetDirectoryResponse(BaseValidatorModel):
    Directory: Directory
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_directories' function.
class ListDirectoriesResponse(BaseValidatorModel):
    Directories: List[Directory]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class FacetAttributeDefinitionOutput(BaseValidatorModel):
    Type: FacetAttributeTypeType
    DefaultValue: Optional[TypedAttributeValueOutput] = None
    IsImmutable: Optional[bool] = None
    Rules: Optional[Dict[str, RuleOutput]] = None


class TypedLinkAttributeDefinitionOutput(BaseValidatorModel):
    Name: str
    Type: FacetAttributeTypeType
    RequiredBehavior: RequiredAttributeBehaviorType
    DefaultValue: Optional[TypedAttributeValueOutput] = None
    IsImmutable: Optional[bool] = None
    Rules: Optional[Dict[str, RuleOutput]] = None


# This class is the output for the 'get_facet' function.
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


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


class PolicyToPath(BaseValidatorModel):
    Path: Optional[str] = None
    Policies: Optional[List[PolicyAttachment]] = None

RuleUnion = Union[Rule, RuleOutput]


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


# This class is the output for the 'get_link_attributes' function.
class GetLinkAttributesResponse(BaseValidatorModel):
    Attributes: List[AttributeKeyAndValueOutput]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_object_attributes' function.
class GetObjectAttributesResponse(BaseValidatorModel):
    Attributes: List[AttributeKeyAndValueOutput]
    ResponseMetadata: ResponseMetadata


class IndexAttachment(BaseValidatorModel):
    IndexedAttributes: Optional[List[AttributeKeyAndValueOutput]] = None
    ObjectIdentifier: Optional[str] = None


# This class is the output for the 'list_object_attributes' function.
class ListObjectAttributesResponse(BaseValidatorModel):
    Attributes: List[AttributeKeyAndValueOutput]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TypedLinkSpecifierOutput(BaseValidatorModel):
    TypedLinkFacet: TypedLinkSchemaAndFacetName
    SourceObjectReference: ObjectReference
    TargetObjectReference: ObjectReference
    IdentityAttributeValues: List[AttributeNameAndValueOutput]


class FacetAttributeOutput(BaseValidatorModel):
    Name: str
    AttributeDefinition: Optional[FacetAttributeDefinitionOutput] = None
    AttributeReference: Optional[FacetAttributeReference] = None
    RequiredBehavior: Optional[RequiredAttributeBehaviorType] = None


# This class is the output for the 'list_typed_link_facet_attributes' function.
class ListTypedLinkFacetAttributesResponse(BaseValidatorModel):
    Attributes: List[TypedLinkAttributeDefinitionOutput]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class BatchLookupPolicyResponse(BaseValidatorModel):
    PolicyToPathList: Optional[List[PolicyToPath]] = None
    NextToken: Optional[str] = None


# This class is the output for the 'lookup_policy' function.
class LookupPolicyResponse(BaseValidatorModel):
    PolicyToPathList: List[PolicyToPath]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

TypedAttributeValueUnion = Union[TypedAttributeValue, TypedAttributeValueOutput]


class BatchListAttachedIndicesResponse(BaseValidatorModel):
    IndexAttachments: Optional[List[IndexAttachment]] = None
    NextToken: Optional[str] = None


class BatchListIndexResponse(BaseValidatorModel):
    IndexAttachments: Optional[List[IndexAttachment]] = None
    NextToken: Optional[str] = None


# This class is the output for the 'list_attached_indices' function.
class ListAttachedIndicesResponse(BaseValidatorModel):
    IndexAttachments: List[IndexAttachment]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_index' function.
class ListIndexResponse(BaseValidatorModel):
    IndexAttachments: List[IndexAttachment]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'attach_typed_link' function.
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


# This class is the output for the 'list_incoming_typed_links' function.
class ListIncomingTypedLinksResponse(BaseValidatorModel):
    LinkSpecifiers: List[TypedLinkSpecifierOutput]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_outgoing_typed_links' function.
class ListOutgoingTypedLinksResponse(BaseValidatorModel):
    TypedLinkSpecifiers: List[TypedLinkSpecifierOutput]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_facet_attributes' function.
class ListFacetAttributesResponse(BaseValidatorModel):
    Attributes: List[FacetAttributeOutput]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AttributeKeyAndValue(BaseValidatorModel):
    Key: AttributeKey
    Value: TypedAttributeValueUnion


class AttributeNameAndValue(BaseValidatorModel):
    AttributeName: str
    Value: TypedAttributeValueUnion


class FacetAttributeDefinition(BaseValidatorModel):
    Type: FacetAttributeTypeType
    DefaultValue: Optional[TypedAttributeValueUnion] = None
    IsImmutable: Optional[bool] = None
    Rules: Optional[Dict[str, RuleUnion]] = None


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


class TypedLinkAttributeDefinition(BaseValidatorModel):
    Name: str
    Type: FacetAttributeTypeType
    RequiredBehavior: RequiredAttributeBehaviorType
    DefaultValue: Optional[TypedAttributeValueUnion] = None
    IsImmutable: Optional[bool] = None
    Rules: Optional[Dict[str, RuleUnion]] = None


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

AttributeKeyAndValueUnion = Union[AttributeKeyAndValue, AttributeKeyAndValueOutput]


class BatchCreateObject(BaseValidatorModel):
    SchemaFacet: List[SchemaFacet]
    ObjectAttributeList: List[AttributeKeyAndValue]
    ParentReference: Optional[ObjectReference] = None
    LinkName: Optional[str] = None
    BatchReferenceName: Optional[str] = None

AttributeNameAndValueUnion = Union[AttributeNameAndValue, AttributeNameAndValueOutput]

FacetAttributeDefinitionUnion = Union[FacetAttributeDefinition, FacetAttributeDefinitionOutput]


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

TypedLinkAttributeDefinitionUnion = Union[TypedLinkAttributeDefinition, TypedLinkAttributeDefinitionOutput]


# This class is the output for the 'batch_write' function.
class BatchWriteResponse(BaseValidatorModel):
    Responses: List[BatchWriteOperationResponse]
    ResponseMetadata: ResponseMetadata


class BatchReadOperationResponse(BaseValidatorModel):
    SuccessfulResponse: Optional[BatchReadSuccessfulResponse] = None
    ExceptionResponse: Optional[BatchReadException] = None


class AddFacetToObjectRequest(BaseValidatorModel):
    DirectoryArn: str
    SchemaFacet: SchemaFacet
    ObjectReference: ObjectReference
    ObjectAttributeList: Optional[List[AttributeKeyAndValueUnion]] = None


class BatchAddFacetToObject(BaseValidatorModel):
    SchemaFacet: SchemaFacet
    ObjectAttributeList: List[AttributeKeyAndValueUnion]
    ObjectReference: ObjectReference


# This class is the input for the 'create_object' function.
class CreateObjectRequest(BaseValidatorModel):
    DirectoryArn: str
    SchemaFacets: List[SchemaFacet]
    ObjectAttributeList: Optional[List[AttributeKeyAndValueUnion]] = None
    ParentReference: Optional[ObjectReference] = None
    LinkName: Optional[str] = None


# This class is the input for the 'attach_typed_link' function.
class AttachTypedLinkRequest(BaseValidatorModel):
    DirectoryArn: str
    SourceObjectReference: ObjectReference
    TargetObjectReference: ObjectReference
    TypedLinkFacet: TypedLinkSchemaAndFacetName
    Attributes: List[AttributeNameAndValueUnion]


class BatchAttachTypedLink(BaseValidatorModel):
    SourceObjectReference: ObjectReference
    TargetObjectReference: ObjectReference
    TypedLinkFacet: TypedLinkSchemaAndFacetName
    Attributes: List[AttributeNameAndValueUnion]


class TypedLinkSpecifier(BaseValidatorModel):
    TypedLinkFacet: TypedLinkSchemaAndFacetName
    SourceObjectReference: ObjectReference
    TargetObjectReference: ObjectReference
    IdentityAttributeValues: List[AttributeNameAndValueUnion]


class FacetAttribute(BaseValidatorModel):
    Name: str
    AttributeDefinition: Optional[FacetAttributeDefinitionUnion] = None
    AttributeReference: Optional[FacetAttributeReference] = None
    RequiredBehavior: Optional[RequiredAttributeBehaviorType] = None


class BatchUpdateObjectAttributes(BaseValidatorModel):
    ObjectReference: ObjectReference
    AttributeUpdates: List[ObjectAttributeUpdate]


# This class is the input for the 'update_object_attributes' function.
class UpdateObjectAttributesRequest(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReference
    AttributeUpdates: List[ObjectAttributeUpdate]


class BatchListIndex(BaseValidatorModel):
    IndexReference: ObjectReference
    RangesOnIndexedValues: Optional[List[ObjectAttributeRange]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListIndexRequestPaginate(BaseValidatorModel):
    DirectoryArn: str
    IndexReference: ObjectReference
    RangesOnIndexedValues: Optional[List[ObjectAttributeRange]] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_index' function.
class ListIndexRequest(BaseValidatorModel):
    DirectoryArn: str
    IndexReference: ObjectReference
    RangesOnIndexedValues: Optional[List[ObjectAttributeRange]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None


class BatchListIncomingTypedLinks(BaseValidatorModel):
    ObjectReference: ObjectReference
    FilterAttributeRanges: Optional[List[TypedLinkAttributeRange]] = None
    FilterTypedLink: Optional[TypedLinkSchemaAndFacetName] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class BatchListOutgoingTypedLinks(BaseValidatorModel):
    ObjectReference: ObjectReference
    FilterAttributeRanges: Optional[List[TypedLinkAttributeRange]] = None
    FilterTypedLink: Optional[TypedLinkSchemaAndFacetName] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListIncomingTypedLinksRequestPaginate(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReference
    FilterAttributeRanges: Optional[List[TypedLinkAttributeRange]] = None
    FilterTypedLink: Optional[TypedLinkSchemaAndFacetName] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_incoming_typed_links' function.
class ListIncomingTypedLinksRequest(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReference
    FilterAttributeRanges: Optional[List[TypedLinkAttributeRange]] = None
    FilterTypedLink: Optional[TypedLinkSchemaAndFacetName] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None


class ListOutgoingTypedLinksRequestPaginate(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReference
    FilterAttributeRanges: Optional[List[TypedLinkAttributeRange]] = None
    FilterTypedLink: Optional[TypedLinkSchemaAndFacetName] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_outgoing_typed_links' function.
class ListOutgoingTypedLinksRequest(BaseValidatorModel):
    DirectoryArn: str
    ObjectReference: ObjectReference
    FilterAttributeRanges: Optional[List[TypedLinkAttributeRange]] = None
    FilterTypedLink: Optional[TypedLinkSchemaAndFacetName] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ConsistencyLevel: Optional[ConsistencyLevelType] = None


class TypedLinkFacetAttributeUpdate(BaseValidatorModel):
    Attribute: TypedLinkAttributeDefinitionUnion
    Action: UpdateActionTypeType


class TypedLinkFacet(BaseValidatorModel):
    Name: str
    Attributes: List[TypedLinkAttributeDefinitionUnion]
    IdentityAttributeOrder: List[str]


# This class is the output for the 'batch_read' function.
class BatchReadResponse(BaseValidatorModel):
    Responses: List[BatchReadOperationResponse]
    ResponseMetadata: ResponseMetadata

TypedLinkSpecifierUnion = Union[TypedLinkSpecifier, TypedLinkSpecifierOutput]

FacetAttributeUnion = Union[FacetAttribute, FacetAttributeOutput]


class UpdateTypedLinkFacetRequest(BaseValidatorModel):
    SchemaArn: str
    Name: str
    AttributeUpdates: List[TypedLinkFacetAttributeUpdate]
    IdentityAttributeOrder: List[str]


class CreateTypedLinkFacetRequest(BaseValidatorModel):
    SchemaArn: str
    Facet: TypedLinkFacet


class BatchDetachTypedLink(BaseValidatorModel):
    TypedLinkSpecifier: TypedLinkSpecifierUnion


class BatchGetLinkAttributes(BaseValidatorModel):
    TypedLinkSpecifier: TypedLinkSpecifierUnion
    AttributeNames: List[str]


class BatchUpdateLinkAttributes(BaseValidatorModel):
    TypedLinkSpecifier: TypedLinkSpecifierUnion
    AttributeUpdates: List[LinkAttributeUpdate]


# This class is the input for the 'detach_typed_link' function.
class DetachTypedLinkRequest(BaseValidatorModel):
    DirectoryArn: str
    TypedLinkSpecifier: TypedLinkSpecifierUnion


# This class is the input for the 'get_link_attributes' function.
class GetLinkAttributesRequest(BaseValidatorModel):
    DirectoryArn: str
    TypedLinkSpecifier: TypedLinkSpecifierUnion
    AttributeNames: List[str]
    ConsistencyLevel: Optional[ConsistencyLevelType] = None


class UpdateLinkAttributesRequest(BaseValidatorModel):
    DirectoryArn: str
    TypedLinkSpecifier: TypedLinkSpecifierUnion
    AttributeUpdates: List[LinkAttributeUpdate]


class CreateFacetRequest(BaseValidatorModel):
    SchemaArn: str
    Name: str
    Attributes: Optional[List[FacetAttributeUnion]] = None
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
    AttributeUpdates: Optional[List[FacetAttributeUpdate]] = None
    ObjectType: Optional[ObjectTypeType] = None


# This class is the input for the 'batch_read' function.
class BatchReadRequest(BaseValidatorModel):
    DirectoryArn: str
    Operations: List[BatchReadOperation]
    ConsistencyLevel: Optional[ConsistencyLevelType] = None


# This class is the input for the 'batch_write' function.
class BatchWriteRequest(BaseValidatorModel):
    DirectoryArn: str
    Operations: List[BatchWriteOperation]