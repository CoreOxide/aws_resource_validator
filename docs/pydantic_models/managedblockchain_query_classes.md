# Managedblockchain Query Classes

# AddressIdentifierFilterTypeDef

### transactionEventToAddress
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AssetContractTypeDef

### contractIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.ContractIdentifierTypeDef'>
- **Required**: Yes

### tokenStandard
- **Type**: typing.Literal['ERC1155', 'ERC20', 'ERC721']
- **Required**: Yes

### deployerAddress
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetTokenBalanceErrorItemTypeDef

### errorCode
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### errorType
- **Type**: typing.Literal['RESOURCE_NOT_FOUND_EXCEPTION', 'VALIDATION_EXCEPTION']
- **Required**: Yes

### tokenIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.TokenIdentifierTypeDef]

### ownerIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.OwnerIdentifierTypeDef]

### atBlockchainInstant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.BlockchainInstantOutputTypeDef]


# BatchGetTokenBalanceInputItemTypeDef

### tokenIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.TokenIdentifierTypeDef'>
- **Required**: Yes

### ownerIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.OwnerIdentifierTypeDef'>
- **Required**: Yes

### atBlockchainInstant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.BlockchainInstantUnionTypeDef]


# BatchGetTokenBalanceInputTypeDef

### getTokenBalanceInputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.managedblockchain_query_classes.BatchGetTokenBalanceInputItemTypeDef]]


# BatchGetTokenBalanceOutputItemTypeDef

### balance
- **Type**: <class 'str'>
- **Required**: Yes

### atBlockchainInstant
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.BlockchainInstantOutputTypeDef'>
- **Required**: Yes

### ownerIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.OwnerIdentifierTypeDef]

### tokenIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.TokenIdentifierTypeDef]

### lastUpdatedTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.BlockchainInstantOutputTypeDef]


# BatchGetTokenBalanceOutputTypeDef

### tokenBalances
- **Type**: typing.List[aws_resource_validator.pydantic_models.managedblockchain_query_classes.BatchGetTokenBalanceOutputItemTypeDef]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.managedblockchain_query_classes.BatchGetTokenBalanceErrorItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BlockchainInstantOutputTypeDef

### time
- **Type**: typing.Optional[datetime.datetime]


# BlockchainInstantTypeDef

### time
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.TimestampTypeDef]


# BlockchainInstantUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfirmationStatusFilterTypeDef

### include
- **Type**: typing.Sequence[typing.Literal['FINAL', 'NONFINAL']]
- **Required**: Yes


# ContractFilterTypeDef

### network
- **Type**: typing.Literal['BITCOIN_MAINNET', 'BITCOIN_TESTNET', 'ETHEREUM_MAINNET', 'ETHEREUM_SEPOLIA_TESTNET']
- **Required**: Yes

### tokenStandard
- **Type**: typing.Literal['ERC1155', 'ERC20', 'ERC721']
- **Required**: Yes

### deployerAddress
- **Type**: <class 'str'>
- **Required**: Yes


# ContractIdentifierTypeDef

### network
- **Type**: typing.Literal['BITCOIN_MAINNET', 'BITCOIN_TESTNET', 'ETHEREUM_MAINNET', 'ETHEREUM_SEPOLIA_TESTNET']
- **Required**: Yes

### contractAddress
- **Type**: <class 'str'>
- **Required**: Yes


# ContractMetadataTypeDef

### name
- **Type**: typing.Optional[str]

### symbol
- **Type**: typing.Optional[str]

### decimals
- **Type**: typing.Optional[int]


# GetAssetContractInputTypeDef

### contractIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.ContractIdentifierTypeDef'>
- **Required**: Yes


# GetAssetContractOutputTypeDef

### contractIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.ContractIdentifierTypeDef'>
- **Required**: Yes

### tokenStandard
- **Type**: typing.Literal['ERC1155', 'ERC20', 'ERC721']
- **Required**: Yes

### deployerAddress
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.ContractMetadataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTokenBalanceInputTypeDef

### tokenIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.TokenIdentifierTypeDef'>
- **Required**: Yes

### ownerIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.OwnerIdentifierTypeDef'>
- **Required**: Yes

### atBlockchainInstant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.BlockchainInstantUnionTypeDef]


# GetTokenBalanceOutputTypeDef

### ownerIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.OwnerIdentifierTypeDef'>
- **Required**: Yes

### tokenIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.TokenIdentifierTypeDef'>
- **Required**: Yes

### balance
- **Type**: <class 'str'>
- **Required**: Yes

### atBlockchainInstant
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.BlockchainInstantOutputTypeDef'>
- **Required**: Yes

### lastUpdatedTime
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.BlockchainInstantOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTransactionInputTypeDef

### network
- **Type**: typing.Literal['BITCOIN_MAINNET', 'BITCOIN_TESTNET', 'ETHEREUM_MAINNET', 'ETHEREUM_SEPOLIA_TESTNET']
- **Required**: Yes

### transactionHash
- **Type**: typing.Optional[str]

### transactionId
- **Type**: typing.Optional[str]


# GetTransactionOutputTypeDef

### transaction
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.TransactionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAssetContractsInputPaginateTypeDef

### contractFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.ContractFilterTypeDef'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.PaginatorConfigTypeDef]


# ListAssetContractsInputTypeDef

### contractFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.ContractFilterTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAssetContractsOutputTypeDef

### contracts
- **Type**: typing.List[aws_resource_validator.pydantic_models.managedblockchain_query_classes.AssetContractTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFilteredTransactionEventsInputPaginateTypeDef

### network
- **Type**: <class 'str'>
- **Required**: Yes

### addressIdentifierFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.AddressIdentifierFilterTypeDef'>
- **Required**: Yes

### timeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.TimeFilterTypeDef]

### voutFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.VoutFilterTypeDef]

### confirmationStatusFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.ConfirmationStatusFilterTypeDef]

### sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.ListFilteredTransactionEventsSortTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.PaginatorConfigTypeDef]


# ListFilteredTransactionEventsInputTypeDef

### network
- **Type**: <class 'str'>
- **Required**: Yes

### addressIdentifierFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.AddressIdentifierFilterTypeDef'>
- **Required**: Yes

### timeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.TimeFilterTypeDef]

### voutFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.VoutFilterTypeDef]

### confirmationStatusFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.ConfirmationStatusFilterTypeDef]

### sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.ListFilteredTransactionEventsSortTypeDef]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListFilteredTransactionEventsOutputTypeDef

### events
- **Type**: typing.List[aws_resource_validator.pydantic_models.managedblockchain_query_classes.TransactionEventTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFilteredTransactionEventsSortTypeDef

### sortBy
- **Type**: typing.Optional[typing.Literal['blockchainInstant']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# ListTokenBalancesInputPaginateTypeDef

### tokenFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.TokenFilterTypeDef'>
- **Required**: Yes

### ownerFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.OwnerFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.PaginatorConfigTypeDef]


# ListTokenBalancesInputTypeDef

### tokenFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.TokenFilterTypeDef'>
- **Required**: Yes

### ownerFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.OwnerFilterTypeDef]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTokenBalancesOutputTypeDef

### tokenBalances
- **Type**: typing.List[aws_resource_validator.pydantic_models.managedblockchain_query_classes.TokenBalanceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTransactionEventsInputPaginateTypeDef

### network
- **Type**: typing.Literal['BITCOIN_MAINNET', 'BITCOIN_TESTNET', 'ETHEREUM_MAINNET', 'ETHEREUM_SEPOLIA_TESTNET']
- **Required**: Yes

### transactionHash
- **Type**: typing.Optional[str]

### transactionId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.PaginatorConfigTypeDef]


# ListTransactionEventsInputTypeDef

### network
- **Type**: typing.Literal['BITCOIN_MAINNET', 'BITCOIN_TESTNET', 'ETHEREUM_MAINNET', 'ETHEREUM_SEPOLIA_TESTNET']
- **Required**: Yes

### transactionHash
- **Type**: typing.Optional[str]

### transactionId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTransactionEventsOutputTypeDef

### events
- **Type**: typing.List[aws_resource_validator.pydantic_models.managedblockchain_query_classes.TransactionEventTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTransactionsInputPaginateTypeDef

### address
- **Type**: <class 'str'>
- **Required**: Yes

### network
- **Type**: typing.Literal['BITCOIN_MAINNET', 'BITCOIN_TESTNET', 'ETHEREUM_MAINNET', 'ETHEREUM_SEPOLIA_TESTNET']
- **Required**: Yes

### fromBlockchainInstant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.BlockchainInstantUnionTypeDef]

### toBlockchainInstant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.BlockchainInstantUnionTypeDef]

### sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.ListTransactionsSortTypeDef]

### confirmationStatusFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.ConfirmationStatusFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.PaginatorConfigTypeDef]


# ListTransactionsInputTypeDef

### address
- **Type**: <class 'str'>
- **Required**: Yes

### network
- **Type**: typing.Literal['BITCOIN_MAINNET', 'BITCOIN_TESTNET', 'ETHEREUM_MAINNET', 'ETHEREUM_SEPOLIA_TESTNET']
- **Required**: Yes

### fromBlockchainInstant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.BlockchainInstantUnionTypeDef]

### toBlockchainInstant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.BlockchainInstantUnionTypeDef]

### sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.ListTransactionsSortTypeDef]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### confirmationStatusFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.ConfirmationStatusFilterTypeDef]


# ListTransactionsOutputTypeDef

### transactions
- **Type**: typing.List[aws_resource_validator.pydantic_models.managedblockchain_query_classes.TransactionOutputItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTransactionsSortTypeDef

### sortBy
- **Type**: typing.Optional[typing.Literal['TRANSACTION_TIMESTAMP']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# OwnerFilterTypeDef

### address
- **Type**: <class 'str'>
- **Required**: Yes


# OwnerIdentifierTypeDef

### address
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


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


# TimeFilterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TokenBalanceTypeDef

### balance
- **Type**: <class 'str'>
- **Required**: Yes

### atBlockchainInstant
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.BlockchainInstantOutputTypeDef'>
- **Required**: Yes

### ownerIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.OwnerIdentifierTypeDef]

### tokenIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.TokenIdentifierTypeDef]

### lastUpdatedTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.BlockchainInstantOutputTypeDef]


# TokenFilterTypeDef

### network
- **Type**: typing.Literal['BITCOIN_MAINNET', 'BITCOIN_TESTNET', 'ETHEREUM_MAINNET', 'ETHEREUM_SEPOLIA_TESTNET']
- **Required**: Yes

### contractAddress
- **Type**: typing.Optional[str]

### tokenId
- **Type**: typing.Optional[str]


# TokenIdentifierTypeDef

### network
- **Type**: typing.Literal['BITCOIN_MAINNET', 'BITCOIN_TESTNET', 'ETHEREUM_MAINNET', 'ETHEREUM_SEPOLIA_TESTNET']
- **Required**: Yes

### contractAddress
- **Type**: typing.Optional[str]

### tokenId
- **Type**: typing.Optional[str]


# TransactionEventTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TransactionOutputItemTypeDef

### transactionHash
- **Type**: <class 'str'>
- **Required**: Yes

### network
- **Type**: typing.Literal['BITCOIN_MAINNET', 'BITCOIN_TESTNET', 'ETHEREUM_MAINNET', 'ETHEREUM_SEPOLIA_TESTNET']
- **Required**: Yes

### transactionTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### transactionId
- **Type**: typing.Optional[str]

### confirmationStatus
- **Type**: typing.Optional[typing.Literal['FINAL', 'NONFINAL']]


# TransactionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VoutFilterTypeDef

### voutSpent
- **Type**: <class 'bool'>
- **Required**: Yes


