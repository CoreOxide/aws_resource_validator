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
from aws_resource_validator.pydantic_models.supplychain_constants import *

class BillOfMaterialsImportJobTypeDef(BaseValidatorModel):
    instanceId: str
    jobId: str
    status: ConfigurationJobStatusType
    s3uri: str
    message: Optional[str] = None


class CreateBillOfMaterialsImportJobRequestTypeDef(BaseValidatorModel):
    instanceId: str
    s3uri: str
    clientToken: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateInstanceRequestTypeDef(BaseValidatorModel):
    instanceName: Optional[str] = None
    instanceDescription: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    webAppDnsDomain: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None


class InstanceTypeDef(BaseValidatorModel):
    instanceId: str
    awsAccountId: str
    state: InstanceStateType
    errorMessage: Optional[str] = None
    webAppDnsDomain: Optional[str] = None
    createdTime: Optional[datetime] = None
    lastModifiedTime: Optional[datetime] = None
    instanceName: Optional[str] = None
    instanceDescription: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    versionNumber: Optional[float] = None


class DataIntegrationFlowDatasetOptionsTypeDef(BaseValidatorModel):
    loadType: Optional[DataIntegrationFlowLoadTypeType] = None
    dedupeRecords: Optional[bool] = None


class DataIntegrationFlowS3OptionsTypeDef(BaseValidatorModel):
    fileType: Optional[DataIntegrationFlowFileTypeType] = None


class DataIntegrationFlowSQLTransformationConfigurationTypeDef(BaseValidatorModel):
    query: str


class DeleteDataIntegrationFlowRequestTypeDef(BaseValidatorModel):
    instanceId: str
    name: str


class DeleteDataLakeDatasetRequestTypeDef(BaseValidatorModel):
    instanceId: str
    namespace: str
    name: str


class DeleteInstanceRequestTypeDef(BaseValidatorModel):
    instanceId: str


class GetBillOfMaterialsImportJobRequestTypeDef(BaseValidatorModel):
    instanceId: str
    jobId: str


class GetDataIntegrationFlowRequestTypeDef(BaseValidatorModel):
    instanceId: str
    name: str


class GetDataLakeDatasetRequestTypeDef(BaseValidatorModel):
    instanceId: str
    namespace: str
    name: str


class GetInstanceRequestTypeDef(BaseValidatorModel):
    instanceId: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListDataIntegrationFlowsRequestTypeDef(BaseValidatorModel):
    instanceId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDataLakeDatasetsRequestTypeDef(BaseValidatorModel):
    instanceId: str
    namespace: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListInstancesRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    instanceNameFilter: Optional[Sequence[str]] = None
    instanceStateFilter: Optional[Sequence[InstanceStateType]] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateDataLakeDatasetRequestTypeDef(BaseValidatorModel):
    instanceId: str
    namespace: str
    name: str
    description: Optional[str] = None


class UpdateInstanceRequestTypeDef(BaseValidatorModel):
    instanceId: str
    instanceName: Optional[str] = None
    instanceDescription: Optional[str] = None


