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
from aws_resource_validator.pydantic_models.finspace_data_constants import *

class AssociateUserToPermissionGroupRequestRequestTypeDef(BaseModel):
    permissionGroupId: str
    userId: str
    clientToken: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class AwsCredentialsTypeDef(BaseModel):
    accessKeyId: Optional[str] = None
    secretAccessKey: Optional[str] = None
    sessionToken: Optional[str] = None
    expiration: Optional[int] = None

class ChangesetErrorInfoTypeDef(BaseModel):
    errorMessage: Optional[str] = None
    errorCategory: Optional[ErrorCategoryType] = None

class ColumnDefinitionTypeDef(BaseModel):
    dataType: Optional[ColumnDataTypeType] = None
    columnName: Optional[str] = None
    columnDescription: Optional[str] = None

class CreateChangesetRequestRequestTypeDef(BaseModel):
    datasetId: str
    changeType: ChangeTypeType
    sourceParams: Mapping[str, str]
    formatParams: Mapping[str, str]
    clientToken: Optional[str] = None

class DataViewDestinationTypeParamsTypeDef(BaseModel):
    destinationType: str
    s3DestinationExportFileFormat: Optional[ExportFileFormatType] = None
    s3DestinationExportFileFormatOptions: Optional[Mapping[str, str]] = None

class DatasetOwnerInfoTypeDef(BaseModel):
    name: Optional[str] = None
    phoneNumber: Optional[str] = None
    email: Optional[str] = None

class CreatePermissionGroupRequestRequestTypeDef(BaseModel):
    name: str
    applicationPermissions: Sequence[ApplicationPermissionType]
    description: Optional[str] = None
    clientToken: Optional[str] = None

class CreateUserRequestRequestTypeDef(BaseModel):
    emailAddress: str
    type: UserTypeType
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    apiAccess: Optional[ApiAccessType] = None
    apiAccessPrincipalArn: Optional[str] = None
    clientToken: Optional[str] = None

class CredentialsTypeDef(BaseModel):
    accessKeyId: Optional[str] = None
    secretAccessKey: Optional[str] = None
    sessionToken: Optional[str] = None

class DataViewDestinationTypeParamsPaginatorTypeDef(BaseModel):
    destinationType: str
    s3DestinationExportFileFormat: Optional[ExportFileFormatType] = None
    s3DestinationExportFileFormatOptions: Optional[Dict[str, str]] = None

class DataViewErrorInfoTypeDef(BaseModel):
    errorMessage: Optional[str] = None
    errorCategory: Optional[ErrorCategoryType] = None

class DeleteDatasetRequestRequestTypeDef(BaseModel):
    datasetId: str
    clientToken: Optional[str] = None

class DeletePermissionGroupRequestRequestTypeDef(BaseModel):
    permissionGroupId: str
    clientToken: Optional[str] = None

class DisableUserRequestRequestTypeDef(BaseModel):
    userId: str
    clientToken: Optional[str] = None

class DisassociateUserFromPermissionGroupRequestRequestTypeDef(BaseModel):
    permissionGroupId: str
    userId: str
    clientToken: Optional[str] = None

class EnableUserRequestRequestTypeDef(BaseModel):
    userId: str
    clientToken: Optional[str] = None

class GetChangesetRequestRequestTypeDef(BaseModel):
    datasetId: str
    changesetId: str

class GetDataViewRequestRequestTypeDef(BaseModel):
    dataViewId: str
    datasetId: str

class GetDatasetRequestRequestTypeDef(BaseModel):
    datasetId: str

class GetExternalDataViewAccessDetailsRequestRequestTypeDef(BaseModel):
    dataViewId: str
    datasetId: str

class S3LocationTypeDef(BaseModel):
    bucket: str
    key: str

class GetPermissionGroupRequestRequestTypeDef(BaseModel):
    permissionGroupId: str

class PermissionGroupTypeDef(BaseModel):
    permissionGroupId: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    applicationPermissions: Optional[List[ApplicationPermissionType]] = None
    createTime: Optional[int] = None
    lastModifiedTime: Optional[int] = None
    membershipStatus: Optional[PermissionGroupMembershipStatusType] = None

