from typing import Literal, Union, Optional, List, Dict, Any, Sequence, Mapping, IO
from datetime import datetime

AcceleratorManufacturerType = Literal["amazon-web-services", "amd", "habana", "nvidia", "xilinx"]
AcceleratorNameType = Literal["a100",
    "a10g",
    "h100",
    "inferentia",
    "k520",
    "k80",
    "m60",
    "radeon-pro-v520",
    "t4",
    "t4g",
    "v100",
    "vu9p",]
AcceleratorTypeType = Literal["fpga", "gpu", "inference"]
AccountAttributeNameType = Literal["default-vpc", "supported-platforms"]
ActivityStatusType = Literal["error", "fulfilled", "pending_fulfillment", "pending_termination"]
AddressAttributeNameType = Literal["domain-name"]
AddressFamilyType = Literal["ipv4", "ipv6"]
AddressTransferStatusType = Literal["accepted", "disabled", "pending"]
AffinityType = Literal["default", "host"]
AllocationStateType = Literal["available",
    "pending",
    "permanent-failure",
    "released",
    "released-permanent-failure",
    "under-assessment",]
AllocationStrategyType = Literal["capacityOptimized",
    "capacityOptimizedPrioritized",
    "diversified",
    "lowestPrice",
    "priceCapacityOptimized",]
AllocationTypeType = Literal["used"]
AllowsMultipleInstanceTypesType = Literal["off", "on"]
AmdSevSnpSpecificationType = Literal["disabled", "enabled"]
AnalysisStatusType = Literal["failed", "running", "succeeded"]
ApplianceModeSupportValueType = Literal["disable", "enable"]
ArchitectureTypeType = Literal["arm64", "arm64_mac", "i386", "x86_64", "x86_64_mac"]
ArchitectureValuesType = Literal["arm64", "arm64_mac", "i386", "x86_64", "x86_64_mac"]
AsnAssociationStateType = Literal["associated",
    "disassociated",
    "failed-association",
    "failed-disassociation",
    "pending-association",
    "pending-disassociation",]
AsnStateType = Literal["deprovisioned",
    "failed-deprovision",
    "failed-provision",
    "pending-deprovision",
    "pending-provision",
    "provisioned",]
AssociatedNetworkTypeType = Literal["vpc"]
AssociationStatusCodeType = Literal["associated", "associating", "association-failed", "disassociated", "disassociating"]
AttachmentStatusType = Literal["attached", "attaching", "detached", "detaching"]
AutoAcceptSharedAssociationsValueType = Literal["disable", "enable"]
AutoAcceptSharedAttachmentsValueType = Literal["disable", "enable"]
AutoPlacementType = Literal["off", "on"]
AvailabilityZoneOptInStatusType = Literal["not-opted-in", "opt-in-not-required", "opted-in"]
AvailabilityZoneStateType = Literal["available", "constrained", "impaired", "information", "unavailable"]
BareMetalType = Literal["excluded", "included", "required"]
BatchStateType = Literal["active",
    "cancelled",
    "cancelled_running",
    "cancelled_terminating",
    "failed",
    "modifying",
    "submitted",]
BgpStatusType = Literal["down", "up"]
BootModeTypeType = Literal["legacy-bios", "uefi"]
BootModeValuesType = Literal["legacy-bios", "uefi", "uefi-preferred"]
BundleTaskCompleteWaiterName = Literal["bundle_task_complete"]
BundleTaskStateType = Literal["bundling", "cancelling", "complete", "failed", "pending", "storing", "waiting-for-shutdown"]
BurstablePerformanceType = Literal["excluded", "included", "required"]
ByoipCidrStateType = Literal["advertised",
    "deprovisioned",
    "failed-deprovision",
    "failed-provision",
    "pending-deprovision",
    "pending-provision",
    "provisioned",
    "provisioned-not-publicly-advertisable",]
CancelBatchErrorCodeType = Literal["fleetRequestIdDoesNotExist",
    "fleetRequestIdMalformed",
    "fleetRequestNotInCancellableState",
    "unexpectedError",]
CancelSpotInstanceRequestStateType = Literal["active", "cancelled", "closed", "completed", "open"]
CapacityReservationFleetStateType = Literal["active",
    "cancelled",
    "cancelling",
    "expired",
    "expiring",
    "failed",
    "modifying",
    "partially_fulfilled",
    "submitted",]
CapacityReservationInstancePlatformType = Literal["Linux with SQL Server Enterprise",
    "Linux with SQL Server Standard",
    "Linux with SQL Server Web",
    "Linux/UNIX",
    "RHEL with HA",
    "RHEL with HA and SQL Server Enterprise",
    "RHEL with HA and SQL Server Standard",
    "RHEL with SQL Server Enterprise",
    "RHEL with SQL Server Standard",
    "RHEL with SQL Server Web",
    "Red Hat Enterprise Linux",
    "SUSE Linux",
    "Ubuntu Pro",
    "Windows",
    "Windows with SQL Server",
    "Windows with SQL Server Enterprise",
    "Windows with SQL Server Standard",
    "Windows with SQL Server Web",]
CapacityReservationPreferenceType = Literal["none", "open"]
CapacityReservationStateType = Literal["active",
    "cancelled",
    "expired",
    "failed",
    "payment-failed",
    "payment-pending",
    "pending",
    "scheduled",]
