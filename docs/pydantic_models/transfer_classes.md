# transfer_classes

# As2ConnectorConfigTypeDef

### LocalProfileId
- **Type**: typing.Optional[str]

### PartnerProfileId
- **Type**: typing.Optional[str]

### MessageSubject
- **Type**: typing.Optional[str]

### Compression
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ZLIB']]

### EncryptionAlgorithm
- **Type**: typing.Optional[typing.Literal['AES128_CBC', 'AES192_CBC', 'AES256_CBC', 'DES_EDE3_CBC', 'NONE']]

### SigningAlgorithm
- **Type**: typing.Optional[typing.Literal['NONE', 'SHA1', 'SHA256', 'SHA384', 'SHA512']]

### MdnSigningAlgorithm
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'NONE', 'SHA1', 'SHA256', 'SHA384', 'SHA512']]

### MdnResponse
- **Type**: typing.Optional[typing.Literal['NONE', 'SYNC']]

### BasicAuthSecretId
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CopyStepDetailsTypeDef

### Name
- **Type**: typing.Optional[str]

### DestinationFileLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.InputFileLocationTypeDef]

### OverwriteExisting
- **Type**: typing.Optional[typing.Literal['FALSE', 'TRUE']]

### SourceFileLocation
- **Type**: typing.Optional[str]


# CreateAccessRequestRequestTypeDef

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### ExternalId
- **Type**: <class 'str'>
- **Required**: Yes

### HomeDirectory
- **Type**: typing.Optional[str]

### HomeDirectoryType
- **Type**: typing.Optional[typing.Literal['LOGICAL', 'PATH']]

### HomeDirectoryMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.transfer_classes.HomeDirectoryMapEntryTypeDef]]

### Policy
- **Type**: typing.Optional[str]

### PosixProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.PosixProfileTypeDef]


# CreateAccessResponseTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### ExternalId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAgreementRequestRequestTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### LocalProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### PartnerProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### BaseDirectory
- **Type**: <class 'str'>
- **Required**: Yes

### AccessRole
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.transfer_classes.TagTypeDef]]


# CreateAgreementResponseTypeDef

### AgreementId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateConnectorRequestRequestTypeDef

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### AccessRole
- **Type**: <class 'str'>
- **Required**: Yes

### As2Config
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.As2ConnectorConfigTypeDef]

### LoggingRole
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.transfer_classes.TagTypeDef]]

### SftpConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.SftpConnectorConfigTypeDef]

### SecurityPolicyName
- **Type**: typing.Optional[str]


# CreateConnectorResponseTypeDef

### ConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProfileRequestRequestTypeDef

### As2Id
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileType
- **Type**: typing.Literal['LOCAL', 'PARTNER']
- **Required**: Yes

### CertificateIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.transfer_classes.TagTypeDef]]


# CreateProfileResponseTypeDef

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateServerRequestRequestTypeDef

### Certificate
- **Type**: typing.Optional[str]

### Domain
- **Type**: typing.Optional[typing.Literal['EFS', 'S3']]

### EndpointDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.EndpointDetailsTypeDef]

### EndpointType
- **Type**: typing.Optional[typing.Literal['PUBLIC', 'VPC', 'VPC_ENDPOINT']]

### HostKey
- **Type**: typing.Optional[str]

### IdentityProviderDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.IdentityProviderDetailsTypeDef]

### IdentityProviderType
- **Type**: typing.Optional[typing.Literal['API_GATEWAY', 'AWS_DIRECTORY_SERVICE', 'AWS_LAMBDA', 'SERVICE_MANAGED']]

### LoggingRole
- **Type**: typing.Optional[str]

### PostAuthenticationLoginBanner
- **Type**: typing.Optional[str]

### PreAuthenticationLoginBanner
- **Type**: typing.Optional[str]

### Protocols
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AS2', 'FTP', 'FTPS', 'SFTP']]]

### ProtocolDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.ProtocolDetailsTypeDef]

### SecurityPolicyName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.transfer_classes.TagTypeDef]]

### WorkflowDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.WorkflowDetailsTypeDef]

### StructuredLogDestinations
- **Type**: typing.Optional[typing.Sequence[str]]

### S3StorageOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.S3StorageOptionsTypeDef]


# CreateServerResponseTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUserRequestRequestTypeDef

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### HomeDirectory
- **Type**: typing.Optional[str]

### HomeDirectoryType
- **Type**: typing.Optional[typing.Literal['LOGICAL', 'PATH']]

### HomeDirectoryMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.transfer_classes.HomeDirectoryMapEntryTypeDef]]

### Policy
- **Type**: typing.Optional[str]

### PosixProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.PosixProfileTypeDef]

### SshPublicKeyBody
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.transfer_classes.TagTypeDef]]


# CreateUserResponseTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWorkflowRequestRequestTypeDef

### Steps
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.transfer_classes.WorkflowStepTypeDef, aws_resource_validator.pydantic_models.transfer_classes.WorkflowStepOutputTypeDef]]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### OnExceptionSteps
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.transfer_classes.WorkflowStepTypeDef, aws_resource_validator.pydantic_models.transfer_classes.WorkflowStepOutputTypeDef]]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.transfer_classes.TagTypeDef]]


# CreateWorkflowResponseTypeDef

### WorkflowId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomStepDetailsTypeDef

### Name
- **Type**: typing.Optional[str]

### Target
- **Type**: typing.Optional[str]

### TimeoutSeconds
- **Type**: typing.Optional[int]

### SourceFileLocation
- **Type**: typing.Optional[str]


# DecryptStepDetailsTypeDef

### Type
- **Type**: typing.Literal['PGP']
- **Required**: Yes

### DestinationFileLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.InputFileLocationTypeDef'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### SourceFileLocation
- **Type**: typing.Optional[str]

### OverwriteExisting
- **Type**: typing.Optional[typing.Literal['FALSE', 'TRUE']]


# DeleteAccessRequestRequestTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### ExternalId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAgreementRequestRequestTypeDef

### AgreementId
- **Type**: <class 'str'>
- **Required**: Yes

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCertificateRequestRequestTypeDef

### CertificateId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConnectorRequestRequestTypeDef

### ConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHostKeyRequestRequestTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### HostKeyId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProfileRequestRequestTypeDef

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServerRequestRequestTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSshPublicKeyRequestRequestTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### SshPublicKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStepDetailsTypeDef

### Name
- **Type**: typing.Optional[str]

### SourceFileLocation
- **Type**: typing.Optional[str]


# DeleteUserRequestRequestTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkflowRequestRequestTypeDef

### WorkflowId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccessRequestRequestTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### ExternalId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccessResponseTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### Access
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.DescribedAccessTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAgreementRequestRequestTypeDef

### AgreementId
- **Type**: <class 'str'>
- **Required**: Yes

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAgreementResponseTypeDef

### Agreement
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.DescribedAgreementTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCertificateRequestRequestTypeDef

### CertificateId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCertificateResponseTypeDef

### Certificate
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.DescribedCertificateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeConnectorRequestRequestTypeDef

### ConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeConnectorResponseTypeDef

### Connector
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.DescribedConnectorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeExecutionRequestRequestTypeDef

### ExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkflowId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeExecutionResponseTypeDef

### WorkflowId
- **Type**: <class 'str'>
- **Required**: Yes

### Execution
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.DescribedExecutionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeHostKeyRequestRequestTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### HostKeyId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeHostKeyResponseTypeDef

### HostKey
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.DescribedHostKeyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeProfileRequestRequestTypeDef

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeProfileResponseTypeDef

### Profile
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.DescribedProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSecurityPolicyRequestRequestTypeDef

### SecurityPolicyName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSecurityPolicyResponseTypeDef

### SecurityPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.DescribedSecurityPolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeServerRequestRequestTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeServerRequestServerOfflineWaitTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.WaiterConfigTypeDef]


# DescribeServerRequestServerOnlineWaitTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.WaiterConfigTypeDef]


# DescribeServerResponseTypeDef

### Server
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.DescribedServerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeUserRequestRequestTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeUserResponseTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.DescribedUserTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeWorkflowRequestRequestTypeDef

### WorkflowId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWorkflowResponseTypeDef

### Workflow
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.DescribedWorkflowTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribedAccessTypeDef

### HomeDirectory
- **Type**: typing.Optional[str]

### HomeDirectoryMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer_classes.HomeDirectoryMapEntryTypeDef]]

