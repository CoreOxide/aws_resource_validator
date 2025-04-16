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
from aws_resource_validator.pydantic_models.ssm_quicksetup_constants import *

class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteConfigurationManagerInput(BaseValidatorModel):
    ManagerArn: str


class Filter(BaseValidatorModel):
    Key: str
    Values: Sequence[str]


class GetConfigurationInput(BaseValidatorModel):
    ConfigurationId: str


class GetConfigurationManagerInput(BaseValidatorModel):
    ManagerArn: str


class ServiceSettings(BaseValidatorModel):
    ExplorerEnablingRoleArn: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class TagEntry(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class TagResourceInput(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceInput(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateConfigurationDefinitionInput(BaseValidatorModel):
    Id: str
    ManagerArn: str
    LocalDeploymentAdministrationRoleArn: Optional[str] = None
    LocalDeploymentExecutionRoleName: Optional[str] = None
    Parameters: Optional[Mapping[str, str]] = None
    TypeVersion: Optional[str] = None


class UpdateConfigurationManagerInput(BaseValidatorModel):
    ManagerArn: str
    Description: Optional[str] = None
    Name: Optional[str] = None


class UpdateServiceSettingsInput(BaseValidatorModel):
    ExplorerEnablingRoleArn: Optional[str] = None


class ConfigurationDefinitionInput(BaseValidatorModel):
    pass


class CreateConfigurationManagerInput(BaseValidatorModel):
    ConfigurationDefinitions: Sequence[ConfigurationDefinitionInput]
    Description: Optional[str] = None
    Name: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class ConfigurationDefinitionSummary(BaseValidatorModel):
    pass


class StatusSummary(BaseValidatorModel):
    pass


class ConfigurationManagerSummary(BaseValidatorModel):
    ManagerArn: str
    ConfigurationDefinitionSummaries: Optional[List[ConfigurationDefinitionSummary]] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    StatusSummaries: Optional[List[StatusSummary]] = None


class CreateConfigurationManagerOutput(BaseValidatorModel):
    ManagerArn: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ConfigurationDefinition(BaseValidatorModel):
    pass


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


class ListConfigurationManagersInput(BaseValidatorModel):
    Filters: Optional[Sequence[Filter]] = None
    MaxItems: Optional[int] = None
    StartingToken: Optional[str] = None


class ListConfigurationsInput(BaseValidatorModel):
    ConfigurationDefinitionId: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None
    ManagerArn: Optional[str] = None
    MaxItems: Optional[int] = None
    StartingToken: Optional[str] = None


class GetServiceSettingsOutput(BaseValidatorModel):
    ServiceSettings: ServiceSettings
    ResponseMetadata: ResponseMetadata


class ListConfigurationManagersInputPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListConfigurationsInputPaginate(BaseValidatorModel):
    ConfigurationDefinitionId: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None
    ManagerArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class QuickSetupTypeOutput(BaseValidatorModel):
    pass


class ListQuickSetupTypesOutput(BaseValidatorModel):
    QuickSetupTypeList: List[QuickSetupTypeOutput]
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[TagEntry]
    ResponseMetadata: ResponseMetadata


class ListConfigurationManagersOutput(BaseValidatorModel):
    ConfigurationManagersList: List[ConfigurationManagerSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ConfigurationSummary(BaseValidatorModel):
    pass


class ListConfigurationsOutput(BaseValidatorModel):
    ConfigurationsList: List[ConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


