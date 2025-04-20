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


class SendSSHPublicKeyRequest(BaseValidatorModel):
    InstanceId: str
    InstanceOSUser: str
    SSHPublicKey: str
    AvailabilityZone: Optional[str] = None


class SendSerialConsoleSSHPublicKeyRequest(BaseValidatorModel):
    InstanceId: str
    SSHPublicKey: str
    SerialPort: Optional[int] = None


class SendSSHPublicKeyResponse(BaseValidatorModel):
    RequestId: str
    Success: bool
    ResponseMetadata: ResponseMetadata


class SendSerialConsoleSSHPublicKeyResponse(BaseValidatorModel):
    RequestId: str
    Success: bool
    ResponseMetadata: ResponseMetadata