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
from aws_resource_validator.pydantic_models.appconfigdata_constants import *

class GetLatestConfigurationRequestTypeDef(BaseValidatorModel):
    ConfigurationToken: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class StartConfigurationSessionRequestTypeDef(BaseValidatorModel):
    ApplicationIdentifier: str
    EnvironmentIdentifier: str
    ConfigurationProfileIdentifier: str
    RequiredMinimumPollIntervalInSeconds: Optional[int] = None


class GetLatestConfigurationResponseTypeDef(BaseValidatorModel):
    NextPollConfigurationToken: str
    NextPollIntervalInSeconds: int
    ContentType: str
    Configuration: StreamingBody
    VersionLabel: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartConfigurationSessionResponseTypeDef(BaseValidatorModel):
    InitialConfigurationToken: str
    ResponseMetadata: ResponseMetadataTypeDef


