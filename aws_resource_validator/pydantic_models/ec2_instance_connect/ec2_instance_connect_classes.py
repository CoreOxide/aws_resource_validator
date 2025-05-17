from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.ec2_instance_connect.ec2_instance_connect_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'send_ssh_public_key' function.
class SendSSHPublicKeyRequest(BaseValidatorModel):
    InstanceId: str
    InstanceOSUser: str
    SSHPublicKey: str
    AvailabilityZone: Optional[str] = None


# This class is the input for the 'send_serial_console_ssh_public_key' function.
class SendSerialConsoleSSHPublicKeyRequest(BaseValidatorModel):
    InstanceId: str
    SSHPublicKey: str
    SerialPort: Optional[int] = None


# This class is the output for the 'send_ssh_public_key' function.
class SendSSHPublicKeyResponse(BaseValidatorModel):
    RequestId: str
    Success: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'send_serial_console_ssh_public_key' function.
class SendSerialConsoleSSHPublicKeyResponse(BaseValidatorModel):
    RequestId: str
    Success: bool
    ResponseMetadata: ResponseMetadata