from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.observabilityadmin.observabilityadmin_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




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
    AccountIdentifiers: Optional[List[str]] = None
    ResourceIdentifierPrefix: Optional[str] = None
    ResourceTypes: Optional[List[ResourceTypeType]] = None
    TelemetryConfigurationState: Optional[Dict[TelemetryTypeType, TelemetryStateType]] = None
    ResourceTags: Optional[Dict[str, str]] = None
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
    ResourceTypes: Optional[List[ResourceTypeType]] = None
    TelemetryConfigurationState: Optional[Dict[TelemetryTypeType, TelemetryStateType]] = None
    ResourceTags: Optional[Dict[str, str]] = None
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
    AccountIdentifiers: Optional[List[str]] = None
    ResourceIdentifierPrefix: Optional[str] = None
    ResourceTypes: Optional[List[ResourceTypeType]] = None
    TelemetryConfigurationState: Optional[Dict[TelemetryTypeType, TelemetryStateType]] = None
    ResourceTags: Optional[Dict[str, str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourceTelemetryInputPaginate(BaseValidatorModel):
    ResourceIdentifierPrefix: Optional[str] = None
    ResourceTypes: Optional[List[ResourceTypeType]] = None
    TelemetryConfigurationState: Optional[Dict[TelemetryTypeType, TelemetryStateType]] = None
    ResourceTags: Optional[Dict[str, str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourceTelemetryForOrganizationOutput(BaseValidatorModel):
    TelemetryConfigurations: List[TelemetryConfiguration]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListResourceTelemetryOutput(BaseValidatorModel):
    TelemetryConfigurations: List[TelemetryConfiguration]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None