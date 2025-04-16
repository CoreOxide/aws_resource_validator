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
from aws_resource_validator.pydantic_models.appfabric_constants import *

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


class AuthRequest(BaseValidatorModel):
    redirectUri: str
    code: str


class BatchGetUserAccessTasksRequest(BaseValidatorModel):
    appBundleIdentifier: str
    taskIdList: Sequence[str]


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
    ingestionType: Literal["auditLog"]


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


class GetAppAuthorizationRequest(BaseValidatorModel):
    appBundleIdentifier: str
    appAuthorizationIdentifier: str


class GetAppBundleRequest(BaseValidatorModel):
    appBundleIdentifier: str


class GetIngestionDestinationRequest(BaseValidatorModel):
    appBundleIdentifier: str
    ingestionIdentifier: str
    ingestionDestinationIdentifier: str


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


class ListAppAuthorizationsRequest(BaseValidatorModel):
    appBundleIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAppBundlesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListIngestionDestinationsRequest(BaseValidatorModel):
    appBundleIdentifier: str
    ingestionIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListIngestionsRequest(BaseValidatorModel):
    appBundleIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class StartIngestionRequest(BaseValidatorModel):
    ingestionIdentifier: str
    appBundleIdentifier: str


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
    tagKeys: Sequence[str]


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


class AuditLogProcessingConfiguration(BaseValidatorModel):
    pass


class ProcessingConfiguration(BaseValidatorModel):
    auditLog: Optional[AuditLogProcessingConfiguration] = None


class ConnectAppAuthorizationRequest(BaseValidatorModel):
    appBundleIdentifier: str
    appAuthorizationIdentifier: str
    authRequest: Optional[AuthRequest] = None


class CreateAppBundleResponse(BaseValidatorModel):
    appBundle: AppBundle
    ResponseMetadata: ResponseMetadata


class GetAppBundleResponse(BaseValidatorModel):
    appBundle: AppBundle
    ResponseMetadata: ResponseMetadata


class ListAppBundlesResponse(BaseValidatorModel):
    appBundleSummaryList: List[AppBundleSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreateAppBundleRequest(BaseValidatorModel):
    clientToken: Optional[str] = None
    customerManagedKeyIdentifier: Optional[str] = None
    tags: Optional[Sequence[Tag]] = None


class CreateIngestionRequest(BaseValidatorModel):
    appBundleIdentifier: str
    app: str
    tenantId: str
    ingestionType: Literal["auditLog"]
    clientToken: Optional[str] = None
    tags: Optional[Sequence[Tag]] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[Tag]


class CreateIngestionResponse(BaseValidatorModel):
    ingestion: Ingestion
    ResponseMetadata: ResponseMetadata


class GetIngestionResponse(BaseValidatorModel):
    ingestion: Ingestion
    ResponseMetadata: ResponseMetadata


class Credential(BaseValidatorModel):
    oauth2Credential: Optional[Oauth2Credential] = None
    apiKeyCredential: Optional[ApiKeyCredential] = None


class Destination(BaseValidatorModel):
    s3Bucket: Optional[S3Bucket] = None
    firehoseStream: Optional[FirehoseStream] = None


class ListIngestionDestinationsResponse(BaseValidatorModel):
    ingestionDestinations: List[IngestionDestinationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


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


class ConnectAppAuthorizationResponse(BaseValidatorModel):
    appAuthorizationSummary: AppAuthorizationSummary
    ResponseMetadata: ResponseMetadata


class ListAppAuthorizationsResponse(BaseValidatorModel):
    appAuthorizationSummaryList: List[AppAuthorizationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreateAppAuthorizationResponse(BaseValidatorModel):
    appAuthorization: AppAuthorization
    ResponseMetadata: ResponseMetadata


class GetAppAuthorizationResponse(BaseValidatorModel):
    appAuthorization: AppAuthorization
    ResponseMetadata: ResponseMetadata


class UpdateAppAuthorizationResponse(BaseValidatorModel):
    appAuthorization: AppAuthorization
    ResponseMetadata: ResponseMetadata


class CreateAppAuthorizationRequest(BaseValidatorModel):
    appBundleIdentifier: str
    app: str
    credential: Credential
    tenant: Tenant
    authType: AuthTypeType
    clientToken: Optional[str] = None
    tags: Optional[Sequence[Tag]] = None


class UpdateAppAuthorizationRequest(BaseValidatorModel):
    appBundleIdentifier: str
    appAuthorizationIdentifier: str
    credential: Optional[Credential] = None
    tenant: Optional[Tenant] = None


class AuditLogDestinationConfiguration(BaseValidatorModel):
    destination: Destination


class BatchGetUserAccessTasksResponse(BaseValidatorModel):
    userAccessResultsList: List[UserAccessResultItem]
    ResponseMetadata: ResponseMetadata


class StartUserAccessTasksResponse(BaseValidatorModel):
    userAccessTasksList: List[UserAccessTaskItem]
    ResponseMetadata: ResponseMetadata


class DestinationConfiguration(BaseValidatorModel):
    auditLog: Optional[AuditLogDestinationConfiguration] = None


class CreateIngestionDestinationRequest(BaseValidatorModel):
    appBundleIdentifier: str
    ingestionIdentifier: str
    processingConfiguration: ProcessingConfiguration
    destinationConfiguration: DestinationConfiguration
    clientToken: Optional[str] = None
    tags: Optional[Sequence[Tag]] = None


class IngestionDestination(BaseValidatorModel):
    arn: str
    ingestionArn: str
    processingConfiguration: ProcessingConfiguration
    destinationConfiguration: DestinationConfiguration
    status: Optional[IngestionDestinationStatusType] = None
    statusReason: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None


class UpdateIngestionDestinationRequest(BaseValidatorModel):
    appBundleIdentifier: str
    ingestionIdentifier: str
    ingestionDestinationIdentifier: str
    destinationConfiguration: DestinationConfiguration


class CreateIngestionDestinationResponse(BaseValidatorModel):
    ingestionDestination: IngestionDestination
    ResponseMetadata: ResponseMetadata


class GetIngestionDestinationResponse(BaseValidatorModel):
    ingestionDestination: IngestionDestination
    ResponseMetadata: ResponseMetadata


class UpdateIngestionDestinationResponse(BaseValidatorModel):
    ingestionDestination: IngestionDestination
    ResponseMetadata: ResponseMetadata