### HomeDirectoryType
- **Type**: typing.Optional[typing.Literal['LOGICAL', 'PATH']]

### Policy
- **Type**: typing.Optional[str]

### PosixProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.PosixProfileOutputTypeDef]

### Role
- **Type**: typing.Optional[str]

### ExternalId
- **Type**: typing.Optional[str]


# DescribedAgreementTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AgreementId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### ServerId
- **Type**: typing.Optional[str]

### LocalProfileId
- **Type**: typing.Optional[str]

### PartnerProfileId
- **Type**: typing.Optional[str]

### BaseDirectory
- **Type**: typing.Optional[str]

### AccessRole
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer_classes.TagTypeDef]]


# DescribedCertificateTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateId
- **Type**: typing.Optional[str]

### Usage
- **Type**: typing.Optional[typing.Literal['ENCRYPTION', 'SIGNING', 'TLS']]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE', 'PENDING_ROTATION']]

### Certificate
- **Type**: typing.Optional[str]

### CertificateChain
- **Type**: typing.Optional[str]

### ActiveDate
- **Type**: typing.Optional[datetime.datetime]

### InactiveDate
- **Type**: typing.Optional[datetime.datetime]

### Serial
- **Type**: typing.Optional[str]

### NotBeforeDate
- **Type**: typing.Optional[datetime.datetime]

### NotAfterDate
- **Type**: typing.Optional[datetime.datetime]

### Type
- **Type**: typing.Optional[typing.Literal['CERTIFICATE', 'CERTIFICATE_WITH_PRIVATE_KEY']]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer_classes.TagTypeDef]]


# DescribedConnectorTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectorId
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]

### As2Config
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.As2ConnectorConfigTypeDef]

### AccessRole
- **Type**: typing.Optional[str]

### LoggingRole
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer_classes.TagTypeDef]]

### SftpConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.SftpConnectorConfigOutputTypeDef]

### ServiceManagedEgressIpAddresses
- **Type**: typing.Optional[typing.List[str]]

### SecurityPolicyName
- **Type**: typing.Optional[str]


# DescribedExecutionTypeDef

### ExecutionId
- **Type**: typing.Optional[str]

### InitialFileLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.FileLocationTypeDef]

### ServiceMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.ServiceMetadataTypeDef]

### ExecutionRole
- **Type**: typing.Optional[str]

### LoggingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.LoggingConfigurationTypeDef]

### PosixProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.PosixProfileOutputTypeDef]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'EXCEPTION', 'HANDLING_EXCEPTION', 'IN_PROGRESS']]

### Results
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.ExecutionResultsTypeDef]


# DescribedHostKeyTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### HostKeyId
- **Type**: typing.Optional[str]

### HostKeyFingerprint
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### DateImported
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer_classes.TagTypeDef]]


# DescribedProfileTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileId
- **Type**: typing.Optional[str]

### ProfileType
- **Type**: typing.Optional[typing.Literal['LOCAL', 'PARTNER']]

### As2Id
- **Type**: typing.Optional[str]

### CertificateIds
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer_classes.TagTypeDef]]


# DescribedSecurityPolicyTypeDef

### SecurityPolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### Fips
- **Type**: typing.Optional[bool]

### SshCiphers
- **Type**: typing.Optional[typing.List[str]]

### SshKexs
- **Type**: typing.Optional[typing.List[str]]

### SshMacs
- **Type**: typing.Optional[typing.List[str]]

### TlsCiphers
- **Type**: typing.Optional[typing.List[str]]

### SshHostKeyAlgorithms
- **Type**: typing.Optional[typing.List[str]]

### Type
- **Type**: typing.Optional[typing.Literal['CONNECTOR', 'SERVER']]

### Protocols
- **Type**: typing.Optional[typing.List[typing.Literal['FTPS', 'SFTP']]]


# DescribedServerTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Certificate
- **Type**: typing.Optional[str]

### ProtocolDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.ProtocolDetailsOutputTypeDef]

### Domain
- **Type**: typing.Optional[typing.Literal['EFS', 'S3']]

### EndpointDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.EndpointDetailsOutputTypeDef]

### EndpointType
- **Type**: typing.Optional[typing.Literal['PUBLIC', 'VPC', 'VPC_ENDPOINT']]

