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
from aws_resource_validator.pydantic_models.serverlessrepo_constants import *

class ApplicationDependencySummaryTypeDef(BaseValidatorModel):
    ApplicationId: str
    SemanticVersion: str

class ApplicationPolicyStatementTypeDef(BaseValidatorModel):
    Actions: List[str]
    Principals: List[str]
    PrincipalOrgIDs: Optional[List[str]] = None
    StatementId: Optional[str] = None

class ApplicationSummaryTypeDef(BaseValidatorModel):
    ApplicationId: str
    Author: str
    Description: str
    Name: str
    CreationTime: Optional[str] = None
    HomePageUrl: Optional[str] = None
    Labels: Optional[List[str]] = None
    SpdxLicenseId: Optional[str] = None

class CreateApplicationRequestRequestTypeDef(BaseValidatorModel):
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

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateApplicationVersionRequestRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    SemanticVersion: str
    SourceCodeArchiveUrl: Optional[str] = None
    SourceCodeUrl: Optional[str] = None
    TemplateBody: Optional[str] = None
    TemplateUrl: Optional[str] = None

class ParameterDefinitionTypeDef(BaseValidatorModel):
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

class ParameterValueTypeDef(BaseValidatorModel):
    Name: str
    Value: str

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class CreateCloudFormationTemplateRequestRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    SemanticVersion: Optional[str] = None

class DeleteApplicationRequestRequestTypeDef(BaseValidatorModel):
    ApplicationId: str

class GetApplicationPolicyRequestRequestTypeDef(BaseValidatorModel):
    ApplicationId: str

class GetApplicationRequestRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    SemanticVersion: Optional[str] = None

class GetCloudFormationTemplateRequestRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    TemplateId: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListApplicationDependenciesRequestRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    MaxItems: Optional[int] = None
    NextToken: Optional[str] = None
    SemanticVersion: Optional[str] = None

class ListApplicationVersionsRequestRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    MaxItems: Optional[int] = None
    NextToken: Optional[str] = None

class VersionSummaryTypeDef(BaseValidatorModel):
    ApplicationId: str
    CreationTime: str
    SemanticVersion: str
    SourceCodeUrl: Optional[str] = None

class ListApplicationsRequestRequestTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    NextToken: Optional[str] = None

class RollbackTriggerTypeDef(BaseValidatorModel):
    Arn: str
    Type: str

class UnshareApplicationRequestRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    OrganizationId: str

class UpdateApplicationRequestRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    Author: Optional[str] = None
    Description: Optional[str] = None
    HomePageUrl: Optional[str] = None
    Labels: Optional[Sequence[str]] = None
    ReadmeBody: Optional[str] = None
    ReadmeUrl: Optional[str] = None

class PutApplicationPolicyRequestRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    Statements: Sequence[ApplicationPolicyStatementTypeDef]

class CreateCloudFormationChangeSetResponseTypeDef(BaseValidatorModel):
    ApplicationId: str
    ChangeSetId: str
    SemanticVersion: str
    StackId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCloudFormationTemplateResponseTypeDef(BaseValidatorModel):
    ApplicationId: str
    CreationTime: str
    ExpirationTime: str
    SemanticVersion: str
    Status: StatusType
    TemplateId: str
    TemplateUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetApplicationPolicyResponseTypeDef(BaseValidatorModel):
    Statements: List[ApplicationPolicyStatementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetCloudFormationTemplateResponseTypeDef(BaseValidatorModel):
    ApplicationId: str
    CreationTime: str
    ExpirationTime: str
    SemanticVersion: str
    Status: StatusType
    TemplateId: str
    TemplateUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationDependenciesResponseTypeDef(BaseValidatorModel):
    Dependencies: List[ApplicationDependencySummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationsResponseTypeDef(BaseValidatorModel):
    Applications: List[ApplicationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutApplicationPolicyResponseTypeDef(BaseValidatorModel):
    Statements: List[ApplicationPolicyStatementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApplicationVersionResponseTypeDef(BaseValidatorModel):
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

class VersionTypeDef(BaseValidatorModel):
    ApplicationId: str
    CreationTime: str
    ParameterDefinitions: List[ParameterDefinitionTypeDef]
    RequiredCapabilities: List[CapabilityType]
    ResourcesSupported: bool
    SemanticVersion: str
    TemplateUrl: str
    SourceCodeArchiveUrl: Optional[str] = None
    SourceCodeUrl: Optional[str] = None

class ListApplicationDependenciesRequestListApplicationDependenciesPaginateTypeDef(BaseValidatorModel):
    ApplicationId: str
    SemanticVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationVersionsRequestListApplicationVersionsPaginateTypeDef(BaseValidatorModel):
    ApplicationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationsRequestListApplicationsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationVersionsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Versions: List[VersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RollbackConfigurationTypeDef(BaseValidatorModel):
    MonitoringTimeInMinutes: Optional[int] = None
    RollbackTriggers: Optional[Sequence[RollbackTriggerTypeDef]] = None

class CreateApplicationResponseTypeDef(BaseValidatorModel):
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

class GetApplicationResponseTypeDef(BaseValidatorModel):
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

class UpdateApplicationResponseTypeDef(BaseValidatorModel):
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

class CreateCloudFormationChangeSetRequestRequestTypeDef(BaseValidatorModel):
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

