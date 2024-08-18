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
from aws_resource_validator.pydantic_models.finspace_data_constants import *

class AssociateUserToPermissionGroupRequestRequestTypeDef(BaseValidatorModel):
    permissionGroupId: str
    userId: str
    clientToken: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

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

class CreateChangesetRequestRequestTypeDef(BaseValidatorModel):
    datasetId: str
    changeType: ChangeTypeType
    sourceParams: Mapping[str, str]
    formatParams: Mapping[str, str]
    clientToken: Optional[str] = None

class DataViewDestinationTypeParamsTypeDef(BaseValidatorModel):
    destinationType: str
    s3DestinationExportFileFormat: Optional[ExportFileFormatType] = None
    s3DestinationExportFileFormatOptions: Optional[Mapping[str, str]] = None

class DatasetOwnerInfoTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    phoneNumber: Optional[str] = None
    email: Optional[str] = None

class CreatePermissionGroupRequestRequestTypeDef(BaseValidatorModel):
    name: str
    applicationPermissions: Sequence[ApplicationPermissionType]
    description: Optional[str] = None
    clientToken: Optional[str] = None

class CreateUserRequestRequestTypeDef(BaseValidatorModel):
    emailAddress: str
    type: UserTypeType
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    apiAccess: Optional[ApiAccessType] = None
    apiAccessPrincipalArn: Optional[str] = None
    clientToken: Optional[str] = None

class CredentialsTypeDef(BaseValidatorModel):
    accessKeyId: Optional[str] = None
    secretAccessKey: Optional[str] = None
    sessionToken: Optional[str] = None

class DataViewDestinationTypeParamsPaginatorTypeDef(BaseValidatorModel):
    destinationType: str
    s3DestinationExportFileFormat: Optional[ExportFileFormatType] = None
    s3DestinationExportFileFormatOptions: Optional[Dict[str, str]] = None

class DataViewErrorInfoTypeDef(BaseValidatorModel):
    errorMessage: Optional[str] = None
    errorCategory: Optional[ErrorCategoryType] = None

class DeleteDatasetRequestRequestTypeDef(BaseValidatorModel):
    datasetId: str
    clientToken: Optional[str] = None

class DeletePermissionGroupRequestRequestTypeDef(BaseValidatorModel):
    permissionGroupId: str
    clientToken: Optional[str] = None

class DisableUserRequestRequestTypeDef(BaseValidatorModel):
    userId: str
    clientToken: Optional[str] = None

class DisassociateUserFromPermissionGroupRequestRequestTypeDef(BaseValidatorModel):
    permissionGroupId: str
    userId: str
    clientToken: Optional[str] = None

class EnableUserRequestRequestTypeDef(BaseValidatorModel):
    userId: str
    clientToken: Optional[str] = None

class GetChangesetRequestRequestTypeDef(BaseValidatorModel):
    datasetId: str
    changesetId: str

class GetDataViewRequestRequestTypeDef(BaseValidatorModel):
    dataViewId: str
    datasetId: str

class GetDatasetRequestRequestTypeDef(BaseValidatorModel):
    datasetId: str

class GetExternalDataViewAccessDetailsRequestRequestTypeDef(BaseValidatorModel):
    dataViewId: str
    datasetId: str

class S3LocationTypeDef(BaseValidatorModel):
    bucket: str
    key: str

class GetPermissionGroupRequestRequestTypeDef(BaseValidatorModel):
    permissionGroupId: str

class PermissionGroupTypeDef(BaseValidatorModel):
    permissionGroupId: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    applicationPermissions: Optional[List[ApplicationPermissionType]] = None
    createTime: Optional[int] = None
    lastModifiedTime: Optional[int] = None
    membershipStatus: Optional[PermissionGroupMembershipStatusType] = None

class GetProgrammaticAccessCredentialsRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    durationInMinutes: Optional[int] = None

class GetUserRequestRequestTypeDef(BaseValidatorModel):
    userId: str

class GetWorkingLocationRequestRequestTypeDef(BaseValidatorModel):
    locationType: Optional[locationTypeType] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListChangesetsRequestRequestTypeDef(BaseValidatorModel):
    datasetId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListDataViewsRequestRequestTypeDef(BaseValidatorModel):
    datasetId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDatasetsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListPermissionGroupsByUserRequestRequestTypeDef(BaseValidatorModel):
    userId: str
    maxResults: int
    nextToken: Optional[str] = None

class PermissionGroupByUserTypeDef(BaseValidatorModel):
    permissionGroupId: Optional[str] = None
    name: Optional[str] = None
    membershipStatus: Optional[PermissionGroupMembershipStatusType] = None

class ListPermissionGroupsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: int
    nextToken: Optional[str] = None

class ListUsersByPermissionGroupRequestRequestTypeDef(BaseValidatorModel):
    permissionGroupId: str
    maxResults: int
    nextToken: Optional[str] = None

class UserByPermissionGroupTypeDef(BaseValidatorModel):
    userId: Optional[str] = None
    status: Optional[UserStatusType] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    emailAddress: Optional[str] = None
    type: Optional[UserTypeType] = None
    apiAccess: Optional[ApiAccessType] = None
    apiAccessPrincipalArn: Optional[str] = None
    membershipStatus: Optional[PermissionGroupMembershipStatusType] = None