### HostKeyFingerprint
- **Type**: typing.Optional[str]

### IdentityProviderDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.IdentityProviderDetailsTypeDef]

### IdentityProviderType
- **Type**: typing.Optional[typing.Literal['API_GATEWAY', 'AWS_DIRECTORY_SERVICE', 'AWS_LAMBDA', 'SERVICE_MANAGED']]

### LoggingRole
- **Type**: typing.Optional[str]

### PostAuthenticationLoginBanner
- **Type**: typing.Optional[str]

### PreAuthenticationLoginBanner
- **Type**: typing.Optional[str]

### Protocols
- **Type**: typing.Optional[typing.List[typing.Literal['AS2', 'FTP', 'FTPS', 'SFTP']]]

### SecurityPolicyName
- **Type**: typing.Optional[str]

### ServerId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['OFFLINE', 'ONLINE', 'STARTING', 'START_FAILED', 'STOPPING', 'STOP_FAILED']]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer_classes.TagTypeDef]]

### UserCount
- **Type**: typing.Optional[int]

### WorkflowDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.WorkflowDetailsOutputTypeDef]

### StructuredLogDestinations
- **Type**: typing.Optional[typing.List[str]]

### S3StorageOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.S3StorageOptionsTypeDef]

### As2ServiceManagedEgressIpAddresses
- **Type**: typing.Optional[typing.List[str]]


# DescribedUserTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### HomeDirectory
- **Type**: typing.Optional[str]

### HomeDirectoryMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer_classes.HomeDirectoryMapEntryTypeDef]]

### HomeDirectoryType
- **Type**: typing.Optional[typing.Literal['LOGICAL', 'PATH']]

### Policy
- **Type**: typing.Optional[str]

### PosixProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.PosixProfileOutputTypeDef]

### Role
- **Type**: typing.Optional[str]

### SshPublicKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer_classes.SshPublicKeyTypeDef]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer_classes.TagTypeDef]]

### UserName
- **Type**: typing.Optional[str]


# DescribedWorkflowTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Steps
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer_classes.WorkflowStepOutputTypeDef]]

### OnExceptionSteps
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer_classes.WorkflowStepOutputTypeDef]]

### WorkflowId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer_classes.TagTypeDef]]


# EfsFileLocationTypeDef

### FileSystemId
- **Type**: typing.Optional[str]

### Path
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EndpointDetailsOutputTypeDef

### AddressAllocationIds
- **Type**: typing.Optional[typing.List[str]]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### VpcEndpointId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# EndpointDetailsTypeDef

### AddressAllocationIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SubnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### VpcEndpointId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]


# ExecutionErrorTypeDef

### Type
- **Type**: typing.Literal['ALREADY_EXISTS', 'BAD_REQUEST', 'CUSTOM_STEP_FAILED', 'INTERNAL_SERVER_ERROR', 'NOT_FOUND', 'PERMISSION_DENIED', 'THROTTLED', 'TIMEOUT']
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes


# ExecutionResultsTypeDef

### Steps
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer_classes.ExecutionStepResultTypeDef]]

### OnExceptionSteps
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer_classes.ExecutionStepResultTypeDef]]


# ExecutionStepResultTypeDef

### StepType
- **Type**: typing.Optional[typing.Literal['COPY', 'CUSTOM', 'DECRYPT', 'DELETE', 'TAG']]

### Outputs
- **Type**: typing.Optional[str]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.ExecutionErrorTypeDef]


# FileLocationTypeDef

### S3FileLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.S3FileLocationTypeDef]

### EfsFileLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.EfsFileLocationTypeDef]


# HomeDirectoryMapEntryTypeDef

### Entry
- **Type**: <class 'str'>
- **Required**: Yes

### Target
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Optional[typing.Literal['DIRECTORY', 'FILE']]


# IdentityProviderDetailsTypeDef

### Url
- **Type**: typing.Optional[str]

### InvocationRole
- **Type**: typing.Optional[str]

### DirectoryId
- **Type**: typing.Optional[str]

### Function
- **Type**: typing.Optional[str]

### SftpAuthenticationMethods
- **Type**: typing.Optional[typing.Literal['PASSWORD', 'PUBLIC_KEY', 'PUBLIC_KEY_AND_PASSWORD', 'PUBLIC_KEY_OR_PASSWORD']]


