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


class CreateChangesetRequest(BaseValidatorModel):
    datasetId: str
    changeType: ChangeTypeType
    sourceParams: Mapping[str, str]
    formatParams: Mapping[str, str]
    clientToken: Optional[str] = None


class DatasetOwnerInfo(BaseValidatorModel):
    name: Optional[str] = None
    phoneNumber: Optional[str] = None
    email: Optional[str] = None


class CreatePermissionGroupRequest(BaseValidatorModel):
    name: str
    applicationPermissions: Sequence[ApplicationPermissionType]
    description: Optional[str] = None
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
    s3DestinationExportFileFormatOptions: Optional[Mapping[str, str]] = None


class DataViewErrorInfo(BaseValidatorModel):
    errorMessage: Optional[str] = None
    errorCategory: Optional[ErrorCategoryType] = None


class DeleteDatasetRequest(BaseValidatorModel):
    datasetId: str
    clientToken: Optional[str] = None


class DeletePermissionGroupRequest(BaseValidatorModel):
    permissionGroupId: str
    clientToken: Optional[str] = None


class DisableUserRequest(BaseValidatorModel):
    userId: str
    clientToken: Optional[str] = None


class DisassociateUserFromPermissionGroupRequest(BaseValidatorModel):
    permissionGroupId: str
    userId: str
    clientToken: Optional[str] = None


class EnableUserRequest(BaseValidatorModel):
    userId: str
    clientToken: Optional[str] = None


class GetChangesetRequest(BaseValidatorModel):
    datasetId: str
    changesetId: str


class GetDataViewRequest(BaseValidatorModel):
    dataViewId: str
    datasetId: str


class GetDatasetRequest(BaseValidatorModel):
    datasetId: str


class GetExternalDataViewAccessDetailsRequest(BaseValidatorModel):
    dataViewId: str
    datasetId: str


class S3Location(BaseValidatorModel):
    bucket: str
    key: str


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


class GetProgrammaticAccessCredentialsRequest(BaseValidatorModel):
    environmentId: str
    durationInMinutes: Optional[int] = None


class GetUserRequest(BaseValidatorModel):
    userId: str


class GetWorkingLocationRequest(BaseValidatorModel):
    locationType: Optional[LocationTypeType] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListChangesetsRequest(BaseValidatorModel):
    datasetId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListDataViewsRequest(BaseValidatorModel):
    datasetId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDatasetsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListPermissionGroupsByUserRequest(BaseValidatorModel):
    userId: str
    maxResults: int
    nextToken: Optional[str] = None


class PermissionGroupByUser(BaseValidatorModel):
    permissionGroupId: Optional[str] = None
    name: Optional[str] = None
    membershipStatus: Optional[PermissionGroupMembershipStatusType] = None


class ListPermissionGroupsRequest(BaseValidatorModel):
    maxResults: int
    nextToken: Optional[str] = None


class ListUsersByPermissionGroupRequest(BaseValidatorModel):
    permissionGroupId: str
    maxResults: int
    nextToken: Optional[str] = None


class ListUsersRequest(BaseValidatorModel):
    maxResults: int
    nextToken: Optional[str] = None


class ResourcePermission(BaseValidatorModel):
    permission: Optional[str] = None


class ResetUserPasswordRequest(BaseValidatorModel):
    userId: str
    clientToken: Optional[str] = None


class UpdateChangesetRequest(BaseValidatorModel):
    datasetId: str
    changesetId: str
    sourceParams: Mapping[str, str]
    formatParams: Mapping[str, str]
    clientToken: Optional[str] = None


class UpdatePermissionGroupRequest(BaseValidatorModel):
    permissionGroupId: str
    name: Optional[str] = None
    description: Optional[str] = None
    applicationPermissions: Optional[Sequence[ApplicationPermissionType]] = None
    clientToken: Optional[str] = None


class AssociateUserToPermissionGroupResponse(BaseValidatorModel):
    statusCode: int
    ResponseMetadata: ResponseMetadata


class CreateChangesetResponse(BaseValidatorModel):
    datasetId: str
    changesetId: str
    ResponseMetadata: ResponseMetadata


class CreateDataViewResponse(BaseValidatorModel):
    datasetId: str
    dataViewId: str
    ResponseMetadata: ResponseMetadata


class CreateDatasetResponse(BaseValidatorModel):
    datasetId: str
    ResponseMetadata: ResponseMetadata


class CreatePermissionGroupResponse(BaseValidatorModel):
    permissionGroupId: str
    ResponseMetadata: ResponseMetadata


