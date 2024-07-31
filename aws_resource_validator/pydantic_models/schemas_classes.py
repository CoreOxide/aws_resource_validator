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
from aws_resource_validator.pydantic_models.schemas_constants import *

class CreateDiscovererRequestRequestTypeDef(BaseModel):
    SourceArn: str
    Description: Optional[str] = None
    CrossAccount: Optional[bool] = None
    Tags: Optional[Mapping[str, str]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateRegistryRequestRequestTypeDef(BaseModel):
    RegistryName: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateSchemaRequestRequestTypeDef(BaseModel):
    Content: str
    RegistryName: str
    SchemaName: str
    Type: TypeType
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class DeleteDiscovererRequestRequestTypeDef(BaseModel):
    DiscovererId: str

class DeleteRegistryRequestRequestTypeDef(BaseModel):
    RegistryName: str

class DeleteResourcePolicyRequestRequestTypeDef(BaseModel):
    RegistryName: Optional[str] = None

class DeleteSchemaRequestRequestTypeDef(BaseModel):
    RegistryName: str
    SchemaName: str

class DeleteSchemaVersionRequestRequestTypeDef(BaseModel):
    RegistryName: str
    SchemaName: str
    SchemaVersion: str

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeCodeBindingRequestRequestTypeDef(BaseModel):
    Language: str
    RegistryName: str
    SchemaName: str
    SchemaVersion: Optional[str] = None

class DescribeDiscovererRequestRequestTypeDef(BaseModel):
    DiscovererId: str

class DescribeRegistryRequestRequestTypeDef(BaseModel):
    RegistryName: str

class DescribeSchemaRequestRequestTypeDef(BaseModel):
    RegistryName: str
    SchemaName: str
    SchemaVersion: Optional[str] = None

class DiscovererSummaryTypeDef(BaseModel):
    DiscovererArn: Optional[str] = None
    DiscovererId: Optional[str] = None
    SourceArn: Optional[str] = None
    State: Optional[DiscovererStateType] = None
    CrossAccount: Optional[bool] = None
    Tags: Optional[Dict[str, str]] = None

class ExportSchemaRequestRequestTypeDef(BaseModel):
    RegistryName: str
    SchemaName: str
    Type: str
    SchemaVersion: Optional[str] = None

class GetCodeBindingSourceRequestRequestTypeDef(BaseModel):
    Language: str
    RegistryName: str
    SchemaName: str
    SchemaVersion: Optional[str] = None

class GetDiscoveredSchemaRequestRequestTypeDef(BaseModel):
    Events: Sequence[str]
    Type: TypeType

class GetResourcePolicyRequestRequestTypeDef(BaseModel):
    RegistryName: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListDiscoverersRequestRequestTypeDef(BaseModel):
    DiscovererIdPrefix: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None
    SourceArnPrefix: Optional[str] = None

class ListRegistriesRequestRequestTypeDef(BaseModel):
    Limit: Optional[int] = None
    NextToken: Optional[str] = None
    RegistryNamePrefix: Optional[str] = None
    Scope: Optional[str] = None

class RegistrySummaryTypeDef(BaseModel):
    RegistryArn: Optional[str] = None
    RegistryName: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class ListSchemaVersionsRequestRequestTypeDef(BaseModel):
    RegistryName: str
    SchemaName: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class SchemaVersionSummaryTypeDef(BaseModel):
    SchemaArn: Optional[str] = None
    SchemaName: Optional[str] = None
    SchemaVersion: Optional[str] = None
    Type: Optional[TypeType] = None

class ListSchemasRequestRequestTypeDef(BaseModel):
    RegistryName: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None
    SchemaNamePrefix: Optional[str] = None

class SchemaSummaryTypeDef(BaseModel):
    LastModified: Optional[datetime] = None
    SchemaArn: Optional[str] = None
    SchemaName: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    VersionCount: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class PutCodeBindingRequestRequestTypeDef(BaseModel):
    Language: str
    RegistryName: str
    SchemaName: str
    SchemaVersion: Optional[str] = None

class PutResourcePolicyRequestRequestTypeDef(BaseModel):
    Policy: str
    RegistryName: Optional[str] = None
    RevisionId: Optional[str] = None

class SearchSchemaVersionSummaryTypeDef(BaseModel):
    CreatedDate: Optional[datetime] = None
    SchemaVersion: Optional[str] = None
    Type: Optional[TypeType] = None

class SearchSchemasRequestRequestTypeDef(BaseModel):
    Keywords: str
    RegistryName: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class StartDiscovererRequestRequestTypeDef(BaseModel):
    DiscovererId: str

class StopDiscovererRequestRequestTypeDef(BaseModel):
    DiscovererId: str

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateDiscovererRequestRequestTypeDef(BaseModel):
    DiscovererId: str
    Description: Optional[str] = None
    CrossAccount: Optional[bool] = None

class UpdateRegistryRequestRequestTypeDef(BaseModel):
    RegistryName: str
    Description: Optional[str] = None

class UpdateSchemaRequestRequestTypeDef(BaseModel):
    RegistryName: str
    SchemaName: str
    ClientTokenId: Optional[str] = None
    Content: Optional[str] = None
    Description: Optional[str] = None
    Type: Optional[TypeType] = None

class CreateDiscovererResponseTypeDef(BaseModel):
    Description: str
    DiscovererArn: str
    DiscovererId: str
    SourceArn: str
    State: DiscovererStateType
    CrossAccount: bool
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRegistryResponseTypeDef(BaseModel):
    Description: str
    RegistryArn: str
    RegistryName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSchemaResponseTypeDef(BaseModel):
    Description: str
    LastModified: datetime
    SchemaArn: str
    SchemaName: str
    SchemaVersion: str
    Tags: Dict[str, str]
    Type: str
    VersionCreatedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCodeBindingResponseTypeDef(BaseModel):
    CreationDate: datetime
    LastModified: datetime
    SchemaVersion: str
    Status: CodeGenerationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDiscovererResponseTypeDef(BaseModel):
    Description: str
    DiscovererArn: str
    DiscovererId: str
    SourceArn: str
    State: DiscovererStateType
    CrossAccount: bool
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRegistryResponseTypeDef(BaseModel):
    Description: str
    RegistryArn: str
    RegistryName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSchemaResponseTypeDef(BaseModel):
    Content: str
    Description: str
    LastModified: datetime
    SchemaArn: str
    SchemaName: str
    SchemaVersion: str
    Tags: Dict[str, str]
    Type: str
    VersionCreatedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ExportSchemaResponseTypeDef(BaseModel):
    Content: str
    SchemaArn: str
    SchemaName: str
    SchemaVersion: str
    Type: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCodeBindingSourceResponseTypeDef(BaseModel):
    Body: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class GetDiscoveredSchemaResponseTypeDef(BaseModel):
    Content: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePolicyResponseTypeDef(BaseModel):
    Policy: str
    RevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutCodeBindingResponseTypeDef(BaseModel):
    CreationDate: datetime
    LastModified: datetime
    SchemaVersion: str
    Status: CodeGenerationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourcePolicyResponseTypeDef(BaseModel):
    Policy: str
    RevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDiscovererResponseTypeDef(BaseModel):
    DiscovererId: str
    State: DiscovererStateType
    ResponseMetadata: ResponseMetadataTypeDef

class StopDiscovererResponseTypeDef(BaseModel):
    DiscovererId: str
    State: DiscovererStateType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDiscovererResponseTypeDef(BaseModel):
    Description: str
    DiscovererArn: str
    DiscovererId: str
    SourceArn: str
    State: DiscovererStateType
    CrossAccount: bool
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRegistryResponseTypeDef(BaseModel):
    Description: str
    RegistryArn: str
    RegistryName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSchemaResponseTypeDef(BaseModel):
    Description: str
    LastModified: datetime
    SchemaArn: str
    SchemaName: str
    SchemaVersion: str
    Tags: Dict[str, str]
    Type: str
    VersionCreatedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCodeBindingRequestCodeBindingExistsWaitTypeDef(BaseModel):
    Language: str
    RegistryName: str
    SchemaName: str
    SchemaVersion: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class ListDiscoverersResponseTypeDef(BaseModel):
    Discoverers: List[DiscovererSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDiscoverersRequestListDiscoverersPaginateTypeDef(BaseModel):
    DiscovererIdPrefix: Optional[str] = None
    SourceArnPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRegistriesRequestListRegistriesPaginateTypeDef(BaseModel):
    RegistryNamePrefix: Optional[str] = None
    Scope: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSchemaVersionsRequestListSchemaVersionsPaginateTypeDef(BaseModel):
    RegistryName: str
    SchemaName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSchemasRequestListSchemasPaginateTypeDef(BaseModel):
    RegistryName: str
    SchemaNamePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchSchemasRequestSearchSchemasPaginateTypeDef(BaseModel):
    Keywords: str
    RegistryName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRegistriesResponseTypeDef(BaseModel):
    NextToken: str
    Registries: List[RegistrySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSchemaVersionsResponseTypeDef(BaseModel):
    NextToken: str
    SchemaVersions: List[SchemaVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSchemasResponseTypeDef(BaseModel):
    NextToken: str
    Schemas: List[SchemaSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SearchSchemaSummaryTypeDef(BaseModel):
    RegistryName: Optional[str] = None
    SchemaArn: Optional[str] = None
    SchemaName: Optional[str] = None
    SchemaVersions: Optional[List[SearchSchemaVersionSummaryTypeDef]] = None

class SearchSchemasResponseTypeDef(BaseModel):
    NextToken: str
    Schemas: List[SearchSchemaSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