# ImportCertificateRequestRequestTypeDef

### Usage
- **Type**: typing.Literal['ENCRYPTION', 'SIGNING', 'TLS']
- **Required**: Yes

### Certificate
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateChain
- **Type**: typing.Optional[str]

### PrivateKey
- **Type**: typing.Optional[str]

### ActiveDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### InactiveDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.transfer_classes.TagTypeDef]]


# ImportCertificateResponseTypeDef

### CertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImportHostKeyRequestRequestTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### HostKeyBody
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.transfer_classes.TagTypeDef]]


# ImportHostKeyResponseTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### HostKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImportSshPublicKeyRequestRequestTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### SshPublicKeyBody
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes


# ImportSshPublicKeyResponseTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### SshPublicKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InputFileLocationTypeDef

### S3FileLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.S3InputFileLocationTypeDef]

### EfsFileLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.EfsFileLocationTypeDef]


# ListAccessesRequestListAccessesPaginateTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.PaginatorConfigTypeDef]


# ListAccessesRequestRequestTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAccessesResponseTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### Accesses
- **Type**: typing.List[aws_resource_validator.pydantic_models.transfer_classes.ListedAccessTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAgreementsRequestListAgreementsPaginateTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.PaginatorConfigTypeDef]


# ListAgreementsRequestRequestTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAgreementsResponseTypeDef

### Agreements
- **Type**: typing.List[aws_resource_validator.pydantic_models.transfer_classes.ListedAgreementTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCertificatesRequestListCertificatesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.PaginatorConfigTypeDef]


# ListCertificatesRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCertificatesResponseTypeDef

### Certificates
- **Type**: typing.List[aws_resource_validator.pydantic_models.transfer_classes.ListedCertificateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConnectorsRequestListConnectorsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.PaginatorConfigTypeDef]


# ListConnectorsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListConnectorsResponseTypeDef

### Connectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.transfer_classes.ListedConnectorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListExecutionsRequestListExecutionsPaginateTypeDef

### WorkflowId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.PaginatorConfigTypeDef]


# ListExecutionsRequestRequestTypeDef

### WorkflowId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListExecutionsResponseTypeDef

### WorkflowId
- **Type**: <class 'str'>
- **Required**: Yes

