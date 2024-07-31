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
from aws_resource_validator.pydantic_models.serverlessrepo_constants import *

class ApplicationDependencySummaryTypeDef(BaseModel):
    ApplicationId: str
    SemanticVersion: str

class ApplicationPolicyStatementTypeDef(BaseModel):
    Actions: List[str]
    Principals: List[str]
    PrincipalOrgIDs: Optional[List[str]] = None
    StatementId: Optional[str] = None

class ApplicationSummaryTypeDef(BaseModel):
    ApplicationId: str
    Author: str
    Description: str
    Name: str
    CreationTime: Optional[str] = None
    HomePageUrl: Optional[str] = None
    Labels: Optional[List[str]] = None
    SpdxLicenseId: Optional[str] = None

class CreateApplicationRequestRequestTypeDef(BaseModel):
    Author: str
    Description: str
    Name: str
    HomePageUrl: Optional[str] = None
    Labels: Optional[Sequence[str]] = None
    LicenseBody: Optional[str] = None
    LicenseUrl: Optional[str] = None
    ReadmeBody: Optional[str] = None
    ReadmeUrl: Optional[str] = None
    SemanticVersion: Optional[str] = None
    SourceCodeArchiveUrl: Optional[str] = None
    SourceCodeUrl: Optional[str] = None
    SpdxLicenseId: Optional[str] = None
    TemplateBody: Optional[str] = None
    TemplateUrl: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateApplicationVersionRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    SemanticVersion: str
    SourceCodeArchiveUrl: Optional[str] = None
    SourceCodeUrl: Optional[str] = None
    TemplateBody: Optional[str] = None
    TemplateUrl: Optional[str] = None

class ParameterDefinitionTypeDef(BaseModel):
    Name: str
    ReferencedByResources: List[str]
    AllowedPattern: Optional[str] = None
    AllowedValues: Optional[List[str]] = None
    ConstraintDescription: Optional[str] = None
    DefaultValue: Optional[str] = None
    Description: Optional[str] = None
    MaxLength: Optional[int] = None
    MaxValue: Optional[int] = None
    MinLength: Optional[int] = None
    MinValue: Optional[int] = None
    NoEcho: Optional[bool] = None
    Type: Optional[str] = None

class ParameterValueTypeDef(BaseModel):
    Name: str
    Value: str

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class CreateCloudFormationTemplateRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    SemanticVersion: Optional[str] = None

class DeleteApplicationRequestRequestTypeDef(BaseModel):
    ApplicationId: str

class GetApplicationPolicyRequestRequestTypeDef(BaseModel):
    ApplicationId: str

class GetApplicationRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    SemanticVersion: Optional[str] = None

class GetCloudFormationTemplateRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    TemplateId: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListApplicationDependenciesRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    MaxItems: Optional[int] = None
    NextToken: Optional[str] = None
    SemanticVersion: Optional[str] = None

class ListApplicationVersionsRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    MaxItems: Optional[int] = None
    NextToken: Optional[str] = None

class VersionSummaryTypeDef(BaseModel):
    ApplicationId: str
    CreationTime: str
    SemanticVersion: str
    SourceCodeUrl: Optional[str] = None

class ListApplicationsRequestRequestTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    NextToken: Optional[str] = None

class RollbackTriggerTypeDef(BaseModel):
    Arn: str
    Type: str

class UnshareApplicationRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    OrganizationId: str

class UpdateApplicationRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    Author: Optional[str] = None
    Description: Optional[str] = None
    HomePageUrl: Optional[str] = None
    Labels: Optional[Sequence[str]] = None
    ReadmeBody: Optional[str] = None
    ReadmeUrl: Optional[str] = None

class PutApplicationPolicyRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    Statements: Sequence[ApplicationPolicyStatementTypeDef]