CapacityReservationTenancyType = Literal["dedicated", "default"]
CapacityReservationTypeType = Literal["capacity-block", "default"]
CarrierGatewayStateType = Literal["available", "deleted", "deleting", "pending"]
ClientCertificateRevocationListStatusCodeType = Literal["active", "pending"]
ClientVpnAuthenticationTypeType = Literal["certificate-authentication", "directory-service-authentication", "federated-authentication"]
ClientVpnAuthorizationRuleStatusCodeType = Literal["active", "authorizing", "failed", "revoking"]
ClientVpnConnectionStatusCodeType = Literal["active", "failed-to-terminate", "terminated", "terminating"]
ClientVpnEndpointAttributeStatusCodeType = Literal["applied", "applying"]
ClientVpnEndpointStatusCodeType = Literal["available", "deleted", "deleting", "pending-associate"]
ClientVpnRouteStatusCodeType = Literal["active", "creating", "deleting", "failed"]
ConnectionNotificationStateType = Literal["Disabled", "Enabled"]
ConnectionNotificationTypeType = Literal["Topic"]
ConnectivityTypeType = Literal["private", "public"]
ContainerFormatType = Literal["ova"]
ConversionTaskCancelledWaiterName = Literal["conversion_task_cancelled"]
ConversionTaskCompletedWaiterName = Literal["conversion_task_completed"]
ConversionTaskDeletedWaiterName = Literal["conversion_task_deleted"]
ConversionTaskStateType = Literal["active", "cancelled", "cancelling", "completed"]
CopyTagsFromSourceType = Literal["volume"]
CpuManufacturerType = Literal["amazon-web-services", "amd", "intel"]
CurrencyCodeValuesType = Literal["USD"]
CustomerGatewayAvailableWaiterName = Literal["customer_gateway_available"]
DatafeedSubscriptionStateType = Literal["Active", "Inactive"]
DefaultInstanceMetadataEndpointStateType = Literal["disabled", "enabled", "no-preference"]
DefaultInstanceMetadataTagsStateType = Literal["disabled", "enabled", "no-preference"]
DefaultRouteTableAssociationValueType = Literal["disable", "enable"]
DefaultRouteTablePropagationValueType = Literal["disable", "enable"]
DefaultTargetCapacityTypeType = Literal["capacity-block", "on-demand", "spot"]
DeleteFleetErrorCodeType = Literal["fleetIdDoesNotExist", "fleetIdMalformed", "fleetNotInDeletableState", "unexpectedError"]
DeleteQueuedReservedInstancesErrorCodeType = Literal["reserved-instances-id-invalid", "reserved-instances-not-in-queued-state", "unexpected-error"]
DescribeAddressTransfersPaginatorName = Literal["describe_address_transfers"]
DescribeAddressesAttributePaginatorName = Literal["describe_addresses_attribute"]
DescribeAwsNetworkPerformanceMetricSubscriptionsPaginatorName = Literal["describe_aws_network_performance_metric_subscriptions"]
DescribeByoipCidrsPaginatorName = Literal["describe_byoip_cidrs"]
DescribeCapacityBlockOfferingsPaginatorName = Literal["describe_capacity_block_offerings"]
DescribeCapacityReservationFleetsPaginatorName = Literal["describe_capacity_reservation_fleets"]
DescribeCapacityReservationsPaginatorName = Literal["describe_capacity_reservations"]
DescribeCarrierGatewaysPaginatorName = Literal["describe_carrier_gateways"]
DescribeClassicLinkInstancesPaginatorName = Literal["describe_classic_link_instances"]
DescribeClientVpnAuthorizationRulesPaginatorName = Literal["describe_client_vpn_authorization_rules"]
DescribeClientVpnConnectionsPaginatorName = Literal["describe_client_vpn_connections"]
DescribeClientVpnEndpointsPaginatorName = Literal["describe_client_vpn_endpoints"]
DescribeClientVpnRoutesPaginatorName = Literal["describe_client_vpn_routes"]
DescribeClientVpnTargetNetworksPaginatorName = Literal["describe_client_vpn_target_networks"]
DescribeCoipPoolsPaginatorName = Literal["describe_coip_pools"]
DescribeDhcpOptionsPaginatorName = Literal["describe_dhcp_options"]
DescribeEgressOnlyInternetGatewaysPaginatorName = Literal["describe_egress_only_internet_gateways"]
DescribeExportImageTasksPaginatorName = Literal["describe_export_image_tasks"]
DescribeFastLaunchImagesPaginatorName = Literal["describe_fast_launch_images"]
DescribeFastSnapshotRestoresPaginatorName = Literal["describe_fast_snapshot_restores"]
DescribeFleetsPaginatorName = Literal["describe_fleets"]
DescribeFlowLogsPaginatorName = Literal["describe_flow_logs"]
DescribeFpgaImagesPaginatorName = Literal["describe_fpga_images"]
DescribeHostReservationOfferingsPaginatorName = Literal["describe_host_reservation_offerings"]
DescribeHostReservationsPaginatorName = Literal["describe_host_reservations"]
DescribeHostsPaginatorName = Literal["describe_hosts"]
DescribeIamInstanceProfileAssociationsPaginatorName = Literal["describe_iam_instance_profile_associations"]
DescribeImagesPaginatorName = Literal["describe_images"]
DescribeImportImageTasksPaginatorName = Literal["describe_import_image_tasks"]
DescribeImportSnapshotTasksPaginatorName = Literal["describe_import_snapshot_tasks"]
DescribeInstanceConnectEndpointsPaginatorName = Literal["describe_instance_connect_endpoints"]
DescribeInstanceCreditSpecificationsPaginatorName = Literal["describe_instance_credit_specifications"]
DescribeInstanceEventWindowsPaginatorName = Literal["describe_instance_event_windows"]
DescribeInstanceStatusPaginatorName = Literal["describe_instance_status"]
DescribeInstanceTopologyPaginatorName = Literal["describe_instance_topology"]
DescribeInstanceTypeOfferingsPaginatorName = Literal["describe_instance_type_offerings"]
DescribeInstanceTypesPaginatorName = Literal["describe_instance_types"]
DescribeInstancesPaginatorName = Literal["describe_instances"]
DescribeInternetGatewaysPaginatorName = Literal["describe_internet_gateways"]
DescribeIpamPoolsPaginatorName = Literal["describe_ipam_pools"]
DescribeIpamResourceDiscoveriesPaginatorName = Literal["describe_ipam_resource_discoveries"]
DescribeIpamResourceDiscoveryAssociationsPaginatorName = Literal["describe_ipam_resource_discovery_associations"]
DescribeIpamScopesPaginatorName = Literal["describe_ipam_scopes"]
DescribeIpamsPaginatorName = Literal["describe_ipams"]
DescribeIpv6PoolsPaginatorName = Literal["describe_ipv6_pools"]
DescribeLaunchTemplateVersionsPaginatorName = Literal["describe_launch_template_versions"]
DescribeLaunchTemplatesPaginatorName = Literal["describe_launch_templates"]
DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginatorName = Literal["describe_local_gateway_route_table_virtual_interface_group_associations"]
DescribeLocalGatewayRouteTableVpcAssociationsPaginatorName = Literal["describe_local_gateway_route_table_vpc_associations"]
DescribeLocalGatewayRouteTablesPaginatorName = Literal["describe_local_gateway_route_tables"]
DescribeLocalGatewayVirtualInterfaceGroupsPaginatorName = Literal["describe_local_gateway_virtual_interface_groups"]
DescribeLocalGatewayVirtualInterfacesPaginatorName = Literal["describe_local_gateway_virtual_interfaces"]
DescribeLocalGatewaysPaginatorName = Literal["describe_local_gateways"]
DescribeMacHostsPaginatorName = Literal["describe_mac_hosts"]
DescribeManagedPrefixListsPaginatorName = Literal["describe_managed_prefix_lists"]
DescribeMovingAddressesPaginatorName = Literal["describe_moving_addresses"]
DescribeNatGatewaysPaginatorName = Literal["describe_nat_gateways"]
DescribeNetworkAclsPaginatorName = Literal["describe_network_acls"]
DescribeNetworkInsightsAccessScopeAnalysesPaginatorName = Literal["describe_network_insights_access_scope_analyses"]
DescribeNetworkInsightsAccessScopesPaginatorName = Literal["describe_network_insights_access_scopes"]
DescribeNetworkInsightsAnalysesPaginatorName = Literal["describe_network_insights_analyses"]
DescribeNetworkInsightsPathsPaginatorName = Literal["describe_network_insights_paths"]
DescribeNetworkInterfacePermissionsPaginatorName = Literal["describe_network_interface_permissions"]
DescribeNetworkInterfacesPaginatorName = Literal["describe_network_interfaces"]
DescribePrefixListsPaginatorName = Literal["describe_prefix_lists"]
DescribePrincipalIdFormatPaginatorName = Literal["describe_principal_id_format"]
DescribePublicIpv4PoolsPaginatorName = Literal["describe_public_ipv4_pools"]
DescribeReplaceRootVolumeTasksPaginatorName = Literal["describe_replace_root_volume_tasks"]
DescribeReservedInstancesModificationsPaginatorName = Literal["describe_reserved_instances_modifications"]
DescribeReservedInstancesOfferingsPaginatorName = Literal["describe_reserved_instances_offerings"]
DescribeRouteTablesPaginatorName = Literal["describe_route_tables"]
DescribeScheduledInstanceAvailabilityPaginatorName = Literal["describe_scheduled_instance_availability"]
DescribeScheduledInstancesPaginatorName = Literal["describe_scheduled_instances"]
DescribeSecurityGroupRulesPaginatorName = Literal["describe_security_group_rules"]
DescribeSecurityGroupsPaginatorName = Literal["describe_security_groups"]
DescribeSnapshotTierStatusPaginatorName = Literal["describe_snapshot_tier_status"]
DescribeSnapshotsPaginatorName = Literal["describe_snapshots"]
DescribeSpotFleetInstancesPaginatorName = Literal["describe_spot_fleet_instances"]
DescribeSpotFleetRequestsPaginatorName = Literal["describe_spot_fleet_requests"]
DescribeSpotInstanceRequestsPaginatorName = Literal["describe_spot_instance_requests"]
DescribeSpotPriceHistoryPaginatorName = Literal["describe_spot_price_history"]
DescribeStaleSecurityGroupsPaginatorName = Literal["describe_stale_security_groups"]
DescribeStoreImageTasksPaginatorName = Literal["describe_store_image_tasks"]
DescribeSubnetsPaginatorName = Literal["describe_subnets"]
DescribeTagsPaginatorName = Literal["describe_tags"]
DescribeTrafficMirrorFiltersPaginatorName = Literal["describe_traffic_mirror_filters"]
DescribeTrafficMirrorSessionsPaginatorName = Literal["describe_traffic_mirror_sessions"]
DescribeTrafficMirrorTargetsPaginatorName = Literal["describe_traffic_mirror_targets"]
DescribeTransitGatewayAttachmentsPaginatorName = Literal["describe_transit_gateway_attachments"]
DescribeTransitGatewayConnectPeersPaginatorName = Literal["describe_transit_gateway_connect_peers"]
DescribeTransitGatewayConnectsPaginatorName = Literal["describe_transit_gateway_connects"]
DescribeTransitGatewayMulticastDomainsPaginatorName = Literal["describe_transit_gateway_multicast_domains"]
DescribeTransitGatewayPeeringAttachmentsPaginatorName = Literal["describe_transit_gateway_peering_attachments"]
DescribeTransitGatewayPolicyTablesPaginatorName = Literal["describe_transit_gateway_policy_tables"]
DescribeTransitGatewayRouteTableAnnouncementsPaginatorName = Literal["describe_transit_gateway_route_table_announcements"]
DescribeTransitGatewayRouteTablesPaginatorName = Literal["describe_transit_gateway_route_tables"]
DescribeTransitGatewayVpcAttachmentsPaginatorName = Literal["describe_transit_gateway_vpc_attachments"]
DescribeTransitGatewaysPaginatorName = Literal["describe_transit_gateways"]
DescribeTrunkInterfaceAssociationsPaginatorName = Literal["describe_trunk_interface_associations"]
DescribeVerifiedAccessEndpointsPaginatorName = Literal["describe_verified_access_endpoints"]
DescribeVerifiedAccessGroupsPaginatorName = Literal["describe_verified_access_groups"]
DescribeVerifiedAccessInstanceLoggingConfigurationsPaginatorName = Literal["describe_verified_access_instance_logging_configurations"]
DescribeVerifiedAccessInstancesPaginatorName = Literal["describe_verified_access_instances"]
DescribeVerifiedAccessTrustProvidersPaginatorName = Literal["describe_verified_access_trust_providers"]
DescribeVolumeStatusPaginatorName = Literal["describe_volume_status"]
DescribeVolumesModificationsPaginatorName = Literal["describe_volumes_modifications"]
DescribeVolumesPaginatorName = Literal["describe_volumes"]
DescribeVpcClassicLinkDnsSupportPaginatorName = Literal["describe_vpc_classic_link_dns_support"]
DescribeVpcEndpointConnectionNotificationsPaginatorName = Literal["describe_vpc_endpoint_connection_notifications"]
DescribeVpcEndpointConnectionsPaginatorName = Literal["describe_vpc_endpoint_connections"]
DescribeVpcEndpointServiceConfigurationsPaginatorName = Literal["describe_vpc_endpoint_service_configurations"]
DescribeVpcEndpointServicePermissionsPaginatorName = Literal["describe_vpc_endpoint_service_permissions"]
DescribeVpcEndpointServicesPaginatorName = Literal["describe_vpc_endpoint_services"]
DescribeVpcEndpointsPaginatorName = Literal["describe_vpc_endpoints"]
DescribeVpcPeeringConnectionsPaginatorName = Literal["describe_vpc_peering_connections"]
DescribeVpcsPaginatorName = Literal["describe_vpcs"]
DestinationFileFormatType = Literal["parquet", "plain-text"]
DeviceTrustProviderTypeType = Literal["crowdstrike", "jamf", "jumpcloud"]
DeviceTypeType = Literal["ebs", "instance-store"]
DiskImageFormatType = Literal["RAW", "VHD", "VMDK"]
DiskTypeType = Literal["hdd", "ssd"]
DnsNameStateType = Literal["failed", "pendingVerification", "verified"]
DnsRecordIpTypeType = Literal["dualstack", "ipv4", "ipv6", "service-defined"]
DnsSupportValueType = Literal["disable", "enable"]
DomainTypeType = Literal["standard", "vpc"]
DynamicRoutingValueType = Literal["disable", "enable"]
EbsEncryptionSupportType = Literal["supported", "unsupported"]
EbsNvmeSupportType = Literal["required", "supported", "unsupported"]
EbsOptimizedSupportType = Literal["default", "supported", "unsupported"]
Ec2InstanceConnectEndpointStateType = Literal["create-complete",
    "create-failed",
    "create-in-progress",
    "delete-complete",
    "delete-failed",
    "delete-in-progress",]
EkPubKeyFormatType = Literal["der", "tpmt"]
EkPubKeyTypeType = Literal["ecc-sec-p384", "rsa-2048"]
ElasticGpuStateType = Literal["ATTACHED"]
ElasticGpuStatusType = Literal["IMPAIRED", "OK"]
EnaSupportType = Literal["required", "supported", "unsupported"]
EndDateTypeType = Literal["limited", "unlimited"]
EphemeralNvmeSupportType = Literal["required", "supported", "unsupported"]
EventCodeType = Literal["instance-reboot", "instance-retirement", "instance-stop", "system-maintenance", "system-reboot"]
EventTypeType = Literal["error", "fleetRequestChange", "information", "instanceChange"]
ExcessCapacityTerminationPolicyType = Literal["default", "noTermination"]
ExportEnvironmentType = Literal["citrix", "microsoft", "vmware"]
ExportTaskCancelledWaiterName = Literal["export_task_cancelled"]
ExportTaskCompletedWaiterName = Literal["export_task_completed"]
ExportTaskStateType = Literal["active", "cancelled", "cancelling", "completed"]
FastLaunchResourceTypeType = Literal["snapshot"]
FastLaunchStateCodeType = Literal["disabling", "disabling-failed", "enabled", "enabled-failed", "enabling", "enabling-failed"]
FastSnapshotRestoreStateCodeType = Literal["disabled", "disabling", "enabled", "enabling", "optimizing"]
FindingsFoundType = Literal["false", "true", "unknown"]
FleetActivityStatusType = Literal["error", "fulfilled", "pending_fulfillment", "pending_termination"]
FleetCapacityReservationTenancyType = Literal["default"]
FleetCapacityReservationUsageStrategyType = Literal["use-capacity-reservations-first"]
FleetEventTypeType = Literal["fleet-change", "instance-change", "service-error"]
FleetExcessCapacityTerminationPolicyType = Literal["no-termination", "termination"]
FleetInstanceMatchCriteriaType = Literal["open"]
FleetOnDemandAllocationStrategyType = Literal["lowest-price", "prioritized"]
FleetReplacementStrategyType = Literal["launch", "launch-before-terminate"]
FleetStateCodeType = Literal["active",
    "deleted",
    "deleted_running",
    "deleted_terminating",
    "failed",
    "modifying",
    "submitted",]
