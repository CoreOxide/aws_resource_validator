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
from aws_resource_validator.pydantic_models.finspace_data_constants import *

class AssociateUserToPermissionGroupRequestTypeDef(BaseValidatorModel):
    permissionGroupId: str
    userId: str
    clientToken: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AwsCredentialsTypeDef(BaseValidatorModel):
    accessKeyId: Optional[str] = None
    secretAccessKey: Optional[str] = None
    sessionToken: Optional[str] = None
    expiration: Optional[int] = None


class ChangesetErrorInfoTypeDef(BaseValidatorModel):
    errorMessage: Optional[str] = None
    errorCategory: Optional[ErrorCategoryType] = None


class ColumnDefinitionTypeDef(BaseValidatorModel):
    dataType: Optional[ColumnDataTypeType] = None
    columnName: Optional[str] = None
    columnDescription: Optional[str] = None


class CreateChangesetRequestTypeDef(BaseValidatorModel):
    datasetId: str
    changeType: ChangeTypeType
    sourceParams: Mapping[str, str]
    formatParams: Mapping[str, str]
    clientToken: Optional[str] = None


class DatasetOwnerInfoTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    phoneNumber: Optional[str] = None
    email: Optional[str] = None


class CreatePermissionGroupRequestTypeDef(BaseValidatorModel):
    name: str
    applicationPermissions: Sequence[ApplicationPermissionType]
    description: Optional[str] = None
    clientToken: Optional[str] = None


class CredentialsTypeDef(BaseValidatorModel):
    accessKeyId: Optional[str] = None
    secretAccessKey: Optional[str] = None
    sessionToken: Optional[str] = None


class DataViewDestinationTypeParamsOutputTypeDef(BaseValidatorModel):
    destinationType: str
    s3DestinationExportFileFormat: Optional[ExportFileFormatType] = None
    s3DestinationExportFileFormatOptions: Optional[Dict[str, str]] = None


class DataViewDestinationTypeParamsTypeDef(BaseValidatorModel):
    destinationType: str
    s3DestinationExportFileFormat: Optional[ExportFileFormatType] = None
    s3DestinationExportFileFormatOptions: Optional[Mapping[str, str]] = None


class DataViewErrorInfoTypeDef(BaseValidatorModel):
    errorMessage: Optional[str] = None
    errorCategory: Optional[ErrorCategoryType] = None


class DeleteDatasetRequestTypeDef(BaseValidatorModel):
    datasetId: str
    clientToken: Optional[str] = None


class DeletePermissionGroupRequestTypeDef(BaseValidatorModel):
    permissionGroupId: str
    clientToken: Optional[str] = None


class DisableUserRequestTypeDef(BaseValidatorModel):
    userId: str
    clientToken: Optional[str] = None


class DisassociateUserFromPermissionGroupRequestTypeDef(BaseValidatorModel):
    permissionGroupId: str
    userId: str
    clientToken: Optional[str] = None


class EnableUserRequestTypeDef(BaseValidatorModel):
    userId: str
    clientToken: Optional[str] = None


class GetChangesetRequestTypeDef(BaseValidatorModel):
    datasetId: str
    changesetId: str


class GetDataViewRequestTypeDef(BaseValidatorModel):
    dataViewId: str
    datasetId: str


class GetDatasetRequestTypeDef(BaseValidatorModel):
    datasetId: str


class GetExternalDataViewAccessDetailsRequestTypeDef(BaseValidatorModel):
    dataViewId: str
    datasetId: str


class S3LocationTypeDef(BaseValidatorModel):
    bucket: str
    key: str


class GetPermissionGroupRequestTypeDef(BaseValidatorModel):
    permissionGroupId: str


class PermissionGroupTypeDef(BaseValidatorModel):
    permissionGroupId: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    applicationPermissions: Optional[List[ApplicationPermissionType]] = None
    createTime: Optional[int] = None
    lastModifiedTime: Optional[int] = None
    membershipStatus: Optional[PermissionGroupMembershipStatusType] = None


class GetProgrammaticAccessCredentialsRequestTypeDef(BaseValidatorModel):
    environmentId: str
    durationInMinutes: Optional[int] = None


class GetUserRequestTypeDef(BaseValidatorModel):
    userId: str


class GetWorkingLocationRequestTypeDef(BaseValidatorModel):
    locationType: Optional[LocationTypeType] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListChangesetsRequestTypeDef(BaseValidatorModel):
    datasetId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListDataViewsRequestTypeDef(BaseValidatorModel):
    datasetId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDatasetsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListPermissionGroupsByUserRequestTypeDef(BaseValidatorModel):
    userId: str
    maxResults: int
    nextToken: Optional[str] = None


class PermissionGroupByUserTypeDef(BaseValidatorModel):
    permissionGroupId: Optional[str] = None
    name: Optional[str] = None
    membershipStatus: Optional[PermissionGroupMembershipStatusType] = None


class ListPermissionGroupsRequestTypeDef(BaseValidatorModel):
    maxResults: int
    nextToken: Optional[str] = None


