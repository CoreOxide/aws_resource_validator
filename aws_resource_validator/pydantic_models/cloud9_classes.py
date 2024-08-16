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
from aws_resource_validator.pydantic_models.cloud9_constants import *

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateEnvironmentMembershipRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    userArn: str
    permissions: MemberPermissionsType

class EnvironmentMemberTypeDef(BaseValidatorModel):
    permissions: PermissionsType
    userId: str
    userArn: str
    environmentId: str
    lastAccess: Optional[datetime] = None

class DeleteEnvironmentMembershipRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    userArn: str

class DeleteEnvironmentRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeEnvironmentMembershipsRequestRequestTypeDef(BaseValidatorModel):
    userArn: Optional[str] = None
    environmentId: Optional[str] = None
    permissions: Optional[Sequence[PermissionsType]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class DescribeEnvironmentStatusRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str

class DescribeEnvironmentsRequestRequestTypeDef(BaseValidatorModel):
    environmentIds: Sequence[str]

class EnvironmentLifecycleTypeDef(BaseValidatorModel):
    status: Optional[EnvironmentLifecycleStatusType] = None
    reason: Optional[str] = None
    failureResource: Optional[str] = None

class ListEnvironmentsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateEnvironmentMembershipRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    userArn: str
    permissions: MemberPermissionsType

class UpdateEnvironmentRequestRequestTypeDef(BaseValidatorModel):
    environmentId: str
    name: Optional[str] = None
    description: Optional[str] = None
    managedCredentialsAction: Optional[ManagedCredentialsActionType] = None

class CreateEnvironmentEC2RequestRequestTypeDef(BaseValidatorModel):
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

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
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
    nextToken: str
    environmentIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEnvironmentMembershipResultTypeDef(BaseValidatorModel):
    membership: EnvironmentMemberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEnvironmentMembershipsResultTypeDef(BaseValidatorModel):
    memberships: List[EnvironmentMemberTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnvironmentMembershipResultTypeDef(BaseValidatorModel):
    membership: EnvironmentMemberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEnvironmentMembershipsRequestDescribeEnvironmentMembershipsPaginateTypeDef(BaseValidatorModel):
    userArn: Optional[str] = None
    environmentId: Optional[str] = None
    permissions: Optional[Sequence[PermissionsType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnvironmentsRequestListEnvironmentsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class EnvironmentTypeDef(BaseValidatorModel):
    type: EnvironmentTypeType
    arn: str
    ownerArn: str
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    connectionType: Optional[ConnectionTypeType] = None
    lifecycle: Optional[EnvironmentLifecycleTypeDef] = None
    managedCredentialsStatus: Optional[ManagedCredentialsStatusType] = None

class DescribeEnvironmentsResultTypeDef(BaseValidatorModel):
    environments: List[EnvironmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

