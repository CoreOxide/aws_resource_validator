from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AddressIdentifierFilter(BaseValidatorModel):
    transactionEventToAddress: List[str]


class ContractIdentifier(BaseValidatorModel):
    network: QueryNetworkType
    contractAddress: str


class BlockchainInstantOutput(BaseValidatorModel):
    time: Optional[datetime] = None


class OwnerIdentifier(BaseValidatorModel):
    address: str


class TokenIdentifier(BaseValidatorModel):
    network: QueryNetworkType
    contractAddress: Optional[str] = None
    tokenId: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

Timestamp = Union[datetime, str]


class ConfirmationStatusFilter(BaseValidatorModel):
    include: List[ConfirmationStatusType]


class ContractFilter(BaseValidatorModel):
    network: QueryNetworkType
    tokenStandard: QueryTokenStandardType
    deployerAddress: str


class ContractMetadata(BaseValidatorModel):
    name: Optional[str] = None
    symbol: Optional[str] = None
    decimals: Optional[int] = None


# This class is the input for the 'get_transaction' function.
class GetTransactionInput(BaseValidatorModel):
    network: QueryNetworkType
    transactionHash: Optional[str] = None
    transactionId: Optional[str] = None


class Transaction(BaseValidatorModel):
    network: QueryNetworkType
    transactionHash: str
    transactionTimestamp: datetime
    transactionIndex: int
    numberOfTransactions: int
    to: str
    blockHash: Optional[str] = None
    blockNumber: Optional[str] = None
    from_: Optional[str] = None
    contractAddress: Optional[str] = None
    gasUsed: Optional[str] = None
    cumulativeGasUsed: Optional[str] = None
    effectiveGasPrice: Optional[str] = None
    signatureV: Optional[int] = None
    signatureR: Optional[str] = None
    signatureS: Optional[str] = None
    transactionFee: Optional[str] = None
    transactionId: Optional[str] = None
    confirmationStatus: Optional[ConfirmationStatusType] = None
    executionStatus: Optional[ExecutionStatusType] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListFilteredTransactionEventsSort(BaseValidatorModel):
    sortBy: Optional[Literal['blockchainInstant']] = None
    sortOrder: Optional[SortOrderType] = None


class VoutFilter(BaseValidatorModel):
    voutSpent: bool


class OwnerFilter(BaseValidatorModel):
    address: str


class TokenFilter(BaseValidatorModel):
    network: QueryNetworkType
    contractAddress: Optional[str] = None
    tokenId: Optional[str] = None


# This class is the input for the 'list_transaction_events' function.
class ListTransactionEventsInput(BaseValidatorModel):
    network: QueryNetworkType
    transactionHash: Optional[str] = None
    transactionId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTransactionsSort(BaseValidatorModel):
    sortBy: Optional[Literal['TRANSACTION_TIMESTAMP']] = None
    sortOrder: Optional[SortOrderType] = None


class TransactionOutputItem(BaseValidatorModel):
    transactionHash: str
    network: QueryNetworkType
    transactionTimestamp: datetime
    transactionId: Optional[str] = None
    confirmationStatus: Optional[ConfirmationStatusType] = None


class AssetContract(BaseValidatorModel):
    contractIdentifier: ContractIdentifier
    tokenStandard: QueryTokenStandardType
    deployerAddress: str


# This class is the input for the 'get_asset_contract' function.
class GetAssetContractInput(BaseValidatorModel):
    contractIdentifier: ContractIdentifier


class TransactionEvent(BaseValidatorModel):
    network: QueryNetworkType
    transactionHash: str
    eventType: QueryTransactionEventTypeType
    from_: Optional[str] = None
    to: Optional[str] = None
    value: Optional[str] = None
    contractAddress: Optional[str] = None
    tokenId: Optional[str] = None
    transactionId: Optional[str] = None
    voutIndex: Optional[int] = None
    voutSpent: Optional[bool] = None
    spentVoutTransactionId: Optional[str] = None
    spentVoutTransactionHash: Optional[str] = None
    spentVoutIndex: Optional[int] = None
    blockchainInstant: Optional[BlockchainInstantOutput] = None
    confirmationStatus: Optional[ConfirmationStatusType] = None


class BatchGetTokenBalanceErrorItem(BaseValidatorModel):
    errorCode: str
    errorMessage: str
    errorType: ErrorTypeType
    tokenIdentifier: Optional[TokenIdentifier] = None
    ownerIdentifier: Optional[OwnerIdentifier] = None
    atBlockchainInstant: Optional[BlockchainInstantOutput] = None


class BatchGetTokenBalanceOutputItem(BaseValidatorModel):
    balance: str
    atBlockchainInstant: BlockchainInstantOutput
    ownerIdentifier: Optional[OwnerIdentifier] = None
    tokenIdentifier: Optional[TokenIdentifier] = None
    lastUpdatedTime: Optional[BlockchainInstantOutput] = None


class TokenBalance(BaseValidatorModel):
    balance: str
    atBlockchainInstant: BlockchainInstantOutput
    ownerIdentifier: Optional[OwnerIdentifier] = None
    tokenIdentifier: Optional[TokenIdentifier] = None
    lastUpdatedTime: Optional[BlockchainInstantOutput] = None