class ListUsersByPermissionGroupRequestTypeDef(BaseValidatorModel):
    permissionGroupId: str
    maxResults: int
    nextToken: Optional[str] = None


class ListUsersRequestTypeDef(BaseValidatorModel):
    maxResults: int
    nextToken: Optional[str] = None


class ResourcePermissionTypeDef(BaseValidatorModel):
    permission: Optional[str] = None


class ResetUserPasswordRequestTypeDef(BaseValidatorModel):
    userId: str
    clientToken: Optional[str] = None


class UpdateChangesetRequestTypeDef(BaseValidatorModel):
    datasetId: str
    changesetId: str
    sourceParams: Mapping[str, str]
    formatParams: Mapping[str, str]
    clientToken: Optional[str] = None


class UpdatePermissionGroupRequestTypeDef(BaseValidatorModel):
    permissionGroupId: str
    name: Optional[str] = None
    description: Optional[str] = None
    applicationPermissions: Optional[Sequence[ApplicationPermissionType]] = None
    clientToken: Optional[str] = None


class AssociateUserToPermissionGroupResponseTypeDef(BaseValidatorModel):
    statusCode: int
    ResponseMetadata: ResponseMetadataTypeDef


class CreateChangesetResponseTypeDef(BaseValidatorModel):
    datasetId: str
    changesetId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDataViewResponseTypeDef(BaseValidatorModel):
    datasetId: str
    dataViewId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDatasetResponseTypeDef(BaseValidatorModel):
    datasetId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePermissionGroupResponseTypeDef(BaseValidatorModel):
    permissionGroupId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateUserResponseTypeDef(BaseValidatorModel):
    userId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDatasetResponseTypeDef(BaseValidatorModel):
    datasetId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeletePermissionGroupResponseTypeDef(BaseValidatorModel):
    permissionGroupId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DisableUserResponseTypeDef(BaseValidatorModel):
    userId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DisassociateUserFromPermissionGroupResponseTypeDef(BaseValidatorModel):
    statusCode: int
    ResponseMetadata: ResponseMetadataTypeDef


class EnableUserResponseTypeDef(BaseValidatorModel):
    userId: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetWorkingLocationResponseTypeDef(BaseValidatorModel):
    s3Uri: str
    s3Path: str
    s3Bucket: str
    ResponseMetadata: ResponseMetadataTypeDef


class ResetUserPasswordResponseTypeDef(BaseValidatorModel):
    userId: str
    temporaryPassword: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateChangesetResponseTypeDef(BaseValidatorModel):
    changesetId: str
    datasetId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDatasetResponseTypeDef(BaseValidatorModel):
    datasetId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePermissionGroupResponseTypeDef(BaseValidatorModel):
    permissionGroupId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateUserResponseTypeDef(BaseValidatorModel):
    userId: str
    ResponseMetadata: ResponseMetadataTypeDef


class ChangesetSummaryTypeDef(BaseValidatorModel):
    changesetId: Optional[str] = None
    changesetArn: Optional[str] = None
    datasetId: Optional[str] = None
    changeType: Optional[ChangeTypeType] = None
    sourceParams: Optional[Dict[str, str]] = None
    formatParams: Optional[Dict[str, str]] = None
    createTime: Optional[int] = None
    status: Optional[IngestionStatusType] = None
    errorInfo: Optional[ChangesetErrorInfoTypeDef] = None
    activeUntilTimestamp: Optional[int] = None
    activeFromTimestamp: Optional[int] = None
    updatesChangesetId: Optional[str] = None
    updatedByChangesetId: Optional[str] = None


class GetChangesetResponseTypeDef(BaseValidatorModel):
    changesetId: str
    changesetArn: str
    datasetId: str
    changeType: ChangeTypeType
    sourceParams: Dict[str, str]
    formatParams: Dict[str, str]
    createTime: int
    status: IngestionStatusType
    errorInfo: ChangesetErrorInfoTypeDef
    activeUntilTimestamp: int
    activeFromTimestamp: int
    updatesChangesetId: str
    updatedByChangesetId: str
    ResponseMetadata: ResponseMetadataTypeDef


class SchemaDefinitionOutputTypeDef(BaseValidatorModel):
    columns: Optional[List[ColumnDefinitionTypeDef]] = None
    primaryKeyColumns: Optional[List[str]] = None


class SchemaDefinitionTypeDef(BaseValidatorModel):
    columns: Optional[Sequence[ColumnDefinitionTypeDef]] = None
    primaryKeyColumns: Optional[Sequence[str]] = None


class GetProgrammaticAccessCredentialsResponseTypeDef(BaseValidatorModel):
    credentials: CredentialsTypeDef
    durationInMinutes: int
    ResponseMetadata: ResponseMetadataTypeDef


