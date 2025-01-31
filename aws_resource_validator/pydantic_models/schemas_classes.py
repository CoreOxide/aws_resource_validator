from datetime import datetime

from botocore.response import StreamingBody

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
from aws_resource_validator.pydantic_models.schemas_constants import *

class CreateDiscovererRequestRequestTypeDef(BaseValidatorModel):
    SourceArn: str
    Description: Optional[str] = None
    CrossAccount: Optional[bool] = None
    Tags: Optional[Mapping[str, str]] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateRegistryRequestRequestTypeDef(BaseValidatorModel):
    RegistryName: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateSchemaRequestRequestTypeDef(BaseValidatorModel):
    Content: str
    RegistryName: str
    SchemaName: str
    Type: TypeType
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class DeleteDiscovererRequestRequestTypeDef(BaseValidatorModel):
    DiscovererId: str

class DeleteRegistryRequestRequestTypeDef(BaseValidatorModel):
    RegistryName: str

class DeleteResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    RegistryName: Optional[str] = None

class DeleteSchemaRequestRequestTypeDef(BaseValidatorModel):
    RegistryName: str
    SchemaName: str

class DeleteSchemaVersionRequestRequestTypeDef(BaseValidatorModel):
    RegistryName: str
    SchemaName: str
    SchemaVersion: str

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeCodeBindingRequestRequestTypeDef(BaseValidatorModel):
    Language: str
    RegistryName: str
    SchemaName: str
    SchemaVersion: Optional[str] = None

class DescribeDiscovererRequestRequestTypeDef(BaseValidatorModel):
    DiscovererId: str

class DescribeRegistryRequestRequestTypeDef(BaseValidatorModel):
    RegistryName: str

class DescribeSchemaRequestRequestTypeDef(BaseValidatorModel):
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

class ExportSchemaRequestRequestTypeDef(BaseValidatorModel):
    RegistryName: str
    SchemaName: str
    Type: str
    SchemaVersion: Optional[str] = None

class GetCodeBindingSourceRequestRequestTypeDef(BaseValidatorModel):
    Language: str
    RegistryName: str
    SchemaName: str
    SchemaVersion: Optional[str] = None

class GetDiscoveredSchemaRequestRequestTypeDef(BaseValidatorModel):
    Events: Sequence[str]
    Type: TypeType

class GetResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    RegistryName: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListDiscoverersRequestRequestTypeDef(BaseValidatorModel):
    DiscovererIdPrefix: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None
    SourceArnPrefix: Optional[str] = None

class ListRegistriesRequestRequestTypeDef(BaseValidatorModel):
    Limit: Optional[int] = None
    NextToken: Optional[str] = None
    RegistryNamePrefix: Optional[str] = None
    Scope: Optional[str] = None

class RegistrySummaryTypeDef(BaseValidatorModel):
    RegistryArn: Optional[str] = None
    RegistryName: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class ListSchemaVersionsRequestRequestTypeDef(BaseValidatorModel):
    RegistryName: str
    SchemaName: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class SchemaVersionSummaryTypeDef(BaseValidatorModel):
    SchemaArn: Optional[str] = None
    SchemaName: Optional[str] = None
    SchemaVersion: Optional[str] = None
    Type: Optional[TypeType] = None

class ListSchemasRequestRequestTypeDef(BaseValidatorModel):
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

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class PutCodeBindingRequestRequestTypeDef(BaseValidatorModel):
    Language: str
    RegistryName: str
    SchemaName: str
    SchemaVersion: Optional[str] = None

class PutResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    Policy: str
    RegistryName: Optional[str] = None
    RevisionId: Optional[str] = None

class SearchSchemaVersionSummaryTypeDef(BaseValidatorModel):
    CreatedDate: Optional[datetime] = None
    SchemaVersion: Optional[str] = None
    Type: Optional[TypeType] = None

class SearchSchemasRequestRequestTypeDef(BaseValidatorModel):
    Keywords: str
    RegistryName: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class StartDiscovererRequestRequestTypeDef(BaseValidatorModel):
    DiscovererId: str

class StopDiscovererRequestRequestTypeDef(BaseValidatorModel):
    DiscovererId: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateDiscovererRequestRequestTypeDef(BaseValidatorModel):
    DiscovererId: str
    Description: Optional[str] = None
    CrossAccount: Optional[bool] = None

class UpdateRegistryRequestRequestTypeDef(BaseValidatorModel):
    RegistryName: str
    Description: Optional[str] = None

class UpdateSchemaRequestRequestTypeDef(BaseValidatorModel):
    RegistryName: str
    SchemaName: str
    ClientTokenId: Optional[str] = None
    Content: Optional[str] = None
    Description: Optional[str] = None
    Type: Optional[TypeType] = None

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

class CreateSchemaResponseTypeDef(BaseValidatorModel):
    Description: str
    LastModified: datetime
    SchemaArn: str
    SchemaName: str
    SchemaVersion: str
    Tags: Dict[str, str]
    Type: str
    VersionCreatedDate: datetime
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

class DescribeSchemaResponseTypeDef(BaseValidatorModel):
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

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ExportSchemaResponseTypeDef(BaseValidatorModel):
    Content: str
    SchemaArn: str
    SchemaName: str
    SchemaVersion: str
    Type: str
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

class UpdateSchemaResponseTypeDef(BaseValidatorModel):
    Description: str
    LastModified: datetime
    SchemaArn: str
    SchemaName: str
    SchemaVersion: str
    Tags: Dict[str, str]
    Type: str
    VersionCreatedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCodeBindingRequestCodeBindingExistsWaitTypeDef(BaseValidatorModel):
    Language: str
    RegistryName: str
    SchemaName: str
    SchemaVersion: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class ListDiscoverersResponseTypeDef(BaseValidatorModel):
    Discoverers: List[DiscovererSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDiscoverersRequestListDiscoverersPaginateTypeDef(BaseValidatorModel):
    DiscovererIdPrefix: Optional[str] = None
    SourceArnPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRegistriesRequestListRegistriesPaginateTypeDef(BaseValidatorModel):
    RegistryNamePrefix: Optional[str] = None
    Scope: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSchemaVersionsRequestListSchemaVersionsPaginateTypeDef(BaseValidatorModel):
    RegistryName: str
    SchemaName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSchemasRequestListSchemasPaginateTypeDef(BaseValidatorModel):
    RegistryName: str
    SchemaNamePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchSchemasRequestSearchSchemasPaginateTypeDef(BaseValidatorModel):
    Keywords: str
    RegistryName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRegistriesResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Registries: List[RegistrySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSchemaVersionsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    SchemaVersions: List[SchemaVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSchemasResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Schemas: List[SchemaSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SearchSchemaSummaryTypeDef(BaseValidatorModel):
    RegistryName: Optional[str] = None
    SchemaArn: Optional[str] = None
    SchemaName: Optional[str] = None
    SchemaVersions: Optional[List[SearchSchemaVersionSummaryTypeDef]] = None

class SearchSchemasResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Schemas: List[SearchSchemaSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