FleetTypeType = Literal["instant", "maintain", "request"]
FlowLogsResourceTypeType = Literal["NetworkInterface", "Subnet", "TransitGateway", "TransitGatewayAttachment", "VPC"]
FpgaImageAttributeNameType = Literal["description", "loadPermission", "name", "productCodes"]
FpgaImageStateCodeType = Literal["available", "failed", "pending", "unavailable"]
GatewayAssociationStateType = Literal["associated", "associating", "disassociating", "not-associated"]
GatewayTypeType = Literal["ipsec.1"]
GetAssociatedIpv6PoolCidrsPaginatorName = Literal["get_associated_ipv6_pool_cidrs"]
GetAwsNetworkPerformanceDataPaginatorName = Literal["get_aws_network_performance_data"]
GetGroupsForCapacityReservationPaginatorName = Literal["get_groups_for_capacity_reservation"]
GetInstanceTypesFromInstanceRequirementsPaginatorName = Literal["get_instance_types_from_instance_requirements"]
GetIpamAddressHistoryPaginatorName = Literal["get_ipam_address_history"]
GetIpamDiscoveredAccountsPaginatorName = Literal["get_ipam_discovered_accounts"]
GetIpamDiscoveredResourceCidrsPaginatorName = Literal["get_ipam_discovered_resource_cidrs"]
GetIpamPoolAllocationsPaginatorName = Literal["get_ipam_pool_allocations"]
GetIpamPoolCidrsPaginatorName = Literal["get_ipam_pool_cidrs"]
GetIpamResourceCidrsPaginatorName = Literal["get_ipam_resource_cidrs"]
GetManagedPrefixListAssociationsPaginatorName = Literal["get_managed_prefix_list_associations"]
GetManagedPrefixListEntriesPaginatorName = Literal["get_managed_prefix_list_entries"]
GetNetworkInsightsAccessScopeAnalysisFindingsPaginatorName = Literal["get_network_insights_access_scope_analysis_findings"]
GetSecurityGroupsForVpcPaginatorName = Literal["get_security_groups_for_vpc"]
GetSpotPlacementScoresPaginatorName = Literal["get_spot_placement_scores"]
GetTransitGatewayAttachmentPropagationsPaginatorName = Literal["get_transit_gateway_attachment_propagations"]
GetTransitGatewayMulticastDomainAssociationsPaginatorName = Literal["get_transit_gateway_multicast_domain_associations"]
GetTransitGatewayPolicyTableAssociationsPaginatorName = Literal["get_transit_gateway_policy_table_associations"]
GetTransitGatewayPrefixListReferencesPaginatorName = Literal["get_transit_gateway_prefix_list_references"]
GetTransitGatewayRouteTableAssociationsPaginatorName = Literal["get_transit_gateway_route_table_associations"]
GetTransitGatewayRouteTablePropagationsPaginatorName = Literal["get_transit_gateway_route_table_propagations"]
GetVpnConnectionDeviceTypesPaginatorName = Literal["get_vpn_connection_device_types"]
HostMaintenanceType = Literal["off", "on"]
HostRecoveryType = Literal["off", "on"]
HostTenancyType = Literal["dedicated", "default", "host"]
HostnameTypeType = Literal["ip-name", "resource-name"]
HttpTokensStateType = Literal["optional", "required"]
HypervisorTypeType = Literal["ovm", "xen"]
IamInstanceProfileAssociationStateType = Literal["associated", "associating", "disassociated", "disassociating"]
Igmpv2SupportValueType = Literal["disable", "enable"]
ImageAttributeNameType = Literal["blockDeviceMapping",
    "bootMode",
    "deregistrationProtection",
    "description",
    "imdsSupport",
    "kernel",
    "lastLaunchedTime",
    "launchPermission",
    "productCodes",
    "ramdisk",
    "sriovNetSupport",
    "tpmSupport",
    "uefiData",]
ImageAvailableWaiterName = Literal["image_available"]
ImageBlockPublicAccessDisabledStateType = Literal["unblocked"]
ImageBlockPublicAccessEnabledStateType = Literal["block-new-sharing"]
ImageExistsWaiterName = Literal["image_exists"]
ImageStateType = Literal["available", "deregistered", "disabled", "error", "failed", "invalid", "pending", "transient"]
ImageTypeValuesType = Literal["kernel", "machine", "ramdisk"]
ImdsSupportValuesType = Literal["v2.0"]
InstanceAttributeNameType = Literal["blockDeviceMapping",
    "disableApiStop",
    "disableApiTermination",
    "ebsOptimized",
    "enaSupport",
    "enclaveOptions",
    "groupSet",
    "instanceInitiatedShutdownBehavior",
    "instanceType",
    "kernel",
    "productCodes",
    "ramdisk",
    "rootDeviceName",
    "sourceDestCheck",
    "sriovNetSupport",
    "userData",]
