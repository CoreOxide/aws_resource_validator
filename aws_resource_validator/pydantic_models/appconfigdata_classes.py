from datetime import datetime
from pydantic import BaseModel
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

class GetLatestConfigurationRequestRequestTypeDef(BaseModel):
    ConfigurationToken: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class StartConfigurationSessionRequestRequestTypeDef(BaseModel):
    ApplicationIdentifier: str
    EnvironmentIdentifier: str
    ConfigurationProfileIdentifier: str
    RequiredMinimumPollIntervalInSeconds: Optional[int] = None

class GetLatestConfigurationResponseTypeDef(BaseModel):
    NextPollConfigurationToken: str
    NextPollIntervalInSeconds: int
    ContentType: str
    Configuration: StreamingBody
    VersionLabel: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartConfigurationSessionResponseTypeDef(BaseModel):
    InitialConfigurationToken: str
    ResponseMetadata: ResponseMetadataTypeDef

