from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.schemas.schemas_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'create_discoverer' function.
class CreateDiscovererRequest(BaseValidatorModel):
    SourceArn: str
    Description: Optional[str] = None
    CrossAccount: Optional[bool] = None
    Tags: Optional[Dict[str, str]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'create_registry' function.
class CreateRegistryRequest(BaseValidatorModel):
    RegistryName: str
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'create_schema' function.
class CreateSchemaRequest(BaseValidatorModel):
    Content: str
    RegistryName: str
    SchemaName: str
    Type: TypeType
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'delete_discoverer' function.
class DeleteDiscovererRequest(BaseValidatorModel):
    DiscovererId: str


# This class is the input for the 'delete_registry' function.
class DeleteRegistryRequest(BaseValidatorModel):
    RegistryName: str


# This class is the input for the 'delete_resource_policy' function.
class DeleteResourcePolicyRequest(BaseValidatorModel):
    RegistryName: Optional[str] = None


# This class is the input for the 'delete_schema' function.
class DeleteSchemaRequest(BaseValidatorModel):
    RegistryName: str
    SchemaName: str


# This class is the input for the 'delete_schema_version' function.
class DeleteSchemaVersionRequest(BaseValidatorModel):
    RegistryName: str
    SchemaName: str
    SchemaVersion: str


# This class is the input for the 'describe_code_binding' function.
class DescribeCodeBindingRequest(BaseValidatorModel):
    Language: str
    RegistryName: str
    SchemaName: str
    SchemaVersion: Optional[str] = None


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


# This class is the input for the 'describe_discoverer' function.
class DescribeDiscovererRequest(BaseValidatorModel):
    DiscovererId: str


# This class is the input for the 'describe_registry' function.
class DescribeRegistryRequest(BaseValidatorModel):
    RegistryName: str


# This class is the input for the 'describe_schema' function.
class DescribeSchemaRequest(BaseValidatorModel):
    RegistryName: str
    SchemaName: str
    SchemaVersion: Optional[str] = None


class DiscovererSummary(BaseValidatorModel):
    DiscovererArn: Optional[str] = None
    DiscovererId: Optional[str] = None
    SourceArn: Optional[str] = None
    State: Optional[DiscovererStateType] = None
    CrossAccount: Optional[bool] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'export_schema' function.
class ExportSchemaRequest(BaseValidatorModel):
    RegistryName: str
    SchemaName: str
    Type: str
    SchemaVersion: Optional[str] = None


# This class is the input for the 'get_code_binding_source' function.
class GetCodeBindingSourceRequest(BaseValidatorModel):
    Language: str
    RegistryName: str
    SchemaName: str
    SchemaVersion: Optional[str] = None


# This class is the input for the 'get_discovered_schema' function.
class GetDiscoveredSchemaRequest(BaseValidatorModel):
    Events: List[str]
    Type: TypeType


# This class is the input for the 'get_resource_policy' function.
class GetResourcePolicyRequest(BaseValidatorModel):
    RegistryName: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_discoverers' function.
class ListDiscoverersRequest(BaseValidatorModel):
    DiscovererIdPrefix: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None
    SourceArnPrefix: Optional[str] = None


# This class is the input for the 'list_registries' function.
class ListRegistriesRequest(BaseValidatorModel):
    Limit: Optional[int] = None
    NextToken: Optional[str] = None
    RegistryNamePrefix: Optional[str] = None
    Scope: Optional[str] = None


class RegistrySummary(BaseValidatorModel):
    RegistryArn: Optional[str] = None
    RegistryName: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'list_schema_versions' function.
class ListSchemaVersionsRequest(BaseValidatorModel):
    RegistryName: str
    SchemaName: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class SchemaVersionSummary(BaseValidatorModel):
    SchemaArn: Optional[str] = None
    SchemaName: Optional[str] = None
    SchemaVersion: Optional[str] = None
    Type: Optional[TypeType] = None


# This class is the input for the 'list_schemas' function.
class ListSchemasRequest(BaseValidatorModel):
    RegistryName: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None
    SchemaNamePrefix: Optional[str] = None


class SchemaSummary(BaseValidatorModel):
    LastModified: Optional[datetime] = None
    SchemaArn: Optional[str] = None
    SchemaName: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    VersionCount: Optional[int] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'put_code_binding' function.
class PutCodeBindingRequest(BaseValidatorModel):
    Language: str
    RegistryName: str
    SchemaName: str
    SchemaVersion: Optional[str] = None


# This class is the input for the 'put_resource_policy' function.
class PutResourcePolicyRequest(BaseValidatorModel):
    Policy: str
    RegistryName: Optional[str] = None
    RevisionId: Optional[str] = None


class SearchSchemaVersionSummary(BaseValidatorModel):
    CreatedDate: Optional[datetime] = None
    SchemaVersion: Optional[str] = None
    Type: Optional[TypeType] = None


# This class is the input for the 'search_schemas' function.
class SearchSchemasRequest(BaseValidatorModel):
    Keywords: str
    RegistryName: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'start_discoverer' function.
class StartDiscovererRequest(BaseValidatorModel):
    DiscovererId: str


# This class is the input for the 'stop_discoverer' function.
class StopDiscovererRequest(BaseValidatorModel):
    DiscovererId: str


# This class is the input for the 'tag_resource' function.
class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


# This class is the input for the 'untag_resource' function.
class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


# This class is the input for the 'update_discoverer' function.
class UpdateDiscovererRequest(BaseValidatorModel):
    DiscovererId: str
    Description: Optional[str] = None
    CrossAccount: Optional[bool] = None


# This class is the input for the 'update_registry' function.
class UpdateRegistryRequest(BaseValidatorModel):
    RegistryName: str
    Description: Optional[str] = None


# This class is the input for the 'update_schema' function.
class UpdateSchemaRequest(BaseValidatorModel):
    RegistryName: str
    SchemaName: str
    ClientTokenId: Optional[str] = None
    Content: Optional[str] = None
    Description: Optional[str] = None
    Type: Optional[TypeType] = None


# This class is the output for the 'create_discoverer' function.
class CreateDiscovererResponse(BaseValidatorModel):
    Description: str
    DiscovererArn: str
    DiscovererId: str
    SourceArn: str
    State: DiscovererStateType
    CrossAccount: bool
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_registry' function.
class CreateRegistryResponse(BaseValidatorModel):
    Description: str
    RegistryArn: str
    RegistryName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_schema' function.
class CreateSchemaResponse(BaseValidatorModel):
    Description: str
    LastModified: datetime
    SchemaArn: str
    SchemaName: str
    SchemaVersion: str
    Tags: Dict[str, str]
    Type: str
    VersionCreatedDate: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_code_binding' function.
class DescribeCodeBindingResponse(BaseValidatorModel):
    CreationDate: datetime
    LastModified: datetime
    SchemaVersion: str
    Status: CodeGenerationStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_discoverer' function.
class DescribeDiscovererResponse(BaseValidatorModel):
    Description: str
    DiscovererArn: str
    DiscovererId: str
    SourceArn: str
    State: DiscovererStateType
    CrossAccount: bool
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_registry' function.
class DescribeRegistryResponse(BaseValidatorModel):
    Description: str
    RegistryArn: str
    RegistryName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_schema' function.
class DescribeSchemaResponse(BaseValidatorModel):
    Content: str
    Description: str
    LastModified: datetime
    SchemaArn: str
    SchemaName: str
    SchemaVersion: str
    Tags: Dict[str, str]
    Type: str
    VersionCreatedDate: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'untag_resource' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'export_schema' function.
class ExportSchemaResponse(BaseValidatorModel):
    Content: str
    SchemaArn: str
    SchemaName: str
    SchemaVersion: str
    Type: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_code_binding_source' function.
class GetCodeBindingSourceResponse(BaseValidatorModel):
    Body: StreamingBody
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_discovered_schema' function.
class GetDiscoveredSchemaResponse(BaseValidatorModel):
    Content: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_resource_policy' function.
class GetResourcePolicyResponse(BaseValidatorModel):
    Policy: str
    RevisionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_code_binding' function.
class PutCodeBindingResponse(BaseValidatorModel):
    CreationDate: datetime
    LastModified: datetime
    SchemaVersion: str
    Status: CodeGenerationStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_resource_policy' function.
class PutResourcePolicyResponse(BaseValidatorModel):
    Policy: str
    RevisionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_discoverer' function.
class StartDiscovererResponse(BaseValidatorModel):
    DiscovererId: str
    State: DiscovererStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_discoverer' function.
class StopDiscovererResponse(BaseValidatorModel):
    DiscovererId: str
    State: DiscovererStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_discoverer' function.
class UpdateDiscovererResponse(BaseValidatorModel):
    Description: str
    DiscovererArn: str
    DiscovererId: str
    SourceArn: str
    State: DiscovererStateType
    CrossAccount: bool
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_registry' function.
class UpdateRegistryResponse(BaseValidatorModel):
    Description: str
    RegistryArn: str
    RegistryName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_schema' function.
class UpdateSchemaResponse(BaseValidatorModel):
    Description: str
    LastModified: datetime
    SchemaArn: str
    SchemaName: str
    SchemaVersion: str
    Tags: Dict[str, str]
    Type: str
    VersionCreatedDate: datetime
    ResponseMetadata: ResponseMetadata


class DescribeCodeBindingRequestWait(BaseValidatorModel):
    Language: str
    RegistryName: str
    SchemaName: str
    SchemaVersion: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


# This class is the output for the 'list_discoverers' function.
class ListDiscoverersResponse(BaseValidatorModel):
    Discoverers: List[DiscovererSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListDiscoverersRequestPaginate(BaseValidatorModel):
    DiscovererIdPrefix: Optional[str] = None
    SourceArnPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRegistriesRequestPaginate(BaseValidatorModel):
    RegistryNamePrefix: Optional[str] = None
    Scope: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSchemaVersionsRequestPaginate(BaseValidatorModel):
    RegistryName: str
    SchemaName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSchemasRequestPaginate(BaseValidatorModel):
    RegistryName: str
    SchemaNamePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchSchemasRequestPaginate(BaseValidatorModel):
    Keywords: str
    RegistryName: str
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_registries' function.
class ListRegistriesResponse(BaseValidatorModel):
    Registries: List[RegistrySummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_schema_versions' function.
class ListSchemaVersionsResponse(BaseValidatorModel):
    SchemaVersions: List[SchemaVersionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_schemas' function.
class ListSchemasResponse(BaseValidatorModel):
    Schemas: List[SchemaSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SearchSchemaSummary(BaseValidatorModel):
    RegistryName: Optional[str] = None
    SchemaArn: Optional[str] = None
    SchemaName: Optional[str] = None
    SchemaVersions: Optional[List[SearchSchemaVersionSummary]] = None


# This class is the output for the 'search_schemas' function.
class SearchSchemasResponse(BaseValidatorModel):
    Schemas: List[SearchSchemaSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None