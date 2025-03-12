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
from aws_resource_validator.pydantic_models.cloud9_constants import *

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateEnvironmentMembershipRequestTypeDef(BaseValidatorModel):
    environmentId: str
    userArn: str
    permissions: MemberPermissionsType


class EnvironmentMemberTypeDef(BaseValidatorModel):
    permissions: PermissionsType
    userId: str
    userArn: str
    environmentId: str
    lastAccess: Optional[datetime] = None


class DeleteEnvironmentMembershipRequestTypeDef(BaseValidatorModel):
    environmentId: str
    userArn: str


class DeleteEnvironmentRequestTypeDef(BaseValidatorModel):
    environmentId: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeEnvironmentMembershipsRequestTypeDef(BaseValidatorModel):
    userArn: Optional[str] = None
    environmentId: Optional[str] = None
    permissions: Optional[Sequence[PermissionsType]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class DescribeEnvironmentStatusRequestTypeDef(BaseValidatorModel):
    environmentId: str


class DescribeEnvironmentsRequestTypeDef(BaseValidatorModel):
    environmentIds: Sequence[str]


class EnvironmentLifecycleTypeDef(BaseValidatorModel):
    status: Optional[EnvironmentLifecycleStatusType] = None
    reason: Optional[str] = None
    failureResource: Optional[str] = None


class ListEnvironmentsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateEnvironmentMembershipRequestTypeDef(BaseValidatorModel):
    environmentId: str
    userArn: str
    permissions: MemberPermissionsType


class UpdateEnvironmentRequestTypeDef(BaseValidatorModel):
    environmentId: str
    name: Optional[str] = None
    description: Optional[str] = None
    managedCredentialsAction: Optional[ManagedCredentialsActionType] = None


class CreateEnvironmentEC2RequestTypeDef(BaseValidatorModel):
    name: str
    instanceType: str
    imageId: str
    description: Optional[str] = None
    clientRequestToken: Optional[str] = None
    subnetId: Optional[str] = None
    automaticStopTimeMinutes: Optional[int] = None
    ownerArn: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    connectionType: Optional[ConnectionTypeType] = None
    dryRun: Optional[bool] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]


class CreateEnvironmentEC2ResultTypeDef(BaseValidatorModel):
    environmentId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeEnvironmentStatusResultTypeDef(BaseValidatorModel):
    status: EnvironmentStatusType
    message: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListEnvironmentsResultTypeDef(BaseValidatorModel):
    environmentIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateEnvironmentMembershipResultTypeDef(BaseValidatorModel):
    membership: EnvironmentMemberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeEnvironmentMembershipsResultTypeDef(BaseValidatorModel):
    memberships: List[EnvironmentMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateEnvironmentMembershipResultTypeDef(BaseValidatorModel):
    membership: EnvironmentMemberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeEnvironmentMembershipsRequestPaginateTypeDef(BaseValidatorModel):
    userArn: Optional[str] = None
    environmentId: Optional[str] = None
    permissions: Optional[Sequence[PermissionsType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEnvironmentsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class EnvironmentTypeDef(BaseValidatorModel):
    pass


class DescribeEnvironmentsResultTypeDef(BaseValidatorModel):
    environments: List[EnvironmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


