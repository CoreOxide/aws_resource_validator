from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.finspace_data.finspace_data_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'associate_user_to_permission_group' function.
class AssociateUserToPermissionGroupRequest(BaseValidatorModel):
    permissionGroupId: str
    userId: str
    clientToken: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AwsCredentials(BaseValidatorModel):
    accessKeyId: Optional[str] = None
    secretAccessKey: Optional[str] = None
    sessionToken: Optional[str] = None
    expiration: Optional[int] = None


class ChangesetErrorInfo(BaseValidatorModel):
    errorMessage: Optional[str] = None
    errorCategory: Optional[ErrorCategoryType] = None


class ColumnDefinition(BaseValidatorModel):
    dataType: Optional[ColumnDataTypeType] = None
    columnName: Optional[str] = None
    columnDescription: Optional[str] = None


# This class is the input for the 'create_changeset' function.
class CreateChangesetRequest(BaseValidatorModel):
    datasetId: str
    changeType: ChangeTypeType
    sourceParams: Dict[str, str]
    formatParams: Dict[str, str]
    clientToken: Optional[str] = None


class DatasetOwnerInfo(BaseValidatorModel):
    name: Optional[str] = None
    phoneNumber: Optional[str] = None
    email: Optional[str] = None


# This class is the input for the 'create_permission_group' function.
class CreatePermissionGroupRequest(BaseValidatorModel):
    name: str
    applicationPermissions: List[ApplicationPermissionType]
    description: Optional[str] = None
    clientToken: Optional[str] = None


# This class is the input for the 'create_user' function.
class CreateUserRequest(BaseValidatorModel):
    emailAddress: str
    type: UserTypeType
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    apiAccess: Optional[ApiAccessType] = None
    apiAccessPrincipalArn: Optional[str] = None
    clientToken: Optional[str] = None


class Credentials(BaseValidatorModel):
    accessKeyId: Optional[str] = None
    secretAccessKey: Optional[str] = None
    sessionToken: Optional[str] = None


class DataViewDestinationTypeParamsOutput(BaseValidatorModel):
    destinationType: str
    s3DestinationExportFileFormat: Optional[ExportFileFormatType] = None
    s3DestinationExportFileFormatOptions: Optional[Dict[str, str]] = None


class DataViewDestinationTypeParams(BaseValidatorModel):
    destinationType: str
    s3DestinationExportFileFormat: Optional[ExportFileFormatType] = None
    s3DestinationExportFileFormatOptions: Optional[Dict[str, str]] = None


class DataViewErrorInfo(BaseValidatorModel):
    errorMessage: Optional[str] = None
    errorCategory: Optional[ErrorCategoryType] = None


# This class is the input for the 'delete_dataset' function.
class DeleteDatasetRequest(BaseValidatorModel):
    datasetId: str
    clientToken: Optional[str] = None


# This class is the input for the 'delete_permission_group' function.
class DeletePermissionGroupRequest(BaseValidatorModel):
    permissionGroupId: str
    clientToken: Optional[str] = None


# This class is the input for the 'disable_user' function.
class DisableUserRequest(BaseValidatorModel):
    userId: str
    clientToken: Optional[str] = None


# This class is the input for the 'disassociate_user_from_permission_group' function.
class DisassociateUserFromPermissionGroupRequest(BaseValidatorModel):
    permissionGroupId: str
    userId: str
    clientToken: Optional[str] = None


# This class is the input for the 'enable_user' function.
class EnableUserRequest(BaseValidatorModel):
    userId: str
    clientToken: Optional[str] = None


# This class is the input for the 'get_changeset' function.
class GetChangesetRequest(BaseValidatorModel):
    datasetId: str
    changesetId: str


# This class is the input for the 'get_data_view' function.
class GetDataViewRequest(BaseValidatorModel):
    dataViewId: str
    datasetId: str


# This class is the input for the 'get_dataset' function.
class GetDatasetRequest(BaseValidatorModel):
    datasetId: str


# This class is the input for the 'get_external_data_view_access_details' function.
class GetExternalDataViewAccessDetailsRequest(BaseValidatorModel):
    dataViewId: str
    datasetId: str


class S3Location(BaseValidatorModel):
    bucket: str
    key: str


