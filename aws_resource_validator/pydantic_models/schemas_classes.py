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

class CreateDiscovererRequestTypeDef(BaseValidatorModel):
    SourceArn: str
    Description: Optional[str] = None
    CrossAccount: Optional[bool] = None
    Tags: Optional[Mapping[str, str]] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateRegistryRequestTypeDef(BaseValidatorModel):
    RegistryName: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class DeleteDiscovererRequestTypeDef(BaseValidatorModel):
    DiscovererId: str


class DeleteRegistryRequestTypeDef(BaseValidatorModel):
    RegistryName: str


class DeleteResourcePolicyRequestTypeDef(BaseValidatorModel):
    RegistryName: Optional[str] = None


class DeleteSchemaRequestTypeDef(BaseValidatorModel):
    RegistryName: str
    SchemaName: str


class DeleteSchemaVersionRequestTypeDef(BaseValidatorModel):
    RegistryName: str
    SchemaName: str
    SchemaVersion: str


class DescribeCodeBindingRequestTypeDef(BaseValidatorModel):
    Language: str
    RegistryName: str
    SchemaName: str
    SchemaVersion: Optional[str] = None


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeDiscovererRequestTypeDef(BaseValidatorModel):
    DiscovererId: str


class DescribeRegistryRequestTypeDef(BaseValidatorModel):
    RegistryName: str


class DescribeSchemaRequestTypeDef(BaseValidatorModel):
    RegistryName: str
    SchemaName: str
    SchemaVersion: Optional[str] = None


class DiscovererSummaryTypeDef(BaseValidatorModel):
    DiscovererArn: Optional[str] = None
    DiscovererId: Optional[str] = None
    SourceArn: Optional[str] = None
    State: Optional[DiscovererStateType] = None
    CrossAccount: Optional[bool] = None
    Tags: Optional[Dict[str, str]] = None


class GetCodeBindingSourceRequestTypeDef(BaseValidatorModel):
    Language: str
    RegistryName: str
    SchemaName: str
    SchemaVersion: Optional[str] = None


class GetResourcePolicyRequestTypeDef(BaseValidatorModel):
    RegistryName: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListDiscoverersRequestTypeDef(BaseValidatorModel):
    DiscovererIdPrefix: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None
    SourceArnPrefix: Optional[str] = None


class ListRegistriesRequestTypeDef(BaseValidatorModel):
    Limit: Optional[int] = None
    NextToken: Optional[str] = None
    RegistryNamePrefix: Optional[str] = None
    Scope: Optional[str] = None


class RegistrySummaryTypeDef(BaseValidatorModel):
    RegistryArn: Optional[str] = None
    RegistryName: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class ListSchemaVersionsRequestTypeDef(BaseValidatorModel):
    RegistryName: str
    SchemaName: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListSchemasRequestTypeDef(BaseValidatorModel):
    RegistryName: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None
    SchemaNamePrefix: Optional[str] = None


class SchemaSummaryTypeDef(BaseValidatorModel):
    LastModified: Optional[datetime] = None
    SchemaArn: Optional[str] = None
    SchemaName: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    VersionCount: Optional[int] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class PutCodeBindingRequestTypeDef(BaseValidatorModel):
    Language: str
    RegistryName: str
    SchemaName: str
    SchemaVersion: Optional[str] = None


class PutResourcePolicyRequestTypeDef(BaseValidatorModel):
    Policy: str
    RegistryName: Optional[str] = None
    RevisionId: Optional[str] = None


class SearchSchemasRequestTypeDef(BaseValidatorModel):
    Keywords: str
    RegistryName: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class StartDiscovererRequestTypeDef(BaseValidatorModel):
    DiscovererId: str


class StopDiscovererRequestTypeDef(BaseValidatorModel):
    DiscovererId: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateDiscovererRequestTypeDef(BaseValidatorModel):
    DiscovererId: str
    Description: Optional[str] = None
    CrossAccount: Optional[bool] = None


