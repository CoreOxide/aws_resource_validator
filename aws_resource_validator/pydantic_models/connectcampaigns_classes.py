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
from aws_resource_validator.pydantic_models.connectcampaigns_constants import *

class AgentlessDialerConfigTypeDef(BaseModel):
    dialingCapacity: Optional[float] = None

class AnswerMachineDetectionConfigTypeDef(BaseModel):
    enableAnswerMachineDetection: bool
    awaitAnswerMachinePrompt: Optional[bool] = None

class InstanceIdFilterTypeDef(BaseModel):
    value: str
    operator: Literal["Eq"]

class CampaignSummaryTypeDef(BaseModel):
    id: str
    arn: str
    name: str
    connectInstanceId: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DeleteCampaignRequestRequestTypeDef(BaseModel):
    id: str

class DeleteConnectInstanceConfigRequestRequestTypeDef(BaseModel):
    connectInstanceId: str

class DeleteInstanceOnboardingJobRequestRequestTypeDef(BaseModel):
    connectInstanceId: str

class DescribeCampaignRequestRequestTypeDef(BaseModel):
    id: str

class PredictiveDialerConfigTypeDef(BaseModel):
    bandwidthAllocation: float
    dialingCapacity: Optional[float] = None

class ProgressiveDialerConfigTypeDef(BaseModel):
    bandwidthAllocation: float
    dialingCapacity: Optional[float] = None

class EncryptionConfigTypeDef(BaseModel):
    enabled: bool
    encryptionType: Optional[Literal["KMS"]] = None
    keyArn: Optional[str] = None

class FailedCampaignStateResponseTypeDef(BaseModel):
    campaignId: Optional[str] = None
    failureCode: Optional[GetCampaignStateBatchFailureCodeType] = None

class FailedRequestTypeDef(BaseModel):
    clientToken: Optional[str] = None
    id: Optional[str] = None
    failureCode: Optional[FailureCodeType] = None

class GetCampaignStateBatchRequestRequestTypeDef(BaseModel):
    campaignIds: Sequence[str]

class SuccessfulCampaignStateResponseTypeDef(BaseModel):
    campaignId: Optional[str] = None
    state: Optional[CampaignStateType] = None

class GetCampaignStateRequestRequestTypeDef(BaseModel):
    id: str

class GetConnectInstanceConfigRequestRequestTypeDef(BaseModel):
    connectInstanceId: str

class GetInstanceOnboardingJobStatusRequestRequestTypeDef(BaseModel):
    connectInstanceId: str

class InstanceOnboardingJobStatusTypeDef(BaseModel):
    connectInstanceId: str
    status: InstanceOnboardingJobStatusCodeType
    failureCode: Optional[InstanceOnboardingJobFailureCodeType] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    arn: str

class PauseCampaignRequestRequestTypeDef(BaseModel):
    id: str

class SuccessfulRequestTypeDef(BaseModel):
    clientToken: Optional[str] = None
    id: Optional[str] = None

class ResumeCampaignRequestRequestTypeDef(BaseModel):
    id: str

class StartCampaignRequestRequestTypeDef(BaseModel):
    id: str

class StopCampaignRequestRequestTypeDef(BaseModel):
    id: str

class TagResourceRequestRequestTypeDef(BaseModel):
    arn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    arn: str
    tagKeys: Sequence[str]

class UpdateCampaignNameRequestRequestTypeDef(BaseModel):
    id: str
    name: str

class OutboundCallConfigTypeDef(BaseModel):
    connectContactFlowId: str
    connectSourcePhoneNumber: Optional[str] = None
    connectQueueId: Optional[str] = None
    answerMachineDetectionConfig: Optional[AnswerMachineDetectionConfigTypeDef] = None

class UpdateCampaignOutboundCallConfigRequestRequestTypeDef(BaseModel):
    id: str
    connectContactFlowId: Optional[str] = None
    connectSourcePhoneNumber: Optional[str] = None
    answerMachineDetectionConfig: Optional[AnswerMachineDetectionConfigTypeDef] = None

class CampaignFiltersTypeDef(BaseModel):
    instanceIdFilter: Optional[InstanceIdFilterTypeDef] = None

class CreateCampaignResponseTypeDef(BaseModel):
    id: str
    arn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetCampaignStateResponseTypeDef(BaseModel):
    state: CampaignStateType
    ResponseMetadata: ResponseMetadataTypeDef

class ListCampaignsResponseTypeDef(BaseModel):
    nextToken: str
    campaignSummaryList: List[CampaignSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DialRequestTypeDef(BaseModel):
    clientToken: str
    phoneNumber: str
    expirationTime: TimestampTypeDef
    attributes: Mapping[str, str]

class DialerConfigTypeDef(BaseModel):
    progressiveDialerConfig: Optional[ProgressiveDialerConfigTypeDef] = None
    predictiveDialerConfig: Optional[PredictiveDialerConfigTypeDef] = None
    agentlessDialerConfig: Optional[AgentlessDialerConfigTypeDef] = None

class InstanceConfigTypeDef(BaseModel):
    connectInstanceId: str
    serviceLinkedRoleArn: str
    encryptionConfig: EncryptionConfigTypeDef

class StartInstanceOnboardingJobRequestRequestTypeDef(BaseModel):
    connectInstanceId: str
    encryptionConfig: EncryptionConfigTypeDef

class GetCampaignStateBatchResponseTypeDef(BaseModel):
    successfulRequests: List[SuccessfulCampaignStateResponseTypeDef]
    failedRequests: List[FailedCampaignStateResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetInstanceOnboardingJobStatusResponseTypeDef(BaseModel):
    connectInstanceOnboardingJobStatus: InstanceOnboardingJobStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartInstanceOnboardingJobResponseTypeDef(BaseModel):
    connectInstanceOnboardingJobStatus: InstanceOnboardingJobStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutDialRequestBatchResponseTypeDef(BaseModel):
    successfulRequests: List[SuccessfulRequestTypeDef]
    failedRequests: List[FailedRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListCampaignsRequestListCampaignsPaginateTypeDef(BaseModel):
    filters: Optional[CampaignFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCampaignsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filters: Optional[CampaignFiltersTypeDef] = None

class PutDialRequestBatchRequestRequestTypeDef(BaseModel):
    id: str
    dialRequests: Sequence[DialRequestTypeDef]

class CampaignTypeDef(BaseModel):
    id: str
    arn: str
    name: str
    connectInstanceId: str
    dialerConfig: DialerConfigTypeDef
    outboundCallConfig: OutboundCallConfigTypeDef
    tags: Optional[Dict[str, str]] = None

class CreateCampaignRequestRequestTypeDef(BaseModel):
    name: str
    connectInstanceId: str
    dialerConfig: DialerConfigTypeDef
    outboundCallConfig: OutboundCallConfigTypeDef
    tags: Optional[Mapping[str, str]] = None

class UpdateCampaignDialerConfigRequestRequestTypeDef(BaseModel):
    id: str
    dialerConfig: DialerConfigTypeDef

class GetConnectInstanceConfigResponseTypeDef(BaseModel):
    connectInstanceConfig: InstanceConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCampaignResponseTypeDef(BaseModel):
    campaign: CampaignTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

