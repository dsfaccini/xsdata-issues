from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime

from generated.ext.xmldsig_core_schema import (
    KeyValue,
    Signature,
)

__NAMESPACE__ = "http://uri.etsi.org/02231/v2#"


@dataclass
class AnyType:
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class ElectronicAddressType:
    URI: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "min_occurs": 1,
            "min_length": 1,
        },
    )


@dataclass
class ExpiredCertsRevocationInfo:
    class Meta:
        namespace = "http://uri.etsi.org/02231/v2#"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class MultiLangNormStringType:
    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
            "required": True,
        },
    )


@dataclass
class MultiLangStringType:
    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
            "required": True,
        },
    )


@dataclass
class NextUpdateType:
    dateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
        },
    )


@dataclass
class NonEmptyMultiLangURIType:
    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
            "required": True,
        },
    )


@dataclass
class NonEmptyURIListType:
    URI: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "min_occurs": 1,
            "min_length": 1,
        },
    )


@dataclass
class PostalAddressType:
    StreetAddress: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
            "min_length": 1,
        },
    )
    Locality: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
            "min_length": 1,
        },
    )
    StateOrProvince: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "min_length": 1,
        },
    )
    PostalCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "min_length": 1,
        },
    )
    CountryName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
            "min_length": 1,
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
            "required": True,
        },
    )


@dataclass
class SchemeTerritory:
    class Meta:
        namespace = "http://uri.etsi.org/02231/v2#"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "length": 2,
        },
    )


@dataclass
class ServiceStatus:
    class Meta:
        namespace = "http://uri.etsi.org/02231/v2#"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        },
    )


@dataclass
class ServiceSupplyPointsType:
    ServiceSupplyPoint: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "min_occurs": 1,
            "min_length": 1,
        },
    )


@dataclass
class ServiceTypeIdentifier:
    class Meta:
        namespace = "http://uri.etsi.org/02231/v2#"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        },
    )


class TSLTagType(Enum):
    HTTP_URI_ETSI_ORG_02231_TSLTAG = "http://uri.etsi.org/02231/TSLTag"


@dataclass
class TSLType:
    class Meta:
        namespace = "http://uri.etsi.org/02231/v2#"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        },
    )


@dataclass
class AdditionalInformationType:
    TextualInformation: List[MultiLangStringType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
        },
    )
    OtherInformation: List[AnyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
        },
    )


@dataclass
class AdditionalServiceInformationType:
    URI: Optional[NonEmptyMultiLangURIType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
        },
    )
    InformationValue: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
        },
    )
    OtherInformation: Optional[AnyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
        },
    )


@dataclass
class DigitalIdentityType:
    X509Certificate: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "format": "base64",
        },
    )
    X509SubjectName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
        },
    )
    KeyValue: Optional[KeyValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    X509SKI: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "format": "base64",
        },
    )
    Other: Optional[AnyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
        },
    )


@dataclass
class DistributionPoints(ElectronicAddressType):
    class Meta:
        namespace = "http://uri.etsi.org/02231/v2#"


@dataclass
class ElectronicAddress(ElectronicAddressType):
    class Meta:
        namespace = "http://uri.etsi.org/02231/v2#"


@dataclass
class ExtensionType(AnyType):
    Critical: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class InternationalNamesType:
    Name: List[MultiLangNormStringType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "min_occurs": 1,
        },
    )


@dataclass
class NextUpdate(NextUpdateType):
    class Meta:
        namespace = "http://uri.etsi.org/02231/v2#"


@dataclass
class NonEmptyMultiLangURIListType:
    URI: List[NonEmptyMultiLangURIType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "min_occurs": 1,
        },
    )


@dataclass
class PolicyOrLegalnoticeType:
    TSLPolicy: List[NonEmptyMultiLangURIType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
        },
    )
    TSLLegalNotice: List[MultiLangStringType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
        },
    )


@dataclass
class PostalAddress(PostalAddressType):
    class Meta:
        namespace = "http://uri.etsi.org/02231/v2#"


@dataclass
class SchemeTypeCommunityRules(NonEmptyURIListType):
    class Meta:
        namespace = "http://uri.etsi.org/02231/v2#"


@dataclass
class ServiceSupplyPoints(ServiceSupplyPointsType):
    class Meta:
        namespace = "http://uri.etsi.org/02231/v2#"


