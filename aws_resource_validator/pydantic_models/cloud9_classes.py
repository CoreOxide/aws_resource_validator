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
from aws_resource_validator.pydantic_models.cloud9_constants import *

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateEnvironmentMembershipRequestRequestTypeDef(BaseModel):
    environmentId: str
    userArn: str
    permissions: MemberPermissionsType

class EnvironmentMemberTypeDef(BaseModel):
    permissions: PermissionsType
    userId: str
    userArn: str
    environmentId: str
    lastAccess: Optional[datetime] = None

class DeleteEnvironmentMembershipRequestRequestTypeDef(BaseModel):
    environmentId: str
    userArn: str

class DeleteEnvironmentRequestRequestTypeDef(BaseModel):
    environmentId: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeEnvironmentMembershipsRequestRequestTypeDef(BaseModel):
    userArn: Optional[str] = None
    environmentId: Optional[str] = None
    permissions: Optional[Sequence[PermissionsType]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class DescribeEnvironmentStatusRequestRequestTypeDef(BaseModel):
    environmentId: str

class DescribeEnvironmentsRequestRequestTypeDef(BaseModel):
    environmentIds: Sequence[str]

class EnvironmentLifecycleTypeDef(BaseModel):
    status: Optional[EnvironmentLifecycleStatusType] = None
    reason: Optional[str] = None
    failureResource: Optional[str] = None

class ListEnvironmentsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateEnvironmentMembershipRequestRequestTypeDef(BaseModel):
    environmentId: str
    userArn: str
    permissions: MemberPermissionsType

class UpdateEnvironmentRequestRequestTypeDef(BaseModel):
    environmentId: str
    name: Optional[str] = None
    description: Optional[str] = None
    managedCredentialsAction: Optional[ManagedCredentialsActionType] = None

class CreateEnvironmentEC2RequestRequestTypeDef(BaseModel):
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

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateEnvironmentEC2ResultTypeDef(BaseModel):
    environmentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEnvironmentStatusResultTypeDef(BaseModel):
    status: EnvironmentStatusType
    message: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnvironmentsResultTypeDef(BaseModel):
    nextToken: str
    environmentIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEnvironmentMembershipResultTypeDef(BaseModel):
    membership: EnvironmentMemberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEnvironmentMembershipsResultTypeDef(BaseModel):
    memberships: List[EnvironmentMemberTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnvironmentMembershipResultTypeDef(BaseModel):
    membership: EnvironmentMemberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEnvironmentMembershipsRequestDescribeEnvironmentMembershipsPaginateTypeDef(BaseModel):
    userArn: Optional[str] = None
    environmentId: Optional[str] = None
    permissions: Optional[Sequence[PermissionsType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnvironmentsRequestListEnvironmentsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class EnvironmentTypeDef(BaseModel):
    type: EnvironmentTypeType
    arn: str
    ownerArn: str
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    connectionType: Optional[ConnectionTypeType] = None
    lifecycle: Optional[EnvironmentLifecycleTypeDef] = None
    managedCredentialsStatus: Optional[ManagedCredentialsStatusType] = None

class DescribeEnvironmentsResultTypeDef(BaseModel):
    environments: List[EnvironmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

