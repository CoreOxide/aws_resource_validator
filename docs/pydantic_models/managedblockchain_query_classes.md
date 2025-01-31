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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.BlockchainInstantTypeDef]


# BatchGetTokenBalanceInputItemTypeDef

### tokenIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.TokenIdentifierTypeDef'>
- **Required**: Yes

### ownerIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.OwnerIdentifierTypeDef'>
- **Required**: Yes

### atBlockchainInstant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.BlockchainInstantTypeDef]


# BatchGetTokenBalanceInputRequestTypeDef

### getTokenBalanceInputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.managedblockchain_query_classes.BatchGetTokenBalanceInputItemTypeDef]]


# BatchGetTokenBalanceOutputItemTypeDef

### balance
- **Type**: <class 'str'>
- **Required**: Yes

### atBlockchainInstant
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.BlockchainInstantTypeDef'>
- **Required**: Yes

### ownerIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.OwnerIdentifierTypeDef]

### tokenIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.TokenIdentifierTypeDef]

### lastUpdatedTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.BlockchainInstantTypeDef]


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


# BlockchainInstantTypeDef

### time
- **Type**: typing.Union[datetime.datetime, str, NoneType]


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


# GetAssetContractInputRequestTypeDef

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


# GetTokenBalanceInputRequestTypeDef

### tokenIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.TokenIdentifierTypeDef'>
- **Required**: Yes

### ownerIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.OwnerIdentifierTypeDef'>
- **Required**: Yes

### atBlockchainInstant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.BlockchainInstantTypeDef]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.BlockchainInstantTypeDef'>
- **Required**: Yes

### lastUpdatedTime
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.BlockchainInstantTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTransactionInputRequestTypeDef

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


# ListAssetContractsInputListAssetContractsPaginateTypeDef

### contractFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.ContractFilterTypeDef'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.PaginatorConfigTypeDef]


# ListAssetContractsInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFilteredTransactionEventsInputListFilteredTransactionEventsPaginateTypeDef

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


# ListFilteredTransactionEventsInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFilteredTransactionEventsSortTypeDef

### sortBy
- **Type**: typing.Optional[typing.Literal['blockchainInstant']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# ListTokenBalancesInputListTokenBalancesPaginateTypeDef

### tokenFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.TokenFilterTypeDef'>
- **Required**: Yes

### ownerFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.OwnerFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.PaginatorConfigTypeDef]


# ListTokenBalancesInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTransactionEventsInputListTransactionEventsPaginateTypeDef

### network
- **Type**: typing.Literal['BITCOIN_MAINNET', 'BITCOIN_TESTNET', 'ETHEREUM_MAINNET', 'ETHEREUM_SEPOLIA_TESTNET']
- **Required**: Yes

### transactionHash
- **Type**: typing.Optional[str]

### transactionId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.PaginatorConfigTypeDef]


# ListTransactionEventsInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTransactionsInputListTransactionsPaginateTypeDef

### address
- **Type**: <class 'str'>
- **Required**: Yes

### network
- **Type**: typing.Literal['BITCOIN_MAINNET', 'BITCOIN_TESTNET', 'ETHEREUM_MAINNET', 'ETHEREUM_SEPOLIA_TESTNET']
- **Required**: Yes

### fromBlockchainInstant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.BlockchainInstantTypeDef]

### toBlockchainInstant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.BlockchainInstantTypeDef]

### sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.ListTransactionsSortTypeDef]

### confirmationStatusFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.ConfirmationStatusFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.PaginatorConfigTypeDef]


# ListTransactionsInputRequestTypeDef

### address
- **Type**: <class 'str'>
- **Required**: Yes

### network
- **Type**: typing.Literal['BITCOIN_MAINNET', 'BITCOIN_TESTNET', 'ETHEREUM_MAINNET', 'ETHEREUM_SEPOLIA_TESTNET']
- **Required**: Yes

### fromBlockchainInstant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.BlockchainInstantTypeDef]

### toBlockchainInstant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.BlockchainInstantTypeDef]

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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

### to
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.BlockchainInstantTypeDef]


# TokenBalanceTypeDef

### balance
- **Type**: <class 'str'>
- **Required**: Yes

### atBlockchainInstant
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query_classes.BlockchainInstantTypeDef'>
- **Required**: Yes

### ownerIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.OwnerIdentifierTypeDef]

### tokenIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.TokenIdentifierTypeDef]

### lastUpdatedTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.BlockchainInstantTypeDef]


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

### network
- **Type**: typing.Literal['BITCOIN_MAINNET', 'BITCOIN_TESTNET', 'ETHEREUM_MAINNET', 'ETHEREUM_SEPOLIA_TESTNET']
- **Required**: Yes

### transactionHash
- **Type**: <class 'str'>
- **Required**: Yes

### eventType
- **Type**: typing.Literal['BITCOIN_VIN', 'BITCOIN_VOUT', 'ERC1155_TRANSFER', 'ERC20_BURN', 'ERC20_DEPOSIT', 'ERC20_MINT', 'ERC20_TRANSFER', 'ERC20_WITHDRAWAL', 'ERC721_TRANSFER', 'ETH_TRANSFER', 'INTERNAL_ETH_TRANSFER']
- **Required**: Yes

### to
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]

### contractAddress
- **Type**: typing.Optional[str]

### tokenId
- **Type**: typing.Optional[str]

### transactionId
- **Type**: typing.Optional[str]

### voutIndex
- **Type**: typing.Optional[int]

### voutSpent
- **Type**: typing.Optional[bool]

### spentVoutTransactionId
- **Type**: typing.Optional[str]

### spentVoutTransactionHash
- **Type**: typing.Optional[str]

### spentVoutIndex
- **Type**: typing.Optional[int]

### blockchainInstant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query_classes.BlockchainInstantTypeDef]

### confirmationStatus
- **Type**: typing.Optional[typing.Literal['FINAL', 'NONFINAL']]


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

### network
- **Type**: typing.Literal['BITCOIN_MAINNET', 'BITCOIN_TESTNET', 'ETHEREUM_MAINNET', 'ETHEREUM_SEPOLIA_TESTNET']
- **Required**: Yes

### transactionHash
- **Type**: <class 'str'>
- **Required**: Yes

### transactionTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### transactionIndex
- **Type**: <class 'int'>
- **Required**: Yes

### numberOfTransactions
- **Type**: <class 'int'>
- **Required**: Yes

### to
- **Type**: <class 'str'>
- **Required**: Yes

### blockHash
- **Type**: typing.Optional[str]

### blockNumber
- **Type**: typing.Optional[str]

### contractAddress
- **Type**: typing.Optional[str]

### gasUsed
- **Type**: typing.Optional[str]

### cumulativeGasUsed
- **Type**: typing.Optional[str]

### effectiveGasPrice
- **Type**: typing.Optional[str]

### signatureV
- **Type**: typing.Optional[int]

### signatureR
- **Type**: typing.Optional[str]

### signatureS
- **Type**: typing.Optional[str]

### transactionFee
- **Type**: typing.Optional[str]

### transactionId
- **Type**: typing.Optional[str]

### confirmationStatus
- **Type**: typing.Optional[typing.Literal['FINAL', 'NONFINAL']]

### executionStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'SUCCEEDED']]


# VoutFilterTypeDef

### voutSpent
- **Type**: <class 'bool'>
- **Required**: Yes