class GetProgrammaticAccessCredentialsRequestRequestTypeDef(BaseModel):
    environmentId: str
    durationInMinutes: Optional[int] = None

class GetUserRequestRequestTypeDef(BaseModel):
    userId: str

class GetWorkingLocationRequestRequestTypeDef(BaseModel):
    locationType: Optional[locationTypeType] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListChangesetsRequestRequestTypeDef(BaseModel):
    datasetId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListDataViewsRequestRequestTypeDef(BaseModel):
    datasetId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDatasetsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListPermissionGroupsByUserRequestRequestTypeDef(BaseModel):
    userId: str
    maxResults: int
    nextToken: Optional[str] = None

class PermissionGroupByUserTypeDef(BaseModel):
    permissionGroupId: Optional[str] = None
    name: Optional[str] = None
    membershipStatus: Optional[PermissionGroupMembershipStatusType] = None

class ListPermissionGroupsRequestRequestTypeDef(BaseModel):
    maxResults: int
    nextToken: Optional[str] = None

class ListUsersByPermissionGroupRequestRequestTypeDef(BaseModel):
    permissionGroupId: str
    maxResults: int
    nextToken: Optional[str] = None

class UserByPermissionGroupTypeDef(BaseModel):
    userId: Optional[str] = None
    status: Optional[UserStatusType] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    emailAddress: Optional[str] = None
    type: Optional[UserTypeType] = None
    apiAccess: Optional[ApiAccessType] = None
    apiAccessPrincipalArn: Optional[str] = None
    membershipStatus: Optional[PermissionGroupMembershipStatusType] = None

class ListUsersRequestRequestTypeDef(BaseModel):
    maxResults: int
    nextToken: Optional[str] = None

class UserTypeDef(BaseModel):
    userId: Optional[str] = None
    status: Optional[UserStatusType] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    emailAddress: Optional[str] = None
    type: Optional[UserTypeType] = None
    apiAccess: Optional[ApiAccessType] = None
    apiAccessPrincipalArn: Optional[str] = None
    createTime: Optional[int] = None
    lastEnabledTime: Optional[int] = None
    lastDisabledTime: Optional[int] = None
    lastModifiedTime: Optional[int] = None
    lastLoginTime: Optional[int] = None

class ResourcePermissionTypeDef(BaseModel):
    permission: Optional[str] = None

class ResetUserPasswordRequestRequestTypeDef(BaseModel):
    userId: str
    clientToken: Optional[str] = None

class UpdateChangesetRequestRequestTypeDef(BaseModel):
    datasetId: str
    changesetId: str
    sourceParams: Mapping[str, str]
    formatParams: Mapping[str, str]
    clientToken: Optional[str] = None

class UpdatePermissionGroupRequestRequestTypeDef(BaseModel):
    permissionGroupId: str
    name: Optional[str] = None
    description: Optional[str] = None
    applicationPermissions: Optional[Sequence[ApplicationPermissionType]] = None
    clientToken: Optional[str] = None

class UpdateUserRequestRequestTypeDef(BaseModel):
    userId: str
    type: Optional[UserTypeType] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    apiAccess: Optional[ApiAccessType] = None
    apiAccessPrincipalArn: Optional[str] = None
    clientToken: Optional[str] = None

class AssociateUserToPermissionGroupResponseTypeDef(BaseModel):
    statusCode: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChangesetResponseTypeDef(BaseModel):
    datasetId: str
    changesetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataViewResponseTypeDef(BaseModel):
    datasetId: str
    dataViewId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatasetResponseTypeDef(BaseModel):
    datasetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePermissionGroupResponseTypeDef(BaseModel):
    permissionGroupId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserResponseTypeDef(BaseModel):
    userId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDatasetResponseTypeDef(BaseModel):
    datasetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePermissionGroupResponseTypeDef(BaseModel):
    permissionGroupId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisableUserResponseTypeDef(BaseModel):
    userId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateUserFromPermissionGroupResponseTypeDef(BaseModel):
    statusCode: int
    ResponseMetadata: ResponseMetadataTypeDef