class CreateCloudFormationChangeSetResponseTypeDef(BaseModel):
    ApplicationId: str
    ChangeSetId: str
    SemanticVersion: str
    StackId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCloudFormationTemplateResponseTypeDef(BaseModel):
    ApplicationId: str
    CreationTime: str
    ExpirationTime: str
    SemanticVersion: str
    Status: StatusType
    TemplateId: str
    TemplateUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetApplicationPolicyResponseTypeDef(BaseModel):
    Statements: List[ApplicationPolicyStatementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetCloudFormationTemplateResponseTypeDef(BaseModel):
    ApplicationId: str
    CreationTime: str
    ExpirationTime: str
    SemanticVersion: str
    Status: StatusType
    TemplateId: str
    TemplateUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationDependenciesResponseTypeDef(BaseModel):
    Dependencies: List[ApplicationDependencySummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationsResponseTypeDef(BaseModel):
    Applications: List[ApplicationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutApplicationPolicyResponseTypeDef(BaseModel):
    Statements: List[ApplicationPolicyStatementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApplicationVersionResponseTypeDef(BaseModel):
    ApplicationId: str
    CreationTime: str
    ParameterDefinitions: List[ParameterDefinitionTypeDef]
    RequiredCapabilities: List[CapabilityType]
    ResourcesSupported: bool
    SemanticVersion: str
    SourceCodeArchiveUrl: str
    SourceCodeUrl: str
    TemplateUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class VersionTypeDef(BaseModel):
    ApplicationId: str
    CreationTime: str
    ParameterDefinitions: List[ParameterDefinitionTypeDef]
    RequiredCapabilities: List[CapabilityType]
    ResourcesSupported: bool
    SemanticVersion: str
    TemplateUrl: str
    SourceCodeArchiveUrl: Optional[str] = None
    SourceCodeUrl: Optional[str] = None

class ListApplicationDependenciesRequestListApplicationDependenciesPaginateTypeDef(BaseModel):
    ApplicationId: str
    SemanticVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationVersionsRequestListApplicationVersionsPaginateTypeDef(BaseModel):
    ApplicationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationsRequestListApplicationsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationVersionsResponseTypeDef(BaseModel):
    NextToken: str
    Versions: List[VersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RollbackConfigurationTypeDef(BaseModel):
    MonitoringTimeInMinutes: Optional[int] = None
    RollbackTriggers: Optional[Sequence[RollbackTriggerTypeDef]] = None

class CreateApplicationResponseTypeDef(BaseModel):
    ApplicationId: str
    Author: str
    CreationTime: str
    Description: str
    HomePageUrl: str
    IsVerifiedAuthor: bool
    Labels: List[str]
    LicenseUrl: str
    Name: str
    ReadmeUrl: str
    SpdxLicenseId: str
    VerifiedAuthorUrl: str
    Version: VersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetApplicationResponseTypeDef(BaseModel):
    ApplicationId: str
    Author: str
    CreationTime: str
    Description: str
    HomePageUrl: str
    IsVerifiedAuthor: bool
    Labels: List[str]
    LicenseUrl: str
    Name: str
    ReadmeUrl: str
    SpdxLicenseId: str
    VerifiedAuthorUrl: str
    Version: VersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApplicationResponseTypeDef(BaseModel):
    ApplicationId: str
    Author: str
    CreationTime: str
    Description: str
    HomePageUrl: str
    IsVerifiedAuthor: bool
    Labels: List[str]
    LicenseUrl: str
    Name: str
    ReadmeUrl: str
    SpdxLicenseId: str
    VerifiedAuthorUrl: str
    Version: VersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCloudFormationChangeSetRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    StackName: str
    Capabilities: Optional[Sequence[str]] = None
    ChangeSetName: Optional[str] = None
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    NotificationArns: Optional[Sequence[str]] = None
    ParameterOverrides: Optional[Sequence[ParameterValueTypeDef]] = None
    ResourceTypes: Optional[Sequence[str]] = None
    RollbackConfiguration: Optional[RollbackConfigurationTypeDef] = None
    SemanticVersion: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    TemplateId: Optional[str] = None