# This class is the input for the 'get_permission_group' function.
class GetPermissionGroupRequest(BaseValidatorModel):
    permissionGroupId: str


class PermissionGroup(BaseValidatorModel):
    permissionGroupId: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    applicationPermissions: Optional[List[ApplicationPermissionType]] = None
    createTime: Optional[int] = None
    lastModifiedTime: Optional[int] = None
    membershipStatus: Optional[PermissionGroupMembershipStatusType] = None


# This class is the input for the 'get_programmatic_access_credentials' function.
class GetProgrammaticAccessCredentialsRequest(BaseValidatorModel):
    environmentId: str
    durationInMinutes: Optional[int] = None


# This class is the input for the 'get_user' function.
class GetUserRequest(BaseValidatorModel):
    userId: str


# This class is the input for the 'get_working_location' function.
class GetWorkingLocationRequest(BaseValidatorModel):
    locationType: Optional[LocationTypeType] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_changesets' function.
class ListChangesetsRequest(BaseValidatorModel):
    datasetId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_data_views' function.
class ListDataViewsRequest(BaseValidatorModel):
    datasetId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_datasets' function.
class ListDatasetsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_permission_groups_by_user' function.
class ListPermissionGroupsByUserRequest(BaseValidatorModel):
    userId: str
    maxResults: int
    nextToken: Optional[str] = None


class PermissionGroupByUser(BaseValidatorModel):
    permissionGroupId: Optional[str] = None
    name: Optional[str] = None
    membershipStatus: Optional[PermissionGroupMembershipStatusType] = None


# This class is the input for the 'list_permission_groups' function.
class ListPermissionGroupsRequest(BaseValidatorModel):
    maxResults: int
    nextToken: Optional[str] = None


# This class is the input for the 'list_users_by_permission_group' function.
class ListUsersByPermissionGroupRequest(BaseValidatorModel):
    permissionGroupId: str
    maxResults: int
    nextToken: Optional[str] = None


class UserByPermissionGroup(BaseValidatorModel):
    userId: Optional[str] = None
    status: Optional[UserStatusType] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    emailAddress: Optional[str] = None
    type: Optional[UserTypeType] = None
    apiAccess: Optional[ApiAccessType] = None
    apiAccessPrincipalArn: Optional[str] = None
    membershipStatus: Optional[PermissionGroupMembershipStatusType] = None


# This class is the input for the 'list_users' function.
class ListUsersRequest(BaseValidatorModel):
    maxResults: int
    nextToken: Optional[str] = None


class User(BaseValidatorModel):
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


class ResourcePermission(BaseValidatorModel):
    permission: Optional[str] = None


# This class is the input for the 'reset_user_password' function.
class ResetUserPasswordRequest(BaseValidatorModel):
    userId: str
    clientToken: Optional[str] = None


# This class is the input for the 'update_changeset' function.
class UpdateChangesetRequest(BaseValidatorModel):
    datasetId: str
    changesetId: str
    sourceParams: Dict[str, str]
    formatParams: Dict[str, str]
    clientToken: Optional[str] = None


# This class is the input for the 'update_permission_group' function.
class UpdatePermissionGroupRequest(BaseValidatorModel):
    permissionGroupId: str
    name: Optional[str] = None
    description: Optional[str] = None
    applicationPermissions: Optional[List[ApplicationPermissionType]] = None
    clientToken: Optional[str] = None


# This class is the input for the 'update_user' function.
class UpdateUserRequest(BaseValidatorModel):
    userId: str
    type: Optional[UserTypeType] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    apiAccess: Optional[ApiAccessType] = None
    apiAccessPrincipalArn: Optional[str] = None
    clientToken: Optional[str] = None


# This class is the output for the 'associate_user_to_permission_group' function.
class AssociateUserToPermissionGroupResponse(BaseValidatorModel):
    statusCode: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_changeset' function.
class CreateChangesetResponse(BaseValidatorModel):
    datasetId: str
    changesetId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_data_view' function.
class CreateDataViewResponse(BaseValidatorModel):
    datasetId: str
    dataViewId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_dataset' function.
class CreateDatasetResponse(BaseValidatorModel):
    datasetId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_permission_group' function.
class CreatePermissionGroupResponse(BaseValidatorModel):
    permissionGroupId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_user' function.
