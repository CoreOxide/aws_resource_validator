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
from aws_resource_validator.pydantic_models.notificationscontacts_constants import *

class ActivateEmailContactRequestTypeDef(BaseValidatorModel):
    arn: str
    code: str


class CreateEmailContactRequestTypeDef(BaseValidatorModel):
    name: str
    emailAddress: str
    tags: Optional[Mapping[str, str]] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteEmailContactRequestTypeDef(BaseValidatorModel):
    arn: str


class EmailContactTypeDef(BaseValidatorModel):
    arn: str
    name: str
    address: str
    status: EmailContactStatusType
    creationTime: datetime
    updateTime: datetime


class GetEmailContactRequestTypeDef(BaseValidatorModel):
    arn: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListEmailContactsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    arn: str


class SendActivationCodeRequestTypeDef(BaseValidatorModel):
    arn: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    arn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    arn: str
    tagKeys: Sequence[str]


class CreateEmailContactResponseTypeDef(BaseValidatorModel):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetEmailContactResponseTypeDef(BaseValidatorModel):
    emailContact: EmailContactTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListEmailContactsResponseTypeDef(BaseValidatorModel):
    emailContacts: List[EmailContactTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListEmailContactsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


