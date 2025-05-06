from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.appconfigdata.appconfigdata_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class GetLatestConfigurationRequest(BaseValidatorModel):
    ConfigurationToken: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class StartConfigurationSessionRequest(BaseValidatorModel):
    ApplicationIdentifier: str
    EnvironmentIdentifier: str
    ConfigurationProfileIdentifier: str
    RequiredMinimumPollIntervalInSeconds: Optional[int] = None


class GetLatestConfigurationResponse(BaseValidatorModel):
    NextPollConfigurationToken: str
    NextPollIntervalInSeconds: int
    ContentType: str
    Configuration: StreamingBody
    VersionLabel: str
    ResponseMetadata: ResponseMetadata


class StartConfigurationSessionResponse(BaseValidatorModel):
    InitialConfigurationToken: str
    ResponseMetadata: ResponseMetadata