class CreateUserResponse(BaseValidatorModel):
    userId: str
    ResponseMetadata: ResponseMetadata


class DeleteDatasetResponse(BaseValidatorModel):
    datasetId: str
    ResponseMetadata: ResponseMetadata


class DeletePermissionGroupResponse(BaseValidatorModel):
    permissionGroupId: str
    ResponseMetadata: ResponseMetadata


class DisableUserResponse(BaseValidatorModel):
    userId: str
    ResponseMetadata: ResponseMetadata


class DisassociateUserFromPermissionGroupResponse(BaseValidatorModel):
    statusCode: int
    ResponseMetadata: ResponseMetadata


class EnableUserResponse(BaseValidatorModel):
    userId: str
    ResponseMetadata: ResponseMetadata


class GetWorkingLocationResponse(BaseValidatorModel):
    s3Uri: str
    s3Path: str
    s3Bucket: str
    ResponseMetadata: ResponseMetadata


class ResetUserPasswordResponse(BaseValidatorModel):
    userId: str
    temporaryPassword: str
    ResponseMetadata: ResponseMetadata


class UpdateChangesetResponse(BaseValidatorModel):
    changesetId: str
    datasetId: str
    ResponseMetadata: ResponseMetadata


class UpdateDatasetResponse(BaseValidatorModel):
    datasetId: str
    ResponseMetadata: ResponseMetadata


class UpdatePermissionGroupResponse(BaseValidatorModel):
    permissionGroupId: str
    ResponseMetadata: ResponseMetadata


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
    columns: Optional[Sequence[ColumnDefinition]] = None
    primaryKeyColumns: Optional[Sequence[str]] = None


class GetProgrammaticAccessCredentialsResponse(BaseValidatorModel):
    credentials: Credentials
    durationInMinutes: int
    ResponseMetadata: ResponseMetadata


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


class GetExternalDataViewAccessDetailsResponse(BaseValidatorModel):
    credentials: AwsCredentials
    s3Location: S3Location
    ResponseMetadata: ResponseMetadata


class GetPermissionGroupResponse(BaseValidatorModel):
    permissionGroup: PermissionGroup
    ResponseMetadata: ResponseMetadata


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


class ListPermissionGroupsByUserResponse(BaseValidatorModel):
    permissionGroups: List[PermissionGroupByUser]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UserByPermissionGroup(BaseValidatorModel):
    pass


class ListUsersByPermissionGroupResponse(BaseValidatorModel):
    users: List[UserByPermissionGroup]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class User(BaseValidatorModel):
    pass


class ListUsersResponse(BaseValidatorModel):
    users: List[User]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class PermissionGroupParams(BaseValidatorModel):
    permissionGroupId: Optional[str] = None
    datasetPermissions: Optional[Sequence[ResourcePermission]] = None


class ListChangesetsResponse(BaseValidatorModel):
    changesets: List[ChangesetSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SchemaUnionOutput(BaseValidatorModel):
    tabularSchemaConfig: Optional[SchemaDefinitionOutput] = None


class SchemaUnion(BaseValidatorModel):
    tabularSchemaConfig: Optional[SchemaDefinition] = None


class DataViewDestinationTypeParamsUnion(BaseValidatorModel):
    pass


class CreateDataViewRequest(BaseValidatorModel):
    datasetId: str
    destinationTypeParams: DataViewDestinationTypeParamsUnion
    clientToken: Optional[str] = None
    autoUpdate: Optional[bool] = None
    sortColumns: Optional[Sequence[str]] = None
    partitionColumns: Optional[Sequence[str]] = None
    asOfTimestamp: Optional[int] = None


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


class ListDatasetsResponse(BaseValidatorModel):
    datasets: List[Dataset]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SchemaUnionUnion(BaseValidatorModel):
    pass


class CreateDatasetRequest(BaseValidatorModel):
    datasetTitle: str
    kind: DatasetKindType
    permissionGroupParams: PermissionGroupParams
    clientToken: Optional[str] = None
    datasetDescription: Optional[str] = None
    ownerInfo: Optional[DatasetOwnerInfo] = None
    alias: Optional[str] = None
    schemaDefinition: Optional[SchemaUnionUnion] = None


class UpdateDatasetRequest(BaseValidatorModel):
    datasetId: str
    datasetTitle: str
    kind: DatasetKindType
    clientToken: Optional[str] = None
    datasetDescription: Optional[str] = None
    alias: Optional[str] = None
    schemaDefinition: Optional[SchemaUnionUnion] = None


