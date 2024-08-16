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
from aws_resource_validator.pydantic_models.rolesanywhere_constants import *

class MappingRuleTypeDef(BaseValidatorModel):
    specifier: str

class TagTypeDef(BaseValidatorModel):
    key: str
    value: str

class NotificationSettingTypeDef(BaseValidatorModel):
    enabled: bool
    event: NotificationEventType
    channel: Optional[Literal["ALL"]] = None
    threshold: Optional[int] = None

class CredentialSummaryTypeDef(BaseValidatorModel):
    enabled: Optional[bool] = None
    failed: Optional[bool] = None
    issuer: Optional[str] = None
    seenAt: Optional[datetime] = None
    serialNumber: Optional[str] = None
    x509CertificateData: Optional[str] = None

class CrlDetailTypeDef(BaseValidatorModel):
    createdAt: Optional[datetime] = None
    crlArn: Optional[str] = None
    crlData: Optional[bytes] = None
    crlId: Optional[str] = None
    enabled: Optional[bool] = None
    name: Optional[str] = None
    trustAnchorArn: Optional[str] = None
    updatedAt: Optional[datetime] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DeleteAttributeMappingRequestRequestTypeDef(BaseValidatorModel):
    certificateField: CertificateFieldType
    profileId: str
    specifiers: Optional[Sequence[str]] = None

class InstancePropertyTypeDef(BaseValidatorModel):
    failed: Optional[bool] = None
    properties: Optional[Dict[str, str]] = None
    seenAt: Optional[datetime] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    pageSize: Optional[int] = None

class SubjectSummaryTypeDef(BaseValidatorModel):
    createdAt: Optional[datetime] = None
    enabled: Optional[bool] = None
    lastSeenAt: Optional[datetime] = None
    subjectArn: Optional[str] = None
    subjectId: Optional[str] = None
    updatedAt: Optional[datetime] = None
    x509Subject: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class NotificationSettingDetailTypeDef(BaseValidatorModel):
    enabled: bool
    event: NotificationEventType
    channel: Optional[Literal["ALL"]] = None
    configuredBy: Optional[str] = None
    threshold: Optional[int] = None

class NotificationSettingKeyTypeDef(BaseValidatorModel):
    event: NotificationEventType
    channel: Optional[Literal["ALL"]] = None

class ScalarCrlRequestRequestTypeDef(BaseValidatorModel):
    crlId: str

class ScalarProfileRequestRequestTypeDef(BaseValidatorModel):
    profileId: str

class ScalarSubjectRequestRequestTypeDef(BaseValidatorModel):
    subjectId: str

class ScalarTrustAnchorRequestRequestTypeDef(BaseValidatorModel):
    trustAnchorId: str

class SourceDataTypeDef(BaseValidatorModel):
    acmPcaArn: Optional[str] = None
    x509CertificateData: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateProfileRequestRequestTypeDef(BaseValidatorModel):
    profileId: str
    durationSeconds: Optional[int] = None
    managedPolicyArns: Optional[Sequence[str]] = None
    name: Optional[str] = None
    roleArns: Optional[Sequence[str]] = None
    sessionPolicy: Optional[str] = None

class AttributeMappingTypeDef(BaseValidatorModel):
    certificateField: Optional[CertificateFieldType] = None
    mappingRules: Optional[List[MappingRuleTypeDef]] = None

class PutAttributeMappingRequestRequestTypeDef(BaseValidatorModel):
    certificateField: CertificateFieldType
    mappingRules: Sequence[MappingRuleTypeDef]
    profileId: str

class UpdateCrlRequestRequestTypeDef(BaseValidatorModel):
    crlId: str
    crlData: Optional[BlobTypeDef] = None
    name: Optional[str] = None