class EnableUserResponseTypeDef(BaseModel):
    userId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetUserResponseTypeDef(BaseModel):
    userId: str
    status: UserStatusType
    firstName: str
    lastName: str
    emailAddress: str
    type: UserTypeType
    apiAccess: ApiAccessType
    apiAccessPrincipalArn: str
    createTime: int
    lastEnabledTime: int
    lastDisabledTime: int
    lastModifiedTime: int
    lastLoginTime: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorkingLocationResponseTypeDef(BaseModel):
    s3Uri: str
    s3Path: str
    s3Bucket: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResetUserPasswordResponseTypeDef(BaseModel):
    userId: str
    temporaryPassword: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChangesetResponseTypeDef(BaseModel):
    changesetId: str
    datasetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDatasetResponseTypeDef(BaseModel):
    datasetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePermissionGroupResponseTypeDef(BaseModel):
    permissionGroupId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserResponseTypeDef(BaseModel):
    userId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ChangesetSummaryTypeDef(BaseModel):
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

class GetChangesetResponseTypeDef(BaseModel):
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

class SchemaDefinitionPaginatorTypeDef(BaseModel):
    columns: Optional[List[ColumnDefinitionTypeDef]] = None
    primaryKeyColumns: Optional[List[str]] = None

class SchemaDefinitionTypeDef(BaseModel):
    columns: Optional[Sequence[ColumnDefinitionTypeDef]] = None
    primaryKeyColumns: Optional[Sequence[str]] = None

class CreateDataViewRequestRequestTypeDef(BaseModel):
    datasetId: str
    destinationTypeParams: DataViewDestinationTypeParamsTypeDef
    clientToken: Optional[str] = None
    autoUpdate: Optional[bool] = None
    sortColumns: Optional[Sequence[str]] = None
    partitionColumns: Optional[Sequence[str]] = None
    asOfTimestamp: Optional[int] = None

class GetProgrammaticAccessCredentialsResponseTypeDef(BaseModel):
    credentials: CredentialsTypeDef
    durationInMinutes: int
    ResponseMetadata: ResponseMetadataTypeDef

class DataViewSummaryPaginatorTypeDef(BaseModel):
    dataViewId: Optional[str] = None
    dataViewArn: Optional[str] = None
    datasetId: Optional[str] = None
    asOfTimestamp: Optional[int] = None
    partitionColumns: Optional[List[str]] = None
    sortColumns: Optional[List[str]] = None
    status: Optional[DataViewStatusType] = None
    errorInfo: Optional[DataViewErrorInfoTypeDef] = None
    destinationTypeProperties: Optional[DataViewDestinationTypeParamsPaginatorTypeDef] = None
    autoUpdate: Optional[bool] = None
    createTime: Optional[int] = None
    lastModifiedTime: Optional[int] = None

class DataViewSummaryTypeDef(BaseModel):
    dataViewId: Optional[str] = None
    dataViewArn: Optional[str] = None
    datasetId: Optional[str] = None
    asOfTimestamp: Optional[int] = None
    partitionColumns: Optional[List[str]] = None
    sortColumns: Optional[List[str]] = None
    status: Optional[DataViewStatusType] = None
    errorInfo: Optional[DataViewErrorInfoTypeDef] = None
    destinationTypeProperties: Optional[DataViewDestinationTypeParamsTypeDef] = None
    autoUpdate: Optional[bool] = None
    createTime: Optional[int] = None
    lastModifiedTime: Optional[int] = None