InstanceAutoRecoveryStateType = Literal["default", "disabled"]
InstanceBootModeValuesType = Literal["legacy-bios", "uefi"]
InstanceEventWindowStateType = Literal["active", "creating", "deleted", "deleting"]
InstanceExistsWaiterName = Literal["instance_exists"]
InstanceGenerationType = Literal["current", "previous"]
InstanceHealthStatusType = Literal["healthy", "unhealthy"]
InstanceInterruptionBehaviorType = Literal["hibernate", "stop", "terminate"]
InstanceLifecycleType = Literal["on-demand", "spot"]
InstanceLifecycleTypeType = Literal["capacity-block", "scheduled", "spot"]
InstanceMatchCriteriaType = Literal["open", "targeted"]
InstanceMetadataEndpointStateType = Literal["disabled", "enabled"]
InstanceMetadataOptionsStateType = Literal["applied", "pending"]
InstanceMetadataProtocolStateType = Literal["disabled", "enabled"]
InstanceMetadataTagsStateType = Literal["disabled", "enabled"]
InstanceRunningWaiterName = Literal["instance_running"]
InstanceStateNameType = Literal["pending", "running", "shutting-down", "stopped", "stopping", "terminated"]
InstanceStatusOkWaiterName = Literal["instance_status_ok"]
InstanceStoppedWaiterName = Literal["instance_stopped"]
InstanceStorageEncryptionSupportType = Literal["required", "unsupported"]
InstanceTerminatedWaiterName = Literal["instance_terminated"]
InstanceTypeHypervisorType = Literal["nitro", "xen"]
InstanceTypeType = Literal["a1.2xlarge",
    "a1.4xlarge",
    "a1.large",
    "a1.medium",
    "a1.metal",
    "a1.xlarge",
    "c1.medium",
    "c1.xlarge",
    "c3.2xlarge",
    "c3.4xlarge",
    "c3.8xlarge",
    "c3.large",
    "c3.xlarge",
    "c4.2xlarge",
    "c4.4xlarge",
    "c4.8xlarge",
    "c4.large",
    "c4.xlarge",
    "c5.12xlarge",
    "c5.18xlarge",
    "c5.24xlarge",
    "c5.2xlarge",
    "c5.4xlarge",
    "c5.9xlarge",
    "c5.large",
    "c5.metal",
    "c5.xlarge",
    "c5a.12xlarge",
    "c5a.16xlarge",
    "c5a.24xlarge",
    "c5a.2xlarge",
    "c5a.4xlarge",
    "c5a.8xlarge",
    "c5a.large",
    "c5a.xlarge",
    "c5ad.12xlarge",
    "c5ad.16xlarge",
    "c5ad.24xlarge",
    "c5ad.2xlarge",
    "c5ad.4xlarge",
    "c5ad.8xlarge",
    "c5ad.large",
    "c5ad.xlarge",
    "c5d.12xlarge",
    "c5d.18xlarge",
    "c5d.24xlarge",
    "c5d.2xlarge",
    "c5d.4xlarge",
    "c5d.9xlarge",
    "c5d.large",
    "c5d.metal",
    "c5d.xlarge",
    "c5n.18xlarge",
    "c5n.2xlarge",
    "c5n.4xlarge",
    "c5n.9xlarge",
    "c5n.large",
    "c5n.metal",
    "c5n.xlarge",
    "c6a.12xlarge",
    "c6a.16xlarge",
    "c6a.24xlarge",
    "c6a.2xlarge",
    "c6a.32xlarge",
    "c6a.48xlarge",
    "c6a.4xlarge",
    "c6a.8xlarge",
    "c6a.large",
    "c6a.metal",
    "c6a.xlarge",
    "c6g.12xlarge",
    "c6g.16xlarge",
    "c6g.2xlarge",
    "c6g.4xlarge",
    "c6g.8xlarge",
    "c6g.large",
    "c6g.medium",
    "c6g.metal",
    "c6g.xlarge",
    "c6gd.12xlarge",
    "c6gd.16xlarge",
    "c6gd.2xlarge",
    "c6gd.4xlarge",
    "c6gd.8xlarge",
    "c6gd.large",
    "c6gd.medium",
    "c6gd.metal",
    "c6gd.xlarge",
    "c6gn.12xlarge",
    "c6gn.16xlarge",
    "c6gn.2xlarge",
    "c6gn.4xlarge",
    "c6gn.8xlarge",
    "c6gn.large",
    "c6gn.medium",
    "c6gn.xlarge",
    "c6i.12xlarge",
    "c6i.16xlarge",
    "c6i.24xlarge",
    "c6i.2xlarge",
    "c6i.32xlarge",
    "c6i.4xlarge",
    "c6i.8xlarge",
    "c6i.large",
    "c6i.metal",
    "c6i.xlarge",
    "c6id.12xlarge",
    "c6id.16xlarge",
    "c6id.24xlarge",
    "c6id.2xlarge",
    "c6id.32xlarge",
    "c6id.4xlarge",
    "c6id.8xlarge",
    "c6id.large",
    "c6id.metal",
    "c6id.xlarge",
    "c6in.12xlarge",
    "c6in.16xlarge",
    "c6in.24xlarge",
    "c6in.2xlarge",
    "c6in.32xlarge",
    "c6in.4xlarge",
    "c6in.8xlarge",
    "c6in.large",
    "c6in.metal",
    "c6in.xlarge",
    "c7a.12xlarge",
    "c7a.16xlarge",
    "c7a.24xlarge",
    "c7a.2xlarge",
    "c7a.32xlarge",
    "c7a.48xlarge",
    "c7a.4xlarge",
    "c7a.8xlarge",
    "c7a.large",
    "c7a.medium",
    "c7a.metal-48xl",
    "c7a.xlarge",
    "c7g.12xlarge",
    "c7g.16xlarge",
    "c7g.2xlarge",
    "c7g.4xlarge",
    "c7g.8xlarge",
    "c7g.large",
    "c7g.medium",
    "c7g.metal",
    "c7g.xlarge",
    "c7gd.12xlarge",
    "c7gd.16xlarge",
    "c7gd.2xlarge",
    "c7gd.4xlarge",
    "c7gd.8xlarge",
    "c7gd.large",
    "c7gd.medium",
    "c7gd.metal",
    "c7gd.xlarge",
    "c7gn.12xlarge",
    "c7gn.16xlarge",
    "c7gn.2xlarge",
    "c7gn.4xlarge",
    "c7gn.8xlarge",
    "c7gn.large",
    "c7gn.medium",
    "c7gn.metal",
    "c7gn.xlarge",
    "c7i-flex.2xlarge",
    "c7i-flex.4xlarge",
    "c7i-flex.8xlarge",
    "c7i-flex.large",
    "c7i-flex.xlarge",
    "c7i.12xlarge",
    "c7i.16xlarge",
    "c7i.24xlarge",
    "c7i.2xlarge",
    "c7i.48xlarge",
    "c7i.4xlarge",
    "c7i.8xlarge",
    "c7i.large",
    "c7i.metal-24xl",
    "c7i.metal-48xl",
    "c7i.xlarge",
    "cc1.4xlarge",
    "cc2.8xlarge",
    "cg1.4xlarge",
    "cr1.8xlarge",
    "d2.2xlarge",
    "d2.4xlarge",
    "d2.8xlarge",
    "d2.xlarge",
    "d3.2xlarge",
    "d3.4xlarge",
    "d3.8xlarge",
    "d3.xlarge",
    "d3en.12xlarge",
    "d3en.2xlarge",
    "d3en.4xlarge",
    "d3en.6xlarge",
    "d3en.8xlarge",
    "d3en.xlarge",
    "dl1.24xlarge",
    "dl2q.24xlarge",
    "f1.16xlarge",
    "f1.2xlarge",
    "f1.4xlarge",
    "g2.2xlarge",
    "g2.8xlarge",
    "g3.16xlarge",
    "g3.4xlarge",
    "g3.8xlarge",
    "g3s.xlarge",
    "g4ad.16xlarge",
    "g4ad.2xlarge",
    "g4ad.4xlarge",
    "g4ad.8xlarge",
    "g4ad.xlarge",
    "g4dn.12xlarge",
    "g4dn.16xlarge",
    "g4dn.2xlarge",
    "g4dn.4xlarge",
    "g4dn.8xlarge",
    "g4dn.metal",
    "g4dn.xlarge",
    "g5.12xlarge",
    "g5.16xlarge",
    "g5.24xlarge",
    "g5.2xlarge",
    "g5.48xlarge",
    "g5.4xlarge",
    "g5.8xlarge",
    "g5.xlarge",
    "g5g.16xlarge",
    "g5g.2xlarge",
    "g5g.4xlarge",
    "g5g.8xlarge",
    "g5g.metal",
    "g5g.xlarge",
    "g6.12xlarge",
    "g6.16xlarge",
    "g6.24xlarge",
    "g6.2xlarge",
    "g6.48xlarge",
    "g6.4xlarge",
    "g6.8xlarge",
    "g6.xlarge",
    "gr6.4xlarge",
    "gr6.8xlarge",
    "h1.16xlarge",
    "h1.2xlarge",
    "h1.4xlarge",
    "h1.8xlarge",
    "hi1.4xlarge",
    "hpc6a.48xlarge",
    "hpc6id.32xlarge",
    "hpc7a.12xlarge",
    "hpc7a.24xlarge",
    "hpc7a.48xlarge",
    "hpc7a.96xlarge",
    "hpc7g.16xlarge",
    "hpc7g.4xlarge",
    "hpc7g.8xlarge",
    "hs1.8xlarge",
    "i2.2xlarge",
    "i2.4xlarge",
    "i2.8xlarge",
    "i2.xlarge",
    "i3.16xlarge",
    "i3.2xlarge",
    "i3.4xlarge",
    "i3.8xlarge",
    "i3.large",
    "i3.metal",
    "i3.xlarge",
    "i3en.12xlarge",
    "i3en.24xlarge",
    "i3en.2xlarge",
    "i3en.3xlarge",
    "i3en.6xlarge",
    "i3en.large",
    "i3en.metal",
    "i3en.xlarge",
    "i4g.16xlarge",
    "i4g.2xlarge",
    "i4g.4xlarge",
    "i4g.8xlarge",
    "i4g.large",
    "i4g.xlarge",
    "i4i.12xlarge",
    "i4i.16xlarge",
    "i4i.24xlarge",
    "i4i.2xlarge",
    "i4i.32xlarge",
    "i4i.4xlarge",
    "i4i.8xlarge",
    "i4i.large",
    "i4i.metal",
    "i4i.xlarge",
    "im4gn.16xlarge",
    "im4gn.2xlarge",
    "im4gn.4xlarge",
    "im4gn.8xlarge",
    "im4gn.large",
    "im4gn.xlarge",
    "inf1.24xlarge",
    "inf1.2xlarge",
    "inf1.6xlarge",
    "inf1.xlarge",
    "inf2.24xlarge",
    "inf2.48xlarge",
    "inf2.8xlarge",
    "inf2.xlarge",
    "is4gen.2xlarge",
    "is4gen.4xlarge",
    "is4gen.8xlarge",
    "is4gen.large",
    "is4gen.medium",
    "is4gen.xlarge",
    "m1.large",
    "m1.medium",
    "m1.small",
    "m1.xlarge",
    "m2.2xlarge",
    "m2.4xlarge",
    "m2.xlarge",
    "m3.2xlarge",
    "m3.large",
    "m3.medium",
    "m3.xlarge",
    "m4.10xlarge",
    "m4.16xlarge",
    "m4.2xlarge",
    "m4.4xlarge",
    "m4.large",
    "m4.xlarge",
    "m5.12xlarge",
    "m5.16xlarge",
    "m5.24xlarge",
    "m5.2xlarge",
    "m5.4xlarge",
    "m5.8xlarge",
    "m5.large",
    "m5.metal",
    "m5.xlarge",
    "m5a.12xlarge",
    "m5a.16xlarge",
    "m5a.24xlarge",
    "m5a.2xlarge",
    "m5a.4xlarge",
    "m5a.8xlarge",
    "m5a.large",
    "m5a.xlarge",
    "m5ad.12xlarge",
    "m5ad.16xlarge",
    "m5ad.24xlarge",
    "m5ad.2xlarge",
    "m5ad.4xlarge",
    "m5ad.8xlarge",
    "m5ad.large",
    "m5ad.xlarge",
    "m5d.12xlarge",
    "m5d.16xlarge",
    "m5d.24xlarge",
    "m5d.2xlarge",
    "m5d.4xlarge",
    "m5d.8xlarge",
    "m5d.large",
    "m5d.metal",
    "m5d.xlarge",
    "m5dn.12xlarge",
    "m5dn.16xlarge",
    "m5dn.24xlarge",
    "m5dn.2xlarge",
    "m5dn.4xlarge",
    "m5dn.8xlarge",
    "m5dn.large",
    "m5dn.metal",
    "m5dn.xlarge",
    "m5n.12xlarge",
    "m5n.16xlarge",
    "m5n.24xlarge",
    "m5n.2xlarge",
    "m5n.4xlarge",
    "m5n.8xlarge",
    "m5n.large",
    "m5n.metal",
    "m5n.xlarge",
    "m5zn.12xlarge",
    "m5zn.2xlarge",
    "m5zn.3xlarge",
    "m5zn.6xlarge",
    "m5zn.large",
    "m5zn.metal",
    "m5zn.xlarge",
    "m6a.12xlarge",
    "m6a.16xlarge",
    "m6a.24xlarge",
    "m6a.2xlarge",
    "m6a.32xlarge",
    "m6a.48xlarge",
    "m6a.4xlarge",
    "m6a.8xlarge",
    "m6a.large",
    "m6a.metal",
    "m6a.xlarge",
    "m6g.12xlarge",
    "m6g.16xlarge",
    "m6g.2xlarge",
    "m6g.4xlarge",
    "m6g.8xlarge",
    "m6g.large",
    "m6g.medium",
    "m6g.metal",
    "m6g.xlarge",
    "m6gd.12xlarge",
    "m6gd.16xlarge",
    "m6gd.2xlarge",
    "m6gd.4xlarge",
    "m6gd.8xlarge",
    "m6gd.large",
    "m6gd.medium",
    "m6gd.metal",
    "m6gd.xlarge",
    "m6i.12xlarge",
    "m6i.16xlarge",
    "m6i.24xlarge",
    "m6i.2xlarge",
    "m6i.32xlarge",
    "m6i.4xlarge",
    "m6i.8xlarge",
    "m6i.large",
    "m6i.metal",
    "m6i.xlarge",
    "m6id.12xlarge",
    "m6id.16xlarge",
    "m6id.24xlarge",
    "m6id.2xlarge",
    "m6id.32xlarge",
    "m6id.4xlarge",
    "m6id.8xlarge",
    "m6id.large",
    "m6id.metal",
    "m6id.xlarge",
    "m6idn.12xlarge",
    "m6idn.16xlarge",
    "m6idn.24xlarge",
    "m6idn.2xlarge",
    "m6idn.32xlarge",
    "m6idn.4xlarge",
    "m6idn.8xlarge",
    "m6idn.large",
    "m6idn.metal",
    "m6idn.xlarge",
    "m6in.12xlarge",
    "m6in.16xlarge",
    "m6in.24xlarge",
    "m6in.2xlarge",
    "m6in.32xlarge",
    "m6in.4xlarge",
    "m6in.8xlarge",
    "m6in.large",
    "m6in.metal",
    "m6in.xlarge",
    "m7a.12xlarge",
    "m7a.16xlarge",
    "m7a.24xlarge",
    "m7a.2xlarge",
    "m7a.32xlarge",
    "m7a.48xlarge",
    "m7a.4xlarge",
    "m7a.8xlarge",
    "m7a.large",
    "m7a.medium",
    "m7a.metal-48xl",
    "m7a.xlarge",
    "m7g.12xlarge",
    "m7g.16xlarge",
    "m7g.2xlarge",
    "m7g.4xlarge",
    "m7g.8xlarge",
    "m7g.large",
    "m7g.medium",
    "m7g.metal",
    "m7g.xlarge",
    "m7gd.12xlarge",
    "m7gd.16xlarge",
    "m7gd.2xlarge",
    "m7gd.4xlarge",
    "m7gd.8xlarge",
    "m7gd.large",
    "m7gd.medium",
    "m7gd.metal",
    "m7gd.xlarge",
    "m7i-flex.2xlarge",
    "m7i-flex.4xlarge",
    "m7i-flex.8xlarge",
    "m7i-flex.large",
    "m7i-flex.xlarge",
    "m7i.12xlarge",
    "m7i.16xlarge",
    "m7i.24xlarge",
    "m7i.2xlarge",
    "m7i.48xlarge",
    "m7i.4xlarge",
    "m7i.8xlarge",
    "m7i.large",
    "m7i.metal-24xl",
    "m7i.metal-48xl",
    "m7i.xlarge",
    "mac1.metal",
    "mac2-m1ultra.metal",
    "mac2-m2.metal",
    "mac2-m2pro.metal",
    "mac2.metal",
    "p2.16xlarge",
    "p2.8xlarge",
    "p2.xlarge",
    "p3.16xlarge",
    "p3.2xlarge",
    "p3.8xlarge",
    "p3dn.24xlarge",
    "p4d.24xlarge",
    "p4de.24xlarge",
    "p5.48xlarge",
    "r3.2xlarge",
    "r3.4xlarge",
    "r3.8xlarge",
    "r3.large",
    "r3.xlarge",
    "r4.16xlarge",
    "r4.2xlarge",
    "r4.4xlarge",
    "r4.8xlarge",
    "r4.large",
    "r4.xlarge",
    "r5.12xlarge",
    "r5.16xlarge",
    "r5.24xlarge",
    "r5.2xlarge",
    "r5.4xlarge",
    "r5.8xlarge",
    "r5.large",
    "r5.metal",
    "r5.xlarge",
    "r5a.12xlarge",
    "r5a.16xlarge",
    "r5a.24xlarge",
    "r5a.2xlarge",
    "r5a.4xlarge",
    "r5a.8xlarge",
    "r5a.large",
    "r5a.xlarge",
    "r5ad.12xlarge",
    "r5ad.16xlarge",
    "r5ad.24xlarge",
    "r5ad.2xlarge",
    "r5ad.4xlarge",
    "r5ad.8xlarge",
    "r5ad.large",
    "r5ad.xlarge",
    "r5b.12xlarge",
    "r5b.16xlarge",
    "r5b.24xlarge",
    "r5b.2xlarge",
    "r5b.4xlarge",
    "r5b.8xlarge",
    "r5b.large",
    "r5b.metal",
    "r5b.xlarge",
    "r5d.12xlarge",
    "r5d.16xlarge",
    "r5d.24xlarge",
    "r5d.2xlarge",
    "r5d.4xlarge",
    "r5d.8xlarge",
    "r5d.large",
    "r5d.metal",
    "r5d.xlarge",
    "r5dn.12xlarge",
    "r5dn.16xlarge",
    "r5dn.24xlarge",
    "r5dn.2xlarge",
    "r5dn.4xlarge",
    "r5dn.8xlarge",
    "r5dn.large",
    "r5dn.metal",
    "r5dn.xlarge",
    "r5n.12xlarge",
    "r5n.16xlarge",
    "r5n.24xlarge",
    "r5n.2xlarge",
    "r5n.4xlarge",
    "r5n.8xlarge",
    "r5n.large",
    "r5n.metal",
    "r5n.xlarge",
    "r6a.12xlarge",
    "r6a.16xlarge",
    "r6a.24xlarge",
    "r6a.2xlarge",
    "r6a.32xlarge",
    "r6a.48xlarge",
    "r6a.4xlarge",
    "r6a.8xlarge",
    "r6a.large",
    "r6a.metal",
    "r6a.xlarge",
    "r6g.12xlarge",
    "r6g.16xlarge",
    "r6g.2xlarge",
    "r6g.4xlarge",
    "r6g.8xlarge",
    "r6g.large",
    "r6g.medium",
    "r6g.metal",
    "r6g.xlarge",
    "r6gd.12xlarge",
    "r6gd.16xlarge",
    "r6gd.2xlarge",
    "r6gd.4xlarge",
    "r6gd.8xlarge",
    "r6gd.large",
    "r6gd.medium",
    "r6gd.metal",
    "r6gd.xlarge",
    "r6i.12xlarge",
    "r6i.16xlarge",
    "r6i.24xlarge",
    "r6i.2xlarge",
    "r6i.32xlarge",
    "r6i.4xlarge",
    "r6i.8xlarge",
    "r6i.large",
    "r6i.metal",
    "r6i.xlarge",
    "r6id.12xlarge",
    "r6id.16xlarge",
    "r6id.24xlarge",
    "r6id.2xlarge",
    "r6id.32xlarge",
    "r6id.4xlarge",
    "r6id.8xlarge",
    "r6id.large",
    "r6id.metal",
    "r6id.xlarge",
    "r6idn.12xlarge",
    "r6idn.16xlarge",
    "r6idn.24xlarge",
    "r6idn.2xlarge",
    "r6idn.32xlarge",
    "r6idn.4xlarge",
    "r6idn.8xlarge",
    "r6idn.large",
    "r6idn.metal",
    "r6idn.xlarge",
    "r6in.12xlarge",
    "r6in.16xlarge",
    "r6in.24xlarge",
    "r6in.2xlarge",
    "r6in.32xlarge",
    "r6in.4xlarge",
    "r6in.8xlarge",
    "r6in.large",
    "r6in.metal",
    "r6in.xlarge",
    "r7a.12xlarge",
    "r7a.16xlarge",
    "r7a.24xlarge",
    "r7a.2xlarge",
    "r7a.32xlarge",
    "r7a.48xlarge",
    "r7a.4xlarge",
    "r7a.8xlarge",
    "r7a.large",
    "r7a.medium",
    "r7a.metal-48xl",
    "r7a.xlarge",
    "r7g.12xlarge",
    "r7g.16xlarge",
    "r7g.2xlarge",
    "r7g.4xlarge",
    "r7g.8xlarge",
    "r7g.large",
    "r7g.medium",
    "r7g.metal",
    "r7g.xlarge",
    "r7gd.12xlarge",
    "r7gd.16xlarge",
    "r7gd.2xlarge",
    "r7gd.4xlarge",
    "r7gd.8xlarge",
    "r7gd.large",
    "r7gd.medium",
    "r7gd.metal",
    "r7gd.xlarge",
    "r7i.12xlarge",
    "r7i.16xlarge",
    "r7i.24xlarge",
    "r7i.2xlarge",
    "r7i.48xlarge",
    "r7i.4xlarge",
    "r7i.8xlarge",
    "r7i.large",
    "r7i.metal-24xl",
    "r7i.metal-48xl",
    "r7i.xlarge",
    "r7iz.12xlarge",
    "r7iz.16xlarge",
    "r7iz.2xlarge",
    "r7iz.32xlarge",
    "r7iz.4xlarge",
    "r7iz.8xlarge",
    "r7iz.large",
    "r7iz.metal-16xl",
    "r7iz.metal-32xl",
    "r7iz.xlarge",
    "r8g.12xlarge",
    "r8g.16xlarge",
    "r8g.24xlarge",
    "r8g.2xlarge",
    "r8g.48xlarge",
    "r8g.4xlarge",
    "r8g.8xlarge",
    "r8g.large",
    "r8g.medium",
    "r8g.metal-24xl",
    "r8g.metal-48xl",
    "r8g.xlarge",
    "t1.micro",
    "t2.2xlarge",
    "t2.large",
    "t2.medium",
    "t2.micro",
    "t2.nano",
    "t2.small",
    "t2.xlarge",
    "t3.2xlarge",
    "t3.large",
    "t3.medium",
    "t3.micro",
    "t3.nano",
    "t3.small",
    "t3.xlarge",
    "t3a.2xlarge",
    "t3a.large",
    "t3a.medium",
    "t3a.micro",
    "t3a.nano",
    "t3a.small",
    "t3a.xlarge",
    "t4g.2xlarge",
    "t4g.large",
    "t4g.medium",
    "t4g.micro",
    "t4g.nano",
    "t4g.small",
    "t4g.xlarge",
    "trn1.2xlarge",
    "trn1.32xlarge",
    "trn1n.32xlarge",
    "u-12tb1.112xlarge",
    "u-12tb1.metal",
    "u-18tb1.112xlarge",
    "u-18tb1.metal",
    "u-24tb1.112xlarge",
    "u-24tb1.metal",
    "u-3tb1.56xlarge",
    "u-6tb1.112xlarge",
    "u-6tb1.56xlarge",
    "u-6tb1.metal",
    "u-9tb1.112xlarge",
    "u-9tb1.metal",
    "u7i-12tb.224xlarge",
    "u7ib-12tb.224xlarge",
    "u7in-16tb.224xlarge",
    "u7in-24tb.224xlarge",
    "u7in-32tb.224xlarge",
    "vt1.24xlarge",
    "vt1.3xlarge",
    "vt1.6xlarge",
    "x1.16xlarge",
    "x1.32xlarge",
    "x1e.16xlarge",
    "x1e.2xlarge",
    "x1e.32xlarge",
    "x1e.4xlarge",
    "x1e.8xlarge",
    "x1e.xlarge",
    "x2gd.12xlarge",
    "x2gd.16xlarge",
    "x2gd.2xlarge",
    "x2gd.4xlarge",
    "x2gd.8xlarge",
    "x2gd.large",
    "x2gd.medium",
    "x2gd.metal",
    "x2gd.xlarge",
    "x2idn.16xlarge",
    "x2idn.24xlarge",
    "x2idn.32xlarge",
    "x2idn.metal",
    "x2iedn.16xlarge",
    "x2iedn.24xlarge",
    "x2iedn.2xlarge",
    "x2iedn.32xlarge",
    "x2iedn.4xlarge",
    "x2iedn.8xlarge",
    "x2iedn.metal",
    "x2iedn.xlarge",
    "x2iezn.12xlarge",
    "x2iezn.2xlarge",
    "x2iezn.4xlarge",
    "x2iezn.6xlarge",
    "x2iezn.8xlarge",
    "x2iezn.metal",
    "z1d.12xlarge",
    "z1d.2xlarge",
    "z1d.3xlarge",
    "z1d.6xlarge",
    "z1d.large",
    "z1d.metal",
    "z1d.xlarge",]