### Executions
- **Type**: typing.List[aws_resource_validator.pydantic_models.transfer_classes.ListedExecutionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHostKeysRequestRequestTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListHostKeysResponseTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### HostKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.transfer_classes.ListedHostKeyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProfilesRequestListProfilesPaginateTypeDef

### ProfileType
- **Type**: typing.Optional[typing.Literal['LOCAL', 'PARTNER']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.PaginatorConfigTypeDef]


# ListProfilesRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ProfileType
- **Type**: typing.Optional[typing.Literal['LOCAL', 'PARTNER']]


# ListProfilesResponseTypeDef

### Profiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.transfer_classes.ListedProfileTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSecurityPoliciesRequestListSecurityPoliciesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.PaginatorConfigTypeDef]


# ListSecurityPoliciesRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSecurityPoliciesResponseTypeDef

### SecurityPolicyNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListServersRequestListServersPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.PaginatorConfigTypeDef]


# ListServersRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListServersResponseTypeDef

### Servers
- **Type**: typing.List[aws_resource_validator.pydantic_models.transfer_classes.ListedServerTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestListTagsForResourcePaginateTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.PaginatorConfigTypeDef]


# ListTagsForResourceRequestRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.transfer_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListUsersRequestListUsersPaginateTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.PaginatorConfigTypeDef]


# ListUsersRequestRequestTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListUsersResponseTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### Users
- **Type**: typing.List[aws_resource_validator.pydantic_models.transfer_classes.ListedUserTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListWorkflowsRequestListWorkflowsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.PaginatorConfigTypeDef]


# ListWorkflowsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListWorkflowsResponseTypeDef

### Workflows
- **Type**: typing.List[aws_resource_validator.pydantic_models.transfer_classes.ListedWorkflowTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListedAccessTypeDef

### HomeDirectory
- **Type**: typing.Optional[str]

### HomeDirectoryType
- **Type**: typing.Optional[typing.Literal['LOGICAL', 'PATH']]

### Role
- **Type**: typing.Optional[str]

### ExternalId
- **Type**: typing.Optional[str]


# ListedAgreementTypeDef

### Arn
- **Type**: typing.Optional[str]

### AgreementId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### ServerId
- **Type**: typing.Optional[str]

### LocalProfileId
- **Type**: typing.Optional[str]

### PartnerProfileId
- **Type**: typing.Optional[str]


# ListedCertificateTypeDef

### Arn
- **Type**: typing.Optional[str]

### CertificateId
- **Type**: typing.Optional[str]

### Usage
- **Type**: typing.Optional[typing.Literal['ENCRYPTION', 'SIGNING', 'TLS']]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE', 'PENDING_ROTATION']]

### ActiveDate
- **Type**: typing.Optional[datetime.datetime]

### InactiveDate
- **Type**: typing.Optional[datetime.datetime]

### Type
- **Type**: typing.Optional[typing.Literal['CERTIFICATE', 'CERTIFICATE_WITH_PRIVATE_KEY']]

### Description
- **Type**: typing.Optional[str]


# ListedConnectorTypeDef

### Arn
- **Type**: typing.Optional[str]

### ConnectorId
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# ListedExecutionTypeDef

### ExecutionId
- **Type**: typing.Optional[str]

### InitialFileLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.FileLocationTypeDef]

### ServiceMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.ServiceMetadataTypeDef]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'EXCEPTION', 'HANDLING_EXCEPTION', 'IN_PROGRESS']]


# ListedHostKeyTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### HostKeyId
- **Type**: typing.Optional[str]

### Fingerprint
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### DateImported
- **Type**: typing.Optional[datetime.datetime]


# ListedProfileTypeDef

### Arn
- **Type**: typing.Optional[str]

### ProfileId
- **Type**: typing.Optional[str]

### As2Id
- **Type**: typing.Optional[str]

### ProfileType
- **Type**: typing.Optional[typing.Literal['LOCAL', 'PARTNER']]


# ListedServerTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: typing.Optional[typing.Literal['EFS', 'S3']]

### IdentityProviderType
- **Type**: typing.Optional[typing.Literal['API_GATEWAY', 'AWS_DIRECTORY_SERVICE', 'AWS_LAMBDA', 'SERVICE_MANAGED']]

### EndpointType
- **Type**: typing.Optional[typing.Literal['PUBLIC', 'VPC', 'VPC_ENDPOINT']]

### LoggingRole
- **Type**: typing.Optional[str]

### ServerId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['OFFLINE', 'ONLINE', 'STARTING', 'START_FAILED', 'STOPPING', 'STOP_FAILED']]

### UserCount
- **Type**: typing.Optional[int]


# ListedUserTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### HomeDirectory
- **Type**: typing.Optional[str]

### HomeDirectoryType
- **Type**: typing.Optional[typing.Literal['LOGICAL', 'PATH']]

### Role
- **Type**: typing.Optional[str]

### SshPublicKeyCount
- **Type**: typing.Optional[int]

### UserName
- **Type**: typing.Optional[str]


# ListedWorkflowTypeDef

### WorkflowId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]


# LoggingConfigurationTypeDef

### LoggingRole
- **Type**: typing.Optional[str]

### LogGroupName
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PosixProfileOutputTypeDef

### Uid
- **Type**: <class 'int'>
- **Required**: Yes

### Gid
- **Type**: <class 'int'>
- **Required**: Yes

### SecondaryGids
- **Type**: typing.Optional[typing.List[int]]


# PosixProfileTypeDef

### Uid
- **Type**: <class 'int'>
- **Required**: Yes

### Gid
- **Type**: <class 'int'>
- **Required**: Yes

### SecondaryGids
- **Type**: typing.Optional[typing.Sequence[int]]


# ProtocolDetailsOutputTypeDef

### PassiveIp
- **Type**: typing.Optional[str]

### TlsSessionResumptionMode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'ENFORCED']]

### SetStatOption
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'ENABLE_NO_OP']]

### As2Transports
- **Type**: typing.Optional[typing.List[typing.Literal['HTTP']]]


# ProtocolDetailsTypeDef

### PassiveIp
- **Type**: typing.Optional[str]

### TlsSessionResumptionMode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'ENFORCED']]

### SetStatOption
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'ENABLE_NO_OP']]

