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

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListResourceTelemetryForOrganizationInputTypeDef(BaseValidatorModel):
    AccountIdentifiers: Optional[Sequence[str]] = None
    ResourceIdentifierPrefix: Optional[str] = None
    ResourceTypes: Optional[Sequence[ResourceTypeType]] = None
    TelemetryConfigurationState: Optional[Mapping[TelemetryTypeType, TelemetryStateType]] = None
    ResourceTags: Optional[Mapping[str, str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class TelemetryConfigurationTypeDef(BaseValidatorModel):
    AccountIdentifier: Optional[str] = None
    TelemetryConfigurationState: Optional[Dict[TelemetryTypeType, TelemetryStateType]] = None
    ResourceType: Optional[ResourceTypeType] = None
    ResourceIdentifier: Optional[str] = None
    ResourceTags: Optional[Dict[str, str]] = None
    LastUpdateTimeStamp: Optional[int] = None


class ListResourceTelemetryInputTypeDef(BaseValidatorModel):
    ResourceIdentifierPrefix: Optional[str] = None
    ResourceTypes: Optional[Sequence[ResourceTypeType]] = None
    TelemetryConfigurationState: Optional[Mapping[TelemetryTypeType, TelemetryStateType]] = None
    ResourceTags: Optional[Mapping[str, str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetTelemetryEvaluationStatusForOrganizationOutputTypeDef(BaseValidatorModel):
    Status: StatusType
    FailureReason: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetTelemetryEvaluationStatusOutputTypeDef(BaseValidatorModel):
    Status: StatusType
    FailureReason: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListResourceTelemetryForOrganizationInputPaginateTypeDef(BaseValidatorModel):
    AccountIdentifiers: Optional[Sequence[str]] = None
    ResourceIdentifierPrefix: Optional[str] = None
    ResourceTypes: Optional[Sequence[ResourceTypeType]] = None
    TelemetryConfigurationState: Optional[Mapping[TelemetryTypeType, TelemetryStateType]] = None
    ResourceTags: Optional[Mapping[str, str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResourceTelemetryInputPaginateTypeDef(BaseValidatorModel):
    ResourceIdentifierPrefix: Optional[str] = None
    ResourceTypes: Optional[Sequence[ResourceTypeType]] = None
    TelemetryConfigurationState: Optional[Mapping[TelemetryTypeType, TelemetryStateType]] = None
    ResourceTags: Optional[Mapping[str, str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResourceTelemetryForOrganizationOutputTypeDef(BaseValidatorModel):
    TelemetryConfigurations: List[TelemetryConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListResourceTelemetryOutputTypeDef(BaseValidatorModel):
    TelemetryConfigurations: List[TelemetryConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