class CreateProfileRequestRequestTypeDef(BaseValidatorModel):
    name: str
    roleArns: Sequence[str]
    durationSeconds: Optional[int] = None
    enabled: Optional[bool] = None
    managedPolicyArns: Optional[Sequence[str]] = None
    requireInstanceProperties: Optional[bool] = None
    sessionPolicy: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class ImportCrlRequestRequestTypeDef(BaseValidatorModel):
    crlData: BlobTypeDef
    name: str
    trustAnchorArn: str
    enabled: Optional[bool] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class PutNotificationSettingsRequestRequestTypeDef(BaseValidatorModel):
    notificationSettings: Sequence[NotificationSettingTypeDef]
    trustAnchorId: str

class CrlDetailResponseTypeDef(BaseValidatorModel):
    crl: CrlDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCrlsResponseTypeDef(BaseValidatorModel):
    crls: List[CrlDetailTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SubjectDetailTypeDef(BaseValidatorModel):
    createdAt: Optional[datetime] = None
    credentials: Optional[List[CredentialSummaryTypeDef]] = None
    enabled: Optional[bool] = None
    instanceProperties: Optional[List[InstancePropertyTypeDef]] = None
    lastSeenAt: Optional[datetime] = None
    subjectArn: Optional[str] = None
    subjectId: Optional[str] = None
    updatedAt: Optional[datetime] = None
    x509Subject: Optional[str] = None

class ListRequestListCrlsPaginateTypeDef(BaseValidatorModel):
    pageSize: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRequestListProfilesPaginateTypeDef(BaseValidatorModel):
    pageSize: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRequestListSubjectsPaginateTypeDef(BaseValidatorModel):
    pageSize: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRequestListTrustAnchorsPaginateTypeDef(BaseValidatorModel):
    pageSize: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSubjectsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    subjects: List[SubjectSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ResetNotificationSettingsRequestRequestTypeDef(BaseValidatorModel):
    notificationSettingKeys: Sequence[NotificationSettingKeyTypeDef]
    trustAnchorId: str

class SourceTypeDef(BaseValidatorModel):
    sourceData: Optional[SourceDataTypeDef] = None
    sourceType: Optional[TrustAnchorTypeType] = None

class ProfileDetailTypeDef(BaseValidatorModel):
    attributeMappings: Optional[List[AttributeMappingTypeDef]] = None
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

class SubjectDetailResponseTypeDef(BaseValidatorModel):
    subject: SubjectDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrustAnchorRequestRequestTypeDef(BaseValidatorModel):
    name: str
    source: SourceTypeDef
    enabled: Optional[bool] = None
    notificationSettings: Optional[Sequence[NotificationSettingTypeDef]] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class TrustAnchorDetailTypeDef(BaseValidatorModel):
    createdAt: Optional[datetime] = None
    enabled: Optional[bool] = None
    name: Optional[str] = None
    notificationSettings: Optional[List[NotificationSettingDetailTypeDef]] = None
    source: Optional[SourceTypeDef] = None
    trustAnchorArn: Optional[str] = None
    trustAnchorId: Optional[str] = None
    updatedAt: Optional[datetime] = None

class UpdateTrustAnchorRequestRequestTypeDef(BaseValidatorModel):
    trustAnchorId: str
    name: Optional[str] = None
    source: Optional[SourceTypeDef] = None

class DeleteAttributeMappingResponseTypeDef(BaseValidatorModel):
    profile: ProfileDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListProfilesResponseTypeDef(BaseValidatorModel):
    nextToken: str
    profiles: List[ProfileDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ProfileDetailResponseTypeDef(BaseValidatorModel):
    profile: ProfileDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutAttributeMappingResponseTypeDef(BaseValidatorModel):
    profile: ProfileDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTrustAnchorsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    trustAnchors: List[TrustAnchorDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutNotificationSettingsResponseTypeDef(BaseValidatorModel):
    trustAnchor: TrustAnchorDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ResetNotificationSettingsResponseTypeDef(BaseValidatorModel):
    trustAnchor: TrustAnchorDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TrustAnchorDetailResponseTypeDef(BaseValidatorModel):
    trustAnchor: TrustAnchorDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

