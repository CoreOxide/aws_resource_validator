from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.connectcampaigns.connectcampaigns_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AgentlessDialerConfig(BaseValidatorModel):
    dialingCapacity: Optional[float] = None


class AnswerMachineDetectionConfig(BaseValidatorModel):
    enableAnswerMachineDetection: bool
    awaitAnswerMachinePrompt: Optional[bool] = None


class InstanceIdFilter(BaseValidatorModel):
    value: str
    operator: Literal['Eq']


class CampaignSummary(BaseValidatorModel):
    id: str
    arn: str
    name: str
    connectInstanceId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteCampaignRequest(BaseValidatorModel):
    id: str


class DeleteConnectInstanceConfigRequest(BaseValidatorModel):
    connectInstanceId: str


class DeleteInstanceOnboardingJobRequest(BaseValidatorModel):
    connectInstanceId: str


class DescribeCampaignRequest(BaseValidatorModel):
    id: str

Timestamp = Union[datetime, str]


class PredictiveDialerConfig(BaseValidatorModel):
    bandwidthAllocation: float
    dialingCapacity: Optional[float] = None


class ProgressiveDialerConfig(BaseValidatorModel):
    bandwidthAllocation: float
    dialingCapacity: Optional[float] = None


class EncryptionConfig(BaseValidatorModel):
    enabled: bool
    encryptionType: Optional[Literal['KMS']] = None
    keyArn: Optional[str] = None


class FailedCampaignStateResponse(BaseValidatorModel):
    campaignId: Optional[str] = None
    failureCode: Optional[GetCampaignStateBatchFailureCodeType] = None


class FailedRequest(BaseValidatorModel):
    clientToken: Optional[str] = None
    id: Optional[str] = None
    failureCode: Optional[FailureCodeType] = None


class GetCampaignStateBatchRequest(BaseValidatorModel):
    campaignIds: List[str]


class SuccessfulCampaignStateResponse(BaseValidatorModel):
    campaignId: Optional[str] = None
    state: Optional[CampaignStateType] = None


class GetCampaignStateRequest(BaseValidatorModel):
    id: str


class GetConnectInstanceConfigRequest(BaseValidatorModel):
    connectInstanceId: str


class GetInstanceOnboardingJobStatusRequest(BaseValidatorModel):
    connectInstanceId: str


class InstanceOnboardingJobStatus(BaseValidatorModel):
    connectInstanceId: str
    status: InstanceOnboardingJobStatusCodeType
    failureCode: Optional[InstanceOnboardingJobFailureCodeType] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    arn: str


class PauseCampaignRequest(BaseValidatorModel):
    id: str


class SuccessfulRequest(BaseValidatorModel):
    clientToken: Optional[str] = None
    id: Optional[str] = None


class ResumeCampaignRequest(BaseValidatorModel):
    id: str


class StartCampaignRequest(BaseValidatorModel):
    id: str


class StopCampaignRequest(BaseValidatorModel):
    id: str


class TagResourceRequest(BaseValidatorModel):
    arn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    arn: str
    tagKeys: List[str]


class UpdateCampaignNameRequest(BaseValidatorModel):
    id: str
    name: str


class OutboundCallConfig(BaseValidatorModel):
    connectContactFlowId: str
    connectSourcePhoneNumber: Optional[str] = None
    connectQueueId: Optional[str] = None
    answerMachineDetectionConfig: Optional[AnswerMachineDetectionConfig] = None


class UpdateCampaignOutboundCallConfigRequest(BaseValidatorModel):
    id: str
    connectContactFlowId: Optional[str] = None
    connectSourcePhoneNumber: Optional[str] = None
    answerMachineDetectionConfig: Optional[AnswerMachineDetectionConfig] = None


class CampaignFilters(BaseValidatorModel):
    instanceIdFilter: Optional[InstanceIdFilter] = None


class CreateCampaignResponse(BaseValidatorModel):
    id: str
    arn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetCampaignStateResponse(BaseValidatorModel):
    state: CampaignStateType
    ResponseMetadata: ResponseMetadata


class ListCampaignsResponse(BaseValidatorModel):
    campaignSummaryList: List[CampaignSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class DialRequest(BaseValidatorModel):
    clientToken: str
    phoneNumber: str
    expirationTime: Timestamp
    attributes: Dict[str, str]


class DialerConfig(BaseValidatorModel):
    progressiveDialerConfig: Optional[ProgressiveDialerConfig] = None
    predictiveDialerConfig: Optional[PredictiveDialerConfig] = None
    agentlessDialerConfig: Optional[AgentlessDialerConfig] = None


class InstanceConfig(BaseValidatorModel):
    connectInstanceId: str
    serviceLinkedRoleArn: str
    encryptionConfig: EncryptionConfig


class StartInstanceOnboardingJobRequest(BaseValidatorModel):
    connectInstanceId: str
    encryptionConfig: EncryptionConfig


class GetCampaignStateBatchResponse(BaseValidatorModel):
    successfulRequests: List[SuccessfulCampaignStateResponse]
    failedRequests: List[FailedCampaignStateResponse]
    ResponseMetadata: ResponseMetadata


class GetInstanceOnboardingJobStatusResponse(BaseValidatorModel):
    connectInstanceOnboardingJobStatus: InstanceOnboardingJobStatus
    ResponseMetadata: ResponseMetadata


class StartInstanceOnboardingJobResponse(BaseValidatorModel):
    connectInstanceOnboardingJobStatus: InstanceOnboardingJobStatus
    ResponseMetadata: ResponseMetadata


class PutDialRequestBatchResponse(BaseValidatorModel):
    successfulRequests: List[SuccessfulRequest]
    failedRequests: List[FailedRequest]
    ResponseMetadata: ResponseMetadata


class ListCampaignsRequestPaginate(BaseValidatorModel):
    filters: Optional[CampaignFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCampaignsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filters: Optional[CampaignFilters] = None


class PutDialRequestBatchRequest(BaseValidatorModel):
    id: str
    dialRequests: List[DialRequest]


class Campaign(BaseValidatorModel):
    id: str
    arn: str
    name: str
    connectInstanceId: str
    dialerConfig: DialerConfig
    outboundCallConfig: OutboundCallConfig
    tags: Optional[Dict[str, str]] = None


class CreateCampaignRequest(BaseValidatorModel):
    name: str
    connectInstanceId: str
    dialerConfig: DialerConfig
    outboundCallConfig: OutboundCallConfig
    tags: Optional[Dict[str, str]] = None


class UpdateCampaignDialerConfigRequest(BaseValidatorModel):
    id: str
    dialerConfig: DialerConfig


class GetConnectInstanceConfigResponse(BaseValidatorModel):
    connectInstanceConfig: InstanceConfig
    ResponseMetadata: ResponseMetadata


class DescribeCampaignResponse(BaseValidatorModel):
    campaign: Campaign
    ResponseMetadata: ResponseMetadata