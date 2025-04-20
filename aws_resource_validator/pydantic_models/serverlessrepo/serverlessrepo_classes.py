from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.serverlessrepo.serverlessrepo_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ApplicationDependencySummary(BaseValidatorModel):
    ApplicationId: str
    SemanticVersion: str


class ApplicationPolicyStatementOutput(BaseValidatorModel):
    Actions: List[str]
    Principals: List[str]
    PrincipalOrgIDs: Optional[List[str]] = None
    StatementId: Optional[str] = None


class ApplicationPolicyStatement(BaseValidatorModel):
    Actions: List[str]
    Principals: List[str]
    PrincipalOrgIDs: Optional[List[str]] = None
    StatementId: Optional[str] = None


class ApplicationSummary(BaseValidatorModel):
    ApplicationId: str
    Author: str
    Description: str
    Name: str
    CreationTime: Optional[str] = None
    HomePageUrl: Optional[str] = None
    Labels: Optional[List[str]] = None
    SpdxLicenseId: Optional[str] = None


class CreateApplicationRequest(BaseValidatorModel):
    Author: str
    Description: str
    Name: str
    HomePageUrl: Optional[str] = None
    Labels: Optional[List[str]] = None
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


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateApplicationVersionRequest(BaseValidatorModel):
    ApplicationId: str
    SemanticVersion: str
    SourceCodeArchiveUrl: Optional[str] = None
    SourceCodeUrl: Optional[str] = None
    TemplateBody: Optional[str] = None
    TemplateUrl: Optional[str] = None


class ParameterDefinition(BaseValidatorModel):
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


class ParameterValue(BaseValidatorModel):
    Name: str
    Value: str


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class CreateCloudFormationTemplateRequest(BaseValidatorModel):
    ApplicationId: str
    SemanticVersion: Optional[str] = None


class DeleteApplicationRequest(BaseValidatorModel):
    ApplicationId: str


class GetApplicationPolicyRequest(BaseValidatorModel):
    ApplicationId: str


class GetApplicationRequest(BaseValidatorModel):
    ApplicationId: str
    SemanticVersion: Optional[str] = None


class GetCloudFormationTemplateRequest(BaseValidatorModel):
    ApplicationId: str
    TemplateId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListApplicationDependenciesRequest(BaseValidatorModel):
    ApplicationId: str
    MaxItems: Optional[int] = None
    NextToken: Optional[str] = None
    SemanticVersion: Optional[str] = None


class ListApplicationVersionsRequest(BaseValidatorModel):
    ApplicationId: str
    MaxItems: Optional[int] = None
    NextToken: Optional[str] = None


class VersionSummary(BaseValidatorModel):
    ApplicationId: str
    CreationTime: str
    SemanticVersion: str
    SourceCodeUrl: Optional[str] = None


class ListApplicationsRequest(BaseValidatorModel):
    MaxItems: Optional[int] = None
    NextToken: Optional[str] = None


class RollbackTrigger(BaseValidatorModel):
    Arn: str
    Type: str


class UnshareApplicationRequest(BaseValidatorModel):
    ApplicationId: str
    OrganizationId: str


class UpdateApplicationRequest(BaseValidatorModel):
    ApplicationId: str
    Author: Optional[str] = None
    Description: Optional[str] = None
    HomePageUrl: Optional[str] = None
    Labels: Optional[List[str]] = None
    ReadmeBody: Optional[str] = None
    ReadmeUrl: Optional[str] = None

ApplicationPolicyStatementUnion = Union[ApplicationPolicyStatement, ApplicationPolicyStatementOutput]


class CreateCloudFormationChangeSetResponse(BaseValidatorModel):
    ApplicationId: str
    ChangeSetId: str
    SemanticVersion: str
    StackId: str
    ResponseMetadata: ResponseMetadata


class CreateCloudFormationTemplateResponse(BaseValidatorModel):
    ApplicationId: str
    CreationTime: str
    ExpirationTime: str
    SemanticVersion: str
    Status: StatusType
    TemplateId: str
    TemplateUrl: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetApplicationPolicyResponse(BaseValidatorModel):
    Statements: List[ApplicationPolicyStatementOutput]
    ResponseMetadata: ResponseMetadata


class GetCloudFormationTemplateResponse(BaseValidatorModel):
    ApplicationId: str
    CreationTime: str
    ExpirationTime: str
    SemanticVersion: str
    Status: StatusType
    TemplateId: str
    TemplateUrl: str
    ResponseMetadata: ResponseMetadata


class ListApplicationDependenciesResponse(BaseValidatorModel):
    Dependencies: List[ApplicationDependencySummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListApplicationsResponse(BaseValidatorModel):
    Applications: List[ApplicationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PutApplicationPolicyResponse(BaseValidatorModel):
    Statements: List[ApplicationPolicyStatementOutput]
    ResponseMetadata: ResponseMetadata


class CreateApplicationVersionResponse(BaseValidatorModel):
    ApplicationId: str
    CreationTime: str
    ParameterDefinitions: List[ParameterDefinition]
    RequiredCapabilities: List[CapabilityType]
    ResourcesSupported: bool
    SemanticVersion: str
    SourceCodeArchiveUrl: str
    SourceCodeUrl: str
    TemplateUrl: str
    ResponseMetadata: ResponseMetadata


class Version(BaseValidatorModel):
    ApplicationId: str
    CreationTime: str
    ParameterDefinitions: List[ParameterDefinition]
    RequiredCapabilities: List[CapabilityType]
    ResourcesSupported: bool
    SemanticVersion: str
    TemplateUrl: str
    SourceCodeArchiveUrl: Optional[str] = None
    SourceCodeUrl: Optional[str] = None


class ListApplicationDependenciesRequestPaginate(BaseValidatorModel):
    ApplicationId: str
    SemanticVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListApplicationVersionsRequestPaginate(BaseValidatorModel):
    ApplicationId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListApplicationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListApplicationVersionsResponse(BaseValidatorModel):
    Versions: List[VersionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RollbackConfiguration(BaseValidatorModel):
    MonitoringTimeInMinutes: Optional[int] = None
    RollbackTriggers: Optional[List[RollbackTrigger]] = None


class PutApplicationPolicyRequest(BaseValidatorModel):
    ApplicationId: str
    Statements: List[ApplicationPolicyStatementUnion]


class CreateApplicationResponse(BaseValidatorModel):
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
    Version: Version
    ResponseMetadata: ResponseMetadata


class GetApplicationResponse(BaseValidatorModel):
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
    Version: Version
    ResponseMetadata: ResponseMetadata


class UpdateApplicationResponse(BaseValidatorModel):
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
    Version: Version
    ResponseMetadata: ResponseMetadata


class CreateCloudFormationChangeSetRequest(BaseValidatorModel):
    ApplicationId: str
    StackName: str
    Capabilities: Optional[List[str]] = None
    ChangeSetName: Optional[str] = None
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    NotificationArns: Optional[List[str]] = None
    ParameterOverrides: Optional[List[ParameterValue]] = None
    ResourceTypes: Optional[List[str]] = None
    RollbackConfiguration: Optional[RollbackConfiguration] = None
    SemanticVersion: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    TemplateId: Optional[str] = None