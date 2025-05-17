from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.appfabric.appfabric_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ApiKeyCredential(BaseValidatorModel):
    apiKey: str


class Tenant(BaseValidatorModel):
    tenantIdentifier: str
    tenantDisplayName: str


class AppBundleSummary(BaseValidatorModel):
    arn: str


class AppBundle(BaseValidatorModel):
    arn: str
    customerManagedKeyArn: Optional[str] = None


class AuditLogProcessingConfiguration(BaseValidatorModel):
    schema: SchemaType
    format: FormatType


class AuthRequest(BaseValidatorModel):
    redirectUri: str
    code: str


# This class is the input for the 'batch_get_user_access_tasks' function.
class BatchGetUserAccessTasksRequest(BaseValidatorModel):
    appBundleIdentifier: str
    taskIdList: List[str]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Tag(BaseValidatorModel):
    key: str
    value: str


class Ingestion(BaseValidatorModel):
    arn: str
    appBundleArn: str
    app: str
    tenantId: str
    createdAt: datetime
    updatedAt: datetime
    state: IngestionStateType
    ingestionType: Literal['auditLog']


class Oauth2Credential(BaseValidatorModel):
    clientId: str
    clientSecret: str


class DeleteAppAuthorizationRequest(BaseValidatorModel):
    appBundleIdentifier: str
    appAuthorizationIdentifier: str


class DeleteAppBundleRequest(BaseValidatorModel):
    appBundleIdentifier: str


class DeleteIngestionDestinationRequest(BaseValidatorModel):
    appBundleIdentifier: str
    ingestionIdentifier: str
    ingestionDestinationIdentifier: str


class DeleteIngestionRequest(BaseValidatorModel):
    appBundleIdentifier: str
    ingestionIdentifier: str


class FirehoseStream(BaseValidatorModel):
    streamName: str


class S3Bucket(BaseValidatorModel):
    bucketName: str
    prefix: Optional[str] = None


# This class is the input for the 'get_app_authorization' function.
class GetAppAuthorizationRequest(BaseValidatorModel):
    appBundleIdentifier: str
    appAuthorizationIdentifier: str


# This class is the input for the 'get_app_bundle' function.
class GetAppBundleRequest(BaseValidatorModel):
    appBundleIdentifier: str


# This class is the input for the 'get_ingestion_destination' function.
class GetIngestionDestinationRequest(BaseValidatorModel):
    appBundleIdentifier: str
    ingestionIdentifier: str
    ingestionDestinationIdentifier: str


# This class is the input for the 'get_ingestion' function.
class GetIngestionRequest(BaseValidatorModel):
    appBundleIdentifier: str
    ingestionIdentifier: str


class IngestionDestinationSummary(BaseValidatorModel):
    arn: str


class IngestionSummary(BaseValidatorModel):
    arn: str
    app: str
    tenantId: str
    state: IngestionStateType


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_app_authorizations' function.
class ListAppAuthorizationsRequest(BaseValidatorModel):
    appBundleIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_app_bundles' function.
class ListAppBundlesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_ingestion_destinations' function.
class ListIngestionDestinationsRequest(BaseValidatorModel):
    appBundleIdentifier: str
    ingestionIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_ingestions' function.
class ListIngestionsRequest(BaseValidatorModel):
    appBundleIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class StartIngestionRequest(BaseValidatorModel):
    ingestionIdentifier: str
    appBundleIdentifier: str


# This class is the input for the 'start_user_access_tasks' function.
class StartUserAccessTasksRequest(BaseValidatorModel):
    appBundleIdentifier: str
    email: str


class StopIngestionRequest(BaseValidatorModel):
    ingestionIdentifier: str
    appBundleIdentifier: str


class TaskError(BaseValidatorModel):
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class AppAuthorizationSummary(BaseValidatorModel):
    appAuthorizationArn: str
    appBundleArn: str
    app: str
    tenant: Tenant
    status: AppAuthorizationStatusType
    updatedAt: datetime


class AppAuthorization(BaseValidatorModel):
    appAuthorizationArn: str
    appBundleArn: str
    app: str
    tenant: Tenant
    authType: AuthTypeType
    status: AppAuthorizationStatusType
    createdAt: datetime
    updatedAt: datetime
    persona: Optional[PersonaType] = None
    authUrl: Optional[str] = None


class ProcessingConfiguration(BaseValidatorModel):
    auditLog: Optional[AuditLogProcessingConfiguration] = None


# This class is the input for the 'connect_app_authorization' function.
class ConnectAppAuthorizationRequest(BaseValidatorModel):
    appBundleIdentifier: str
    appAuthorizationIdentifier: str
    authRequest: Optional[AuthRequest] = None