InterfacePermissionTypeType = Literal["EIP-ASSOCIATE", "INSTANCE-ATTACH"]
InterfaceProtocolTypeType = Literal["GRE", "VLAN"]
InternetGatewayExistsWaiterName = Literal["internet_gateway_exists"]
IpAddressTypeType = Literal["dualstack", "ipv4", "ipv6"]
IpamAddressHistoryResourceTypeType = Literal["eip", "instance", "network-interface", "subnet", "vpc"]
IpamAssociatedResourceDiscoveryStatusType = Literal["active", "not-found"]
IpamComplianceStatusType = Literal["compliant", "ignored", "noncompliant", "unmanaged"]
IpamDiscoveryFailureCodeType = Literal["assume-role-failure", "throttling-failure", "unauthorized-failure"]
IpamManagementStateType = Literal["ignored", "managed", "unmanaged"]
IpamNetworkInterfaceAttachmentStatusType = Literal["available", "in-use"]
IpamOverlapStatusType = Literal["ignored", "nonoverlapping", "overlapping"]
IpamPoolAllocationResourceTypeType = Literal["custom", "ec2-public-ipv4-pool", "ipam-pool", "subnet", "vpc"]
IpamPoolAwsServiceType = Literal["ec2"]
IpamPoolCidrFailureCodeType = Literal["cidr-not-available", "limit-exceeded"]
IpamPoolCidrStateType = Literal["deprovisioned",
    "failed-deprovision",
    "failed-import",
    "failed-provision",
    "pending-deprovision",
    "pending-import",
    "pending-provision",
    "provisioned",]
IpamPoolPublicIpSourceType = Literal["amazon", "byoip"]
IpamPoolSourceResourceTypeType = Literal["vpc"]
IpamPoolStateType = Literal["create-complete",
    "create-failed",
    "create-in-progress",
    "delete-complete",
    "delete-failed",
    "delete-in-progress",
    "isolate-complete",
    "isolate-in-progress",
    "modify-complete",
    "modify-failed",
    "modify-in-progress",
    "restore-in-progress",]
IpamPublicAddressAssociationStatusType = Literal["associated", "disassociated"]
IpamPublicAddressAwsServiceType = Literal["database-migration-service",
    "elastic-container-service",
    "global-accelerator",
    "load-balancer",
    "nat-gateway",
    "other",
    "redshift",
    "relational-database-service",
    "site-to-site-vpn",]
IpamPublicAddressTypeType = Literal["amazon-owned-eip", "byoip", "ec2-public-ip", "service-managed-byoip", "service-managed-ip"]
IpamResourceDiscoveryAssociationStateType = Literal["associate-complete",
    "associate-failed",
    "associate-in-progress",
    "disassociate-complete",
    "disassociate-failed",
    "disassociate-in-progress",
    "isolate-complete",
    "isolate-in-progress",
    "restore-in-progress",]
IpamResourceDiscoveryStateType = Literal["create-complete",
    "create-failed",
    "create-in-progress",
    "delete-complete",
    "delete-failed",
    "delete-in-progress",
    "isolate-complete",
    "isolate-in-progress",
    "modify-complete",
    "modify-failed",
    "modify-in-progress",
    "restore-in-progress",]
IpamResourceTypeType = Literal["eip", "eni", "ipv6-pool", "public-ipv4-pool", "subnet", "vpc"]
IpamScopeStateType = Literal["create-complete",
    "create-failed",
    "create-in-progress",
    "delete-complete",
    "delete-failed",
    "delete-in-progress",
    "isolate-complete",
    "isolate-in-progress",
    "modify-complete",
    "modify-failed",
    "modify-in-progress",
    "restore-in-progress",]
IpamScopeTypeType = Literal["private", "public"]
IpamStateType = Literal["create-complete",
    "create-failed",
    "create-in-progress",
    "delete-complete",
    "delete-failed",
    "delete-in-progress",
    "isolate-complete",
    "isolate-in-progress",
    "modify-complete",
    "modify-failed",
    "modify-in-progress",
    "restore-in-progress",]
IpamTierType = Literal["advanced", "free"]
Ipv6SupportValueType = Literal["disable", "enable"]
KeyFormatType = Literal["pem", "ppk"]
KeyPairExistsWaiterName = Literal["key_pair_exists"]
KeyTypeType = Literal["ed25519", "rsa"]
LaunchTemplateAutoRecoveryStateType = Literal["default", "disabled"]
LaunchTemplateErrorCodeType = Literal["launchTemplateIdDoesNotExist",
    "launchTemplateIdMalformed",
    "launchTemplateNameDoesNotExist",
    "launchTemplateNameMalformed",
    "launchTemplateVersionDoesNotExist",
    "unexpectedError",]