class DataViewSummaryTypeDef(BaseValidatorModel):
    dataViewId: Optional[str] = None
    dataViewArn: Optional[str] = None
    datasetId: Optional[str] = None
    asOfTimestamp: Optional[int] = None
    partitionColumns: Optional[List[str]] = None
    sortColumns: Optional[List[str]] = None
    status: Optional[DataViewStatusType] = None
    errorInfo: Optional[DataViewErrorInfoTypeDef] = None
    destinationTypeProperties: Optional[DataViewDestinationTypeParamsOutputTypeDef] = None
    autoUpdate: Optional[bool] = None
    createTime: Optional[int] = None
    lastModifiedTime: Optional[int] = None


class GetDataViewResponseTypeDef(BaseValidatorModel):
    autoUpdate: bool
    partitionColumns: List[str]
    datasetId: str
    asOfTimestamp: int
    errorInfo: DataViewErrorInfoTypeDef
    lastModifiedTime: int
    createTime: int
    sortColumns: List[str]
    dataViewId: str
    dataViewArn: str
    destinationTypeParams: DataViewDestinationTypeParamsOutputTypeDef
    status: DataViewStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class GetExternalDataViewAccessDetailsResponseTypeDef(BaseValidatorModel):
    credentials: AwsCredentialsTypeDef
    s3Location: S3LocationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetPermissionGroupResponseTypeDef(BaseValidatorModel):
    permissionGroup: PermissionGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListPermissionGroupsResponseTypeDef(BaseValidatorModel):
    permissionGroups: List[PermissionGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListChangesetsRequestPaginateTypeDef(BaseValidatorModel):
    datasetId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDataViewsRequestPaginateTypeDef(BaseValidatorModel):
    datasetId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDatasetsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPermissionGroupsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListUsersRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPermissionGroupsByUserResponseTypeDef(BaseValidatorModel):
    permissionGroups: List[PermissionGroupByUserTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UserByPermissionGroupTypeDef(BaseValidatorModel):
    pass


class ListUsersByPermissionGroupResponseTypeDef(BaseValidatorModel):
    users: List[UserByPermissionGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UserTypeDef(BaseValidatorModel):
    pass


class ListUsersResponseTypeDef(BaseValidatorModel):
    users: List[UserTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PermissionGroupParamsTypeDef(BaseValidatorModel):
    permissionGroupId: Optional[str] = None
    datasetPermissions: Optional[Sequence[ResourcePermissionTypeDef]] = None


class ListChangesetsResponseTypeDef(BaseValidatorModel):
    changesets: List[ChangesetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SchemaUnionOutputTypeDef(BaseValidatorModel):
    tabularSchemaConfig: Optional[SchemaDefinitionOutputTypeDef] = None


class SchemaUnionTypeDef(BaseValidatorModel):
    tabularSchemaConfig: Optional[SchemaDefinitionTypeDef] = None


class DataViewDestinationTypeParamsUnionTypeDef(BaseValidatorModel):
    pass


class CreateDataViewRequestTypeDef(BaseValidatorModel):
    datasetId: str
    destinationTypeParams: DataViewDestinationTypeParamsUnionTypeDef
    clientToken: Optional[str] = None
    autoUpdate: Optional[bool] = None
    sortColumns: Optional[Sequence[str]] = None
    partitionColumns: Optional[Sequence[str]] = None
    asOfTimestamp: Optional[int] = None


class ListDataViewsResponseTypeDef(BaseValidatorModel):
    dataViews: List[DataViewSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DatasetTypeDef(BaseValidatorModel):
    datasetId: Optional[str] = None
    datasetArn: Optional[str] = None
    datasetTitle: Optional[str] = None
    kind: Optional[DatasetKindType] = None
    datasetDescription: Optional[str] = None
    ownerInfo: Optional[DatasetOwnerInfoTypeDef] = None
    createTime: Optional[int] = None
    lastModifiedTime: Optional[int] = None
    schemaDefinition: Optional[SchemaUnionOutputTypeDef] = None
    alias: Optional[str] = None


class GetDatasetResponseTypeDef(BaseValidatorModel):
    datasetId: str
    datasetArn: str
    datasetTitle: str
    kind: DatasetKindType
    datasetDescription: str
    createTime: int
    lastModifiedTime: int
    schemaDefinition: SchemaUnionOutputTypeDef
    alias: str
    status: DatasetStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class ListDatasetsResponseTypeDef(BaseValidatorModel):
    datasets: List[DatasetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SchemaUnionUnionTypeDef(BaseValidatorModel):
    pass


class CreateDatasetRequestTypeDef(BaseValidatorModel):
    datasetTitle: str
    kind: DatasetKindType
    permissionGroupParams: PermissionGroupParamsTypeDef
    clientToken: Optional[str] = None
    datasetDescription: Optional[str] = None
    ownerInfo: Optional[DatasetOwnerInfoTypeDef] = None
    alias: Optional[str] = None
    schemaDefinition: Optional[SchemaUnionUnionTypeDef] = None


class UpdateDatasetRequestTypeDef(BaseValidatorModel):
    datasetId: str
    datasetTitle: str
    kind: DatasetKindType
    clientToken: Optional[str] = None
    datasetDescription: Optional[str] = None
    alias: Optional[str] = None
    schemaDefinition: Optional[SchemaUnionUnionTypeDef] = None