# This class is the output for the 'get_token_balance' function.
class GetTokenBalanceOutput(BaseValidatorModel):
    ownerIdentifier: OwnerIdentifier
    tokenIdentifier: TokenIdentifier
    balance: str
    atBlockchainInstant: BlockchainInstantOutput
    lastUpdatedTime: BlockchainInstantOutput
    ResponseMetadata: ResponseMetadata


class BlockchainInstant(BaseValidatorModel):
    time: Optional[Timestamp] = None


# This class is the input for the 'list_asset_contracts' function.
class ListAssetContractsInput(BaseValidatorModel):
    contractFilter: ContractFilter
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the output for the 'get_asset_contract' function.
class GetAssetContractOutput(BaseValidatorModel):
    contractIdentifier: ContractIdentifier
    tokenStandard: QueryTokenStandardType
    deployerAddress: str
    metadata: ContractMetadata
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_transaction' function.
class GetTransactionOutput(BaseValidatorModel):
    transaction: Transaction
    ResponseMetadata: ResponseMetadata


class ListAssetContractsInputPaginate(BaseValidatorModel):
    contractFilter: ContractFilter
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTransactionEventsInputPaginate(BaseValidatorModel):
    network: QueryNetworkType
    transactionHash: Optional[str] = None
    transactionId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTokenBalancesInputPaginate(BaseValidatorModel):
    tokenFilter: TokenFilter
    ownerFilter: Optional[OwnerFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_token_balances' function.
class ListTokenBalancesInput(BaseValidatorModel):
    tokenFilter: TokenFilter
    ownerFilter: Optional[OwnerFilter] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the output for the 'list_transactions' function.
class ListTransactionsOutput(BaseValidatorModel):
    transactions: List[TransactionOutputItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_asset_contracts' function.
class ListAssetContractsOutput(BaseValidatorModel):
    contracts: List[AssetContract]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_filtered_transaction_events' function.
class ListFilteredTransactionEventsOutput(BaseValidatorModel):
    events: List[TransactionEvent]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_transaction_events' function.
class ListTransactionEventsOutput(BaseValidatorModel):
    events: List[TransactionEvent]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'batch_get_token_balance' function.
class BatchGetTokenBalanceOutput(BaseValidatorModel):
    tokenBalances: List[BatchGetTokenBalanceOutputItem]
    errors: List[BatchGetTokenBalanceErrorItem]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_token_balances' function.
class ListTokenBalancesOutput(BaseValidatorModel):
    tokenBalances: List[TokenBalance]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

BlockchainInstantUnion = Union[BlockchainInstant, BlockchainInstantOutput]


class BatchGetTokenBalanceInputItem(BaseValidatorModel):
    tokenIdentifier: TokenIdentifier
    ownerIdentifier: OwnerIdentifier
    atBlockchainInstant: Optional[BlockchainInstantUnion] = None


# This class is the input for the 'get_token_balance' function.
class GetTokenBalanceInput(BaseValidatorModel):
    tokenIdentifier: TokenIdentifier
    ownerIdentifier: OwnerIdentifier
    atBlockchainInstant: Optional[BlockchainInstantUnion] = None


class ListTransactionsInputPaginate(BaseValidatorModel):
    address: str
    network: QueryNetworkType
    fromBlockchainInstant: Optional[BlockchainInstantUnion] = None
    toBlockchainInstant: Optional[BlockchainInstantUnion] = None
    sort: Optional[ListTransactionsSort] = None
    confirmationStatusFilter: Optional[ConfirmationStatusFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_transactions' function.
class ListTransactionsInput(BaseValidatorModel):
    address: str
    network: QueryNetworkType
    fromBlockchainInstant: Optional[BlockchainInstantUnion] = None
    toBlockchainInstant: Optional[BlockchainInstantUnion] = None
    sort: Optional[ListTransactionsSort] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    confirmationStatusFilter: Optional[ConfirmationStatusFilter] = None


class TimeFilter(BaseValidatorModel):
    from_: Optional[BlockchainInstantUnion] = None
    to: Optional[BlockchainInstantUnion] = None


# This class is the input for the 'batch_get_token_balance' function.
class BatchGetTokenBalanceInput(BaseValidatorModel):
    getTokenBalanceInputs: Optional[List[BatchGetTokenBalanceInputItem]] = None


class ListFilteredTransactionEventsInputPaginate(BaseValidatorModel):
    network: str
    addressIdentifierFilter: AddressIdentifierFilter
    timeFilter: Optional[TimeFilter] = None
    voutFilter: Optional[VoutFilter] = None
    confirmationStatusFilter: Optional[ConfirmationStatusFilter] = None
    sort: Optional[ListFilteredTransactionEventsSort] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_filtered_transaction_events' function.
class ListFilteredTransactionEventsInput(BaseValidatorModel):
    network: str
    addressIdentifierFilter: AddressIdentifierFilter
    timeFilter: Optional[TimeFilter] = None
    voutFilter: Optional[VoutFilter] = None
    confirmationStatusFilter: Optional[ConfirmationStatusFilter] = None
    sort: Optional[ListFilteredTransactionEventsSort] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None