LaunchTemplateHttpTokensStateType = Literal["optional", "required"]
LaunchTemplateInstanceMetadataEndpointStateType = Literal["disabled", "enabled"]
LaunchTemplateInstanceMetadataOptionsStateType = Literal["applied", "pending"]
LaunchTemplateInstanceMetadataProtocolIpv6Type = Literal["disabled", "enabled"]
LaunchTemplateInstanceMetadataTagsStateType = Literal["disabled", "enabled"]
ListImagesInRecycleBinPaginatorName = Literal["list_images_in_recycle_bin"]
ListSnapshotsInRecycleBinPaginatorName = Literal["list_snapshots_in_recycle_bin"]
ListingStateType = Literal["available", "cancelled", "pending", "sold"]
ListingStatusType = Literal["active", "cancelled", "closed", "pending"]
LocalGatewayRouteStateType = Literal["active", "blackhole", "deleted", "deleting", "pending"]
LocalGatewayRouteTableModeType = Literal["coip", "direct-vpc-routing"]
LocalGatewayRouteTypeType = Literal["propagated", "static"]
LocalStorageType = Literal["excluded", "included", "required"]
LocalStorageTypeType = Literal["hdd", "ssd"]
LocationTypeType = Literal["availability-zone", "availability-zone-id", "outpost", "region"]
LockModeType = Literal["compliance", "governance"]
LockStateType = Literal["compliance", "compliance-cooloff", "expired", "governance"]
LogDestinationTypeType = Literal["cloud-watch-logs", "kinesis-data-firehose", "s3"]
MarketTypeType = Literal["capacity-block", "spot"]
MembershipTypeType = Literal["igmp", "static"]
MetadataDefaultHttpTokensStateType = Literal["no-preference", "optional", "required"]
MetricTypeType = Literal["aggregate-latency"]
ModifyAvailabilityZoneOptInStatusType = Literal["not-opted-in", "opted-in"]
MonitoringStateType = Literal["disabled", "disabling", "enabled", "pending"]
MoveStatusType = Literal["movingToVpc", "restoringToClassic"]
MulticastSupportValueType = Literal["disable", "enable"]
NatGatewayAddressStatusType = Literal["assigning", "associating", "disassociating", "failed", "succeeded", "unassigning"]
NatGatewayAvailableWaiterName = Literal["nat_gateway_available"]
NatGatewayDeletedWaiterName = Literal["nat_gateway_deleted"]
NatGatewayStateType = Literal["available", "deleted", "deleting", "failed", "pending"]
NetworkInterfaceAttributeType = Literal["associatePublicIpAddress", "attachment", "description", "groupSet", "sourceDestCheck"]
NetworkInterfaceAvailableWaiterName = Literal["network_interface_available"]
NetworkInterfaceCreationTypeType = Literal["branch", "efa", "trunk"]
NetworkInterfacePermissionStateCodeType = Literal["granted", "pending", "revoked", "revoking"]
NetworkInterfaceStatusType = Literal["associated", "attaching", "available", "detaching", "in-use"]
NetworkInterfaceTypeType = Literal["api_gateway_managed",
    "aws_codestar_connections_managed",
    "branch",
    "efa",
    "gateway_load_balancer",
    "gateway_load_balancer_endpoint",
    "global_accelerator_managed",
    "interface",
    "iot_rules_managed",
    "lambda",
    "load_balancer",
    "natGateway",
    "network_load_balancer",
    "quicksight",
    "transit_gateway",
    "trunk",
    "vpc_endpoint",]
NitroEnclavesSupportType = Literal["supported", "unsupported"]
NitroTpmSupportType = Literal["supported", "unsupported"]
OfferingClassTypeType = Literal["convertible", "standard"]
OfferingTypeValuesType = Literal["All Upfront",
    "Heavy Utilization",
    "Light Utilization",
    "Medium Utilization",
    "No Upfront",
    "Partial Upfront",]
OnDemandAllocationStrategyType = Literal["lowestPrice", "prioritized"]
OperationTypeType = Literal["add", "remove"]
PartitionLoadFrequencyType = Literal["daily", "monthly", "none", "weekly"]
PasswordDataAvailableWaiterName = Literal["password_data_available"]
PayerResponsibilityType = Literal["ServiceOwner"]
PaymentOptionType = Literal["AllUpfront", "NoUpfront", "PartialUpfront"]
PeriodTypeType = Literal["fifteen-minutes", "five-minutes", "one-day", "one-hour", "one-week", "three-hours"]
PermissionGroupType = Literal["all"]
PhcSupportType = Literal["supported", "unsupported"]
PlacementGroupStateType = Literal["available", "deleted", "deleting", "pending"]
PlacementGroupStrategyType = Literal["cluster", "partition", "spread"]
PlacementStrategyType = Literal["cluster", "partition", "spread"]
PlatformValuesType = Literal["windows"]
PrefixListStateType = Literal["create-complete",
    "create-failed",
    "create-in-progress",
    "delete-complete",
    "delete-failed",
    "delete-in-progress",
    "modify-complete",
    "modify-failed",
    "modify-in-progress",
    "restore-complete",
    "restore-failed",
    "restore-in-progress",]
PrincipalTypeType = Literal["Account", "All", "OrganizationUnit", "Role", "Service", "User"]
ProductCodeValuesType = Literal["devpay", "marketplace"]
ProtocolType = Literal["tcp", "udp"]
ProtocolValueType = Literal["gre"]
RIProductDescriptionType = Literal["Linux/UNIX", "Linux/UNIX (Amazon VPC)", "Windows", "Windows (Amazon VPC)"]
RecurringChargeFrequencyType = Literal["Hourly"]
ReplaceRootVolumeTaskStateType = Literal["failed", "failed-detached", "failing", "in-progress", "pending", "succeeded"]
ReplacementStrategyType = Literal["launch", "launch-before-terminate"]
ReportInstanceReasonCodesType = Literal["instance-stuck-in-state",
    "not-accepting-credentials",
    "other",
    "password-not-available",
    "performance-ebs-volume",
    "performance-instance-store",
    "performance-network",
    "performance-other",
    "unresponsive",]
ReportStatusTypeType = Literal["impaired", "ok"]
ReservationStateType = Literal["active", "payment-failed", "payment-pending", "retired"]
ReservedInstanceStateType = Literal["active", "payment-failed", "payment-pending", "queued", "queued-deleted", "retired"]
ResetFpgaImageAttributeNameType = Literal["loadPermission"]
ResetImageAttributeNameType = Literal["launchPermission"]
ResourceTypeType = Literal["capacity-reservation",
    "capacity-reservation-fleet",
    "carrier-gateway",
    "client-vpn-endpoint",
    "coip-pool",
    "customer-gateway",
    "dedicated-host",
    "dhcp-options",
    "egress-only-internet-gateway",
    "elastic-gpu",
    "elastic-ip",
    "export-image-task",
    "export-instance-task",
    "fleet",
    "fpga-image",
    "host-reservation",
    "image",
    "import-image-task",
    "import-snapshot-task",
    "instance",
    "instance-connect-endpoint",
    "instance-event-window",
    "internet-gateway",
    "ipam",
    "ipam-pool",
    "ipam-resource-discovery",
    "ipam-resource-discovery-association",
    "ipam-scope",
    "ipv4pool-ec2",
    "ipv6pool-ec2",
    "key-pair",
    "launch-template",
    "local-gateway",
    "local-gateway-route-table",
    "local-gateway-route-table-virtual-interface-group-association",
    "local-gateway-route-table-vpc-association",
    "local-gateway-virtual-interface",
    "local-gateway-virtual-interface-group",
    "natgateway",
    "network-acl",
    "network-insights-access-scope",
    "network-insights-access-scope-analysis",
    "network-insights-analysis",
    "network-insights-path",
    "network-interface",
    "placement-group",
    "prefix-list",
    "replace-root-volume-task",
    "reserved-instances",
    "route-table",
    "security-group",
    "security-group-rule",
    "snapshot",
    "spot-fleet-request",
    "spot-instances-request",
    "subnet",
    "subnet-cidr-reservation",
    "traffic-mirror-filter",
    "traffic-mirror-filter-rule",
    "traffic-mirror-session",
    "traffic-mirror-target",
    "transit-gateway",
    "transit-gateway-attachment",
    "transit-gateway-connect-peer",
    "transit-gateway-multicast-domain",
    "transit-gateway-policy-table",
    "transit-gateway-route-table",
    "transit-gateway-route-table-announcement",
    "verified-access-endpoint",
    "verified-access-group",
    "verified-access-instance",
    "verified-access-policy",
    "verified-access-trust-provider",
    "volume",
    "vpc",
    "vpc-block-public-access-exclusion",
    "vpc-encryption-control",
    "vpc-endpoint",
    "vpc-endpoint-connection",
    "vpc-endpoint-connection-device-type",
    "vpc-endpoint-service",
    "vpc-endpoint-service-permission",
    "vpc-flow-log",
    "vpc-peering-connection",
    "vpn-connection",
    "vpn-connection-device-type",
    "vpn-gateway",]
RootDeviceTypeType = Literal["ebs", "instance-store"]
RouteOriginType = Literal["CreateRoute", "CreateRouteTable", "EnableVgwRoutePropagation"]
RouteStateType = Literal["active", "blackhole"]
RouteTableAssociationStateCodeType = Literal["associated", "associating", "disassociated", "disassociating", "failed"]
RuleActionType = Literal["allow", "deny"]
SSETypeType = Literal["none", "sse-ebs", "sse-kms"]
ScopeType = Literal["Availability Zone", "Region"]
SearchLocalGatewayRoutesPaginatorName = Literal["search_local_gateway_routes"]
SearchTransitGatewayMulticastGroupsPaginatorName = Literal["search_transit_gateway_multicast_groups"]
SecurityGroupExistsWaiterName = Literal["security_group_exists"]
SecurityGroupReferencingSupportValueType = Literal["disable", "enable"]
SelfServicePortalType = Literal["disabled", "enabled"]
ServiceConnectivityTypeType = Literal["ipv4", "ipv6"]
ServiceStateType = Literal["Available", "Deleted", "Deleting", "Failed", "Pending"]
ServiceTypeType = Literal["Gateway", "GatewayLoadBalancer", "Interface"]
ShutdownBehaviorType = Literal["stop", "terminate"]
SnapshotAttributeNameType = Literal["createVolumePermission", "productCodes"]
SnapshotBlockPublicAccessStateType = Literal["block-all-sharing", "block-new-sharing", "unblocked"]
SnapshotCompletedWaiterName = Literal["snapshot_completed"]
SnapshotImportedWaiterName = Literal["snapshot_imported"]
SnapshotStateType = Literal["completed", "error", "pending", "recoverable", "recovering"]
SpotAllocationStrategyType = Literal["capacity-optimized",
    "capacity-optimized-prioritized",
    "diversified",
    "lowest-price",
    "price-capacity-optimized",]
SpotInstanceInterruptionBehaviorType = Literal["hibernate", "stop", "terminate"]
SpotInstanceRequestFulfilledWaiterName = Literal["spot_instance_request_fulfilled"]
SpotInstanceStateType = Literal["active", "cancelled", "closed", "disabled", "failed", "open"]
SpotInstanceTypeType = Literal["one-time", "persistent"]
SpreadLevelType = Literal["host", "rack"]
StateType = Literal["Available",
    "Deleted",
    "Deleting",
    "Expired",
    "Failed",
    "Pending",
    "PendingAcceptance",
    "Rejected",]
StaticSourcesSupportValueType = Literal["disable", "enable"]
StatisticTypeType = Literal["p50"]
StatusNameType = Literal["reachability"]
StatusType = Literal["InClassic", "InVpc", "MoveInProgress"]
StatusTypeType = Literal["failed", "initializing", "insufficient-data", "passed"]
StorageTierType = Literal["archive", "standard"]
StoreImageTaskCompleteWaiterName = Literal["store_image_task_complete"]
SubnetAvailableWaiterName = Literal["subnet_available"]
SubnetCidrBlockStateCodeType = Literal["associated", "associating", "disassociated", "disassociating", "failed", "failing"]
SubnetCidrReservationTypeType = Literal["explicit", "prefix"]
SubnetStateType = Literal["available", "pending", "unavailable"]
SummaryStatusType = Literal["impaired", "initializing", "insufficient-data", "not-applicable", "ok"]
SupportedAdditionalProcessorFeatureType = Literal["amd-sev-snp"]
SystemStatusOkWaiterName = Literal["system_status_ok"]
TargetCapacityUnitTypeType = Literal["memory-mib", "units", "vcpu"]
TargetStorageTierType = Literal["archive"]
TelemetryStatusType = Literal["DOWN", "UP"]
TenancyType = Literal["dedicated", "default", "host"]
TieringOperationStatusType = Literal["archival-completed",
    "archival-failed",
    "archival-in-progress",
    "permanent-restore-completed",
    "permanent-restore-failed",
    "permanent-restore-in-progress",
    "temporary-restore-completed",
    "temporary-restore-failed",
    "temporary-restore-in-progress",]