class GetDataViewResponseTypeDef(BaseModel):
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
    destinationTypeParams: DataViewDestinationTypeParamsTypeDef
    status: DataViewStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetExternalDataViewAccessDetailsResponseTypeDef(BaseModel):
    credentials: AwsCredentialsTypeDef
    s3Location: S3LocationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPermissionGroupResponseTypeDef(BaseModel):
    permissionGroup: PermissionGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPermissionGroupsResponseTypeDef(BaseModel):
    permissionGroups: List[PermissionGroupTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListChangesetsRequestListChangesetsPaginateTypeDef(BaseModel):
    datasetId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataViewsRequestListDataViewsPaginateTypeDef(BaseModel):
    datasetId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDatasetsRequestListDatasetsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPermissionGroupsRequestListPermissionGroupsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUsersRequestListUsersPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPermissionGroupsByUserResponseTypeDef(BaseModel):
    permissionGroups: List[PermissionGroupByUserTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListUsersByPermissionGroupResponseTypeDef(BaseModel):
    users: List[UserByPermissionGroupTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListUsersResponseTypeDef(BaseModel):
    users: List[UserTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PermissionGroupParamsTypeDef(BaseModel):
    permissionGroupId: Optional[str] = None
    datasetPermissions: Optional[Sequence[ResourcePermissionTypeDef]] = None

class ListChangesetsResponseTypeDef(BaseModel):
    changesets: List[ChangesetSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SchemaUnionPaginatorTypeDef(BaseModel):
    tabularSchemaConfig: Optional[SchemaDefinitionPaginatorTypeDef] = None

class SchemaUnionTypeDef(BaseModel):
    tabularSchemaConfig: Optional[SchemaDefinitionTypeDef] = None

class ListDataViewsResponsePaginatorTypeDef(BaseModel):
    nextToken: str
    dataViews: List[DataViewSummaryPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataViewsResponseTypeDef(BaseModel):
    nextToken: str
    dataViews: List[DataViewSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DatasetPaginatorTypeDef(BaseModel):
    datasetId: Optional[str] = None
    datasetArn: Optional[str] = None
    datasetTitle: Optional[str] = None
    kind: Optional[DatasetKindType] = None
    datasetDescription: Optional[str] = None
    ownerInfo: Optional[DatasetOwnerInfoTypeDef] = None
    createTime: Optional[int] = None
    lastModifiedTime: Optional[int] = None
    schemaDefinition: Optional[SchemaUnionPaginatorTypeDef] = None
    alias: Optional[str] = None

class CreateDatasetRequestRequestTypeDef(BaseModel):
    datasetTitle: str
    kind: DatasetKindType
    permissionGroupParams: PermissionGroupParamsTypeDef
    clientToken: Optional[str] = None
    datasetDescription: Optional[str] = None
    ownerInfo: Optional[DatasetOwnerInfoTypeDef] = None
    alias: Optional[str] = None
    schemaDefinition: Optional[SchemaUnionTypeDef] = None

class DatasetTypeDef(BaseModel):
    datasetId: Optional[str] = None
    datasetArn: Optional[str] = None
    datasetTitle: Optional[str] = None
    kind: Optional[DatasetKindType] = None
    datasetDescription: Optional[str] = None
    ownerInfo: Optional[DatasetOwnerInfoTypeDef] = None
    createTime: Optional[int] = None
    lastModifiedTime: Optional[int] = None
    schemaDefinition: Optional[SchemaUnionTypeDef] = None
    alias: Optional[str] = None

class GetDatasetResponseTypeDef(BaseModel):
    datasetId: str
    datasetArn: str
    datasetTitle: str
    kind: DatasetKindType
    datasetDescription: str
    createTime: int
    lastModifiedTime: int
    schemaDefinition: SchemaUnionTypeDef
    alias: str
    status: DatasetStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDatasetRequestRequestTypeDef(BaseModel):
    datasetId: str
    datasetTitle: str
    kind: DatasetKindType
    clientToken: Optional[str] = None
    datasetDescription: Optional[str] = None
    alias: Optional[str] = None
    schemaDefinition: Optional[SchemaUnionTypeDef] = None

class ListDatasetsResponsePaginatorTypeDef(BaseModel):
    datasets: List[DatasetPaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatasetsResponseTypeDef(BaseModel):
    datasets: List[DatasetTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

