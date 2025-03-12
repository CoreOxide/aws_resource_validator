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
from aws_resource_validator.pydantic_models.connectcampaigns_constants import *

class AgentlessDialerConfigTypeDef(BaseValidatorModel):
    dialingCapacity: Optional[float] = None


class AnswerMachineDetectionConfigTypeDef(BaseValidatorModel):
    enableAnswerMachineDetection: bool
    awaitAnswerMachinePrompt: Optional[bool] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteConnectInstanceConfigRequestTypeDef(BaseValidatorModel):
    connectInstanceId: str


class DeleteInstanceOnboardingJobRequestTypeDef(BaseValidatorModel):
    connectInstanceId: str


class PredictiveDialerConfigTypeDef(BaseValidatorModel):
    bandwidthAllocation: float
    dialingCapacity: Optional[float] = None


class ProgressiveDialerConfigTypeDef(BaseValidatorModel):
    bandwidthAllocation: float
    dialingCapacity: Optional[float] = None


class EncryptionConfigTypeDef(BaseValidatorModel):
    enabled: bool
    encryptionType: Optional[Literal["KMS"]] = None
    keyArn: Optional[str] = None


class FailedCampaignStateResponseTypeDef(BaseValidatorModel):
    campaignId: Optional[str] = None
    failureCode: Optional[GetCampaignStateBatchFailureCodeType] = None


class GetCampaignStateBatchRequestTypeDef(BaseValidatorModel):
    campaignIds: Sequence[str]


class SuccessfulCampaignStateResponseTypeDef(BaseValidatorModel):
    campaignId: Optional[str] = None
    state: Optional[CampaignStateType] = None


class GetConnectInstanceConfigRequestTypeDef(BaseValidatorModel):
    connectInstanceId: str


class GetInstanceOnboardingJobStatusRequestTypeDef(BaseValidatorModel):
    connectInstanceId: str


class InstanceOnboardingJobStatusTypeDef(BaseValidatorModel):
    connectInstanceId: str
    status: InstanceOnboardingJobStatusCodeType
    failureCode: Optional[InstanceOnboardingJobFailureCodeType] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    arn: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    arn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    arn: str
    tagKeys: Sequence[str]


class OutboundCallConfigTypeDef(BaseValidatorModel):
    connectContactFlowId: str
    connectSourcePhoneNumber: Optional[str] = None
    connectQueueId: Optional[str] = None
    answerMachineDetectionConfig: Optional[AnswerMachineDetectionConfigTypeDef] = None


class InstanceIdFilterTypeDef(BaseValidatorModel):
    pass


class CampaignFiltersTypeDef(BaseValidatorModel):
    instanceIdFilter: Optional[InstanceIdFilterTypeDef] = None


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetCampaignStateResponseTypeDef(BaseValidatorModel):
    state: CampaignStateType
    ResponseMetadata: ResponseMetadataTypeDef


class CampaignSummaryTypeDef(BaseValidatorModel):
    pass


class ListCampaignsResponseTypeDef(BaseValidatorModel):
    campaignSummaryList: List[CampaignSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class TimestampTypeDef(BaseValidatorModel):
    pass


class DialRequestTypeDef(BaseValidatorModel):
    clientToken: str
    phoneNumber: str
    expirationTime: TimestampTypeDef
    attributes: Mapping[str, str]


class DialerConfigTypeDef(BaseValidatorModel):
    progressiveDialerConfig: Optional[ProgressiveDialerConfigTypeDef] = None
    predictiveDialerConfig: Optional[PredictiveDialerConfigTypeDef] = None
    agentlessDialerConfig: Optional[AgentlessDialerConfigTypeDef] = None


class InstanceConfigTypeDef(BaseValidatorModel):
    connectInstanceId: str
    serviceLinkedRoleArn: str
    encryptionConfig: EncryptionConfigTypeDef


class StartInstanceOnboardingJobRequestTypeDef(BaseValidatorModel):
    connectInstanceId: str
    encryptionConfig: EncryptionConfigTypeDef


class GetCampaignStateBatchResponseTypeDef(BaseValidatorModel):
    successfulRequests: List[SuccessfulCampaignStateResponseTypeDef]
    failedRequests: List[FailedCampaignStateResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetInstanceOnboardingJobStatusResponseTypeDef(BaseValidatorModel):
    connectInstanceOnboardingJobStatus: InstanceOnboardingJobStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StartInstanceOnboardingJobResponseTypeDef(BaseValidatorModel):
    connectInstanceOnboardingJobStatus: InstanceOnboardingJobStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class FailedRequestTypeDef(BaseValidatorModel):
    pass


class SuccessfulRequestTypeDef(BaseValidatorModel):
    pass


class PutDialRequestBatchResponseTypeDef(BaseValidatorModel):
    successfulRequests: List[SuccessfulRequestTypeDef]
    failedRequests: List[FailedRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListCampaignsRequestPaginateTypeDef(BaseValidatorModel):
    filters: Optional[CampaignFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCampaignsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filters: Optional[CampaignFiltersTypeDef] = None


class CreateCampaignRequestTypeDef(BaseValidatorModel):
    name: str
    connectInstanceId: str
    dialerConfig: DialerConfigTypeDef
    outboundCallConfig: OutboundCallConfigTypeDef
    tags: Optional[Mapping[str, str]] = None


class GetConnectInstanceConfigResponseTypeDef(BaseValidatorModel):
    connectInstanceConfig: InstanceConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CampaignTypeDef(BaseValidatorModel):
    pass


class DescribeCampaignResponseTypeDef(BaseValidatorModel):
    campaign: CampaignTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