TpmSupportValuesType = Literal["v2.0"]
TrafficDirectionType = Literal["egress", "ingress"]
TrafficMirrorFilterRuleFieldType = Literal["description", "destination-port-range", "protocol", "source-port-range"]
TrafficMirrorNetworkServiceType = Literal["amazon-dns"]
TrafficMirrorRuleActionType = Literal["accept", "reject"]
TrafficMirrorSessionFieldType = Literal["description", "packet-length", "virtual-network-id"]
TrafficMirrorTargetTypeType = Literal["gateway-load-balancer-endpoint", "network-interface", "network-load-balancer"]
TrafficTypeType = Literal["ACCEPT", "ALL", "REJECT"]
TransitGatewayAssociationStateType = Literal["associated", "associating", "disassociated", "disassociating"]
TransitGatewayAttachmentResourceTypeType = Literal["connect", "direct-connect-gateway", "peering", "tgw-peering", "vpc", "vpn"]
TransitGatewayAttachmentStateType = Literal["available",
    "deleted",
    "deleting",
    "failed",
    "failing",
    "initiating",
    "initiatingRequest",
    "modifying",
    "pending",
    "pendingAcceptance",
    "rejected",
    "rejecting",
    "rollingBack",]
TransitGatewayConnectPeerStateType = Literal["available", "deleted", "deleting", "pending"]
TransitGatewayMulitcastDomainAssociationStateType = Literal["associated",
    "associating",
    "disassociated",
    "disassociating",
    "failed",
    "pendingAcceptance",
    "rejected",]
TransitGatewayMulticastDomainStateType = Literal["available", "deleted", "deleting", "pending"]
TransitGatewayPolicyTableStateType = Literal["available", "deleted", "deleting", "pending"]
TransitGatewayPrefixListReferenceStateType = Literal["available", "deleting", "modifying", "pending"]
TransitGatewayPropagationStateType = Literal["disabled", "disabling", "enabled", "enabling"]
TransitGatewayRouteStateType = Literal["active", "blackhole", "deleted", "deleting", "pending"]
TransitGatewayRouteTableAnnouncementDirectionType = Literal["incoming", "outgoing"]
TransitGatewayRouteTableAnnouncementStateType = Literal["available", "deleted", "deleting", "failed", "failing", "pending"]
TransitGatewayRouteTableStateType = Literal["available", "deleted", "deleting", "pending"]
TransitGatewayRouteTypeType = Literal["propagated", "static"]
TransitGatewayStateType = Literal["available", "deleted", "deleting", "modifying", "pending"]
TransportProtocolType = Literal["tcp", "udp"]
TrustProviderTypeType = Literal["device", "user"]
TunnelInsideIpVersionType = Literal["ipv4", "ipv6"]
UnlimitedSupportedInstanceFamilyType = Literal["t2", "t3", "t3a", "t4g"]
UnsuccessfulInstanceCreditSpecificationErrorCodeType = Literal["IncorrectInstanceState",
    "InstanceCreditSpecification.NotSupported",
    "InvalidInstanceID.Malformed",
    "InvalidInstanceID.NotFound",]
UsageClassTypeType = Literal["capacity-block", "on-demand", "spot"]
UserTrustProviderTypeType = Literal["iam-identity-center", "oidc"]
VerifiedAccessEndpointAttachmentTypeType = Literal["vpc"]
VerifiedAccessEndpointProtocolType = Literal["http", "https"]
VerifiedAccessEndpointStatusCodeType = Literal["active", "deleted", "deleting", "pending", "updating"]
VerifiedAccessEndpointTypeType = Literal["load-balancer", "network-interface"]
VerifiedAccessLogDeliveryStatusCodeType = Literal["failed", "success"]
VirtualizationTypeType = Literal["hvm", "paravirtual"]
VolumeAttachmentStateType = Literal["attached", "attaching", "busy", "detached", "detaching"]
VolumeAttributeNameType = Literal["autoEnableIO", "productCodes"]
VolumeAvailableWaiterName = Literal["volume_available"]
VolumeDeletedWaiterName = Literal["volume_deleted"]
VolumeInUseWaiterName = Literal["volume_in_use"]
VolumeModificationStateType = Literal["completed", "failed", "modifying", "optimizing"]
VolumeStateType = Literal["available", "creating", "deleted", "deleting", "error", "in-use"]
VolumeStatusInfoStatusType = Literal["impaired", "insufficient-data", "ok"]
VolumeStatusNameType = Literal["io-enabled", "io-performance"]
VolumeTypeType = Literal["gp2", "gp3", "io1", "io2", "sc1", "st1", "standard"]
VpcAttributeNameType = Literal["enableDnsHostnames", "enableDnsSupport", "enableNetworkAddressUsageMetrics"]
VpcAvailableWaiterName = Literal["vpc_available"]
VpcCidrBlockStateCodeType = Literal["associated", "associating", "disassociated", "disassociating", "failed", "failing"]
VpcEndpointTypeType = Literal["Gateway", "GatewayLoadBalancer", "Interface"]
VpcExistsWaiterName = Literal["vpc_exists"]
VpcPeeringConnectionDeletedWaiterName = Literal["vpc_peering_connection_deleted"]
VpcPeeringConnectionExistsWaiterName = Literal["vpc_peering_connection_exists"]
VpcPeeringConnectionStateReasonCodeType = Literal["active",
    "deleted",
    "deleting",
    "expired",
    "failed",
    "initiating-request",
    "pending-acceptance",
    "provisioning",
    "rejected",]
VpcStateType = Literal["available", "pending"]
VpcTenancyType = Literal["default"]
VpnConnectionAvailableWaiterName = Literal["vpn_connection_available"]
VpnConnectionDeletedWaiterName = Literal["vpn_connection_deleted"]
VpnEcmpSupportValueType = Literal["disable", "enable"]
VpnProtocolType = Literal["openvpn"]
VpnStateType = Literal["available", "deleted", "deleting", "pending"]
VpnStaticRouteSourceType = Literal["Static"]
WeekDayType = Literal["friday", "monday", "saturday", "sunday", "thursday", "tuesday", "wednesday"]
EC2ServiceName = Literal["ec2"]
ServiceName = Literal["accessanalyzer",
    "account",
    "acm",
    "acm-pca",
    "amp",
    "amplify",
    "amplifybackend",
    "amplifyuibuilder",
    "apigateway",
    "apigatewaymanagementapi",
    "apigatewayv2",
    "appconfig",
    "appconfigdata",
    "appfabric",
    "appflow",
    "appintegrations",
    "application-autoscaling",
    "application-insights",
    "application-signals",
    "applicationcostprofiler",
    "appmesh",
    "apprunner",
    "appstream",
    "appsync",
    "apptest",
    "arc-zonal-shift",
    "artifact",
    "athena",
    "auditmanager",
    "autoscaling",
    "autoscaling-plans",
    "b2bi",
    "backup",
    "backup-gateway",
    "batch",
    "bcm-data-exports",
    "bedrock",
    "bedrock-agent",
    "bedrock-agent-runtime",
    "bedrock-runtime",
    "billingconductor",
    "braket",
    "budgets",
    "ce",
    "chatbot",
    "chime",
    "chime-sdk-identity",
    "chime-sdk-media-pipelines",
    "chime-sdk-meetings",
    "chime-sdk-messaging",
    "chime-sdk-voice",
    "cleanrooms",
    "cleanroomsml",
    "cloud9",
    "cloudcontrol",
    "clouddirectory",
    "cloudformation",
    "cloudfront",
    "cloudfront-keyvaluestore",
    "cloudhsm",
    "cloudhsmv2",
    "cloudsearch",
    "cloudsearchdomain",
    "cloudtrail",
    "cloudtrail-data",
    "cloudwatch",
    "codeartifact",
    "codebuild",
    "codecatalyst",
    "codecommit",
    "codeconnections",
    "codedeploy",
    "codeguru-reviewer",
    "codeguru-security",
    "codeguruprofiler",
    "codepipeline",
    "codestar",
    "codestar-connections",
    "codestar-notifications",
    "cognito-identity",
    "cognito-idp",
    "cognito-sync",
    "comprehend",
    "comprehendmedical",
    "compute-optimizer",
    "config",
    "connect",
    "connect-contact-lens",
    "connectcampaigns",
    "connectcases",
    "connectparticipant",
    "controlcatalog",
    "controltower",
    "cost-optimization-hub",
    "cur",
    "customer-profiles",
    "databrew",
    "dataexchange",
    "datapipeline",
    "datasync",
    "datazone",
    "dax",
    "deadline",
    "detective",
    "devicefarm",
    "devops-guru",
    "directconnect",
    "discovery",
    "dlm",
    "dms",
    "docdb",
    "docdb-elastic",
    "drs",
    "ds",
    "dynamodb",
    "dynamodbstreams",
    "ebs",
    "ec2",
    "ec2-instance-connect",
    "ecr",
    "ecr-public",
    "ecs",
    "efs",
    "eks",
    "eks-auth",
    "elastic-inference",
    "elasticache",
    "elasticbeanstalk",
    "elastictranscoder",
    "elb",
    "elbv2",
    "emr",
    "emr-containers",
    "emr-serverless",
    "entityresolution",
    "es",
    "events",
    "evidently",
    "finspace",
    "finspace-data",
    "firehose",
    "fis",
    "fms",
    "forecast",
    "forecastquery",
    "frauddetector",
    "freetier",
    "fsx",
    "gamelift",
    "glacier",
    "globalaccelerator",
    "glue",
    "grafana",
    "greengrass",
    "greengrassv2",
    "groundstation",
    "guardduty",
    "health",
    "healthlake",
    "iam",
    "identitystore",
    "imagebuilder",
    "importexport",
    "inspector",
    "inspector-scan",
    "inspector2",
    "internetmonitor",
    "iot",
    "iot-data",
    "iot-jobs-data",
    "iot1click-devices",
    "iot1click-projects",
    "iotanalytics",
    "iotdeviceadvisor",
    "iotevents",
    "iotevents-data",
    "iotfleethub",
    "iotfleetwise",
    "iotsecuretunneling",
    "iotsitewise",
    "iotthingsgraph",
    "iottwinmaker",
    "iotwireless",
    "ivs",
    "ivs-realtime",
    "ivschat",
    "kafka",
    "kafkaconnect",
    "kendra",
    "kendra-ranking",
    "keyspaces",
    "kinesis",
    "kinesis-video-archived-media",
    "kinesis-video-media",
    "kinesis-video-signaling",
    "kinesis-video-webrtc-storage",
    "kinesisanalytics",
    "kinesisanalyticsv2",
    "kinesisvideo",
    "kms",
    "lakeformation",
    "lambda",
    "launch-wizard",
    "lex-models",
    "lex-runtime",
    "lexv2-models",
    "lexv2-runtime",
    "license-manager",
    "license-manager-linux-subscriptions",
    "license-manager-user-subscriptions",
    "lightsail",
    "location",
    "logs",
    "lookoutequipment",
    "lookoutmetrics",
    "lookoutvision",
    "m2",
    "machinelearning",
    "macie2",
    "mailmanager",
    "managedblockchain",
    "managedblockchain-query",
    "marketplace-agreement",
    "marketplace-catalog",
    "marketplace-deployment",
    "marketplace-entitlement",
    "marketplacecommerceanalytics",
    "mediaconnect",
    "mediaconvert",
    "medialive",
    "mediapackage",
    "mediapackage-vod",
    "mediapackagev2",
    "mediastore",
    "mediastore-data",
    "mediatailor",
    "medical-imaging",
    "memorydb",
    "meteringmarketplace",
    "mgh",
    "mgn",
    "migration-hub-refactor-spaces",
    "migrationhub-config",
    "migrationhuborchestrator",
    "migrationhubstrategy",
    "mobile",
    "mq",
    "mturk",
    "mwaa",
    "neptune",
    "neptune-graph",
    "neptunedata",
    "network-firewall",
    "networkmanager",
    "networkmonitor",
    "nimble",
    "oam",
    "omics",
    "opensearch",
    "opensearchserverless",
    "opsworks",
    "opsworkscm",
    "organizations",
    "osis",
    "outposts",
    "panorama",
    "payment-cryptography",
    "payment-cryptography-data",
    "pca-connector-ad",
    "pca-connector-scep",
    "personalize",
    "personalize-events",
    "personalize-runtime",
    "pi",
    "pinpoint",
    "pinpoint-email",
    "pinpoint-sms-voice",
    "pinpoint-sms-voice-v2",
    "pipes",
    "polly",
    "pricing",
    "privatenetworks",
    "proton",
    "qapps",
    "qbusiness",
    "qconnect",
    "qldb",
    "qldb-session",
    "quicksight",
    "ram",
    "rbin",
    "rds",
    "rds-data",
    "redshift",
    "redshift-data",
    "redshift-serverless",
    "rekognition",
    "repostspace",
    "resiliencehub",
    "resource-explorer-2",
    "resource-groups",
    "resourcegroupstaggingapi",
    "robomaker",
    "rolesanywhere",
    "route53",
    "route53-recovery-cluster",
    "route53-recovery-control-config",
    "route53-recovery-readiness",
    "route53domains",
    "route53profiles",
    "route53resolver",
    "rum",
    "s3",
    "s3control",
    "s3outposts",
    "sagemaker",
    "sagemaker-a2i-runtime",
    "sagemaker-edge",
    "sagemaker-featurestore-runtime",
    "sagemaker-geospatial",
    "sagemaker-metrics",
    "sagemaker-runtime",
    "savingsplans",
    "scheduler",
    "schemas",
    "sdb",
    "secretsmanager",
    "securityhub",
    "securitylake",
    "serverlessrepo",
    "service-quotas",
    "servicecatalog",
    "servicecatalog-appregistry",
    "servicediscovery",
    "ses",
    "sesv2",
    "shield",
    "signer",
    "simspaceweaver",
    "sms",
    "sms-voice",
    "snow-device-management",
    "snowball",
    "sns",
    "sqs",
    "ssm",
    "ssm-contacts",
    "ssm-incidents",
    "ssm-sap",
    "sso",
    "sso-admin",
    "sso-oidc",
    "stepfunctions",
    "storagegateway",
    "sts",
    "supplychain",
    "support",
    "support-app",
    "swf",
    "synthetics",
    "taxsettings",
    "textract",
    "timestream-influxdb",
    "timestream-query",
    "timestream-write",
    "tnb",
    "transcribe",
    "transfer",
    "translate",
    "trustedadvisor",
    "verifiedpermissions",
    "voice-id",
    "vpc-lattice",
    "waf",
    "waf-regional",
    "wafv2",
    "wellarchitected",
    "wisdom",
    "workdocs",
    "worklink",
    "workmail",
    "workmailmessageflow",
    "workspaces",
    "workspaces-thin-client",
    "workspaces-web",
    "xray",]