@dataclass
class AdditionalInformation(AdditionalInformationType):
    class Meta:
        namespace = "http://uri.etsi.org/02231/v2#"


@dataclass
class AdditionalServiceInformation(AdditionalServiceInformationType):
    class Meta:
        namespace = "http://uri.etsi.org/02231/v2#"


@dataclass
class DigitalIdentityListType:
    DigitalId: List[DigitalIdentityType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
        },
    )


@dataclass
class Extension(ExtensionType):
    class Meta:
        namespace = "http://uri.etsi.org/02231/v2#"


@dataclass
class PolicyOrLegalNotice(PolicyOrLegalnoticeType):
    class Meta:
        namespace = "http://uri.etsi.org/02231/v2#"


@dataclass
class PostalAddressListType:
    PostalAddress: List[PostalAddress] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "min_occurs": 1,
        },
    )


@dataclass
class SchemeInformationURI(NonEmptyMultiLangURIListType):
    class Meta:
        namespace = "http://uri.etsi.org/02231/v2#"


@dataclass
class SchemeName(InternationalNamesType):
    class Meta:
        namespace = "http://uri.etsi.org/02231/v2#"


@dataclass
class SchemeOperatorName(InternationalNamesType):
    class Meta:
        namespace = "http://uri.etsi.org/02231/v2#"


@dataclass
class ExtensionsListType:
    Extension: List[Extension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "min_occurs": 1,
        },
    )


@dataclass
class PostalAddresses(PostalAddressListType):
    class Meta:
        namespace = "http://uri.etsi.org/02231/v2#"


@dataclass
class ServiceDigitalIdentity(DigitalIdentityListType):
    class Meta:
        namespace = "http://uri.etsi.org/02231/v2#"


@dataclass
class AddressType:
    PostalAddresses: Optional[PostalAddresses] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
        },
    )
    ElectronicAddress: Optional[ElectronicAddress] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
        },
    )


@dataclass
class ServiceDigitalIdentityListType:
    ServiceDigitalIdentity: List[ServiceDigitalIdentity] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "min_occurs": 1,
        },
    )


@dataclass
class ServiceHistoryInstanceType:
    ServiceTypeIdentifier: Optional[ServiceTypeIdentifier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
        },
    )
    ServiceName: Optional[InternationalNamesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
        },
    )
    ServiceDigitalIdentity: Optional[ServiceDigitalIdentity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
        },
    )
    ServiceStatus: Optional[ServiceStatus] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
        },
    )
    StatusStartingTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
        },
    )
    ServiceInformationExtensions: Optional[ExtensionsListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
        },
    )


@dataclass
class TSPServiceInformationType:
    ServiceTypeIdentifier: Optional[ServiceTypeIdentifier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
        },
    )
    ServiceName: Optional[InternationalNamesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
        },
    )
    ServiceDigitalIdentity: Optional[ServiceDigitalIdentity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
        },
    )
    ServiceStatus: Optional[ServiceStatus] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
        },
    )
    StatusStartingTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
        },
    )
    SchemeServiceDefinitionURI: Optional[NonEmptyMultiLangURIListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
        },
    )
    ServiceSupplyPoints: Optional[ServiceSupplyPoints] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
        },
    )
    TSPServiceDefinitionURI: Optional[NonEmptyMultiLangURIListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
        },
    )
    ServiceInformationExtensions: Optional[ExtensionsListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
        },
    )


@dataclass
class ServiceDigitalIdentities(ServiceDigitalIdentityListType):
    class Meta:
        namespace = "http://uri.etsi.org/02231/v2#"


@dataclass
class ServiceHistoryInstance(ServiceHistoryInstanceType):
    class Meta:
        namespace = "http://uri.etsi.org/02231/v2#"


@dataclass
class ServiceInformation(TSPServiceInformationType):
    class Meta:
        namespace = "http://uri.etsi.org/02231/v2#"


@dataclass
class TSPInformationType:
    TSPName: Optional[InternationalNamesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
        },
    )
    TSPTradeName: Optional[InternationalNamesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
        },
    )
    TSPAddress: Optional[AddressType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
        },
    )
    TSPInformationURI: Optional[NonEmptyMultiLangURIListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
        },
    )
    TSPInformationExtensions: Optional[ExtensionsListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
        },
    )