### As2Transports
- **Type**: typing.Optional[typing.Sequence[typing.Literal['HTTP']]]


# ResponseMetadataTypeDef

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


# S3FileLocationTypeDef

### Bucket
- **Type**: typing.Optional[str]

### Key
- **Type**: typing.Optional[str]

### VersionId
- **Type**: typing.Optional[str]

### Etag
- **Type**: typing.Optional[str]


# S3InputFileLocationTypeDef

### Bucket
- **Type**: typing.Optional[str]

### Key
- **Type**: typing.Optional[str]


# S3StorageOptionsTypeDef

### DirectoryListingOptimization
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# S3TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# SendWorkflowStepStateRequestRequestTypeDef

### WorkflowId
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### Token
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILURE', 'SUCCESS']
- **Required**: Yes


# ServiceMetadataTypeDef

### UserDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.UserDetailsTypeDef'>
- **Required**: Yes


# SftpConnectorConfigOutputTypeDef

### UserSecretId
- **Type**: typing.Optional[str]

### TrustedHostKeys
- **Type**: typing.Optional[typing.List[str]]


# SftpConnectorConfigTypeDef

### UserSecretId
- **Type**: typing.Optional[str]

### TrustedHostKeys
- **Type**: typing.Optional[typing.Sequence[str]]


# SshPublicKeyTypeDef

### DateImported
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SshPublicKeyBody
- **Type**: <class 'str'>
- **Required**: Yes

### SshPublicKeyId
- **Type**: <class 'str'>
- **Required**: Yes


# StartDirectoryListingRequestRequestTypeDef

### ConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### RemoteDirectoryPath
- **Type**: <class 'str'>
- **Required**: Yes

### OutputDirectoryPath
- **Type**: <class 'str'>
- **Required**: Yes

### MaxItems
- **Type**: typing.Optional[int]


# StartDirectoryListingResponseTypeDef

### ListingId
- **Type**: <class 'str'>
- **Required**: Yes

### OutputFileName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartFileTransferRequestRequestTypeDef

### ConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### SendFilePaths
- **Type**: typing.Optional[typing.Sequence[str]]

### RetrieveFilePaths
- **Type**: typing.Optional[typing.Sequence[str]]

### LocalDirectoryPath
- **Type**: typing.Optional[str]

### RemoteDirectoryPath
- **Type**: typing.Optional[str]


# StartFileTransferResponseTypeDef

### TransferId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartServerRequestRequestTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes


# StopServerRequestRequestTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.transfer_classes.TagTypeDef]
- **Required**: Yes


# TagStepDetailsOutputTypeDef

### Name
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer_classes.S3TagTypeDef]]

### SourceFileLocation
- **Type**: typing.Optional[str]


# TagStepDetailsTypeDef

### Name
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.transfer_classes.S3TagTypeDef]]

### SourceFileLocation
- **Type**: typing.Optional[str]


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TestConnectionRequestRequestTypeDef

### ConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# TestConnectionResponseTypeDef

### ConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TestIdentityProviderRequestRequestTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### ServerProtocol
- **Type**: typing.Optional[typing.Literal['AS2', 'FTP', 'FTPS', 'SFTP']]

### SourceIp
- **Type**: typing.Optional[str]

### UserPassword
- **Type**: typing.Optional[str]


# TestIdentityProviderResponseTypeDef

### Response
- **Type**: <class 'str'>
- **Required**: Yes

### StatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAccessRequestRequestTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### ExternalId
- **Type**: <class 'str'>
- **Required**: Yes

### HomeDirectory
- **Type**: typing.Optional[str]

### HomeDirectoryType
- **Type**: typing.Optional[typing.Literal['LOGICAL', 'PATH']]

### HomeDirectoryMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.transfer_classes.HomeDirectoryMapEntryTypeDef]]

### Policy
- **Type**: typing.Optional[str]

### PosixProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.PosixProfileTypeDef]

### Role
- **Type**: typing.Optional[str]


# UpdateAccessResponseTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### ExternalId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAgreementRequestRequestTypeDef

### AgreementId
- **Type**: <class 'str'>
- **Required**: Yes

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### LocalProfileId
- **Type**: typing.Optional[str]

### PartnerProfileId
- **Type**: typing.Optional[str]

