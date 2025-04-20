from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.rolesanywhere.rolesanywhere_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class MappingRule(BaseValidatorModel):
    specifier: str

Blob = Union[str, bytes, IO[Any], StreamingBody]


class Tag(BaseValidatorModel):
    key: str
    value: str


class NotificationSetting(BaseValidatorModel):
    enabled: bool
    event: NotificationEventType
    channel: Optional[Literal['ALL']] = None
    threshold: Optional[int] = None


class CredentialSummary(BaseValidatorModel):
    enabled: Optional[bool] = None
    failed: Optional[bool] = None
    issuer: Optional[str] = None
    seenAt: Optional[datetime] = None
    serialNumber: Optional[str] = None
    x509CertificateData: Optional[str] = None


class CrlDetail(BaseValidatorModel):
    createdAt: Optional[datetime] = None
    crlArn: Optional[str] = None
    crlData: Optional[bytes] = None
    crlId: Optional[str] = None
    enabled: Optional[bool] = None
    name: Optional[str] = None
    trustAnchorArn: Optional[str] = None
    updatedAt: Optional[datetime] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteAttributeMappingRequest(BaseValidatorModel):
    certificateField: CertificateFieldType
    profileId: str
    specifiers: Optional[List[str]] = None


class InstanceProperty(BaseValidatorModel):
    failed: Optional[bool] = None
    properties: Optional[Dict[str, str]] = None
    seenAt: Optional[datetime] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListRequestRequestExtraExtra(BaseValidatorModel):
    nextToken: Optional[str] = None
    pageSize: Optional[int] = None


class ListRequestRequestExtra(BaseValidatorModel):
    nextToken: Optional[str] = None
    pageSize: Optional[int] = None


class ListRequestRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    pageSize: Optional[int] = None


class ListRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    pageSize: Optional[int] = None


class SubjectSummary(BaseValidatorModel):
    createdAt: Optional[datetime] = None
    enabled: Optional[bool] = None
    lastSeenAt: Optional[datetime] = None
    subjectArn: Optional[str] = None
    subjectId: Optional[str] = None
    updatedAt: Optional[datetime] = None
    x509Subject: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class NotificationSettingDetail(BaseValidatorModel):
    enabled: bool
    event: NotificationEventType
    channel: Optional[Literal['ALL']] = None
    configuredBy: Optional[str] = None
    threshold: Optional[int] = None


class NotificationSettingKey(BaseValidatorModel):
    event: NotificationEventType
    channel: Optional[Literal['ALL']] = None


class ScalarCrlRequestRequestExtraExtra(BaseValidatorModel):
    crlId: str


class ScalarCrlRequestRequestExtra(BaseValidatorModel):
    crlId: str


class ScalarCrlRequestRequest(BaseValidatorModel):
    crlId: str


class ScalarCrlRequest(BaseValidatorModel):
    crlId: str


class ScalarProfileRequestRequestExtraExtra(BaseValidatorModel):
    profileId: str


class ScalarProfileRequestRequestExtra(BaseValidatorModel):
    profileId: str


class ScalarProfileRequestRequest(BaseValidatorModel):
    profileId: str


class ScalarProfileRequest(BaseValidatorModel):
    profileId: str


class ScalarSubjectRequest(BaseValidatorModel):
    subjectId: str


class ScalarTrustAnchorRequestRequestExtraExtra(BaseValidatorModel):
    trustAnchorId: str


class ScalarTrustAnchorRequestRequestExtra(BaseValidatorModel):
    trustAnchorId: str


class ScalarTrustAnchorRequestRequest(BaseValidatorModel):
    trustAnchorId: str


class ScalarTrustAnchorRequest(BaseValidatorModel):
    trustAnchorId: str


class SourceData(BaseValidatorModel):
    acmPcaArn: Optional[str] = None
    x509CertificateData: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class UpdateProfileRequest(BaseValidatorModel):
    profileId: str
    acceptRoleSessionName: Optional[bool] = None
    durationSeconds: Optional[int] = None
    managedPolicyArns: Optional[List[str]] = None
    name: Optional[str] = None
    roleArns: Optional[List[str]] = None
    sessionPolicy: Optional[str] = None


class AttributeMapping(BaseValidatorModel):
    certificateField: Optional[CertificateFieldType] = None
    mappingRules: Optional[List[MappingRule]] = None


class PutAttributeMappingRequest(BaseValidatorModel):
    certificateField: CertificateFieldType
    mappingRules: List[MappingRule]
    profileId: str


class UpdateCrlRequest(BaseValidatorModel):
    crlId: str
    crlData: Optional[Blob] = None
    name: Optional[str] = None