@dataclass
class OtherTSLPointerType:
    ServiceDigitalIdentities: Optional[ServiceDigitalIdentities] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
        },
    )
    TSLLocation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
            "min_length": 1,
        },
    )
    AdditionalInformation: Optional[AdditionalInformation] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
        },
    )


@dataclass
class ServiceHistoryType:
    ServiceHistoryInstance: List[ServiceHistoryInstance] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
        },
    )


@dataclass
class TSPInformation(TSPInformationType):
    class Meta:
        namespace = "http://uri.etsi.org/02231/v2#"


@dataclass
class OtherTSLPointer(OtherTSLPointerType):
    class Meta:
        namespace = "http://uri.etsi.org/02231/v2#"


@dataclass
class ServiceHistory(ServiceHistoryType):
    class Meta:
        namespace = "http://uri.etsi.org/02231/v2#"


@dataclass
class OtherTSLPointersType:
    OtherTSLPointer: List[OtherTSLPointer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "min_occurs": 1,
        },
    )


@dataclass
class TSPServiceType:
    ServiceInformation: Optional[ServiceInformation] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
        },
    )
    ServiceHistory: Optional[ServiceHistory] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
        },
    )


@dataclass
class PointersToOtherTSL(OtherTSLPointersType):
    class Meta:
        namespace = "http://uri.etsi.org/02231/v2#"


@dataclass
class TSPService(TSPServiceType):
    class Meta:
        namespace = "http://uri.etsi.org/02231/v2#"


@dataclass
class TSLSchemeInformationType:
    TSLVersionIdentifier: int = field(
        init=False,
        default=3,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
        },
    )
    TSLSequenceNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
        },
    )
    TSLType: Optional[TSLType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
        },
    )
    SchemeOperatorName: Optional[SchemeOperatorName] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
        },
    )
    SchemeOperatorAddress: Optional[AddressType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
        },
    )
    SchemeName: Optional[SchemeName] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
        },
    )
    SchemeInformationURI: Optional[SchemeInformationURI] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
        },
    )
    StatusDeterminationApproach: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
            "min_length": 1,
        },
    )
    SchemeTypeCommunityRules: Optional[SchemeTypeCommunityRules] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
        },
    )
    SchemeTerritory: Optional[SchemeTerritory] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
        },
    )
    PolicyOrLegalNotice: Optional[PolicyOrLegalNotice] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
        },
    )
    HistoricalInformationPeriod: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
        },
    )
    PointersToOtherTSL: Optional[PointersToOtherTSL] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
        },
    )
    ListIssueDateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
        },
    )
    NextUpdate: Optional[NextUpdate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
        },
    )
    DistributionPoints: Optional[DistributionPoints] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
        },
    )
    SchemeExtensions: Optional[ExtensionsListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
        },
    )


@dataclass
class TSPServicesListType:
    TSPService: List[TSPService] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "min_occurs": 1,
        },
    )


@dataclass
class SchemeInformation(TSLSchemeInformationType):
    class Meta:
        namespace = "http://uri.etsi.org/02231/v2#"


@dataclass
class TSPServices(TSPServicesListType):
    class Meta:
        namespace = "http://uri.etsi.org/02231/v2#"


@dataclass
class TSPType:
    TSPInformation: Optional[TSPInformation] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
        },
    )
    TSPServices: Optional[TSPServices] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
        },
    )


@dataclass
class TrustServiceProvider(TSPType):
    class Meta:
        namespace = "http://uri.etsi.org/02231/v2#"


@dataclass
class TrustServiceProviderListType:
    TrustServiceProvider: List[TrustServiceProvider] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "min_occurs": 1,
        },
    )


@dataclass
class TrustServiceProviderList(TrustServiceProviderListType):
    class Meta:
        namespace = "http://uri.etsi.org/02231/v2#"


@dataclass
class TrustStatusListType:
    SchemeInformation: Optional[SchemeInformation] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
            "required": True,
        },
    )
    TrustServiceProviderList: Optional[TrustServiceProviderList] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/02231/v2#",
        },
    )
    Signature: Optional[Signature] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    TSLTag: Optional[TSLTagType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TrustServiceStatusList(TrustStatusListType):
    class Meta:
        namespace = "http://uri.etsi.org/02231/v2#"
