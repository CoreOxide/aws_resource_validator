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


# This class is the input for the 'delete_attribute_mapping' function.
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


# This class is the input for the 'list_trust_anchors' function.
class ListRequestRequestExtraExtra(BaseValidatorModel):
    nextToken: Optional[str] = None
    pageSize: Optional[int] = None


# This class is the input for the 'list_subjects' function.
class ListRequestRequestExtra(BaseValidatorModel):
    nextToken: Optional[str] = None
    pageSize: Optional[int] = None


# This class is the input for the 'list_profiles' function.
class ListRequestRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    pageSize: Optional[int] = None


# This class is the input for the 'list_crls' function.
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


# This class is the input for the 'list_tags_for_resource' function.
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


# This class is the input for the 'get_crl' function.
class ScalarCrlRequestRequestExtraExtra(BaseValidatorModel):
    crlId: str


# This class is the input for the 'enable_crl' function.
class ScalarCrlRequestRequestExtra(BaseValidatorModel):
    crlId: str


# This class is the input for the 'disable_crl' function.
class ScalarCrlRequestRequest(BaseValidatorModel):
    crlId: str


# This class is the input for the 'delete_crl' function.
class ScalarCrlRequest(BaseValidatorModel):
    crlId: str


# This class is the input for the 'get_profile' function.
class ScalarProfileRequestRequestExtraExtra(BaseValidatorModel):
    profileId: str


# This class is the input for the 'enable_profile' function.
class ScalarProfileRequestRequestExtra(BaseValidatorModel):
    profileId: str


# This class is the input for the 'disable_profile' function.
class ScalarProfileRequestRequest(BaseValidatorModel):
    profileId: str


# This class is the input for the 'delete_profile' function.
class ScalarProfileRequest(BaseValidatorModel):
    profileId: str


# This class is the input for the 'get_subject' function.
class ScalarSubjectRequest(BaseValidatorModel):
    subjectId: str


# This class is the input for the 'get_trust_anchor' function.
class ScalarTrustAnchorRequestRequestExtraExtra(BaseValidatorModel):
    trustAnchorId: str


# This class is the input for the 'enable_trust_anchor' function.
class ScalarTrustAnchorRequestRequestExtra(BaseValidatorModel):
    trustAnchorId: str


# This class is the input for the 'disable_trust_anchor' function.
class ScalarTrustAnchorRequestRequest(BaseValidatorModel):
    trustAnchorId: str


# This class is the input for the 'delete_trust_anchor' function.
class ScalarTrustAnchorRequest(BaseValidatorModel):
    trustAnchorId: str


class SourceData(BaseValidatorModel):
    acmPcaArn: Optional[str] = None
    x509CertificateData: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_profile' function.
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


# This class is the input for the 'put_attribute_mapping' function.
class PutAttributeMappingRequest(BaseValidatorModel):
    certificateField: CertificateFieldType
    mappingRules: List[MappingRule]
    profileId: str


# This class is the input for the 'update_crl' function.
class UpdateCrlRequest(BaseValidatorModel):
    crlId: str
    crlData: Optional[Blob] = None
    name: Optional[str] = None


# This class is the input for the 'create_profile' function.
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


# This class is the input for the 'import_crl' function.
class ImportCrlRequest(BaseValidatorModel):
    crlData: Blob
    name: str
    trustAnchorArn: str
    enabled: Optional[bool] = None
    tags: Optional[List[Tag]] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: List[Tag]


# This class is the input for the 'put_notification_settings' function.
class PutNotificationSettingsRequest(BaseValidatorModel):
    notificationSettings: List[NotificationSetting]
    trustAnchorId: str


# This class is the output for the 'update_crl' function.
class CrlDetailResponse(BaseValidatorModel):
    crl: CrlDetail
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_crls' function.
class ListCrlsResponse(BaseValidatorModel):
    crls: List[CrlDetail]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
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


# This class is the output for the 'list_subjects' function.
class ListSubjectsResponse(BaseValidatorModel):
    subjects: List[SubjectSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'reset_notification_settings' function.
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


# This class is the output for the 'get_subject' function.
class SubjectDetailResponse(BaseValidatorModel):
    subject: SubjectDetail
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_trust_anchor' function.
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


# This class is the input for the 'update_trust_anchor' function.
class UpdateTrustAnchorRequest(BaseValidatorModel):
    trustAnchorId: str
    name: Optional[str] = None
    source: Optional[Source] = None


# This class is the output for the 'delete_attribute_mapping' function.
class DeleteAttributeMappingResponse(BaseValidatorModel):
    profile: ProfileDetail
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_profiles' function.
class ListProfilesResponse(BaseValidatorModel):
    profiles: List[ProfileDetail]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_profile' function.
class ProfileDetailResponse(BaseValidatorModel):
    profile: ProfileDetail
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_attribute_mapping' function.
class PutAttributeMappingResponse(BaseValidatorModel):
    profile: ProfileDetail
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_trust_anchors' function.
class ListTrustAnchorsResponse(BaseValidatorModel):
    trustAnchors: List[TrustAnchorDetail]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'put_notification_settings' function.
class PutNotificationSettingsResponse(BaseValidatorModel):
    trustAnchor: TrustAnchorDetail
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reset_notification_settings' function.
class ResetNotificationSettingsResponse(BaseValidatorModel):
    trustAnchor: TrustAnchorDetail
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_trust_anchor' function.
class TrustAnchorDetailResponse(BaseValidatorModel):
    trustAnchor: TrustAnchorDetail
    ResponseMetadata: ResponseMetadata