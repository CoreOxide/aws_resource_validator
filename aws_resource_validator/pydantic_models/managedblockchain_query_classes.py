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
from aws_resource_validator.pydantic_models.managedblockchain_query_constants import *

class AddressIdentifierFilter(BaseValidatorModel):
    transactionEventToAddress: Sequence[str]


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


class ConfirmationStatusFilter(BaseValidatorModel):
    include: Sequence[ConfirmationStatusType]


class ContractFilter(BaseValidatorModel):
    network: QueryNetworkType
    tokenStandard: QueryTokenStandardType
    deployerAddress: str


class ContractMetadata(BaseValidatorModel):
    name: Optional[str] = None
    symbol: Optional[str] = None
    decimals: Optional[int] = None


class GetTransactionInput(BaseValidatorModel):
    network: QueryNetworkType
    transactionHash: Optional[str] = None
    transactionId: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListFilteredTransactionEventsSort(BaseValidatorModel):
    sortBy: Optional[Literal["blockchainInstant"]] = None
    sortOrder: Optional[SortOrderType] = None


class VoutFilter(BaseValidatorModel):
    voutSpent: bool


class OwnerFilter(BaseValidatorModel):
    address: str


class TokenFilter(BaseValidatorModel):
    network: QueryNetworkType
    contractAddress: Optional[str] = None
    tokenId: Optional[str] = None


class ListTransactionEventsInput(BaseValidatorModel):
    network: QueryNetworkType
    transactionHash: Optional[str] = None
    transactionId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTransactionsSort(BaseValidatorModel):
    sortBy: Optional[Literal["TRANSACTION_TIMESTAMP"]] = None
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


class GetAssetContractInput(BaseValidatorModel):
    contractIdentifier: ContractIdentifier


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


class GetTokenBalanceOutput(BaseValidatorModel):
    ownerIdentifier: OwnerIdentifier
    tokenIdentifier: TokenIdentifier
    balance: str
    atBlockchainInstant: BlockchainInstantOutput
    lastUpdatedTime: BlockchainInstantOutput
    ResponseMetadata: ResponseMetadata


class Timestamp(BaseValidatorModel):
    pass


class BlockchainInstant(BaseValidatorModel):
    time: Optional[Timestamp] = None


class ListAssetContractsInput(BaseValidatorModel):
    contractFilter: ContractFilter
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetAssetContractOutput(BaseValidatorModel):
    contractIdentifier: ContractIdentifier
    tokenStandard: QueryTokenStandardType
    deployerAddress: str
    metadata: ContractMetadata
    ResponseMetadata: ResponseMetadata


class Transaction(BaseValidatorModel):
    pass


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


class ListTokenBalancesInput(BaseValidatorModel):
    tokenFilter: TokenFilter
    ownerFilter: Optional[OwnerFilter] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTransactionsOutput(BaseValidatorModel):
    transactions: List[TransactionOutputItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListAssetContractsOutput(BaseValidatorModel):
    contracts: List[AssetContract]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class TransactionEvent(BaseValidatorModel):
    pass


class ListFilteredTransactionEventsOutput(BaseValidatorModel):
    events: List[TransactionEvent]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTransactionEventsOutput(BaseValidatorModel):
    events: List[TransactionEvent]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class BatchGetTokenBalanceOutput(BaseValidatorModel):
    tokenBalances: List[BatchGetTokenBalanceOutputItem]
    errors: List[BatchGetTokenBalanceErrorItem]
    ResponseMetadata: ResponseMetadata


class ListTokenBalancesOutput(BaseValidatorModel):
    tokenBalances: List[TokenBalance]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class BlockchainInstantUnion(BaseValidatorModel):
    pass


class BatchGetTokenBalanceInputItem(BaseValidatorModel):
    tokenIdentifier: TokenIdentifier
    ownerIdentifier: OwnerIdentifier
    atBlockchainInstant: Optional[BlockchainInstantUnion] = None


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


class ListTransactionsInput(BaseValidatorModel):
    address: str
    network: QueryNetworkType
    fromBlockchainInstant: Optional[BlockchainInstantUnion] = None
    toBlockchainInstant: Optional[BlockchainInstantUnion] = None
    sort: Optional[ListTransactionsSort] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    confirmationStatusFilter: Optional[ConfirmationStatusFilter] = None


class BatchGetTokenBalanceInput(BaseValidatorModel):
    getTokenBalanceInputs: Optional[Sequence[BatchGetTokenBalanceInputItem]] = None


class TimeFilter(BaseValidatorModel):
    pass


class ListFilteredTransactionEventsInputPaginate(BaseValidatorModel):
    network: str
    addressIdentifierFilter: AddressIdentifierFilter
    timeFilter: Optional[TimeFilter] = None
    voutFilter: Optional[VoutFilter] = None
    confirmationStatusFilter: Optional[ConfirmationStatusFilter] = None
    sort: Optional[ListFilteredTransactionEventsSort] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFilteredTransactionEventsInput(BaseValidatorModel):
    network: str
    addressIdentifierFilter: AddressIdentifierFilter
    timeFilter: Optional[TimeFilter] = None
    voutFilter: Optional[VoutFilter] = None
    confirmationStatusFilter: Optional[ConfirmationStatusFilter] = None
    sort: Optional[ListFilteredTransactionEventsSort] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


