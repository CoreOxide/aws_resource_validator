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

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteConfigurationManagerInputTypeDef(BaseValidatorModel):
    ManagerArn: str


class FilterTypeDef(BaseValidatorModel):
    Key: str
    Values: Sequence[str]


class GetConfigurationInputTypeDef(BaseValidatorModel):
    ConfigurationId: str


class GetConfigurationManagerInputTypeDef(BaseValidatorModel):
    ManagerArn: str


class ServiceSettingsTypeDef(BaseValidatorModel):
    ExplorerEnablingRoleArn: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class TagEntryTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class TagResourceInputTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceInputTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateConfigurationDefinitionInputTypeDef(BaseValidatorModel):
    Id: str
    ManagerArn: str
    LocalDeploymentAdministrationRoleArn: Optional[str] = None
    LocalDeploymentExecutionRoleName: Optional[str] = None
    Parameters: Optional[Mapping[str, str]] = None
    TypeVersion: Optional[str] = None


class UpdateConfigurationManagerInputTypeDef(BaseValidatorModel):
    ManagerArn: str
    Description: Optional[str] = None
    Name: Optional[str] = None


class UpdateServiceSettingsInputTypeDef(BaseValidatorModel):
    ExplorerEnablingRoleArn: Optional[str] = None


class ConfigurationDefinitionInputTypeDef(BaseValidatorModel):
    pass


class CreateConfigurationManagerInputTypeDef(BaseValidatorModel):
    ConfigurationDefinitions: Sequence[ConfigurationDefinitionInputTypeDef]
    Description: Optional[str] = None
    Name: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class ConfigurationDefinitionSummaryTypeDef(BaseValidatorModel):
    pass


class StatusSummaryTypeDef(BaseValidatorModel):
    pass


class ConfigurationManagerSummaryTypeDef(BaseValidatorModel):
    ManagerArn: str
    ConfigurationDefinitionSummaries: Optional[List[ConfigurationDefinitionSummaryTypeDef]] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    StatusSummaries: Optional[List[StatusSummaryTypeDef]] = None


class CreateConfigurationManagerOutputTypeDef(BaseValidatorModel):
    ManagerArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class ConfigurationDefinitionTypeDef(BaseValidatorModel):
    pass


class GetConfigurationManagerOutputTypeDef(BaseValidatorModel):
    ConfigurationDefinitions: List[ConfigurationDefinitionTypeDef]
    CreatedAt: datetime
    Description: str
    LastModifiedAt: datetime
    ManagerArn: str
    Name: str
    StatusSummaries: List[StatusSummaryTypeDef]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class ListConfigurationManagersInputTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxItems: Optional[int] = None
    StartingToken: Optional[str] = None


class ListConfigurationsInputTypeDef(BaseValidatorModel):
    ConfigurationDefinitionId: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ManagerArn: Optional[str] = None
    MaxItems: Optional[int] = None
    StartingToken: Optional[str] = None


class GetServiceSettingsOutputTypeDef(BaseValidatorModel):
    ServiceSettings: ServiceSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListConfigurationManagersInputPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListConfigurationsInputPaginateTypeDef(BaseValidatorModel):
    ConfigurationDefinitionId: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ManagerArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class QuickSetupTypeOutputTypeDef(BaseValidatorModel):
    pass


class ListQuickSetupTypesOutputTypeDef(BaseValidatorModel):
    QuickSetupTypeList: List[QuickSetupTypeOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListConfigurationManagersOutputTypeDef(BaseValidatorModel):
    ConfigurationManagersList: List[ConfigurationManagerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ConfigurationSummaryTypeDef(BaseValidatorModel):
    pass


class ListConfigurationsOutputTypeDef(BaseValidatorModel):
    ConfigurationsList: List[ConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


