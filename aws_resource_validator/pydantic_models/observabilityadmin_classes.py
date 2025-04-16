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
from aws_resource_validator.pydantic_models.observabilityadmin_constants import *

class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListResourceTelemetryForOrganizationInput(BaseValidatorModel):
    AccountIdentifiers: Optional[Sequence[str]] = None
    ResourceIdentifierPrefix: Optional[str] = None
    ResourceTypes: Optional[Sequence[ResourceTypeType]] = None
    TelemetryConfigurationState: Optional[Mapping[TelemetryTypeType, TelemetryStateType]] = None
    ResourceTags: Optional[Mapping[str, str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class TelemetryConfiguration(BaseValidatorModel):
    AccountIdentifier: Optional[str] = None
    TelemetryConfigurationState: Optional[Dict[TelemetryTypeType, TelemetryStateType]] = None
    ResourceType: Optional[ResourceTypeType] = None
    ResourceIdentifier: Optional[str] = None
    ResourceTags: Optional[Dict[str, str]] = None
    LastUpdateTimeStamp: Optional[int] = None


class ListResourceTelemetryInput(BaseValidatorModel):
    ResourceIdentifierPrefix: Optional[str] = None
    ResourceTypes: Optional[Sequence[ResourceTypeType]] = None
    TelemetryConfigurationState: Optional[Mapping[TelemetryTypeType, TelemetryStateType]] = None
    ResourceTags: Optional[Mapping[str, str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetTelemetryEvaluationStatusForOrganizationOutput(BaseValidatorModel):
    Status: StatusType
    FailureReason: str
    ResponseMetadata: ResponseMetadata


class GetTelemetryEvaluationStatusOutput(BaseValidatorModel):
    Status: StatusType
    FailureReason: str
    ResponseMetadata: ResponseMetadata


class ListResourceTelemetryForOrganizationInputPaginate(BaseValidatorModel):
    AccountIdentifiers: Optional[Sequence[str]] = None
    ResourceIdentifierPrefix: Optional[str] = None
    ResourceTypes: Optional[Sequence[ResourceTypeType]] = None
    TelemetryConfigurationState: Optional[Mapping[TelemetryTypeType, TelemetryStateType]] = None
    ResourceTags: Optional[Mapping[str, str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourceTelemetryInputPaginate(BaseValidatorModel):
    ResourceIdentifierPrefix: Optional[str] = None
    ResourceTypes: Optional[Sequence[ResourceTypeType]] = None
    TelemetryConfigurationState: Optional[Mapping[TelemetryTypeType, TelemetryStateType]] = None
    ResourceTags: Optional[Mapping[str, str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourceTelemetryForOrganizationOutput(BaseValidatorModel):
    TelemetryConfigurations: List[TelemetryConfiguration]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListResourceTelemetryOutput(BaseValidatorModel):
    TelemetryConfigurations: List[TelemetryConfiguration]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


