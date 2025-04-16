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
from aws_resource_validator.pydantic_models.schemas_constants import *

class CreateDiscovererRequest(BaseValidatorModel):
    SourceArn: str
    Description: Optional[str] = None
    CrossAccount: Optional[bool] = None
    Tags: Optional[Mapping[str, str]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateRegistryRequest(BaseValidatorModel):
    RegistryName: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class DeleteDiscovererRequest(BaseValidatorModel):
    DiscovererId: str


class DeleteRegistryRequest(BaseValidatorModel):
    RegistryName: str


class DeleteResourcePolicyRequest(BaseValidatorModel):
    RegistryName: Optional[str] = None


class DeleteSchemaRequest(BaseValidatorModel):
    RegistryName: str
    SchemaName: str


class DeleteSchemaVersionRequest(BaseValidatorModel):
    RegistryName: str
    SchemaName: str
    SchemaVersion: str


class DescribeCodeBindingRequest(BaseValidatorModel):
    Language: str
    RegistryName: str
    SchemaName: str
    SchemaVersion: Optional[str] = None


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeDiscovererRequest(BaseValidatorModel):
    DiscovererId: str


class DescribeRegistryRequest(BaseValidatorModel):
    RegistryName: str


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


class GetCodeBindingSourceRequest(BaseValidatorModel):
    Language: str
    RegistryName: str
    SchemaName: str
    SchemaVersion: Optional[str] = None


class GetResourcePolicyRequest(BaseValidatorModel):
    RegistryName: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListDiscoverersRequest(BaseValidatorModel):
    DiscovererIdPrefix: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None
    SourceArnPrefix: Optional[str] = None


class ListRegistriesRequest(BaseValidatorModel):
    Limit: Optional[int] = None
    NextToken: Optional[str] = None
    RegistryNamePrefix: Optional[str] = None
    Scope: Optional[str] = None


class RegistrySummary(BaseValidatorModel):
    RegistryArn: Optional[str] = None
    RegistryName: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class ListSchemaVersionsRequest(BaseValidatorModel):
    RegistryName: str
    SchemaName: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


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


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class PutCodeBindingRequest(BaseValidatorModel):
    Language: str
    RegistryName: str
    SchemaName: str
    SchemaVersion: Optional[str] = None


class PutResourcePolicyRequest(BaseValidatorModel):
    Policy: str
    RegistryName: Optional[str] = None
    RevisionId: Optional[str] = None


class SearchSchemasRequest(BaseValidatorModel):
    Keywords: str
    RegistryName: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class StartDiscovererRequest(BaseValidatorModel):
    DiscovererId: str


class StopDiscovererRequest(BaseValidatorModel):
    DiscovererId: str


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateDiscovererRequest(BaseValidatorModel):
    DiscovererId: str
    Description: Optional[str] = None
    CrossAccount: Optional[bool] = None


class UpdateRegistryRequest(BaseValidatorModel):
    RegistryName: str
    Description: Optional[str] = None


class CreateDiscovererResponse(BaseValidatorModel):
    Description: str
    DiscovererArn: str
    DiscovererId: str
    SourceArn: str
    State: DiscovererStateType
    CrossAccount: bool
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateRegistryResponse(BaseValidatorModel):
    Description: str
    RegistryArn: str
    RegistryName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class DescribeCodeBindingResponse(BaseValidatorModel):
    CreationDate: datetime
    LastModified: datetime
    SchemaVersion: str
    Status: CodeGenerationStatusType
    ResponseMetadata: ResponseMetadata


class DescribeDiscovererResponse(BaseValidatorModel):
    Description: str
    DiscovererArn: str
    DiscovererId: str
    SourceArn: str
    State: DiscovererStateType
    CrossAccount: bool
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class DescribeRegistryResponse(BaseValidatorModel):
    Description: str
    RegistryArn: str
    RegistryName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetCodeBindingSourceResponse(BaseValidatorModel):
    Body: StreamingBody
    ResponseMetadata: ResponseMetadata


class GetDiscoveredSchemaResponse(BaseValidatorModel):
    Content: str
    ResponseMetadata: ResponseMetadata


class GetResourcePolicyResponse(BaseValidatorModel):
    Policy: str
    RevisionId: str
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class PutCodeBindingResponse(BaseValidatorModel):
    CreationDate: datetime
    LastModified: datetime
    SchemaVersion: str
    Status: CodeGenerationStatusType
    ResponseMetadata: ResponseMetadata


class PutResourcePolicyResponse(BaseValidatorModel):
    Policy: str
    RevisionId: str
    ResponseMetadata: ResponseMetadata


class StartDiscovererResponse(BaseValidatorModel):
    DiscovererId: str
    State: DiscovererStateType
    ResponseMetadata: ResponseMetadata


class StopDiscovererResponse(BaseValidatorModel):
    DiscovererId: str
    State: DiscovererStateType
    ResponseMetadata: ResponseMetadata


class UpdateDiscovererResponse(BaseValidatorModel):
    Description: str
    DiscovererArn: str
    DiscovererId: str
    SourceArn: str
    State: DiscovererStateType
    CrossAccount: bool
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdateRegistryResponse(BaseValidatorModel):
    Description: str
    RegistryArn: str
    RegistryName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class DescribeCodeBindingRequestWait(BaseValidatorModel):
    Language: str
    RegistryName: str
    SchemaName: str
    SchemaVersion: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


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


class ListRegistriesResponse(BaseValidatorModel):
    Registries: List[RegistrySummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SchemaVersionSummary(BaseValidatorModel):
    pass


class ListSchemaVersionsResponse(BaseValidatorModel):
    SchemaVersions: List[SchemaVersionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListSchemasResponse(BaseValidatorModel):
    Schemas: List[SchemaSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SearchSchemaVersionSummary(BaseValidatorModel):
    pass


class SearchSchemaSummary(BaseValidatorModel):
    RegistryName: Optional[str] = None
    SchemaArn: Optional[str] = None
    SchemaName: Optional[str] = None
    SchemaVersions: Optional[List[SearchSchemaVersionSummary]] = None


class SearchSchemasResponse(BaseValidatorModel):
    Schemas: List[SearchSchemaSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