class CreateBillOfMaterialsImportJobResponseTypeDef(BaseValidatorModel):
    jobId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDataIntegrationFlowResponseTypeDef(BaseValidatorModel):
    instanceId: str
    name: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDataIntegrationFlowResponseTypeDef(BaseValidatorModel):
    instanceId: str
    name: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDataLakeDatasetResponseTypeDef(BaseValidatorModel):
    instanceId: str
    namespace: str
    name: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetBillOfMaterialsImportJobResponseTypeDef(BaseValidatorModel):
    job: BillOfMaterialsImportJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class SendDataIntegrationEventResponseTypeDef(BaseValidatorModel):
    eventId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateInstanceResponseTypeDef(BaseValidatorModel):
    instance: InstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteInstanceResponseTypeDef(BaseValidatorModel):
    instance: InstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetInstanceResponseTypeDef(BaseValidatorModel):
    instance: InstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListInstancesResponseTypeDef(BaseValidatorModel):
    instances: List[InstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateInstanceResponseTypeDef(BaseValidatorModel):
    instance: InstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DataIntegrationFlowDatasetSourceConfigurationTypeDef(BaseValidatorModel):
    datasetIdentifier: str
    options: Optional[DataIntegrationFlowDatasetOptionsTypeDef] = None


class DataIntegrationFlowDatasetTargetConfigurationTypeDef(BaseValidatorModel):
    datasetIdentifier: str
    options: Optional[DataIntegrationFlowDatasetOptionsTypeDef] = None


class DataIntegrationFlowS3SourceConfigurationTypeDef(BaseValidatorModel):
    bucketName: str
    prefix: str
    options: Optional[DataIntegrationFlowS3OptionsTypeDef] = None


class DataIntegrationFlowS3TargetConfigurationTypeDef(BaseValidatorModel):
    bucketName: str
    prefix: str
    options: Optional[DataIntegrationFlowS3OptionsTypeDef] = None


class DataIntegrationFlowTransformationTypeDef(BaseValidatorModel):
    transformationType: DataIntegrationFlowTransformationTypeType
    sqlTransformation: Optional[DataIntegrationFlowSQLTransformationConfigurationTypeDef] = None


class DataLakeDatasetSchemaFieldTypeDef(BaseValidatorModel):
    pass


class DataLakeDatasetSchemaOutputTypeDef(BaseValidatorModel):
    name: str
    fields: List[DataLakeDatasetSchemaFieldTypeDef]


class DataLakeDatasetSchemaTypeDef(BaseValidatorModel):
    name: str
    fields: Sequence[DataLakeDatasetSchemaFieldTypeDef]


class ListDataIntegrationFlowsRequestPaginateTypeDef(BaseValidatorModel):
    instanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDataLakeDatasetsRequestPaginateTypeDef(BaseValidatorModel):
    instanceId: str
    namespace: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListInstancesRequestPaginateTypeDef(BaseValidatorModel):
    instanceNameFilter: Optional[Sequence[str]] = None
    instanceStateFilter: Optional[Sequence[InstanceStateType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class SendDataIntegrationEventRequestTypeDef(BaseValidatorModel):
    instanceId: str
    eventType: DataIntegrationEventTypeType
    data: str
    eventGroupId: str
    eventTimestamp: Optional[TimestampTypeDef] = None
    clientToken: Optional[str] = None


class DataIntegrationFlowSourceTypeDef(BaseValidatorModel):
    sourceType: DataIntegrationFlowSourceTypeType
    sourceName: str
    s3Source: Optional[DataIntegrationFlowS3SourceConfigurationTypeDef] = None
    datasetSource: Optional[DataIntegrationFlowDatasetSourceConfigurationTypeDef] = None


class DataIntegrationFlowTargetTypeDef(BaseValidatorModel):
    targetType: DataIntegrationFlowTargetTypeType
    s3Target: Optional[DataIntegrationFlowS3TargetConfigurationTypeDef] = None
    datasetTarget: Optional[DataIntegrationFlowDatasetTargetConfigurationTypeDef] = None


class DataLakeDatasetTypeDef(BaseValidatorModel):
    instanceId: str
    namespace: str
    name: str
    arn: str
    schema: DataLakeDatasetSchemaOutputTypeDef
    createdTime: datetime
    lastModifiedTime: datetime
    description: Optional[str] = None


class CreateDataIntegrationFlowRequestTypeDef(BaseValidatorModel):
    instanceId: str
    name: str
    sources: Sequence[DataIntegrationFlowSourceTypeDef]
    transformation: DataIntegrationFlowTransformationTypeDef
    target: DataIntegrationFlowTargetTypeDef
    tags: Optional[Mapping[str, str]] = None


class DataIntegrationFlowTypeDef(BaseValidatorModel):
    instanceId: str
    name: str
    sources: List[DataIntegrationFlowSourceTypeDef]
    transformation: DataIntegrationFlowTransformationTypeDef
    target: DataIntegrationFlowTargetTypeDef
    createdTime: datetime
    lastModifiedTime: datetime


class UpdateDataIntegrationFlowRequestTypeDef(BaseValidatorModel):
    instanceId: str
    name: str
    sources: Optional[Sequence[DataIntegrationFlowSourceTypeDef]] = None
    transformation: Optional[DataIntegrationFlowTransformationTypeDef] = None
    target: Optional[DataIntegrationFlowTargetTypeDef] = None


class CreateDataLakeDatasetResponseTypeDef(BaseValidatorModel):
    dataset: DataLakeDatasetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetDataLakeDatasetResponseTypeDef(BaseValidatorModel):
    dataset: DataLakeDatasetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListDataLakeDatasetsResponseTypeDef(BaseValidatorModel):
    datasets: List[DataLakeDatasetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateDataLakeDatasetResponseTypeDef(BaseValidatorModel):
    dataset: DataLakeDatasetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DataLakeDatasetSchemaUnionTypeDef(BaseValidatorModel):
    pass


class CreateDataLakeDatasetRequestTypeDef(BaseValidatorModel):
    instanceId: str
    namespace: str
    name: str
    schema: Optional[DataLakeDatasetSchemaUnionTypeDef] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class GetDataIntegrationFlowResponseTypeDef(BaseValidatorModel):
    flow: DataIntegrationFlowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListDataIntegrationFlowsResponseTypeDef(BaseValidatorModel):
    flows: List[DataIntegrationFlowTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateDataIntegrationFlowResponseTypeDef(BaseValidatorModel):
    flow: DataIntegrationFlowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