class CreateUserResponse(BaseValidatorModel):
    userId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_dataset' function.
class DeleteDatasetResponse(BaseValidatorModel):
    datasetId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_permission_group' function.
class DeletePermissionGroupResponse(BaseValidatorModel):
    permissionGroupId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disable_user' function.
class DisableUserResponse(BaseValidatorModel):
    userId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_user_from_permission_group' function.
class DisassociateUserFromPermissionGroupResponse(BaseValidatorModel):
    statusCode: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'enable_user' function.
class EnableUserResponse(BaseValidatorModel):
    userId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_user' function.
class GetUserResponse(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_working_location' function.
class GetWorkingLocationResponse(BaseValidatorModel):
    s3Uri: str
    s3Path: str
    s3Bucket: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reset_user_password' function.
class ResetUserPasswordResponse(BaseValidatorModel):
    userId: str
    temporaryPassword: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_changeset' function.
class UpdateChangesetResponse(BaseValidatorModel):
    changesetId: str
    datasetId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_dataset' function.
class UpdateDatasetResponse(BaseValidatorModel):
    datasetId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_permission_group' function.
class UpdatePermissionGroupResponse(BaseValidatorModel):
    permissionGroupId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_user' function.
class UpdateUserResponse(BaseValidatorModel):
    userId: str
    ResponseMetadata: ResponseMetadata


class ChangesetSummary(BaseValidatorModel):
    changesetId: Optional[str] = None
    changesetArn: Optional[str] = None
    datasetId: Optional[str] = None
    changeType: Optional[ChangeTypeType] = None
    sourceParams: Optional[Dict[str, str]] = None
    formatParams: Optional[Dict[str, str]] = None
    createTime: Optional[int] = None
    status: Optional[IngestionStatusType] = None
    errorInfo: Optional[ChangesetErrorInfo] = None
    activeUntilTimestamp: Optional[int] = None
    activeFromTimestamp: Optional[int] = None
    updatesChangesetId: Optional[str] = None
    updatedByChangesetId: Optional[str] = None


# This class is the output for the 'get_changeset' function.
class GetChangesetResponse(BaseValidatorModel):
    changesetId: str
    changesetArn: str
    datasetId: str
    changeType: ChangeTypeType
    sourceParams: Dict[str, str]
    formatParams: Dict[str, str]
    createTime: int
    status: IngestionStatusType
    errorInfo: ChangesetErrorInfo
    activeUntilTimestamp: int
    activeFromTimestamp: int
    updatesChangesetId: str
    updatedByChangesetId: str
    ResponseMetadata: ResponseMetadata


class SchemaDefinitionOutput(BaseValidatorModel):
    columns: Optional[List[ColumnDefinition]] = None
    primaryKeyColumns: Optional[List[str]] = None


class SchemaDefinition(BaseValidatorModel):
    columns: Optional[List[ColumnDefinition]] = None
    primaryKeyColumns: Optional[List[str]] = None


# This class is the output for the 'get_programmatic_access_credentials' function.
class GetProgrammaticAccessCredentialsResponse(BaseValidatorModel):
    credentials: Credentials
    durationInMinutes: int
    ResponseMetadata: ResponseMetadata

DataViewDestinationTypeParamsUnion = Union[DataViewDestinationTypeParams, DataViewDestinationTypeParamsOutput]


class DataViewSummary(BaseValidatorModel):
    dataViewId: Optional[str] = None
    dataViewArn: Optional[str] = None
    datasetId: Optional[str] = None
    asOfTimestamp: Optional[int] = None
    partitionColumns: Optional[List[str]] = None
    sortColumns: Optional[List[str]] = None
    status: Optional[DataViewStatusType] = None
    errorInfo: Optional[DataViewErrorInfo] = None
    destinationTypeProperties: Optional[DataViewDestinationTypeParamsOutput] = None
    autoUpdate: Optional[bool] = None
    createTime: Optional[int] = None
    lastModifiedTime: Optional[int] = None


# This class is the output for the 'get_data_view' function.
class GetDataViewResponse(BaseValidatorModel):
    autoUpdate: bool
    partitionColumns: List[str]
    datasetId: str
    asOfTimestamp: int
    errorInfo: DataViewErrorInfo
    lastModifiedTime: int
    createTime: int
    sortColumns: List[str]
    dataViewId: str
    dataViewArn: str
    destinationTypeParams: DataViewDestinationTypeParamsOutput
    status: DataViewStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_external_data_view_access_details' function.
class GetExternalDataViewAccessDetailsResponse(BaseValidatorModel):
    credentials: AwsCredentials
    s3Location: S3Location
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_permission_group' function.
class GetPermissionGroupResponse(BaseValidatorModel):
    permissionGroup: PermissionGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_permission_groups' function.
class ListPermissionGroupsResponse(BaseValidatorModel):
    permissionGroups: List[PermissionGroup]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListChangesetsRequestPaginate(BaseValidatorModel):
    datasetId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDataViewsRequestPaginate(BaseValidatorModel):
    datasetId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDatasetsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPermissionGroupsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListUsersRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_permission_groups_by_user' function.
class ListPermissionGroupsByUserResponse(BaseValidatorModel):
    permissionGroups: List[PermissionGroupByUser]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_users_by_permission_group' function.
class ListUsersByPermissionGroupResponse(BaseValidatorModel):
    users: List[UserByPermissionGroup]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_users' function.
class ListUsersResponse(BaseValidatorModel):
    users: List[User]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class PermissionGroupParams(BaseValidatorModel):
    permissionGroupId: Optional[str] = None
    datasetPermissions: Optional[List[ResourcePermission]] = None


# This class is the output for the 'list_changesets' function.
class ListChangesetsResponse(BaseValidatorModel):
    changesets: List[ChangesetSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SchemaUnionOutput(BaseValidatorModel):
    tabularSchemaConfig: Optional[SchemaDefinitionOutput] = None


class SchemaUnion(BaseValidatorModel):
    tabularSchemaConfig: Optional[SchemaDefinition] = None


# This class is the input for the 'create_data_view' function.
class CreateDataViewRequest(BaseValidatorModel):
    datasetId: str
    destinationTypeParams: DataViewDestinationTypeParamsUnion
    clientToken: Optional[str] = None
    autoUpdate: Optional[bool] = None
    sortColumns: Optional[List[str]] = None
    partitionColumns: Optional[List[str]] = None
    asOfTimestamp: Optional[int] = None


# This class is the output for the 'list_data_views' function.
class ListDataViewsResponse(BaseValidatorModel):
    dataViews: List[DataViewSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Dataset(BaseValidatorModel):
    datasetId: Optional[str] = None
    datasetArn: Optional[str] = None
    datasetTitle: Optional[str] = None
    kind: Optional[DatasetKindType] = None
    datasetDescription: Optional[str] = None
    ownerInfo: Optional[DatasetOwnerInfo] = None
    createTime: Optional[int] = None
    lastModifiedTime: Optional[int] = None
    schemaDefinition: Optional[SchemaUnionOutput] = None
    alias: Optional[str] = None


# This class is the output for the 'get_dataset' function.
class GetDatasetResponse(BaseValidatorModel):
    datasetId: str
    datasetArn: str
    datasetTitle: str
    kind: DatasetKindType
    datasetDescription: str
    createTime: int
    lastModifiedTime: int
    schemaDefinition: SchemaUnionOutput
    alias: str
    status: DatasetStatusType
    ResponseMetadata: ResponseMetadata

SchemaUnionUnion = Union[SchemaUnion, SchemaUnionOutput]


# This class is the output for the 'list_datasets' function.
class ListDatasetsResponse(BaseValidatorModel):
    datasets: List[Dataset]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'create_dataset' function.
class CreateDatasetRequest(BaseValidatorModel):
    datasetTitle: str
    kind: DatasetKindType
    permissionGroupParams: PermissionGroupParams
    clientToken: Optional[str] = None
    datasetDescription: Optional[str] = None
    ownerInfo: Optional[DatasetOwnerInfo] = None
    alias: Optional[str] = None
    schemaDefinition: Optional[SchemaUnionUnion] = None


# This class is the input for the 'update_dataset' function.
class UpdateDatasetRequest(BaseValidatorModel):
    datasetId: str
    datasetTitle: str
    kind: DatasetKindType
    clientToken: Optional[str] = None
    datasetDescription: Optional[str] = None
    alias: Optional[str] = None
    schemaDefinition: Optional[SchemaUnionUnion] = None