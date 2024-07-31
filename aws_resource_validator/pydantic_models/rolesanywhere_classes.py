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
from aws_resource_validator.pydantic_models.rolesanywhere_constants import *

class MappingRuleTypeDef(BaseModel):
    specifier: str

class TagTypeDef(BaseModel):
    key: str
    value: str

class NotificationSettingTypeDef(BaseModel):
    enabled: bool
    event: NotificationEventType
    channel: Optional[Literal["ALL"]] = None
    threshold: Optional[int] = None

class CredentialSummaryTypeDef(BaseModel):
    enabled: Optional[bool] = None
    failed: Optional[bool] = None
    issuer: Optional[str] = None
    seenAt: Optional[datetime] = None
    serialNumber: Optional[str] = None
    x509CertificateData: Optional[str] = None

class CrlDetailTypeDef(BaseModel):
    createdAt: Optional[datetime] = None
    crlArn: Optional[str] = None
    crlData: Optional[bytes] = None
    crlId: Optional[str] = None
    enabled: Optional[bool] = None
    name: Optional[str] = None
    trustAnchorArn: Optional[str] = None
    updatedAt: Optional[datetime] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DeleteAttributeMappingRequestRequestTypeDef(BaseModel):
    certificateField: CertificateFieldType
    profileId: str
    specifiers: Optional[Sequence[str]] = None

class InstancePropertyTypeDef(BaseModel):
    failed: Optional[bool] = None
    properties: Optional[Dict[str, str]] = None
    seenAt: Optional[datetime] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    pageSize: Optional[int] = None

class SubjectSummaryTypeDef(BaseModel):
    createdAt: Optional[datetime] = None
    enabled: Optional[bool] = None
    lastSeenAt: Optional[datetime] = None
    subjectArn: Optional[str] = None
    subjectId: Optional[str] = None
    updatedAt: Optional[datetime] = None
    x509Subject: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class NotificationSettingDetailTypeDef(BaseModel):
    enabled: bool
    event: NotificationEventType
    channel: Optional[Literal["ALL"]] = None
    configuredBy: Optional[str] = None
    threshold: Optional[int] = None

class NotificationSettingKeyTypeDef(BaseModel):
    event: NotificationEventType
    channel: Optional[Literal["ALL"]] = None

class ScalarCrlRequestRequestTypeDef(BaseModel):
    crlId: str

class ScalarProfileRequestRequestTypeDef(BaseModel):
    profileId: str

class ScalarSubjectRequestRequestTypeDef(BaseModel):
    subjectId: str

class ScalarTrustAnchorRequestRequestTypeDef(BaseModel):
    trustAnchorId: str

class SourceDataTypeDef(BaseModel):
    acmPcaArn: Optional[str] = None
    x509CertificateData: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateProfileRequestRequestTypeDef(BaseModel):
    profileId: str
    durationSeconds: Optional[int] = None
    managedPolicyArns: Optional[Sequence[str]] = None
    name: Optional[str] = None
    roleArns: Optional[Sequence[str]] = None
    sessionPolicy: Optional[str] = None

class AttributeMappingTypeDef(BaseModel):
    certificateField: Optional[CertificateFieldType] = None
    mappingRules: Optional[List[MappingRuleTypeDef]] = None

class PutAttributeMappingRequestRequestTypeDef(BaseModel):
    certificateField: CertificateFieldType
    mappingRules: Sequence[MappingRuleTypeDef]
    profileId: str

class UpdateCrlRequestRequestTypeDef(BaseModel):
    crlId: str
    crlData: Optional[BlobTypeDef] = None
    name: Optional[str] = None

class CreateProfileRequestRequestTypeDef(BaseModel):
    name: str
    roleArns: Sequence[str]
    durationSeconds: Optional[int] = None
    enabled: Optional[bool] = None
    managedPolicyArns: Optional[Sequence[str]] = None
    requireInstanceProperties: Optional[bool] = None
    sessionPolicy: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class ImportCrlRequestRequestTypeDef(BaseModel):
    crlData: BlobTypeDef
    name: str
    trustAnchorArn: str
    enabled: Optional[bool] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class PutNotificationSettingsRequestRequestTypeDef(BaseModel):
    notificationSettings: Sequence[NotificationSettingTypeDef]
    trustAnchorId: str

class CrlDetailResponseTypeDef(BaseModel):
    crl: CrlDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCrlsResponseTypeDef(BaseModel):
    crls: List[CrlDetailTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SubjectDetailTypeDef(BaseModel):
    createdAt: Optional[datetime] = None
    credentials: Optional[List[CredentialSummaryTypeDef]] = None
    enabled: Optional[bool] = None
    instanceProperties: Optional[List[InstancePropertyTypeDef]] = None
    lastSeenAt: Optional[datetime] = None
    subjectArn: Optional[str] = None
    subjectId: Optional[str] = None
    updatedAt: Optional[datetime] = None
    x509Subject: Optional[str] = None

class ListRequestListCrlsPaginateTypeDef(BaseModel):
    pageSize: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRequestListProfilesPaginateTypeDef(BaseModel):
    pageSize: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRequestListSubjectsPaginateTypeDef(BaseModel):
    pageSize: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRequestListTrustAnchorsPaginateTypeDef(BaseModel):
    pageSize: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSubjectsResponseTypeDef(BaseModel):
    nextToken: str
    subjects: List[SubjectSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ResetNotificationSettingsRequestRequestTypeDef(BaseModel):
    notificationSettingKeys: Sequence[NotificationSettingKeyTypeDef]
    trustAnchorId: str

class SourceTypeDef(BaseModel):
    sourceData: Optional[SourceDataTypeDef] = None
    sourceType: Optional[TrustAnchorTypeType] = None

class ProfileDetailTypeDef(BaseModel):
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

class SubjectDetailResponseTypeDef(BaseModel):
    subject: SubjectDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrustAnchorRequestRequestTypeDef(BaseModel):
    name: str
    source: SourceTypeDef
    enabled: Optional[bool] = None
    notificationSettings: Optional[Sequence[NotificationSettingTypeDef]] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class TrustAnchorDetailTypeDef(BaseModel):
    createdAt: Optional[datetime] = None
    enabled: Optional[bool] = None
    name: Optional[str] = None
    notificationSettings: Optional[List[NotificationSettingDetailTypeDef]] = None
    source: Optional[SourceTypeDef] = None
    trustAnchorArn: Optional[str] = None
    trustAnchorId: Optional[str] = None
    updatedAt: Optional[datetime] = None

class UpdateTrustAnchorRequestRequestTypeDef(BaseModel):
    trustAnchorId: str
    name: Optional[str] = None
    source: Optional[SourceTypeDef] = None

class DeleteAttributeMappingResponseTypeDef(BaseModel):
    profile: ProfileDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListProfilesResponseTypeDef(BaseModel):
    nextToken: str
    profiles: List[ProfileDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ProfileDetailResponseTypeDef(BaseModel):
    profile: ProfileDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutAttributeMappingResponseTypeDef(BaseModel):
    profile: ProfileDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTrustAnchorsResponseTypeDef(BaseModel):
    nextToken: str
    trustAnchors: List[TrustAnchorDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutNotificationSettingsResponseTypeDef(BaseModel):
    trustAnchor: TrustAnchorDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ResetNotificationSettingsResponseTypeDef(BaseModel):
    trustAnchor: TrustAnchorDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TrustAnchorDetailResponseTypeDef(BaseModel):
    trustAnchor: TrustAnchorDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