class UpdateRegistryRequestTypeDef(BaseValidatorModel):
    RegistryName: str
    Description: Optional[str] = None


class CreateDiscovererResponseTypeDef(BaseValidatorModel):
    Description: str
    DiscovererArn: str
    DiscovererId: str
    SourceArn: str
    State: DiscovererStateType
    CrossAccount: bool
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRegistryResponseTypeDef(BaseValidatorModel):
    Description: str
    RegistryArn: str
    RegistryName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeCodeBindingResponseTypeDef(BaseValidatorModel):
    CreationDate: datetime
    LastModified: datetime
    SchemaVersion: str
    Status: CodeGenerationStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDiscovererResponseTypeDef(BaseValidatorModel):
    Description: str
    DiscovererArn: str
    DiscovererId: str
    SourceArn: str
    State: DiscovererStateType
    CrossAccount: bool
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeRegistryResponseTypeDef(BaseValidatorModel):
    Description: str
    RegistryArn: str
    RegistryName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetCodeBindingSourceResponseTypeDef(BaseValidatorModel):
    Body: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef


class GetDiscoveredSchemaResponseTypeDef(BaseValidatorModel):
    Content: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetResourcePolicyResponseTypeDef(BaseValidatorModel):
    Policy: str
    RevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class PutCodeBindingResponseTypeDef(BaseValidatorModel):
    CreationDate: datetime
    LastModified: datetime
    SchemaVersion: str
    Status: CodeGenerationStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class PutResourcePolicyResponseTypeDef(BaseValidatorModel):
    Policy: str
    RevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartDiscovererResponseTypeDef(BaseValidatorModel):
    DiscovererId: str
    State: DiscovererStateType
    ResponseMetadata: ResponseMetadataTypeDef


class StopDiscovererResponseTypeDef(BaseValidatorModel):
    DiscovererId: str
    State: DiscovererStateType
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDiscovererResponseTypeDef(BaseValidatorModel):
    Description: str
    DiscovererArn: str
    DiscovererId: str
    SourceArn: str
    State: DiscovererStateType
    CrossAccount: bool
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateRegistryResponseTypeDef(BaseValidatorModel):
    Description: str
    RegistryArn: str
    RegistryName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeCodeBindingRequestWaitTypeDef(BaseValidatorModel):
    Language: str
    RegistryName: str
    SchemaName: str
    SchemaVersion: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class ListDiscoverersResponseTypeDef(BaseValidatorModel):
    Discoverers: List[DiscovererSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListDiscoverersRequestPaginateTypeDef(BaseValidatorModel):
    DiscovererIdPrefix: Optional[str] = None
    SourceArnPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRegistriesRequestPaginateTypeDef(BaseValidatorModel):
    RegistryNamePrefix: Optional[str] = None
    Scope: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSchemaVersionsRequestPaginateTypeDef(BaseValidatorModel):
    RegistryName: str
    SchemaName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSchemasRequestPaginateTypeDef(BaseValidatorModel):
    RegistryName: str
    SchemaNamePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchSchemasRequestPaginateTypeDef(BaseValidatorModel):
    Keywords: str
    RegistryName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRegistriesResponseTypeDef(BaseValidatorModel):
    Registries: List[RegistrySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class SchemaVersionSummaryTypeDef(BaseValidatorModel):
    pass


class ListSchemaVersionsResponseTypeDef(BaseValidatorModel):
    SchemaVersions: List[SchemaVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListSchemasResponseTypeDef(BaseValidatorModel):
    Schemas: List[SchemaSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class SearchSchemaVersionSummaryTypeDef(BaseValidatorModel):
    pass


class SearchSchemaSummaryTypeDef(BaseValidatorModel):
    RegistryName: Optional[str] = None
    SchemaArn: Optional[str] = None
    SchemaName: Optional[str] = None
    SchemaVersions: Optional[List[SearchSchemaVersionSummaryTypeDef]] = None


class SearchSchemasResponseTypeDef(BaseValidatorModel):
    Schemas: List[SearchSchemaSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