ResourceServiceName = Literal["cloudformation",
    "cloudwatch",
    "dynamodb",
    "ec2",
    "glacier",
    "iam",
    "opsworks",
    "s3",
    "sns",
    "sqs",]
PaginatorName = Literal["describe_address_transfers",
    "describe_addresses_attribute",
    "describe_aws_network_performance_metric_subscriptions",
    "describe_byoip_cidrs",
    "describe_capacity_block_offerings",
    "describe_capacity_reservation_fleets",
    "describe_capacity_reservations",
    "describe_carrier_gateways",
    "describe_classic_link_instances",
    "describe_client_vpn_authorization_rules",
    "describe_client_vpn_connections",
    "describe_client_vpn_endpoints",
    "describe_client_vpn_routes",
    "describe_client_vpn_target_networks",
    "describe_coip_pools",
    "describe_dhcp_options",
    "describe_egress_only_internet_gateways",
    "describe_export_image_tasks",
    "describe_fast_launch_images",
    "describe_fast_snapshot_restores",
    "describe_fleets",
    "describe_flow_logs",
    "describe_fpga_images",
    "describe_host_reservation_offerings",
    "describe_host_reservations",
    "describe_hosts",
    "describe_iam_instance_profile_associations",
    "describe_images",
    "describe_import_image_tasks",
    "describe_import_snapshot_tasks",
    "describe_instance_connect_endpoints",
    "describe_instance_credit_specifications",
    "describe_instance_event_windows",
    "describe_instance_status",
    "describe_instance_topology",
    "describe_instance_type_offerings",
    "describe_instance_types",
    "describe_instances",
    "describe_internet_gateways",
    "describe_ipam_pools",
    "describe_ipam_resource_discoveries",
    "describe_ipam_resource_discovery_associations",
    "describe_ipam_scopes",
    "describe_ipams",
    "describe_ipv6_pools",
    "describe_launch_template_versions",
    "describe_launch_templates",
    "describe_local_gateway_route_table_virtual_interface_group_associations",
    "describe_local_gateway_route_table_vpc_associations",
    "describe_local_gateway_route_tables",
    "describe_local_gateway_virtual_interface_groups",
    "describe_local_gateway_virtual_interfaces",
    "describe_local_gateways",
    "describe_mac_hosts",
    "describe_managed_prefix_lists",
    "describe_moving_addresses",
    "describe_nat_gateways",
    "describe_network_acls",
    "describe_network_insights_access_scope_analyses",
    "describe_network_insights_access_scopes",
    "describe_network_insights_analyses",
    "describe_network_insights_paths",
    "describe_network_interface_permissions",
    "describe_network_interfaces",
    "describe_prefix_lists",
    "describe_principal_id_format",
    "describe_public_ipv4_pools",
    "describe_replace_root_volume_tasks",
    "describe_reserved_instances_modifications",
    "describe_reserved_instances_offerings",
    "describe_route_tables",
    "describe_scheduled_instance_availability",
    "describe_scheduled_instances",
    "describe_security_group_rules",
    "describe_security_groups",
    "describe_snapshot_tier_status",
    "describe_snapshots",
    "describe_spot_fleet_instances",
    "describe_spot_fleet_requests",
    "describe_spot_instance_requests",
    "describe_spot_price_history",
    "describe_stale_security_groups",
    "describe_store_image_tasks",
    "describe_subnets",
    "describe_tags",
    "describe_traffic_mirror_filters",
    "describe_traffic_mirror_sessions",
    "describe_traffic_mirror_targets",
    "describe_transit_gateway_attachments",
    "describe_transit_gateway_connect_peers",
    "describe_transit_gateway_connects",
    "describe_transit_gateway_multicast_domains",
    "describe_transit_gateway_peering_attachments",
    "describe_transit_gateway_policy_tables",
    "describe_transit_gateway_route_table_announcements",
    "describe_transit_gateway_route_tables",
    "describe_transit_gateway_vpc_attachments",
    "describe_transit_gateways",
    "describe_trunk_interface_associations",
    "describe_verified_access_endpoints",
    "describe_verified_access_groups",
    "describe_verified_access_instance_logging_configurations",
    "describe_verified_access_instances",
    "describe_verified_access_trust_providers",
    "describe_volume_status",
    "describe_volumes",
    "describe_volumes_modifications",
    "describe_vpc_classic_link_dns_support",
    "describe_vpc_endpoint_connection_notifications",
    "describe_vpc_endpoint_connections",
    "describe_vpc_endpoint_service_configurations",
    "describe_vpc_endpoint_service_permissions",
    "describe_vpc_endpoint_services",
    "describe_vpc_endpoints",
    "describe_vpc_peering_connections",
    "describe_vpcs",
    "get_associated_ipv6_pool_cidrs",
    "get_aws_network_performance_data",
    "get_groups_for_capacity_reservation",
    "get_instance_types_from_instance_requirements",
    "get_ipam_address_history",
    "get_ipam_discovered_accounts",
    "get_ipam_discovered_resource_cidrs",
    "get_ipam_pool_allocations",
    "get_ipam_pool_cidrs",
    "get_ipam_resource_cidrs",
    "get_managed_prefix_list_associations",
    "get_managed_prefix_list_entries",
    "get_network_insights_access_scope_analysis_findings",
    "get_security_groups_for_vpc",
    "get_spot_placement_scores",
    "get_transit_gateway_attachment_propagations",
    "get_transit_gateway_multicast_domain_associations",
    "get_transit_gateway_policy_table_associations",
    "get_transit_gateway_prefix_list_references",
    "get_transit_gateway_route_table_associations",
    "get_transit_gateway_route_table_propagations",
    "get_vpn_connection_device_types",
    "list_images_in_recycle_bin",
    "list_snapshots_in_recycle_bin",
    "search_local_gateway_routes",
    "search_transit_gateway_multicast_groups",]
WaiterName = Literal["bundle_task_complete",
    "conversion_task_cancelled",
    "conversion_task_completed",
    "conversion_task_deleted",
    "customer_gateway_available",
    "export_task_cancelled",
    "export_task_completed",
    "image_available",
    "image_exists",
    "instance_exists",
    "instance_running",
    "instance_status_ok",
    "instance_stopped",
    "instance_terminated",
    "internet_gateway_exists",
    "key_pair_exists",
    "nat_gateway_available",
    "nat_gateway_deleted",
    "network_interface_available",
    "password_data_available",
    "security_group_exists",
    "snapshot_completed",
    "snapshot_imported",
    "spot_instance_request_fulfilled",
    "store_image_task_complete",
    "subnet_available",
    "system_status_ok",
    "volume_available",
    "volume_deleted",
    "volume_in_use",
    "vpc_available",
    "vpc_exists",
    "vpc_peering_connection_deleted",
    "vpc_peering_connection_exists",
    "vpn_connection_available",
    "vpn_connection_deleted",]
RegionName = Literal["af-south-1",
    "ap-east-1",
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-northeast-3",
    "ap-south-1",
    "ap-south-2",
    "ap-southeast-1",
    "ap-southeast-2",
    "ap-southeast-3",
    "ap-southeast-4",
    "ca-central-1",
    "ca-west-1",
    "eu-central-1",
    "eu-central-2",
    "eu-north-1",
    "eu-south-1",
    "eu-south-2",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "il-central-1",
    "me-central-1",
    "me-south-1",
    "sa-east-1",
    "us-east-1",
    "us-east-2",
    "us-west-1",
    "us-west-2",]
TimestampTypeDef = Union[datetime, str]
BlobTypeDef = Union[str, bytes, IO[Any]]]
TagSpecificationUnionTypeDef = Union['TagSpecificationTypeDef', 'TagSpecificationExtraOutputTypeDef']
IpPermissionUnionTypeDef = Union['IpPermissionTypeDef', 'IpPermissionExtraExtraOutputTypeDef']
StorageUnionTypeDef = Union['StorageTypeDef', 'StorageOutputTypeDef']
InstanceNetworkInterfaceSpecificationUnionTypeDef = Union[   'InstanceNetworkInterfaceSpecificationTypeDef',   'InstanceNetworkInterfaceSpecificationExtraOutputTypeDef', ]
LaunchTemplateConfigUnionTypeDef = Union[   'LaunchTemplateConfigTypeDef', 'LaunchTemplateConfigExtraOutputTypeDef' ]
SpotFleetRequestConfigDataUnionTypeDef = Union[   'SpotFleetRequestConfigDataTypeDef', 'SpotFleetRequestConfigDataExtraOutputTypeDef' ]
