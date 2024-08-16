from datetime import datetime
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
from aws_resource_validator.pydantic_models.ec2_instance_connect_constants import *

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class SendSSHPublicKeyRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    InstanceOSUser: str
    SSHPublicKey: str
    AvailabilityZone: Optional[str] = None

class SendSerialConsoleSSHPublicKeyRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    SSHPublicKey: str
    SerialPort: Optional[int] = None

class SendSSHPublicKeyResponseTypeDef(BaseValidatorModel):
    RequestId: str
    Success: bool
    ResponseMetadata: ResponseMetadataTypeDef

class SendSerialConsoleSSHPublicKeyResponseTypeDef(BaseValidatorModel):
    RequestId: str
    Success: bool
    ResponseMetadata: ResponseMetadataTypeDef

