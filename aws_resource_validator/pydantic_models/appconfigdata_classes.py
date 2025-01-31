from datetime import datetime

from botocore.response import StreamingBody

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
from aws_resource_validator.pydantic_models.appconfigdata_constants import *

class GetLatestConfigurationRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationToken: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class StartConfigurationSessionRequestRequestTypeDef(BaseValidatorModel):
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

