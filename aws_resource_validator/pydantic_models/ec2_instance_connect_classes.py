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
from aws_resource_validator.pydantic_models.ec2_instance_connect_constants import *

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class SendSSHPublicKeyRequestRequestTypeDef(BaseModel):
    InstanceId: str
    InstanceOSUser: str
    SSHPublicKey: str
    AvailabilityZone: Optional[str] = None

class SendSerialConsoleSSHPublicKeyRequestRequestTypeDef(BaseModel):
    InstanceId: str
    SSHPublicKey: str
    SerialPort: Optional[int] = None

class SendSSHPublicKeyResponseTypeDef(BaseModel):
    RequestId: str
    Success: bool
    ResponseMetadata: ResponseMetadataTypeDef

class SendSerialConsoleSSHPublicKeyResponseTypeDef(BaseModel):
    RequestId: str
    Success: bool
    ResponseMetadata: ResponseMetadataTypeDef

