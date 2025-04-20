# Sagemaker Sagemaker Classes

# ActionSource

### SourceUri
- **Type**: <class 'str'>
- **Required**: Yes

### SourceType
- **Type**: typing.Optional[str]

### SourceId
- **Type**: typing.Optional[str]


# ActionSummary

### ActionArn
- **Type**: typing.Optional[str]

### ActionName
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ActionSource]

### ActionType
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping', 'Unknown']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# AddAssociationRequest

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationArn
- **Type**: <class 'str'>
- **Required**: Yes

### AssociationType
- **Type**: typing.Optional[typing.Literal['AssociatedWith', 'ContributedTo', 'DerivedFrom', 'Produced', 'SameAs']]


# AddAssociationResponse

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# AddTagsInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]
- **Required**: Yes


# AddTagsOutput

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# AdditionalInferenceSpecificationDefinition

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Containers
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelPackageContainerDefinition, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelPackageContainerDefinitionOutput]]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### SupportedTransformInstanceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge']]]

### SupportedRealtimeInferenceInstanceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.large', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c5d.18xlarge', 'ml.c5d.2xlarge', 'ml.c5d.4xlarge', 'ml.c5d.9xlarge', 'ml.c5d.large', 'ml.c5d.xlarge', 'ml.c6g.12xlarge', 'ml.c6g.16xlarge', 'ml.c6g.2xlarge', 'ml.c6g.4xlarge', 'ml.c6g.8xlarge', 'ml.c6g.large', 'ml.c6g.xlarge', 'ml.c6gd.12xlarge', 'ml.c6gd.16xlarge', 'ml.c6gd.2xlarge', 'ml.c6gd.4xlarge', 'ml.c6gd.8xlarge', 'ml.c6gd.large', 'ml.c6gd.xlarge', 'ml.c6gn.12xlarge', 'ml.c6gn.16xlarge', 'ml.c6gn.2xlarge', 'ml.c6gn.4xlarge', 'ml.c6gn.8xlarge', 'ml.c6gn.large', 'ml.c6gn.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c7g.12xlarge', 'ml.c7g.16xlarge', 'ml.c7g.2xlarge', 'ml.c7g.4xlarge', 'ml.c7g.8xlarge', 'ml.c7g.large', 'ml.c7g.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.dl1.24xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.inf1.24xlarge', 'ml.inf1.2xlarge', 'ml.inf1.6xlarge', 'ml.inf1.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6g.12xlarge', 'ml.m6g.16xlarge', 'ml.m6g.2xlarge', 'ml.m6g.4xlarge', 'ml.m6g.8xlarge', 'ml.m6g.large', 'ml.m6g.xlarge', 'ml.m6gd.12xlarge', 'ml.m6gd.16xlarge', 'ml.m6gd.2xlarge', 'ml.m6gd.4xlarge', 'ml.m6gd.8xlarge', 'ml.m6gd.large', 'ml.m6gd.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.r6g.12xlarge', 'ml.r6g.16xlarge', 'ml.r6g.2xlarge', 'ml.r6g.4xlarge', 'ml.r6g.8xlarge', 'ml.r6g.large', 'ml.r6g.xlarge', 'ml.r6gd.12xlarge', 'ml.r6gd.16xlarge', 'ml.r6gd.2xlarge', 'ml.r6gd.4xlarge', 'ml.r6gd.8xlarge', 'ml.r6gd.large', 'ml.r6gd.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.r8g.12xlarge', 'ml.r8g.16xlarge', 'ml.r8g.24xlarge', 'ml.r8g.2xlarge', 'ml.r8g.48xlarge', 'ml.r8g.4xlarge', 'ml.r8g.8xlarge', 'ml.r8g.large', 'ml.r8g.medium', 'ml.r8g.xlarge', 'ml.t2.2xlarge', 'ml.t2.large', 'ml.t2.medium', 'ml.t2.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]]

### SupportedContentTypes
- **Type**: typing.Optional[typing.List[str]]

### SupportedResponseMIMETypes
- **Type**: typing.Optional[typing.List[str]]


# AdditionalInferenceSpecificationDefinitionOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Containers
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelPackageContainerDefinitionOutput]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### SupportedTransformInstanceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge']]]

### SupportedRealtimeInferenceInstanceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.large', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c5d.18xlarge', 'ml.c5d.2xlarge', 'ml.c5d.4xlarge', 'ml.c5d.9xlarge', 'ml.c5d.large', 'ml.c5d.xlarge', 'ml.c6g.12xlarge', 'ml.c6g.16xlarge', 'ml.c6g.2xlarge', 'ml.c6g.4xlarge', 'ml.c6g.8xlarge', 'ml.c6g.large', 'ml.c6g.xlarge', 'ml.c6gd.12xlarge', 'ml.c6gd.16xlarge', 'ml.c6gd.2xlarge', 'ml.c6gd.4xlarge', 'ml.c6gd.8xlarge', 'ml.c6gd.large', 'ml.c6gd.xlarge', 'ml.c6gn.12xlarge', 'ml.c6gn.16xlarge', 'ml.c6gn.2xlarge', 'ml.c6gn.4xlarge', 'ml.c6gn.8xlarge', 'ml.c6gn.large', 'ml.c6gn.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c7g.12xlarge', 'ml.c7g.16xlarge', 'ml.c7g.2xlarge', 'ml.c7g.4xlarge', 'ml.c7g.8xlarge', 'ml.c7g.large', 'ml.c7g.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.dl1.24xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.inf1.24xlarge', 'ml.inf1.2xlarge', 'ml.inf1.6xlarge', 'ml.inf1.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6g.12xlarge', 'ml.m6g.16xlarge', 'ml.m6g.2xlarge', 'ml.m6g.4xlarge', 'ml.m6g.8xlarge', 'ml.m6g.large', 'ml.m6g.xlarge', 'ml.m6gd.12xlarge', 'ml.m6gd.16xlarge', 'ml.m6gd.2xlarge', 'ml.m6gd.4xlarge', 'ml.m6gd.8xlarge', 'ml.m6gd.large', 'ml.m6gd.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.r6g.12xlarge', 'ml.r6g.16xlarge', 'ml.r6g.2xlarge', 'ml.r6g.4xlarge', 'ml.r6g.8xlarge', 'ml.r6g.large', 'ml.r6g.xlarge', 'ml.r6gd.12xlarge', 'ml.r6gd.16xlarge', 'ml.r6gd.2xlarge', 'ml.r6gd.4xlarge', 'ml.r6gd.8xlarge', 'ml.r6gd.large', 'ml.r6gd.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.r8g.12xlarge', 'ml.r8g.16xlarge', 'ml.r8g.24xlarge', 'ml.r8g.2xlarge', 'ml.r8g.48xlarge', 'ml.r8g.4xlarge', 'ml.r8g.8xlarge', 'ml.r8g.large', 'ml.r8g.medium', 'ml.r8g.xlarge', 'ml.t2.2xlarge', 'ml.t2.large', 'ml.t2.medium', 'ml.t2.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]]

### SupportedContentTypes
- **Type**: typing.Optional[typing.List[str]]

### SupportedResponseMIMETypes
- **Type**: typing.Optional[typing.List[str]]


# AdditionalModelDataSource

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### S3DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.S3ModelDataSource'>
- **Required**: Yes


# AdditionalS3DataSource

### S3DataType
- **Type**: typing.Literal['S3Object', 'S3Prefix']
- **Required**: Yes

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### CompressionType
- **Type**: typing.Optional[typing.Literal['Gzip', 'None']]

### ETag
- **Type**: typing.Optional[str]


# AgentVersion

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### AgentCount
- **Type**: <class 'int'>
- **Required**: Yes


# Alarm

### AlarmName
- **Type**: typing.Optional[str]


# AlgorithmSpecification

### TrainingInputMode
- **Type**: typing.Literal['FastFile', 'File', 'Pipe']
- **Required**: Yes

### TrainingImage
- **Type**: typing.Optional[str]

### AlgorithmName
- **Type**: typing.Optional[str]

### MetricDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MetricDefinition]]

### EnableSageMakerMetricsTimeSeries
- **Type**: typing.Optional[bool]

### ContainerEntrypoint
- **Type**: typing.Optional[typing.List[str]]

### ContainerArguments
- **Type**: typing.Optional[typing.List[str]]

### TrainingImageConfig
- **Type**: <class 'NoneType'>


# AlgorithmSpecificationOutput

### TrainingInputMode
- **Type**: typing.Literal['FastFile', 'File', 'Pipe']
- **Required**: Yes

### TrainingImage
- **Type**: typing.Optional[str]

### AlgorithmName
- **Type**: typing.Optional[str]

### MetricDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MetricDefinition]]

### EnableSageMakerMetricsTimeSeries
- **Type**: typing.Optional[bool]

### ContainerEntrypoint
- **Type**: typing.Optional[typing.List[str]]

### ContainerArguments
- **Type**: typing.Optional[typing.List[str]]

### TrainingImageConfig
- **Type**: <class 'NoneType'>


# AlgorithmStatusDetails

### ValidationStatuses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AlgorithmStatusItem]]

### ImageScanStatuses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AlgorithmStatusItem]]


# AlgorithmStatusItem

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'NotStarted']
- **Required**: Yes

### FailureReason
- **Type**: typing.Optional[str]


# AlgorithmSummary

### AlgorithmName
- **Type**: <class 'str'>
- **Required**: Yes

### AlgorithmArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AlgorithmStatus
- **Type**: typing.Literal['Completed', 'Deleting', 'Failed', 'InProgress', 'Pending']
- **Required**: Yes

### AlgorithmDescription
- **Type**: typing.Optional[str]


# AlgorithmValidationProfile

### ProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### TrainingJobDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrainingJobDefinition'>
- **Required**: Yes

### TransformJobDefinition
- **Type**: <class 'NoneType'>


# AlgorithmValidationProfileOutput

### ProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### TrainingJobDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrainingJobDefinitionOutput'>
- **Required**: Yes

### TransformJobDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TransformJobDefinitionOutput]


# AlgorithmValidationSpecification

### ValidationRole
- **Type**: <class 'str'>
- **Required**: Yes

### ValidationProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AlgorithmValidationProfile]
- **Required**: Yes


# AlgorithmValidationSpecificationOutput

### ValidationRole
- **Type**: <class 'str'>
- **Required**: Yes

### ValidationProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AlgorithmValidationProfileOutput]
- **Required**: Yes


# AmazonQSettings

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### QProfileArn
- **Type**: typing.Optional[str]


# AnnotationConsolidationConfig

### AnnotationConsolidationLambdaArn
- **Type**: <class 'str'>
- **Required**: Yes


# AppDetails

### DomainId
- **Type**: typing.Optional[str]

### UserProfileName
- **Type**: typing.Optional[str]

### SpaceName
- **Type**: typing.Optional[str]

### AppType
- **Type**: typing.Optional[typing.Literal['Canvas', 'CodeEditor', 'DetailedProfiler', 'JupyterLab', 'JupyterServer', 'KernelGateway', 'RSessionGateway', 'RStudioServerPro', 'TensorBoard']]

### AppName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Deleted', 'Deleting', 'Failed', 'InService', 'Pending']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### ResourceSpec
- **Type**: <class 'NoneType'>


# AppImageConfigDetails

### AppImageConfigArn
- **Type**: typing.Optional[str]

### AppImageConfigName
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### KernelGatewayImageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.KernelGatewayImageConfigOutput]

### JupyterLabAppImageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.JupyterLabAppImageConfigOutput]

### CodeEditorAppImageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CodeEditorAppImageConfigOutput]


# AppLifecycleManagement

### IdleSettings
- **Type**: <class 'NoneType'>


# AppSpecification

### ImageUri
- **Type**: <class 'str'>
- **Required**: Yes

### ContainerEntrypoint
- **Type**: typing.Optional[typing.List[str]]

### ContainerArguments
- **Type**: typing.Optional[typing.List[str]]


# AppSpecificationOutput

### ImageUri
- **Type**: <class 'str'>
- **Required**: Yes

### ContainerEntrypoint
- **Type**: typing.Optional[typing.List[str]]

### ContainerArguments
- **Type**: typing.Optional[typing.List[str]]


# ArtifactSource

### SourceUri
- **Type**: <class 'str'>
- **Required**: Yes

### SourceTypes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ArtifactSourceType]]


# ArtifactSourceOutput

### SourceUri
- **Type**: <class 'str'>
- **Required**: Yes

### SourceTypes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ArtifactSourceType]]


# ArtifactSourceType

### SourceIdType
- **Type**: typing.Literal['Custom', 'MD5Hash', 'S3ETag', 'S3Version']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ArtifactSummary

### ArtifactArn
- **Type**: typing.Optional[str]

### ArtifactName
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ArtifactSourceOutput]

### ArtifactType
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# AssociateTrialComponentRequest

### TrialComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### TrialName
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateTrialComponentResponse

### TrialComponentArn
- **Type**: <class 'str'>
- **Required**: Yes

### TrialArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# AssociationSummary

### SourceArn
- **Type**: typing.Optional[str]

### DestinationArn
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[str]

### DestinationType
- **Type**: typing.Optional[str]

### AssociationType
- **Type**: typing.Optional[typing.Literal['AssociatedWith', 'ContributedTo', 'DerivedFrom', 'Produced', 'SameAs']]

### SourceName
- **Type**: typing.Optional[str]

### DestinationName
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext]


# AsyncInferenceClientConfig

### MaxConcurrentInvocationsPerInstance
- **Type**: typing.Optional[int]


# AsyncInferenceConfig

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AsyncInferenceOutputConfig'>
- **Required**: Yes

### ClientConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AsyncInferenceClientConfig]


# AsyncInferenceConfigOutput

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AsyncInferenceOutputConfigOutput'>
- **Required**: Yes

### ClientConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AsyncInferenceClientConfig]


# AsyncInferenceNotificationConfig

### SuccessTopic
- **Type**: typing.Optional[str]

### ErrorTopic
- **Type**: typing.Optional[str]

### IncludeInferenceResponseIn
- **Type**: typing.Optional[typing.List[typing.Literal['ERROR_NOTIFICATION_TOPIC', 'SUCCESS_NOTIFICATION_TOPIC']]]


# AsyncInferenceNotificationConfigOutput

### SuccessTopic
- **Type**: typing.Optional[str]

### ErrorTopic
- **Type**: typing.Optional[str]

### IncludeInferenceResponseIn
- **Type**: typing.Optional[typing.List[typing.Literal['ERROR_NOTIFICATION_TOPIC', 'SUCCESS_NOTIFICATION_TOPIC']]]


# AsyncInferenceOutputConfig

### KmsKeyId
- **Type**: typing.Optional[str]

### S3OutputPath
- **Type**: typing.Optional[str]

### NotificationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AsyncInferenceNotificationConfig]

### S3FailurePath
- **Type**: typing.Optional[str]


# AsyncInferenceOutputConfigOutput

### KmsKeyId
- **Type**: typing.Optional[str]

### S3OutputPath
- **Type**: typing.Optional[str]

### NotificationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AsyncInferenceNotificationConfigOutput]

### S3FailurePath
- **Type**: typing.Optional[str]


# AthenaDatasetDefinition

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### QueryString
- **Type**: <class 'str'>
- **Required**: Yes

### OutputS3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### OutputFormat
- **Type**: typing.Literal['AVRO', 'JSON', 'ORC', 'PARQUET', 'TEXTFILE']
- **Required**: Yes

### WorkGroup
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### OutputCompression
- **Type**: typing.Optional[typing.Literal['GZIP', 'SNAPPY', 'ZLIB']]


# AutoMLAlgorithmConfig

### AutoMLAlgorithms
- **Type**: typing.List[typing.Literal['arima', 'catboost', 'cnn-qr', 'deepar', 'ets', 'extra-trees', 'fastai', 'lightgbm', 'linear-learner', 'mlp', 'nn-torch', 'npts', 'prophet', 'randomforest', 'xgboost']]
- **Required**: Yes


# AutoMLAlgorithmConfigOutput

### AutoMLAlgorithms
- **Type**: typing.List[typing.Literal['arima', 'catboost', 'cnn-qr', 'deepar', 'ets', 'extra-trees', 'fastai', 'lightgbm', 'linear-learner', 'mlp', 'nn-torch', 'npts', 'prophet', 'randomforest', 'xgboost']]
- **Required**: Yes


# AutoMLCandidate

### CandidateName
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectiveStatus
- **Type**: typing.Literal['Failed', 'Pending', 'Succeeded']
- **Required**: Yes

### CandidateSteps
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLCandidateStep]
- **Required**: Yes

### CandidateStatus
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FinalAutoMLJobObjectiveMetric
- **Type**: <class 'NoneType'>

### InferenceContainers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLContainerDefinition]]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### FailureReason
- **Type**: typing.Optional[str]

### CandidateProperties
- **Type**: <class 'NoneType'>

### InferenceContainerDefinitions
- **Type**: typing.Optional[typing.Dict[typing.Literal['CPU', 'GPU'], typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLContainerDefinition]]]


# AutoMLCandidateGenerationConfig

### FeatureSpecificationS3Uri
- **Type**: typing.Optional[str]

### AlgorithmsConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLAlgorithmConfig]]


# AutoMLCandidateGenerationConfigOutput

### FeatureSpecificationS3Uri
- **Type**: typing.Optional[str]

### AlgorithmsConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLAlgorithmConfigOutput]]


# AutoMLCandidateStep

### CandidateStepType
- **Type**: typing.Literal['AWS::SageMaker::ProcessingJob', 'AWS::SageMaker::TrainingJob', 'AWS::SageMaker::TransformJob']
- **Required**: Yes

### CandidateStepArn
- **Type**: <class 'str'>
- **Required**: Yes

### CandidateStepName
- **Type**: <class 'str'>
- **Required**: Yes


# AutoMLChannel

### TargetAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLDataSource]

### CompressionType
- **Type**: typing.Optional[typing.Literal['Gzip', 'None']]

### ContentType
- **Type**: typing.Optional[str]

### ChannelType
- **Type**: typing.Optional[typing.Literal['training', 'validation']]

### SampleWeightAttributeName
- **Type**: typing.Optional[str]


# AutoMLComputeConfig

### EmrServerlessComputeConfig
- **Type**: <class 'NoneType'>


# AutoMLContainerDefinition

### Image
- **Type**: <class 'str'>
- **Required**: Yes

### ModelDataUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]


# AutoMLDataSource

### S3DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLS3DataSource'>
- **Required**: Yes


# AutoMLDataSplitConfig

### ValidationFraction
- **Type**: typing.Optional[float]


# AutoMLJobArtifacts

### CandidateDefinitionNotebookLocation
- **Type**: typing.Optional[str]

### DataExplorationNotebookLocation
- **Type**: typing.Optional[str]


# AutoMLJobChannel

### ChannelType
- **Type**: typing.Optional[typing.Literal['training', 'validation']]

### ContentType
- **Type**: typing.Optional[str]

### CompressionType
- **Type**: typing.Optional[typing.Literal['Gzip', 'None']]

### DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLDataSource]


# AutoMLJobCompletionCriteria

### MaxCandidates
- **Type**: typing.Optional[int]

### MaxRuntimePerTrainingJobInSeconds
- **Type**: typing.Optional[int]

### MaxAutoMLJobRuntimeInSeconds
- **Type**: typing.Optional[int]


# AutoMLJobConfig

### CompletionCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLJobCompletionCriteria]

### SecurityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLSecurityConfig]

### CandidateGenerationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLCandidateGenerationConfig]

### DataSplitConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLDataSplitConfig]

### Mode
- **Type**: typing.Optional[typing.Literal['AUTO', 'ENSEMBLING', 'HYPERPARAMETER_TUNING']]


# AutoMLJobConfigOutput

### CompletionCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLJobCompletionCriteria]

### SecurityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLSecurityConfigOutput]

### CandidateGenerationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLCandidateGenerationConfigOutput]

### DataSplitConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLDataSplitConfig]

### Mode
- **Type**: typing.Optional[typing.Literal['AUTO', 'ENSEMBLING', 'HYPERPARAMETER_TUNING']]


# AutoMLJobObjective

### MetricName
- **Type**: typing.Literal['AUC', 'Accuracy', 'AverageWeightedQuantileLoss', 'BalancedAccuracy', 'F1', 'F1macro', 'MAE', 'MAPE', 'MASE', 'MSE', 'Precision', 'PrecisionMacro', 'R2', 'RMSE', 'Recall', 'RecallMacro', 'WAPE']
- **Required**: Yes


# AutoMLJobStepMetadata

### Arn
- **Type**: typing.Optional[str]


# AutoMLJobSummary

### AutoMLJobName
- **Type**: <class 'str'>
- **Required**: Yes

### AutoMLJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### AutoMLJobStatus
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']
- **Required**: Yes

### AutoMLJobSecondaryStatus
- **Type**: typing.Literal['AnalyzingData', 'CandidateDefinitionsGenerated', 'Completed', 'DeployingModel', 'ExplainabilityError', 'Failed', 'FeatureEngineering', 'GeneratingExplainabilityReport', 'GeneratingModelInsightsReport', 'MaxAutoMLJobRuntimeReached', 'MaxCandidatesReached', 'ModelDeploymentError', 'ModelInsightsError', 'ModelTuning', 'PreTraining', 'Starting', 'Stopped', 'Stopping', 'TrainingModels']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### FailureReason
- **Type**: typing.Optional[str]

### PartialFailureReasons
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLPartialFailureReason]]


# AutoMLOutputDataConfig

### S3OutputPath
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# AutoMLPartialFailureReason

### PartialFailureMessage
- **Type**: typing.Optional[str]


# AutoMLProblemTypeConfig

### ImageClassificationJobConfig
- **Type**: <class 'NoneType'>

### TextClassificationJobConfig
- **Type**: <class 'NoneType'>

### TimeSeriesForecastingJobConfig
- **Type**: <class 'NoneType'>

### TabularJobConfig
- **Type**: <class 'NoneType'>

### TextGenerationJobConfig
- **Type**: <class 'NoneType'>


# AutoMLProblemTypeConfigOutput

### ImageClassificationJobConfig
- **Type**: <class 'NoneType'>

### TextClassificationJobConfig
- **Type**: <class 'NoneType'>

### TimeSeriesForecastingJobConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TimeSeriesForecastingJobConfigOutput]

### TabularJobConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TabularJobConfigOutput]

### TextGenerationJobConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TextGenerationJobConfigOutput]


# AutoMLProblemTypeResolvedAttributes

### TabularResolvedAttributes
- **Type**: <class 'NoneType'>

### TextGenerationResolvedAttributes
- **Type**: <class 'NoneType'>


# AutoMLResolvedAttributes

### AutoMLJobObjective
- **Type**: <class 'NoneType'>

### CompletionCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLJobCompletionCriteria]

### AutoMLProblemTypeResolvedAttributes
- **Type**: <class 'NoneType'>


# AutoMLS3DataSource

### S3DataType
- **Type**: typing.Literal['AugmentedManifestFile', 'ManifestFile', 'S3Prefix']
- **Required**: Yes

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes


# AutoMLSecurityConfig

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### EnableInterContainerTrafficEncryption
- **Type**: typing.Optional[bool]

### VpcConfig
- **Type**: <class 'NoneType'>


# AutoMLSecurityConfigOutput

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### EnableInterContainerTrafficEncryption
- **Type**: typing.Optional[bool]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.VpcConfigOutput]


# AutoParameter

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ValueHint
- **Type**: <class 'str'>
- **Required**: Yes


# AutoRollbackConfig

### Alarms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Alarm]]


# AutoRollbackConfigOutput

### Alarms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Alarm]]


# Autotune

### Mode
- **Type**: typing.Literal['Enabled']
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDataCaptureConfig

### DestinationS3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]

### GenerateInferenceId
- **Type**: typing.Optional[bool]


# BatchDeleteClusterNodesError

### Code
- **Type**: typing.Literal['InvalidNodeStatus', 'NodeIdInUse', 'NodeIdNotFound']
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### NodeId
- **Type**: <class 'str'>
- **Required**: Yes


# BatchDeleteClusterNodesRequest

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### NodeIds
- **Type**: typing.List[str]
- **Required**: Yes


# BatchDeleteClusterNodesResponse

### Failed
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.BatchDeleteClusterNodesError]
- **Required**: Yes

### Successful
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDescribeModelPackageError

### ErrorCode
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorResponse
- **Type**: <class 'str'>
- **Required**: Yes


# BatchDescribeModelPackageInput

### ModelPackageArnList
- **Type**: typing.List[str]
- **Required**: Yes


# BatchDescribeModelPackageOutput

### ModelPackageSummaries
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.BatchDescribeModelPackageSummary]
- **Required**: Yes

### BatchDescribeModelPackageErrorMap
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.BatchDescribeModelPackageError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDescribeModelPackageSummary

### ModelPackageGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelPackageArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### InferenceSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceSpecificationOutput'>
- **Required**: Yes

### ModelPackageStatus
- **Type**: typing.Literal['Completed', 'Deleting', 'Failed', 'InProgress', 'Pending']
- **Required**: Yes

### ModelPackageVersion
- **Type**: typing.Optional[int]

### ModelPackageDescription
- **Type**: typing.Optional[str]

### ModelApprovalStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'PendingManualApproval', 'Rejected']]


# BatchTransformInput

### DataCapturedDestinationS3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetFormat
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringDatasetFormat'>
- **Required**: Yes

### LocalPath
- **Type**: <class 'str'>
- **Required**: Yes

### S3InputMode
- **Type**: typing.Optional[typing.Literal['File', 'Pipe']]

### S3DataDistributionType
- **Type**: typing.Optional[typing.Literal['FullyReplicated', 'ShardedByS3Key']]

### FeaturesAttribute
- **Type**: typing.Optional[str]

### InferenceAttribute
- **Type**: typing.Optional[str]

### ProbabilityAttribute
- **Type**: typing.Optional[str]

### ProbabilityThresholdAttribute
- **Type**: typing.Optional[float]

### StartTimeOffset
- **Type**: typing.Optional[str]

### EndTimeOffset
- **Type**: typing.Optional[str]

### ExcludeFeaturesAttribute
- **Type**: typing.Optional[str]


# BatchTransformInputOutput

### DataCapturedDestinationS3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetFormat
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringDatasetFormatOutput'>
- **Required**: Yes

### LocalPath
- **Type**: <class 'str'>
- **Required**: Yes

### S3InputMode
- **Type**: typing.Optional[typing.Literal['File', 'Pipe']]

### S3DataDistributionType
- **Type**: typing.Optional[typing.Literal['FullyReplicated', 'ShardedByS3Key']]

### FeaturesAttribute
- **Type**: typing.Optional[str]

### InferenceAttribute
- **Type**: typing.Optional[str]

### ProbabilityAttribute
- **Type**: typing.Optional[str]

### ProbabilityThresholdAttribute
- **Type**: typing.Optional[float]

### StartTimeOffset
- **Type**: typing.Optional[str]

### EndTimeOffset
- **Type**: typing.Optional[str]

### ExcludeFeaturesAttribute
- **Type**: typing.Optional[str]


# BestObjectiveNotImproving

### MaxNumberOfTrainingJobsNotImproving
- **Type**: typing.Optional[int]


# Bias

### Report
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MetricsSource]

### PreTrainingReport
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MetricsSource]

### PostTrainingReport
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MetricsSource]


# BlueGreenUpdatePolicy

### TrafficRoutingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrafficRoutingConfig'>
- **Required**: Yes

### TerminationWaitInSeconds
- **Type**: typing.Optional[int]

### MaximumExecutionTimeoutInSeconds
- **Type**: typing.Optional[int]


# CacheHitResult

### SourcePipelineExecutionArn
- **Type**: typing.Optional[str]


# CallbackStepMetadata

### CallbackToken
- **Type**: typing.Optional[str]

### SqsQueueUrl
- **Type**: typing.Optional[str]

### OutputParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OutputParameter]]


# CandidateArtifactLocations

### Explainability
- **Type**: <class 'str'>
- **Required**: Yes

### ModelInsights
- **Type**: typing.Optional[str]

### BacktestResults
- **Type**: typing.Optional[str]


# CandidateGenerationConfig

### AlgorithmsConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLAlgorithmConfig]]


# CandidateGenerationConfigOutput

### AlgorithmsConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLAlgorithmConfigOutput]]


# CandidateProperties

### CandidateArtifactLocations
- **Type**: <class 'NoneType'>

### CandidateMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MetricDatum]]


# CanvasAppSettings

### TimeSeriesForecastingSettings
- **Type**: <class 'NoneType'>

### ModelRegisterSettings
- **Type**: <class 'NoneType'>

### WorkspaceSettings
- **Type**: <class 'NoneType'>

### IdentityProviderOAuthSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.IdentityProviderOAuthSetting]]

### DirectDeploySettings
- **Type**: <class 'NoneType'>

### KendraSettings
- **Type**: <class 'NoneType'>

### GenerativeAiSettings
- **Type**: <class 'NoneType'>

### EmrServerlessSettings
- **Type**: <class 'NoneType'>


# CanvasAppSettingsOutput

### TimeSeriesForecastingSettings
- **Type**: <class 'NoneType'>

### ModelRegisterSettings
- **Type**: <class 'NoneType'>

### WorkspaceSettings
- **Type**: <class 'NoneType'>

### IdentityProviderOAuthSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.IdentityProviderOAuthSetting]]

### DirectDeploySettings
- **Type**: <class 'NoneType'>

### KendraSettings
- **Type**: <class 'NoneType'>

### GenerativeAiSettings
- **Type**: <class 'NoneType'>

### EmrServerlessSettings
- **Type**: <class 'NoneType'>


# CapacitySize

### Type
- **Type**: typing.Literal['CAPACITY_PERCENT', 'INSTANCE_COUNT']
- **Required**: Yes

### Value
- **Type**: <class 'int'>
- **Required**: Yes


# CaptureContentTypeHeader

### CsvContentTypes
- **Type**: typing.Optional[typing.List[str]]

### JsonContentTypes
- **Type**: typing.Optional[typing.List[str]]


# CaptureContentTypeHeaderOutput

### CsvContentTypes
- **Type**: typing.Optional[typing.List[str]]

### JsonContentTypes
- **Type**: typing.Optional[typing.List[str]]


# CaptureOption

### CaptureMode
- **Type**: typing.Literal['Input', 'InputAndOutput', 'Output']
- **Required**: Yes


# CategoricalParameter

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.List[str]
- **Required**: Yes


# CategoricalParameterOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.List[str]
- **Required**: Yes


# CategoricalParameterRange

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# CategoricalParameterRangeOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# CategoricalParameterRangeSpecification

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# CategoricalParameterRangeSpecificationOutput

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# Channel

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### DataSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DataSource, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DataSourceOutput]
- **Required**: Yes

### ContentType
- **Type**: typing.Optional[str]

### CompressionType
- **Type**: typing.Optional[typing.Literal['Gzip', 'None']]

### RecordWrapperType
- **Type**: <class 'NoneType'>

### InputMode
- **Type**: typing.Optional[typing.Literal['FastFile', 'File', 'Pipe']]

### ShuffleConfig
- **Type**: <class 'NoneType'>


# ChannelOutput

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DataSourceOutput'>
- **Required**: Yes

### ContentType
- **Type**: typing.Optional[str]

### CompressionType
- **Type**: typing.Optional[typing.Literal['Gzip', 'None']]

### RecordWrapperType
- **Type**: <class 'NoneType'>

### InputMode
- **Type**: typing.Optional[typing.Literal['FastFile', 'File', 'Pipe']]

### ShuffleConfig
- **Type**: <class 'NoneType'>


# ChannelSpecification

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SupportedContentTypes
- **Type**: typing.List[str]
- **Required**: Yes

### SupportedInputModes
- **Type**: typing.List[typing.Literal['FastFile', 'File', 'Pipe']]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### IsRequired
- **Type**: typing.Optional[bool]

### SupportedCompressionTypes
- **Type**: typing.Optional[typing.List[typing.Literal['Gzip', 'None']]]


# ChannelSpecificationOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SupportedContentTypes
- **Type**: typing.List[str]
- **Required**: Yes

### SupportedInputModes
- **Type**: typing.List[typing.Literal['FastFile', 'File', 'Pipe']]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### IsRequired
- **Type**: typing.Optional[bool]

### SupportedCompressionTypes
- **Type**: typing.Optional[typing.List[typing.Literal['Gzip', 'None']]]


# CheckpointConfig

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### LocalPath
- **Type**: typing.Optional[str]


# ClarifyCheckStepMetadata

### CheckType
- **Type**: typing.Optional[str]

### BaselineUsedForDriftCheckConstraints
- **Type**: typing.Optional[str]

### CalculatedBaselineConstraints
- **Type**: typing.Optional[str]

### ModelPackageGroupName
- **Type**: typing.Optional[str]

### ViolationReport
- **Type**: typing.Optional[str]

### CheckJobArn
- **Type**: typing.Optional[str]

### SkipCheck
- **Type**: typing.Optional[bool]

### RegisterNewBaseline
- **Type**: typing.Optional[bool]


# ClarifyExplainerConfig

### ShapConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ClarifyShapConfig'>
- **Required**: Yes

### EnableExplanations
- **Type**: typing.Optional[str]

### InferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ClarifyInferenceConfig]


# ClarifyExplainerConfigOutput

### ShapConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ClarifyShapConfig'>
- **Required**: Yes

### EnableExplanations
- **Type**: typing.Optional[str]

### InferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ClarifyInferenceConfigOutput]


# ClarifyInferenceConfig

### FeaturesAttribute
- **Type**: typing.Optional[str]

### ContentTemplate
- **Type**: typing.Optional[str]

### MaxRecordCount
- **Type**: typing.Optional[int]

### MaxPayloadInMB
- **Type**: typing.Optional[int]

### ProbabilityIndex
- **Type**: typing.Optional[int]

### LabelIndex
- **Type**: typing.Optional[int]

### ProbabilityAttribute
- **Type**: typing.Optional[str]

### LabelAttribute
- **Type**: typing.Optional[str]

### LabelHeaders
- **Type**: typing.Optional[typing.List[str]]

### FeatureHeaders
- **Type**: typing.Optional[typing.List[str]]

### FeatureTypes
- **Type**: typing.Optional[typing.List[typing.Literal['categorical', 'numerical', 'text']]]


# ClarifyInferenceConfigOutput

### FeaturesAttribute
- **Type**: typing.Optional[str]

### ContentTemplate
- **Type**: typing.Optional[str]

### MaxRecordCount
- **Type**: typing.Optional[int]

### MaxPayloadInMB
- **Type**: typing.Optional[int]

### ProbabilityIndex
- **Type**: typing.Optional[int]

### LabelIndex
- **Type**: typing.Optional[int]

### ProbabilityAttribute
- **Type**: typing.Optional[str]

### LabelAttribute
- **Type**: typing.Optional[str]

### LabelHeaders
- **Type**: typing.Optional[typing.List[str]]

### FeatureHeaders
- **Type**: typing.Optional[typing.List[str]]

### FeatureTypes
- **Type**: typing.Optional[typing.List[typing.Literal['categorical', 'numerical', 'text']]]


# ClarifyShapBaselineConfig

### MimeType
- **Type**: typing.Optional[str]

### ShapBaseline
- **Type**: typing.Optional[str]

### ShapBaselineUri
- **Type**: typing.Optional[str]


# ClarifyShapConfig

### ShapBaselineConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ClarifyShapBaselineConfig'>
- **Required**: Yes

### NumberOfSamples
- **Type**: typing.Optional[int]

### UseLogit
- **Type**: typing.Optional[bool]

### Seed
- **Type**: typing.Optional[int]

### TextConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ClarifyTextConfig]


# ClarifyTextConfig

### Language
- **Type**: typing.Literal['af', 'ar', 'bg', 'bn', 'ca', 'cs', 'da', 'de', 'el', 'en', 'es', 'et', 'eu', 'fa', 'fi', 'fr', 'ga', 'gu', 'he', 'hi', 'hr', 'hu', 'hy', 'id', 'is', 'it', 'kn', 'ky', 'lb', 'lij', 'lt', 'lv', 'mk', 'ml', 'mr', 'nb', 'ne', 'nl', 'pl', 'pt', 'ro', 'ru', 'sa', 'si', 'sk', 'sl', 'sq', 'sr', 'sv', 'ta', 'te', 'tl', 'tn', 'tr', 'tt', 'uk', 'ur', 'xx', 'yo', 'zh']
- **Required**: Yes

### Granularity
- **Type**: typing.Literal['paragraph', 'sentence', 'token']
- **Required**: Yes


# ClusterEbsVolumeConfig

### VolumeSizeInGB
- **Type**: <class 'int'>
- **Required**: Yes


# ClusterInstanceGroupDetails

### CurrentCount
- **Type**: typing.Optional[int]

### TargetCount
- **Type**: typing.Optional[int]

### InstanceGroupName
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c5.12xlarge', 'ml.c5.18xlarge', 'ml.c5.24xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c5n.18xlarge', 'ml.c5n.2xlarge', 'ml.c5n.4xlarge', 'ml.c5n.9xlarge', 'ml.c5n.large', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.gr6.4xlarge', 'ml.gr6.8xlarge', 'ml.m5.12xlarge', 'ml.m5.16xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.8xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]

### LifeCycleConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ClusterLifeCycleConfig]

### ExecutionRole
- **Type**: typing.Optional[str]

### ThreadsPerCore
- **Type**: typing.Optional[int]

### InstanceStorageConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ClusterInstanceStorageConfig]]

### OnStartDeepHealthChecks
- **Type**: typing.Optional[typing.List[typing.Literal['InstanceConnectivity', 'InstanceStress']]]

### Status
- **Type**: typing.Optional[typing.Literal['Creating', 'Degraded', 'Deleting', 'Failed', 'InService', 'SystemUpdating', 'Updating']]

### TrainingPlanArn
- **Type**: typing.Optional[str]

### TrainingPlanStatus
- **Type**: typing.Optional[str]

### OverrideVpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.VpcConfigOutput]


# ClusterInstanceGroupSpecification

### InstanceCount
- **Type**: <class 'int'>
- **Required**: Yes

### InstanceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceType
- **Type**: typing.Literal['ml.c5.12xlarge', 'ml.c5.18xlarge', 'ml.c5.24xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c5n.18xlarge', 'ml.c5n.2xlarge', 'ml.c5n.4xlarge', 'ml.c5n.9xlarge', 'ml.c5n.large', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.gr6.4xlarge', 'ml.gr6.8xlarge', 'ml.m5.12xlarge', 'ml.m5.16xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.8xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']
- **Required**: Yes

### LifeCycleConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ClusterLifeCycleConfig'>
- **Required**: Yes

### ExecutionRole
- **Type**: <class 'str'>
- **Required**: Yes

### ThreadsPerCore
- **Type**: typing.Optional[int]

### InstanceStorageConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ClusterInstanceStorageConfig]]

### OnStartDeepHealthChecks
- **Type**: typing.Optional[typing.List[typing.Literal['InstanceConnectivity', 'InstanceStress']]]

### TrainingPlanArn
- **Type**: typing.Optional[str]

### OverrideVpcConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.VpcConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.VpcConfigOutput, NoneType]


# ClusterInstancePlacement

### AvailabilityZone
- **Type**: typing.Optional[str]

### AvailabilityZoneId
- **Type**: typing.Optional[str]


# ClusterInstanceStatusDetails

### Status
- **Type**: typing.Literal['DeepHealthCheckInProgress', 'Failure', 'Pending', 'Running', 'ShuttingDown', 'SystemUpdating']
- **Required**: Yes

### Message
- **Type**: typing.Optional[str]


# ClusterInstanceStorageConfig

### EbsVolumeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ClusterEbsVolumeConfig]


# ClusterLifeCycleConfig

### SourceS3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### OnCreate
- **Type**: <class 'str'>
- **Required**: Yes


# ClusterNodeDetails

### InstanceGroupName
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### InstanceStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ClusterInstanceStatusDetails]

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c5.12xlarge', 'ml.c5.18xlarge', 'ml.c5.24xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c5n.18xlarge', 'ml.c5n.2xlarge', 'ml.c5n.4xlarge', 'ml.c5n.9xlarge', 'ml.c5n.large', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.gr6.4xlarge', 'ml.gr6.8xlarge', 'ml.m5.12xlarge', 'ml.m5.16xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.8xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]

### LaunchTime
- **Type**: typing.Optional[datetime.datetime]

### LifeCycleConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ClusterLifeCycleConfig]

### OverrideVpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.VpcConfigOutput]

### ThreadsPerCore
- **Type**: typing.Optional[int]

### InstanceStorageConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ClusterInstanceStorageConfig]]

### PrivatePrimaryIp
- **Type**: typing.Optional[str]

### PrivatePrimaryIpv6
- **Type**: typing.Optional[str]

### PrivateDnsHostname
- **Type**: typing.Optional[str]

### Placement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ClusterInstancePlacement]


# ClusterNodeSummary

### InstanceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceType
- **Type**: typing.Literal['ml.c5.12xlarge', 'ml.c5.18xlarge', 'ml.c5.24xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c5n.18xlarge', 'ml.c5n.2xlarge', 'ml.c5n.4xlarge', 'ml.c5n.9xlarge', 'ml.c5n.large', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.gr6.4xlarge', 'ml.gr6.8xlarge', 'ml.m5.12xlarge', 'ml.m5.16xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.8xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']
- **Required**: Yes

### LaunchTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### InstanceStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ClusterInstanceStatusDetails'>
- **Required**: Yes


# ClusterOrchestrator

### Eks
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ClusterOrchestratorEksConfig'>
- **Required**: Yes


# ClusterOrchestratorEksConfig

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes


# ClusterSchedulerConfigSummary

### ClusterSchedulerConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterSchedulerConfigId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CreateFailed', 'CreateRollbackFailed', 'Created', 'Creating', 'DeleteFailed', 'DeleteRollbackFailed', 'Deleted', 'Deleting', 'UpdateFailed', 'UpdateRollbackFailed', 'Updated', 'Updating']
- **Required**: Yes

### ClusterSchedulerConfigVersion
- **Type**: typing.Optional[int]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### ClusterArn
- **Type**: typing.Optional[str]


# ClusterSummary

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ClusterStatus
- **Type**: typing.Literal['Creating', 'Deleting', 'Failed', 'InService', 'RollingBack', 'SystemUpdating', 'Updating']
- **Required**: Yes

### TrainingPlanArns
- **Type**: typing.Optional[typing.List[str]]


# CodeEditorAppImageConfig

### FileSystemConfig
- **Type**: <class 'NoneType'>

### ContainerConfig
- **Type**: <class 'NoneType'>


# CodeEditorAppImageConfigOutput

### FileSystemConfig
- **Type**: <class 'NoneType'>

### ContainerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ContainerConfigOutput]


# CodeEditorAppSettings

### DefaultResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResourceSpec]

### CustomImages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CustomImage]]

### LifecycleConfigArns
- **Type**: typing.Optional[typing.List[str]]

### AppLifecycleManagement
- **Type**: <class 'NoneType'>

### BuiltInLifecycleConfigArn
- **Type**: typing.Optional[str]


# CodeEditorAppSettingsOutput

### DefaultResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResourceSpec]

### CustomImages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CustomImage]]

### LifecycleConfigArns
- **Type**: typing.Optional[typing.List[str]]

### AppLifecycleManagement
- **Type**: <class 'NoneType'>

### BuiltInLifecycleConfigArn
- **Type**: typing.Optional[str]


# CodeRepository

### RepositoryUrl
- **Type**: <class 'str'>
- **Required**: Yes


# CodeRepositorySummary

### CodeRepositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### CodeRepositoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### GitConfig
- **Type**: <class 'NoneType'>


# CognitoConfig

### UserPool
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes


# CognitoMemberDefinition

### UserPool
- **Type**: <class 'str'>
- **Required**: Yes

### UserGroup
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes


# CollectionConfig

### VectorConfig
- **Type**: <class 'NoneType'>


# CollectionConfiguration

### CollectionName
- **Type**: typing.Optional[str]

### CollectionParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# CollectionConfigurationOutput

### CollectionName
- **Type**: typing.Optional[str]

### CollectionParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# CompilationJobSummary

### CompilationJobName
- **Type**: <class 'str'>
- **Required**: Yes

### CompilationJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CompilationJobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'INPROGRESS', 'STARTING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### CompilationStartTime
- **Type**: typing.Optional[datetime.datetime]

### CompilationEndTime
- **Type**: typing.Optional[datetime.datetime]

### CompilationTargetDevice
- **Type**: typing.Optional[typing.Literal['aisage', 'amba_cv2', 'amba_cv22', 'amba_cv25', 'coreml', 'deeplens', 'imx8mplus', 'imx8qm', 'jacinto_tda4vm', 'jetson_nano', 'jetson_tx1', 'jetson_tx2', 'jetson_xavier', 'lambda', 'ml_c4', 'ml_c5', 'ml_c6g', 'ml_eia2', 'ml_g4dn', 'ml_inf1', 'ml_inf2', 'ml_m4', 'ml_m5', 'ml_m6g', 'ml_p2', 'ml_p3', 'ml_trn1', 'qcs603', 'qcs605', 'rasp3b', 'rasp4b', 'rk3288', 'rk3399', 'sbe_c', 'sitara_am57x', 'x86_win32', 'x86_win64']]

### CompilationTargetPlatformOs
- **Type**: typing.Optional[typing.Literal['ANDROID', 'LINUX']]

### CompilationTargetPlatformArch
- **Type**: typing.Optional[typing.Literal['ARM64', 'ARM_EABI', 'ARM_EABIHF', 'X86', 'X86_64']]

### CompilationTargetPlatformAccelerator
- **Type**: typing.Optional[typing.Literal['INTEL_GRAPHICS', 'MALI', 'NNA', 'NVIDIA']]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# ComputeQuotaConfig

### ComputeQuotaResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ComputeQuotaResourceConfig]]

### ResourceSharingConfig
- **Type**: <class 'NoneType'>

### PreemptTeamTasks
- **Type**: typing.Optional[typing.Literal['LowerPriority', 'Never']]


# ComputeQuotaConfigOutput

### ComputeQuotaResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ComputeQuotaResourceConfig]]

### ResourceSharingConfig
- **Type**: <class 'NoneType'>

### PreemptTeamTasks
- **Type**: typing.Optional[typing.Literal['LowerPriority', 'Never']]


# ComputeQuotaResourceConfig

### InstanceType
- **Type**: typing.Literal['ml.c5.12xlarge', 'ml.c5.18xlarge', 'ml.c5.24xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c5n.18xlarge', 'ml.c5n.2xlarge', 'ml.c5n.4xlarge', 'ml.c5n.9xlarge', 'ml.c5n.large', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.gr6.4xlarge', 'ml.gr6.8xlarge', 'ml.m5.12xlarge', 'ml.m5.16xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.8xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']
- **Required**: Yes

### Count
- **Type**: <class 'int'>
- **Required**: Yes


# ComputeQuotaSummary

### ComputeQuotaArn
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeQuotaId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CreateFailed', 'CreateRollbackFailed', 'Created', 'Creating', 'DeleteFailed', 'DeleteRollbackFailed', 'Deleted', 'Deleting', 'UpdateFailed', 'UpdateRollbackFailed', 'Updated', 'Updating']
- **Required**: Yes

### ComputeQuotaTarget
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ComputeQuotaTarget'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ComputeQuotaVersion
- **Type**: typing.Optional[int]

### ClusterArn
- **Type**: typing.Optional[str]

### ComputeQuotaConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ComputeQuotaConfigOutput]

### ActivationState
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# ComputeQuotaTarget

### TeamName
- **Type**: <class 'str'>
- **Required**: Yes

### FairShareWeight
- **Type**: typing.Optional[int]


# ConditionStepMetadata

### Outcome
- **Type**: typing.Optional[typing.Literal['False', 'True']]


# ContainerConfig

### ContainerArguments
- **Type**: typing.Optional[typing.List[str]]

### ContainerEntrypoint
- **Type**: typing.Optional[typing.List[str]]

### ContainerEnvironmentVariables
- **Type**: typing.Optional[typing.Dict[str, str]]


# ContainerConfigOutput

### ContainerArguments
- **Type**: typing.Optional[typing.List[str]]

### ContainerEntrypoint
- **Type**: typing.Optional[typing.List[str]]

### ContainerEnvironmentVariables
- **Type**: typing.Optional[typing.Dict[str, str]]


# ContainerDefinition

### ContainerHostname
- **Type**: typing.Optional[str]

### Image
- **Type**: typing.Optional[str]

### ImageConfig
- **Type**: <class 'NoneType'>

### Mode
- **Type**: typing.Optional[typing.Literal['MultiModel', 'SingleModel']]

### ModelDataUrl
- **Type**: typing.Optional[str]

### ModelDataSource
- **Type**: <class 'NoneType'>

### AdditionalModelDataSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AdditionalModelDataSource]]

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]

### ModelPackageName
- **Type**: typing.Optional[str]

### InferenceSpecificationName
- **Type**: typing.Optional[str]

### MultiModelConfig
- **Type**: <class 'NoneType'>


# ContainerDefinitionOutput

### ContainerHostname
- **Type**: typing.Optional[str]

### Image
- **Type**: typing.Optional[str]

### ImageConfig
- **Type**: <class 'NoneType'>

### Mode
- **Type**: typing.Optional[typing.Literal['MultiModel', 'SingleModel']]

### ModelDataUrl
- **Type**: typing.Optional[str]

### ModelDataSource
- **Type**: <class 'NoneType'>

### AdditionalModelDataSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AdditionalModelDataSource]]

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]

### ModelPackageName
- **Type**: typing.Optional[str]

### InferenceSpecificationName
- **Type**: typing.Optional[str]

### MultiModelConfig
- **Type**: <class 'NoneType'>


# ContextSource

### SourceUri
- **Type**: <class 'str'>
- **Required**: Yes

### SourceType
- **Type**: typing.Optional[str]

### SourceId
- **Type**: typing.Optional[str]


# ContextSummary

### ContextArn
- **Type**: typing.Optional[str]

### ContextName
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ContextSource]

### ContextType
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# ContinuousParameterRange

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MinValue
- **Type**: <class 'str'>
- **Required**: Yes

### MaxValue
- **Type**: <class 'str'>
- **Required**: Yes

### ScalingType
- **Type**: typing.Optional[typing.Literal['Auto', 'Linear', 'Logarithmic', 'ReverseLogarithmic']]


# ContinuousParameterRangeSpecification

### MinValue
- **Type**: <class 'str'>
- **Required**: Yes

### MaxValue
- **Type**: <class 'str'>
- **Required**: Yes


# ConvergenceDetected

### CompleteOnConvergence
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# CreateActionRequest

### ActionName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ActionSource'>
- **Required**: Yes

### ActionType
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping', 'Unknown']]

### Properties
- **Type**: typing.Optional[typing.Dict[str, str]]

### MetadataProperties
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateActionResponse

### ActionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAlgorithmInput

### AlgorithmName
- **Type**: <class 'str'>
- **Required**: Yes

### TrainingSpecification
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrainingSpecification, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrainingSpecificationOutput]
- **Required**: Yes

### AlgorithmDescription
- **Type**: typing.Optional[str]

### InferenceSpecification
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceSpecification, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceSpecificationOutput, NoneType]

### ValidationSpecification
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AlgorithmValidationSpecification, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AlgorithmValidationSpecificationOutput, NoneType]

### CertifyForMarketplace
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateAlgorithmOutput

### AlgorithmArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAppImageConfigRequest

### AppImageConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]

### KernelGatewayImageConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.KernelGatewayImageConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.KernelGatewayImageConfigOutput, NoneType]

### JupyterLabAppImageConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.JupyterLabAppImageConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.JupyterLabAppImageConfigOutput, NoneType]

### CodeEditorAppImageConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CodeEditorAppImageConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CodeEditorAppImageConfigOutput, NoneType]


# CreateAppImageConfigResponse

### AppImageConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAppRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### AppType
- **Type**: typing.Literal['Canvas', 'CodeEditor', 'DetailedProfiler', 'JupyterLab', 'JupyterServer', 'KernelGateway', 'RSessionGateway', 'RStudioServerPro', 'TensorBoard']
- **Required**: Yes

### AppName
- **Type**: <class 'str'>
- **Required**: Yes

### UserProfileName
- **Type**: typing.Optional[str]

### SpaceName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]

### ResourceSpec
- **Type**: <class 'NoneType'>


# CreateAppResponse

### AppArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateArtifactRequest

### Source
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ArtifactSource, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ArtifactSourceOutput]
- **Required**: Yes

### ArtifactType
- **Type**: <class 'str'>
- **Required**: Yes

### ArtifactName
- **Type**: typing.Optional[str]

### Properties
- **Type**: typing.Optional[typing.Dict[str, str]]

### MetadataProperties
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateArtifactResponse

### ArtifactArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAutoMLJobRequest

### AutoMLJobName
- **Type**: <class 'str'>
- **Required**: Yes

### InputDataConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLChannel]
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLOutputDataConfig'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProblemType
- **Type**: typing.Optional[typing.Literal['BinaryClassification', 'MulticlassClassification', 'Regression']]

### AutoMLJobObjective
- **Type**: <class 'NoneType'>

### AutoMLJobConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLJobConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLJobConfigOutput, NoneType]

### GenerateCandidateDefinitionsOnly
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]

### ModelDeployConfig
- **Type**: <class 'NoneType'>


# CreateAutoMLJobResponse

### AutoMLJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAutoMLJobV2Request

### AutoMLJobName
- **Type**: <class 'str'>
- **Required**: Yes

### AutoMLJobInputDataConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLJobChannel]
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLOutputDataConfig'>
- **Required**: Yes

### AutoMLProblemTypeConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLProblemTypeConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLProblemTypeConfigOutput]
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]

### SecurityConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLSecurityConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLSecurityConfigOutput, NoneType]

### AutoMLJobObjective
- **Type**: <class 'NoneType'>

### ModelDeployConfig
- **Type**: <class 'NoneType'>

### DataSplitConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLDataSplitConfig]

### AutoMLComputeConfig
- **Type**: <class 'NoneType'>


# CreateAutoMLJobV2Response

### AutoMLJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateClusterRequest

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ClusterInstanceGroupSpecification]
- **Required**: Yes

### VpcConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.VpcConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.VpcConfigOutput, NoneType]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]

### Orchestrator
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ClusterOrchestrator]

### NodeRecovery
- **Type**: typing.Optional[typing.Literal['Automatic', 'None']]


# CreateClusterResponse

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateClusterSchedulerConfigRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### SchedulerConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SchedulerConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SchedulerConfigOutput]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateClusterSchedulerConfigResponse

### ClusterSchedulerConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterSchedulerConfigId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCodeRepositoryInput

### CodeRepositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### GitConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.GitConfig'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateCodeRepositoryOutput

### CodeRepositoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCompilationJobRequest

### CompilationJobName
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OutputConfig'>
- **Required**: Yes

### StoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.StoppingCondition'>
- **Required**: Yes

### ModelPackageVersionArn
- **Type**: typing.Optional[str]

### InputConfig
- **Type**: <class 'NoneType'>

### VpcConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.NeoVpcConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.NeoVpcConfigOutput, NoneType]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateCompilationJobResponse

### CompilationJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateComputeQuotaRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeQuotaConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ComputeQuotaConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ComputeQuotaConfigOutput]
- **Required**: Yes

### ComputeQuotaTarget
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ComputeQuotaTarget'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ActivationState
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateComputeQuotaResponse

### ComputeQuotaArn
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeQuotaId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateContextRequest

### ContextName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ContextSource'>
- **Required**: Yes

### ContextType
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Properties
- **Type**: typing.Optional[typing.Dict[str, str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateContextResponse

### ContextArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDataQualityJobDefinitionRequest

### JobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### DataQualityAppSpecification
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DataQualityAppSpecification, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DataQualityAppSpecificationOutput]
- **Required**: Yes

### DataQualityJobInput
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DataQualityJobInput, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DataQualityJobInputOutput]
- **Required**: Yes

### DataQualityJobOutputConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringOutputConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringOutputConfigOutput]
- **Required**: Yes

### JobResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringResources'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DataQualityBaselineConfig
- **Type**: <class 'NoneType'>

### NetworkConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringNetworkConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringNetworkConfigOutput, NoneType]

### StoppingCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringStoppingCondition]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateDataQualityJobDefinitionResponse

### JobDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDeviceFleetRequest

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EdgeOutputConfig'>
- **Required**: Yes

### RoleArn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]

### EnableIotRoleAlias
- **Type**: typing.Optional[bool]


# CreateDomainRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### AuthMode
- **Type**: typing.Literal['IAM', 'SSO']
- **Required**: Yes

### DefaultUserSettings
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserSettings, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserSettingsOutput]
- **Required**: Yes

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainSettings
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DomainSettings, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DomainSettingsOutput, NoneType]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]

### AppNetworkAccessType
- **Type**: typing.Optional[typing.Literal['PublicInternetOnly', 'VpcOnly']]

### HomeEfsFileSystemKmsKeyId
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### AppSecurityGroupManagement
- **Type**: typing.Optional[typing.Literal['Customer', 'Service']]

### TagPropagation
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DefaultSpaceSettings
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DefaultSpaceSettings, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DefaultSpaceSettingsOutput, NoneType]


# CreateDomainResponse

### DomainArn
- **Type**: <class 'str'>
- **Required**: Yes

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEdgeDeploymentPlanRequest

### EdgeDeploymentPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EdgeDeploymentModelConfig]
- **Required**: Yes

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes

### Stages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DeploymentStage]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateEdgeDeploymentPlanResponse

### EdgeDeploymentPlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEdgeDeploymentStageRequest

### EdgeDeploymentPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### Stages
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DeploymentStage]
- **Required**: Yes


# CreateEdgePackagingJobRequest

### EdgePackagingJobName
- **Type**: <class 'str'>
- **Required**: Yes

### CompilationJobName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EdgeOutputConfig'>
- **Required**: Yes

### ResourceKey
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateEndpointConfigInput

### EndpointConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### ProductionVariants
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProductionVariant]
- **Required**: Yes

### DataCaptureConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DataCaptureConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DataCaptureConfigOutput, NoneType]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]

### KmsKeyId
- **Type**: typing.Optional[str]

### AsyncInferenceConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AsyncInferenceConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AsyncInferenceConfigOutput, NoneType]

### ExplainerConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ExplainerConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ExplainerConfigOutput, NoneType]

### ShadowProductionVariants
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProductionVariant]]

### ExecutionRoleArn
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.VpcConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.VpcConfigOutput, NoneType]

### EnableNetworkIsolation
- **Type**: typing.Optional[bool]


# CreateEndpointConfigOutput

### EndpointConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEndpointInput

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### DeploymentConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DeploymentConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DeploymentConfigOutput, NoneType]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateEndpointOutput

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateExperimentRequest

### ExperimentName
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateExperimentResponse

### ExperimentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFeatureGroupRequest

### FeatureGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### RecordIdentifierFeatureName
- **Type**: <class 'str'>
- **Required**: Yes

### EventTimeFeatureName
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.FeatureDefinition]
- **Required**: Yes

### OnlineStoreConfig
- **Type**: <class 'NoneType'>

### OfflineStoreConfig
- **Type**: <class 'NoneType'>

### ThroughputConfig
- **Type**: <class 'NoneType'>

### RoleArn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateFeatureGroupResponse

### FeatureGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFlowDefinitionRequest

### FlowDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.FlowDefinitionOutputConfig'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### HumanLoopRequestSource
- **Type**: <class 'NoneType'>

### HumanLoopActivationConfig
- **Type**: <class 'NoneType'>

### HumanLoopConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HumanLoopConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HumanLoopConfigOutput, NoneType]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateFlowDefinitionResponse

### FlowDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateHubContentReferenceRequest

### HubName
- **Type**: <class 'str'>
- **Required**: Yes

### SageMakerPublicHubContentArn
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentName
- **Type**: typing.Optional[str]

### MinVersion
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateHubContentReferenceResponse

### HubArn
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateHubRequest

### HubName
- **Type**: <class 'str'>
- **Required**: Yes

### HubDescription
- **Type**: <class 'str'>
- **Required**: Yes

### HubDisplayName
- **Type**: typing.Optional[str]

### HubSearchKeywords
- **Type**: typing.Optional[typing.List[str]]

### S3StorageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HubS3StorageConfig]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateHubResponse

### HubArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateHumanTaskUiRequest

### HumanTaskUiName
- **Type**: <class 'str'>
- **Required**: Yes

### UiTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UiTemplate'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateHumanTaskUiResponse

### HumanTaskUiArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateHyperParameterTuningJobRequest

### HyperParameterTuningJobName
- **Type**: <class 'str'>
- **Required**: Yes

### HyperParameterTuningJobConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTuningJobConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTuningJobConfigOutput]
- **Required**: Yes

### TrainingJobDefinition
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTrainingJobDefinition, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTrainingJobDefinitionOutput, NoneType]

### TrainingJobDefinitions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTrainingJobDefinition, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTrainingJobDefinitionOutput]]]

### WarmStartConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTuningJobWarmStartConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTuningJobWarmStartConfigOutput, NoneType]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]

### Autotune
- **Type**: <class 'NoneType'>


# CreateHyperParameterTuningJobResponse

### HyperParameterTuningJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateImageRequest

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateImageResponse

### ImageArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateImageVersionRequest

### BaseImage
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### Aliases
- **Type**: typing.Optional[typing.List[str]]

### VendorGuidance
- **Type**: typing.Optional[typing.Literal['ARCHIVED', 'NOT_PROVIDED', 'STABLE', 'TO_BE_ARCHIVED']]

### JobType
- **Type**: typing.Optional[typing.Literal['INFERENCE', 'NOTEBOOK_KERNEL', 'TRAINING']]

### MLFramework
- **Type**: typing.Optional[str]

### ProgrammingLang
- **Type**: typing.Optional[str]

### Processor
- **Type**: typing.Optional[typing.Literal['CPU', 'GPU']]

### Horovod
- **Type**: typing.Optional[bool]

### ReleaseNotes
- **Type**: typing.Optional[str]


# CreateImageVersionResponse

### ImageVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateInferenceComponentInput

### InferenceComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### Specification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceComponentSpecification'>
- **Required**: Yes

### VariantName
- **Type**: typing.Optional[str]

### RuntimeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceComponentRuntimeConfig]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateInferenceComponentOutput

### InferenceComponentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateInferenceExperimentRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['ShadowMode']
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVariants
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelVariantConfig]
- **Required**: Yes

### ShadowModeConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ShadowModeConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ShadowModeConfigOutput]
- **Required**: Yes

### Schedule
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceExperimentSchedule, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceExperimentScheduleOutput, NoneType]

### Description
- **Type**: typing.Optional[str]

### DataStorageConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceExperimentDataStorageConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceExperimentDataStorageConfigOutput, NoneType]

### KmsKey
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateInferenceExperimentResponse

### InferenceExperimentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateInferenceRecommendationsJobRequest

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### JobType
- **Type**: typing.Literal['Advanced', 'Default']
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### InputConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.RecommendationJobInputConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.RecommendationJobInputConfigOutput]
- **Required**: Yes

### JobDescription
- **Type**: typing.Optional[str]

### StoppingConditions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.RecommendationJobStoppingConditions, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.RecommendationJobStoppingConditionsOutput, NoneType]

### OutputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.RecommendationJobOutputConfig]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateInferenceRecommendationsJobResponse

### JobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLabelingJobRequest

### LabelingJobName
- **Type**: <class 'str'>
- **Required**: Yes

### LabelAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### InputConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.LabelingJobInputConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.LabelingJobInputConfigOutput]
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.LabelingJobOutputConfig'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### HumanTaskConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HumanTaskConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HumanTaskConfigOutput]
- **Required**: Yes

### LabelCategoryConfigS3Uri
- **Type**: typing.Optional[str]

### StoppingConditions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.LabelingJobStoppingConditions]

### LabelingJobAlgorithmsConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.LabelingJobAlgorithmsConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.LabelingJobAlgorithmsConfigOutput, NoneType]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateLabelingJobResponse

### LabelingJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMlflowTrackingServerRequest

### TrackingServerName
- **Type**: <class 'str'>
- **Required**: Yes

### ArtifactStoreUri
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### TrackingServerSize
- **Type**: typing.Optional[typing.Literal['Large', 'Medium', 'Small']]

### MlflowVersion
- **Type**: typing.Optional[str]

### AutomaticModelRegistration
- **Type**: typing.Optional[bool]

### WeeklyMaintenanceWindowStart
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateMlflowTrackingServerResponse

### TrackingServerArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateModelBiasJobDefinitionRequest

### JobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelBiasAppSpecification
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelBiasAppSpecification, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelBiasAppSpecificationOutput]
- **Required**: Yes

### ModelBiasJobInput
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelBiasJobInput, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelBiasJobInputOutput]
- **Required**: Yes

### ModelBiasJobOutputConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringOutputConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringOutputConfigOutput]
- **Required**: Yes

### JobResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringResources'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ModelBiasBaselineConfig
- **Type**: <class 'NoneType'>

### NetworkConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringNetworkConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringNetworkConfigOutput, NoneType]

### StoppingCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringStoppingCondition]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateModelBiasJobDefinitionResponse

### JobDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateModelCardExportJobRequest

### ModelCardName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelCardExportJobName
- **Type**: <class 'str'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelCardExportOutputConfig'>
- **Required**: Yes

### ModelCardVersion
- **Type**: typing.Optional[int]


# CreateModelCardExportJobResponse

### ModelCardExportJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateModelCardRequest

### ModelCardName
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: <class 'str'>
- **Required**: Yes

### ModelCardStatus
- **Type**: typing.Literal['Approved', 'Archived', 'Draft', 'PendingReview']
- **Required**: Yes

### SecurityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelCardSecurityConfig]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateModelCardResponse

### ModelCardArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateModelExplainabilityJobDefinitionRequest

### JobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelExplainabilityAppSpecification
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelExplainabilityAppSpecification, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelExplainabilityAppSpecificationOutput]
- **Required**: Yes

### ModelExplainabilityJobInput
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelExplainabilityJobInput, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelExplainabilityJobInputOutput]
- **Required**: Yes

### ModelExplainabilityJobOutputConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringOutputConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringOutputConfigOutput]
- **Required**: Yes

### JobResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringResources'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ModelExplainabilityBaselineConfig
- **Type**: <class 'NoneType'>

### NetworkConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringNetworkConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringNetworkConfigOutput, NoneType]

### StoppingCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringStoppingCondition]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateModelExplainabilityJobDefinitionResponse

### JobDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateModelInput

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### PrimaryContainer
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ContainerDefinition, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ContainerDefinitionOutput, NoneType]

### Containers
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ContainerDefinition, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ContainerDefinitionOutput]]]

### InferenceExecutionConfig
- **Type**: <class 'NoneType'>

### ExecutionRoleArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]

### VpcConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.VpcConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.VpcConfigOutput, NoneType]

### EnableNetworkIsolation
- **Type**: typing.Optional[bool]


# CreateModelOutput

### ModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateModelPackageGroupInput

### ModelPackageGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelPackageGroupDescription
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateModelPackageGroupOutput

### ModelPackageGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateModelPackageInput

### ModelPackageName
- **Type**: typing.Optional[str]

### ModelPackageGroupName
- **Type**: typing.Optional[str]

### ModelPackageDescription
- **Type**: typing.Optional[str]

### InferenceSpecification
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceSpecification, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceSpecificationOutput, NoneType]

### ValidationSpecification
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelPackageValidationSpecification, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelPackageValidationSpecificationOutput, NoneType]

### SourceAlgorithmSpecification
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SourceAlgorithmSpecification, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SourceAlgorithmSpecificationOutput, NoneType]

### CertifyForMarketplace
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]

### ModelApprovalStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'PendingManualApproval', 'Rejected']]

### MetadataProperties
- **Type**: <class 'NoneType'>

### ModelMetrics
- **Type**: <class 'NoneType'>

### ClientToken
- **Type**: typing.Optional[str]

### Domain
- **Type**: typing.Optional[str]

### Task
- **Type**: typing.Optional[str]

### SamplePayloadUrl
- **Type**: typing.Optional[str]

### CustomerMetadataProperties
- **Type**: typing.Optional[typing.Dict[str, str]]

### DriftCheckBaselines
- **Type**: <class 'NoneType'>

### AdditionalInferenceSpecifications
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AdditionalInferenceSpecificationDefinition, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AdditionalInferenceSpecificationDefinitionOutput]]]

### SkipModelValidation
- **Type**: typing.Optional[typing.Literal['All', 'None']]

### SourceUri
- **Type**: typing.Optional[str]

### SecurityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelPackageSecurityConfig]

### ModelCard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelPackageModelCard]

### ModelLifeCycle
- **Type**: <class 'NoneType'>


# CreateModelPackageOutput

### ModelPackageArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateModelQualityJobDefinitionRequest

### JobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelQualityAppSpecification
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelQualityAppSpecification, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelQualityAppSpecificationOutput]
- **Required**: Yes

### ModelQualityJobInput
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelQualityJobInput, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelQualityJobInputOutput]
- **Required**: Yes

### ModelQualityJobOutputConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringOutputConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringOutputConfigOutput]
- **Required**: Yes

### JobResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringResources'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ModelQualityBaselineConfig
- **Type**: <class 'NoneType'>

### NetworkConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringNetworkConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringNetworkConfigOutput, NoneType]

### StoppingCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringStoppingCondition]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateModelQualityJobDefinitionResponse

### JobDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMonitoringScheduleRequest

### MonitoringScheduleName
- **Type**: <class 'str'>
- **Required**: Yes

### MonitoringScheduleConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringScheduleConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringScheduleConfigOutput]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateMonitoringScheduleResponse

### MonitoringScheduleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateNotebookInstanceInput

### NotebookInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceType
- **Type**: typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c5d.18xlarge', 'ml.c5d.2xlarge', 'ml.c5d.4xlarge', 'ml.c5d.9xlarge', 'ml.c5d.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c6id.12xlarge', 'ml.c6id.16xlarge', 'ml.c6id.24xlarge', 'ml.c6id.2xlarge', 'ml.c6id.32xlarge', 'ml.c6id.4xlarge', 'ml.c6id.8xlarge', 'ml.c6id.large', 'ml.c6id.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.inf1.24xlarge', 'ml.inf1.2xlarge', 'ml.inf1.6xlarge', 'ml.inf1.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.16xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.8xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m6id.12xlarge', 'ml.m6id.16xlarge', 'ml.m6id.24xlarge', 'ml.m6id.2xlarge', 'ml.m6id.32xlarge', 'ml.m6id.4xlarge', 'ml.m6id.8xlarge', 'ml.m6id.large', 'ml.m6id.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r6id.12xlarge', 'ml.r6id.16xlarge', 'ml.r6id.24xlarge', 'ml.r6id.2xlarge', 'ml.r6id.32xlarge', 'ml.r6id.4xlarge', 'ml.r6id.8xlarge', 'ml.r6id.large', 'ml.r6id.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.t2.2xlarge', 'ml.t2.large', 'ml.t2.medium', 'ml.t2.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge']
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetId
- **Type**: typing.Optional[str]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### KmsKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]

### LifecycleConfigName
- **Type**: typing.Optional[str]

### DirectInternetAccess
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### VolumeSizeInGB
- **Type**: typing.Optional[int]

### AcceleratorTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ml.eia1.large', 'ml.eia1.medium', 'ml.eia1.xlarge', 'ml.eia2.large', 'ml.eia2.medium', 'ml.eia2.xlarge']]]

### DefaultCodeRepository
- **Type**: typing.Optional[str]

### AdditionalCodeRepositories
- **Type**: typing.Optional[typing.List[str]]

### RootAccess
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### PlatformIdentifier
- **Type**: typing.Optional[str]

### InstanceMetadataServiceConfiguration
- **Type**: <class 'NoneType'>


# CreateNotebookInstanceLifecycleConfigInput

### NotebookInstanceLifecycleConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### OnCreate
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.NotebookInstanceLifecycleHook]]

### OnStart
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.NotebookInstanceLifecycleHook]]


# CreateNotebookInstanceLifecycleConfigOutput

### NotebookInstanceLifecycleConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateNotebookInstanceOutput

### NotebookInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateOptimizationJobRequest

### OptimizationJobName
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ModelSource
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OptimizationJobModelSource'>
- **Required**: Yes

### DeploymentInstanceType
- **Type**: typing.Literal['ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge']
- **Required**: Yes

### OptimizationConfigs
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OptimizationConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OptimizationConfigOutput]]
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OptimizationJobOutputConfig'>
- **Required**: Yes

### StoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.StoppingCondition'>
- **Required**: Yes

### OptimizationEnvironment
- **Type**: typing.Optional[typing.Dict[str, str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]

### VpcConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OptimizationVpcConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OptimizationVpcConfigOutput, NoneType]


# CreateOptimizationJobResponse

### OptimizationJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePartnerAppPresignedUrlRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ExpiresInSeconds
- **Type**: typing.Optional[int]

### SessionExpirationDurationInSeconds
- **Type**: typing.Optional[int]


# CreatePartnerAppPresignedUrlResponse

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePartnerAppRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['comet', 'deepchecks-llm-evaluation', 'fiddler', 'lakera-guard']
- **Required**: Yes

### ExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tier
- **Type**: <class 'str'>
- **Required**: Yes

### AuthType
- **Type**: typing.Literal['IAM']
- **Required**: Yes

### MaintenanceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PartnerAppMaintenanceConfig]

### ApplicationConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PartnerAppConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PartnerAppConfigOutput, NoneType]

### EnableIamSessionBasedIdentity
- **Type**: typing.Optional[bool]

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreatePartnerAppResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePipelineRequest

### PipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineDisplayName
- **Type**: typing.Optional[str]

### PipelineDefinition
- **Type**: typing.Optional[str]

### PipelineDefinitionS3Location
- **Type**: <class 'NoneType'>

### PipelineDescription
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]

### ParallelismConfiguration
- **Type**: <class 'NoneType'>


# CreatePipelineResponse

### PipelineArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePresignedDomainUrlRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### UserProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### SessionExpirationDurationInSeconds
- **Type**: typing.Optional[int]

### ExpiresInSeconds
- **Type**: typing.Optional[int]

### SpaceName
- **Type**: typing.Optional[str]

### LandingUri
- **Type**: typing.Optional[str]


# CreatePresignedDomainUrlResponse

### AuthorizedUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePresignedMlflowTrackingServerUrlRequest

### TrackingServerName
- **Type**: <class 'str'>
- **Required**: Yes

### ExpiresInSeconds
- **Type**: typing.Optional[int]

### SessionExpirationDurationInSeconds
- **Type**: typing.Optional[int]


# CreatePresignedMlflowTrackingServerUrlResponse

### AuthorizedUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePresignedNotebookInstanceUrlInput

### NotebookInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### SessionExpirationDurationInSeconds
- **Type**: typing.Optional[int]


# CreatePresignedNotebookInstanceUrlOutput

### AuthorizedUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProcessingJobRequest

### ProcessingJobName
- **Type**: <class 'str'>
- **Required**: Yes

### ProcessingResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProcessingResources'>
- **Required**: Yes

### AppSpecification
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AppSpecification, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AppSpecificationOutput]
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProcessingInputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProcessingInput]]

### ProcessingOutputConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProcessingOutputConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProcessingOutputConfigOutput, NoneType]

### StoppingCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProcessingStoppingCondition]

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]

### NetworkConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.NetworkConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.NetworkConfigOutput, NoneType]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]

### ExperimentConfig
- **Type**: <class 'NoneType'>


# CreateProcessingJobResponse

### ProcessingJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProjectInput

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceCatalogProvisioningDetails
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ServiceCatalogProvisioningDetails, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ServiceCatalogProvisioningDetailsOutput]
- **Required**: Yes

### ProjectDescription
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateProjectOutput

### ProjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProjectId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSpaceRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### SpaceName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]

### SpaceSettings
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SpaceSettings, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SpaceSettingsOutput, NoneType]

### OwnershipSettings
- **Type**: <class 'NoneType'>

### SpaceSharingSettings
- **Type**: <class 'NoneType'>

### SpaceDisplayName
- **Type**: typing.Optional[str]


# CreateSpaceResponse

### SpaceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateStudioLifecycleConfigRequest

### StudioLifecycleConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### StudioLifecycleConfigContent
- **Type**: <class 'str'>
- **Required**: Yes

### StudioLifecycleConfigAppType
- **Type**: typing.Literal['CodeEditor', 'JupyterLab', 'JupyterServer', 'KernelGateway']
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateStudioLifecycleConfigResponse

### StudioLifecycleConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTrainingJobRequest

### TrainingJobName
- **Type**: <class 'str'>
- **Required**: Yes

### AlgorithmSpecification
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AlgorithmSpecification, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AlgorithmSpecificationOutput]
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OutputDataConfig'>
- **Required**: Yes

### ResourceConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResourceConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResourceConfigOutput]
- **Required**: Yes

### StoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.StoppingCondition'>
- **Required**: Yes

### HyperParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### InputDataConfig
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Channel, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ChannelOutput]]]

### VpcConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.VpcConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.VpcConfigOutput, NoneType]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]

### EnableNetworkIsolation
- **Type**: typing.Optional[bool]

### EnableInterContainerTrafficEncryption
- **Type**: typing.Optional[bool]

### EnableManagedSpotTraining
- **Type**: typing.Optional[bool]

### CheckpointConfig
- **Type**: <class 'NoneType'>

### DebugHookConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DebugHookConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DebugHookConfigOutput, NoneType]

### DebugRuleConfigurations
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DebugRuleConfiguration, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DebugRuleConfigurationOutput]]]

### TensorBoardOutputConfig
- **Type**: <class 'NoneType'>

### ExperimentConfig
- **Type**: <class 'NoneType'>

### ProfilerConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProfilerConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProfilerConfigOutput, NoneType]

### ProfilerRuleConfigurations
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProfilerRuleConfiguration, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProfilerRuleConfigurationOutput]]]

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]

### RetryStrategy
- **Type**: <class 'NoneType'>

### RemoteDebugConfig
- **Type**: <class 'NoneType'>

### InfraCheckConfig
- **Type**: <class 'NoneType'>

### SessionChainingConfig
- **Type**: <class 'NoneType'>


# CreateTrainingJobResponse

### TrainingJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTrainingPlanRequest

### TrainingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### TrainingPlanOfferingId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateTrainingPlanResponse

### TrainingPlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTransformJobRequest

### TransformJobName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### TransformInput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TransformInput'>
- **Required**: Yes

### TransformOutput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TransformOutput'>
- **Required**: Yes

### TransformResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TransformResources'>
- **Required**: Yes

### MaxConcurrentTransforms
- **Type**: typing.Optional[int]

### ModelClientConfig
- **Type**: <class 'NoneType'>

### MaxPayloadInMB
- **Type**: typing.Optional[int]

### BatchStrategy
- **Type**: typing.Optional[typing.Literal['MultiRecord', 'SingleRecord']]

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]

### DataCaptureConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.BatchDataCaptureConfig]

### DataProcessing
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]

### ExperimentConfig
- **Type**: <class 'NoneType'>


# CreateTransformJobResponse

### TransformJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTrialComponentRequest

### TrialComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrialComponentStatus]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrialComponentParameterValue]]

### InputArtifacts
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrialComponentArtifact]]

### OutputArtifacts
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrialComponentArtifact]]

### MetadataProperties
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateTrialComponentResponse

### TrialComponentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTrialRequest

### TrialName
- **Type**: <class 'str'>
- **Required**: Yes

### ExperimentName
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### MetadataProperties
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateTrialResponse

### TrialArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUserProfileRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### UserProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### SingleSignOnUserIdentifier
- **Type**: typing.Optional[str]

### SingleSignOnUserValue
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]

### UserSettings
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserSettings, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserSettingsOutput, NoneType]


# CreateUserProfileResponse

### UserProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWorkforceRequest

### WorkforceName
- **Type**: <class 'str'>
- **Required**: Yes

### CognitoConfig
- **Type**: <class 'NoneType'>

### OidcConfig
- **Type**: <class 'NoneType'>

### SourceIpConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SourceIpConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SourceIpConfigOutput, NoneType]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]

### WorkforceVpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.WorkforceVpcConfigRequest]


# CreateWorkforceResponse

### WorkforceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWorkteamRequest

### WorkteamName
- **Type**: <class 'str'>
- **Required**: Yes

### MemberDefinitions
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MemberDefinition, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MemberDefinitionOutput]]
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### WorkforceName
- **Type**: typing.Optional[str]

### NotificationConfiguration
- **Type**: <class 'NoneType'>

### WorkerAccessConfiguration
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# CreateWorkteamResponse

### WorkteamArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# CustomFileSystem

### EFSFileSystem
- **Type**: <class 'NoneType'>

### FSxLustreFileSystem
- **Type**: <class 'NoneType'>


# CustomFileSystemConfig

### EFSFileSystemConfig
- **Type**: <class 'NoneType'>

### FSxLustreFileSystemConfig
- **Type**: <class 'NoneType'>


# CustomImage

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### AppImageConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### ImageVersionNumber
- **Type**: typing.Optional[int]


# CustomPosixUserConfig

### Uid
- **Type**: <class 'int'>
- **Required**: Yes

### Gid
- **Type**: <class 'int'>
- **Required**: Yes


# CustomizedMetricSpecification

### MetricName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### Statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]


# DataCaptureConfig

### InitialSamplingPercentage
- **Type**: <class 'int'>
- **Required**: Yes

### DestinationS3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### CaptureOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CaptureOption]
- **Required**: Yes

### EnableCapture
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### CaptureContentTypeHeader
- **Type**: <class 'NoneType'>


# DataCaptureConfigOutput

### InitialSamplingPercentage
- **Type**: <class 'int'>
- **Required**: Yes

### DestinationS3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### CaptureOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CaptureOption]
- **Required**: Yes

### EnableCapture
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### CaptureContentTypeHeader
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CaptureContentTypeHeaderOutput]


# DataCaptureConfigSummary

### EnableCapture
- **Type**: <class 'bool'>
- **Required**: Yes

### CaptureStatus
- **Type**: typing.Literal['Started', 'Stopped']
- **Required**: Yes

### CurrentSamplingPercentage
- **Type**: <class 'int'>
- **Required**: Yes

### DestinationS3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes


# DataCatalogConfig

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes


# DataProcessing

### InputFilter
- **Type**: typing.Optional[str]

### OutputFilter
- **Type**: typing.Optional[str]

### JoinSource
- **Type**: typing.Optional[typing.Literal['Input', 'None']]


# DataQualityAppSpecification

### ImageUri
- **Type**: <class 'str'>
- **Required**: Yes

### ContainerEntrypoint
- **Type**: typing.Optional[typing.List[str]]

### ContainerArguments
- **Type**: typing.Optional[typing.List[str]]

### RecordPreprocessorSourceUri
- **Type**: typing.Optional[str]

### PostAnalyticsProcessorSourceUri
- **Type**: typing.Optional[str]

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]


# DataQualityAppSpecificationOutput

### ImageUri
- **Type**: <class 'str'>
- **Required**: Yes

### ContainerEntrypoint
- **Type**: typing.Optional[typing.List[str]]

### ContainerArguments
- **Type**: typing.Optional[typing.List[str]]

### RecordPreprocessorSourceUri
- **Type**: typing.Optional[str]

### PostAnalyticsProcessorSourceUri
- **Type**: typing.Optional[str]

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]


# DataQualityBaselineConfig

### BaseliningJobName
- **Type**: typing.Optional[str]

### ConstraintsResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringConstraintsResource]

### StatisticsResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringStatisticsResource]


# DataQualityJobInput

### EndpointInput
- **Type**: <class 'NoneType'>

### BatchTransformInput
- **Type**: <class 'NoneType'>


# DataQualityJobInputOutput

### EndpointInput
- **Type**: <class 'NoneType'>

### BatchTransformInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.BatchTransformInputOutput]


# DataSource

### S3DataSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.S3DataSource, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.S3DataSourceOutput, NoneType]

### FileSystemDataSource
- **Type**: <class 'NoneType'>


# DataSourceOutput

### S3DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.S3DataSourceOutput]

### FileSystemDataSource
- **Type**: <class 'NoneType'>


# DatasetDefinition

### AthenaDatasetDefinition
- **Type**: <class 'NoneType'>

### RedshiftDatasetDefinition
- **Type**: <class 'NoneType'>

### LocalPath
- **Type**: typing.Optional[str]

### DataDistributionType
- **Type**: typing.Optional[typing.Literal['FullyReplicated', 'ShardedByS3Key']]

### InputMode
- **Type**: typing.Optional[typing.Literal['File', 'Pipe']]


# DebugHookConfig

### S3OutputPath
- **Type**: <class 'str'>
- **Required**: Yes

### LocalPath
- **Type**: typing.Optional[str]

### HookParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### CollectionConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CollectionConfiguration]]


# DebugHookConfigOutput

### S3OutputPath
- **Type**: <class 'str'>
- **Required**: Yes

### LocalPath
- **Type**: typing.Optional[str]

### HookParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### CollectionConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CollectionConfigurationOutput]]


# DebugRuleConfiguration

### RuleConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### RuleEvaluatorImage
- **Type**: <class 'str'>
- **Required**: Yes

### LocalPath
- **Type**: typing.Optional[str]

### S3OutputPath
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.16xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.8xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge']]

### VolumeSizeInGB
- **Type**: typing.Optional[int]

### RuleParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# DebugRuleConfigurationOutput

### RuleConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### RuleEvaluatorImage
- **Type**: <class 'str'>
- **Required**: Yes

### LocalPath
- **Type**: typing.Optional[str]

### S3OutputPath
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.16xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.8xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge']]

### VolumeSizeInGB
- **Type**: typing.Optional[int]

### RuleParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# DebugRuleEvaluationStatus

### RuleConfigurationName
- **Type**: typing.Optional[str]

### RuleEvaluationJobArn
- **Type**: typing.Optional[str]

### RuleEvaluationStatus
- **Type**: typing.Optional[typing.Literal['Error', 'InProgress', 'IssuesFound', 'NoIssuesFound', 'Stopped', 'Stopping']]

### StatusDetails
- **Type**: typing.Optional[str]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# DefaultEbsStorageSettings

### DefaultEbsVolumeSizeInGb
- **Type**: <class 'int'>
- **Required**: Yes

### MaximumEbsVolumeSizeInGb
- **Type**: <class 'int'>
- **Required**: Yes


# DefaultSpaceSettings

### ExecutionRole
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### JupyterServerAppSettings
- **Type**: <class 'NoneType'>

### KernelGatewayAppSettings
- **Type**: <class 'NoneType'>

### JupyterLabAppSettings
- **Type**: <class 'NoneType'>

### SpaceStorageSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DefaultSpaceStorageSettings]

### CustomPosixUserConfig
- **Type**: <class 'NoneType'>

### CustomFileSystemConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CustomFileSystemConfig]]


# DefaultSpaceSettingsOutput

### ExecutionRole
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### JupyterServerAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.JupyterServerAppSettingsOutput]

### KernelGatewayAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.KernelGatewayAppSettingsOutput]

### JupyterLabAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.JupyterLabAppSettingsOutput]

### SpaceStorageSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DefaultSpaceStorageSettings]

### CustomPosixUserConfig
- **Type**: <class 'NoneType'>

### CustomFileSystemConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CustomFileSystemConfig]]


# DefaultSpaceStorageSettings

### DefaultEbsStorageSettings
- **Type**: <class 'NoneType'>


# DeleteActionRequest

### ActionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteActionResponse

### ActionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAlgorithmInput

### AlgorithmName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAppImageConfigRequest

### AppImageConfigName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAppRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### AppType
- **Type**: typing.Literal['Canvas', 'CodeEditor', 'DetailedProfiler', 'JupyterLab', 'JupyterServer', 'KernelGateway', 'RSessionGateway', 'RStudioServerPro', 'TensorBoard']
- **Required**: Yes

### AppName
- **Type**: <class 'str'>
- **Required**: Yes

### UserProfileName
- **Type**: typing.Optional[str]

### SpaceName
- **Type**: typing.Optional[str]


# DeleteArtifactRequest

### ArtifactArn
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ArtifactSource, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ArtifactSourceOutput, NoneType]


# DeleteArtifactResponse

### ArtifactArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAssociationRequest

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAssociationResponse

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteClusterRequest

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteClusterResponse

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteClusterSchedulerConfigRequest

### ClusterSchedulerConfigId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCodeRepositoryInput

### CodeRepositoryName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCompilationJobRequest

### CompilationJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteComputeQuotaRequest

### ComputeQuotaId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContextRequest

### ContextName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContextResponse

### ContextArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDataQualityJobDefinitionRequest

### JobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeviceFleetRequest

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### RetentionPolicy
- **Type**: <class 'NoneType'>


# DeleteEdgeDeploymentPlanRequest

### EdgeDeploymentPlanName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEdgeDeploymentStageRequest

### EdgeDeploymentPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### StageName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEndpointConfigInput

### EndpointConfigName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEndpointInput

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteExperimentRequest

### ExperimentName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteExperimentResponse

### ExperimentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteFeatureGroupRequest

### FeatureGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFlowDefinitionRequest

### FlowDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHubContentReferenceRequest

### HubName
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentType
- **Type**: typing.Literal['Model', 'ModelReference', 'Notebook']
- **Required**: Yes

### HubContentName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHubContentRequest

### HubName
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentType
- **Type**: typing.Literal['Model', 'ModelReference', 'Notebook']
- **Required**: Yes

### HubContentName
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentVersion
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHubRequest

### HubName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHumanTaskUiRequest

### HumanTaskUiName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHyperParameterTuningJobRequest

### HyperParameterTuningJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteImageRequest

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteImageVersionRequest

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[int]

### Alias
- **Type**: typing.Optional[str]


# DeleteInferenceComponentInput

### InferenceComponentName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInferenceExperimentRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInferenceExperimentResponse

### InferenceExperimentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteMlflowTrackingServerRequest

### TrackingServerName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMlflowTrackingServerResponse

### TrackingServerArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteModelBiasJobDefinitionRequest

### JobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteModelCardRequest

### ModelCardName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteModelExplainabilityJobDefinitionRequest

### JobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteModelInput

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteModelPackageGroupInput

### ModelPackageGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteModelPackageGroupPolicyInput

### ModelPackageGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteModelPackageInput

### ModelPackageName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteModelQualityJobDefinitionRequest

### JobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMonitoringScheduleRequest

### MonitoringScheduleName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNotebookInstanceInput

### NotebookInstanceName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNotebookInstanceLifecycleConfigInput

### NotebookInstanceLifecycleConfigName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOptimizationJobRequest

### OptimizationJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePartnerAppRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# DeletePartnerAppResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DeletePipelineRequest

### PipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePipelineResponse

### PipelineArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteProjectInput

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSpaceRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### SpaceName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStudioLifecycleConfigRequest

### StudioLifecycleConfigName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTagsInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# DeleteTrialComponentRequest

### TrialComponentName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTrialComponentResponse

### TrialComponentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteTrialRequest

### TrialName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTrialResponse

### TrialArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteUserProfileRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### UserProfileName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkforceRequest

### WorkforceName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkteamRequest

### WorkteamName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkteamResponse

### Success
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DeployedImage

### SpecifiedImage
- **Type**: typing.Optional[str]

### ResolvedImage
- **Type**: typing.Optional[str]

### ResolutionTime
- **Type**: typing.Optional[datetime.datetime]


# DeploymentConfig

### BlueGreenUpdatePolicy
- **Type**: <class 'NoneType'>

### RollingUpdatePolicy
- **Type**: <class 'NoneType'>

### AutoRollbackConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoRollbackConfig]


# DeploymentConfigOutput

### BlueGreenUpdatePolicy
- **Type**: <class 'NoneType'>

### RollingUpdatePolicy
- **Type**: <class 'NoneType'>

### AutoRollbackConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoRollbackConfigOutput]


# DeploymentRecommendation

### RecommendationStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'NOT_APPLICABLE']
- **Required**: Yes

### RealTimeInferenceRecommendations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.RealTimeInferenceRecommendation]]


# DeploymentStage

### StageName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceSelectionConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DeviceSelectionConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DeviceSelectionConfigOutput]
- **Required**: Yes

### DeploymentConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EdgeDeploymentConfig]


# DeploymentStageStatusSummary

### StageName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceSelectionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DeviceSelectionConfigOutput'>
- **Required**: Yes

### DeploymentConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EdgeDeploymentConfig'>
- **Required**: Yes

### DeploymentStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EdgeDeploymentStatus'>
- **Required**: Yes


# DeregisterDevicesRequest

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceNames
- **Type**: typing.List[str]
- **Required**: Yes


# DerivedInformation

### DerivedDataInputConfig
- **Type**: typing.Optional[str]


# DescribeActionRequest

### ActionName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeActionResponse

### ActionName
- **Type**: <class 'str'>
- **Required**: Yes

### ActionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ActionSource'>
- **Required**: Yes

### ActionType
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping', 'Unknown']
- **Required**: Yes

### Properties
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext'>
- **Required**: Yes

### MetadataProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MetadataProperties'>
- **Required**: Yes

### LineageGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAlgorithmInput

### AlgorithmName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAlgorithmOutput

### AlgorithmName
- **Type**: <class 'str'>
- **Required**: Yes

### AlgorithmArn
- **Type**: <class 'str'>
- **Required**: Yes

### AlgorithmDescription
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TrainingSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrainingSpecificationOutput'>
- **Required**: Yes

### InferenceSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceSpecificationOutput'>
- **Required**: Yes

### ValidationSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AlgorithmValidationSpecificationOutput'>
- **Required**: Yes

### AlgorithmStatus
- **Type**: typing.Literal['Completed', 'Deleting', 'Failed', 'InProgress', 'Pending']
- **Required**: Yes

### AlgorithmStatusDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AlgorithmStatusDetails'>
- **Required**: Yes

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### CertifyForMarketplace
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAppImageConfigRequest

### AppImageConfigName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAppImageConfigResponse

### AppImageConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppImageConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### KernelGatewayImageConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.KernelGatewayImageConfigOutput'>
- **Required**: Yes

### JupyterLabAppImageConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.JupyterLabAppImageConfigOutput'>
- **Required**: Yes

### CodeEditorAppImageConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CodeEditorAppImageConfigOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAppRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### AppType
- **Type**: typing.Literal['Canvas', 'CodeEditor', 'DetailedProfiler', 'JupyterLab', 'JupyterServer', 'KernelGateway', 'RSessionGateway', 'RStudioServerPro', 'TensorBoard']
- **Required**: Yes

### AppName
- **Type**: <class 'str'>
- **Required**: Yes

### UserProfileName
- **Type**: typing.Optional[str]

### SpaceName
- **Type**: typing.Optional[str]


# DescribeAppResponse

### AppArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppType
- **Type**: typing.Literal['Canvas', 'CodeEditor', 'DetailedProfiler', 'JupyterLab', 'JupyterServer', 'KernelGateway', 'RSessionGateway', 'RStudioServerPro', 'TensorBoard']
- **Required**: Yes

### AppName
- **Type**: <class 'str'>
- **Required**: Yes

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### UserProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### SpaceName
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Deleted', 'Deleting', 'Failed', 'InService', 'Pending']
- **Required**: Yes

### LastHealthCheckTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUserActivityTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSpec
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResourceSpec'>
- **Required**: Yes

### BuiltInLifecycleConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeArtifactRequest

### ArtifactArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeArtifactResponse

### ArtifactName
- **Type**: <class 'str'>
- **Required**: Yes

### ArtifactArn
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ArtifactSourceOutput'>
- **Required**: Yes

### ArtifactType
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext'>
- **Required**: Yes

### MetadataProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MetadataProperties'>
- **Required**: Yes

### LineageGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAutoMLJobRequest

### AutoMLJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAutoMLJobResponse

### AutoMLJobName
- **Type**: <class 'str'>
- **Required**: Yes

### AutoMLJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### InputDataConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLChannel]
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLOutputDataConfig'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### AutoMLJobObjective
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLJobObjective'>
- **Required**: Yes

### ProblemType
- **Type**: typing.Literal['BinaryClassification', 'MulticlassClassification', 'Regression']
- **Required**: Yes

### AutoMLJobConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLJobConfigOutput'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### PartialFailureReasons
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLPartialFailureReason]
- **Required**: Yes

### BestCandidate
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLCandidate'>
- **Required**: Yes

### AutoMLJobStatus
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']
- **Required**: Yes

### AutoMLJobSecondaryStatus
- **Type**: typing.Literal['AnalyzingData', 'CandidateDefinitionsGenerated', 'Completed', 'DeployingModel', 'ExplainabilityError', 'Failed', 'FeatureEngineering', 'GeneratingExplainabilityReport', 'GeneratingModelInsightsReport', 'MaxAutoMLJobRuntimeReached', 'MaxCandidatesReached', 'ModelDeploymentError', 'ModelInsightsError', 'ModelTuning', 'PreTraining', 'Starting', 'Stopped', 'Stopping', 'TrainingModels']
- **Required**: Yes

### GenerateCandidateDefinitionsOnly
- **Type**: <class 'bool'>
- **Required**: Yes

### AutoMLJobArtifacts
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLJobArtifacts'>
- **Required**: Yes

### ResolvedAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResolvedAttributes'>
- **Required**: Yes

### ModelDeployConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelDeployConfig'>
- **Required**: Yes

### ModelDeployResult
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelDeployResult'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAutoMLJobV2Request

### AutoMLJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAutoMLJobV2Response

### AutoMLJobName
- **Type**: <class 'str'>
- **Required**: Yes

### AutoMLJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### AutoMLJobInputDataConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLJobChannel]
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLOutputDataConfig'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### AutoMLJobObjective
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLJobObjective'>
- **Required**: Yes

### AutoMLProblemTypeConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLProblemTypeConfigOutput'>
- **Required**: Yes

### AutoMLProblemTypeConfigName
- **Type**: typing.Literal['ImageClassification', 'Tabular', 'TextClassification', 'TextGeneration', 'TimeSeriesForecasting']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### PartialFailureReasons
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLPartialFailureReason]
- **Required**: Yes

### BestCandidate
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLCandidate'>
- **Required**: Yes

### AutoMLJobStatus
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']
- **Required**: Yes

### AutoMLJobSecondaryStatus
- **Type**: typing.Literal['AnalyzingData', 'CandidateDefinitionsGenerated', 'Completed', 'DeployingModel', 'ExplainabilityError', 'Failed', 'FeatureEngineering', 'GeneratingExplainabilityReport', 'GeneratingModelInsightsReport', 'MaxAutoMLJobRuntimeReached', 'MaxCandidatesReached', 'ModelDeploymentError', 'ModelInsightsError', 'ModelTuning', 'PreTraining', 'Starting', 'Stopped', 'Stopping', 'TrainingModels']
- **Required**: Yes

### AutoMLJobArtifacts
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLJobArtifacts'>
- **Required**: Yes

### ResolvedAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLResolvedAttributes'>
- **Required**: Yes

### ModelDeployConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelDeployConfig'>
- **Required**: Yes

### ModelDeployResult
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelDeployResult'>
- **Required**: Yes

### DataSplitConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLDataSplitConfig'>
- **Required**: Yes

### SecurityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLSecurityConfigOutput'>
- **Required**: Yes

### AutoMLComputeConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLComputeConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeClusterNodeRequest

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### NodeId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeClusterNodeResponse

### NodeDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ClusterNodeDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeClusterRequest

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeClusterResponse

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterStatus
- **Type**: typing.Literal['Creating', 'Deleting', 'Failed', 'InService', 'RollingBack', 'SystemUpdating', 'Updating']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureMessage
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ClusterInstanceGroupDetails]
- **Required**: Yes

### VpcConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.VpcConfigOutput'>
- **Required**: Yes

### Orchestrator
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ClusterOrchestrator'>
- **Required**: Yes

### NodeRecovery
- **Type**: typing.Literal['Automatic', 'None']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeClusterSchedulerConfigRequest

### ClusterSchedulerConfigId
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterSchedulerConfigVersion
- **Type**: typing.Optional[int]


# DescribeClusterSchedulerConfigResponse

### ClusterSchedulerConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterSchedulerConfigId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterSchedulerConfigVersion
- **Type**: <class 'int'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CreateFailed', 'CreateRollbackFailed', 'Created', 'Creating', 'DeleteFailed', 'DeleteRollbackFailed', 'Deleted', 'Deleting', 'UpdateFailed', 'UpdateRollbackFailed', 'Updated', 'Updating']
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### SchedulerConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SchedulerConfigOutput'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCodeRepositoryInput

### CodeRepositoryName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCodeRepositoryOutput

### CodeRepositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### CodeRepositoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### GitConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.GitConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCompilationJobRequest

### CompilationJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCompilationJobResponse

### CompilationJobName
- **Type**: <class 'str'>
- **Required**: Yes

### CompilationJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### CompilationJobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'INPROGRESS', 'STARTING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### CompilationStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CompilationEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### StoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.StoppingCondition'>
- **Required**: Yes

### InferenceImage
- **Type**: <class 'str'>
- **Required**: Yes

### ModelPackageVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### ModelArtifacts
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelArtifacts'>
- **Required**: Yes

### ModelDigests
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelDigests'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### InputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InputConfig'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OutputConfig'>
- **Required**: Yes

### VpcConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.NeoVpcConfigOutput'>
- **Required**: Yes

### DerivedInformation
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DerivedInformation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeComputeQuotaRequest

### ComputeQuotaId
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeQuotaVersion
- **Type**: typing.Optional[int]


# DescribeComputeQuotaResponse

### ComputeQuotaArn
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeQuotaId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeQuotaVersion
- **Type**: <class 'int'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CreateFailed', 'CreateRollbackFailed', 'Created', 'Creating', 'DeleteFailed', 'DeleteRollbackFailed', 'Deleted', 'Deleting', 'UpdateFailed', 'UpdateRollbackFailed', 'Updated', 'Updating']
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeQuotaConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ComputeQuotaConfigOutput'>
- **Required**: Yes

### ComputeQuotaTarget
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ComputeQuotaTarget'>
- **Required**: Yes

### ActivationState
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeContextRequest

### ContextName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeContextResponse

### ContextName
- **Type**: <class 'str'>
- **Required**: Yes

### ContextArn
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ContextSource'>
- **Required**: Yes

### ContextType
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext'>
- **Required**: Yes

### LineageGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDataQualityJobDefinitionRequest

### JobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDataQualityJobDefinitionResponse

### JobDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### JobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DataQualityBaselineConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DataQualityBaselineConfig'>
- **Required**: Yes

### DataQualityAppSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DataQualityAppSpecificationOutput'>
- **Required**: Yes

### DataQualityJobInput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DataQualityJobInputOutput'>
- **Required**: Yes

### DataQualityJobOutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringOutputConfigOutput'>
- **Required**: Yes

### JobResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringResources'>
- **Required**: Yes

### NetworkConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringNetworkConfigOutput'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### StoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringStoppingCondition'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDeviceFleetRequest

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDeviceFleetResponse

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceFleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EdgeOutputConfig'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### IotRoleAlias
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDeviceRequest

### DeviceName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeDeviceResponse

### DeviceArn
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes

### IotThingName
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LatestHeartbeat
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Models
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EdgeModel]
- **Required**: Yes

### MaxModels
- **Type**: <class 'int'>
- **Required**: Yes

### AgentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeDomainRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDomainResponse

### DomainArn
- **Type**: <class 'str'>
- **Required**: Yes

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### HomeEfsFileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### SingleSignOnManagedApplicationInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SingleSignOnApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Delete_Failed', 'Deleting', 'Failed', 'InService', 'Pending', 'Update_Failed', 'Updating']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroupIdForDomainBoundary
- **Type**: <class 'str'>
- **Required**: Yes

### AuthMode
- **Type**: typing.Literal['IAM', 'SSO']
- **Required**: Yes

### DefaultUserSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserSettingsOutput'>
- **Required**: Yes

### DomainSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DomainSettingsOutput'>
- **Required**: Yes

### AppNetworkAccessType
- **Type**: typing.Literal['PublicInternetOnly', 'VpcOnly']
- **Required**: Yes

### HomeEfsFileSystemKmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### AppSecurityGroupManagement
- **Type**: typing.Literal['Customer', 'Service']
- **Required**: Yes

### TagPropagation
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### DefaultSpaceSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DefaultSpaceSettingsOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEdgeDeploymentPlanRequest

### EdgeDeploymentPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeEdgeDeploymentPlanResponse

### EdgeDeploymentPlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### EdgeDeploymentPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EdgeDeploymentModelConfig]
- **Required**: Yes

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes

### EdgeDeploymentSuccess
- **Type**: <class 'int'>
- **Required**: Yes

### EdgeDeploymentPending
- **Type**: <class 'int'>
- **Required**: Yes

### EdgeDeploymentFailed
- **Type**: <class 'int'>
- **Required**: Yes

### Stages
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DeploymentStageStatusSummary]
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeEdgePackagingJobRequest

### EdgePackagingJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEdgePackagingJobResponse

### EdgePackagingJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### EdgePackagingJobName
- **Type**: <class 'str'>
- **Required**: Yes

### CompilationJobName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EdgeOutputConfig'>
- **Required**: Yes

### ResourceKey
- **Type**: <class 'str'>
- **Required**: Yes

### EdgePackagingJobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'INPROGRESS', 'STARTING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### EdgePackagingJobStatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ModelArtifact
- **Type**: <class 'str'>
- **Required**: Yes

### ModelSignature
- **Type**: <class 'str'>
- **Required**: Yes

### PresetDeploymentOutput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EdgePresetDeploymentOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEndpointConfigInput

### EndpointConfigName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEndpointConfigOutput

### EndpointConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProductionVariants
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProductionVariant]
- **Required**: Yes

### DataCaptureConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DataCaptureConfigOutput'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AsyncInferenceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AsyncInferenceConfigOutput'>
- **Required**: Yes

### ExplainerConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ExplainerConfigOutput'>
- **Required**: Yes

### ShadowProductionVariants
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProductionVariant]
- **Required**: Yes

### ExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### VpcConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.VpcConfigOutput'>
- **Required**: Yes

### EnableNetworkIsolation
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEndpointInput

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEndpointInputWait

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeEndpointInputWaitExtra

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeEndpointOutput

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### ProductionVariants
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProductionVariantSummary]
- **Required**: Yes

### DataCaptureConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DataCaptureConfigSummary'>
- **Required**: Yes

### EndpointStatus
- **Type**: typing.Literal['Creating', 'Deleting', 'Failed', 'InService', 'OutOfService', 'RollingBack', 'SystemUpdating', 'UpdateRollbackFailed', 'Updating']
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastDeploymentConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DeploymentConfigOutput'>
- **Required**: Yes

### AsyncInferenceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AsyncInferenceConfigOutput'>
- **Required**: Yes

### PendingDeploymentSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PendingDeploymentSummary'>
- **Required**: Yes

### ExplainerConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ExplainerConfigOutput'>
- **Required**: Yes

### ShadowProductionVariants
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProductionVariantSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeExperimentRequest

### ExperimentName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeExperimentResponse

### ExperimentName
- **Type**: <class 'str'>
- **Required**: Yes

### ExperimentArn
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ExperimentSource'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFeatureGroupRequest

### FeatureGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeFeatureGroupResponse

### FeatureGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### RecordIdentifierFeatureName
- **Type**: <class 'str'>
- **Required**: Yes

### EventTimeFeatureName
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.FeatureDefinition]
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### OnlineStoreConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OnlineStoreConfig'>
- **Required**: Yes

### OfflineStoreConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OfflineStoreConfig'>
- **Required**: Yes

### ThroughputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ThroughputConfigDescription'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureGroupStatus
- **Type**: typing.Literal['CreateFailed', 'Created', 'Creating', 'DeleteFailed', 'Deleting']
- **Required**: Yes

### OfflineStoreStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OfflineStoreStatus'>
- **Required**: Yes

### LastUpdateStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.LastUpdateStatus'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### OnlineStoreTotalSizeBytes
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFeatureMetadataRequest

### FeatureGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFeatureMetadataResponse

### FeatureGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureName
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureType
- **Type**: typing.Literal['Fractional', 'Integral', 'String']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.FeatureParameter]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFlowDefinitionRequest

### FlowDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFlowDefinitionResponse

### FlowDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### FlowDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### FlowDefinitionStatus
- **Type**: typing.Literal['Active', 'Deleting', 'Failed', 'Initializing']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### HumanLoopRequestSource
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HumanLoopRequestSource'>
- **Required**: Yes

### HumanLoopActivationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HumanLoopActivationConfig'>
- **Required**: Yes

### HumanLoopConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HumanLoopConfigOutput'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.FlowDefinitionOutputConfig'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeHubContentRequest

### HubName
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentType
- **Type**: typing.Literal['Model', 'ModelReference', 'Notebook']
- **Required**: Yes

### HubContentName
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentVersion
- **Type**: typing.Optional[str]


# DescribeHubContentResponse

### HubContentName
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentArn
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentType
- **Type**: typing.Literal['Model', 'ModelReference', 'Notebook']
- **Required**: Yes

### DocumentSchemaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### HubName
- **Type**: <class 'str'>
- **Required**: Yes

### HubArn
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentDisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentDescription
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentMarkdown
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentDocument
- **Type**: <class 'str'>
- **Required**: Yes

### SageMakerPublicHubContentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ReferenceMinVersion
- **Type**: <class 'str'>
- **Required**: Yes

### SupportStatus
- **Type**: typing.Literal['Deprecated', 'Restricted', 'Supported']
- **Required**: Yes

### HubContentSearchKeywords
- **Type**: typing.List[str]
- **Required**: Yes

### HubContentDependencies
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HubContentDependency]
- **Required**: Yes

### HubContentStatus
- **Type**: typing.Literal['Available', 'DeleteFailed', 'Deleting', 'ImportFailed', 'Importing']
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeHubRequest

### HubName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeHubResponse

### HubName
- **Type**: <class 'str'>
- **Required**: Yes

### HubArn
- **Type**: <class 'str'>
- **Required**: Yes

### HubDisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### HubDescription
- **Type**: <class 'str'>
- **Required**: Yes

### HubSearchKeywords
- **Type**: typing.List[str]
- **Required**: Yes

### S3StorageConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HubS3StorageConfig'>
- **Required**: Yes

### HubStatus
- **Type**: typing.Literal['CreateFailed', 'Creating', 'DeleteFailed', 'Deleting', 'InService', 'UpdateFailed', 'Updating']
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeHumanTaskUiRequest

### HumanTaskUiName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeHumanTaskUiResponse

### HumanTaskUiArn
- **Type**: <class 'str'>
- **Required**: Yes

### HumanTaskUiName
- **Type**: <class 'str'>
- **Required**: Yes

### HumanTaskUiStatus
- **Type**: typing.Literal['Active', 'Deleting']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UiTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UiTemplateInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeHyperParameterTuningJobRequest

### HyperParameterTuningJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeHyperParameterTuningJobResponse

### HyperParameterTuningJobName
- **Type**: <class 'str'>
- **Required**: Yes

### HyperParameterTuningJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### HyperParameterTuningJobConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTuningJobConfigOutput'>
- **Required**: Yes

### TrainingJobDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTrainingJobDefinitionOutput'>
- **Required**: Yes

### TrainingJobDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTrainingJobDefinitionOutput]
- **Required**: Yes

### HyperParameterTuningJobStatus
- **Type**: typing.Literal['Completed', 'DeleteFailed', 'Deleting', 'Failed', 'InProgress', 'Stopped', 'Stopping']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### HyperParameterTuningEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TrainingJobStatusCounters
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrainingJobStatusCounters'>
- **Required**: Yes

### ObjectiveStatusCounters
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ObjectiveStatusCounters'>
- **Required**: Yes

### BestTrainingJob
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTrainingJobSummary'>
- **Required**: Yes

### OverallBestTrainingJob
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTrainingJobSummary'>
- **Required**: Yes

### WarmStartConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTuningJobWarmStartConfigOutput'>
- **Required**: Yes

### Autotune
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Autotune'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### TuningJobCompletionDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTuningJobCompletionDetails'>
- **Required**: Yes

### ConsumedResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTuningJobConsumedResources'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeImageRequest

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeImageRequestWait

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeImageRequestWaitExtra

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeImageRequestWaitExtraExtra

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeImageResponse

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### ImageArn
- **Type**: <class 'str'>
- **Required**: Yes

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### ImageStatus
- **Type**: typing.Literal['CREATED', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeImageVersionRequest

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[int]

### Alias
- **Type**: typing.Optional[str]


# DescribeImageVersionRequestWait

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[int]

### Alias
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeImageVersionRequestWaitExtra

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[int]

### Alias
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeImageVersionResponse

### BaseImage
- **Type**: <class 'str'>
- **Required**: Yes

### ContainerImage
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### ImageArn
- **Type**: <class 'str'>
- **Required**: Yes

### ImageVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ImageVersionStatus
- **Type**: typing.Literal['CREATED', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING']
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Version
- **Type**: <class 'int'>
- **Required**: Yes

### VendorGuidance
- **Type**: typing.Literal['ARCHIVED', 'NOT_PROVIDED', 'STABLE', 'TO_BE_ARCHIVED']
- **Required**: Yes

### JobType
- **Type**: typing.Literal['INFERENCE', 'NOTEBOOK_KERNEL', 'TRAINING']
- **Required**: Yes

### MLFramework
- **Type**: <class 'str'>
- **Required**: Yes

### ProgrammingLang
- **Type**: <class 'str'>
- **Required**: Yes

### Processor
- **Type**: typing.Literal['CPU', 'GPU']
- **Required**: Yes

### Horovod
- **Type**: <class 'bool'>
- **Required**: Yes

### ReleaseNotes
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeInferenceComponentInput

### InferenceComponentName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeInferenceComponentOutput

### InferenceComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### InferenceComponentArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### VariantName
- **Type**: <class 'str'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### Specification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceComponentSpecificationSummary'>
- **Required**: Yes

### RuntimeConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceComponentRuntimeConfigSummary'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### InferenceComponentStatus
- **Type**: typing.Literal['Creating', 'Deleting', 'Failed', 'InService', 'Updating']
- **Required**: Yes

### LastDeploymentConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceComponentDeploymentConfigOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeInferenceExperimentRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeInferenceExperimentResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['ShadowMode']
- **Required**: Yes

### Schedule
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceExperimentScheduleOutput'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Cancelled', 'Completed', 'Created', 'Creating', 'Running', 'Starting', 'Stopping', 'Updating']
- **Required**: Yes

### StatusReason
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CompletionTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EndpointMetadata'>
- **Required**: Yes

### ModelVariants
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelVariantConfigSummary]
- **Required**: Yes

### DataStorageConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceExperimentDataStorageConfigOutput'>
- **Required**: Yes

### ShadowModeConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ShadowModeConfigOutput'>
- **Required**: Yes

### KmsKey
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeInferenceRecommendationsJobRequest

### JobName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeInferenceRecommendationsJobResponse

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### JobDescription
- **Type**: <class 'str'>
- **Required**: Yes

### JobType
- **Type**: typing.Literal['Advanced', 'Default']
- **Required**: Yes

### JobArn
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'DELETED', 'DELETING', 'FAILED', 'IN_PROGRESS', 'PENDING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CompletionTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### InputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.RecommendationJobInputConfigOutput'>
- **Required**: Yes

### StoppingConditions
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.RecommendationJobStoppingConditionsOutput'>
- **Required**: Yes

### InferenceRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceRecommendation]
- **Required**: Yes

### EndpointPerformances
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EndpointPerformance]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLabelingJobRequest

### LabelingJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLabelingJobResponse

### LabelingJobStatus
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Initializing', 'Stopped', 'Stopping']
- **Required**: Yes

### LabelCounters
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.LabelCounters'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### JobReferenceCode
- **Type**: <class 'str'>
- **Required**: Yes

### LabelingJobName
- **Type**: <class 'str'>
- **Required**: Yes

### LabelingJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### LabelAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### InputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.LabelingJobInputConfigOutput'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.LabelingJobOutputConfig'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### LabelCategoryConfigS3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### StoppingConditions
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.LabelingJobStoppingConditions'>
- **Required**: Yes

### LabelingJobAlgorithmsConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.LabelingJobAlgorithmsConfigOutput'>
- **Required**: Yes

### HumanTaskConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HumanTaskConfigOutput'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]
- **Required**: Yes

### LabelingJobOutput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.LabelingJobOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLineageGroupRequest

### LineageGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLineageGroupResponse

### LineageGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### LineageGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeMlflowTrackingServerRequest

### TrackingServerName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMlflowTrackingServerResponse

### TrackingServerArn
- **Type**: <class 'str'>
- **Required**: Yes

### TrackingServerName
- **Type**: <class 'str'>
- **Required**: Yes

### ArtifactStoreUri
- **Type**: <class 'str'>
- **Required**: Yes

### TrackingServerSize
- **Type**: typing.Literal['Large', 'Medium', 'Small']
- **Required**: Yes

### MlflowVersion
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### TrackingServerStatus
- **Type**: typing.Literal['CreateFailed', 'Created', 'Creating', 'DeleteFailed', 'Deleting', 'MaintenanceComplete', 'MaintenanceFailed', 'MaintenanceInProgress', 'StartFailed', 'Started', 'Starting', 'StopFailed', 'Stopped', 'Stopping', 'UpdateFailed', 'Updated', 'Updating']
- **Required**: Yes

### IsActive
- **Type**: typing.Literal['Active', 'Inactive']
- **Required**: Yes

### TrackingServerUrl
- **Type**: <class 'str'>
- **Required**: Yes

### WeeklyMaintenanceWindowStart
- **Type**: <class 'str'>
- **Required**: Yes

### AutomaticModelRegistration
- **Type**: <class 'bool'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeModelBiasJobDefinitionRequest

### JobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeModelBiasJobDefinitionResponse

### JobDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### JobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ModelBiasBaselineConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelBiasBaselineConfig'>
- **Required**: Yes

### ModelBiasAppSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelBiasAppSpecificationOutput'>
- **Required**: Yes

### ModelBiasJobInput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelBiasJobInputOutput'>
- **Required**: Yes

### ModelBiasJobOutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringOutputConfigOutput'>
- **Required**: Yes

### JobResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringResources'>
- **Required**: Yes

### NetworkConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringNetworkConfigOutput'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### StoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringStoppingCondition'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeModelCardExportJobRequest

### ModelCardExportJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeModelCardExportJobResponse

### ModelCardExportJobName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelCardExportJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress']
- **Required**: Yes

### ModelCardName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelCardVersion
- **Type**: <class 'int'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelCardExportOutputConfig'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### ExportArtifacts
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelCardExportArtifacts'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeModelCardRequest

### ModelCardName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelCardVersion
- **Type**: typing.Optional[int]


# DescribeModelCardResponse

### ModelCardArn
- **Type**: <class 'str'>
- **Required**: Yes

### ModelCardName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelCardVersion
- **Type**: <class 'int'>
- **Required**: Yes

### Content
- **Type**: <class 'str'>
- **Required**: Yes

### ModelCardStatus
- **Type**: typing.Literal['Approved', 'Archived', 'Draft', 'PendingReview']
- **Required**: Yes

### SecurityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelCardSecurityConfig'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext'>
- **Required**: Yes

### ModelCardProcessingStatus
- **Type**: typing.Literal['ContentDeleted', 'DeleteCompleted', 'DeleteFailed', 'DeleteInProgress', 'DeletePending', 'ExportJobsDeleted']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeModelExplainabilityJobDefinitionRequest

### JobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeModelExplainabilityJobDefinitionResponse

### JobDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### JobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ModelExplainabilityBaselineConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelExplainabilityBaselineConfig'>
- **Required**: Yes

### ModelExplainabilityAppSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelExplainabilityAppSpecificationOutput'>
- **Required**: Yes

### ModelExplainabilityJobInput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelExplainabilityJobInputOutput'>
- **Required**: Yes

### ModelExplainabilityJobOutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringOutputConfigOutput'>
- **Required**: Yes

### JobResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringResources'>
- **Required**: Yes

### NetworkConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringNetworkConfigOutput'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### StoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringStoppingCondition'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeModelInput

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeModelOutput

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### PrimaryContainer
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ContainerDefinitionOutput'>
- **Required**: Yes

### Containers
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ContainerDefinitionOutput]
- **Required**: Yes

### InferenceExecutionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceExecutionConfig'>
- **Required**: Yes

### ExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### VpcConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.VpcConfigOutput'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### EnableNetworkIsolation
- **Type**: <class 'bool'>
- **Required**: Yes

### DeploymentRecommendation
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DeploymentRecommendation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeModelPackageGroupInput

### ModelPackageGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeModelPackageGroupOutput

### ModelPackageGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelPackageGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ModelPackageGroupDescription
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext'>
- **Required**: Yes

### ModelPackageGroupStatus
- **Type**: typing.Literal['Completed', 'DeleteFailed', 'Deleting', 'Failed', 'InProgress', 'Pending']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeModelPackageInput

### ModelPackageName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeModelPackageOutput

### ModelPackageName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelPackageGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelPackageVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ModelPackageArn
- **Type**: <class 'str'>
- **Required**: Yes

### ModelPackageDescription
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### InferenceSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceSpecificationOutput'>
- **Required**: Yes

### SourceAlgorithmSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SourceAlgorithmSpecificationOutput'>
- **Required**: Yes

### ValidationSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelPackageValidationSpecificationOutput'>
- **Required**: Yes

### ModelPackageStatus
- **Type**: typing.Literal['Completed', 'Deleting', 'Failed', 'InProgress', 'Pending']
- **Required**: Yes

### ModelPackageStatusDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelPackageStatusDetails'>
- **Required**: Yes

### CertifyForMarketplace
- **Type**: <class 'bool'>
- **Required**: Yes

### ModelApprovalStatus
- **Type**: typing.Literal['Approved', 'PendingManualApproval', 'Rejected']
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext'>
- **Required**: Yes

### MetadataProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MetadataProperties'>
- **Required**: Yes

### ModelMetrics
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelMetrics'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext'>
- **Required**: Yes

### ApprovalDescription
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### Task
- **Type**: <class 'str'>
- **Required**: Yes

### SamplePayloadUrl
- **Type**: <class 'str'>
- **Required**: Yes

### CustomerMetadataProperties
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### DriftCheckBaselines
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DriftCheckBaselines'>
- **Required**: Yes

### AdditionalInferenceSpecifications
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AdditionalInferenceSpecificationDefinitionOutput]
- **Required**: Yes

### SkipModelValidation
- **Type**: typing.Literal['All', 'None']
- **Required**: Yes

### SourceUri
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelPackageSecurityConfig'>
- **Required**: Yes

### ModelCard
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelPackageModelCard'>
- **Required**: Yes

### ModelLifeCycle
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelLifeCycle'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeModelQualityJobDefinitionRequest

### JobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeModelQualityJobDefinitionResponse

### JobDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### JobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ModelQualityBaselineConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelQualityBaselineConfig'>
- **Required**: Yes

### ModelQualityAppSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelQualityAppSpecificationOutput'>
- **Required**: Yes

### ModelQualityJobInput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelQualityJobInputOutput'>
- **Required**: Yes

### ModelQualityJobOutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringOutputConfigOutput'>
- **Required**: Yes

### JobResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringResources'>
- **Required**: Yes

### NetworkConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringNetworkConfigOutput'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### StoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringStoppingCondition'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeMonitoringScheduleRequest

### MonitoringScheduleName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMonitoringScheduleResponse

### MonitoringScheduleArn
- **Type**: <class 'str'>
- **Required**: Yes

### MonitoringScheduleName
- **Type**: <class 'str'>
- **Required**: Yes

### MonitoringScheduleStatus
- **Type**: typing.Literal['Failed', 'Pending', 'Scheduled', 'Stopped']
- **Required**: Yes

### MonitoringType
- **Type**: typing.Literal['DataQuality', 'ModelBias', 'ModelExplainability', 'ModelQuality']
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### MonitoringScheduleConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringScheduleConfigOutput'>
- **Required**: Yes

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### LastMonitoringExecutionSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringExecutionSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeNotebookInstanceInput

### NotebookInstanceName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeNotebookInstanceInputWait

### NotebookInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeNotebookInstanceInputWaitExtra

### NotebookInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeNotebookInstanceInputWaitExtraExtra

### NotebookInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeNotebookInstanceLifecycleConfigInput

### NotebookInstanceLifecycleConfigName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeNotebookInstanceLifecycleConfigOutput

### NotebookInstanceLifecycleConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### NotebookInstanceLifecycleConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### OnCreate
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.NotebookInstanceLifecycleHook]
- **Required**: Yes

### OnStart
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.NotebookInstanceLifecycleHook]
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeNotebookInstanceOutput

### NotebookInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### NotebookInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### NotebookInstanceStatus
- **Type**: typing.Literal['Deleting', 'Failed', 'InService', 'Pending', 'Stopped', 'Stopping', 'Updating']
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceType
- **Type**: typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c5d.18xlarge', 'ml.c5d.2xlarge', 'ml.c5d.4xlarge', 'ml.c5d.9xlarge', 'ml.c5d.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c6id.12xlarge', 'ml.c6id.16xlarge', 'ml.c6id.24xlarge', 'ml.c6id.2xlarge', 'ml.c6id.32xlarge', 'ml.c6id.4xlarge', 'ml.c6id.8xlarge', 'ml.c6id.large', 'ml.c6id.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.inf1.24xlarge', 'ml.inf1.2xlarge', 'ml.inf1.6xlarge', 'ml.inf1.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.16xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.8xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m6id.12xlarge', 'ml.m6id.16xlarge', 'ml.m6id.24xlarge', 'ml.m6id.2xlarge', 'ml.m6id.32xlarge', 'ml.m6id.4xlarge', 'ml.m6id.8xlarge', 'ml.m6id.large', 'ml.m6id.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r6id.12xlarge', 'ml.r6id.16xlarge', 'ml.r6id.24xlarge', 'ml.r6id.2xlarge', 'ml.r6id.32xlarge', 'ml.r6id.4xlarge', 'ml.r6id.8xlarge', 'ml.r6id.large', 'ml.r6id.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.t2.2xlarge', 'ml.t2.large', 'ml.t2.medium', 'ml.t2.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge']
- **Required**: Yes

### SubnetId
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroups
- **Type**: typing.List[str]
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkInterfaceId
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### NotebookInstanceLifecycleConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### DirectInternetAccess
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### VolumeSizeInGB
- **Type**: <class 'int'>
- **Required**: Yes

### AcceleratorTypes
- **Type**: typing.List[typing.Literal['ml.eia1.large', 'ml.eia1.medium', 'ml.eia1.xlarge', 'ml.eia2.large', 'ml.eia2.medium', 'ml.eia2.xlarge']]
- **Required**: Yes

### DefaultCodeRepository
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalCodeRepositories
- **Type**: typing.List[str]
- **Required**: Yes

### RootAccess
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### PlatformIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceMetadataServiceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InstanceMetadataServiceConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeOptimizationJobRequest

### OptimizationJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeOptimizationJobResponse

### OptimizationJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### OptimizationJobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'INPROGRESS', 'STARTING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### OptimizationStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### OptimizationEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### OptimizationJobName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelSource
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OptimizationJobModelSource'>
- **Required**: Yes

### OptimizationEnvironment
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### DeploymentInstanceType
- **Type**: typing.Literal['ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge']
- **Required**: Yes

### OptimizationConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OptimizationConfigOutput]
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OptimizationJobOutputConfig'>
- **Required**: Yes

### OptimizationOutput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OptimizationOutput'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### StoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.StoppingCondition'>
- **Required**: Yes

### VpcConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OptimizationVpcConfigOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePartnerAppRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePartnerAppResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['comet', 'deepchecks-llm-evaluation', 'fiddler', 'lakera-guard']
- **Required**: Yes

### Status
- **Type**: typing.Literal['Available', 'Creating', 'Deleted', 'Deleting', 'Failed', 'UpdateFailed', 'Updating']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### BaseUrl
- **Type**: <class 'str'>
- **Required**: Yes

### MaintenanceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PartnerAppMaintenanceConfig'>
- **Required**: Yes

### Tier
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PartnerAppConfigOutput'>
- **Required**: Yes

### AuthType
- **Type**: typing.Literal['IAM']
- **Required**: Yes

### EnableIamSessionBasedIdentity
- **Type**: <class 'bool'>
- **Required**: Yes

### Error
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ErrorInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePipelineDefinitionForExecutionRequest

### PipelineExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePipelineDefinitionForExecutionResponse

### PipelineDefinition
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePipelineExecutionRequest

### PipelineExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePipelineExecutionResponse

### PipelineArn
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineExecutionDisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineExecutionStatus
- **Type**: typing.Literal['Executing', 'Failed', 'Stopped', 'Stopping', 'Succeeded']
- **Required**: Yes

### PipelineExecutionDescription
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineExperimentConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PipelineExperimentConfig'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext'>
- **Required**: Yes

### ParallelismConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ParallelismConfiguration'>
- **Required**: Yes

### SelectiveExecutionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SelectiveExecutionConfigOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePipelineRequest

### PipelineName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePipelineResponse

### PipelineArn
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineDisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineDefinition
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineDescription
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineStatus
- **Type**: typing.Literal['Active', 'Deleting']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastRunTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext'>
- **Required**: Yes

### ParallelismConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ParallelismConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeProcessingJobRequest

### ProcessingJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeProcessingJobRequestWait

### ProcessingJobName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeProcessingJobResponse

### ProcessingInputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProcessingInput]
- **Required**: Yes

### ProcessingOutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProcessingOutputConfigOutput'>
- **Required**: Yes

### ProcessingJobName
- **Type**: <class 'str'>
- **Required**: Yes

### ProcessingResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProcessingResources'>
- **Required**: Yes

### StoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProcessingStoppingCondition'>
- **Required**: Yes

### AppSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AppSpecificationOutput'>
- **Required**: Yes

### Environment
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### NetworkConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.NetworkConfigOutput'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExperimentConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ExperimentConfig'>
- **Required**: Yes

### ProcessingJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProcessingJobStatus
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']
- **Required**: Yes

### ExitMessage
- **Type**: <class 'str'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### ProcessingEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ProcessingStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### MonitoringScheduleArn
- **Type**: <class 'str'>
- **Required**: Yes

### AutoMLJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### TrainingJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeProjectInput

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeProjectOutput

### ProjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### ProjectId
- **Type**: <class 'str'>
- **Required**: Yes

### ProjectDescription
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceCatalogProvisioningDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ServiceCatalogProvisioningDetailsOutput'>
- **Required**: Yes

### ServiceCatalogProvisionedProductDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ServiceCatalogProvisionedProductDetails'>
- **Required**: Yes

### ProjectStatus
- **Type**: typing.Literal['CreateCompleted', 'CreateFailed', 'CreateInProgress', 'DeleteCompleted', 'DeleteFailed', 'DeleteInProgress', 'Pending', 'UpdateCompleted', 'UpdateFailed', 'UpdateInProgress']
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSpaceRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### SpaceName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSpaceResponse

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### SpaceArn
- **Type**: <class 'str'>
- **Required**: Yes

### SpaceName
- **Type**: <class 'str'>
- **Required**: Yes

### HomeEfsFileSystemUid
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Delete_Failed', 'Deleting', 'Failed', 'InService', 'Pending', 'Update_Failed', 'Updating']
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### SpaceSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SpaceSettingsOutput'>
- **Required**: Yes

### OwnershipSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OwnershipSettings'>
- **Required**: Yes

### SpaceSharingSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SpaceSharingSettings'>
- **Required**: Yes

### SpaceDisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeStudioLifecycleConfigRequest

### StudioLifecycleConfigName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeStudioLifecycleConfigResponse

### StudioLifecycleConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### StudioLifecycleConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### StudioLifecycleConfigContent
- **Type**: <class 'str'>
- **Required**: Yes

### StudioLifecycleConfigAppType
- **Type**: typing.Literal['CodeEditor', 'JupyterLab', 'JupyterServer', 'KernelGateway']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSubscribedWorkteamRequest

### WorkteamArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSubscribedWorkteamResponse

### SubscribedWorkteam
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SubscribedWorkteam'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTrainingJobRequest

### TrainingJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTrainingJobRequestWait

### TrainingJobName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeTrainingJobResponse

### TrainingJobName
- **Type**: <class 'str'>
- **Required**: Yes

### TrainingJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### TuningJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### LabelingJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### AutoMLJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ModelArtifacts
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelArtifacts'>
- **Required**: Yes

### TrainingJobStatus
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']
- **Required**: Yes

### SecondaryStatus
- **Type**: typing.Literal['Completed', 'Downloading', 'DownloadingTrainingImage', 'Failed', 'Interrupted', 'LaunchingMLInstances', 'MaxRuntimeExceeded', 'MaxWaitTimeExceeded', 'Pending', 'PreparingTrainingStack', 'Restarting', 'Starting', 'Stopped', 'Stopping', 'Training', 'Updating', 'Uploading']
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### HyperParameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### AlgorithmSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AlgorithmSpecificationOutput'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### InputDataConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ChannelOutput]
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OutputDataConfig'>
- **Required**: Yes

### ResourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResourceConfigOutput'>
- **Required**: Yes

### WarmPoolStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.WarmPoolStatus'>
- **Required**: Yes

### VpcConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.VpcConfigOutput'>
- **Required**: Yes

### StoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.StoppingCondition'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TrainingStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TrainingEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SecondaryStatusTransitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SecondaryStatusTransition]
- **Required**: Yes

### FinalMetricDataList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MetricData]
- **Required**: Yes

### EnableNetworkIsolation
- **Type**: <class 'bool'>
- **Required**: Yes

### EnableInterContainerTrafficEncryption
- **Type**: <class 'bool'>
- **Required**: Yes

### EnableManagedSpotTraining
- **Type**: <class 'bool'>
- **Required**: Yes

### CheckpointConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CheckpointConfig'>
- **Required**: Yes

### TrainingTimeInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### BillableTimeInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### DebugHookConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DebugHookConfigOutput'>
- **Required**: Yes

### ExperimentConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ExperimentConfig'>
- **Required**: Yes

### DebugRuleConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DebugRuleConfigurationOutput]
- **Required**: Yes

### TensorBoardOutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TensorBoardOutputConfig'>
- **Required**: Yes

### DebugRuleEvaluationStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DebugRuleEvaluationStatus]
- **Required**: Yes

### ProfilerConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProfilerConfigOutput'>
- **Required**: Yes

### ProfilerRuleConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProfilerRuleConfigurationOutput]
- **Required**: Yes

### ProfilerRuleEvaluationStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProfilerRuleEvaluationStatus]
- **Required**: Yes

### ProfilingStatus
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### Environment
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RetryStrategy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.RetryStrategy'>
- **Required**: Yes

### RemoteDebugConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.RemoteDebugConfig'>
- **Required**: Yes

### InfraCheckConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InfraCheckConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTrainingPlanRequest

### TrainingPlanName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTrainingPlanResponse

### TrainingPlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### TrainingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Active', 'Expired', 'Failed', 'Pending', 'Scheduled']
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### DurationHours
- **Type**: <class 'int'>
- **Required**: Yes

### DurationMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpfrontFee
- **Type**: <class 'str'>
- **Required**: Yes

### CurrencyCode
- **Type**: <class 'str'>
- **Required**: Yes

### TotalInstanceCount
- **Type**: <class 'int'>
- **Required**: Yes

### AvailableInstanceCount
- **Type**: <class 'int'>
- **Required**: Yes

### InUseInstanceCount
- **Type**: <class 'int'>
- **Required**: Yes

### TargetResources
- **Type**: typing.List[typing.Literal['hyperpod-cluster', 'training-job']]
- **Required**: Yes

### ReservedCapacitySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ReservedCapacitySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTransformJobRequest

### TransformJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTransformJobRequestWait

### TransformJobName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeTransformJobResponse

### TransformJobName
- **Type**: <class 'str'>
- **Required**: Yes

### TransformJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### TransformJobStatus
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxConcurrentTransforms
- **Type**: <class 'int'>
- **Required**: Yes

### ModelClientConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelClientConfig'>
- **Required**: Yes

### MaxPayloadInMB
- **Type**: <class 'int'>
- **Required**: Yes

### BatchStrategy
- **Type**: typing.Literal['MultiRecord', 'SingleRecord']
- **Required**: Yes

### Environment
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### TransformInput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TransformInput'>
- **Required**: Yes

### TransformOutput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TransformOutput'>
- **Required**: Yes

### DataCaptureConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.BatchDataCaptureConfig'>
- **Required**: Yes

### TransformResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TransformResources'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TransformStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TransformEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LabelingJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### AutoMLJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### DataProcessing
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DataProcessing'>
- **Required**: Yes

### ExperimentConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ExperimentConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTrialComponentRequest

### TrialComponentName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTrialComponentResponse

### TrialComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### TrialComponentArn
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrialComponentSource'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrialComponentStatus'>
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext'>
- **Required**: Yes

### Parameters
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrialComponentParameterValue]
- **Required**: Yes

### InputArtifacts
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrialComponentArtifact]
- **Required**: Yes

### OutputArtifacts
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrialComponentArtifact]
- **Required**: Yes

### MetadataProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MetadataProperties'>
- **Required**: Yes

### Metrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrialComponentMetricSummary]
- **Required**: Yes

### LineageGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### Sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrialComponentSource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTrialRequest

### TrialName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTrialResponse

### TrialName
- **Type**: <class 'str'>
- **Required**: Yes

### TrialArn
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### ExperimentName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrialSource'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext'>
- **Required**: Yes

### MetadataProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MetadataProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeUserProfileRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### UserProfileName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeUserProfileResponse

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### UserProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### UserProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### HomeEfsFileSystemUid
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Delete_Failed', 'Deleting', 'Failed', 'InService', 'Pending', 'Update_Failed', 'Updating']
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### SingleSignOnUserIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SingleSignOnUserValue
- **Type**: <class 'str'>
- **Required**: Yes

### UserSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserSettingsOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeWorkforceRequest

### WorkforceName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWorkforceResponse

### Workforce
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Workforce'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeWorkteamRequest

### WorkteamName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWorkteamResponse

### Workteam
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Workteam'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DesiredWeightAndCapacity

### VariantName
- **Type**: <class 'str'>
- **Required**: Yes

### DesiredWeight
- **Type**: typing.Optional[float]

### DesiredInstanceCount
- **Type**: typing.Optional[int]

### ServerlessUpdateConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProductionVariantServerlessUpdateConfig]


# Device

### DeviceName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### IotThingName
- **Type**: typing.Optional[str]


# DeviceDeploymentSummary

### EdgeDeploymentPlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### EdgeDeploymentPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### StageName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceArn
- **Type**: <class 'str'>
- **Required**: Yes

### DeployedStageName
- **Type**: typing.Optional[str]

### DeviceFleetName
- **Type**: typing.Optional[str]

### DeviceDeploymentStatus
- **Type**: typing.Optional[typing.Literal['DEPLOYED', 'FAILED', 'INPROGRESS', 'READYTODEPLOY', 'STOPPED', 'STOPPING']]

### DeviceDeploymentStatusMessage
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DeploymentStartTime
- **Type**: typing.Optional[datetime.datetime]


# DeviceFleetSummary

### DeviceFleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# DeviceSelectionConfig

### DeviceSubsetType
- **Type**: typing.Literal['NAMECONTAINS', 'PERCENTAGE', 'SELECTION']
- **Required**: Yes

### Percentage
- **Type**: typing.Optional[int]

### DeviceNames
- **Type**: typing.Optional[typing.List[str]]

### DeviceNameContains
- **Type**: typing.Optional[str]


# DeviceSelectionConfigOutput

### DeviceSubsetType
- **Type**: typing.Literal['NAMECONTAINS', 'PERCENTAGE', 'SELECTION']
- **Required**: Yes

### Percentage
- **Type**: typing.Optional[int]

### DeviceNames
- **Type**: typing.Optional[typing.List[str]]

### DeviceNameContains
- **Type**: typing.Optional[str]


# DeviceStats

### ConnectedDeviceCount
- **Type**: <class 'int'>
- **Required**: Yes

### RegisteredDeviceCount
- **Type**: <class 'int'>
- **Required**: Yes


# DeviceSummary

### DeviceName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### DeviceFleetName
- **Type**: typing.Optional[str]

### IotThingName
- **Type**: typing.Optional[str]

### RegistrationTime
- **Type**: typing.Optional[datetime.datetime]

### LatestHeartbeat
- **Type**: typing.Optional[datetime.datetime]

### Models
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EdgeModelSummary]]

### AgentVersion
- **Type**: typing.Optional[str]


# DirectDeploySettings

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# DisassociateTrialComponentRequest

### TrialComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### TrialName
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateTrialComponentResponse

### TrialComponentArn
- **Type**: <class 'str'>
- **Required**: Yes

### TrialArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# DockerSettings

### EnableDockerAccess
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### VpcOnlyTrustedAccounts
- **Type**: typing.Optional[typing.List[str]]


# DockerSettingsOutput

### EnableDockerAccess
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### VpcOnlyTrustedAccounts
- **Type**: typing.Optional[typing.List[str]]


# DomainDetails

### DomainArn
- **Type**: typing.Optional[str]

### DomainId
- **Type**: typing.Optional[str]

### DomainName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Delete_Failed', 'Deleting', 'Failed', 'InService', 'Pending', 'Update_Failed', 'Updating']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### Url
- **Type**: typing.Optional[str]


# DomainSettings

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### RStudioServerProDomainSettings
- **Type**: <class 'NoneType'>

### ExecutionRoleIdentityConfig
- **Type**: typing.Optional[typing.Literal['DISABLED', 'USER_PROFILE_NAME']]

### DockerSettings
- **Type**: <class 'NoneType'>

### AmazonQSettings
- **Type**: <class 'NoneType'>


# DomainSettingsForUpdate

### RStudioServerProDomainSettingsForUpdate
- **Type**: <class 'NoneType'>

### ExecutionRoleIdentityConfig
- **Type**: typing.Optional[typing.Literal['DISABLED', 'USER_PROFILE_NAME']]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### DockerSettings
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DockerSettings, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DockerSettingsOutput, NoneType]

### AmazonQSettings
- **Type**: <class 'NoneType'>


# DomainSettingsOutput

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### RStudioServerProDomainSettings
- **Type**: <class 'NoneType'>

### ExecutionRoleIdentityConfig
- **Type**: typing.Optional[typing.Literal['DISABLED', 'USER_PROFILE_NAME']]

### DockerSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DockerSettingsOutput]

### AmazonQSettings
- **Type**: <class 'NoneType'>


# DriftCheckBaselines

### Bias
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DriftCheckBias]

### Explainability
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DriftCheckExplainability]

### ModelQuality
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DriftCheckModelQuality]

### ModelDataQuality
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DriftCheckModelDataQuality]


# DriftCheckBias

### ConfigFile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.FileSource]

### PreTrainingConstraints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MetricsSource]

### PostTrainingConstraints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MetricsSource]


# DriftCheckExplainability

### Constraints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MetricsSource]

### ConfigFile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.FileSource]


# DriftCheckModelDataQuality

### Statistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MetricsSource]

### Constraints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MetricsSource]


# DriftCheckModelQuality

### Statistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MetricsSource]

### Constraints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MetricsSource]


# DynamicScalingConfiguration

### MinCapacity
- **Type**: typing.Optional[int]

### MaxCapacity
- **Type**: typing.Optional[int]

### ScaleInCooldown
- **Type**: typing.Optional[int]

### ScaleOutCooldown
- **Type**: typing.Optional[int]

### ScalingPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ScalingPolicy]]


# EFSFileSystem

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes


# EFSFileSystemConfig

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### FileSystemPath
- **Type**: typing.Optional[str]


# EMRStepMetadata

### ClusterId
- **Type**: typing.Optional[str]

### StepId
- **Type**: typing.Optional[str]

### StepName
- **Type**: typing.Optional[str]

### LogFilePath
- **Type**: typing.Optional[str]


# EbsStorageSettings

### EbsVolumeSizeInGb
- **Type**: <class 'int'>
- **Required**: Yes


# Edge

### SourceArn
- **Type**: typing.Optional[str]

### DestinationArn
- **Type**: typing.Optional[str]

### AssociationType
- **Type**: typing.Optional[typing.Literal['AssociatedWith', 'ContributedTo', 'DerivedFrom', 'Produced', 'SameAs']]


# EdgeDeploymentConfig

### FailureHandlingPolicy
- **Type**: typing.Literal['DO_NOTHING', 'ROLLBACK_ON_FAILURE']
- **Required**: Yes


# EdgeDeploymentModelConfig

### ModelHandle
- **Type**: <class 'str'>
- **Required**: Yes

### EdgePackagingJobName
- **Type**: <class 'str'>
- **Required**: Yes


# EdgeDeploymentPlanSummary

### EdgeDeploymentPlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### EdgeDeploymentPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes

### EdgeDeploymentSuccess
- **Type**: <class 'int'>
- **Required**: Yes

### EdgeDeploymentPending
- **Type**: <class 'int'>
- **Required**: Yes

### EdgeDeploymentFailed
- **Type**: <class 'int'>
- **Required**: Yes

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# EdgeDeploymentStatus

### StageStatus
- **Type**: typing.Literal['CREATING', 'DEPLOYED', 'FAILED', 'INPROGRESS', 'READYTODEPLOY', 'STARTING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### EdgeDeploymentSuccessInStage
- **Type**: <class 'int'>
- **Required**: Yes

### EdgeDeploymentPendingInStage
- **Type**: <class 'int'>
- **Required**: Yes

### EdgeDeploymentFailedInStage
- **Type**: <class 'int'>
- **Required**: Yes

### EdgeDeploymentStatusMessage
- **Type**: typing.Optional[str]

### EdgeDeploymentStageStartTime
- **Type**: typing.Optional[datetime.datetime]


# EdgeModel

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### LatestSampleTime
- **Type**: typing.Optional[datetime.datetime]

### LatestInference
- **Type**: typing.Optional[datetime.datetime]


# EdgeModelStat

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### OfflineDeviceCount
- **Type**: <class 'int'>
- **Required**: Yes

### ConnectedDeviceCount
- **Type**: <class 'int'>
- **Required**: Yes

### ActiveDeviceCount
- **Type**: <class 'int'>
- **Required**: Yes

### SamplingDeviceCount
- **Type**: <class 'int'>
- **Required**: Yes


# EdgeModelSummary

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes


# EdgeOutputConfig

### S3OutputLocation
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]

### PresetDeploymentType
- **Type**: typing.Optional[typing.Literal['GreengrassV2Component']]

### PresetDeploymentConfig
- **Type**: typing.Optional[str]


# EdgePackagingJobSummary

### EdgePackagingJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### EdgePackagingJobName
- **Type**: <class 'str'>
- **Required**: Yes

### EdgePackagingJobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'INPROGRESS', 'STARTING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### CompilationJobName
- **Type**: typing.Optional[str]

### ModelName
- **Type**: typing.Optional[str]

### ModelVersion
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# EdgePresetDeploymentOutput

### Type
- **Type**: typing.Literal['GreengrassV2Component']
- **Required**: Yes

### Artifact
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED']]

### StatusMessage
- **Type**: typing.Optional[str]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# EmrServerlessComputeConfig

### ExecutionRoleARN
- **Type**: <class 'str'>
- **Required**: Yes


# EmrServerlessSettings

### ExecutionRoleArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# EmrSettings

### AssumableRoleArns
- **Type**: typing.Optional[typing.List[str]]

### ExecutionRoleArns
- **Type**: typing.Optional[typing.List[str]]


# EmrSettingsOutput

### AssumableRoleArns
- **Type**: typing.Optional[typing.List[str]]

### ExecutionRoleArns
- **Type**: typing.Optional[typing.List[str]]


# Endpoint

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointStatus
- **Type**: typing.Literal['Creating', 'Deleting', 'Failed', 'InService', 'OutOfService', 'RollingBack', 'SystemUpdating', 'UpdateRollbackFailed', 'Updating']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ProductionVariants
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProductionVariantSummary]]

### DataCaptureConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DataCaptureConfigSummary]

### FailureReason
- **Type**: typing.Optional[str]

### MonitoringSchedules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringSchedule]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]

### ShadowProductionVariants
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProductionVariantSummary]]


# EndpointConfigStepMetadata

### Arn
- **Type**: typing.Optional[str]


# EndpointConfigSummary

### EndpointConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# EndpointInfo

### EndpointName
- **Type**: typing.Optional[str]


# EndpointInput

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### LocalPath
- **Type**: <class 'str'>
- **Required**: Yes

### S3InputMode
- **Type**: typing.Optional[typing.Literal['File', 'Pipe']]

### S3DataDistributionType
- **Type**: typing.Optional[typing.Literal['FullyReplicated', 'ShardedByS3Key']]

### FeaturesAttribute
- **Type**: typing.Optional[str]

### InferenceAttribute
- **Type**: typing.Optional[str]

### ProbabilityAttribute
- **Type**: typing.Optional[str]

### ProbabilityThresholdAttribute
- **Type**: typing.Optional[float]

### StartTimeOffset
- **Type**: typing.Optional[str]

### EndTimeOffset
- **Type**: typing.Optional[str]

### ExcludeFeaturesAttribute
- **Type**: typing.Optional[str]


# EndpointInputConfiguration

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.large', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c5d.18xlarge', 'ml.c5d.2xlarge', 'ml.c5d.4xlarge', 'ml.c5d.9xlarge', 'ml.c5d.large', 'ml.c5d.xlarge', 'ml.c6g.12xlarge', 'ml.c6g.16xlarge', 'ml.c6g.2xlarge', 'ml.c6g.4xlarge', 'ml.c6g.8xlarge', 'ml.c6g.large', 'ml.c6g.xlarge', 'ml.c6gd.12xlarge', 'ml.c6gd.16xlarge', 'ml.c6gd.2xlarge', 'ml.c6gd.4xlarge', 'ml.c6gd.8xlarge', 'ml.c6gd.large', 'ml.c6gd.xlarge', 'ml.c6gn.12xlarge', 'ml.c6gn.16xlarge', 'ml.c6gn.2xlarge', 'ml.c6gn.4xlarge', 'ml.c6gn.8xlarge', 'ml.c6gn.large', 'ml.c6gn.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c7g.12xlarge', 'ml.c7g.16xlarge', 'ml.c7g.2xlarge', 'ml.c7g.4xlarge', 'ml.c7g.8xlarge', 'ml.c7g.large', 'ml.c7g.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.dl1.24xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.inf1.24xlarge', 'ml.inf1.2xlarge', 'ml.inf1.6xlarge', 'ml.inf1.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6g.12xlarge', 'ml.m6g.16xlarge', 'ml.m6g.2xlarge', 'ml.m6g.4xlarge', 'ml.m6g.8xlarge', 'ml.m6g.large', 'ml.m6g.xlarge', 'ml.m6gd.12xlarge', 'ml.m6gd.16xlarge', 'ml.m6gd.2xlarge', 'ml.m6gd.4xlarge', 'ml.m6gd.8xlarge', 'ml.m6gd.large', 'ml.m6gd.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.r6g.12xlarge', 'ml.r6g.16xlarge', 'ml.r6g.2xlarge', 'ml.r6g.4xlarge', 'ml.r6g.8xlarge', 'ml.r6g.large', 'ml.r6g.xlarge', 'ml.r6gd.12xlarge', 'ml.r6gd.16xlarge', 'ml.r6gd.2xlarge', 'ml.r6gd.4xlarge', 'ml.r6gd.8xlarge', 'ml.r6gd.large', 'ml.r6gd.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.r8g.12xlarge', 'ml.r8g.16xlarge', 'ml.r8g.24xlarge', 'ml.r8g.2xlarge', 'ml.r8g.48xlarge', 'ml.r8g.4xlarge', 'ml.r8g.8xlarge', 'ml.r8g.large', 'ml.r8g.medium', 'ml.r8g.xlarge', 'ml.t2.2xlarge', 'ml.t2.large', 'ml.t2.medium', 'ml.t2.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]

### ServerlessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProductionVariantServerlessConfig]

### InferenceSpecificationName
- **Type**: typing.Optional[str]

### EnvironmentParameterRanges
- **Type**: <class 'NoneType'>


# EndpointInputConfigurationOutput

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.large', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c5d.18xlarge', 'ml.c5d.2xlarge', 'ml.c5d.4xlarge', 'ml.c5d.9xlarge', 'ml.c5d.large', 'ml.c5d.xlarge', 'ml.c6g.12xlarge', 'ml.c6g.16xlarge', 'ml.c6g.2xlarge', 'ml.c6g.4xlarge', 'ml.c6g.8xlarge', 'ml.c6g.large', 'ml.c6g.xlarge', 'ml.c6gd.12xlarge', 'ml.c6gd.16xlarge', 'ml.c6gd.2xlarge', 'ml.c6gd.4xlarge', 'ml.c6gd.8xlarge', 'ml.c6gd.large', 'ml.c6gd.xlarge', 'ml.c6gn.12xlarge', 'ml.c6gn.16xlarge', 'ml.c6gn.2xlarge', 'ml.c6gn.4xlarge', 'ml.c6gn.8xlarge', 'ml.c6gn.large', 'ml.c6gn.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c7g.12xlarge', 'ml.c7g.16xlarge', 'ml.c7g.2xlarge', 'ml.c7g.4xlarge', 'ml.c7g.8xlarge', 'ml.c7g.large', 'ml.c7g.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.dl1.24xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.inf1.24xlarge', 'ml.inf1.2xlarge', 'ml.inf1.6xlarge', 'ml.inf1.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6g.12xlarge', 'ml.m6g.16xlarge', 'ml.m6g.2xlarge', 'ml.m6g.4xlarge', 'ml.m6g.8xlarge', 'ml.m6g.large', 'ml.m6g.xlarge', 'ml.m6gd.12xlarge', 'ml.m6gd.16xlarge', 'ml.m6gd.2xlarge', 'ml.m6gd.4xlarge', 'ml.m6gd.8xlarge', 'ml.m6gd.large', 'ml.m6gd.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.r6g.12xlarge', 'ml.r6g.16xlarge', 'ml.r6g.2xlarge', 'ml.r6g.4xlarge', 'ml.r6g.8xlarge', 'ml.r6g.large', 'ml.r6g.xlarge', 'ml.r6gd.12xlarge', 'ml.r6gd.16xlarge', 'ml.r6gd.2xlarge', 'ml.r6gd.4xlarge', 'ml.r6gd.8xlarge', 'ml.r6gd.large', 'ml.r6gd.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.r8g.12xlarge', 'ml.r8g.16xlarge', 'ml.r8g.24xlarge', 'ml.r8g.2xlarge', 'ml.r8g.48xlarge', 'ml.r8g.4xlarge', 'ml.r8g.8xlarge', 'ml.r8g.large', 'ml.r8g.medium', 'ml.r8g.xlarge', 'ml.t2.2xlarge', 'ml.t2.large', 'ml.t2.medium', 'ml.t2.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]

### ServerlessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProductionVariantServerlessConfig]

### InferenceSpecificationName
- **Type**: typing.Optional[str]

### EnvironmentParameterRanges
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EnvironmentParameterRangesOutput]


# EndpointMetadata

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointConfigName
- **Type**: typing.Optional[str]

### EndpointStatus
- **Type**: typing.Optional[typing.Literal['Creating', 'Deleting', 'Failed', 'InService', 'OutOfService', 'RollingBack', 'SystemUpdating', 'UpdateRollbackFailed', 'Updating']]

### FailureReason
- **Type**: typing.Optional[str]


# EndpointOutputConfiguration

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### VariantName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.large', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c5d.18xlarge', 'ml.c5d.2xlarge', 'ml.c5d.4xlarge', 'ml.c5d.9xlarge', 'ml.c5d.large', 'ml.c5d.xlarge', 'ml.c6g.12xlarge', 'ml.c6g.16xlarge', 'ml.c6g.2xlarge', 'ml.c6g.4xlarge', 'ml.c6g.8xlarge', 'ml.c6g.large', 'ml.c6g.xlarge', 'ml.c6gd.12xlarge', 'ml.c6gd.16xlarge', 'ml.c6gd.2xlarge', 'ml.c6gd.4xlarge', 'ml.c6gd.8xlarge', 'ml.c6gd.large', 'ml.c6gd.xlarge', 'ml.c6gn.12xlarge', 'ml.c6gn.16xlarge', 'ml.c6gn.2xlarge', 'ml.c6gn.4xlarge', 'ml.c6gn.8xlarge', 'ml.c6gn.large', 'ml.c6gn.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c7g.12xlarge', 'ml.c7g.16xlarge', 'ml.c7g.2xlarge', 'ml.c7g.4xlarge', 'ml.c7g.8xlarge', 'ml.c7g.large', 'ml.c7g.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.dl1.24xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.inf1.24xlarge', 'ml.inf1.2xlarge', 'ml.inf1.6xlarge', 'ml.inf1.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6g.12xlarge', 'ml.m6g.16xlarge', 'ml.m6g.2xlarge', 'ml.m6g.4xlarge', 'ml.m6g.8xlarge', 'ml.m6g.large', 'ml.m6g.xlarge', 'ml.m6gd.12xlarge', 'ml.m6gd.16xlarge', 'ml.m6gd.2xlarge', 'ml.m6gd.4xlarge', 'ml.m6gd.8xlarge', 'ml.m6gd.large', 'ml.m6gd.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.r6g.12xlarge', 'ml.r6g.16xlarge', 'ml.r6g.2xlarge', 'ml.r6g.4xlarge', 'ml.r6g.8xlarge', 'ml.r6g.large', 'ml.r6g.xlarge', 'ml.r6gd.12xlarge', 'ml.r6gd.16xlarge', 'ml.r6gd.2xlarge', 'ml.r6gd.4xlarge', 'ml.r6gd.8xlarge', 'ml.r6gd.large', 'ml.r6gd.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.r8g.12xlarge', 'ml.r8g.16xlarge', 'ml.r8g.24xlarge', 'ml.r8g.2xlarge', 'ml.r8g.48xlarge', 'ml.r8g.4xlarge', 'ml.r8g.8xlarge', 'ml.r8g.large', 'ml.r8g.medium', 'ml.r8g.xlarge', 'ml.t2.2xlarge', 'ml.t2.large', 'ml.t2.medium', 'ml.t2.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]

### InitialInstanceCount
- **Type**: typing.Optional[int]

### ServerlessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProductionVariantServerlessConfig]


# EndpointPerformance

### Metrics
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceMetrics'>
- **Required**: Yes

### EndpointInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EndpointInfo'>
- **Required**: Yes


# EndpointStepMetadata

### Arn
- **Type**: typing.Optional[str]


# EndpointSummary

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndpointStatus
- **Type**: typing.Literal['Creating', 'Deleting', 'Failed', 'InService', 'OutOfService', 'RollingBack', 'SystemUpdating', 'UpdateRollbackFailed', 'Updating']
- **Required**: Yes


# EnvironmentParameter

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### ValueType
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# EnvironmentParameterRanges

### CategoricalParameterRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CategoricalParameter]]


# EnvironmentParameterRangesOutput

### CategoricalParameterRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CategoricalParameterOutput]]


# ErrorInfo

### Code
- **Type**: typing.Optional[str]

### Reason
- **Type**: typing.Optional[str]


# Experiment

### ExperimentName
- **Type**: typing.Optional[str]

### ExperimentArn
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ExperimentSource]

### Description
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# ExperimentConfig

### ExperimentName
- **Type**: typing.Optional[str]

### TrialName
- **Type**: typing.Optional[str]

### TrialComponentDisplayName
- **Type**: typing.Optional[str]

### RunName
- **Type**: typing.Optional[str]


# ExperimentSource

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceType
- **Type**: typing.Optional[str]


# ExperimentSummary

### ExperimentArn
- **Type**: typing.Optional[str]

### ExperimentName
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### ExperimentSource
- **Type**: <class 'NoneType'>

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# Explainability

### Report
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MetricsSource]


# ExplainerConfig

### ClarifyExplainerConfig
- **Type**: <class 'NoneType'>


# ExplainerConfigOutput

### ClarifyExplainerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ClarifyExplainerConfigOutput]


# FSxLustreFileSystem

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes


# FSxLustreFileSystemConfig

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### FileSystemPath
- **Type**: typing.Optional[str]


# FailStepMetadata

### ErrorMessage
- **Type**: typing.Optional[str]


# FeatureDefinition

### FeatureName
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureType
- **Type**: typing.Literal['Fractional', 'Integral', 'String']
- **Required**: Yes

### CollectionType
- **Type**: typing.Optional[typing.Literal['List', 'Set', 'Vector']]

### CollectionConfig
- **Type**: <class 'NoneType'>


# FeatureGroup

### FeatureGroupArn
- **Type**: typing.Optional[str]

### FeatureGroupName
- **Type**: typing.Optional[str]

### RecordIdentifierFeatureName
- **Type**: typing.Optional[str]

### EventTimeFeatureName
- **Type**: typing.Optional[str]

### FeatureDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.FeatureDefinition]]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### OnlineStoreConfig
- **Type**: <class 'NoneType'>

### OfflineStoreConfig
- **Type**: <class 'NoneType'>

### RoleArn
- **Type**: typing.Optional[str]

### FeatureGroupStatus
- **Type**: typing.Optional[typing.Literal['CreateFailed', 'Created', 'Creating', 'DeleteFailed', 'Deleting']]

### OfflineStoreStatus
- **Type**: <class 'NoneType'>

### LastUpdateStatus
- **Type**: <class 'NoneType'>

### FailureReason
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# FeatureGroupSummary

### FeatureGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FeatureGroupStatus
- **Type**: typing.Optional[typing.Literal['CreateFailed', 'Created', 'Creating', 'DeleteFailed', 'Deleting']]

### OfflineStoreStatus
- **Type**: <class 'NoneType'>


# FeatureMetadata

### FeatureGroupArn
- **Type**: typing.Optional[str]

### FeatureGroupName
- **Type**: typing.Optional[str]

### FeatureName
- **Type**: typing.Optional[str]

### FeatureType
- **Type**: typing.Optional[typing.Literal['Fractional', 'Integral', 'String']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.FeatureParameter]]


# FeatureParameter

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# FileSource

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### ContentType
- **Type**: typing.Optional[str]

### ContentDigest
- **Type**: typing.Optional[str]


# FileSystemConfig

### MountPath
- **Type**: typing.Optional[str]

### DefaultUid
- **Type**: typing.Optional[int]

### DefaultGid
- **Type**: typing.Optional[int]


# FileSystemDataSource

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### FileSystemAccessMode
- **Type**: typing.Literal['ro', 'rw']
- **Required**: Yes

### FileSystemType
- **Type**: typing.Literal['EFS', 'FSxLustre']
- **Required**: Yes

### DirectoryPath
- **Type**: <class 'str'>
- **Required**: Yes


# Filter

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Operator
- **Type**: typing.Optional[typing.Literal['Contains', 'Equals', 'Exists', 'GreaterThan', 'GreaterThanOrEqualTo', 'In', 'LessThan', 'LessThanOrEqualTo', 'NotEquals', 'NotExists']]

### Value
- **Type**: typing.Optional[str]


# FinalAutoMLJobObjectiveMetric

### MetricName
- **Type**: typing.Literal['AUC', 'Accuracy', 'AverageWeightedQuantileLoss', 'BalancedAccuracy', 'F1', 'F1macro', 'MAE', 'MAPE', 'MASE', 'MSE', 'Precision', 'PrecisionMacro', 'R2', 'RMSE', 'Recall', 'RecallMacro', 'WAPE']
- **Required**: Yes

### Value
- **Type**: <class 'float'>
- **Required**: Yes

### Type
- **Type**: typing.Optional[typing.Literal['Maximize', 'Minimize']]

### StandardMetricName
- **Type**: typing.Optional[typing.Literal['AUC', 'Accuracy', 'AverageWeightedQuantileLoss', 'BalancedAccuracy', 'F1', 'F1macro', 'MAE', 'MAPE', 'MASE', 'MSE', 'Precision', 'PrecisionMacro', 'R2', 'RMSE', 'Recall', 'RecallMacro', 'WAPE']]


# FinalHyperParameterTuningJobObjectiveMetric

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'float'>
- **Required**: Yes

### Type
- **Type**: typing.Optional[typing.Literal['Maximize', 'Minimize']]


# FlowDefinitionOutputConfig

### S3OutputPath
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# FlowDefinitionSummary

### FlowDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### FlowDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### FlowDefinitionStatus
- **Type**: typing.Literal['Active', 'Deleting', 'Failed', 'Initializing']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureReason
- **Type**: typing.Optional[str]


# GenerativeAiSettings

### AmazonBedrockRoleArn
- **Type**: typing.Optional[str]


# GetDeviceFleetReportRequest

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeviceFleetReportResponse

### DeviceFleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EdgeOutputConfig'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ReportGenerated
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DeviceStats
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DeviceStats'>
- **Required**: Yes

### AgentVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AgentVersion]
- **Required**: Yes

### ModelStats
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EdgeModelStat]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# GetLineageGroupPolicyRequest

### LineageGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# GetLineageGroupPolicyResponse

### LineageGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourcePolicy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# GetModelPackageGroupPolicyInput

### ModelPackageGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# GetModelPackageGroupPolicyOutput

### ResourcePolicy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# GetSagemakerServicecatalogPortfolioStatusOutput

### Status
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# GetScalingConfigurationRecommendationRequest

### InferenceRecommendationsJobName
- **Type**: <class 'str'>
- **Required**: Yes

### RecommendationId
- **Type**: typing.Optional[str]

### EndpointName
- **Type**: typing.Optional[str]

### TargetCpuUtilizationPerCore
- **Type**: typing.Optional[int]

### ScalingPolicyObjective
- **Type**: <class 'NoneType'>


# GetScalingConfigurationRecommendationResponse

### InferenceRecommendationsJobName
- **Type**: <class 'str'>
- **Required**: Yes

### RecommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetCpuUtilizationPerCore
- **Type**: <class 'int'>
- **Required**: Yes

### ScalingPolicyObjective
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ScalingPolicyObjective'>
- **Required**: Yes

### Metric
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ScalingPolicyMetric'>
- **Required**: Yes

### DynamicScalingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DynamicScalingConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# GetSearchSuggestionsRequest

### Resource
- **Type**: typing.Literal['Endpoint', 'Experiment', 'ExperimentTrial', 'ExperimentTrialComponent', 'FeatureGroup', 'FeatureMetadata', 'HyperParameterTuningJob', 'Image', 'ImageVersion', 'Model', 'ModelCard', 'ModelPackage', 'ModelPackageGroup', 'Pipeline', 'PipelineExecution', 'Project', 'TrainingJob']
- **Required**: Yes

### SuggestionQuery
- **Type**: <class 'NoneType'>


# GetSearchSuggestionsResponse

### PropertyNameSuggestions
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PropertyNameSuggestion]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# GitConfig

### RepositoryUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Branch
- **Type**: typing.Optional[str]

### SecretArn
- **Type**: typing.Optional[str]


# GitConfigForUpdate

### SecretArn
- **Type**: typing.Optional[str]


# HiddenSageMakerImage

### SageMakerImageName
- **Type**: typing.Optional[typing.Literal['sagemaker_distribution']]

### VersionAliases
- **Type**: typing.Optional[typing.List[str]]


# HiddenSageMakerImageOutput

### SageMakerImageName
- **Type**: typing.Optional[typing.Literal['sagemaker_distribution']]

### VersionAliases
- **Type**: typing.Optional[typing.List[str]]


# HolidayConfigAttributes

### CountryCode
- **Type**: typing.Optional[str]


# HubAccessConfig

### HubContentArn
- **Type**: <class 'str'>
- **Required**: Yes


# HubContentDependency

### DependencyOriginPath
- **Type**: typing.Optional[str]

### DependencyCopyPath
- **Type**: typing.Optional[str]


# HubContentInfo

### HubContentName
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentArn
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentType
- **Type**: typing.Literal['Model', 'ModelReference', 'Notebook']
- **Required**: Yes

### DocumentSchemaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentStatus
- **Type**: typing.Literal['Available', 'DeleteFailed', 'Deleting', 'ImportFailed', 'Importing']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SageMakerPublicHubContentArn
- **Type**: typing.Optional[str]

### HubContentDisplayName
- **Type**: typing.Optional[str]

### HubContentDescription
- **Type**: typing.Optional[str]

### SupportStatus
- **Type**: typing.Optional[typing.Literal['Deprecated', 'Restricted', 'Supported']]

### HubContentSearchKeywords
- **Type**: typing.Optional[typing.List[str]]

### OriginalCreationTime
- **Type**: typing.Optional[datetime.datetime]


# HubInfo

### HubName
- **Type**: <class 'str'>
- **Required**: Yes

### HubArn
- **Type**: <class 'str'>
- **Required**: Yes

### HubStatus
- **Type**: typing.Literal['CreateFailed', 'Creating', 'DeleteFailed', 'Deleting', 'InService', 'UpdateFailed', 'Updating']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### HubDisplayName
- **Type**: typing.Optional[str]

### HubDescription
- **Type**: typing.Optional[str]

### HubSearchKeywords
- **Type**: typing.Optional[typing.List[str]]


# HubS3StorageConfig

### S3OutputPath
- **Type**: typing.Optional[str]


# HumanLoopActivationConditionsConfig

### HumanLoopActivationConditions
- **Type**: <class 'str'>
- **Required**: Yes


# HumanLoopActivationConfig

### HumanLoopActivationConditionsConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HumanLoopActivationConditionsConfig'>
- **Required**: Yes


# HumanLoopConfig

### WorkteamArn
- **Type**: <class 'str'>
- **Required**: Yes

### HumanTaskUiArn
- **Type**: <class 'str'>
- **Required**: Yes

### TaskTitle
- **Type**: <class 'str'>
- **Required**: Yes

### TaskDescription
- **Type**: <class 'str'>
- **Required**: Yes

### TaskCount
- **Type**: <class 'int'>
- **Required**: Yes

### TaskAvailabilityLifetimeInSeconds
- **Type**: typing.Optional[int]

### TaskTimeLimitInSeconds
- **Type**: typing.Optional[int]

### TaskKeywords
- **Type**: typing.Optional[typing.List[str]]

### PublicWorkforceTaskPrice
- **Type**: <class 'NoneType'>


# HumanLoopConfigOutput

### WorkteamArn
- **Type**: <class 'str'>
- **Required**: Yes

### HumanTaskUiArn
- **Type**: <class 'str'>
- **Required**: Yes

### TaskTitle
- **Type**: <class 'str'>
- **Required**: Yes

### TaskDescription
- **Type**: <class 'str'>
- **Required**: Yes

### TaskCount
- **Type**: <class 'int'>
- **Required**: Yes

### TaskAvailabilityLifetimeInSeconds
- **Type**: typing.Optional[int]

### TaskTimeLimitInSeconds
- **Type**: typing.Optional[int]

### TaskKeywords
- **Type**: typing.Optional[typing.List[str]]

### PublicWorkforceTaskPrice
- **Type**: <class 'NoneType'>


# HumanLoopRequestSource

### AwsManagedHumanLoopRequestSource
- **Type**: typing.Literal['AWS/Rekognition/DetectModerationLabels/Image/V3', 'AWS/Textract/AnalyzeDocument/Forms/V1']
- **Required**: Yes


# HumanTaskConfig

### WorkteamArn
- **Type**: <class 'str'>
- **Required**: Yes

### UiConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UiConfig'>
- **Required**: Yes

### TaskTitle
- **Type**: <class 'str'>
- **Required**: Yes

### TaskDescription
- **Type**: <class 'str'>
- **Required**: Yes

### NumberOfHumanWorkersPerDataObject
- **Type**: <class 'int'>
- **Required**: Yes

### TaskTimeLimitInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### PreHumanTaskLambdaArn
- **Type**: typing.Optional[str]

### TaskKeywords
- **Type**: typing.Optional[typing.List[str]]

### TaskAvailabilityLifetimeInSeconds
- **Type**: typing.Optional[int]

### MaxConcurrentTaskCount
- **Type**: typing.Optional[int]

### AnnotationConsolidationConfig
- **Type**: <class 'NoneType'>

### PublicWorkforceTaskPrice
- **Type**: <class 'NoneType'>


# HumanTaskConfigOutput

### WorkteamArn
- **Type**: <class 'str'>
- **Required**: Yes

### UiConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UiConfig'>
- **Required**: Yes

### TaskTitle
- **Type**: <class 'str'>
- **Required**: Yes

### TaskDescription
- **Type**: <class 'str'>
- **Required**: Yes

### NumberOfHumanWorkersPerDataObject
- **Type**: <class 'int'>
- **Required**: Yes

### TaskTimeLimitInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### PreHumanTaskLambdaArn
- **Type**: typing.Optional[str]

### TaskKeywords
- **Type**: typing.Optional[typing.List[str]]

### TaskAvailabilityLifetimeInSeconds
- **Type**: typing.Optional[int]

### MaxConcurrentTaskCount
- **Type**: typing.Optional[int]

### AnnotationConsolidationConfig
- **Type**: <class 'NoneType'>

### PublicWorkforceTaskPrice
- **Type**: <class 'NoneType'>


# HumanTaskUiSummary

### HumanTaskUiName
- **Type**: <class 'str'>
- **Required**: Yes

### HumanTaskUiArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# HyperParameterAlgorithmSpecification

### TrainingInputMode
- **Type**: typing.Literal['FastFile', 'File', 'Pipe']
- **Required**: Yes

### TrainingImage
- **Type**: typing.Optional[str]

### AlgorithmName
- **Type**: typing.Optional[str]

### MetricDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MetricDefinition]]


# HyperParameterAlgorithmSpecificationOutput

### TrainingInputMode
- **Type**: typing.Literal['FastFile', 'File', 'Pipe']
- **Required**: Yes

### TrainingImage
- **Type**: typing.Optional[str]

### AlgorithmName
- **Type**: typing.Optional[str]

### MetricDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MetricDefinition]]


# HyperParameterSpecification

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['Categorical', 'Continuous', 'FreeText', 'Integer']
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Range
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ParameterRange]

### IsTunable
- **Type**: typing.Optional[bool]

### IsRequired
- **Type**: typing.Optional[bool]

### DefaultValue
- **Type**: typing.Optional[str]


# HyperParameterSpecificationOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['Categorical', 'Continuous', 'FreeText', 'Integer']
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Range
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ParameterRangeOutput]

### IsTunable
- **Type**: typing.Optional[bool]

### IsRequired
- **Type**: typing.Optional[bool]

### DefaultValue
- **Type**: typing.Optional[str]


# HyperParameterTrainingJobDefinition

### AlgorithmSpecification
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterAlgorithmSpecification, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterAlgorithmSpecificationOutput]
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OutputDataConfig'>
- **Required**: Yes

### StoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.StoppingCondition'>
- **Required**: Yes

### DefinitionName
- **Type**: typing.Optional[str]

### TuningObjective
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTuningJobObjective]

### HyperParameterRanges
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ParameterRanges, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ParameterRangesOutput, NoneType]

### StaticHyperParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### InputDataConfig
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Channel, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ChannelOutput]]]

### VpcConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.VpcConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.VpcConfigOutput, NoneType]

### ResourceConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResourceConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResourceConfigOutput, NoneType]

### HyperParameterTuningResourceConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTuningResourceConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTuningResourceConfigOutput, NoneType]

### EnableNetworkIsolation
- **Type**: typing.Optional[bool]

### EnableInterContainerTrafficEncryption
- **Type**: typing.Optional[bool]

### EnableManagedSpotTraining
- **Type**: typing.Optional[bool]

### CheckpointConfig
- **Type**: <class 'NoneType'>

### RetryStrategy
- **Type**: <class 'NoneType'>

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]


# HyperParameterTrainingJobDefinitionOutput

### AlgorithmSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterAlgorithmSpecificationOutput'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OutputDataConfig'>
- **Required**: Yes

### StoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.StoppingCondition'>
- **Required**: Yes

### DefinitionName
- **Type**: typing.Optional[str]

### TuningObjective
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTuningJobObjective]

### HyperParameterRanges
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ParameterRangesOutput]

### StaticHyperParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### InputDataConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ChannelOutput]]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.VpcConfigOutput]

### ResourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResourceConfigOutput]

### HyperParameterTuningResourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTuningResourceConfigOutput]

### EnableNetworkIsolation
- **Type**: typing.Optional[bool]

### EnableInterContainerTrafficEncryption
- **Type**: typing.Optional[bool]

### EnableManagedSpotTraining
- **Type**: typing.Optional[bool]

### CheckpointConfig
- **Type**: <class 'NoneType'>

### RetryStrategy
- **Type**: <class 'NoneType'>

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]


# HyperParameterTrainingJobSummary

### TrainingJobName
- **Type**: <class 'str'>
- **Required**: Yes

### TrainingJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TrainingJobStatus
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']
- **Required**: Yes

### TunedHyperParameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### TrainingJobDefinitionName
- **Type**: typing.Optional[str]

### TuningJobName
- **Type**: typing.Optional[str]

### TrainingStartTime
- **Type**: typing.Optional[datetime.datetime]

### TrainingEndTime
- **Type**: typing.Optional[datetime.datetime]

### FailureReason
- **Type**: typing.Optional[str]

### FinalHyperParameterTuningJobObjectiveMetric
- **Type**: <class 'NoneType'>

### ObjectiveStatus
- **Type**: typing.Optional[typing.Literal['Failed', 'Pending', 'Succeeded']]


# HyperParameterTuningInstanceConfig

### InstanceType
- **Type**: typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c5n.18xlarge', 'ml.c5n.2xlarge', 'ml.c5n.4xlarge', 'ml.c5n.9xlarge', 'ml.c5n.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.16xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.8xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']
- **Required**: Yes

### InstanceCount
- **Type**: <class 'int'>
- **Required**: Yes

### VolumeSizeInGB
- **Type**: <class 'int'>
- **Required**: Yes


# HyperParameterTuningJobCompletionDetails

### NumberOfTrainingJobsObjectiveNotImproving
- **Type**: typing.Optional[int]

### ConvergenceDetectedTime
- **Type**: typing.Optional[datetime.datetime]


# HyperParameterTuningJobConfig

### Strategy
- **Type**: typing.Literal['Bayesian', 'Grid', 'Hyperband', 'Random']
- **Required**: Yes

### ResourceLimits
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResourceLimits'>
- **Required**: Yes

### StrategyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTuningJobStrategyConfig]

### HyperParameterTuningJobObjective
- **Type**: <class 'NoneType'>

### ParameterRanges
- **Type**: <class 'NoneType'>

### TrainingJobEarlyStoppingType
- **Type**: typing.Optional[typing.Literal['Auto', 'Off']]

### TuningJobCompletionCriteria
- **Type**: <class 'NoneType'>

### RandomSeed
- **Type**: typing.Optional[int]


# HyperParameterTuningJobConfigOutput

### Strategy
- **Type**: typing.Literal['Bayesian', 'Grid', 'Hyperband', 'Random']
- **Required**: Yes

### ResourceLimits
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResourceLimits'>
- **Required**: Yes

### StrategyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTuningJobStrategyConfig]

### HyperParameterTuningJobObjective
- **Type**: <class 'NoneType'>

### ParameterRanges
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ParameterRangesOutput]

### TrainingJobEarlyStoppingType
- **Type**: typing.Optional[typing.Literal['Auto', 'Off']]

### TuningJobCompletionCriteria
- **Type**: <class 'NoneType'>

### RandomSeed
- **Type**: typing.Optional[int]


# HyperParameterTuningJobConsumedResources

### RuntimeInSeconds
- **Type**: typing.Optional[int]


# HyperParameterTuningJobObjective

### Type
- **Type**: typing.Literal['Maximize', 'Minimize']
- **Required**: Yes

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes


# HyperParameterTuningJobSearchEntity

### HyperParameterTuningJobName
- **Type**: typing.Optional[str]

### HyperParameterTuningJobArn
- **Type**: typing.Optional[str]

### HyperParameterTuningJobConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTuningJobConfigOutput]

### TrainingJobDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTrainingJobDefinitionOutput]

### TrainingJobDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTrainingJobDefinitionOutput]]

### HyperParameterTuningJobStatus
- **Type**: typing.Optional[typing.Literal['Completed', 'DeleteFailed', 'Deleting', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### HyperParameterTuningEndTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### TrainingJobStatusCounters
- **Type**: <class 'NoneType'>

### ObjectiveStatusCounters
- **Type**: <class 'NoneType'>

### BestTrainingJob
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTrainingJobSummary]

### OverallBestTrainingJob
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTrainingJobSummary]

### WarmStartConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTuningJobWarmStartConfigOutput]

### FailureReason
- **Type**: typing.Optional[str]

### TuningJobCompletionDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTuningJobCompletionDetails]

### ConsumedResources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTuningJobConsumedResources]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# HyperParameterTuningJobStrategyConfig

### HyperbandStrategyConfig
- **Type**: <class 'NoneType'>


# HyperParameterTuningJobSummary

### HyperParameterTuningJobName
- **Type**: <class 'str'>
- **Required**: Yes

### HyperParameterTuningJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### HyperParameterTuningJobStatus
- **Type**: typing.Literal['Completed', 'DeleteFailed', 'Deleting', 'Failed', 'InProgress', 'Stopped', 'Stopping']
- **Required**: Yes

### Strategy
- **Type**: typing.Literal['Bayesian', 'Grid', 'Hyperband', 'Random']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TrainingJobStatusCounters
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrainingJobStatusCounters'>
- **Required**: Yes

### ObjectiveStatusCounters
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ObjectiveStatusCounters'>
- **Required**: Yes

### HyperParameterTuningEndTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### ResourceLimits
- **Type**: <class 'NoneType'>


# HyperParameterTuningJobWarmStartConfig

### ParentHyperParameterTuningJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ParentHyperParameterTuningJob]
- **Required**: Yes

### WarmStartType
- **Type**: typing.Literal['IdenticalDataAndAlgorithm', 'TransferLearning']
- **Required**: Yes


# HyperParameterTuningJobWarmStartConfigOutput

### ParentHyperParameterTuningJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ParentHyperParameterTuningJob]
- **Required**: Yes

### WarmStartType
- **Type**: typing.Literal['IdenticalDataAndAlgorithm', 'TransferLearning']
- **Required**: Yes


# HyperParameterTuningResourceConfig

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c5n.18xlarge', 'ml.c5n.2xlarge', 'ml.c5n.4xlarge', 'ml.c5n.9xlarge', 'ml.c5n.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.16xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.8xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]

### InstanceCount
- **Type**: typing.Optional[int]

### VolumeSizeInGB
- **Type**: typing.Optional[int]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### AllocationStrategy
- **Type**: typing.Optional[typing.Literal['Prioritized']]

### InstanceConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTuningInstanceConfig]]


# HyperParameterTuningResourceConfigOutput

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c5n.18xlarge', 'ml.c5n.2xlarge', 'ml.c5n.4xlarge', 'ml.c5n.9xlarge', 'ml.c5n.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.16xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.8xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]

### InstanceCount
- **Type**: typing.Optional[int]

### VolumeSizeInGB
- **Type**: typing.Optional[int]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### AllocationStrategy
- **Type**: typing.Optional[typing.Literal['Prioritized']]

### InstanceConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTuningInstanceConfig]]


# HyperbandStrategyConfig

### MinResource
- **Type**: typing.Optional[int]

### MaxResource
- **Type**: typing.Optional[int]


# IamIdentity

### Arn
- **Type**: typing.Optional[str]

### PrincipalId
- **Type**: typing.Optional[str]

### SourceIdentity
- **Type**: typing.Optional[str]


# IamPolicyConstraints

### SourceIp
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### VpcSourceIp
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# IdentityProviderOAuthSetting

### DataSourceName
- **Type**: typing.Optional[typing.Literal['SalesforceGenie', 'Snowflake']]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### SecretArn
- **Type**: typing.Optional[str]


# IdleSettings

### LifecycleManagement
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### IdleTimeoutInMinutes
- **Type**: typing.Optional[int]

### MinIdleTimeoutInMinutes
- **Type**: typing.Optional[int]

### MaxIdleTimeoutInMinutes
- **Type**: typing.Optional[int]


# Image

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ImageArn
- **Type**: <class 'str'>
- **Required**: Yes

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### ImageStatus
- **Type**: typing.Literal['CREATED', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### FailureReason
- **Type**: typing.Optional[str]


# ImageClassificationJobConfig

### CompletionCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLJobCompletionCriteria]


# ImageConfig

### RepositoryAccessMode
- **Type**: typing.Literal['Platform', 'Vpc']
- **Required**: Yes

### RepositoryAuthConfig
- **Type**: <class 'NoneType'>


# ImageVersion

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ImageArn
- **Type**: <class 'str'>
- **Required**: Yes

### ImageVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ImageVersionStatus
- **Type**: typing.Literal['CREATED', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING']
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Version
- **Type**: <class 'int'>
- **Required**: Yes

### FailureReason
- **Type**: typing.Optional[str]


# ImportHubContentRequest

### HubContentName
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentType
- **Type**: typing.Literal['Model', 'ModelReference', 'Notebook']
- **Required**: Yes

### DocumentSchemaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### HubName
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentDocument
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentVersion
- **Type**: typing.Optional[str]

### HubContentDisplayName
- **Type**: typing.Optional[str]

### HubContentDescription
- **Type**: typing.Optional[str]

### HubContentMarkdown
- **Type**: typing.Optional[str]

### SupportStatus
- **Type**: typing.Optional[typing.Literal['Deprecated', 'Restricted', 'Supported']]

### HubContentSearchKeywords
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# ImportHubContentResponse

### HubArn
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# InferenceComponentCapacitySize

### Type
- **Type**: typing.Literal['CAPACITY_PERCENT', 'COPY_COUNT']
- **Required**: Yes

### Value
- **Type**: <class 'int'>
- **Required**: Yes


# InferenceComponentComputeResourceRequirements

### MinMemoryRequiredInMb
- **Type**: <class 'int'>
- **Required**: Yes

### NumberOfCpuCoresRequired
- **Type**: typing.Optional[float]

### NumberOfAcceleratorDevicesRequired
- **Type**: typing.Optional[float]

### MaxMemoryRequiredInMb
- **Type**: typing.Optional[int]


# InferenceComponentContainerSpecification

### Image
- **Type**: typing.Optional[str]

### ArtifactUrl
- **Type**: typing.Optional[str]

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]


# InferenceComponentContainerSpecificationSummary

### DeployedImage
- **Type**: <class 'NoneType'>

### ArtifactUrl
- **Type**: typing.Optional[str]

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]


# InferenceComponentDeploymentConfig

### RollingUpdatePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceComponentRollingUpdatePolicy'>
- **Required**: Yes

### AutoRollbackConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoRollbackConfig]


# InferenceComponentDeploymentConfigOutput

### RollingUpdatePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceComponentRollingUpdatePolicy'>
- **Required**: Yes

### AutoRollbackConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoRollbackConfigOutput]


# InferenceComponentRollingUpdatePolicy

### MaximumBatchSize
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceComponentCapacitySize'>
- **Required**: Yes

### WaitIntervalInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### MaximumExecutionTimeoutInSeconds
- **Type**: typing.Optional[int]

### RollbackMaximumBatchSize
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceComponentCapacitySize]


# InferenceComponentRuntimeConfig

### CopyCount
- **Type**: <class 'int'>
- **Required**: Yes


# InferenceComponentRuntimeConfigSummary

### DesiredCopyCount
- **Type**: typing.Optional[int]

### CurrentCopyCount
- **Type**: typing.Optional[int]


# InferenceComponentSpecification

### ModelName
- **Type**: typing.Optional[str]

### Container
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceComponentContainerSpecification]

### StartupParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceComponentStartupParameters]

### ComputeResourceRequirements
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceComponentComputeResourceRequirements]

### BaseInferenceComponentName
- **Type**: typing.Optional[str]


# InferenceComponentSpecificationSummary

### ModelName
- **Type**: typing.Optional[str]

### Container
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceComponentContainerSpecificationSummary]

### StartupParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceComponentStartupParameters]

### ComputeResourceRequirements
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceComponentComputeResourceRequirements]

### BaseInferenceComponentName
- **Type**: typing.Optional[str]


# InferenceComponentStartupParameters

### ModelDataDownloadTimeoutInSeconds
- **Type**: typing.Optional[int]

### ContainerStartupHealthCheckTimeoutInSeconds
- **Type**: typing.Optional[int]


# InferenceComponentSummary

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### InferenceComponentArn
- **Type**: <class 'str'>
- **Required**: Yes

### InferenceComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### VariantName
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### InferenceComponentStatus
- **Type**: typing.Optional[typing.Literal['Creating', 'Deleting', 'Failed', 'InService', 'Updating']]


# InferenceExecutionConfig

### Mode
- **Type**: typing.Literal['Direct', 'Serial']
- **Required**: Yes


# InferenceExperimentDataStorageConfig

### Destination
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKey
- **Type**: typing.Optional[str]

### ContentType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CaptureContentTypeHeader]


# InferenceExperimentDataStorageConfigOutput

### Destination
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKey
- **Type**: typing.Optional[str]

### ContentType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CaptureContentTypeHeaderOutput]


# InferenceExperimentSchedule

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# InferenceExperimentScheduleOutput

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]


# InferenceExperimentSummary

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['ShadowMode']
- **Required**: Yes

### Status
- **Type**: typing.Literal['Cancelled', 'Completed', 'Created', 'Creating', 'Running', 'Starting', 'Stopping', 'Updating']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceExperimentScheduleOutput]

### StatusReason
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CompletionTime
- **Type**: typing.Optional[datetime.datetime]

### RoleArn
- **Type**: typing.Optional[str]


# InferenceHubAccessConfig

### HubContentArn
- **Type**: <class 'str'>
- **Required**: Yes


# InferenceMetrics

### MaxInvocations
- **Type**: <class 'int'>
- **Required**: Yes

### ModelLatency
- **Type**: <class 'int'>
- **Required**: Yes


# InferenceRecommendation

### EndpointConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EndpointOutputConfiguration'>
- **Required**: Yes

### ModelConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelConfiguration'>
- **Required**: Yes

### RecommendationId
- **Type**: typing.Optional[str]

### Metrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.RecommendationMetrics]

### InvocationEndTime
- **Type**: typing.Optional[datetime.datetime]

### InvocationStartTime
- **Type**: typing.Optional[datetime.datetime]


# InferenceRecommendationsJob

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### JobDescription
- **Type**: <class 'str'>
- **Required**: Yes

### JobType
- **Type**: typing.Literal['Advanced', 'Default']
- **Required**: Yes

### JobArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'DELETED', 'DELETING', 'FAILED', 'IN_PROGRESS', 'PENDING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CompletionTime
- **Type**: typing.Optional[datetime.datetime]

### FailureReason
- **Type**: typing.Optional[str]

### ModelName
- **Type**: typing.Optional[str]

### SamplePayloadUrl
- **Type**: typing.Optional[str]

### ModelPackageVersionArn
- **Type**: typing.Optional[str]


# InferenceRecommendationsJobStep

### StepType
- **Type**: typing.Literal['BENCHMARK']
- **Required**: Yes

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'DELETED', 'DELETING', 'FAILED', 'IN_PROGRESS', 'PENDING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### InferenceBenchmark
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.RecommendationJobInferenceBenchmark]


# InferenceSpecification

### Containers
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelPackageContainerDefinition]
- **Required**: Yes

### SupportedTransformInstanceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge']]]

### SupportedRealtimeInferenceInstanceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.large', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c5d.18xlarge', 'ml.c5d.2xlarge', 'ml.c5d.4xlarge', 'ml.c5d.9xlarge', 'ml.c5d.large', 'ml.c5d.xlarge', 'ml.c6g.12xlarge', 'ml.c6g.16xlarge', 'ml.c6g.2xlarge', 'ml.c6g.4xlarge', 'ml.c6g.8xlarge', 'ml.c6g.large', 'ml.c6g.xlarge', 'ml.c6gd.12xlarge', 'ml.c6gd.16xlarge', 'ml.c6gd.2xlarge', 'ml.c6gd.4xlarge', 'ml.c6gd.8xlarge', 'ml.c6gd.large', 'ml.c6gd.xlarge', 'ml.c6gn.12xlarge', 'ml.c6gn.16xlarge', 'ml.c6gn.2xlarge', 'ml.c6gn.4xlarge', 'ml.c6gn.8xlarge', 'ml.c6gn.large', 'ml.c6gn.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c7g.12xlarge', 'ml.c7g.16xlarge', 'ml.c7g.2xlarge', 'ml.c7g.4xlarge', 'ml.c7g.8xlarge', 'ml.c7g.large', 'ml.c7g.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.dl1.24xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.inf1.24xlarge', 'ml.inf1.2xlarge', 'ml.inf1.6xlarge', 'ml.inf1.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6g.12xlarge', 'ml.m6g.16xlarge', 'ml.m6g.2xlarge', 'ml.m6g.4xlarge', 'ml.m6g.8xlarge', 'ml.m6g.large', 'ml.m6g.xlarge', 'ml.m6gd.12xlarge', 'ml.m6gd.16xlarge', 'ml.m6gd.2xlarge', 'ml.m6gd.4xlarge', 'ml.m6gd.8xlarge', 'ml.m6gd.large', 'ml.m6gd.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.r6g.12xlarge', 'ml.r6g.16xlarge', 'ml.r6g.2xlarge', 'ml.r6g.4xlarge', 'ml.r6g.8xlarge', 'ml.r6g.large', 'ml.r6g.xlarge', 'ml.r6gd.12xlarge', 'ml.r6gd.16xlarge', 'ml.r6gd.2xlarge', 'ml.r6gd.4xlarge', 'ml.r6gd.8xlarge', 'ml.r6gd.large', 'ml.r6gd.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.r8g.12xlarge', 'ml.r8g.16xlarge', 'ml.r8g.24xlarge', 'ml.r8g.2xlarge', 'ml.r8g.48xlarge', 'ml.r8g.4xlarge', 'ml.r8g.8xlarge', 'ml.r8g.large', 'ml.r8g.medium', 'ml.r8g.xlarge', 'ml.t2.2xlarge', 'ml.t2.large', 'ml.t2.medium', 'ml.t2.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]]

### SupportedContentTypes
- **Type**: typing.Optional[typing.List[str]]

### SupportedResponseMIMETypes
- **Type**: typing.Optional[typing.List[str]]


# InferenceSpecificationOutput

### Containers
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelPackageContainerDefinitionOutput]
- **Required**: Yes

### SupportedTransformInstanceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge']]]

### SupportedRealtimeInferenceInstanceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.large', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c5d.18xlarge', 'ml.c5d.2xlarge', 'ml.c5d.4xlarge', 'ml.c5d.9xlarge', 'ml.c5d.large', 'ml.c5d.xlarge', 'ml.c6g.12xlarge', 'ml.c6g.16xlarge', 'ml.c6g.2xlarge', 'ml.c6g.4xlarge', 'ml.c6g.8xlarge', 'ml.c6g.large', 'ml.c6g.xlarge', 'ml.c6gd.12xlarge', 'ml.c6gd.16xlarge', 'ml.c6gd.2xlarge', 'ml.c6gd.4xlarge', 'ml.c6gd.8xlarge', 'ml.c6gd.large', 'ml.c6gd.xlarge', 'ml.c6gn.12xlarge', 'ml.c6gn.16xlarge', 'ml.c6gn.2xlarge', 'ml.c6gn.4xlarge', 'ml.c6gn.8xlarge', 'ml.c6gn.large', 'ml.c6gn.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c7g.12xlarge', 'ml.c7g.16xlarge', 'ml.c7g.2xlarge', 'ml.c7g.4xlarge', 'ml.c7g.8xlarge', 'ml.c7g.large', 'ml.c7g.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.dl1.24xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.inf1.24xlarge', 'ml.inf1.2xlarge', 'ml.inf1.6xlarge', 'ml.inf1.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6g.12xlarge', 'ml.m6g.16xlarge', 'ml.m6g.2xlarge', 'ml.m6g.4xlarge', 'ml.m6g.8xlarge', 'ml.m6g.large', 'ml.m6g.xlarge', 'ml.m6gd.12xlarge', 'ml.m6gd.16xlarge', 'ml.m6gd.2xlarge', 'ml.m6gd.4xlarge', 'ml.m6gd.8xlarge', 'ml.m6gd.large', 'ml.m6gd.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.r6g.12xlarge', 'ml.r6g.16xlarge', 'ml.r6g.2xlarge', 'ml.r6g.4xlarge', 'ml.r6g.8xlarge', 'ml.r6g.large', 'ml.r6g.xlarge', 'ml.r6gd.12xlarge', 'ml.r6gd.16xlarge', 'ml.r6gd.2xlarge', 'ml.r6gd.4xlarge', 'ml.r6gd.8xlarge', 'ml.r6gd.large', 'ml.r6gd.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.r8g.12xlarge', 'ml.r8g.16xlarge', 'ml.r8g.24xlarge', 'ml.r8g.2xlarge', 'ml.r8g.48xlarge', 'ml.r8g.4xlarge', 'ml.r8g.8xlarge', 'ml.r8g.large', 'ml.r8g.medium', 'ml.r8g.xlarge', 'ml.t2.2xlarge', 'ml.t2.large', 'ml.t2.medium', 'ml.t2.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]]

### SupportedContentTypes
- **Type**: typing.Optional[typing.List[str]]

### SupportedResponseMIMETypes
- **Type**: typing.Optional[typing.List[str]]


# InfraCheckConfig

### EnableInfraCheck
- **Type**: typing.Optional[bool]


# InputConfig

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### Framework
- **Type**: typing.Literal['DARKNET', 'KERAS', 'MXNET', 'ONNX', 'PYTORCH', 'SKLEARN', 'TENSORFLOW', 'TFLITE', 'XGBOOST']
- **Required**: Yes

### DataInputConfig
- **Type**: typing.Optional[str]

### FrameworkVersion
- **Type**: typing.Optional[str]


# InstanceGroup

### InstanceType
- **Type**: typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c5n.18xlarge', 'ml.c5n.2xlarge', 'ml.c5n.4xlarge', 'ml.c5n.9xlarge', 'ml.c5n.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.16xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.8xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']
- **Required**: Yes

### InstanceCount
- **Type**: <class 'int'>
- **Required**: Yes

### InstanceGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# InstanceMetadataServiceConfiguration

### MinimumInstanceMetadataServiceVersion
- **Type**: <class 'str'>
- **Required**: Yes


# IntegerParameterRange

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MinValue
- **Type**: <class 'str'>
- **Required**: Yes

### MaxValue
- **Type**: <class 'str'>
- **Required**: Yes

### ScalingType
- **Type**: typing.Optional[typing.Literal['Auto', 'Linear', 'Logarithmic', 'ReverseLogarithmic']]


# IntegerParameterRangeSpecification

### MinValue
- **Type**: <class 'str'>
- **Required**: Yes

### MaxValue
- **Type**: <class 'str'>
- **Required**: Yes


# JupyterLabAppImageConfig

### FileSystemConfig
- **Type**: <class 'NoneType'>

### ContainerConfig
- **Type**: <class 'NoneType'>


# JupyterLabAppImageConfigOutput

### FileSystemConfig
- **Type**: <class 'NoneType'>

### ContainerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ContainerConfigOutput]


# JupyterLabAppSettings

### DefaultResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResourceSpec]

### CustomImages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CustomImage]]

### LifecycleConfigArns
- **Type**: typing.Optional[typing.List[str]]

### CodeRepositories
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CodeRepository]]

### AppLifecycleManagement
- **Type**: <class 'NoneType'>

### EmrSettings
- **Type**: <class 'NoneType'>

### BuiltInLifecycleConfigArn
- **Type**: typing.Optional[str]


# JupyterLabAppSettingsOutput

### DefaultResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResourceSpec]

### CustomImages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CustomImage]]

### LifecycleConfigArns
- **Type**: typing.Optional[typing.List[str]]

### CodeRepositories
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CodeRepository]]

### AppLifecycleManagement
- **Type**: <class 'NoneType'>

### EmrSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EmrSettingsOutput]

### BuiltInLifecycleConfigArn
- **Type**: typing.Optional[str]


# JupyterServerAppSettings

### DefaultResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResourceSpec]

### LifecycleConfigArns
- **Type**: typing.Optional[typing.List[str]]

### CodeRepositories
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CodeRepository]]


# JupyterServerAppSettingsOutput

### DefaultResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResourceSpec]

### LifecycleConfigArns
- **Type**: typing.Optional[typing.List[str]]

### CodeRepositories
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CodeRepository]]


# KendraSettings

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# KernelGatewayAppSettings

### DefaultResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResourceSpec]

### CustomImages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CustomImage]]

### LifecycleConfigArns
- **Type**: typing.Optional[typing.List[str]]


# KernelGatewayAppSettingsOutput

### DefaultResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResourceSpec]

### CustomImages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CustomImage]]

### LifecycleConfigArns
- **Type**: typing.Optional[typing.List[str]]


# KernelGatewayImageConfig

### KernelSpecs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.KernelSpec]
- **Required**: Yes

### FileSystemConfig
- **Type**: <class 'NoneType'>


# KernelGatewayImageConfigOutput

### KernelSpecs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.KernelSpec]
- **Required**: Yes

### FileSystemConfig
- **Type**: <class 'NoneType'>


# KernelSpec

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]


# LabelCounters

### TotalLabeled
- **Type**: typing.Optional[int]

### HumanLabeled
- **Type**: typing.Optional[int]

### MachineLabeled
- **Type**: typing.Optional[int]

### FailedNonRetryableError
- **Type**: typing.Optional[int]

### Unlabeled
- **Type**: typing.Optional[int]


# LabelCountersForWorkteam

### HumanLabeled
- **Type**: typing.Optional[int]

### PendingHuman
- **Type**: typing.Optional[int]

### Total
- **Type**: typing.Optional[int]


# LabelingJobAlgorithmsConfig

### LabelingJobAlgorithmSpecificationArn
- **Type**: <class 'str'>
- **Required**: Yes

### InitialActiveLearningModelArn
- **Type**: typing.Optional[str]

### LabelingJobResourceConfig
- **Type**: <class 'NoneType'>


# LabelingJobAlgorithmsConfigOutput

### LabelingJobAlgorithmSpecificationArn
- **Type**: <class 'str'>
- **Required**: Yes

### InitialActiveLearningModelArn
- **Type**: typing.Optional[str]

### LabelingJobResourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.LabelingJobResourceConfigOutput]


# LabelingJobDataAttributes

### ContentClassifiers
- **Type**: typing.Optional[typing.List[typing.Literal['FreeOfAdultContent', 'FreeOfPersonallyIdentifiableInformation']]]


# LabelingJobDataAttributesOutput

### ContentClassifiers
- **Type**: typing.Optional[typing.List[typing.Literal['FreeOfAdultContent', 'FreeOfPersonallyIdentifiableInformation']]]


# LabelingJobDataSource

### S3DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.LabelingJobS3DataSource]

### SnsDataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.LabelingJobSnsDataSource]


# LabelingJobForWorkteamSummary

### JobReferenceCode
- **Type**: <class 'str'>
- **Required**: Yes

### WorkRequesterAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LabelingJobName
- **Type**: typing.Optional[str]

### LabelCounters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.LabelCountersForWorkteam]

### NumberOfHumanWorkersPerDataObject
- **Type**: typing.Optional[int]


# LabelingJobInputConfig

### DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.LabelingJobDataSource'>
- **Required**: Yes

### DataAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.LabelingJobDataAttributes]


# LabelingJobInputConfigOutput

### DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.LabelingJobDataSource'>
- **Required**: Yes

### DataAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.LabelingJobDataAttributesOutput]


# LabelingJobOutput

### OutputDatasetS3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### FinalActiveLearningModelArn
- **Type**: typing.Optional[str]


# LabelingJobOutputConfig

### S3OutputPath
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]

### SnsTopicArn
- **Type**: typing.Optional[str]


# LabelingJobResourceConfig

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: <class 'NoneType'>


# LabelingJobResourceConfigOutput

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.VpcConfigOutput]


# LabelingJobS3DataSource

### ManifestS3Uri
- **Type**: <class 'str'>
- **Required**: Yes


# LabelingJobSnsDataSource

### SnsTopicArn
- **Type**: <class 'str'>
- **Required**: Yes


# LabelingJobStoppingConditions

### MaxHumanLabeledObjectCount
- **Type**: typing.Optional[int]

### MaxPercentageOfInputDatasetLabeled
- **Type**: typing.Optional[int]


# LabelingJobSummary

### LabelingJobName
- **Type**: <class 'str'>
- **Required**: Yes

### LabelingJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LabelingJobStatus
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Initializing', 'Stopped', 'Stopping']
- **Required**: Yes

### LabelCounters
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.LabelCounters'>
- **Required**: Yes

### WorkteamArn
- **Type**: <class 'str'>
- **Required**: Yes

### PreHumanTaskLambdaArn
- **Type**: typing.Optional[str]

### AnnotationConsolidationLambdaArn
- **Type**: typing.Optional[str]

### FailureReason
- **Type**: typing.Optional[str]

### LabelingJobOutput
- **Type**: <class 'NoneType'>

### InputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.LabelingJobInputConfigOutput]


# LambdaStepMetadata

### Arn
- **Type**: typing.Optional[str]

### OutputParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OutputParameter]]


# LastUpdateStatus

### Status
- **Type**: typing.Literal['Failed', 'InProgress', 'Successful']
- **Required**: Yes

### FailureReason
- **Type**: typing.Optional[str]


# LineageGroupSummary

### LineageGroupArn
- **Type**: typing.Optional[str]

### LineageGroupName
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# ListActionsRequest

### SourceUri
- **Type**: typing.Optional[str]

### ActionType
- **Type**: typing.Optional[str]

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListActionsRequestPaginate

### SourceUri
- **Type**: typing.Optional[str]

### ActionType
- **Type**: typing.Optional[str]

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListActionsResponse

### ActionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ActionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAlgorithmsInput

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListAlgorithmsInputPaginate

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NameContains
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListAlgorithmsOutput

### AlgorithmSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AlgorithmSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAliasesRequest

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### Alias
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[int]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAliasesRequestPaginate

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### Alias
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListAliasesResponse

### SageMakerImageVersionAliases
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAppImageConfigsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'LastModifiedTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListAppImageConfigsRequestPaginate

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'LastModifiedTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListAppImageConfigsResponse

### AppImageConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AppImageConfigDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAppsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### DomainIdEquals
- **Type**: typing.Optional[str]

### UserProfileNameEquals
- **Type**: typing.Optional[str]

### SpaceNameEquals
- **Type**: typing.Optional[str]


# ListAppsRequestPaginate

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### DomainIdEquals
- **Type**: typing.Optional[str]

### UserProfileNameEquals
- **Type**: typing.Optional[str]

### SpaceNameEquals
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListAppsResponse

### Apps
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AppDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListArtifactsRequest

### SourceUri
- **Type**: typing.Optional[str]

### ArtifactType
- **Type**: typing.Optional[str]

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListArtifactsRequestPaginate

### SourceUri
- **Type**: typing.Optional[str]

### ArtifactType
- **Type**: typing.Optional[str]

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListArtifactsResponse

### ArtifactSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ArtifactSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAssociationsRequest

### SourceArn
- **Type**: typing.Optional[str]

### DestinationArn
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[str]

### DestinationType
- **Type**: typing.Optional[str]

### AssociationType
- **Type**: typing.Optional[typing.Literal['AssociatedWith', 'ContributedTo', 'DerivedFrom', 'Produced', 'SameAs']]

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'DestinationArn', 'DestinationType', 'SourceArn', 'SourceType']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAssociationsRequestPaginate

### SourceArn
- **Type**: typing.Optional[str]

### DestinationArn
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[str]

### DestinationType
- **Type**: typing.Optional[str]

### AssociationType
- **Type**: typing.Optional[typing.Literal['AssociatedWith', 'ContributedTo', 'DerivedFrom', 'Produced', 'SameAs']]

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'DestinationArn', 'DestinationType', 'SourceArn', 'SourceType']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListAssociationsResponse

### AssociationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAutoMLJobsRequest

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAutoMLJobsRequestPaginate

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListAutoMLJobsResponse

### AutoMLJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCandidatesForAutoMLJobRequest

### AutoMLJobName
- **Type**: <class 'str'>
- **Required**: Yes

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### CandidateNameEquals
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'FinalObjectiveMetricValue', 'Status']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCandidatesForAutoMLJobRequestPaginate

### AutoMLJobName
- **Type**: <class 'str'>
- **Required**: Yes

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### CandidateNameEquals
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'FinalObjectiveMetricValue', 'Status']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListCandidatesForAutoMLJobResponse

### Candidates
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLCandidate]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListClusterNodesRequest

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### InstanceGroupNameContains
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CREATION_TIME', 'NAME']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListClusterNodesRequestPaginate

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### InstanceGroupNameContains
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CREATION_TIME', 'NAME']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListClusterNodesResponse

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterNodeSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ClusterNodeSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# ListClusterSchedulerConfigsRequest

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NameContains
- **Type**: typing.Optional[str]

### ClusterArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CreateFailed', 'CreateRollbackFailed', 'Created', 'Creating', 'DeleteFailed', 'DeleteRollbackFailed', 'Deleted', 'Deleting', 'UpdateFailed', 'UpdateRollbackFailed', 'Updated', 'Updating']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListClusterSchedulerConfigsRequestPaginate

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NameContains
- **Type**: typing.Optional[str]

### ClusterArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CreateFailed', 'CreateRollbackFailed', 'Created', 'Creating', 'DeleteFailed', 'DeleteRollbackFailed', 'Deleted', 'Deleting', 'UpdateFailed', 'UpdateRollbackFailed', 'Updated', 'Updating']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListClusterSchedulerConfigsResponse

### ClusterSchedulerConfigSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ClusterSchedulerConfigSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListClustersRequest

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CREATION_TIME', 'NAME']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### TrainingPlanArn
- **Type**: typing.Optional[str]


# ListClustersRequestPaginate

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NameContains
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CREATION_TIME', 'NAME']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### TrainingPlanArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListClustersResponse

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ClusterSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# ListCodeRepositoriesInput

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'LastModifiedTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListCodeRepositoriesInputPaginate

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NameContains
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'LastModifiedTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListCodeRepositoriesOutput

### CodeRepositorySummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CodeRepositorySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCompilationJobsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'INPROGRESS', 'STARTING', 'STOPPED', 'STOPPING']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListCompilationJobsRequestPaginate

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'INPROGRESS', 'STARTING', 'STOPPED', 'STOPPING']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListCompilationJobsResponse

### CompilationJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CompilationJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListComputeQuotasRequest

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NameContains
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CreateFailed', 'CreateRollbackFailed', 'Created', 'Creating', 'DeleteFailed', 'DeleteRollbackFailed', 'Deleted', 'Deleting', 'UpdateFailed', 'UpdateRollbackFailed', 'Updated', 'Updating']]

### ClusterArn
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['ClusterArn', 'CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListComputeQuotasRequestPaginate

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NameContains
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CreateFailed', 'CreateRollbackFailed', 'Created', 'Creating', 'DeleteFailed', 'DeleteRollbackFailed', 'Deleted', 'Deleting', 'UpdateFailed', 'UpdateRollbackFailed', 'Updated', 'Updating']]

### ClusterArn
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['ClusterArn', 'CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListComputeQuotasResponse

### ComputeQuotaSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ComputeQuotaSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListContextsRequest

### SourceUri
- **Type**: typing.Optional[str]

### ContextType
- **Type**: typing.Optional[str]

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListContextsRequestPaginate

### SourceUri
- **Type**: typing.Optional[str]

### ContextType
- **Type**: typing.Optional[str]

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListContextsResponse

### ContextSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ContextSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDataQualityJobDefinitionsRequest

### EndpointName
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# ListDataQualityJobDefinitionsRequestPaginate

### EndpointName
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListDataQualityJobDefinitionsResponse

### JobDefinitionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringJobDefinitionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDeviceFleetsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NameContains
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CREATION_TIME', 'LAST_MODIFIED_TIME', 'NAME']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListDeviceFleetsRequestPaginate

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NameContains
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CREATION_TIME', 'LAST_MODIFIED_TIME', 'NAME']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListDeviceFleetsResponse

### DeviceFleetSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DeviceFleetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDevicesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### LatestHeartbeatAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ModelName
- **Type**: typing.Optional[str]

### DeviceFleetName
- **Type**: typing.Optional[str]


# ListDevicesRequestPaginate

### LatestHeartbeatAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ModelName
- **Type**: typing.Optional[str]

### DeviceFleetName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListDevicesResponse

### DeviceSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DeviceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDomainsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDomainsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListDomainsResponse

### Domains
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DomainDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEdgeDeploymentPlansRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NameContains
- **Type**: typing.Optional[str]

### DeviceFleetNameContains
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CREATION_TIME', 'DEVICE_FLEET_NAME', 'LAST_MODIFIED_TIME', 'NAME']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListEdgeDeploymentPlansRequestPaginate

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NameContains
- **Type**: typing.Optional[str]

### DeviceFleetNameContains
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CREATION_TIME', 'DEVICE_FLEET_NAME', 'LAST_MODIFIED_TIME', 'NAME']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListEdgeDeploymentPlansResponse

### EdgeDeploymentPlanSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EdgeDeploymentPlanSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEdgePackagingJobsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NameContains
- **Type**: typing.Optional[str]

### ModelNameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'INPROGRESS', 'STARTING', 'STOPPED', 'STOPPING']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CREATION_TIME', 'LAST_MODIFIED_TIME', 'MODEL_NAME', 'NAME', 'STATUS']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListEdgePackagingJobsRequestPaginate

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NameContains
- **Type**: typing.Optional[str]

### ModelNameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'INPROGRESS', 'STARTING', 'STOPPED', 'STOPPING']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CREATION_TIME', 'LAST_MODIFIED_TIME', 'MODEL_NAME', 'NAME', 'STATUS']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListEdgePackagingJobsResponse

### EdgePackagingJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EdgePackagingJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEndpointConfigsInput

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# ListEndpointConfigsInputPaginate

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListEndpointConfigsOutput

### EndpointConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EndpointConfigSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEndpointsInput

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Creating', 'Deleting', 'Failed', 'InService', 'OutOfService', 'RollingBack', 'SystemUpdating', 'UpdateRollbackFailed', 'Updating']]


# ListEndpointsInputPaginate

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Creating', 'Deleting', 'Failed', 'InService', 'OutOfService', 'RollingBack', 'SystemUpdating', 'UpdateRollbackFailed', 'Updating']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListEndpointsOutput

### Endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EndpointSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListExperimentsRequest

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListExperimentsRequestPaginate

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListExperimentsResponse

### ExperimentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ExperimentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFeatureGroupsRequest

### NameContains
- **Type**: typing.Optional[str]

### FeatureGroupStatusEquals
- **Type**: typing.Optional[typing.Literal['CreateFailed', 'Created', 'Creating', 'DeleteFailed', 'Deleting']]

### OfflineStoreStatusEquals
- **Type**: typing.Optional[typing.Literal['Active', 'Blocked', 'Disabled']]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'FeatureGroupStatus', 'Name', 'OfflineStoreStatus']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListFeatureGroupsRequestPaginate

### NameContains
- **Type**: typing.Optional[str]

### FeatureGroupStatusEquals
- **Type**: typing.Optional[typing.Literal['CreateFailed', 'Created', 'Creating', 'DeleteFailed', 'Deleting']]

### OfflineStoreStatusEquals
- **Type**: typing.Optional[typing.Literal['Active', 'Blocked', 'Disabled']]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'FeatureGroupStatus', 'Name', 'OfflineStoreStatus']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListFeatureGroupsResponse

### FeatureGroupSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.FeatureGroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFlowDefinitionsRequest

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListFlowDefinitionsRequestPaginate

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListFlowDefinitionsResponse

### FlowDefinitionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.FlowDefinitionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHubContentVersionsRequest

### HubName
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentType
- **Type**: typing.Literal['Model', 'ModelReference', 'Notebook']
- **Required**: Yes

### HubContentName
- **Type**: <class 'str'>
- **Required**: Yes

### MinVersion
- **Type**: typing.Optional[str]

### MaxSchemaVersion
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'HubContentName', 'HubContentStatus']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListHubContentVersionsResponse

### HubContentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HubContentInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHubContentsRequest

### HubName
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentType
- **Type**: typing.Literal['Model', 'ModelReference', 'Notebook']
- **Required**: Yes

### NameContains
- **Type**: typing.Optional[str]

### MaxSchemaVersion
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'HubContentName', 'HubContentStatus']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListHubContentsResponse

### HubContentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HubContentInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHubsRequest

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortBy
- **Type**: typing.Optional[typing.Literal['AccountIdOwner', 'CreationTime', 'HubName', 'HubStatus']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListHubsResponse

### HubSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HubInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHumanTaskUisRequest

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListHumanTaskUisRequestPaginate

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListHumanTaskUisResponse

### HumanTaskUiSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HumanTaskUiSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHyperParameterTuningJobsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'DeleteFailed', 'Deleting', 'Failed', 'InProgress', 'Stopped', 'Stopping']]


# ListHyperParameterTuningJobsRequestPaginate

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'DeleteFailed', 'Deleting', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListHyperParameterTuningJobsResponse

### HyperParameterTuningJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTuningJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListImageVersionsRequest

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CREATION_TIME', 'LAST_MODIFIED_TIME', 'VERSION']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# ListImageVersionsRequestPaginate

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortBy
- **Type**: typing.Optional[typing.Literal['CREATION_TIME', 'LAST_MODIFIED_TIME', 'VERSION']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListImageVersionsResponse

### ImageVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ImageVersion]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListImagesRequest

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CREATION_TIME', 'IMAGE_NAME', 'LAST_MODIFIED_TIME']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# ListImagesRequestPaginate

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NameContains
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CREATION_TIME', 'IMAGE_NAME', 'LAST_MODIFIED_TIME']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListImagesResponse

### Images
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Image]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInferenceComponentsInput

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Creating', 'Deleting', 'Failed', 'InService', 'Updating']]

### EndpointNameEquals
- **Type**: typing.Optional[str]

### VariantNameEquals
- **Type**: typing.Optional[str]


# ListInferenceComponentsInputPaginate

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Creating', 'Deleting', 'Failed', 'InService', 'Updating']]

### EndpointNameEquals
- **Type**: typing.Optional[str]

### VariantNameEquals
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListInferenceComponentsOutput

### InferenceComponents
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceComponentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInferenceExperimentsRequest

### NameContains
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['ShadowMode']]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Cancelled', 'Completed', 'Created', 'Creating', 'Running', 'Starting', 'Stopping', 'Updating']]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListInferenceExperimentsRequestPaginate

### NameContains
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['ShadowMode']]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Cancelled', 'Completed', 'Created', 'Creating', 'Running', 'Starting', 'Stopping', 'Updating']]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListInferenceExperimentsResponse

### InferenceExperiments
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceExperimentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInferenceRecommendationsJobStepsRequest

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'DELETED', 'DELETING', 'FAILED', 'IN_PROGRESS', 'PENDING', 'STOPPED', 'STOPPING']]

### StepType
- **Type**: typing.Optional[typing.Literal['BENCHMARK']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListInferenceRecommendationsJobStepsRequestPaginate

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'DELETED', 'DELETING', 'FAILED', 'IN_PROGRESS', 'PENDING', 'STOPPED', 'STOPPING']]

### StepType
- **Type**: typing.Optional[typing.Literal['BENCHMARK']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListInferenceRecommendationsJobStepsResponse

### Steps
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceRecommendationsJobStep]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInferenceRecommendationsJobsRequest

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'DELETED', 'DELETING', 'FAILED', 'IN_PROGRESS', 'PENDING', 'STOPPED', 'STOPPING']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ModelNameEquals
- **Type**: typing.Optional[str]

### ModelPackageVersionArnEquals
- **Type**: typing.Optional[str]


# ListInferenceRecommendationsJobsRequestPaginate

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'DELETED', 'DELETING', 'FAILED', 'IN_PROGRESS', 'PENDING', 'STOPPED', 'STOPPING']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### ModelNameEquals
- **Type**: typing.Optional[str]

### ModelPackageVersionArnEquals
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListInferenceRecommendationsJobsResponse

### InferenceRecommendationsJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceRecommendationsJob]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLabelingJobsForWorkteamRequest

### WorkteamArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### JobReferenceCodeContains
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListLabelingJobsForWorkteamRequestPaginate

### WorkteamArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### JobReferenceCodeContains
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListLabelingJobsForWorkteamResponse

### LabelingJobSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.LabelingJobForWorkteamSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLabelingJobsRequest

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### NameContains
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Initializing', 'Stopped', 'Stopping']]


# ListLabelingJobsRequestPaginate

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NameContains
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Initializing', 'Stopped', 'Stopping']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListLabelingJobsResponse

### LabelingJobSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.LabelingJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLineageGroupsRequest

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListLineageGroupsRequestPaginate

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListLineageGroupsResponse

### LineageGroupSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.LineageGroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMlflowTrackingServersRequest

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### TrackingServerStatus
- **Type**: typing.Optional[typing.Literal['CreateFailed', 'Created', 'Creating', 'DeleteFailed', 'Deleting', 'MaintenanceComplete', 'MaintenanceFailed', 'MaintenanceInProgress', 'StartFailed', 'Started', 'Starting', 'StopFailed', 'Stopped', 'Stopping', 'UpdateFailed', 'Updated', 'Updating']]

### MlflowVersion
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMlflowTrackingServersRequestPaginate

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### TrackingServerStatus
- **Type**: typing.Optional[typing.Literal['CreateFailed', 'Created', 'Creating', 'DeleteFailed', 'Deleting', 'MaintenanceComplete', 'MaintenanceFailed', 'MaintenanceInProgress', 'StartFailed', 'Started', 'Starting', 'StopFailed', 'Stopped', 'Stopping', 'UpdateFailed', 'Updated', 'Updating']]

### MlflowVersion
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListMlflowTrackingServersResponse

### TrackingServerSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrackingServerSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListModelBiasJobDefinitionsRequest

### EndpointName
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# ListModelBiasJobDefinitionsRequestPaginate

### EndpointName
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListModelBiasJobDefinitionsResponse

### JobDefinitionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringJobDefinitionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListModelCardExportJobsRequest

### ModelCardName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelCardVersion
- **Type**: typing.Optional[int]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ModelCardExportJobNameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListModelCardExportJobsRequestPaginate

### ModelCardName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelCardVersion
- **Type**: typing.Optional[int]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ModelCardExportJobNameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListModelCardExportJobsResponse

### ModelCardExportJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelCardExportJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListModelCardVersionsRequest

### ModelCardName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### MaxResults
- **Type**: typing.Optional[int]

### ModelCardStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'Archived', 'Draft', 'PendingReview']]

### NextToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['Version']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListModelCardVersionsRequestPaginate

### ModelCardName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ModelCardStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'Archived', 'Draft', 'PendingReview']]

### SortBy
- **Type**: typing.Optional[typing.Literal['Version']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListModelCardVersionsResponse

### ModelCardVersionSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelCardVersionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListModelCardsRequest

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### ModelCardStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'Archived', 'Draft', 'PendingReview']]

### NextToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListModelCardsRequestPaginate

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NameContains
- **Type**: typing.Optional[str]

### ModelCardStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'Archived', 'Draft', 'PendingReview']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListModelCardsResponse

### ModelCardSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelCardSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListModelExplainabilityJobDefinitionsRequest

### EndpointName
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# ListModelExplainabilityJobDefinitionsRequestPaginate

### EndpointName
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListModelExplainabilityJobDefinitionsResponse

### JobDefinitionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringJobDefinitionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListModelMetadataRequest

### SearchExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelMetadataSearchExpression]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListModelMetadataRequestPaginate

### SearchExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelMetadataSearchExpression]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListModelMetadataResponse

### ModelMetadataSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelMetadataSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListModelPackageGroupsInput

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### CrossAccountFilterOption
- **Type**: typing.Optional[typing.Literal['CrossAccount', 'SameAccount']]


# ListModelPackageGroupsInputPaginate

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NameContains
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### CrossAccountFilterOption
- **Type**: typing.Optional[typing.Literal['CrossAccount', 'SameAccount']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListModelPackageGroupsOutput

### ModelPackageGroupSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelPackageGroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListModelPackagesInput

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### ModelApprovalStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'PendingManualApproval', 'Rejected']]

### ModelPackageGroupName
- **Type**: typing.Optional[str]

### ModelPackageType
- **Type**: typing.Optional[typing.Literal['Both', 'Unversioned', 'Versioned']]

### NextToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListModelPackagesInputPaginate

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NameContains
- **Type**: typing.Optional[str]

### ModelApprovalStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'PendingManualApproval', 'Rejected']]

### ModelPackageGroupName
- **Type**: typing.Optional[str]

### ModelPackageType
- **Type**: typing.Optional[typing.Literal['Both', 'Unversioned', 'Versioned']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListModelPackagesOutput

### ModelPackageSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelPackageSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListModelQualityJobDefinitionsRequest

### EndpointName
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# ListModelQualityJobDefinitionsRequestPaginate

### EndpointName
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListModelQualityJobDefinitionsResponse

### JobDefinitionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringJobDefinitionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListModelsInput

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# ListModelsInputPaginate

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListModelsOutput

### Models
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMonitoringAlertHistoryRequest

### MonitoringScheduleName
- **Type**: typing.Optional[str]

### MonitoringAlertName
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['InAlert', 'OK']]


# ListMonitoringAlertHistoryRequestPaginate

### MonitoringScheduleName
- **Type**: typing.Optional[str]

### MonitoringAlertName
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['InAlert', 'OK']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListMonitoringAlertHistoryResponse

### MonitoringAlertHistory
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringAlertHistorySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMonitoringAlertsRequest

### MonitoringScheduleName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMonitoringAlertsRequestPaginate

### MonitoringScheduleName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListMonitoringAlertsResponse

### MonitoringAlertSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringAlertSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMonitoringExecutionsRequest

### MonitoringScheduleName
- **Type**: typing.Optional[str]

### EndpointName
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'ScheduledTime', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ScheduledTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ScheduledTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'CompletedWithViolations', 'Failed', 'InProgress', 'Pending', 'Stopped', 'Stopping']]

### MonitoringJobDefinitionName
- **Type**: typing.Optional[str]

### MonitoringTypeEquals
- **Type**: typing.Optional[typing.Literal['DataQuality', 'ModelBias', 'ModelExplainability', 'ModelQuality']]


# ListMonitoringExecutionsRequestPaginate

### MonitoringScheduleName
- **Type**: typing.Optional[str]

### EndpointName
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'ScheduledTime', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### ScheduledTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ScheduledTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'CompletedWithViolations', 'Failed', 'InProgress', 'Pending', 'Stopped', 'Stopping']]

### MonitoringJobDefinitionName
- **Type**: typing.Optional[str]

### MonitoringTypeEquals
- **Type**: typing.Optional[typing.Literal['DataQuality', 'ModelBias', 'ModelExplainability', 'ModelQuality']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListMonitoringExecutionsResponse

### MonitoringExecutionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringExecutionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMonitoringSchedulesRequest

### EndpointName
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Failed', 'Pending', 'Scheduled', 'Stopped']]

### MonitoringJobDefinitionName
- **Type**: typing.Optional[str]

### MonitoringTypeEquals
- **Type**: typing.Optional[typing.Literal['DataQuality', 'ModelBias', 'ModelExplainability', 'ModelQuality']]


# ListMonitoringSchedulesRequestPaginate

### EndpointName
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Failed', 'Pending', 'Scheduled', 'Stopped']]

### MonitoringJobDefinitionName
- **Type**: typing.Optional[str]

### MonitoringTypeEquals
- **Type**: typing.Optional[typing.Literal['DataQuality', 'ModelBias', 'ModelExplainability', 'ModelQuality']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListMonitoringSchedulesResponse

### MonitoringScheduleSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringScheduleSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNotebookInstanceLifecycleConfigsInput

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'LastModifiedTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# ListNotebookInstanceLifecycleConfigsInputPaginate

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'LastModifiedTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListNotebookInstanceLifecycleConfigsOutput

### NotebookInstanceLifecycleConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.NotebookInstanceLifecycleConfigSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNotebookInstancesInput

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Deleting', 'Failed', 'InService', 'Pending', 'Stopped', 'Stopping', 'Updating']]

### NotebookInstanceLifecycleConfigNameContains
- **Type**: typing.Optional[str]

### DefaultCodeRepositoryContains
- **Type**: typing.Optional[str]

### AdditionalCodeRepositoryEquals
- **Type**: typing.Optional[str]


# ListNotebookInstancesInputPaginate

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Deleting', 'Failed', 'InService', 'Pending', 'Stopped', 'Stopping', 'Updating']]

### NotebookInstanceLifecycleConfigNameContains
- **Type**: typing.Optional[str]

### DefaultCodeRepositoryContains
- **Type**: typing.Optional[str]

### AdditionalCodeRepositoryEquals
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListNotebookInstancesOutput

### NotebookInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.NotebookInstanceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOptimizationJobsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### OptimizationContains
- **Type**: typing.Optional[str]

### NameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'INPROGRESS', 'STARTING', 'STOPPED', 'STOPPING']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListOptimizationJobsRequestPaginate

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### OptimizationContains
- **Type**: typing.Optional[str]

### NameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'INPROGRESS', 'STARTING', 'STOPPED', 'STOPPING']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListOptimizationJobsResponse

### OptimizationJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OptimizationJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPartnerAppsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPartnerAppsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListPartnerAppsResponse

### Summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PartnerAppSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPipelineExecutionStepsRequest

### PipelineExecutionArn
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListPipelineExecutionStepsRequestPaginate

### PipelineExecutionArn
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListPipelineExecutionStepsResponse

### PipelineExecutionSteps
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PipelineExecutionStep]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPipelineExecutionsRequest

### PipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'PipelineExecutionArn']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPipelineExecutionsRequestPaginate

### PipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'PipelineExecutionArn']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListPipelineExecutionsResponse

### PipelineExecutionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PipelineExecutionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPipelineParametersForExecutionRequest

### PipelineExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPipelineParametersForExecutionRequestPaginate

### PipelineExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListPipelineParametersForExecutionResponse

### PipelineParameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Parameter]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPipelinesRequest

### PipelineNamePrefix
- **Type**: typing.Optional[str]

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPipelinesRequestPaginate

### PipelineNamePrefix
- **Type**: typing.Optional[str]

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListPipelinesResponse

### PipelineSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PipelineSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProcessingJobsRequest

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListProcessingJobsRequestPaginate

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListProcessingJobsResponse

### ProcessingJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProcessingJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProjectsInput

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListProjectsOutput

### ProjectSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProjectSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourceCatalogsRequest

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListResourceCatalogsRequestPaginate

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListResourceCatalogsResponse

### ResourceCatalogs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResourceCatalog]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSpacesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'LastModifiedTime']]

### DomainIdEquals
- **Type**: typing.Optional[str]

### SpaceNameContains
- **Type**: typing.Optional[str]


# ListSpacesRequestPaginate

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'LastModifiedTime']]

### DomainIdEquals
- **Type**: typing.Optional[str]

### SpaceNameContains
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListSpacesResponse

### Spaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SpaceDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStageDevicesRequest

### EdgeDeploymentPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### StageName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ExcludeDevicesDeployedInOtherStage
- **Type**: typing.Optional[bool]


# ListStageDevicesRequestPaginate

### EdgeDeploymentPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### StageName
- **Type**: <class 'str'>
- **Required**: Yes

### ExcludeDevicesDeployedInOtherStage
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListStageDevicesResponse

### DeviceDeploymentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DeviceDeploymentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStudioLifecycleConfigsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### NameContains
- **Type**: typing.Optional[str]

### AppTypeEquals
- **Type**: typing.Optional[typing.Literal['CodeEditor', 'JupyterLab', 'JupyterServer', 'KernelGateway']]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'LastModifiedTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListStudioLifecycleConfigsRequestPaginate

### NameContains
- **Type**: typing.Optional[str]

### AppTypeEquals
- **Type**: typing.Optional[typing.Literal['CodeEditor', 'JupyterLab', 'JupyterServer', 'KernelGateway']]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'LastModifiedTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListStudioLifecycleConfigsResponse

### StudioLifecycleConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.StudioLifecycleConfigDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSubscribedWorkteamsRequest

### NameContains
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListSubscribedWorkteamsRequestPaginate

### NameContains
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListSubscribedWorkteamsResponse

### SubscribedWorkteams
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SubscribedWorkteam]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTagsInputPaginate

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListTagsOutput

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTrainingJobsForHyperParameterTuningJobRequest

### HyperParameterTuningJobName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'FinalObjectiveMetricValue', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListTrainingJobsForHyperParameterTuningJobRequestPaginate

### HyperParameterTuningJobName
- **Type**: <class 'str'>
- **Required**: Yes

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'FinalObjectiveMetricValue', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListTrainingJobsForHyperParameterTuningJobResponse

### TrainingJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTrainingJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTrainingJobsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### WarmPoolStatusEquals
- **Type**: typing.Optional[typing.Literal['Available', 'InUse', 'Reused', 'Terminated']]

### TrainingPlanArnEquals
- **Type**: typing.Optional[str]


# ListTrainingJobsRequestPaginate

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### WarmPoolStatusEquals
- **Type**: typing.Optional[typing.Literal['Available', 'InUse', 'Reused', 'Terminated']]

### TrainingPlanArnEquals
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListTrainingJobsResponse

### TrainingJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrainingJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTrainingPlansRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### StartTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### StartTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortBy
- **Type**: typing.Optional[typing.Literal['StartTime', 'Status', 'TrainingPlanName']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrainingPlanFilter]]


# ListTrainingPlansRequestPaginate

### StartTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### StartTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortBy
- **Type**: typing.Optional[typing.Literal['StartTime', 'Status', 'TrainingPlanName']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrainingPlanFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListTrainingPlansResponse

### TrainingPlanSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrainingPlanSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTransformJobsRequest

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTransformJobsRequestPaginate

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListTransformJobsResponse

### TransformJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TransformJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTrialComponentsRequest

### ExperimentName
- **Type**: typing.Optional[str]

### TrialName
- **Type**: typing.Optional[str]

### SourceArn
- **Type**: typing.Optional[str]

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTrialComponentsRequestPaginate

### ExperimentName
- **Type**: typing.Optional[str]

### TrialName
- **Type**: typing.Optional[str]

### SourceArn
- **Type**: typing.Optional[str]

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListTrialComponentsResponse

### TrialComponentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrialComponentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTrialsRequest

### ExperimentName
- **Type**: typing.Optional[str]

### TrialComponentName
- **Type**: typing.Optional[str]

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTrialsRequestPaginate

### ExperimentName
- **Type**: typing.Optional[str]

### TrialComponentName
- **Type**: typing.Optional[str]

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListTrialsResponse

### TrialSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrialSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListUserProfilesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'LastModifiedTime']]

### DomainIdEquals
- **Type**: typing.Optional[str]

### UserProfileNameContains
- **Type**: typing.Optional[str]


# ListUserProfilesRequestPaginate

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'LastModifiedTime']]

### DomainIdEquals
- **Type**: typing.Optional[str]

### UserProfileNameContains
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListUserProfilesResponse

### UserProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserProfileDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListWorkforcesRequest

### SortBy
- **Type**: typing.Optional[typing.Literal['CreateDate', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListWorkforcesRequestPaginate

### SortBy
- **Type**: typing.Optional[typing.Literal['CreateDate', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListWorkforcesResponse

### Workforces
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Workforce]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListWorkteamsRequest

### SortBy
- **Type**: typing.Optional[typing.Literal['CreateDate', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListWorkteamsRequestPaginate

### SortBy
- **Type**: typing.Optional[typing.Literal['CreateDate', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# ListWorkteamsResponse

### Workteams
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Workteam]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MemberDefinition

### CognitoMemberDefinition
- **Type**: <class 'NoneType'>

### OidcMemberDefinition
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OidcMemberDefinition, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OidcMemberDefinitionOutput, NoneType]


# MemberDefinitionOutput

### CognitoMemberDefinition
- **Type**: <class 'NoneType'>

### OidcMemberDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OidcMemberDefinitionOutput]


# MetadataProperties

### CommitId
- **Type**: typing.Optional[str]

### Repository
- **Type**: typing.Optional[str]

### GeneratedBy
- **Type**: typing.Optional[str]

### ProjectId
- **Type**: typing.Optional[str]


# MetricData

### MetricName
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[float]

### Timestamp
- **Type**: typing.Optional[datetime.datetime]


# MetricDatum

### MetricName
- **Type**: typing.Optional[typing.Literal['AUC', 'Accuracy', 'AverageWeightedQuantileLoss', 'BalancedAccuracy', 'F1', 'F1macro', 'MAE', 'MAPE', 'MASE', 'MSE', 'Precision', 'PrecisionMacro', 'R2', 'RMSE', 'Recall', 'RecallMacro', 'WAPE']]

### Value
- **Type**: typing.Optional[float]

### Set
- **Type**: typing.Optional[typing.Literal['Test', 'Train', 'Validation']]

### StandardMetricName
- **Type**: typing.Optional[typing.Literal['AUC', 'Accuracy', 'AverageWeightedQuantileLoss', 'BalancedAccuracy', 'F1', 'F1macro', 'InferenceLatency', 'LogLoss', 'MAE', 'MAPE', 'MASE', 'MSE', 'Perplexity', 'Precision', 'PrecisionMacro', 'R2', 'RMSE', 'Recall', 'RecallMacro', 'Rouge1', 'Rouge2', 'RougeL', 'RougeLSum', 'TrainingLoss', 'ValidationLoss', 'WAPE']]


# MetricDefinition

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Regex
- **Type**: <class 'str'>
- **Required**: Yes


# MetricSpecification

### Predefined
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PredefinedMetricSpecification]

### Customized
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CustomizedMetricSpecification]


# MetricsSource

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### ContentDigest
- **Type**: typing.Optional[str]


# Model

### ModelName
- **Type**: typing.Optional[str]

### PrimaryContainer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ContainerDefinitionOutput]

### Containers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ContainerDefinitionOutput]]

### InferenceExecutionConfig
- **Type**: <class 'NoneType'>

### ExecutionRoleArn
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.VpcConfigOutput]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### ModelArn
- **Type**: typing.Optional[str]

### EnableNetworkIsolation
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]

### DeploymentRecommendation
- **Type**: <class 'NoneType'>


# ModelAccessConfig

### AcceptEula
- **Type**: <class 'bool'>
- **Required**: Yes


# ModelArtifacts

### S3ModelArtifacts
- **Type**: <class 'str'>
- **Required**: Yes


# ModelBiasAppSpecification

### ImageUri
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigUri
- **Type**: <class 'str'>
- **Required**: Yes

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]


# ModelBiasAppSpecificationOutput

### ImageUri
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigUri
- **Type**: <class 'str'>
- **Required**: Yes

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]


# ModelBiasBaselineConfig

### BaseliningJobName
- **Type**: typing.Optional[str]

### ConstraintsResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringConstraintsResource]


# ModelBiasJobInput

### GroundTruthS3Input
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringGroundTruthS3Input'>
- **Required**: Yes

### EndpointInput
- **Type**: <class 'NoneType'>

### BatchTransformInput
- **Type**: <class 'NoneType'>


# ModelBiasJobInputOutput

### GroundTruthS3Input
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringGroundTruthS3Input'>
- **Required**: Yes

### EndpointInput
- **Type**: <class 'NoneType'>

### BatchTransformInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.BatchTransformInputOutput]


# ModelCard

### ModelCardArn
- **Type**: typing.Optional[str]

### ModelCardName
- **Type**: typing.Optional[str]

### ModelCardVersion
- **Type**: typing.Optional[int]

### Content
- **Type**: typing.Optional[str]

### ModelCardStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'Archived', 'Draft', 'PendingReview']]

### SecurityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelCardSecurityConfig]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]

### ModelId
- **Type**: typing.Optional[str]

### RiskRating
- **Type**: typing.Optional[str]

### ModelPackageGroupName
- **Type**: typing.Optional[str]


# ModelCardExportArtifacts

### S3ExportArtifacts
- **Type**: <class 'str'>
- **Required**: Yes


# ModelCardExportJobSummary

### ModelCardExportJobName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelCardExportJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress']
- **Required**: Yes

### ModelCardName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelCardVersion
- **Type**: <class 'int'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ModelCardExportOutputConfig

### S3OutputPath
- **Type**: <class 'str'>
- **Required**: Yes


# ModelCardSecurityConfig

### KmsKeyId
- **Type**: typing.Optional[str]


# ModelCardSummary

### ModelCardName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelCardArn
- **Type**: <class 'str'>
- **Required**: Yes

### ModelCardStatus
- **Type**: typing.Literal['Approved', 'Archived', 'Draft', 'PendingReview']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# ModelCardVersionSummary

### ModelCardName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelCardArn
- **Type**: <class 'str'>
- **Required**: Yes

### ModelCardStatus
- **Type**: typing.Literal['Approved', 'Archived', 'Draft', 'PendingReview']
- **Required**: Yes

### ModelCardVersion
- **Type**: <class 'int'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# ModelClientConfig

### InvocationsTimeoutInSeconds
- **Type**: typing.Optional[int]

### InvocationsMaxRetries
- **Type**: typing.Optional[int]


# ModelCompilationConfig

### Image
- **Type**: typing.Optional[str]

### OverrideEnvironment
- **Type**: typing.Optional[typing.Dict[str, str]]


# ModelCompilationConfigOutput

### Image
- **Type**: typing.Optional[str]

### OverrideEnvironment
- **Type**: typing.Optional[typing.Dict[str, str]]


# ModelConfiguration

### InferenceSpecificationName
- **Type**: typing.Optional[str]

### EnvironmentParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EnvironmentParameter]]

### CompilationJobName
- **Type**: typing.Optional[str]


# ModelDashboardEndpoint

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndpointStatus
- **Type**: typing.Literal['Creating', 'Deleting', 'Failed', 'InService', 'OutOfService', 'RollingBack', 'SystemUpdating', 'UpdateRollbackFailed', 'Updating']
- **Required**: Yes


# ModelDashboardIndicatorAction

### Enabled
- **Type**: typing.Optional[bool]


# ModelDashboardModel

### Model
- **Type**: <class 'NoneType'>

### Endpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelDashboardEndpoint]]

### LastBatchTransformJob
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TransformJob]

### MonitoringSchedules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelDashboardMonitoringSchedule]]

### ModelCard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelDashboardModelCard]


# ModelDashboardModelCard

### ModelCardArn
- **Type**: typing.Optional[str]

### ModelCardName
- **Type**: typing.Optional[str]

### ModelCardVersion
- **Type**: typing.Optional[int]

### ModelCardStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'Archived', 'Draft', 'PendingReview']]

### SecurityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelCardSecurityConfig]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]

### ModelId
- **Type**: typing.Optional[str]

### RiskRating
- **Type**: typing.Optional[str]


# ModelDashboardMonitoringSchedule

### MonitoringScheduleArn
- **Type**: typing.Optional[str]

### MonitoringScheduleName
- **Type**: typing.Optional[str]

### MonitoringScheduleStatus
- **Type**: typing.Optional[typing.Literal['Failed', 'Pending', 'Scheduled', 'Stopped']]

### MonitoringType
- **Type**: typing.Optional[typing.Literal['DataQuality', 'ModelBias', 'ModelExplainability', 'ModelQuality']]

### FailureReason
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### MonitoringScheduleConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringScheduleConfigOutput]

### EndpointName
- **Type**: typing.Optional[str]

### MonitoringAlertSummaries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringAlertSummary]]

### LastMonitoringExecutionSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringExecutionSummary]

### BatchTransformInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.BatchTransformInputOutput]


# ModelDataQuality

### Statistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MetricsSource]

### Constraints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MetricsSource]


# ModelDataSource

### S3DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.S3ModelDataSource]


# ModelDeployConfig

### AutoGenerateEndpointName
- **Type**: typing.Optional[bool]

### EndpointName
- **Type**: typing.Optional[str]


# ModelDeployResult

### EndpointName
- **Type**: typing.Optional[str]


# ModelDigests

### ArtifactDigest
- **Type**: typing.Optional[str]


# ModelExplainabilityAppSpecification

### ImageUri
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigUri
- **Type**: <class 'str'>
- **Required**: Yes

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]


# ModelExplainabilityAppSpecificationOutput

### ImageUri
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigUri
- **Type**: <class 'str'>
- **Required**: Yes

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]


# ModelExplainabilityBaselineConfig

### BaseliningJobName
- **Type**: typing.Optional[str]

### ConstraintsResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringConstraintsResource]


# ModelExplainabilityJobInput

### EndpointInput
- **Type**: <class 'NoneType'>

### BatchTransformInput
- **Type**: <class 'NoneType'>


# ModelExplainabilityJobInputOutput

### EndpointInput
- **Type**: <class 'NoneType'>

### BatchTransformInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.BatchTransformInputOutput]


# ModelInfrastructureConfig

### InfrastructureType
- **Type**: typing.Literal['RealTimeInference']
- **Required**: Yes

### RealTimeInferenceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.RealTimeInferenceConfig'>
- **Required**: Yes


# ModelInput

### DataInputConfig
- **Type**: <class 'str'>
- **Required**: Yes


# ModelLatencyThreshold

### Percentile
- **Type**: typing.Optional[str]

### ValueInMilliseconds
- **Type**: typing.Optional[int]


# ModelLifeCycle

### Stage
- **Type**: <class 'str'>
- **Required**: Yes

### StageStatus
- **Type**: <class 'str'>
- **Required**: Yes

### StageDescription
- **Type**: typing.Optional[str]


# ModelMetadataFilter

### Name
- **Type**: typing.Literal['Domain', 'Framework', 'FrameworkVersion', 'Task']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ModelMetadataSearchExpression

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelMetadataFilter]]


# ModelMetadataSummary

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### Framework
- **Type**: <class 'str'>
- **Required**: Yes

### Task
- **Type**: <class 'str'>
- **Required**: Yes

### Model
- **Type**: <class 'str'>
- **Required**: Yes

### FrameworkVersion
- **Type**: <class 'str'>
- **Required**: Yes


# ModelMetrics

### ModelQuality
- **Type**: <class 'NoneType'>

### ModelDataQuality
- **Type**: <class 'NoneType'>

### Bias
- **Type**: <class 'NoneType'>

### Explainability
- **Type**: <class 'NoneType'>


# ModelPackage

### ModelPackageName
- **Type**: typing.Optional[str]

### ModelPackageGroupName
- **Type**: typing.Optional[str]

### ModelPackageVersion
- **Type**: typing.Optional[int]

### ModelPackageArn
- **Type**: typing.Optional[str]

### ModelPackageDescription
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### InferenceSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceSpecificationOutput]

### SourceAlgorithmSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SourceAlgorithmSpecificationOutput]

### ValidationSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelPackageValidationSpecificationOutput]

### ModelPackageStatus
- **Type**: typing.Optional[typing.Literal['Completed', 'Deleting', 'Failed', 'InProgress', 'Pending']]

### ModelPackageStatusDetails
- **Type**: <class 'NoneType'>

### CertifyForMarketplace
- **Type**: typing.Optional[bool]

### ModelApprovalStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'PendingManualApproval', 'Rejected']]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext]

### MetadataProperties
- **Type**: <class 'NoneType'>

### ModelMetrics
- **Type**: <class 'NoneType'>

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext]

### ApprovalDescription
- **Type**: typing.Optional[str]

### Domain
- **Type**: typing.Optional[str]

### Task
- **Type**: typing.Optional[str]

### SamplePayloadUrl
- **Type**: typing.Optional[str]

### AdditionalInferenceSpecifications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AdditionalInferenceSpecificationDefinitionOutput]]

### SourceUri
- **Type**: typing.Optional[str]

### SecurityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelPackageSecurityConfig]

### ModelCard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelPackageModelCard]

### ModelLifeCycle
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]

### CustomerMetadataProperties
- **Type**: typing.Optional[typing.Dict[str, str]]

### DriftCheckBaselines
- **Type**: <class 'NoneType'>

### SkipModelValidation
- **Type**: typing.Optional[typing.Literal['All', 'None']]


# ModelPackageContainerDefinition

### Image
- **Type**: <class 'str'>
- **Required**: Yes

### ContainerHostname
- **Type**: typing.Optional[str]

### ImageDigest
- **Type**: typing.Optional[str]

### ModelDataUrl
- **Type**: typing.Optional[str]

### ModelDataSource
- **Type**: <class 'NoneType'>

### ProductId
- **Type**: typing.Optional[str]

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]

### ModelInput
- **Type**: <class 'NoneType'>

### Framework
- **Type**: typing.Optional[str]

### FrameworkVersion
- **Type**: typing.Optional[str]

### NearestModelName
- **Type**: typing.Optional[str]

### AdditionalS3DataSource
- **Type**: <class 'NoneType'>

### ModelDataETag
- **Type**: typing.Optional[str]


# ModelPackageContainerDefinitionOutput

### Image
- **Type**: <class 'str'>
- **Required**: Yes

### ContainerHostname
- **Type**: typing.Optional[str]

### ImageDigest
- **Type**: typing.Optional[str]

### ModelDataUrl
- **Type**: typing.Optional[str]

### ModelDataSource
- **Type**: <class 'NoneType'>

### ProductId
- **Type**: typing.Optional[str]

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]

### ModelInput
- **Type**: <class 'NoneType'>

### Framework
- **Type**: typing.Optional[str]

### FrameworkVersion
- **Type**: typing.Optional[str]

### NearestModelName
- **Type**: typing.Optional[str]

### AdditionalS3DataSource
- **Type**: <class 'NoneType'>

### ModelDataETag
- **Type**: typing.Optional[str]


# ModelPackageGroup

### ModelPackageGroupName
- **Type**: typing.Optional[str]

### ModelPackageGroupArn
- **Type**: typing.Optional[str]

### ModelPackageGroupDescription
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext]

### ModelPackageGroupStatus
- **Type**: typing.Optional[typing.Literal['Completed', 'DeleteFailed', 'Deleting', 'Failed', 'InProgress', 'Pending']]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# ModelPackageGroupSummary

### ModelPackageGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelPackageGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ModelPackageGroupStatus
- **Type**: typing.Literal['Completed', 'DeleteFailed', 'Deleting', 'Failed', 'InProgress', 'Pending']
- **Required**: Yes

### ModelPackageGroupDescription
- **Type**: typing.Optional[str]


# ModelPackageModelCard

### ModelCardContent
- **Type**: typing.Optional[str]

### ModelCardStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'Archived', 'Draft', 'PendingReview']]


# ModelPackageSecurityConfig

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes


# ModelPackageStatusDetails

### ValidationStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelPackageStatusItem]
- **Required**: Yes

### ImageScanStatuses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelPackageStatusItem]]


# ModelPackageStatusItem

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'NotStarted']
- **Required**: Yes

### FailureReason
- **Type**: typing.Optional[str]


# ModelPackageSummary

### ModelPackageArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ModelPackageStatus
- **Type**: typing.Literal['Completed', 'Deleting', 'Failed', 'InProgress', 'Pending']
- **Required**: Yes

### ModelPackageName
- **Type**: typing.Optional[str]

### ModelPackageGroupName
- **Type**: typing.Optional[str]

### ModelPackageVersion
- **Type**: typing.Optional[int]

### ModelPackageDescription
- **Type**: typing.Optional[str]

### ModelApprovalStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'PendingManualApproval', 'Rejected']]


# ModelPackageValidationProfile

### ProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### TransformJobDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TransformJobDefinition'>
- **Required**: Yes


# ModelPackageValidationProfileOutput

### ProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### TransformJobDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TransformJobDefinitionOutput'>
- **Required**: Yes


# ModelPackageValidationSpecification

### ValidationRole
- **Type**: <class 'str'>
- **Required**: Yes

### ValidationProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelPackageValidationProfile]
- **Required**: Yes


# ModelPackageValidationSpecificationOutput

### ValidationRole
- **Type**: <class 'str'>
- **Required**: Yes

### ValidationProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelPackageValidationProfileOutput]
- **Required**: Yes


# ModelQuality

### Statistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MetricsSource]

### Constraints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MetricsSource]


# ModelQualityAppSpecification

### ImageUri
- **Type**: <class 'str'>
- **Required**: Yes

### ContainerEntrypoint
- **Type**: typing.Optional[typing.List[str]]

### ContainerArguments
- **Type**: typing.Optional[typing.List[str]]

### RecordPreprocessorSourceUri
- **Type**: typing.Optional[str]

### PostAnalyticsProcessorSourceUri
- **Type**: typing.Optional[str]

### ProblemType
- **Type**: typing.Optional[typing.Literal['BinaryClassification', 'MulticlassClassification', 'Regression']]

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]


# ModelQualityAppSpecificationOutput

### ImageUri
- **Type**: <class 'str'>
- **Required**: Yes

### ContainerEntrypoint
- **Type**: typing.Optional[typing.List[str]]

### ContainerArguments
- **Type**: typing.Optional[typing.List[str]]

### RecordPreprocessorSourceUri
- **Type**: typing.Optional[str]

### PostAnalyticsProcessorSourceUri
- **Type**: typing.Optional[str]

### ProblemType
- **Type**: typing.Optional[typing.Literal['BinaryClassification', 'MulticlassClassification', 'Regression']]

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]


# ModelQualityBaselineConfig

### BaseliningJobName
- **Type**: typing.Optional[str]

### ConstraintsResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringConstraintsResource]


# ModelQualityJobInput

### GroundTruthS3Input
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringGroundTruthS3Input'>
- **Required**: Yes

### EndpointInput
- **Type**: <class 'NoneType'>

### BatchTransformInput
- **Type**: <class 'NoneType'>


# ModelQualityJobInputOutput

### GroundTruthS3Input
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringGroundTruthS3Input'>
- **Required**: Yes

### EndpointInput
- **Type**: <class 'NoneType'>

### BatchTransformInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.BatchTransformInputOutput]


# ModelQuantizationConfig

### Image
- **Type**: typing.Optional[str]

### OverrideEnvironment
- **Type**: typing.Optional[typing.Dict[str, str]]


# ModelQuantizationConfigOutput

### Image
- **Type**: typing.Optional[str]

### OverrideEnvironment
- **Type**: typing.Optional[typing.Dict[str, str]]


# ModelRegisterSettings

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### CrossAccountModelRegisterRoleArn
- **Type**: typing.Optional[str]


# ModelShardingConfig

### Image
- **Type**: typing.Optional[str]

### OverrideEnvironment
- **Type**: typing.Optional[typing.Dict[str, str]]


# ModelShardingConfigOutput

### Image
- **Type**: typing.Optional[str]

### OverrideEnvironment
- **Type**: typing.Optional[typing.Dict[str, str]]


# ModelStepMetadata

### Arn
- **Type**: typing.Optional[str]


# ModelSummary

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ModelVariantConfig

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### VariantName
- **Type**: <class 'str'>
- **Required**: Yes

### InfrastructureConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelInfrastructureConfig'>
- **Required**: Yes


# ModelVariantConfigSummary

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### VariantName
- **Type**: <class 'str'>
- **Required**: Yes

### InfrastructureConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelInfrastructureConfig'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Creating', 'Deleted', 'Deleting', 'InService', 'Updating']
- **Required**: Yes


# MonitoringAlertActions

### ModelDashboardIndicator
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelDashboardIndicatorAction]


# MonitoringAlertHistorySummary

### MonitoringScheduleName
- **Type**: <class 'str'>
- **Required**: Yes

### MonitoringAlertName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AlertStatus
- **Type**: typing.Literal['InAlert', 'OK']
- **Required**: Yes


# MonitoringAlertSummary

### MonitoringAlertName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AlertStatus
- **Type**: typing.Literal['InAlert', 'OK']
- **Required**: Yes

### DatapointsToAlert
- **Type**: <class 'int'>
- **Required**: Yes

### EvaluationPeriod
- **Type**: <class 'int'>
- **Required**: Yes

### Actions
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringAlertActions'>
- **Required**: Yes


# MonitoringAppSpecification

### ImageUri
- **Type**: <class 'str'>
- **Required**: Yes

### ContainerEntrypoint
- **Type**: typing.Optional[typing.List[str]]

### ContainerArguments
- **Type**: typing.Optional[typing.List[str]]

### RecordPreprocessorSourceUri
- **Type**: typing.Optional[str]

### PostAnalyticsProcessorSourceUri
- **Type**: typing.Optional[str]


# MonitoringAppSpecificationOutput

### ImageUri
- **Type**: <class 'str'>
- **Required**: Yes

### ContainerEntrypoint
- **Type**: typing.Optional[typing.List[str]]

### ContainerArguments
- **Type**: typing.Optional[typing.List[str]]

### RecordPreprocessorSourceUri
- **Type**: typing.Optional[str]

### PostAnalyticsProcessorSourceUri
- **Type**: typing.Optional[str]


# MonitoringBaselineConfig

### BaseliningJobName
- **Type**: typing.Optional[str]

### ConstraintsResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringConstraintsResource]

### StatisticsResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringStatisticsResource]


# MonitoringClusterConfig

### InstanceCount
- **Type**: <class 'int'>
- **Required**: Yes

### InstanceType
- **Type**: typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.16xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.8xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge']
- **Required**: Yes

### VolumeSizeInGB
- **Type**: <class 'int'>
- **Required**: Yes

### VolumeKmsKeyId
- **Type**: typing.Optional[str]


# MonitoringConstraintsResource

### S3Uri
- **Type**: typing.Optional[str]


# MonitoringCsvDatasetFormat

### Header
- **Type**: typing.Optional[bool]


# MonitoringDatasetFormat

### Csv
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringCsvDatasetFormat]

### Json
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringJsonDatasetFormat]

### Parquet
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# MonitoringDatasetFormatOutput

### Csv
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringCsvDatasetFormat]

### Json
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringJsonDatasetFormat]

### Parquet
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# MonitoringExecutionSummary

### MonitoringScheduleName
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduledTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### MonitoringExecutionStatus
- **Type**: typing.Literal['Completed', 'CompletedWithViolations', 'Failed', 'InProgress', 'Pending', 'Stopped', 'Stopping']
- **Required**: Yes

### ProcessingJobArn
- **Type**: typing.Optional[str]

### EndpointName
- **Type**: typing.Optional[str]

### FailureReason
- **Type**: typing.Optional[str]

### MonitoringJobDefinitionName
- **Type**: typing.Optional[str]

### MonitoringType
- **Type**: typing.Optional[typing.Literal['DataQuality', 'ModelBias', 'ModelExplainability', 'ModelQuality']]


# MonitoringGroundTruthS3Input

### S3Uri
- **Type**: typing.Optional[str]


# MonitoringInput

### EndpointInput
- **Type**: <class 'NoneType'>

### BatchTransformInput
- **Type**: <class 'NoneType'>


# MonitoringInputOutput

### EndpointInput
- **Type**: <class 'NoneType'>

### BatchTransformInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.BatchTransformInputOutput]


# MonitoringJobDefinition

### MonitoringInputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringInput]
- **Required**: Yes

### MonitoringOutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringOutputConfig'>
- **Required**: Yes

### MonitoringResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringResources'>
- **Required**: Yes

### MonitoringAppSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringAppSpecification'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### BaselineConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringBaselineConfig]

### StoppingCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringStoppingCondition]

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]

### NetworkConfig
- **Type**: <class 'NoneType'>


# MonitoringJobDefinitionOutput

### MonitoringInputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringInputOutput]
- **Required**: Yes

### MonitoringOutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringOutputConfigOutput'>
- **Required**: Yes

### MonitoringResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringResources'>
- **Required**: Yes

### MonitoringAppSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringAppSpecificationOutput'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### BaselineConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringBaselineConfig]

### StoppingCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringStoppingCondition]

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]

### NetworkConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.NetworkConfigOutput]


# MonitoringJobDefinitionSummary

### MonitoringJobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### MonitoringJobDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes


# MonitoringJsonDatasetFormat

### Line
- **Type**: typing.Optional[bool]


# MonitoringNetworkConfig

### EnableInterContainerTrafficEncryption
- **Type**: typing.Optional[bool]

### EnableNetworkIsolation
- **Type**: typing.Optional[bool]

### VpcConfig
- **Type**: <class 'NoneType'>


# MonitoringNetworkConfigOutput

### EnableInterContainerTrafficEncryption
- **Type**: typing.Optional[bool]

### EnableNetworkIsolation
- **Type**: typing.Optional[bool]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.VpcConfigOutput]


# MonitoringOutput

### S3Output
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringS3Output'>
- **Required**: Yes


# MonitoringOutputConfig

### MonitoringOutputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringOutput]
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# MonitoringOutputConfigOutput

### MonitoringOutputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringOutput]
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# MonitoringResources

### ClusterConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringClusterConfig'>
- **Required**: Yes


# MonitoringS3Output

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### LocalPath
- **Type**: <class 'str'>
- **Required**: Yes

### S3UploadMode
- **Type**: typing.Optional[typing.Literal['Continuous', 'EndOfJob']]


# MonitoringSchedule

### MonitoringScheduleArn
- **Type**: typing.Optional[str]

### MonitoringScheduleName
- **Type**: typing.Optional[str]

### MonitoringScheduleStatus
- **Type**: typing.Optional[typing.Literal['Failed', 'Pending', 'Scheduled', 'Stopped']]

### MonitoringType
- **Type**: typing.Optional[typing.Literal['DataQuality', 'ModelBias', 'ModelExplainability', 'ModelQuality']]

### FailureReason
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### MonitoringScheduleConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringScheduleConfigOutput]

### EndpointName
- **Type**: typing.Optional[str]

### LastMonitoringExecutionSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringExecutionSummary]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# MonitoringScheduleConfig

### ScheduleConfig
- **Type**: <class 'NoneType'>

### MonitoringJobDefinition
- **Type**: <class 'NoneType'>

### MonitoringJobDefinitionName
- **Type**: typing.Optional[str]

### MonitoringType
- **Type**: typing.Optional[typing.Literal['DataQuality', 'ModelBias', 'ModelExplainability', 'ModelQuality']]


# MonitoringScheduleConfigOutput

### ScheduleConfig
- **Type**: <class 'NoneType'>

### MonitoringJobDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringJobDefinitionOutput]

### MonitoringJobDefinitionName
- **Type**: typing.Optional[str]

### MonitoringType
- **Type**: typing.Optional[typing.Literal['DataQuality', 'ModelBias', 'ModelExplainability', 'ModelQuality']]


# MonitoringScheduleSummary

### MonitoringScheduleName
- **Type**: <class 'str'>
- **Required**: Yes

### MonitoringScheduleArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### MonitoringScheduleStatus
- **Type**: typing.Literal['Failed', 'Pending', 'Scheduled', 'Stopped']
- **Required**: Yes

### EndpointName
- **Type**: typing.Optional[str]

### MonitoringJobDefinitionName
- **Type**: typing.Optional[str]

### MonitoringType
- **Type**: typing.Optional[typing.Literal['DataQuality', 'ModelBias', 'ModelExplainability', 'ModelQuality']]


# MonitoringStatisticsResource

### S3Uri
- **Type**: typing.Optional[str]


# MonitoringStoppingCondition

### MaxRuntimeInSeconds
- **Type**: <class 'int'>
- **Required**: Yes


# MultiModelConfig

### ModelCacheSetting
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# NeoVpcConfig

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes


# NeoVpcConfigOutput

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes


# NestedFilters

### NestedPropertyName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Filter]
- **Required**: Yes


# NetworkConfig

### EnableInterContainerTrafficEncryption
- **Type**: typing.Optional[bool]

### EnableNetworkIsolation
- **Type**: typing.Optional[bool]

### VpcConfig
- **Type**: <class 'NoneType'>


# NetworkConfigOutput

### EnableInterContainerTrafficEncryption
- **Type**: typing.Optional[bool]

### EnableNetworkIsolation
- **Type**: typing.Optional[bool]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.VpcConfigOutput]


# NotebookInstanceLifecycleConfigSummary

### NotebookInstanceLifecycleConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### NotebookInstanceLifecycleConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# NotebookInstanceLifecycleHook

### Content
- **Type**: typing.Optional[str]


# NotebookInstanceSummary

### NotebookInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### NotebookInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### NotebookInstanceStatus
- **Type**: typing.Optional[typing.Literal['Deleting', 'Failed', 'InService', 'Pending', 'Stopped', 'Stopping', 'Updating']]

### Url
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c5d.18xlarge', 'ml.c5d.2xlarge', 'ml.c5d.4xlarge', 'ml.c5d.9xlarge', 'ml.c5d.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c6id.12xlarge', 'ml.c6id.16xlarge', 'ml.c6id.24xlarge', 'ml.c6id.2xlarge', 'ml.c6id.32xlarge', 'ml.c6id.4xlarge', 'ml.c6id.8xlarge', 'ml.c6id.large', 'ml.c6id.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.inf1.24xlarge', 'ml.inf1.2xlarge', 'ml.inf1.6xlarge', 'ml.inf1.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.16xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.8xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m6id.12xlarge', 'ml.m6id.16xlarge', 'ml.m6id.24xlarge', 'ml.m6id.2xlarge', 'ml.m6id.32xlarge', 'ml.m6id.4xlarge', 'ml.m6id.8xlarge', 'ml.m6id.large', 'ml.m6id.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r6id.12xlarge', 'ml.r6id.16xlarge', 'ml.r6id.24xlarge', 'ml.r6id.2xlarge', 'ml.r6id.32xlarge', 'ml.r6id.4xlarge', 'ml.r6id.8xlarge', 'ml.r6id.large', 'ml.r6id.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.t2.2xlarge', 'ml.t2.large', 'ml.t2.medium', 'ml.t2.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### NotebookInstanceLifecycleConfigName
- **Type**: typing.Optional[str]

### DefaultCodeRepository
- **Type**: typing.Optional[str]

### AdditionalCodeRepositories
- **Type**: typing.Optional[typing.List[str]]


# NotificationConfiguration

### NotificationTopicArn
- **Type**: typing.Optional[str]


# ObjectiveStatusCounters

### Succeeded
- **Type**: typing.Optional[int]

### Pending
- **Type**: typing.Optional[int]

### Failed
- **Type**: typing.Optional[int]


# OfflineStoreConfig

### S3StorageConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.S3StorageConfig'>
- **Required**: Yes

### DisableGlueTableCreation
- **Type**: typing.Optional[bool]

### DataCatalogConfig
- **Type**: <class 'NoneType'>

### TableFormat
- **Type**: typing.Optional[typing.Literal['Default', 'Glue', 'Iceberg']]


# OfflineStoreStatus

### Status
- **Type**: typing.Literal['Active', 'Blocked', 'Disabled']
- **Required**: Yes

### BlockedReason
- **Type**: typing.Optional[str]


# OidcConfig

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientSecret
- **Type**: <class 'str'>
- **Required**: Yes

### Issuer
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizationEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### TokenEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### UserInfoEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### LogoutEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### JwksUri
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Optional[str]

### AuthenticationRequestExtraParams
- **Type**: typing.Optional[typing.Dict[str, str]]


# OidcConfigForResponse

### ClientId
- **Type**: typing.Optional[str]

### Issuer
- **Type**: typing.Optional[str]

### AuthorizationEndpoint
- **Type**: typing.Optional[str]

### TokenEndpoint
- **Type**: typing.Optional[str]

### UserInfoEndpoint
- **Type**: typing.Optional[str]

### LogoutEndpoint
- **Type**: typing.Optional[str]

### JwksUri
- **Type**: typing.Optional[str]

### Scope
- **Type**: typing.Optional[str]

### AuthenticationRequestExtraParams
- **Type**: typing.Optional[typing.Dict[str, str]]


# OidcMemberDefinition

### Groups
- **Type**: typing.Optional[typing.List[str]]


# OidcMemberDefinitionOutput

### Groups
- **Type**: typing.Optional[typing.List[str]]


# OnlineStoreConfig

### SecurityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OnlineStoreSecurityConfig]

### EnableOnlineStore
- **Type**: typing.Optional[bool]

### TtlDuration
- **Type**: <class 'NoneType'>

### StorageType
- **Type**: typing.Optional[typing.Literal['InMemory', 'Standard']]


# OnlineStoreConfigUpdate

### TtlDuration
- **Type**: <class 'NoneType'>


# OnlineStoreSecurityConfig

### KmsKeyId
- **Type**: typing.Optional[str]


# OptimizationConfig

### ModelQuantizationConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelQuantizationConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelQuantizationConfigOutput, NoneType]

### ModelCompilationConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelCompilationConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelCompilationConfigOutput, NoneType]

### ModelShardingConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelShardingConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelShardingConfigOutput, NoneType]


# OptimizationConfigOutput

### ModelQuantizationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelQuantizationConfigOutput]

### ModelCompilationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelCompilationConfigOutput]

### ModelShardingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelShardingConfigOutput]


# OptimizationJobModelSource

### S3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OptimizationJobModelSourceS3]


# OptimizationJobModelSourceS3

### S3Uri
- **Type**: typing.Optional[str]

### ModelAccessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OptimizationModelAccessConfig]


# OptimizationJobOutputConfig

### S3OutputLocation
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# OptimizationJobSummary

### OptimizationJobName
- **Type**: <class 'str'>
- **Required**: Yes

### OptimizationJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### OptimizationJobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'INPROGRESS', 'STARTING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### DeploymentInstanceType
- **Type**: typing.Literal['ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge']
- **Required**: Yes

### OptimizationTypes
- **Type**: typing.List[str]
- **Required**: Yes

### OptimizationStartTime
- **Type**: typing.Optional[datetime.datetime]

### OptimizationEndTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# OptimizationModelAccessConfig

### AcceptEula
- **Type**: <class 'bool'>
- **Required**: Yes


# OptimizationOutput

### RecommendedInferenceImage
- **Type**: typing.Optional[str]


# OptimizationVpcConfig

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes


# OptimizationVpcConfigOutput

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes


# OutputConfig

### S3OutputLocation
- **Type**: <class 'str'>
- **Required**: Yes

### TargetDevice
- **Type**: typing.Optional[typing.Literal['aisage', 'amba_cv2', 'amba_cv22', 'amba_cv25', 'coreml', 'deeplens', 'imx8mplus', 'imx8qm', 'jacinto_tda4vm', 'jetson_nano', 'jetson_tx1', 'jetson_tx2', 'jetson_xavier', 'lambda', 'ml_c4', 'ml_c5', 'ml_c6g', 'ml_eia2', 'ml_g4dn', 'ml_inf1', 'ml_inf2', 'ml_m4', 'ml_m5', 'ml_m6g', 'ml_p2', 'ml_p3', 'ml_trn1', 'qcs603', 'qcs605', 'rasp3b', 'rasp4b', 'rk3288', 'rk3399', 'sbe_c', 'sitara_am57x', 'x86_win32', 'x86_win64']]

### TargetPlatform
- **Type**: <class 'NoneType'>

### CompilerOptions
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]


# OutputDataConfig

### S3OutputPath
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]

### CompressionType
- **Type**: typing.Optional[typing.Literal['GZIP', 'NONE']]


# OutputParameter

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# OwnershipSettings

### OwnerUserProfileName
- **Type**: <class 'str'>
- **Required**: Yes


# OwnershipSettingsSummary

### OwnerUserProfileName
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParallelismConfiguration

### MaxParallelExecutionSteps
- **Type**: <class 'int'>
- **Required**: Yes


# Parameter

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ParameterRange

### IntegerParameterRangeSpecification
- **Type**: <class 'NoneType'>

### ContinuousParameterRangeSpecification
- **Type**: <class 'NoneType'>

### CategoricalParameterRangeSpecification
- **Type**: <class 'NoneType'>


# ParameterRangeOutput

### IntegerParameterRangeSpecification
- **Type**: <class 'NoneType'>

### ContinuousParameterRangeSpecification
- **Type**: <class 'NoneType'>

### CategoricalParameterRangeSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CategoricalParameterRangeSpecificationOutput]


# ParameterRanges

### IntegerParameterRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.IntegerParameterRange]]

### ContinuousParameterRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ContinuousParameterRange]]

### CategoricalParameterRanges
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CategoricalParameterRange, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CategoricalParameterRangeOutput]]]

### AutoParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoParameter]]


# ParameterRangesOutput

### IntegerParameterRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.IntegerParameterRange]]

### ContinuousParameterRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ContinuousParameterRange]]

### CategoricalParameterRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CategoricalParameterRangeOutput]]

### AutoParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoParameter]]


# Parent

### TrialName
- **Type**: typing.Optional[str]

### ExperimentName
- **Type**: typing.Optional[str]


# ParentHyperParameterTuningJob

### HyperParameterTuningJobName
- **Type**: typing.Optional[str]


# PartnerAppConfig

### AdminUsers
- **Type**: typing.Optional[typing.List[str]]

### Arguments
- **Type**: typing.Optional[typing.Dict[str, str]]


# PartnerAppConfigOutput

### AdminUsers
- **Type**: typing.Optional[typing.List[str]]

### Arguments
- **Type**: typing.Optional[typing.Dict[str, str]]


# PartnerAppMaintenanceConfig

### MaintenanceWindowStart
- **Type**: typing.Optional[str]


# PartnerAppSummary

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['comet', 'deepchecks-llm-evaluation', 'fiddler', 'lakera-guard']]

### Status
- **Type**: typing.Optional[typing.Literal['Available', 'Creating', 'Deleted', 'Deleting', 'Failed', 'UpdateFailed', 'Updating']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]


# PendingDeploymentSummary

### EndpointConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### ProductionVariants
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PendingProductionVariantSummary]]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### ShadowProductionVariants
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PendingProductionVariantSummary]]


# PendingProductionVariantSummary

### VariantName
- **Type**: <class 'str'>
- **Required**: Yes

### DeployedImages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DeployedImage]]

### CurrentWeight
- **Type**: typing.Optional[float]

### DesiredWeight
- **Type**: typing.Optional[float]

### CurrentInstanceCount
- **Type**: typing.Optional[int]

### DesiredInstanceCount
- **Type**: typing.Optional[int]

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.large', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c5d.18xlarge', 'ml.c5d.2xlarge', 'ml.c5d.4xlarge', 'ml.c5d.9xlarge', 'ml.c5d.large', 'ml.c5d.xlarge', 'ml.c6g.12xlarge', 'ml.c6g.16xlarge', 'ml.c6g.2xlarge', 'ml.c6g.4xlarge', 'ml.c6g.8xlarge', 'ml.c6g.large', 'ml.c6g.xlarge', 'ml.c6gd.12xlarge', 'ml.c6gd.16xlarge', 'ml.c6gd.2xlarge', 'ml.c6gd.4xlarge', 'ml.c6gd.8xlarge', 'ml.c6gd.large', 'ml.c6gd.xlarge', 'ml.c6gn.12xlarge', 'ml.c6gn.16xlarge', 'ml.c6gn.2xlarge', 'ml.c6gn.4xlarge', 'ml.c6gn.8xlarge', 'ml.c6gn.large', 'ml.c6gn.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c7g.12xlarge', 'ml.c7g.16xlarge', 'ml.c7g.2xlarge', 'ml.c7g.4xlarge', 'ml.c7g.8xlarge', 'ml.c7g.large', 'ml.c7g.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.dl1.24xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.inf1.24xlarge', 'ml.inf1.2xlarge', 'ml.inf1.6xlarge', 'ml.inf1.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6g.12xlarge', 'ml.m6g.16xlarge', 'ml.m6g.2xlarge', 'ml.m6g.4xlarge', 'ml.m6g.8xlarge', 'ml.m6g.large', 'ml.m6g.xlarge', 'ml.m6gd.12xlarge', 'ml.m6gd.16xlarge', 'ml.m6gd.2xlarge', 'ml.m6gd.4xlarge', 'ml.m6gd.8xlarge', 'ml.m6gd.large', 'ml.m6gd.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.r6g.12xlarge', 'ml.r6g.16xlarge', 'ml.r6g.2xlarge', 'ml.r6g.4xlarge', 'ml.r6g.8xlarge', 'ml.r6g.large', 'ml.r6g.xlarge', 'ml.r6gd.12xlarge', 'ml.r6gd.16xlarge', 'ml.r6gd.2xlarge', 'ml.r6gd.4xlarge', 'ml.r6gd.8xlarge', 'ml.r6gd.large', 'ml.r6gd.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.r8g.12xlarge', 'ml.r8g.16xlarge', 'ml.r8g.24xlarge', 'ml.r8g.2xlarge', 'ml.r8g.48xlarge', 'ml.r8g.4xlarge', 'ml.r8g.8xlarge', 'ml.r8g.large', 'ml.r8g.medium', 'ml.r8g.xlarge', 'ml.t2.2xlarge', 'ml.t2.large', 'ml.t2.medium', 'ml.t2.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]

### AcceleratorType
- **Type**: typing.Optional[typing.Literal['ml.eia1.large', 'ml.eia1.medium', 'ml.eia1.xlarge', 'ml.eia2.large', 'ml.eia2.medium', 'ml.eia2.xlarge']]

### VariantStatus
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProductionVariantStatus]]

### CurrentServerlessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProductionVariantServerlessConfig]

### DesiredServerlessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProductionVariantServerlessConfig]

### ManagedInstanceScaling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProductionVariantManagedInstanceScaling]

### RoutingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProductionVariantRoutingConfig]


# Phase

### InitialNumberOfUsers
- **Type**: typing.Optional[int]

### SpawnRate
- **Type**: typing.Optional[int]

### DurationInSeconds
- **Type**: typing.Optional[int]


# Pipeline

### PipelineArn
- **Type**: typing.Optional[str]

### PipelineName
- **Type**: typing.Optional[str]

### PipelineDisplayName
- **Type**: typing.Optional[str]

### PipelineDescription
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### PipelineStatus
- **Type**: typing.Optional[typing.Literal['Active', 'Deleting']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastRunTime
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext]

### LastModifiedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext]

### ParallelismConfiguration
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# PipelineDefinitionS3Location

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectKey
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: typing.Optional[str]


# PipelineExecution

### PipelineArn
- **Type**: typing.Optional[str]

### PipelineExecutionArn
- **Type**: typing.Optional[str]

### PipelineExecutionDisplayName
- **Type**: typing.Optional[str]

### PipelineExecutionStatus
- **Type**: typing.Optional[typing.Literal['Executing', 'Failed', 'Stopped', 'Stopping', 'Succeeded']]

### PipelineExecutionDescription
- **Type**: typing.Optional[str]

### PipelineExperimentConfig
- **Type**: <class 'NoneType'>

### FailureReason
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext]

### LastModifiedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext]

### ParallelismConfiguration
- **Type**: <class 'NoneType'>

### SelectiveExecutionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SelectiveExecutionConfigOutput]

### PipelineParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Parameter]]


# PipelineExecutionStep

### StepName
- **Type**: typing.Optional[str]

### StepDisplayName
- **Type**: typing.Optional[str]

### StepDescription
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### StepStatus
- **Type**: typing.Optional[typing.Literal['Executing', 'Failed', 'Starting', 'Stopped', 'Stopping', 'Succeeded']]

### CacheHitResult
- **Type**: <class 'NoneType'>

### FailureReason
- **Type**: typing.Optional[str]

### Metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PipelineExecutionStepMetadata]

### AttemptCount
- **Type**: typing.Optional[int]

### SelectiveExecutionResult
- **Type**: <class 'NoneType'>


# PipelineExecutionStepMetadata

### TrainingJob
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrainingJobStepMetadata]

### ProcessingJob
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProcessingJobStepMetadata]

### TransformJob
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TransformJobStepMetadata]

### TuningJob
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TuningJobStepMetaData]

### Model
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelStepMetadata]

### RegisterModel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.RegisterModelStepMetadata]

### Condition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ConditionStepMetadata]

### Callback
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CallbackStepMetadata]

### Lambda
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.LambdaStepMetadata]

### EMR
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EMRStepMetadata]

### QualityCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.QualityCheckStepMetadata]

### ClarifyCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ClarifyCheckStepMetadata]

### Fail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.FailStepMetadata]

### AutoMLJob
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLJobStepMetadata]

### Endpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EndpointStepMetadata]

### EndpointConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EndpointConfigStepMetadata]


# PipelineExecutionSummary

### PipelineExecutionArn
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### PipelineExecutionStatus
- **Type**: typing.Optional[typing.Literal['Executing', 'Failed', 'Stopped', 'Stopping', 'Succeeded']]

### PipelineExecutionDescription
- **Type**: typing.Optional[str]

### PipelineExecutionDisplayName
- **Type**: typing.Optional[str]

### PipelineExecutionFailureReason
- **Type**: typing.Optional[str]


# PipelineExperimentConfig

### ExperimentName
- **Type**: typing.Optional[str]

### TrialName
- **Type**: typing.Optional[str]


# PipelineSummary

### PipelineArn
- **Type**: typing.Optional[str]

### PipelineName
- **Type**: typing.Optional[str]

### PipelineDisplayName
- **Type**: typing.Optional[str]

### PipelineDescription
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastExecutionTime
- **Type**: typing.Optional[datetime.datetime]


# PredefinedMetricSpecification

### PredefinedMetricType
- **Type**: typing.Optional[str]


# PriorityClass

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Weight
- **Type**: <class 'int'>
- **Required**: Yes


# ProcessingClusterConfig

### InstanceCount
- **Type**: <class 'int'>
- **Required**: Yes

### InstanceType
- **Type**: typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.16xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.8xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge']
- **Required**: Yes

### VolumeSizeInGB
- **Type**: <class 'int'>
- **Required**: Yes

### VolumeKmsKeyId
- **Type**: typing.Optional[str]


# ProcessingFeatureStoreOutput

### FeatureGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# ProcessingInput

### InputName
- **Type**: <class 'str'>
- **Required**: Yes

### AppManaged
- **Type**: typing.Optional[bool]

### S3Input
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProcessingS3Input]

### DatasetDefinition
- **Type**: <class 'NoneType'>


# ProcessingJob

### ProcessingInputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProcessingInput]]

### ProcessingOutputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProcessingOutputConfigOutput]

### ProcessingJobName
- **Type**: typing.Optional[str]

### ProcessingResources
- **Type**: <class 'NoneType'>

### StoppingCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProcessingStoppingCondition]

### AppSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AppSpecificationOutput]

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]

### NetworkConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.NetworkConfigOutput]

### RoleArn
- **Type**: typing.Optional[str]

### ExperimentConfig
- **Type**: <class 'NoneType'>

### ProcessingJobArn
- **Type**: typing.Optional[str]

### ProcessingJobStatus
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### ExitMessage
- **Type**: typing.Optional[str]

### FailureReason
- **Type**: typing.Optional[str]

### ProcessingEndTime
- **Type**: typing.Optional[datetime.datetime]

### ProcessingStartTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### MonitoringScheduleArn
- **Type**: typing.Optional[str]

### AutoMLJobArn
- **Type**: typing.Optional[str]

### TrainingJobArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# ProcessingJobStepMetadata

### Arn
- **Type**: typing.Optional[str]


# ProcessingJobSummary

### ProcessingJobName
- **Type**: <class 'str'>
- **Required**: Yes

### ProcessingJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ProcessingJobStatus
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']
- **Required**: Yes

### ProcessingEndTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### FailureReason
- **Type**: typing.Optional[str]

### ExitMessage
- **Type**: typing.Optional[str]


# ProcessingOutput

### OutputName
- **Type**: <class 'str'>
- **Required**: Yes

### S3Output
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProcessingS3Output]

### FeatureStoreOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProcessingFeatureStoreOutput]

### AppManaged
- **Type**: typing.Optional[bool]


# ProcessingOutputConfig

### Outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProcessingOutput]
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# ProcessingOutputConfigOutput

### Outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProcessingOutput]
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# ProcessingResources

### ClusterConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProcessingClusterConfig'>
- **Required**: Yes


# ProcessingS3Input

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### S3DataType
- **Type**: typing.Literal['ManifestFile', 'S3Prefix']
- **Required**: Yes

### LocalPath
- **Type**: typing.Optional[str]

### S3InputMode
- **Type**: typing.Optional[typing.Literal['File', 'Pipe']]

### S3DataDistributionType
- **Type**: typing.Optional[typing.Literal['FullyReplicated', 'ShardedByS3Key']]

### S3CompressionType
- **Type**: typing.Optional[typing.Literal['Gzip', 'None']]


# ProcessingS3Output

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### S3UploadMode
- **Type**: typing.Literal['Continuous', 'EndOfJob']
- **Required**: Yes

### LocalPath
- **Type**: typing.Optional[str]


# ProcessingStoppingCondition

### MaxRuntimeInSeconds
- **Type**: <class 'int'>
- **Required**: Yes


# ProductionVariant

### VariantName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelName
- **Type**: typing.Optional[str]

### InitialInstanceCount
- **Type**: typing.Optional[int]

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.large', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c5d.18xlarge', 'ml.c5d.2xlarge', 'ml.c5d.4xlarge', 'ml.c5d.9xlarge', 'ml.c5d.large', 'ml.c5d.xlarge', 'ml.c6g.12xlarge', 'ml.c6g.16xlarge', 'ml.c6g.2xlarge', 'ml.c6g.4xlarge', 'ml.c6g.8xlarge', 'ml.c6g.large', 'ml.c6g.xlarge', 'ml.c6gd.12xlarge', 'ml.c6gd.16xlarge', 'ml.c6gd.2xlarge', 'ml.c6gd.4xlarge', 'ml.c6gd.8xlarge', 'ml.c6gd.large', 'ml.c6gd.xlarge', 'ml.c6gn.12xlarge', 'ml.c6gn.16xlarge', 'ml.c6gn.2xlarge', 'ml.c6gn.4xlarge', 'ml.c6gn.8xlarge', 'ml.c6gn.large', 'ml.c6gn.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c7g.12xlarge', 'ml.c7g.16xlarge', 'ml.c7g.2xlarge', 'ml.c7g.4xlarge', 'ml.c7g.8xlarge', 'ml.c7g.large', 'ml.c7g.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.dl1.24xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.inf1.24xlarge', 'ml.inf1.2xlarge', 'ml.inf1.6xlarge', 'ml.inf1.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6g.12xlarge', 'ml.m6g.16xlarge', 'ml.m6g.2xlarge', 'ml.m6g.4xlarge', 'ml.m6g.8xlarge', 'ml.m6g.large', 'ml.m6g.xlarge', 'ml.m6gd.12xlarge', 'ml.m6gd.16xlarge', 'ml.m6gd.2xlarge', 'ml.m6gd.4xlarge', 'ml.m6gd.8xlarge', 'ml.m6gd.large', 'ml.m6gd.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.r6g.12xlarge', 'ml.r6g.16xlarge', 'ml.r6g.2xlarge', 'ml.r6g.4xlarge', 'ml.r6g.8xlarge', 'ml.r6g.large', 'ml.r6g.xlarge', 'ml.r6gd.12xlarge', 'ml.r6gd.16xlarge', 'ml.r6gd.2xlarge', 'ml.r6gd.4xlarge', 'ml.r6gd.8xlarge', 'ml.r6gd.large', 'ml.r6gd.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.r8g.12xlarge', 'ml.r8g.16xlarge', 'ml.r8g.24xlarge', 'ml.r8g.2xlarge', 'ml.r8g.48xlarge', 'ml.r8g.4xlarge', 'ml.r8g.8xlarge', 'ml.r8g.large', 'ml.r8g.medium', 'ml.r8g.xlarge', 'ml.t2.2xlarge', 'ml.t2.large', 'ml.t2.medium', 'ml.t2.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]

### InitialVariantWeight
- **Type**: typing.Optional[float]

### AcceleratorType
- **Type**: typing.Optional[typing.Literal['ml.eia1.large', 'ml.eia1.medium', 'ml.eia1.xlarge', 'ml.eia2.large', 'ml.eia2.medium', 'ml.eia2.xlarge']]

### CoreDumpConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProductionVariantCoreDumpConfig]

### ServerlessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProductionVariantServerlessConfig]

### VolumeSizeInGB
- **Type**: typing.Optional[int]

### ModelDataDownloadTimeoutInSeconds
- **Type**: typing.Optional[int]

### ContainerStartupHealthCheckTimeoutInSeconds
- **Type**: typing.Optional[int]

### EnableSSMAccess
- **Type**: typing.Optional[bool]

### ManagedInstanceScaling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProductionVariantManagedInstanceScaling]

### RoutingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProductionVariantRoutingConfig]

### InferenceAmiVersion
- **Type**: typing.Optional[typing.Literal['al2-ami-sagemaker-inference-gpu-2', 'al2-ami-sagemaker-inference-gpu-2-1', 'al2-ami-sagemaker-inference-gpu-3-1']]


# ProductionVariantCoreDumpConfig

### DestinationS3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# ProductionVariantManagedInstanceScaling

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### MinInstanceCount
- **Type**: typing.Optional[int]

### MaxInstanceCount
- **Type**: typing.Optional[int]


# ProductionVariantRoutingConfig

### RoutingStrategy
- **Type**: typing.Literal['LEAST_OUTSTANDING_REQUESTS', 'RANDOM']
- **Required**: Yes


# ProductionVariantServerlessConfig

### MemorySizeInMB
- **Type**: <class 'int'>
- **Required**: Yes

### MaxConcurrency
- **Type**: <class 'int'>
- **Required**: Yes

### ProvisionedConcurrency
- **Type**: typing.Optional[int]


# ProductionVariantServerlessUpdateConfig

### MaxConcurrency
- **Type**: typing.Optional[int]

### ProvisionedConcurrency
- **Type**: typing.Optional[int]


# ProductionVariantStatus

### Status
- **Type**: typing.Literal['ActivatingTraffic', 'Baking', 'Creating', 'Deleting', 'Updating']
- **Required**: Yes

### StatusMessage
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]


# ProductionVariantSummary

### VariantName
- **Type**: <class 'str'>
- **Required**: Yes

### DeployedImages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DeployedImage]]

### CurrentWeight
- **Type**: typing.Optional[float]

### DesiredWeight
- **Type**: typing.Optional[float]

### CurrentInstanceCount
- **Type**: typing.Optional[int]

### DesiredInstanceCount
- **Type**: typing.Optional[int]

### VariantStatus
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProductionVariantStatus]]

### CurrentServerlessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProductionVariantServerlessConfig]

### DesiredServerlessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProductionVariantServerlessConfig]

### ManagedInstanceScaling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProductionVariantManagedInstanceScaling]

### RoutingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProductionVariantRoutingConfig]


# ProfilerConfig

### S3OutputPath
- **Type**: typing.Optional[str]

### ProfilingIntervalInMilliseconds
- **Type**: typing.Optional[int]

### ProfilingParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### DisableProfiler
- **Type**: typing.Optional[bool]


# ProfilerConfigForUpdate

### S3OutputPath
- **Type**: typing.Optional[str]

### ProfilingIntervalInMilliseconds
- **Type**: typing.Optional[int]

### ProfilingParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### DisableProfiler
- **Type**: typing.Optional[bool]


# ProfilerConfigOutput

### S3OutputPath
- **Type**: typing.Optional[str]

### ProfilingIntervalInMilliseconds
- **Type**: typing.Optional[int]

### ProfilingParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### DisableProfiler
- **Type**: typing.Optional[bool]


# ProfilerRuleConfiguration

### RuleConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### RuleEvaluatorImage
- **Type**: <class 'str'>
- **Required**: Yes

### LocalPath
- **Type**: typing.Optional[str]

### S3OutputPath
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.16xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.8xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge']]

### VolumeSizeInGB
- **Type**: typing.Optional[int]

### RuleParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# ProfilerRuleConfigurationOutput

### RuleConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### RuleEvaluatorImage
- **Type**: <class 'str'>
- **Required**: Yes

### LocalPath
- **Type**: typing.Optional[str]

### S3OutputPath
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.16xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.8xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge']]

### VolumeSizeInGB
- **Type**: typing.Optional[int]

### RuleParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# ProfilerRuleEvaluationStatus

### RuleConfigurationName
- **Type**: typing.Optional[str]

### RuleEvaluationJobArn
- **Type**: typing.Optional[str]

### RuleEvaluationStatus
- **Type**: typing.Optional[typing.Literal['Error', 'InProgress', 'IssuesFound', 'NoIssuesFound', 'Stopped', 'Stopping']]

### StatusDetails
- **Type**: typing.Optional[str]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# Project

### ProjectArn
- **Type**: typing.Optional[str]

### ProjectName
- **Type**: typing.Optional[str]

### ProjectId
- **Type**: typing.Optional[str]

### ProjectDescription
- **Type**: typing.Optional[str]

### ServiceCatalogProvisioningDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ServiceCatalogProvisioningDetailsOutput]

### ServiceCatalogProvisionedProductDetails
- **Type**: <class 'NoneType'>

### ProjectStatus
- **Type**: typing.Optional[typing.Literal['CreateCompleted', 'CreateFailed', 'CreateInProgress', 'DeleteCompleted', 'DeleteFailed', 'DeleteInProgress', 'Pending', 'UpdateCompleted', 'UpdateFailed', 'UpdateInProgress']]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext]


# ProjectSummary

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### ProjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProjectId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ProjectStatus
- **Type**: typing.Literal['CreateCompleted', 'CreateFailed', 'CreateInProgress', 'DeleteCompleted', 'DeleteFailed', 'DeleteInProgress', 'Pending', 'UpdateCompleted', 'UpdateFailed', 'UpdateInProgress']
- **Required**: Yes

### ProjectDescription
- **Type**: typing.Optional[str]


# PropertyNameQuery

### PropertyNameHint
- **Type**: <class 'str'>
- **Required**: Yes


# PropertyNameSuggestion

### PropertyName
- **Type**: typing.Optional[str]


# ProvisioningParameter

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# PublicWorkforceTaskPrice

### AmountInUsd
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.USD]


# PutModelPackageGroupPolicyInput

### ModelPackageGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourcePolicy
- **Type**: <class 'str'>
- **Required**: Yes


# PutModelPackageGroupPolicyOutput

### ModelPackageGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# QualityCheckStepMetadata

### CheckType
- **Type**: typing.Optional[str]

### BaselineUsedForDriftCheckStatistics
- **Type**: typing.Optional[str]

### BaselineUsedForDriftCheckConstraints
- **Type**: typing.Optional[str]

### CalculatedBaselineStatistics
- **Type**: typing.Optional[str]

### CalculatedBaselineConstraints
- **Type**: typing.Optional[str]

### ModelPackageGroupName
- **Type**: typing.Optional[str]

### ViolationReport
- **Type**: typing.Optional[str]

### CheckJobArn
- **Type**: typing.Optional[str]

### SkipCheck
- **Type**: typing.Optional[bool]

### RegisterNewBaseline
- **Type**: typing.Optional[bool]


# QueryFilters

### Types
- **Type**: typing.Optional[typing.List[str]]

### LineageTypes
- **Type**: typing.Optional[typing.List[typing.Literal['Action', 'Artifact', 'Context', 'TrialComponent']]]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ModifiedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ModifiedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Properties
- **Type**: typing.Optional[typing.Dict[str, str]]


# QueryLineageRequest

### StartArns
- **Type**: typing.Optional[typing.List[str]]

### Direction
- **Type**: typing.Optional[typing.Literal['Ascendants', 'Both', 'Descendants']]

### IncludeEdges
- **Type**: typing.Optional[bool]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.QueryFilters]

### MaxDepth
- **Type**: typing.Optional[int]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# QueryLineageResponse

### Vertices
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Vertex]
- **Required**: Yes

### Edges
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Edge]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# RSessionAppSettings

### DefaultResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResourceSpec]

### CustomImages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CustomImage]]


# RSessionAppSettingsOutput

### DefaultResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResourceSpec]

### CustomImages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CustomImage]]


# RStudioServerProAppSettings

### AccessStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### UserGroup
- **Type**: typing.Optional[typing.Literal['R_STUDIO_ADMIN', 'R_STUDIO_USER']]


# RStudioServerProDomainSettings

### DomainExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### RStudioConnectUrl
- **Type**: typing.Optional[str]

### RStudioPackageManagerUrl
- **Type**: typing.Optional[str]

### DefaultResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResourceSpec]


# RStudioServerProDomainSettingsForUpdate

### DomainExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResourceSpec]

### RStudioConnectUrl
- **Type**: typing.Optional[str]

### RStudioPackageManagerUrl
- **Type**: typing.Optional[str]


# RealTimeInferenceConfig

### InstanceType
- **Type**: typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c5d.18xlarge', 'ml.c5d.2xlarge', 'ml.c5d.4xlarge', 'ml.c5d.9xlarge', 'ml.c5d.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c6id.12xlarge', 'ml.c6id.16xlarge', 'ml.c6id.24xlarge', 'ml.c6id.2xlarge', 'ml.c6id.32xlarge', 'ml.c6id.4xlarge', 'ml.c6id.8xlarge', 'ml.c6id.large', 'ml.c6id.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.inf1.24xlarge', 'ml.inf1.2xlarge', 'ml.inf1.6xlarge', 'ml.inf1.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.16xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.8xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m6id.12xlarge', 'ml.m6id.16xlarge', 'ml.m6id.24xlarge', 'ml.m6id.2xlarge', 'ml.m6id.32xlarge', 'ml.m6id.4xlarge', 'ml.m6id.8xlarge', 'ml.m6id.large', 'ml.m6id.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r6id.12xlarge', 'ml.r6id.16xlarge', 'ml.r6id.24xlarge', 'ml.r6id.2xlarge', 'ml.r6id.32xlarge', 'ml.r6id.4xlarge', 'ml.r6id.8xlarge', 'ml.r6id.large', 'ml.r6id.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.t2.2xlarge', 'ml.t2.large', 'ml.t2.medium', 'ml.t2.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge']
- **Required**: Yes

### InstanceCount
- **Type**: <class 'int'>
- **Required**: Yes


# RealTimeInferenceRecommendation

### RecommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceType
- **Type**: typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.large', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c5d.18xlarge', 'ml.c5d.2xlarge', 'ml.c5d.4xlarge', 'ml.c5d.9xlarge', 'ml.c5d.large', 'ml.c5d.xlarge', 'ml.c6g.12xlarge', 'ml.c6g.16xlarge', 'ml.c6g.2xlarge', 'ml.c6g.4xlarge', 'ml.c6g.8xlarge', 'ml.c6g.large', 'ml.c6g.xlarge', 'ml.c6gd.12xlarge', 'ml.c6gd.16xlarge', 'ml.c6gd.2xlarge', 'ml.c6gd.4xlarge', 'ml.c6gd.8xlarge', 'ml.c6gd.large', 'ml.c6gd.xlarge', 'ml.c6gn.12xlarge', 'ml.c6gn.16xlarge', 'ml.c6gn.2xlarge', 'ml.c6gn.4xlarge', 'ml.c6gn.8xlarge', 'ml.c6gn.large', 'ml.c6gn.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c7g.12xlarge', 'ml.c7g.16xlarge', 'ml.c7g.2xlarge', 'ml.c7g.4xlarge', 'ml.c7g.8xlarge', 'ml.c7g.large', 'ml.c7g.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.dl1.24xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.inf1.24xlarge', 'ml.inf1.2xlarge', 'ml.inf1.6xlarge', 'ml.inf1.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6g.12xlarge', 'ml.m6g.16xlarge', 'ml.m6g.2xlarge', 'ml.m6g.4xlarge', 'ml.m6g.8xlarge', 'ml.m6g.large', 'ml.m6g.xlarge', 'ml.m6gd.12xlarge', 'ml.m6gd.16xlarge', 'ml.m6gd.2xlarge', 'ml.m6gd.4xlarge', 'ml.m6gd.8xlarge', 'ml.m6gd.large', 'ml.m6gd.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.r6g.12xlarge', 'ml.r6g.16xlarge', 'ml.r6g.2xlarge', 'ml.r6g.4xlarge', 'ml.r6g.8xlarge', 'ml.r6g.large', 'ml.r6g.xlarge', 'ml.r6gd.12xlarge', 'ml.r6gd.16xlarge', 'ml.r6gd.2xlarge', 'ml.r6gd.4xlarge', 'ml.r6gd.8xlarge', 'ml.r6gd.large', 'ml.r6gd.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.r8g.12xlarge', 'ml.r8g.16xlarge', 'ml.r8g.24xlarge', 'ml.r8g.2xlarge', 'ml.r8g.48xlarge', 'ml.r8g.4xlarge', 'ml.r8g.8xlarge', 'ml.r8g.large', 'ml.r8g.medium', 'ml.r8g.xlarge', 'ml.t2.2xlarge', 'ml.t2.large', 'ml.t2.medium', 'ml.t2.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']
- **Required**: Yes

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]


# RecommendationJobCompiledOutputConfig

### S3OutputUri
- **Type**: typing.Optional[str]


# RecommendationJobContainerConfig

### Domain
- **Type**: typing.Optional[str]

### Task
- **Type**: typing.Optional[str]

### Framework
- **Type**: typing.Optional[str]

### FrameworkVersion
- **Type**: typing.Optional[str]

### PayloadConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.RecommendationJobPayloadConfig]

### NearestModelName
- **Type**: typing.Optional[str]

### SupportedInstanceTypes
- **Type**: typing.Optional[typing.List[str]]

### SupportedEndpointType
- **Type**: typing.Optional[typing.Literal['RealTime', 'Serverless']]

### DataInputConfig
- **Type**: typing.Optional[str]

### SupportedResponseMIMETypes
- **Type**: typing.Optional[typing.List[str]]


# RecommendationJobContainerConfigOutput

### Domain
- **Type**: typing.Optional[str]

### Task
- **Type**: typing.Optional[str]

### Framework
- **Type**: typing.Optional[str]

### FrameworkVersion
- **Type**: typing.Optional[str]

### PayloadConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.RecommendationJobPayloadConfigOutput]

### NearestModelName
- **Type**: typing.Optional[str]

### SupportedInstanceTypes
- **Type**: typing.Optional[typing.List[str]]

### SupportedEndpointType
- **Type**: typing.Optional[typing.Literal['RealTime', 'Serverless']]

### DataInputConfig
- **Type**: typing.Optional[str]

### SupportedResponseMIMETypes
- **Type**: typing.Optional[typing.List[str]]


# RecommendationJobInferenceBenchmark

### ModelConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelConfiguration'>
- **Required**: Yes

### Metrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.RecommendationMetrics]

### EndpointMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceMetrics]

### EndpointConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EndpointOutputConfiguration]

### FailureReason
- **Type**: typing.Optional[str]

### InvocationEndTime
- **Type**: typing.Optional[datetime.datetime]

### InvocationStartTime
- **Type**: typing.Optional[datetime.datetime]


# RecommendationJobInputConfig

### ModelPackageVersionArn
- **Type**: typing.Optional[str]

### ModelName
- **Type**: typing.Optional[str]

### JobDurationInSeconds
- **Type**: typing.Optional[int]

### TrafficPattern
- **Type**: <class 'NoneType'>

### ResourceLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.RecommendationJobResourceLimit]

### EndpointConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EndpointInputConfiguration]]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### ContainerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.RecommendationJobContainerConfig]

### Endpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EndpointInfo]]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.RecommendationJobVpcConfig]


# RecommendationJobInputConfigOutput

### ModelPackageVersionArn
- **Type**: typing.Optional[str]

### ModelName
- **Type**: typing.Optional[str]

### JobDurationInSeconds
- **Type**: typing.Optional[int]

### TrafficPattern
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrafficPatternOutput]

### ResourceLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.RecommendationJobResourceLimit]

### EndpointConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EndpointInputConfigurationOutput]]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### ContainerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.RecommendationJobContainerConfigOutput]

### Endpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EndpointInfo]]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.RecommendationJobVpcConfigOutput]


# RecommendationJobOutputConfig

### KmsKeyId
- **Type**: typing.Optional[str]

### CompiledOutputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.RecommendationJobCompiledOutputConfig]


# RecommendationJobPayloadConfig

### SamplePayloadUrl
- **Type**: typing.Optional[str]

### SupportedContentTypes
- **Type**: typing.Optional[typing.List[str]]


# RecommendationJobPayloadConfigOutput

### SamplePayloadUrl
- **Type**: typing.Optional[str]

### SupportedContentTypes
- **Type**: typing.Optional[typing.List[str]]


# RecommendationJobResourceLimit

### MaxNumberOfTests
- **Type**: typing.Optional[int]

### MaxParallelOfTests
- **Type**: typing.Optional[int]


# RecommendationJobStoppingConditions

### MaxInvocations
- **Type**: typing.Optional[int]

### ModelLatencyThresholds
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelLatencyThreshold]]

### FlatInvocations
- **Type**: typing.Optional[typing.Literal['Continue', 'Stop']]


# RecommendationJobStoppingConditionsOutput

### MaxInvocations
- **Type**: typing.Optional[int]

### ModelLatencyThresholds
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelLatencyThreshold]]

### FlatInvocations
- **Type**: typing.Optional[typing.Literal['Continue', 'Stop']]


# RecommendationJobVpcConfig

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes


# RecommendationJobVpcConfigOutput

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes


# RecommendationMetrics

### CostPerHour
- **Type**: typing.Optional[float]

### CostPerInference
- **Type**: typing.Optional[float]

### MaxInvocations
- **Type**: typing.Optional[int]

### ModelLatency
- **Type**: typing.Optional[int]

### CpuUtilization
- **Type**: typing.Optional[float]

### MemoryUtilization
- **Type**: typing.Optional[float]

### ModelSetupTime
- **Type**: typing.Optional[int]


# RedshiftDatasetDefinition

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### DbUser
- **Type**: <class 'str'>
- **Required**: Yes

### QueryString
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputS3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### OutputFormat
- **Type**: typing.Literal['CSV', 'PARQUET']
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]

### OutputCompression
- **Type**: typing.Optional[typing.Literal['BZIP2', 'GZIP', 'None', 'SNAPPY', 'ZSTD']]


# RegisterDevicesRequest

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes

### Devices
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Device]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# RegisterModelStepMetadata

### Arn
- **Type**: typing.Optional[str]


# RemoteDebugConfig

### EnableRemoteDebug
- **Type**: typing.Optional[bool]


# RemoteDebugConfigForUpdate

### EnableRemoteDebug
- **Type**: typing.Optional[bool]


# RenderUiTemplateRequest

### Task
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.RenderableTask'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### UiTemplate
- **Type**: <class 'NoneType'>

### HumanTaskUiArn
- **Type**: typing.Optional[str]


# RenderUiTemplateResponse

### RenderedContent
- **Type**: <class 'str'>
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.RenderingError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# RenderableTask

### Input
- **Type**: <class 'str'>
- **Required**: Yes


# RenderingError

### Code
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes


# RepositoryAuthConfig

### RepositoryCredentialsProviderArn
- **Type**: <class 'str'>
- **Required**: Yes


# ReservedCapacityOffering

### InstanceType
- **Type**: typing.Literal['ml.p4d.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.trn1.32xlarge', 'ml.trn2.48xlarge']
- **Required**: Yes

### InstanceCount
- **Type**: <class 'int'>
- **Required**: Yes

### AvailabilityZone
- **Type**: typing.Optional[str]

### DurationHours
- **Type**: typing.Optional[int]

### DurationMinutes
- **Type**: typing.Optional[int]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]


# ReservedCapacitySummary

### ReservedCapacityArn
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceType
- **Type**: typing.Literal['ml.p4d.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.trn1.32xlarge', 'ml.trn2.48xlarge']
- **Required**: Yes

### TotalInstanceCount
- **Type**: <class 'int'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Active', 'Expired', 'Failed', 'Pending', 'Scheduled']
- **Required**: Yes

### AvailabilityZone
- **Type**: typing.Optional[str]

### DurationHours
- **Type**: typing.Optional[int]

### DurationMinutes
- **Type**: typing.Optional[int]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]


# ResolvedAttributes

### AutoMLJobObjective
- **Type**: <class 'NoneType'>

### ProblemType
- **Type**: typing.Optional[typing.Literal['BinaryClassification', 'MulticlassClassification', 'Regression']]

### CompletionCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLJobCompletionCriteria]


# ResourceCatalog

### ResourceCatalogArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceCatalogName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ResourceConfig

### VolumeSizeInGB
- **Type**: <class 'int'>
- **Required**: Yes

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c5n.18xlarge', 'ml.c5n.2xlarge', 'ml.c5n.4xlarge', 'ml.c5n.9xlarge', 'ml.c5n.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.16xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.8xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]

### InstanceCount
- **Type**: typing.Optional[int]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### KeepAlivePeriodInSeconds
- **Type**: typing.Optional[int]

### InstanceGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InstanceGroup]]

### TrainingPlanArn
- **Type**: typing.Optional[str]


# ResourceConfigForUpdate

### KeepAlivePeriodInSeconds
- **Type**: <class 'int'>
- **Required**: Yes


# ResourceConfigOutput

### VolumeSizeInGB
- **Type**: <class 'int'>
- **Required**: Yes

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c5n.18xlarge', 'ml.c5n.2xlarge', 'ml.c5n.4xlarge', 'ml.c5n.9xlarge', 'ml.c5n.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.16xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.8xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]

### InstanceCount
- **Type**: typing.Optional[int]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### KeepAlivePeriodInSeconds
- **Type**: typing.Optional[int]

### InstanceGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InstanceGroup]]

### TrainingPlanArn
- **Type**: typing.Optional[str]


# ResourceLimits

### MaxParallelTrainingJobs
- **Type**: <class 'int'>
- **Required**: Yes

### MaxNumberOfTrainingJobs
- **Type**: typing.Optional[int]

### MaxRuntimeInSeconds
- **Type**: typing.Optional[int]


# ResourceSharingConfig

### Strategy
- **Type**: typing.Literal['DontLend', 'Lend', 'LendAndBorrow']
- **Required**: Yes

### BorrowLimit
- **Type**: typing.Optional[int]


# ResourceSpec

### SageMakerImageArn
- **Type**: typing.Optional[str]

### SageMakerImageVersionArn
- **Type**: typing.Optional[str]

### SageMakerImageVersionAlias
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c5.12xlarge', 'ml.c5.18xlarge', 'ml.c5.24xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c6id.12xlarge', 'ml.c6id.16xlarge', 'ml.c6id.24xlarge', 'ml.c6id.2xlarge', 'ml.c6id.32xlarge', 'ml.c6id.4xlarge', 'ml.c6id.8xlarge', 'ml.c6id.large', 'ml.c6id.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.geospatial.interactive', 'ml.m5.12xlarge', 'ml.m5.16xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.8xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.16xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.8xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m6id.12xlarge', 'ml.m6id.16xlarge', 'ml.m6id.24xlarge', 'ml.m6id.2xlarge', 'ml.m6id.32xlarge', 'ml.m6id.4xlarge', 'ml.m6id.8xlarge', 'ml.m6id.large', 'ml.m6id.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r6id.12xlarge', 'ml.r6id.16xlarge', 'ml.r6id.24xlarge', 'ml.r6id.2xlarge', 'ml.r6id.32xlarge', 'ml.r6id.4xlarge', 'ml.r6id.8xlarge', 'ml.r6id.large', 'ml.r6id.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.micro', 'ml.t3.small', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'system']]

### LifecycleConfigArn
- **Type**: typing.Optional[str]


# ResponseMetadata

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HTTPStatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### HTTPHeaders
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RetryAttempts
- **Type**: <class 'int'>
- **Required**: Yes

### HostId
- **Type**: typing.Optional[str]


# RetentionPolicy

### HomeEfsFileSystem
- **Type**: typing.Optional[typing.Literal['Delete', 'Retain']]


# RetryPipelineExecutionRequest

### PipelineExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### ParallelismConfiguration
- **Type**: <class 'NoneType'>


# RetryPipelineExecutionResponse

### PipelineExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# RetryStrategy

### MaximumRetryAttempts
- **Type**: <class 'int'>
- **Required**: Yes


# RollingUpdatePolicy

### MaximumBatchSize
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CapacitySize'>
- **Required**: Yes

### WaitIntervalInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### MaximumExecutionTimeoutInSeconds
- **Type**: typing.Optional[int]

### RollbackMaximumBatchSize
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CapacitySize]


# S3DataSource

### S3DataType
- **Type**: typing.Literal['AugmentedManifestFile', 'ManifestFile', 'S3Prefix']
- **Required**: Yes

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### S3DataDistributionType
- **Type**: <class 'NoneType'>

### AttributeNames
- **Type**: typing.Optional[typing.List[str]]

### InstanceGroupNames
- **Type**: typing.Optional[typing.List[str]]

### ModelAccessConfig
- **Type**: <class 'NoneType'>

### HubAccessConfig
- **Type**: <class 'NoneType'>


# S3DataSourceOutput

### S3DataType
- **Type**: typing.Literal['AugmentedManifestFile', 'ManifestFile', 'S3Prefix']
- **Required**: Yes

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### S3DataDistributionType
- **Type**: <class 'NoneType'>

### AttributeNames
- **Type**: typing.Optional[typing.List[str]]

### InstanceGroupNames
- **Type**: typing.Optional[typing.List[str]]

### ModelAccessConfig
- **Type**: <class 'NoneType'>

### HubAccessConfig
- **Type**: <class 'NoneType'>


# S3ModelDataSource

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### S3DataType
- **Type**: typing.Literal['S3Object', 'S3Prefix']
- **Required**: Yes

### CompressionType
- **Type**: typing.Literal['Gzip', 'None']
- **Required**: Yes

### ModelAccessConfig
- **Type**: <class 'NoneType'>

### HubAccessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceHubAccessConfig]

### ManifestS3Uri
- **Type**: typing.Optional[str]

### ETag
- **Type**: typing.Optional[str]

### ManifestEtag
- **Type**: typing.Optional[str]


# S3Presign

### IamPolicyConstraints
- **Type**: <class 'NoneType'>


# S3StorageConfig

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]

### ResolvedOutputS3Uri
- **Type**: typing.Optional[str]


# ScalingPolicy

### TargetTracking
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TargetTrackingScalingPolicyConfiguration]


# ScalingPolicyMetric

### InvocationsPerInstance
- **Type**: typing.Optional[int]

### ModelLatency
- **Type**: typing.Optional[int]


# ScalingPolicyObjective

### MinInvocationsPerMinute
- **Type**: typing.Optional[int]

### MaxInvocationsPerMinute
- **Type**: typing.Optional[int]


# ScheduleConfig

### ScheduleExpression
- **Type**: <class 'str'>
- **Required**: Yes

### DataAnalysisStartTime
- **Type**: typing.Optional[str]

### DataAnalysisEndTime
- **Type**: typing.Optional[str]


# SchedulerConfig

### PriorityClasses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PriorityClass]]

### FairShare
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# SchedulerConfigOutput

### PriorityClasses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PriorityClass]]

### FairShare
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# SearchExpression

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Filter]]

### NestedFilters
- **Type**: typing.Optional[typing.List[NoneType]]

### SubExpressions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### Operator
- **Type**: typing.Optional[typing.Literal['And', 'Or']]


# SearchExpressionPaginator

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Filter]]

### NestedFilters
- **Type**: typing.Optional[typing.List[NoneType]]

### SubExpressions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### Operator
- **Type**: typing.Optional[typing.Literal['And', 'Or']]


# SearchRecord

### TrainingJob
- **Type**: <class 'NoneType'>

### Experiment
- **Type**: <class 'NoneType'>

### Trial
- **Type**: <class 'NoneType'>

### TrialComponent
- **Type**: <class 'NoneType'>

### Endpoint
- **Type**: <class 'NoneType'>

### ModelPackage
- **Type**: <class 'NoneType'>

### ModelPackageGroup
- **Type**: <class 'NoneType'>

### Pipeline
- **Type**: <class 'NoneType'>

### PipelineExecution
- **Type**: <class 'NoneType'>

### FeatureGroup
- **Type**: <class 'NoneType'>

### FeatureMetadata
- **Type**: <class 'NoneType'>

### Project
- **Type**: <class 'NoneType'>

### HyperParameterTuningJob
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTuningJobSearchEntity]

### ModelCard
- **Type**: <class 'NoneType'>

### Model
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelDashboardModel]


# SearchRequest

### Resource
- **Type**: typing.Literal['Endpoint', 'Experiment', 'ExperimentTrial', 'ExperimentTrialComponent', 'FeatureGroup', 'FeatureMetadata', 'HyperParameterTuningJob', 'Image', 'ImageVersion', 'Model', 'ModelCard', 'ModelPackage', 'ModelPackageGroup', 'Pipeline', 'PipelineExecution', 'Project', 'TrainingJob']
- **Required**: Yes

### SearchExpression
- **Type**: <class 'NoneType'>

### SortBy
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### CrossAccountFilterOption
- **Type**: typing.Optional[typing.Literal['CrossAccount', 'SameAccount']]

### VisibilityConditions
- **Type**: typing.Optional[typing.List[NoneType]]


# SearchRequestPaginate

### Resource
- **Type**: typing.Literal['Endpoint', 'Experiment', 'ExperimentTrial', 'ExperimentTrialComponent', 'FeatureGroup', 'FeatureMetadata', 'HyperParameterTuningJob', 'Image', 'ImageVersion', 'Model', 'ModelCard', 'ModelPackage', 'ModelPackageGroup', 'Pipeline', 'PipelineExecution', 'Project', 'TrainingJob']
- **Required**: Yes

### SearchExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SearchExpressionPaginator]

### SortBy
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### CrossAccountFilterOption
- **Type**: typing.Optional[typing.Literal['CrossAccount', 'SameAccount']]

### VisibilityConditions
- **Type**: typing.Optional[typing.List[NoneType]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PaginatorConfig]


# SearchResponse

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SearchRecord]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchTrainingPlanOfferingsRequest

### InstanceType
- **Type**: typing.Literal['ml.p4d.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.trn1.32xlarge', 'ml.trn2.48xlarge']
- **Required**: Yes

### InstanceCount
- **Type**: <class 'int'>
- **Required**: Yes

### TargetResources
- **Type**: typing.List[typing.Literal['hyperpod-cluster', 'training-job']]
- **Required**: Yes

### StartTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### DurationHours
- **Type**: typing.Optional[int]


# SearchTrainingPlanOfferingsResponse

### TrainingPlanOfferings
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrainingPlanOffering]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# SecondaryStatusTransition

### Status
- **Type**: typing.Literal['Completed', 'Downloading', 'DownloadingTrainingImage', 'Failed', 'Interrupted', 'LaunchingMLInstances', 'MaxRuntimeExceeded', 'MaxWaitTimeExceeded', 'Pending', 'PreparingTrainingStack', 'Restarting', 'Starting', 'Stopped', 'Stopping', 'Training', 'Updating', 'Uploading']
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### StatusMessage
- **Type**: typing.Optional[str]


# SelectedStep

### StepName
- **Type**: <class 'str'>
- **Required**: Yes


# SelectiveExecutionConfig

### SelectedSteps
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SelectedStep]
- **Required**: Yes

### SourcePipelineExecutionArn
- **Type**: typing.Optional[str]


# SelectiveExecutionConfigOutput

### SelectedSteps
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SelectedStep]
- **Required**: Yes

### SourcePipelineExecutionArn
- **Type**: typing.Optional[str]


# SelectiveExecutionResult

### SourcePipelineExecutionArn
- **Type**: typing.Optional[str]


# SendPipelineExecutionStepFailureRequest

### CallbackToken
- **Type**: <class 'str'>
- **Required**: Yes

### FailureReason
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]


# SendPipelineExecutionStepFailureResponse

### PipelineExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# SendPipelineExecutionStepSuccessRequest

### CallbackToken
- **Type**: <class 'str'>
- **Required**: Yes

### OutputParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OutputParameter]]

### ClientRequestToken
- **Type**: typing.Optional[str]


# SendPipelineExecutionStepSuccessResponse

### PipelineExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# ServiceCatalogProvisionedProductDetails

### ProvisionedProductId
- **Type**: typing.Optional[str]

### ProvisionedProductStatusMessage
- **Type**: typing.Optional[str]


# ServiceCatalogProvisioningDetails

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisioningArtifactId
- **Type**: typing.Optional[str]

### PathId
- **Type**: typing.Optional[str]

### ProvisioningParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProvisioningParameter]]


# ServiceCatalogProvisioningDetailsOutput

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisioningArtifactId
- **Type**: typing.Optional[str]

### PathId
- **Type**: typing.Optional[str]

### ProvisioningParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProvisioningParameter]]


# ServiceCatalogProvisioningUpdateDetails

### ProvisioningArtifactId
- **Type**: typing.Optional[str]

### ProvisioningParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProvisioningParameter]]


# SessionChainingConfig

### EnableSessionTagChaining
- **Type**: typing.Optional[bool]


# ShadowModeConfig

### SourceModelVariantName
- **Type**: <class 'str'>
- **Required**: Yes

### ShadowModelVariants
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ShadowModelVariantConfig]
- **Required**: Yes


# ShadowModeConfigOutput

### SourceModelVariantName
- **Type**: <class 'str'>
- **Required**: Yes

### ShadowModelVariants
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ShadowModelVariantConfig]
- **Required**: Yes


# ShadowModelVariantConfig

### ShadowModelVariantName
- **Type**: <class 'str'>
- **Required**: Yes

### SamplingPercentage
- **Type**: <class 'int'>
- **Required**: Yes


# SharingSettings

### NotebookOutputOption
- **Type**: typing.Optional[typing.Literal['Allowed', 'Disabled']]

### S3OutputPath
- **Type**: typing.Optional[str]

### S3KmsKeyId
- **Type**: typing.Optional[str]


# ShuffleConfig

### Seed
- **Type**: <class 'int'>
- **Required**: Yes


# SourceAlgorithm

### AlgorithmName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelDataUrl
- **Type**: typing.Optional[str]

### ModelDataSource
- **Type**: <class 'NoneType'>

### ModelDataETag
- **Type**: typing.Optional[str]


# SourceAlgorithmSpecification

### SourceAlgorithms
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SourceAlgorithm]
- **Required**: Yes


# SourceAlgorithmSpecificationOutput

### SourceAlgorithms
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SourceAlgorithm]
- **Required**: Yes


# SourceIpConfig

### Cidrs
- **Type**: typing.List[str]
- **Required**: Yes


# SourceIpConfigOutput

### Cidrs
- **Type**: typing.List[str]
- **Required**: Yes


# SpaceAppLifecycleManagement

### IdleSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SpaceIdleSettings]


# SpaceCodeEditorAppSettings

### DefaultResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResourceSpec]

### AppLifecycleManagement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SpaceAppLifecycleManagement]


# SpaceDetails

### DomainId
- **Type**: typing.Optional[str]

### SpaceName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Delete_Failed', 'Deleting', 'Failed', 'InService', 'Pending', 'Update_Failed', 'Updating']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### SpaceSettingsSummary
- **Type**: <class 'NoneType'>

### SpaceSharingSettingsSummary
- **Type**: <class 'NoneType'>

### OwnershipSettingsSummary
- **Type**: <class 'NoneType'>

### SpaceDisplayName
- **Type**: typing.Optional[str]


# SpaceIdleSettings

### IdleTimeoutInMinutes
- **Type**: typing.Optional[int]


# SpaceJupyterLabAppSettings

### DefaultResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResourceSpec]

### CodeRepositories
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CodeRepository]]

### AppLifecycleManagement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SpaceAppLifecycleManagement]


# SpaceJupyterLabAppSettingsOutput

### DefaultResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResourceSpec]

### CodeRepositories
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CodeRepository]]

### AppLifecycleManagement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SpaceAppLifecycleManagement]


# SpaceSettings

### JupyterServerAppSettings
- **Type**: <class 'NoneType'>

### KernelGatewayAppSettings
- **Type**: <class 'NoneType'>

### CodeEditorAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SpaceCodeEditorAppSettings]

### JupyterLabAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SpaceJupyterLabAppSettings]

### AppType
- **Type**: typing.Optional[typing.Literal['Canvas', 'CodeEditor', 'DetailedProfiler', 'JupyterLab', 'JupyterServer', 'KernelGateway', 'RSessionGateway', 'RStudioServerPro', 'TensorBoard']]

### SpaceStorageSettings
- **Type**: <class 'NoneType'>

### CustomFileSystems
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CustomFileSystem]]


# SpaceSettingsOutput

### JupyterServerAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.JupyterServerAppSettingsOutput]

### KernelGatewayAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.KernelGatewayAppSettingsOutput]

### CodeEditorAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SpaceCodeEditorAppSettings]

### JupyterLabAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SpaceJupyterLabAppSettingsOutput]

### AppType
- **Type**: typing.Optional[typing.Literal['Canvas', 'CodeEditor', 'DetailedProfiler', 'JupyterLab', 'JupyterServer', 'KernelGateway', 'RSessionGateway', 'RStudioServerPro', 'TensorBoard']]

### SpaceStorageSettings
- **Type**: <class 'NoneType'>

### CustomFileSystems
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CustomFileSystem]]


# SpaceSettingsSummary

### AppType
- **Type**: typing.Optional[typing.Literal['Canvas', 'CodeEditor', 'DetailedProfiler', 'JupyterLab', 'JupyterServer', 'KernelGateway', 'RSessionGateway', 'RStudioServerPro', 'TensorBoard']]

### SpaceStorageSettings
- **Type**: <class 'NoneType'>


# SpaceSharingSettings

### SharingType
- **Type**: typing.Literal['Private', 'Shared']
- **Required**: Yes


# SpaceSharingSettingsSummary

### SharingType
- **Type**: typing.Optional[typing.Literal['Private', 'Shared']]


# SpaceStorageSettings

### EbsStorageSettings
- **Type**: <class 'NoneType'>


# Stairs

### DurationInSeconds
- **Type**: typing.Optional[int]

### NumberOfSteps
- **Type**: typing.Optional[int]

### UsersPerStep
- **Type**: typing.Optional[int]


# StartEdgeDeploymentStageRequest

### EdgeDeploymentPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### StageName
- **Type**: <class 'str'>
- **Required**: Yes


# StartInferenceExperimentRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# StartInferenceExperimentResponse

### InferenceExperimentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# StartMlflowTrackingServerRequest

### TrackingServerName
- **Type**: <class 'str'>
- **Required**: Yes


# StartMlflowTrackingServerResponse

### TrackingServerArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# StartMonitoringScheduleRequest

### MonitoringScheduleName
- **Type**: <class 'str'>
- **Required**: Yes


# StartNotebookInstanceInput

### NotebookInstanceName
- **Type**: <class 'str'>
- **Required**: Yes


# StartPipelineExecutionRequest

### PipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineExecutionDisplayName
- **Type**: typing.Optional[str]

### PipelineParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Parameter]]

### PipelineExecutionDescription
- **Type**: typing.Optional[str]

### ParallelismConfiguration
- **Type**: <class 'NoneType'>

### SelectiveExecutionConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SelectiveExecutionConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SelectiveExecutionConfigOutput, NoneType]


# StartPipelineExecutionResponse

### PipelineExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# StopAutoMLJobRequest

### AutoMLJobName
- **Type**: <class 'str'>
- **Required**: Yes


# StopCompilationJobRequest

### CompilationJobName
- **Type**: <class 'str'>
- **Required**: Yes


# StopEdgeDeploymentStageRequest

### EdgeDeploymentPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### StageName
- **Type**: <class 'str'>
- **Required**: Yes


# StopEdgePackagingJobRequest

### EdgePackagingJobName
- **Type**: <class 'str'>
- **Required**: Yes


# StopHyperParameterTuningJobRequest

### HyperParameterTuningJobName
- **Type**: <class 'str'>
- **Required**: Yes


# StopInferenceExperimentRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVariantActions
- **Type**: typing.Dict[str, typing.Literal['Promote', 'Remove', 'Retain']]
- **Required**: Yes

### DesiredModelVariants
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelVariantConfig]]

### DesiredState
- **Type**: typing.Optional[typing.Literal['Cancelled', 'Completed']]

### Reason
- **Type**: typing.Optional[str]


# StopInferenceExperimentResponse

### InferenceExperimentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# StopInferenceRecommendationsJobRequest

### JobName
- **Type**: <class 'str'>
- **Required**: Yes


# StopLabelingJobRequest

### LabelingJobName
- **Type**: <class 'str'>
- **Required**: Yes


# StopMlflowTrackingServerRequest

### TrackingServerName
- **Type**: <class 'str'>
- **Required**: Yes


# StopMlflowTrackingServerResponse

### TrackingServerArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# StopMonitoringScheduleRequest

### MonitoringScheduleName
- **Type**: <class 'str'>
- **Required**: Yes


# StopNotebookInstanceInput

### NotebookInstanceName
- **Type**: <class 'str'>
- **Required**: Yes


# StopOptimizationJobRequest

### OptimizationJobName
- **Type**: <class 'str'>
- **Required**: Yes


# StopPipelineExecutionRequest

### PipelineExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# StopPipelineExecutionResponse

### PipelineExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# StopProcessingJobRequest

### ProcessingJobName
- **Type**: <class 'str'>
- **Required**: Yes


# StopTrainingJobRequest

### TrainingJobName
- **Type**: <class 'str'>
- **Required**: Yes


# StopTransformJobRequest

### TransformJobName
- **Type**: <class 'str'>
- **Required**: Yes


# StoppingCondition

### MaxRuntimeInSeconds
- **Type**: typing.Optional[int]

### MaxWaitTimeInSeconds
- **Type**: typing.Optional[int]

### MaxPendingTimeInSeconds
- **Type**: typing.Optional[int]


# StudioLifecycleConfigDetails

### StudioLifecycleConfigArn
- **Type**: typing.Optional[str]

### StudioLifecycleConfigName
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### StudioLifecycleConfigAppType
- **Type**: typing.Optional[typing.Literal['CodeEditor', 'JupyterLab', 'JupyterServer', 'KernelGateway']]


# StudioWebPortalSettings

### HiddenMlTools
- **Type**: typing.Optional[typing.List[typing.Literal['AutoMl', 'Comet', 'DataWrangler', 'DeepchecksLLMEvaluation', 'EmrClusters', 'Endpoints', 'Experiments', 'FeatureStore', 'Fiddler', 'HyperPodClusters', 'InferenceOptimization', 'InferenceRecommender', 'JumpStart', 'LakeraGuard', 'ModelEvaluation', 'Models', 'PerformanceEvaluation', 'Pipelines', 'Projects', 'Training']]]

### HiddenAppTypes
- **Type**: typing.Optional[typing.List[typing.Literal['Canvas', 'CodeEditor', 'DetailedProfiler', 'JupyterLab', 'JupyterServer', 'KernelGateway', 'RSessionGateway', 'RStudioServerPro', 'TensorBoard']]]

### HiddenInstanceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ml.c5.12xlarge', 'ml.c5.18xlarge', 'ml.c5.24xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c6id.12xlarge', 'ml.c6id.16xlarge', 'ml.c6id.24xlarge', 'ml.c6id.2xlarge', 'ml.c6id.32xlarge', 'ml.c6id.4xlarge', 'ml.c6id.8xlarge', 'ml.c6id.large', 'ml.c6id.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.geospatial.interactive', 'ml.m5.12xlarge', 'ml.m5.16xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.8xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.16xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.8xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m6id.12xlarge', 'ml.m6id.16xlarge', 'ml.m6id.24xlarge', 'ml.m6id.2xlarge', 'ml.m6id.32xlarge', 'ml.m6id.4xlarge', 'ml.m6id.8xlarge', 'ml.m6id.large', 'ml.m6id.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r6id.12xlarge', 'ml.r6id.16xlarge', 'ml.r6id.24xlarge', 'ml.r6id.2xlarge', 'ml.r6id.32xlarge', 'ml.r6id.4xlarge', 'ml.r6id.8xlarge', 'ml.r6id.large', 'ml.r6id.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.micro', 'ml.t3.small', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'system']]]

### HiddenSageMakerImageVersionAliases
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HiddenSageMakerImage]]


# StudioWebPortalSettingsOutput

### HiddenMlTools
- **Type**: typing.Optional[typing.List[typing.Literal['AutoMl', 'Comet', 'DataWrangler', 'DeepchecksLLMEvaluation', 'EmrClusters', 'Endpoints', 'Experiments', 'FeatureStore', 'Fiddler', 'HyperPodClusters', 'InferenceOptimization', 'InferenceRecommender', 'JumpStart', 'LakeraGuard', 'ModelEvaluation', 'Models', 'PerformanceEvaluation', 'Pipelines', 'Projects', 'Training']]]

### HiddenAppTypes
- **Type**: typing.Optional[typing.List[typing.Literal['Canvas', 'CodeEditor', 'DetailedProfiler', 'JupyterLab', 'JupyterServer', 'KernelGateway', 'RSessionGateway', 'RStudioServerPro', 'TensorBoard']]]

### HiddenInstanceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ml.c5.12xlarge', 'ml.c5.18xlarge', 'ml.c5.24xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c6id.12xlarge', 'ml.c6id.16xlarge', 'ml.c6id.24xlarge', 'ml.c6id.2xlarge', 'ml.c6id.32xlarge', 'ml.c6id.4xlarge', 'ml.c6id.8xlarge', 'ml.c6id.large', 'ml.c6id.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.geospatial.interactive', 'ml.m5.12xlarge', 'ml.m5.16xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.8xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.16xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.8xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m6id.12xlarge', 'ml.m6id.16xlarge', 'ml.m6id.24xlarge', 'ml.m6id.2xlarge', 'ml.m6id.32xlarge', 'ml.m6id.4xlarge', 'ml.m6id.8xlarge', 'ml.m6id.large', 'ml.m6id.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r6id.12xlarge', 'ml.r6id.16xlarge', 'ml.r6id.24xlarge', 'ml.r6id.2xlarge', 'ml.r6id.32xlarge', 'ml.r6id.4xlarge', 'ml.r6id.8xlarge', 'ml.r6id.large', 'ml.r6id.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.micro', 'ml.t3.small', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'system']]]

### HiddenSageMakerImageVersionAliases
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HiddenSageMakerImageOutput]]


# SubscribedWorkteam

### WorkteamArn
- **Type**: <class 'str'>
- **Required**: Yes

### MarketplaceTitle
- **Type**: typing.Optional[str]

### SellerName
- **Type**: typing.Optional[str]

### MarketplaceDescription
- **Type**: typing.Optional[str]

### ListingId
- **Type**: typing.Optional[str]


# SuggestionQuery

### PropertyNameQuery
- **Type**: <class 'NoneType'>


# TabularJobConfig

### TargetAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### CandidateGenerationConfig
- **Type**: <class 'NoneType'>

### CompletionCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLJobCompletionCriteria]

### FeatureSpecificationS3Uri
- **Type**: typing.Optional[str]

### Mode
- **Type**: typing.Optional[typing.Literal['AUTO', 'ENSEMBLING', 'HYPERPARAMETER_TUNING']]

### GenerateCandidateDefinitionsOnly
- **Type**: typing.Optional[bool]

### ProblemType
- **Type**: typing.Optional[typing.Literal['BinaryClassification', 'MulticlassClassification', 'Regression']]

### SampleWeightAttributeName
- **Type**: typing.Optional[str]


# TabularJobConfigOutput

### TargetAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### CandidateGenerationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CandidateGenerationConfigOutput]

### CompletionCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLJobCompletionCriteria]

### FeatureSpecificationS3Uri
- **Type**: typing.Optional[str]

### Mode
- **Type**: typing.Optional[typing.Literal['AUTO', 'ENSEMBLING', 'HYPERPARAMETER_TUNING']]

### GenerateCandidateDefinitionsOnly
- **Type**: typing.Optional[bool]

### ProblemType
- **Type**: typing.Optional[typing.Literal['BinaryClassification', 'MulticlassClassification', 'Regression']]

### SampleWeightAttributeName
- **Type**: typing.Optional[str]


# TabularResolvedAttributes

### ProblemType
- **Type**: typing.Optional[typing.Literal['BinaryClassification', 'MulticlassClassification', 'Regression']]


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TargetPlatform

### Os
- **Type**: typing.Literal['ANDROID', 'LINUX']
- **Required**: Yes

### Arch
- **Type**: typing.Literal['ARM64', 'ARM_EABI', 'ARM_EABIHF', 'X86', 'X86_64']
- **Required**: Yes

### Accelerator
- **Type**: typing.Optional[typing.Literal['INTEL_GRAPHICS', 'MALI', 'NNA', 'NVIDIA']]


# TargetTrackingScalingPolicyConfiguration

### MetricSpecification
- **Type**: <class 'NoneType'>

### TargetValue
- **Type**: typing.Optional[float]


# TensorBoardAppSettings

### DefaultResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResourceSpec]


# TensorBoardOutputConfig

### S3OutputPath
- **Type**: <class 'str'>
- **Required**: Yes

### LocalPath
- **Type**: typing.Optional[str]


# TextClassificationJobConfig

### ContentColumn
- **Type**: <class 'str'>
- **Required**: Yes

### TargetLabelColumn
- **Type**: <class 'str'>
- **Required**: Yes

### CompletionCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLJobCompletionCriteria]


# TextGenerationJobConfig

### CompletionCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLJobCompletionCriteria]

### BaseModelName
- **Type**: typing.Optional[str]

### TextGenerationHyperParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### ModelAccessConfig
- **Type**: <class 'NoneType'>


# TextGenerationJobConfigOutput

### CompletionCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLJobCompletionCriteria]

### BaseModelName
- **Type**: typing.Optional[str]

### TextGenerationHyperParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### ModelAccessConfig
- **Type**: <class 'NoneType'>


# TextGenerationResolvedAttributes

### BaseModelName
- **Type**: typing.Optional[str]


# ThroughputConfig

### ThroughputMode
- **Type**: typing.Literal['OnDemand', 'Provisioned']
- **Required**: Yes

### ProvisionedReadCapacityUnits
- **Type**: typing.Optional[int]

### ProvisionedWriteCapacityUnits
- **Type**: typing.Optional[int]


# ThroughputConfigDescription

### ThroughputMode
- **Type**: typing.Literal['OnDemand', 'Provisioned']
- **Required**: Yes

### ProvisionedReadCapacityUnits
- **Type**: typing.Optional[int]

### ProvisionedWriteCapacityUnits
- **Type**: typing.Optional[int]


# ThroughputConfigUpdate

### ThroughputMode
- **Type**: typing.Optional[typing.Literal['OnDemand', 'Provisioned']]

### ProvisionedReadCapacityUnits
- **Type**: typing.Optional[int]

### ProvisionedWriteCapacityUnits
- **Type**: typing.Optional[int]


# TimeSeriesConfig

### TargetAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### TimestampAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### ItemIdentifierAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### GroupingAttributeNames
- **Type**: typing.Optional[typing.List[str]]


# TimeSeriesConfigOutput

### TargetAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### TimestampAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### ItemIdentifierAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### GroupingAttributeNames
- **Type**: typing.Optional[typing.List[str]]


# TimeSeriesForecastingJobConfig

### ForecastFrequency
- **Type**: <class 'str'>
- **Required**: Yes

### ForecastHorizon
- **Type**: <class 'int'>
- **Required**: Yes

### TimeSeriesConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TimeSeriesConfig'>
- **Required**: Yes

### FeatureSpecificationS3Uri
- **Type**: typing.Optional[str]

### CompletionCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLJobCompletionCriteria]

### ForecastQuantiles
- **Type**: typing.Optional[typing.List[str]]

### Transformations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TimeSeriesTransformations]

### HolidayConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HolidayConfigAttributes]]

### CandidateGenerationConfig
- **Type**: <class 'NoneType'>


# TimeSeriesForecastingJobConfigOutput

### ForecastFrequency
- **Type**: <class 'str'>
- **Required**: Yes

### ForecastHorizon
- **Type**: <class 'int'>
- **Required**: Yes

### TimeSeriesConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TimeSeriesConfigOutput'>
- **Required**: Yes

### FeatureSpecificationS3Uri
- **Type**: typing.Optional[str]

### CompletionCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AutoMLJobCompletionCriteria]

### ForecastQuantiles
- **Type**: typing.Optional[typing.List[str]]

### Transformations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TimeSeriesTransformationsOutput]

### HolidayConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HolidayConfigAttributes]]

### CandidateGenerationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CandidateGenerationConfigOutput]


# TimeSeriesForecastingSettings

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### AmazonForecastRoleArn
- **Type**: typing.Optional[str]


# TimeSeriesTransformations

### Filling
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[typing.Literal['backfill', 'backfill_value', 'frontfill', 'frontfill_value', 'futurefill', 'futurefill_value', 'middlefill', 'middlefill_value'], str]]]

### Aggregation
- **Type**: typing.Optional[typing.Dict[str, typing.Literal['avg', 'first', 'max', 'min', 'sum']]]


# TimeSeriesTransformationsOutput

### Filling
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[typing.Literal['backfill', 'backfill_value', 'frontfill', 'frontfill_value', 'futurefill', 'futurefill_value', 'middlefill', 'middlefill_value'], str]]]

### Aggregation
- **Type**: typing.Optional[typing.Dict[str, typing.Literal['avg', 'first', 'max', 'min', 'sum']]]


# TrackingServerSummary

### TrackingServerArn
- **Type**: typing.Optional[str]

### TrackingServerName
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### TrackingServerStatus
- **Type**: typing.Optional[typing.Literal['CreateFailed', 'Created', 'Creating', 'DeleteFailed', 'Deleting', 'MaintenanceComplete', 'MaintenanceFailed', 'MaintenanceInProgress', 'StartFailed', 'Started', 'Starting', 'StopFailed', 'Stopped', 'Stopping', 'UpdateFailed', 'Updated', 'Updating']]

### IsActive
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]

### MlflowVersion
- **Type**: typing.Optional[str]


# TrafficPattern

### TrafficType
- **Type**: typing.Optional[typing.Literal['PHASES', 'STAIRS']]

### Phases
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Phase]]

### Stairs
- **Type**: <class 'NoneType'>


# TrafficPatternOutput

### TrafficType
- **Type**: typing.Optional[typing.Literal['PHASES', 'STAIRS']]

### Phases
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Phase]]

### Stairs
- **Type**: <class 'NoneType'>


# TrafficRoutingConfig

### Type
- **Type**: typing.Literal['ALL_AT_ONCE', 'CANARY', 'LINEAR']
- **Required**: Yes

### WaitIntervalInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### CanarySize
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CapacitySize]

### LinearStepSize
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CapacitySize]


# TrainingImageConfig

### TrainingRepositoryAccessMode
- **Type**: typing.Literal['Platform', 'Vpc']
- **Required**: Yes

### TrainingRepositoryAuthConfig
- **Type**: <class 'NoneType'>


# TrainingJob

### TrainingJobName
- **Type**: typing.Optional[str]

### TrainingJobArn
- **Type**: typing.Optional[str]

### TuningJobArn
- **Type**: typing.Optional[str]

### LabelingJobArn
- **Type**: typing.Optional[str]

### AutoMLJobArn
- **Type**: typing.Optional[str]

### ModelArtifacts
- **Type**: <class 'NoneType'>

### TrainingJobStatus
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### SecondaryStatus
- **Type**: typing.Optional[typing.Literal['Completed', 'Downloading', 'DownloadingTrainingImage', 'Failed', 'Interrupted', 'LaunchingMLInstances', 'MaxRuntimeExceeded', 'MaxWaitTimeExceeded', 'Pending', 'PreparingTrainingStack', 'Restarting', 'Starting', 'Stopped', 'Stopping', 'Training', 'Updating', 'Uploading']]

### FailureReason
- **Type**: typing.Optional[str]

### HyperParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### AlgorithmSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AlgorithmSpecificationOutput]

### RoleArn
- **Type**: typing.Optional[str]

### InputDataConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ChannelOutput]]

### OutputDataConfig
- **Type**: <class 'NoneType'>

### ResourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResourceConfigOutput]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.VpcConfigOutput]

### StoppingCondition
- **Type**: <class 'NoneType'>

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### TrainingStartTime
- **Type**: typing.Optional[datetime.datetime]

### TrainingEndTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### SecondaryStatusTransitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SecondaryStatusTransition]]

### FinalMetricDataList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MetricData]]

### EnableNetworkIsolation
- **Type**: typing.Optional[bool]

### EnableInterContainerTrafficEncryption
- **Type**: typing.Optional[bool]

### EnableManagedSpotTraining
- **Type**: typing.Optional[bool]

### CheckpointConfig
- **Type**: <class 'NoneType'>

### TrainingTimeInSeconds
- **Type**: typing.Optional[int]

### BillableTimeInSeconds
- **Type**: typing.Optional[int]

### DebugHookConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DebugHookConfigOutput]

### ExperimentConfig
- **Type**: <class 'NoneType'>

### DebugRuleConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DebugRuleConfigurationOutput]]

### TensorBoardOutputConfig
- **Type**: <class 'NoneType'>

### DebugRuleEvaluationStatuses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DebugRuleEvaluationStatus]]

### ProfilerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProfilerConfigOutput]

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]

### RetryStrategy
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# TrainingJobDefinition

### TrainingInputMode
- **Type**: typing.Literal['FastFile', 'File', 'Pipe']
- **Required**: Yes

### InputDataConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Channel]
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OutputDataConfig'>
- **Required**: Yes

### ResourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResourceConfig'>
- **Required**: Yes

### StoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.StoppingCondition'>
- **Required**: Yes

### HyperParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# TrainingJobDefinitionOutput

### TrainingInputMode
- **Type**: typing.Literal['FastFile', 'File', 'Pipe']
- **Required**: Yes

### InputDataConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ChannelOutput]
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OutputDataConfig'>
- **Required**: Yes

### ResourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResourceConfigOutput'>
- **Required**: Yes

### StoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.StoppingCondition'>
- **Required**: Yes

### HyperParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# TrainingJobStatusCounters

### Completed
- **Type**: typing.Optional[int]

### InProgress
- **Type**: typing.Optional[int]

### RetryableError
- **Type**: typing.Optional[int]

### NonRetryableError
- **Type**: typing.Optional[int]

### Stopped
- **Type**: typing.Optional[int]


# TrainingJobStepMetadata

### Arn
- **Type**: typing.Optional[str]


# TrainingJobSummary

### TrainingJobName
- **Type**: <class 'str'>
- **Required**: Yes

### TrainingJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TrainingJobStatus
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']
- **Required**: Yes

### TrainingEndTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### SecondaryStatus
- **Type**: typing.Optional[typing.Literal['Completed', 'Downloading', 'DownloadingTrainingImage', 'Failed', 'Interrupted', 'LaunchingMLInstances', 'MaxRuntimeExceeded', 'MaxWaitTimeExceeded', 'Pending', 'PreparingTrainingStack', 'Restarting', 'Starting', 'Stopped', 'Stopping', 'Training', 'Updating', 'Uploading']]

### WarmPoolStatus
- **Type**: <class 'NoneType'>

### TrainingPlanArn
- **Type**: typing.Optional[str]


# TrainingPlanFilter

### Name
- **Type**: typing.Literal['Status']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TrainingPlanOffering

### TrainingPlanOfferingId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetResources
- **Type**: typing.List[typing.Literal['hyperpod-cluster', 'training-job']]
- **Required**: Yes

### RequestedStartTimeAfter
- **Type**: typing.Optional[datetime.datetime]

### RequestedEndTimeBefore
- **Type**: typing.Optional[datetime.datetime]

### DurationHours
- **Type**: typing.Optional[int]

### DurationMinutes
- **Type**: typing.Optional[int]

### UpfrontFee
- **Type**: typing.Optional[str]

### CurrencyCode
- **Type**: typing.Optional[str]

### ReservedCapacityOfferings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ReservedCapacityOffering]]


# TrainingPlanSummary

### TrainingPlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### TrainingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Active', 'Expired', 'Failed', 'Pending', 'Scheduled']
- **Required**: Yes

### StatusMessage
- **Type**: typing.Optional[str]

### DurationHours
- **Type**: typing.Optional[int]

### DurationMinutes
- **Type**: typing.Optional[int]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### UpfrontFee
- **Type**: typing.Optional[str]

### CurrencyCode
- **Type**: typing.Optional[str]

### TotalInstanceCount
- **Type**: typing.Optional[int]

### AvailableInstanceCount
- **Type**: typing.Optional[int]

### InUseInstanceCount
- **Type**: typing.Optional[int]

### TargetResources
- **Type**: typing.Optional[typing.List[typing.Literal['hyperpod-cluster', 'training-job']]]

### ReservedCapacitySummaries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ReservedCapacitySummary]]


# TrainingRepositoryAuthConfig

### TrainingRepositoryCredentialsProviderArn
- **Type**: <class 'str'>
- **Required**: Yes


# TrainingSpecification

### TrainingImage
- **Type**: <class 'str'>
- **Required**: Yes

### SupportedTrainingInstanceTypes
- **Type**: typing.List[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c5n.18xlarge', 'ml.c5n.2xlarge', 'ml.c5n.4xlarge', 'ml.c5n.9xlarge', 'ml.c5n.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.16xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.8xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]
- **Required**: Yes

### TrainingChannels
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ChannelSpecification]
- **Required**: Yes

### TrainingImageDigest
- **Type**: typing.Optional[str]

### SupportedHyperParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterSpecification]]

### SupportsDistributedTraining
- **Type**: typing.Optional[bool]

### MetricDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MetricDefinition]]

### SupportedTuningJobObjectiveMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTuningJobObjective]]

### AdditionalS3DataSource
- **Type**: <class 'NoneType'>


# TrainingSpecificationOutput

### TrainingImage
- **Type**: <class 'str'>
- **Required**: Yes

### SupportedTrainingInstanceTypes
- **Type**: typing.List[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c5n.18xlarge', 'ml.c5n.2xlarge', 'ml.c5n.4xlarge', 'ml.c5n.9xlarge', 'ml.c5n.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.16xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.8xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]
- **Required**: Yes

### TrainingChannels
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ChannelSpecificationOutput]
- **Required**: Yes

### TrainingImageDigest
- **Type**: typing.Optional[str]

### SupportedHyperParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterSpecificationOutput]]

### SupportsDistributedTraining
- **Type**: typing.Optional[bool]

### MetricDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MetricDefinition]]

### SupportedTuningJobObjectiveMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.HyperParameterTuningJobObjective]]

### AdditionalS3DataSource
- **Type**: <class 'NoneType'>


# TransformDataSource

### S3DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TransformS3DataSource'>
- **Required**: Yes


# TransformInput

### DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TransformDataSource'>
- **Required**: Yes

### ContentType
- **Type**: typing.Optional[str]

### CompressionType
- **Type**: typing.Optional[typing.Literal['Gzip', 'None']]

### SplitType
- **Type**: typing.Optional[typing.Literal['Line', 'None', 'RecordIO', 'TFRecord']]


# TransformJob

### TransformJobName
- **Type**: typing.Optional[str]

### TransformJobArn
- **Type**: typing.Optional[str]

### TransformJobStatus
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### FailureReason
- **Type**: typing.Optional[str]

### ModelName
- **Type**: typing.Optional[str]

### MaxConcurrentTransforms
- **Type**: typing.Optional[int]

### ModelClientConfig
- **Type**: <class 'NoneType'>

### MaxPayloadInMB
- **Type**: typing.Optional[int]

### BatchStrategy
- **Type**: typing.Optional[typing.Literal['MultiRecord', 'SingleRecord']]

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]

### TransformInput
- **Type**: <class 'NoneType'>

### TransformOutput
- **Type**: <class 'NoneType'>

### DataCaptureConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.BatchDataCaptureConfig]

### TransformResources
- **Type**: <class 'NoneType'>

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### TransformStartTime
- **Type**: typing.Optional[datetime.datetime]

### TransformEndTime
- **Type**: typing.Optional[datetime.datetime]

### LabelingJobArn
- **Type**: typing.Optional[str]

### AutoMLJobArn
- **Type**: typing.Optional[str]

### DataProcessing
- **Type**: <class 'NoneType'>

### ExperimentConfig
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# TransformJobDefinition

### TransformInput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TransformInput'>
- **Required**: Yes

### TransformOutput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TransformOutput'>
- **Required**: Yes

### TransformResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TransformResources'>
- **Required**: Yes

### MaxConcurrentTransforms
- **Type**: typing.Optional[int]

### MaxPayloadInMB
- **Type**: typing.Optional[int]

### BatchStrategy
- **Type**: typing.Optional[typing.Literal['MultiRecord', 'SingleRecord']]

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]


# TransformJobDefinitionOutput

### TransformInput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TransformInput'>
- **Required**: Yes

### TransformOutput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TransformOutput'>
- **Required**: Yes

### TransformResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TransformResources'>
- **Required**: Yes

### MaxConcurrentTransforms
- **Type**: typing.Optional[int]

### MaxPayloadInMB
- **Type**: typing.Optional[int]

### BatchStrategy
- **Type**: typing.Optional[typing.Literal['MultiRecord', 'SingleRecord']]

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]


# TransformJobStepMetadata

### Arn
- **Type**: typing.Optional[str]


# TransformJobSummary

### TransformJobName
- **Type**: <class 'str'>
- **Required**: Yes

### TransformJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TransformJobStatus
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']
- **Required**: Yes

### TransformEndTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### FailureReason
- **Type**: typing.Optional[str]


# TransformOutput

### S3OutputPath
- **Type**: <class 'str'>
- **Required**: Yes

### Accept
- **Type**: typing.Optional[str]

### AssembleWith
- **Type**: typing.Optional[typing.Literal['Line', 'None']]

### KmsKeyId
- **Type**: typing.Optional[str]


# TransformResources

### InstanceType
- **Type**: typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge']
- **Required**: Yes

### InstanceCount
- **Type**: <class 'int'>
- **Required**: Yes

### VolumeKmsKeyId
- **Type**: typing.Optional[str]


# TransformS3DataSource

### S3DataType
- **Type**: typing.Literal['AugmentedManifestFile', 'ManifestFile', 'S3Prefix']
- **Required**: Yes

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes


# Trial

### TrialName
- **Type**: typing.Optional[str]

### TrialArn
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### ExperimentName
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrialSource]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext]

### MetadataProperties
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]

### TrialComponentSummaries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrialComponentSimpleSummary]]


# TrialComponent

### TrialComponentName
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### TrialComponentArn
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrialComponentSource]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrialComponentStatus]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrialComponentParameterValue]]

### InputArtifacts
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrialComponentArtifact]]

### OutputArtifacts
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrialComponentArtifact]]

### Metrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrialComponentMetricSummary]]

### MetadataProperties
- **Type**: <class 'NoneType'>

### SourceDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrialComponentSourceDetail]

### LineageGroupArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]

### Parents
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Parent]]

### RunName
- **Type**: typing.Optional[str]


# TrialComponentArtifact

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### MediaType
- **Type**: typing.Optional[str]


# TrialComponentMetricSummary

### MetricName
- **Type**: typing.Optional[str]

### SourceArn
- **Type**: typing.Optional[str]

### TimeStamp
- **Type**: typing.Optional[datetime.datetime]

### Max
- **Type**: typing.Optional[float]

### Min
- **Type**: typing.Optional[float]

### Last
- **Type**: typing.Optional[float]

### Count
- **Type**: typing.Optional[int]

### Avg
- **Type**: typing.Optional[float]

### StdDev
- **Type**: typing.Optional[float]


# TrialComponentParameterValue

### StringValue
- **Type**: typing.Optional[str]

### NumberValue
- **Type**: typing.Optional[float]


# TrialComponentSimpleSummary

### TrialComponentName
- **Type**: typing.Optional[str]

### TrialComponentArn
- **Type**: typing.Optional[str]

### TrialComponentSource
- **Type**: <class 'NoneType'>

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext]


# TrialComponentSource

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceType
- **Type**: typing.Optional[str]


# TrialComponentSourceDetail

### SourceArn
- **Type**: typing.Optional[str]

### TrainingJob
- **Type**: <class 'NoneType'>

### ProcessingJob
- **Type**: <class 'NoneType'>

### TransformJob
- **Type**: <class 'NoneType'>


# TrialComponentStatus

### PrimaryStatus
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### Message
- **Type**: typing.Optional[str]


# TrialComponentSummary

### TrialComponentName
- **Type**: typing.Optional[str]

### TrialComponentArn
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### TrialComponentSource
- **Type**: <class 'NoneType'>

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrialComponentStatus]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserContext]


# TrialSource

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceType
- **Type**: typing.Optional[str]


# TrialSummary

### TrialArn
- **Type**: typing.Optional[str]

### TrialName
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### TrialSource
- **Type**: <class 'NoneType'>

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# TtlDuration

### Unit
- **Type**: typing.Optional[typing.Literal['Days', 'Hours', 'Minutes', 'Seconds', 'Weeks']]

### Value
- **Type**: typing.Optional[int]


# TuningJobCompletionCriteria

### TargetObjectiveMetricValue
- **Type**: typing.Optional[float]

### BestObjectiveNotImproving
- **Type**: <class 'NoneType'>

### ConvergenceDetected
- **Type**: <class 'NoneType'>


# TuningJobStepMetaData

### Arn
- **Type**: typing.Optional[str]


# USD

### Dollars
- **Type**: typing.Optional[int]

### Cents
- **Type**: typing.Optional[int]

### TenthFractionsOfACent
- **Type**: typing.Optional[int]


# UiConfig

### UiTemplateS3Uri
- **Type**: typing.Optional[str]

### HumanTaskUiArn
- **Type**: typing.Optional[str]


# UiTemplate

### Content
- **Type**: <class 'str'>
- **Required**: Yes


# UiTemplateInfo

### Url
- **Type**: typing.Optional[str]

### ContentSha256
- **Type**: typing.Optional[str]


# UpdateActionRequest

### ActionName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping', 'Unknown']]

### Properties
- **Type**: typing.Optional[typing.Dict[str, str]]

### PropertiesToRemove
- **Type**: typing.Optional[typing.List[str]]


# UpdateActionResponse

### ActionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAppImageConfigRequest

### AppImageConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### KernelGatewayImageConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.KernelGatewayImageConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.KernelGatewayImageConfigOutput, NoneType]

### JupyterLabAppImageConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.JupyterLabAppImageConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.JupyterLabAppImageConfigOutput, NoneType]

### CodeEditorAppImageConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CodeEditorAppImageConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CodeEditorAppImageConfigOutput, NoneType]


# UpdateAppImageConfigResponse

### AppImageConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateArtifactRequest

### ArtifactArn
- **Type**: <class 'str'>
- **Required**: Yes

### ArtifactName
- **Type**: typing.Optional[str]

### Properties
- **Type**: typing.Optional[typing.Dict[str, str]]

### PropertiesToRemove
- **Type**: typing.Optional[typing.List[str]]


# UpdateArtifactResponse

### ArtifactArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateClusterRequest

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ClusterInstanceGroupSpecification]
- **Required**: Yes

### NodeRecovery
- **Type**: typing.Optional[typing.Literal['Automatic', 'None']]

### InstanceGroupsToDelete
- **Type**: typing.Optional[typing.List[str]]


# UpdateClusterResponse

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateClusterSchedulerConfigRequest

### ClusterSchedulerConfigId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetVersion
- **Type**: <class 'int'>
- **Required**: Yes

### SchedulerConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SchedulerConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SchedulerConfigOutput, NoneType]

### Description
- **Type**: typing.Optional[str]


# UpdateClusterSchedulerConfigResponse

### ClusterSchedulerConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterSchedulerConfigVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateClusterSoftwareRequest

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateClusterSoftwareResponse

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateCodeRepositoryInput

### CodeRepositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### GitConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.GitConfigForUpdate]


# UpdateCodeRepositoryOutput

### CodeRepositoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateComputeQuotaRequest

### ComputeQuotaId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ComputeQuotaConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ComputeQuotaConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ComputeQuotaConfigOutput, NoneType]

### ComputeQuotaTarget
- **Type**: <class 'NoneType'>

### ActivationState
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### Description
- **Type**: typing.Optional[str]


# UpdateComputeQuotaResponse

### ComputeQuotaArn
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeQuotaVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateContextRequest

### ContextName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Properties
- **Type**: typing.Optional[typing.Dict[str, str]]

### PropertiesToRemove
- **Type**: typing.Optional[typing.List[str]]


# UpdateContextResponse

### ContextArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDeviceFleetRequest

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.EdgeOutputConfig'>
- **Required**: Yes

### RoleArn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EnableIotRoleAlias
- **Type**: typing.Optional[bool]


# UpdateDevicesRequest

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes

### Devices
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Device]
- **Required**: Yes


# UpdateDomainRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultUserSettings
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserSettings, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserSettingsOutput, NoneType]

### DomainSettingsForUpdate
- **Type**: <class 'NoneType'>

### AppSecurityGroupManagement
- **Type**: typing.Optional[typing.Literal['Customer', 'Service']]

### DefaultSpaceSettings
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DefaultSpaceSettings, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DefaultSpaceSettingsOutput, NoneType]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### AppNetworkAccessType
- **Type**: typing.Optional[typing.Literal['PublicInternetOnly', 'VpcOnly']]

### TagPropagation
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# UpdateDomainResponse

### DomainArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEndpointInput

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### RetainAllVariantProperties
- **Type**: typing.Optional[bool]

### ExcludeRetainedVariantProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.VariantProperty]]

### DeploymentConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DeploymentConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DeploymentConfigOutput, NoneType]

### RetainDeploymentConfig
- **Type**: typing.Optional[bool]


# UpdateEndpointOutput

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEndpointWeightsAndCapacitiesInput

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### DesiredWeightsAndCapacities
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DesiredWeightAndCapacity]
- **Required**: Yes


# UpdateEndpointWeightsAndCapacitiesOutput

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateExperimentRequest

### ExperimentName
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# UpdateExperimentResponse

### ExperimentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFeatureGroupRequest

### FeatureGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureAdditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.FeatureDefinition]]

### OnlineStoreConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OnlineStoreConfigUpdate]

### ThroughputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ThroughputConfigUpdate]


# UpdateFeatureGroupResponse

### FeatureGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFeatureMetadataRequest

### FeatureGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ParameterAdditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.FeatureParameter]]

### ParameterRemovals
- **Type**: typing.Optional[typing.List[str]]


# UpdateHubContentReferenceRequest

### HubName
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentName
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentType
- **Type**: typing.Literal['Model', 'ModelReference', 'Notebook']
- **Required**: Yes

### MinVersion
- **Type**: typing.Optional[str]


# UpdateHubContentReferenceResponse

### HubArn
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateHubContentRequest

### HubName
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentName
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentType
- **Type**: typing.Literal['Model', 'ModelReference', 'Notebook']
- **Required**: Yes

### HubContentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentDisplayName
- **Type**: typing.Optional[str]

### HubContentDescription
- **Type**: typing.Optional[str]

### HubContentMarkdown
- **Type**: typing.Optional[str]

### HubContentSearchKeywords
- **Type**: typing.Optional[typing.List[str]]

### SupportStatus
- **Type**: typing.Optional[typing.Literal['Deprecated', 'Restricted', 'Supported']]


# UpdateHubContentResponse

### HubArn
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateHubRequest

### HubName
- **Type**: <class 'str'>
- **Required**: Yes

### HubDescription
- **Type**: typing.Optional[str]

### HubDisplayName
- **Type**: typing.Optional[str]

### HubSearchKeywords
- **Type**: typing.Optional[typing.List[str]]


# UpdateHubResponse

### HubArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateImageRequest

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### DeleteProperties
- **Type**: typing.Optional[typing.List[str]]

### Description
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]


# UpdateImageResponse

### ImageArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateImageVersionRequest

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### Alias
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[int]

### AliasesToAdd
- **Type**: typing.Optional[typing.List[str]]

### AliasesToDelete
- **Type**: typing.Optional[typing.List[str]]

### VendorGuidance
- **Type**: typing.Optional[typing.Literal['ARCHIVED', 'NOT_PROVIDED', 'STABLE', 'TO_BE_ARCHIVED']]

### JobType
- **Type**: typing.Optional[typing.Literal['INFERENCE', 'NOTEBOOK_KERNEL', 'TRAINING']]

### MLFramework
- **Type**: typing.Optional[str]

### ProgrammingLang
- **Type**: typing.Optional[str]

### Processor
- **Type**: typing.Optional[typing.Literal['CPU', 'GPU']]

### Horovod
- **Type**: typing.Optional[bool]

### ReleaseNotes
- **Type**: typing.Optional[str]


# UpdateImageVersionResponse

### ImageVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateInferenceComponentInput

### InferenceComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### Specification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceComponentSpecification]

### RuntimeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceComponentRuntimeConfig]

### DeploymentConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceComponentDeploymentConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceComponentDeploymentConfigOutput, NoneType]


# UpdateInferenceComponentOutput

### InferenceComponentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateInferenceComponentRuntimeConfigInput

### InferenceComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### DesiredRuntimeConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceComponentRuntimeConfig'>
- **Required**: Yes


# UpdateInferenceComponentRuntimeConfigOutput

### InferenceComponentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateInferenceExperimentRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Schedule
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceExperimentSchedule, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceExperimentScheduleOutput, NoneType]

### Description
- **Type**: typing.Optional[str]

### ModelVariants
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelVariantConfig]]

### DataStorageConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceExperimentDataStorageConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceExperimentDataStorageConfigOutput, NoneType]

### ShadowModeConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ShadowModeConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ShadowModeConfigOutput, NoneType]


# UpdateInferenceExperimentResponse

### InferenceExperimentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateMlflowTrackingServerRequest

### TrackingServerName
- **Type**: <class 'str'>
- **Required**: Yes

### ArtifactStoreUri
- **Type**: typing.Optional[str]

### TrackingServerSize
- **Type**: typing.Optional[typing.Literal['Large', 'Medium', 'Small']]

### AutomaticModelRegistration
- **Type**: typing.Optional[bool]

### WeeklyMaintenanceWindowStart
- **Type**: typing.Optional[str]


# UpdateMlflowTrackingServerResponse

### TrackingServerArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateModelCardRequest

### ModelCardName
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: typing.Optional[str]

### ModelCardStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'Archived', 'Draft', 'PendingReview']]


# UpdateModelCardResponse

### ModelCardArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateModelPackageInput

### ModelPackageArn
- **Type**: <class 'str'>
- **Required**: Yes

### ModelApprovalStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'PendingManualApproval', 'Rejected']]

### ApprovalDescription
- **Type**: typing.Optional[str]

### CustomerMetadataProperties
- **Type**: typing.Optional[typing.Dict[str, str]]

### CustomerMetadataPropertiesToRemove
- **Type**: typing.Optional[typing.List[str]]

### AdditionalInferenceSpecificationsToAdd
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AdditionalInferenceSpecificationDefinition, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.AdditionalInferenceSpecificationDefinitionOutput]]]

### InferenceSpecification
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceSpecification, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.InferenceSpecificationOutput, NoneType]

### SourceUri
- **Type**: typing.Optional[str]

### ModelCard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ModelPackageModelCard]

### ModelLifeCycle
- **Type**: <class 'NoneType'>

### ClientToken
- **Type**: typing.Optional[str]


# UpdateModelPackageOutput

### ModelPackageArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateMonitoringAlertRequest

### MonitoringScheduleName
- **Type**: <class 'str'>
- **Required**: Yes

### MonitoringAlertName
- **Type**: <class 'str'>
- **Required**: Yes

### DatapointsToAlert
- **Type**: <class 'int'>
- **Required**: Yes

### EvaluationPeriod
- **Type**: <class 'int'>
- **Required**: Yes


# UpdateMonitoringAlertResponse

### MonitoringScheduleArn
- **Type**: <class 'str'>
- **Required**: Yes

### MonitoringAlertName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateMonitoringScheduleRequest

### MonitoringScheduleName
- **Type**: <class 'str'>
- **Required**: Yes

### MonitoringScheduleConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringScheduleConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MonitoringScheduleConfigOutput]
- **Required**: Yes


# UpdateMonitoringScheduleResponse

### MonitoringScheduleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateNotebookInstanceInput

### NotebookInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c5d.18xlarge', 'ml.c5d.2xlarge', 'ml.c5d.4xlarge', 'ml.c5d.9xlarge', 'ml.c5d.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c6id.12xlarge', 'ml.c6id.16xlarge', 'ml.c6id.24xlarge', 'ml.c6id.2xlarge', 'ml.c6id.32xlarge', 'ml.c6id.4xlarge', 'ml.c6id.8xlarge', 'ml.c6id.large', 'ml.c6id.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.inf1.24xlarge', 'ml.inf1.2xlarge', 'ml.inf1.6xlarge', 'ml.inf1.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.16xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.8xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m6id.12xlarge', 'ml.m6id.16xlarge', 'ml.m6id.24xlarge', 'ml.m6id.2xlarge', 'ml.m6id.32xlarge', 'ml.m6id.4xlarge', 'ml.m6id.8xlarge', 'ml.m6id.large', 'ml.m6id.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r6id.12xlarge', 'ml.r6id.16xlarge', 'ml.r6id.24xlarge', 'ml.r6id.2xlarge', 'ml.r6id.32xlarge', 'ml.r6id.4xlarge', 'ml.r6id.8xlarge', 'ml.r6id.large', 'ml.r6id.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.t2.2xlarge', 'ml.t2.large', 'ml.t2.medium', 'ml.t2.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge']]

### RoleArn
- **Type**: typing.Optional[str]

### LifecycleConfigName
- **Type**: typing.Optional[str]

### DisassociateLifecycleConfig
- **Type**: typing.Optional[bool]

### VolumeSizeInGB
- **Type**: typing.Optional[int]

### DefaultCodeRepository
- **Type**: typing.Optional[str]

### AdditionalCodeRepositories
- **Type**: typing.Optional[typing.List[str]]

### AcceleratorTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ml.eia1.large', 'ml.eia1.medium', 'ml.eia1.xlarge', 'ml.eia2.large', 'ml.eia2.medium', 'ml.eia2.xlarge']]]

### DisassociateAcceleratorTypes
- **Type**: typing.Optional[bool]

### DisassociateDefaultCodeRepository
- **Type**: typing.Optional[bool]

### DisassociateAdditionalCodeRepositories
- **Type**: typing.Optional[bool]

### RootAccess
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### InstanceMetadataServiceConfiguration
- **Type**: <class 'NoneType'>


# UpdateNotebookInstanceLifecycleConfigInput

### NotebookInstanceLifecycleConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### OnCreate
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.NotebookInstanceLifecycleHook]]

### OnStart
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.NotebookInstanceLifecycleHook]]


# UpdatePartnerAppRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### MaintenanceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PartnerAppMaintenanceConfig]

### Tier
- **Type**: typing.Optional[str]

### ApplicationConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PartnerAppConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.PartnerAppConfigOutput, NoneType]

### EnableIamSessionBasedIdentity
- **Type**: typing.Optional[bool]

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# UpdatePartnerAppResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePipelineExecutionRequest

### PipelineExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineExecutionDescription
- **Type**: typing.Optional[str]

### PipelineExecutionDisplayName
- **Type**: typing.Optional[str]

### ParallelismConfiguration
- **Type**: <class 'NoneType'>


# UpdatePipelineExecutionResponse

### PipelineExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePipelineRequest

### PipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineDisplayName
- **Type**: typing.Optional[str]

### PipelineDefinition
- **Type**: typing.Optional[str]

### PipelineDefinitionS3Location
- **Type**: <class 'NoneType'>

### PipelineDescription
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### ParallelismConfiguration
- **Type**: <class 'NoneType'>


# UpdatePipelineResponse

### PipelineArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateProjectInput

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### ProjectDescription
- **Type**: typing.Optional[str]

### ServiceCatalogProvisioningUpdateDetails
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Tag]]


# UpdateProjectOutput

### ProjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSpaceRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### SpaceName
- **Type**: <class 'str'>
- **Required**: Yes

### SpaceSettings
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SpaceSettings, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SpaceSettingsOutput, NoneType]

### SpaceDisplayName
- **Type**: typing.Optional[str]


# UpdateSpaceResponse

### SpaceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTrainingJobRequest

### TrainingJobName
- **Type**: <class 'str'>
- **Required**: Yes

### ProfilerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProfilerConfigForUpdate]

### ProfilerRuleConfigurations
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProfilerRuleConfiguration, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ProfilerRuleConfigurationOutput]]]

### ResourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResourceConfigForUpdate]

### RemoteDebugConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.RemoteDebugConfigForUpdate]


# UpdateTrainingJobResponse

### TrainingJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTrialComponentRequest

### TrialComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrialComponentStatus]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrialComponentParameterValue]]

### ParametersToRemove
- **Type**: typing.Optional[typing.List[str]]

### InputArtifacts
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrialComponentArtifact]]

### InputArtifactsToRemove
- **Type**: typing.Optional[typing.List[str]]

### OutputArtifacts
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.TrialComponentArtifact]]

### OutputArtifactsToRemove
- **Type**: typing.Optional[typing.List[str]]


# UpdateTrialComponentResponse

### TrialComponentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTrialRequest

### TrialName
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]


# UpdateTrialResponse

### TrialArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateUserProfileRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### UserProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### UserSettings
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserSettings, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.UserSettingsOutput, NoneType]


# UpdateUserProfileResponse

### UserProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateWorkforceRequest

### WorkforceName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceIpConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SourceIpConfig, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SourceIpConfigOutput, NoneType]

### OidcConfig
- **Type**: <class 'NoneType'>

### WorkforceVpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.WorkforceVpcConfigRequest]


# UpdateWorkforceResponse

### Workforce
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Workforce'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateWorkteamRequest

### WorkteamName
- **Type**: <class 'str'>
- **Required**: Yes

### MemberDefinitions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MemberDefinition, aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MemberDefinitionOutput]]]

### Description
- **Type**: typing.Optional[str]

### NotificationConfiguration
- **Type**: <class 'NoneType'>

### WorkerAccessConfiguration
- **Type**: <class 'NoneType'>


# UpdateWorkteamResponse

### Workteam
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.Workteam'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.ResponseMetadata'>
- **Required**: Yes


# UserContext

### UserProfileArn
- **Type**: typing.Optional[str]

### UserProfileName
- **Type**: typing.Optional[str]

### DomainId
- **Type**: typing.Optional[str]

### IamIdentity
- **Type**: <class 'NoneType'>


# UserProfileDetails

### DomainId
- **Type**: typing.Optional[str]

### UserProfileName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Delete_Failed', 'Deleting', 'Failed', 'InService', 'Pending', 'Update_Failed', 'Updating']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# UserSettings

### ExecutionRole
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### SharingSettings
- **Type**: <class 'NoneType'>

### JupyterServerAppSettings
- **Type**: <class 'NoneType'>

### KernelGatewayAppSettings
- **Type**: <class 'NoneType'>

### TensorBoardAppSettings
- **Type**: <class 'NoneType'>

### RStudioServerProAppSettings
- **Type**: <class 'NoneType'>

### RSessionAppSettings
- **Type**: <class 'NoneType'>

### CanvasAppSettings
- **Type**: <class 'NoneType'>

### CodeEditorAppSettings
- **Type**: <class 'NoneType'>

### JupyterLabAppSettings
- **Type**: <class 'NoneType'>

### SpaceStorageSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DefaultSpaceStorageSettings]

### DefaultLandingUri
- **Type**: typing.Optional[str]

### StudioWebPortal
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### CustomPosixUserConfig
- **Type**: <class 'NoneType'>

### CustomFileSystemConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CustomFileSystemConfig]]

### StudioWebPortalSettings
- **Type**: <class 'NoneType'>

### AutoMountHomeEFS
- **Type**: typing.Optional[typing.Literal['DefaultAsDomain', 'Disabled', 'Enabled']]


# UserSettingsOutput

### ExecutionRole
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### SharingSettings
- **Type**: <class 'NoneType'>

### JupyterServerAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.JupyterServerAppSettingsOutput]

### KernelGatewayAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.KernelGatewayAppSettingsOutput]

### TensorBoardAppSettings
- **Type**: <class 'NoneType'>

### RStudioServerProAppSettings
- **Type**: <class 'NoneType'>

### RSessionAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.RSessionAppSettingsOutput]

### CanvasAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CanvasAppSettingsOutput]

### CodeEditorAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CodeEditorAppSettingsOutput]

### JupyterLabAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.JupyterLabAppSettingsOutput]

### SpaceStorageSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.DefaultSpaceStorageSettings]

### DefaultLandingUri
- **Type**: typing.Optional[str]

### StudioWebPortal
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### CustomPosixUserConfig
- **Type**: <class 'NoneType'>

### CustomFileSystemConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.CustomFileSystemConfig]]

### StudioWebPortalSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.StudioWebPortalSettingsOutput]

### AutoMountHomeEFS
- **Type**: typing.Optional[typing.Literal['DefaultAsDomain', 'Disabled', 'Enabled']]


# VariantProperty

### VariantPropertyType
- **Type**: typing.Literal['DataCaptureConfig', 'DesiredInstanceCount', 'DesiredWeight']
- **Required**: Yes


# VectorConfig

### Dimension
- **Type**: <class 'int'>
- **Required**: Yes


# Vertex

### Arn
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### LineageType
- **Type**: typing.Optional[typing.Literal['Action', 'Artifact', 'Context', 'TrialComponent']]


# VisibilityConditions

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# VpcConfig

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes


# VpcConfigOutput

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


# WarmPoolStatus

### Status
- **Type**: typing.Literal['Available', 'InUse', 'Reused', 'Terminated']
- **Required**: Yes

### ResourceRetainedBillableTimeInSeconds
- **Type**: typing.Optional[int]

### ReusedByJob
- **Type**: typing.Optional[str]


# WorkerAccessConfiguration

### S3Presign
- **Type**: <class 'NoneType'>


# Workforce

### WorkforceName
- **Type**: <class 'str'>
- **Required**: Yes

### WorkforceArn
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedDate
- **Type**: typing.Optional[datetime.datetime]

### SourceIpConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.SourceIpConfigOutput]

### SubDomain
- **Type**: typing.Optional[str]

### CognitoConfig
- **Type**: <class 'NoneType'>

### OidcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.OidcConfigForResponse]

### CreateDate
- **Type**: typing.Optional[datetime.datetime]

### WorkforceVpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.WorkforceVpcConfigResponse]

### Status
- **Type**: typing.Optional[typing.Literal['Active', 'Deleting', 'Failed', 'Initializing', 'Updating']]

### FailureReason
- **Type**: typing.Optional[str]


# WorkforceVpcConfigRequest

### VpcId
- **Type**: typing.Optional[str]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### Subnets
- **Type**: typing.Optional[typing.List[str]]


# WorkforceVpcConfigResponse

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes

### VpcEndpointId
- **Type**: typing.Optional[str]


# WorkspaceSettings

### S3ArtifactPath
- **Type**: typing.Optional[str]

### S3KmsKeyId
- **Type**: typing.Optional[str]


# Workteam

### WorkteamName
- **Type**: <class 'str'>
- **Required**: Yes

### MemberDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker.sagemaker_classes.MemberDefinitionOutput]
- **Required**: Yes

### WorkteamArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### WorkforceArn
- **Type**: typing.Optional[str]

### ProductListingIds
- **Type**: typing.Optional[typing.List[str]]

### SubDomain
- **Type**: typing.Optional[str]

### CreateDate
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedDate
- **Type**: typing.Optional[datetime.datetime]

### NotificationConfiguration
- **Type**: <class 'NoneType'>

### WorkerAccessConfiguration
- **Type**: <class 'NoneType'>