### BaseDirectory
- **Type**: typing.Optional[str]

### AccessRole
- **Type**: typing.Optional[str]


# UpdateAgreementResponseTypeDef

### AgreementId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateCertificateRequestRequestTypeDef

### CertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### ActiveDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### InactiveDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Description
- **Type**: typing.Optional[str]


# UpdateCertificateResponseTypeDef

### CertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateConnectorRequestRequestTypeDef

### ConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Url
- **Type**: typing.Optional[str]

### As2Config
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.As2ConnectorConfigTypeDef]

### AccessRole
- **Type**: typing.Optional[str]

### LoggingRole
- **Type**: typing.Optional[str]

### SftpConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.SftpConnectorConfigTypeDef]

### SecurityPolicyName
- **Type**: typing.Optional[str]


# UpdateConnectorResponseTypeDef

### ConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateHostKeyRequestRequestTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### HostKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateHostKeyResponseTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### HostKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateProfileRequestRequestTypeDef

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateIds
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateProfileResponseTypeDef

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateServerRequestRequestTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### Certificate
- **Type**: typing.Optional[str]

### ProtocolDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.ProtocolDetailsTypeDef]

### EndpointDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.EndpointDetailsTypeDef]

### EndpointType
- **Type**: typing.Optional[typing.Literal['PUBLIC', 'VPC', 'VPC_ENDPOINT']]

### HostKey
- **Type**: typing.Optional[str]

### IdentityProviderDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.IdentityProviderDetailsTypeDef]

### LoggingRole
- **Type**: typing.Optional[str]

### PostAuthenticationLoginBanner
- **Type**: typing.Optional[str]

### PreAuthenticationLoginBanner
- **Type**: typing.Optional[str]

### Protocols
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AS2', 'FTP', 'FTPS', 'SFTP']]]

### SecurityPolicyName
- **Type**: typing.Optional[str]

### WorkflowDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.WorkflowDetailsTypeDef]

### StructuredLogDestinations
- **Type**: typing.Optional[typing.Sequence[str]]

### S3StorageOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.S3StorageOptionsTypeDef]


# UpdateServerResponseTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateUserRequestRequestTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### HomeDirectory
- **Type**: typing.Optional[str]

### HomeDirectoryType
- **Type**: typing.Optional[typing.Literal['LOGICAL', 'PATH']]

### HomeDirectoryMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.transfer_classes.HomeDirectoryMapEntryTypeDef]]

### Policy
- **Type**: typing.Optional[str]

### PosixProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.PosixProfileTypeDef]

### Role
- **Type**: typing.Optional[str]


# UpdateUserResponseTypeDef

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UserDetailsTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### SessionId
- **Type**: typing.Optional[str]


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


# WorkflowDetailTypeDef

### WorkflowId
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionRole
- **Type**: <class 'str'>
- **Required**: Yes


# WorkflowDetailsOutputTypeDef

### OnUpload
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer_classes.WorkflowDetailTypeDef]]

### OnPartialUpload
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer_classes.WorkflowDetailTypeDef]]


# WorkflowDetailsTypeDef

### OnUpload
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.transfer_classes.WorkflowDetailTypeDef]]

### OnPartialUpload
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.transfer_classes.WorkflowDetailTypeDef]]


# WorkflowStepOutputTypeDef

### Type
- **Type**: typing.Optional[typing.Literal['COPY', 'CUSTOM', 'DECRYPT', 'DELETE', 'TAG']]

### CopyStepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.CopyStepDetailsTypeDef]

### CustomStepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.CustomStepDetailsTypeDef]

### DeleteStepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.DeleteStepDetailsTypeDef]

### TagStepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.TagStepDetailsOutputTypeDef]

### DecryptStepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.DecryptStepDetailsTypeDef]


# WorkflowStepTypeDef

### Type
- **Type**: typing.Optional[typing.Literal['COPY', 'CUSTOM', 'DECRYPT', 'DELETE', 'TAG']]

### CopyStepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.CopyStepDetailsTypeDef]

### CustomStepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.CustomStepDetailsTypeDef]

### DeleteStepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.DeleteStepDetailsTypeDef]

### TagStepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.TagStepDetailsTypeDef]

### DecryptStepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer_classes.DecryptStepDetailsTypeDef]