# This class is the output for the 'create_app_bundle' function.
class CreateAppBundleResponse(BaseValidatorModel):
    appBundle: AppBundle
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_app_bundle' function.
class GetAppBundleResponse(BaseValidatorModel):
    appBundle: AppBundle
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_app_bundles' function.
class ListAppBundlesResponse(BaseValidatorModel):
    appBundleSummaryList: List[AppBundleSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'create_app_bundle' function.
class CreateAppBundleRequest(BaseValidatorModel):
    clientToken: Optional[str] = None
    customerManagedKeyIdentifier: Optional[str] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'create_ingestion' function.
class CreateIngestionRequest(BaseValidatorModel):
    appBundleIdentifier: str
    app: str
    tenantId: str
    ingestionType: Literal['auditLog']
    clientToken: Optional[str] = None
    tags: Optional[List[Tag]] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: List[Tag]


# This class is the output for the 'create_ingestion' function.
class CreateIngestionResponse(BaseValidatorModel):
    ingestion: Ingestion
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_ingestion' function.
class GetIngestionResponse(BaseValidatorModel):
    ingestion: Ingestion
    ResponseMetadata: ResponseMetadata


class Credential(BaseValidatorModel):
    oauth2Credential: Optional[Oauth2Credential] = None
    apiKeyCredential: Optional[ApiKeyCredential] = None


class Destination(BaseValidatorModel):
    s3Bucket: Optional[S3Bucket] = None
    firehoseStream: Optional[FirehoseStream] = None


# This class is the output for the 'list_ingestion_destinations' function.
class ListIngestionDestinationsResponse(BaseValidatorModel):
    ingestionDestinations: List[IngestionDestinationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_ingestions' function.
class ListIngestionsResponse(BaseValidatorModel):
    ingestions: List[IngestionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListAppAuthorizationsRequestPaginate(BaseValidatorModel):
    appBundleIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAppBundlesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListIngestionDestinationsRequestPaginate(BaseValidatorModel):
    appBundleIdentifier: str
    ingestionIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListIngestionsRequestPaginate(BaseValidatorModel):
    appBundleIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class UserAccessResultItem(BaseValidatorModel):
    app: Optional[str] = None
    tenantId: Optional[str] = None
    tenantDisplayName: Optional[str] = None
    taskId: Optional[str] = None
    resultStatus: Optional[ResultStatusType] = None
    email: Optional[str] = None
    userId: Optional[str] = None
    userFullName: Optional[str] = None
    userFirstName: Optional[str] = None
    userLastName: Optional[str] = None
    userStatus: Optional[str] = None
    taskError: Optional[TaskError] = None


class UserAccessTaskItem(BaseValidatorModel):
    app: str
    tenantId: str
    taskId: Optional[str] = None
    error: Optional[TaskError] = None


# This class is the output for the 'connect_app_authorization' function.
class ConnectAppAuthorizationResponse(BaseValidatorModel):
    appAuthorizationSummary: AppAuthorizationSummary
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_app_authorizations' function.
class ListAppAuthorizationsResponse(BaseValidatorModel):
    appAuthorizationSummaryList: List[AppAuthorizationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'create_app_authorization' function.
class CreateAppAuthorizationResponse(BaseValidatorModel):
    appAuthorization: AppAuthorization
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_app_authorization' function.
class GetAppAuthorizationResponse(BaseValidatorModel):
    appAuthorization: AppAuthorization
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_app_authorization' function.
class UpdateAppAuthorizationResponse(BaseValidatorModel):
    appAuthorization: AppAuthorization
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_app_authorization' function.
class CreateAppAuthorizationRequest(BaseValidatorModel):
    appBundleIdentifier: str
    app: str
    credential: Credential
    tenant: Tenant
    authType: AuthTypeType
    clientToken: Optional[str] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'update_app_authorization' function.
class UpdateAppAuthorizationRequest(BaseValidatorModel):
    appBundleIdentifier: str
    appAuthorizationIdentifier: str
    credential: Optional[Credential] = None
    tenant: Optional[Tenant] = None


class AuditLogDestinationConfiguration(BaseValidatorModel):
    destination: Destination


# This class is the output for the 'batch_get_user_access_tasks' function.
class BatchGetUserAccessTasksResponse(BaseValidatorModel):
    userAccessResultsList: List[UserAccessResultItem]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_user_access_tasks' function.
class StartUserAccessTasksResponse(BaseValidatorModel):
    userAccessTasksList: List[UserAccessTaskItem]
    ResponseMetadata: ResponseMetadata


class DestinationConfiguration(BaseValidatorModel):
    auditLog: Optional[AuditLogDestinationConfiguration] = None


# This class is the input for the 'create_ingestion_destination' function.
class CreateIngestionDestinationRequest(BaseValidatorModel):
    appBundleIdentifier: str
    ingestionIdentifier: str
    processingConfiguration: ProcessingConfiguration
    destinationConfiguration: DestinationConfiguration
    clientToken: Optional[str] = None
    tags: Optional[List[Tag]] = None


class IngestionDestination(BaseValidatorModel):
    arn: str
    ingestionArn: str
    processingConfiguration: ProcessingConfiguration
    destinationConfiguration: DestinationConfiguration
    status: Optional[IngestionDestinationStatusType] = None
    statusReason: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None


# This class is the input for the 'update_ingestion_destination' function.
class UpdateIngestionDestinationRequest(BaseValidatorModel):
    appBundleIdentifier: str
    ingestionIdentifier: str
    ingestionDestinationIdentifier: str
    destinationConfiguration: DestinationConfiguration


# This class is the output for the 'create_ingestion_destination' function.
class CreateIngestionDestinationResponse(BaseValidatorModel):
    ingestionDestination: IngestionDestination
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_ingestion_destination' function.
class GetIngestionDestinationResponse(BaseValidatorModel):
    ingestionDestination: IngestionDestination
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_ingestion_destination' function.
class UpdateIngestionDestinationResponse(BaseValidatorModel):
    ingestionDestination: IngestionDestination
    ResponseMetadata: ResponseMetadata