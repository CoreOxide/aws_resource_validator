from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.ssm_quicksetup.ssm_quicksetup_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ConfigurationDefinitionInput(BaseValidatorModel):
    Parameters: Dict[str, str]
    Type: str
    LocalDeploymentAdministrationRoleArn: Optional[str] = None
    LocalDeploymentExecutionRoleName: Optional[str] = None
    TypeVersion: Optional[str] = None


class ConfigurationDefinitionSummary(BaseValidatorModel):
    FirstClassParameters: Optional[Dict[str, str]] = None
    Id: Optional[str] = None
    Type: Optional[str] = None
    TypeVersion: Optional[str] = None


class ConfigurationDefinition(BaseValidatorModel):
    Parameters: Dict[str, str]
    Type: str
    Id: Optional[str] = None
    LocalDeploymentAdministrationRoleArn: Optional[str] = None
    LocalDeploymentExecutionRoleName: Optional[str] = None
    TypeVersion: Optional[str] = None


class StatusSummary(BaseValidatorModel):
    LastUpdatedAt: datetime
    StatusType: StatusTypeType
    Status: Optional[StatusType] = None
    StatusDetails: Optional[Dict[str, str]] = None
    StatusMessage: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'delete_configuration_manager' function.
class DeleteConfigurationManagerInput(BaseValidatorModel):
    ManagerArn: str


class Filter(BaseValidatorModel):
    Key: str
    Values: List[str]


# This class is the input for the 'get_configuration' function.
class GetConfigurationInput(BaseValidatorModel):
    ConfigurationId: str


# This class is the input for the 'get_configuration_manager' function.
class GetConfigurationManagerInput(BaseValidatorModel):
    ManagerArn: str


class ServiceSettings(BaseValidatorModel):
    ExplorerEnablingRoleArn: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class QuickSetupTypeOutput(BaseValidatorModel):
    LatestVersion: Optional[str] = None
    Type: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class TagEntry(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


# This class is the input for the 'tag_resource' function.
class TagResourceInput(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


# This class is the input for the 'untag_resource' function.
class UntagResourceInput(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


# This class is the input for the 'update_configuration_definition' function.
class UpdateConfigurationDefinitionInput(BaseValidatorModel):
    Id: str
    ManagerArn: str
    LocalDeploymentAdministrationRoleArn: Optional[str] = None
    LocalDeploymentExecutionRoleName: Optional[str] = None
    Parameters: Optional[Dict[str, str]] = None
    TypeVersion: Optional[str] = None


# This class is the input for the 'update_configuration_manager' function.
class UpdateConfigurationManagerInput(BaseValidatorModel):
    ManagerArn: str
    Description: Optional[str] = None
    Name: Optional[str] = None


# This class is the input for the 'update_service_settings' function.
class UpdateServiceSettingsInput(BaseValidatorModel):
    ExplorerEnablingRoleArn: Optional[str] = None


# This class is the input for the 'create_configuration_manager' function.
class CreateConfigurationManagerInput(BaseValidatorModel):
    ConfigurationDefinitions: List[ConfigurationDefinitionInput]
    Description: Optional[str] = None
    Name: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class ConfigurationManagerSummary(BaseValidatorModel):
    ManagerArn: str
    ConfigurationDefinitionSummaries: Optional[List[ConfigurationDefinitionSummary]] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    StatusSummaries: Optional[List[StatusSummary]] = None


class ConfigurationSummary(BaseValidatorModel):
    Account: Optional[str] = None
    ConfigurationDefinitionId: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    FirstClassParameters: Optional[Dict[str, str]] = None
    Id: Optional[str] = None
    ManagerArn: Optional[str] = None
    Region: Optional[str] = None
    StatusSummaries: Optional[List[StatusSummary]] = None
    Type: Optional[str] = None
    TypeVersion: Optional[str] = None


# This class is the output for the 'create_configuration_manager' function.
class CreateConfigurationManagerOutput(BaseValidatorModel):
    ManagerArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_service_settings' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_configuration_manager' function.
class GetConfigurationManagerOutput(BaseValidatorModel):
    ConfigurationDefinitions: List[ConfigurationDefinition]
    CreatedAt: datetime
    Description: str
    LastModifiedAt: datetime
    ManagerArn: str
    Name: str
    StatusSummaries: List[StatusSummary]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_configuration' function.
class GetConfigurationOutput(BaseValidatorModel):
    Account: str
    ConfigurationDefinitionId: str
    CreatedAt: datetime
    Id: str
    LastModifiedAt: datetime
    ManagerArn: str
    Parameters: Dict[str, str]
    Region: str
    StatusSummaries: List[StatusSummary]
    Type: str
    TypeVersion: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'list_configuration_managers' function.
class ListConfigurationManagersInput(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxItems: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_configurations' function.
class ListConfigurationsInput(BaseValidatorModel):
    ConfigurationDefinitionId: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    ManagerArn: Optional[str] = None
    MaxItems: Optional[int] = None
    StartingToken: Optional[str] = None


class GetServiceSettingsOutput(BaseValidatorModel):
    ServiceSettings: ServiceSettings
    ResponseMetadata: ResponseMetadata


class ListConfigurationManagersInputPaginate(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListConfigurationsInputPaginate(BaseValidatorModel):
    ConfigurationDefinitionId: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    ManagerArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListQuickSetupTypesOutput(BaseValidatorModel):
    QuickSetupTypeList: List[QuickSetupTypeOutput]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[TagEntry]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_configuration_managers' function.
class ListConfigurationManagersOutput(BaseValidatorModel):
    ConfigurationManagersList: List[ConfigurationManagerSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_configurations' function.
class ListConfigurationsOutput(BaseValidatorModel):
    ConfigurationsList: List[ConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None