class ListUsersRequestRequestTypeDef(BaseValidatorModel):
    maxResults: int
    nextToken: Optional[str] = None

class UserTypeDef(BaseValidatorModel):
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

class ResourcePermissionTypeDef(BaseValidatorModel):
    permission: Optional[str] = None

class ResetUserPasswordRequestRequestTypeDef(BaseValidatorModel):
    userId: str
    clientToken: Optional[str] = None

class UpdateChangesetRequestRequestTypeDef(BaseValidatorModel):
    datasetId: str
    changesetId: str
    sourceParams: Mapping[str, str]
    formatParams: Mapping[str, str]
    clientToken: Optional[str] = None

class UpdatePermissionGroupRequestRequestTypeDef(BaseValidatorModel):
    permissionGroupId: str
    name: Optional[str] = None
    description: Optional[str] = None
    applicationPermissions: Optional[Sequence[ApplicationPermissionType]] = None
    clientToken: Optional[str] = None

class UpdateUserRequestRequestTypeDef(BaseValidatorModel):
    userId: str
    type: Optional[UserTypeType] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    apiAccess: Optional[ApiAccessType] = None
    apiAccessPrincipalArn: Optional[str] = None
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

class GetUserResponseTypeDef(BaseValidatorModel):
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

class SchemaDefinitionPaginatorTypeDef(BaseValidatorModel):
    columns: Optional[List[ColumnDefinitionTypeDef]] = None
    primaryKeyColumns: Optional[List[str]] = None

class SchemaDefinitionTypeDef(BaseValidatorModel):
    columns: Optional[Sequence[ColumnDefinitionTypeDef]] = None
    primaryKeyColumns: Optional[Sequence[str]] = None

class CreateDataViewRequestRequestTypeDef(BaseValidatorModel):
    datasetId: str
    destinationTypeParams: DataViewDestinationTypeParamsTypeDef
    clientToken: Optional[str] = None
    autoUpdate: Optional[bool] = None
    sortColumns: Optional[Sequence[str]] = None
    partitionColumns: Optional[Sequence[str]] = None
    asOfTimestamp: Optional[int] = None

class GetProgrammaticAccessCredentialsResponseTypeDef(BaseValidatorModel):
    credentials: CredentialsTypeDef
    durationInMinutes: int
    ResponseMetadata: ResponseMetadataTypeDef

class DataViewSummaryPaginatorTypeDef(BaseValidatorModel):
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

class DataViewSummaryTypeDef(BaseValidatorModel):
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
    destinationTypeParams: DataViewDestinationTypeParamsTypeDef
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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListChangesetsRequestListChangesetsPaginateTypeDef(BaseValidatorModel):
    datasetId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataViewsRequestListDataViewsPaginateTypeDef(BaseValidatorModel):
    datasetId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDatasetsRequestListDatasetsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPermissionGroupsRequestListPermissionGroupsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUsersRequestListUsersPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPermissionGroupsByUserResponseTypeDef(BaseValidatorModel):
    permissionGroups: List[PermissionGroupByUserTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListUsersByPermissionGroupResponseTypeDef(BaseValidatorModel):
    users: List[UserByPermissionGroupTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListUsersResponseTypeDef(BaseValidatorModel):
    users: List[UserTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PermissionGroupParamsTypeDef(BaseValidatorModel):
    permissionGroupId: Optional[str] = None
    datasetPermissions: Optional[Sequence[ResourcePermissionTypeDef]] = None

class ListChangesetsResponseTypeDef(BaseValidatorModel):
    changesets: List[ChangesetSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SchemaUnionPaginatorTypeDef(BaseValidatorModel):
    tabularSchemaConfig: Optional[SchemaDefinitionPaginatorTypeDef] = None

class SchemaUnionTypeDef(BaseValidatorModel):
    tabularSchemaConfig: Optional[SchemaDefinitionTypeDef] = None

class ListDataViewsResponsePaginatorTypeDef(BaseValidatorModel):
    nextToken: str
    dataViews: List[DataViewSummaryPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataViewsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    dataViews: List[DataViewSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DatasetPaginatorTypeDef(BaseValidatorModel):
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

class CreateDatasetRequestRequestTypeDef(BaseValidatorModel):
    datasetTitle: str
    kind: DatasetKindType
    permissionGroupParams: PermissionGroupParamsTypeDef
    clientToken: Optional[str] = None
    datasetDescription: Optional[str] = None
    ownerInfo: Optional[DatasetOwnerInfoTypeDef] = None
    alias: Optional[str] = None
    schemaDefinition: Optional[SchemaUnionTypeDef] = None

class DatasetTypeDef(BaseValidatorModel):
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

class GetDatasetResponseTypeDef(BaseValidatorModel):
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

class UpdateDatasetRequestRequestTypeDef(BaseValidatorModel):
    datasetId: str
    datasetTitle: str
    kind: DatasetKindType
    clientToken: Optional[str] = None
    datasetDescription: Optional[str] = None
    alias: Optional[str] = None
    schemaDefinition: Optional[SchemaUnionTypeDef] = None

class ListDatasetsResponsePaginatorTypeDef(BaseValidatorModel):
    datasets: List[DatasetPaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatasetsResponseTypeDef(BaseValidatorModel):
    datasets: List[DatasetTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