class CreateProfileRequest(BaseValidatorModel):
    name: str
    roleArns: List[str]
    acceptRoleSessionName: Optional[bool] = None
    durationSeconds: Optional[int] = None
    enabled: Optional[bool] = None
    managedPolicyArns: Optional[List[str]] = None
    requireInstanceProperties: Optional[bool] = None
    sessionPolicy: Optional[str] = None
    tags: Optional[List[Tag]] = None


class ImportCrlRequest(BaseValidatorModel):
    crlData: Blob
    name: str
    trustAnchorArn: str
    enabled: Optional[bool] = None
    tags: Optional[List[Tag]] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: List[Tag]


class PutNotificationSettingsRequest(BaseValidatorModel):
    notificationSettings: List[NotificationSetting]
    trustAnchorId: str


class CrlDetailResponse(BaseValidatorModel):
    crl: CrlDetail
    ResponseMetadata: ResponseMetadata


class ListCrlsResponse(BaseValidatorModel):
    crls: List[CrlDetail]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class SubjectDetail(BaseValidatorModel):
    createdAt: Optional[datetime] = None
    credentials: Optional[List[CredentialSummary]] = None
    enabled: Optional[bool] = None
    instanceProperties: Optional[List[InstanceProperty]] = None
    lastSeenAt: Optional[datetime] = None
    subjectArn: Optional[str] = None
    subjectId: Optional[str] = None
    updatedAt: Optional[datetime] = None
    x509Subject: Optional[str] = None


class ListRequestPaginateExtraExtraExtra(BaseValidatorModel):
    pageSize: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRequestPaginateExtraExtra(BaseValidatorModel):
    pageSize: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRequestPaginateExtra(BaseValidatorModel):
    pageSize: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRequestPaginate(BaseValidatorModel):
    pageSize: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSubjectsResponse(BaseValidatorModel):
    subjects: List[SubjectSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ResetNotificationSettingsRequest(BaseValidatorModel):
    notificationSettingKeys: List[NotificationSettingKey]
    trustAnchorId: str


class Source(BaseValidatorModel):
    sourceData: Optional[SourceData] = None
    sourceType: Optional[TrustAnchorTypeType] = None


class ProfileDetail(BaseValidatorModel):
    acceptRoleSessionName: Optional[bool] = None
    attributeMappings: Optional[List[AttributeMapping]] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    durationSeconds: Optional[int] = None
    enabled: Optional[bool] = None
    managedPolicyArns: Optional[List[str]] = None
    name: Optional[str] = None
    profileArn: Optional[str] = None
    profileId: Optional[str] = None
    requireInstanceProperties: Optional[bool] = None
    roleArns: Optional[List[str]] = None
    sessionPolicy: Optional[str] = None
    updatedAt: Optional[datetime] = None


class SubjectDetailResponse(BaseValidatorModel):
    subject: SubjectDetail
    ResponseMetadata: ResponseMetadata


class CreateTrustAnchorRequest(BaseValidatorModel):
    name: str
    source: Source
    enabled: Optional[bool] = None
    notificationSettings: Optional[List[NotificationSetting]] = None
    tags: Optional[List[Tag]] = None


class TrustAnchorDetail(BaseValidatorModel):
    createdAt: Optional[datetime] = None
    enabled: Optional[bool] = None
    name: Optional[str] = None
    notificationSettings: Optional[List[NotificationSettingDetail]] = None
    source: Optional[Source] = None
    trustAnchorArn: Optional[str] = None
    trustAnchorId: Optional[str] = None
    updatedAt: Optional[datetime] = None


class UpdateTrustAnchorRequest(BaseValidatorModel):
    trustAnchorId: str
    name: Optional[str] = None
    source: Optional[Source] = None


class DeleteAttributeMappingResponse(BaseValidatorModel):
    profile: ProfileDetail
    ResponseMetadata: ResponseMetadata


class ListProfilesResponse(BaseValidatorModel):
    profiles: List[ProfileDetail]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ProfileDetailResponse(BaseValidatorModel):
    profile: ProfileDetail
    ResponseMetadata: ResponseMetadata


class PutAttributeMappingResponse(BaseValidatorModel):
    profile: ProfileDetail
    ResponseMetadata: ResponseMetadata


class ListTrustAnchorsResponse(BaseValidatorModel):
    trustAnchors: List[TrustAnchorDetail]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class PutNotificationSettingsResponse(BaseValidatorModel):
    trustAnchor: TrustAnchorDetail
    ResponseMetadata: ResponseMetadata


class ResetNotificationSettingsResponse(BaseValidatorModel):
    trustAnchor: TrustAnchorDetail
    ResponseMetadata: ResponseMetadata


class TrustAnchorDetailResponse(BaseValidatorModel):
    trustAnchor: TrustAnchorDetail
    ResponseMetadata: ResponseMetadata