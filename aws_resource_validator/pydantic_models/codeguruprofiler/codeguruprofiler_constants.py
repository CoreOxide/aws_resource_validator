from typing import Literal
from datetime import datetime


ActionGroupType = Literal['agentPermissions']
AgentParameterFieldType = Literal['MaxStackDepth', 'MemoryUsageLimitPercent', 'MinimumTimeForReportingInMilliseconds', 'ReportingIntervalInMilliseconds', 'SamplingIntervalInMilliseconds']
AggregationPeriodType = Literal['P1D', 'PT1H', 'PT5M']
CodeGuruProfilerServiceName = Literal['codeguruprofiler']
ComputePlatformType = Literal['AWSLambda', 'Default']
EventPublisherType = Literal['AnomalyDetection']
FeedbackTypeType = Literal['Negative', 'Positive']
ListProfileTimesPaginatorName = Literal['list_profile_times']
MetadataFieldType = Literal['AgentId', 'AwsRequestId', 'ComputePlatform', 'ExecutionEnvironment', 'LambdaFunctionArn', 'LambdaMemoryLimitInMB', 'LambdaPreviousExecutionTimeInMilliseconds', 'LambdaRemainingTimeInMilliseconds', 'LambdaTimeGapBetweenInvokesInMilliseconds']
MetricTypeType = Literal['AggregatedRelativeTotalTime']
OrderByType = Literal['TimestampAscending', 'TimestampDescending']
PaginatorName = Literal['list_profile_times']
ResourceServiceName = Literal['cloudformation', 'cloudwatch', 'dynamodb', 'ec2', 'glacier', 'iam', 'opsworks', 's3', 'sns', 'sqs']
