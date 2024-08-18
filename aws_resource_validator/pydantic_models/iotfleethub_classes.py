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
from aws_resource_validator.pydantic_models.iotfleethub_constants import *

class ApplicationSummaryTypeDef(BaseValidatorModel):
    applicationId: str
    applicationName: str
    applicationUrl: str
    applicationDescription: Optional[str] = None
    applicationCreationDate: Optional[int] = None
    applicationLastUpdateDate: Optional[int] = None
    applicationState: Optional[ApplicationStateType] = None

class CreateApplicationRequestRequestTypeDef(BaseValidatorModel):
    applicationName: str
    roleArn: str
    applicationDescription: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DeleteApplicationRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    clientToken: Optional[str] = None

class DescribeApplicationRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListApplicationsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateApplicationRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    applicationName: Optional[str] = None
    applicationDescription: Optional[str] = None
    clientToken: Optional[str] = None

class CreateApplicationResponseTypeDef(BaseValidatorModel):
    applicationId: str
    applicationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeApplicationResponseTypeDef(BaseValidatorModel):
    applicationId: str
    applicationArn: str
    applicationName: str
    applicationDescription: str
    applicationUrl: str
    applicationState: ApplicationStateType
    applicationCreationDate: int
    applicationLastUpdateDate: int
    roleArn: str
    ssoClientId: str
    errorMessage: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationsResponseTypeDef(BaseValidatorModel):
    applicationSummaries: List[ApplicationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationsRequestListApplicationsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

