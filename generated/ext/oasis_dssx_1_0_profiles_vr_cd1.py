from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime

from generated.ext.oasis_dss_core_schema_v1_0_os import (
    AnyType,
    InternationalStringType,
    Result,
    TstInfo,
    VerificationTimeInfo,
    VerifyManifestResults,
)
from generated.ext.oasis_sstc_saml_schema_assertion_1_1 import (
    NameIdentifierType,
)
from generated.ext.saml_schema_assertion_2_0 import NameIDType
from generated.ext.tsl import (
    SchemeInformation,
    TrustServiceProviderList,
    TSLTagType,
)
from generated.ext.xad_es import (
    AttributeCertificateRefs,
    AttributeRevocationRefs,
    ClaimedRolesListType,
    CommitmentTypeIndication,
    CompleteCertificateRefs,
    CompleteRevocationRefs,
    CRLIdentifierType,
    DataObjectFormat,
    DigestAlgAndValueType,
    ObjectIdentifierType,
    OCSPIdentifierType,
    SignaturePolicyIdentifier,
    SignatureProductionPlace,
    SigningCertificate,
    SigningTime,
    UnsignedDataObjectProperties,
)
from generated.ext.xmldsig_core_schema import (
    CanonicalizationMethod,
    SignatureValue,
    X509Data,
    X509IssuerSerialType,
)

__NAMESPACE__ = (
    "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#"
)


@dataclass
class HashValueType:
    HashValue: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
            "format": "base16",
        },
    )
    HashedObject: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ReturnVerificationReport:
    class Meta:
        namespace = (
            "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#"
        )

    IncludeVerifier: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    IncludeCertificateValues: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    IncludeRevocationValues: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ExpandBinaryValues: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ReportDetailLevel: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ValidityPeriodType:
    NotBefore: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    NotAfter: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )


@dataclass
class EntityType:
    BaseCertificateID: Optional[X509IssuerSerialType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    Name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    Other: Optional[AnyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )


@dataclass
class IdentifierType:
    X509Data: Optional[X509Data] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    SAMLv1Identifier: Optional[NameIdentifierType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    SAMLv2Identifier: Optional[NameIDType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    Other: Optional[AnyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )


@dataclass
class TstContentType:
    TstInfo: Optional[TstInfo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
        },
    )
    Other: Optional[AnyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )


@dataclass
class VerificationResultType:
    ResultMajor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    ResultMinor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    ResultMessage: Optional[InternationalStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )


@dataclass
class AlgorithmValidityType:
    Algorithm: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    Parameters: Optional[AnyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    Suitability: Optional[VerificationResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )


@dataclass
class AttrCertIDType:
    Holder: Optional[EntityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    Issuer: Optional[EntityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    SerialNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )


@dataclass
class AttributeType:
    Type_value: Optional[VerificationResultType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    Value: List[AnyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )


@dataclass
class CertificatePathValidityType:
    PathValiditySummary: Optional[VerificationResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    CertificateIdentifier: Optional[X509IssuerSerialType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    PathValidityDetail: Optional[
        "CertificatePathValidityVerificationDetailType"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )


@dataclass
class ExtensionType:
    ExtnId: Optional[ObjectIdentifierType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    Critical: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    ExtnValue: Optional[AnyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    ExtensionOK: Optional[VerificationResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )


@dataclass
class ExtensionsType:
    Extension: List[ExtensionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )


@dataclass
class SignatureValidityType:
    SigMathOK: Optional[VerificationResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    SignatureAlgorithm: Optional[AlgorithmValidityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )


@dataclass
class AttributeCertificateContentType:
    Version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    Holder: Optional[EntityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    Issuer: Optional[EntityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    SignatureAlgorithm: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    SerialNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    AttCertValidityPeriod: Optional[ValidityPeriodType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    Attributes: Optional["AttributeCertificateContentType.Attributes"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    IssuerUniqueID: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "format": "base16",
        },
    )
    Extensions: Optional[ExtensionsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )

    @dataclass
    class Attributes:
        Attribute: List[AttributeType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            },
        )


@dataclass
class CRLContentType:
    Version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    Signature: Optional[VerificationResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    Issuer: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    ThisUpdate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    NextUpdate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    RevokedCertificates: Optional["CRLContentType.RevokedCertificates"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            },
        )
    )
    CrlExtensions: Optional[ExtensionsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )

    @dataclass
    class RevokedCertificates:
        UserCertificate: List[int] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
                "sequence": 1,
            },
        )
        RevocationDate: List[XmlDateTime] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
                "sequence": 1,
            },
        )
        CrlEntryExtensions: List[ExtensionsType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
                "sequence": 1,
            },
        )


@dataclass
class CertificateContentType:
    Version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    SerialNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    SignatureAlgorithm: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    Issuer: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    ValidityPeriod: Optional[ValidityPeriodType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    Subject: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    Extensions: Optional[ExtensionsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )


@dataclass
class SingleResponseType:
    CertID: Optional["SingleResponseType.CertID"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    CertStatus: Optional[VerificationResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    ThisUpdate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    NextUpdate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    SingleExtensions: Optional[ExtensionsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )

    @dataclass
    class CertID:
        HashAlgorithm: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
                "required": True,
            },
        )
        IssuerNameHash: Optional[bytes] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
                "required": True,
                "format": "base16",
            },
        )
        IssuerKeyHash: Optional[bytes] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
                "required": True,
                "format": "base16",
            },
        )
        SerialNumber: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
                "required": True,
            },
        )


@dataclass
class TimeStampValidityType:
    FormatOK: Optional[VerificationResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    TimeStampContent: Optional[TstContentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    MessageHashAlgorithm: Optional[AlgorithmValidityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    SignatureOK: Optional[SignatureValidityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    CertificatePathValidity: Optional[CertificatePathValidityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
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
class TrustStatusListValidityType:
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
    SignatureOK: Optional[SignatureValidityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
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
class ArchiveTimeStampValidityType:
    FormatOK: Optional[VerificationResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    DigestAlgorithm: Optional[AlgorithmValidityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    Attributes: Optional["ArchiveTimeStampValidityType.Attributes"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    ReducedHashTree: Optional[
        "ArchiveTimeStampValidityType.ReducedHashTree"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    TimeStamp: Optional[TimeStampValidityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
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
    class Attributes:
        Attribute: List[AttributeType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
                "min_occurs": 1,
            },
        )

    @dataclass
    class ReducedHashTree:
        PartialHashTree: List[
            "ArchiveTimeStampValidityType.ReducedHashTree.PartialHashTree"
        ] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
                "min_occurs": 1,
            },
        )

        @dataclass
        class PartialHashTree:
            HashValue: List[HashValueType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
                    "min_occurs": 1,
                },
            )


@dataclass
class AttributeCertificateValidityType:
    AttributeCertificateIdentifier: Optional[AttrCertIDType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    AttributeCertificateValue: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "format": "base64",
        },
    )
    AttributeCertificateContent: Optional[AttributeCertificateContentType] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            },
        )
    )
    SignatureOK: Optional[SignatureValidityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    CertificatePathValidity: Optional[CertificatePathValidityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )


@dataclass
class CRLValidityType:
    CRLIdentifier: Optional[CRLIdentifierType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    CRLValue: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "format": "base64",
        },
    )
    CRLContent: Optional[CRLContentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    SignatureOK: Optional[SignatureValidityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    CertificatePathValidity: Optional[CertificatePathValidityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
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
class IndividualTimeStampReport(TimeStampValidityType):
    class Meta:
        namespace = (
            "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#"
        )


@dataclass
class OCSPContentType:
    Version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    ResponderID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    producedAt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    Responses: Optional["OCSPContentType.Responses"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    ResponseExtensions: Optional[ExtensionsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )

    @dataclass
    class Responses:
        SingleResponse: List[SingleResponseType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            },
        )


@dataclass
class SignedDataObjectPropertiesType:
    DataObjectFormat: List[DataObjectFormat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    CommitmentTypeIndication: List[CommitmentTypeIndication] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    Reason: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    AllDataObjectsTimeStamp: List[TimeStampValidityType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    IndividualDataObjectsTimeStamp: List[TimeStampValidityType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class CertifiedRolesListType:
    AttributeCertificateValidity: List[AttributeCertificateValidityType] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
                "min_occurs": 1,
            },
        )
    )


@dataclass
class EvidenceRecordValidityType:
    FormatOK: Optional[VerificationResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    Version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    DigestAlgorithm: List[AlgorithmValidityType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    CryptoInfos: Optional["EvidenceRecordValidityType.CryptoInfos"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    EncryptionInfo: Optional["EvidenceRecordValidityType.EncryptionInfo"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            },
        )
    )
    ArchiveTimeStampSequence: Optional[
        "EvidenceRecordValidityType.ArchiveTimeStampSequence"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
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
    class CryptoInfos:
        Attribute: List[AttributeType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
                "min_occurs": 1,
            },
        )

    @dataclass
    class EncryptionInfo:
        EncryptionInfoType: Optional[AlgorithmValidityType] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
                "required": True,
            },
        )
        EncryptionInfoValue: Optional[AnyType] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
                "required": True,
            },
        )

    @dataclass
    class ArchiveTimeStampSequence:
        ArchiveTimeStampChain: List[
            "EvidenceRecordValidityType.ArchiveTimeStampSequence.ArchiveTimeStampChain"
        ] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            },
        )

        @dataclass
        class ArchiveTimeStampChain:
            ArchiveTimeStamp: List[ArchiveTimeStampValidityType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
                },
            )


@dataclass
class IndividualAttributeCertificateReport(AttributeCertificateValidityType):
    class Meta:
        namespace = (
            "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#"
        )


@dataclass
class IndividualCRLReport(CRLValidityType):
    class Meta:
        namespace = (
            "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#"
        )


@dataclass
class OCSPValidityType:
    OCSPIdentifier: Optional[OCSPIdentifierType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    OCSPValue: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "format": "base64",
        },
    )
    OCSPContent: Optional[OCSPContentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    SignatureOK: Optional[SignatureValidityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    CertificatePathValidity: Optional[CertificatePathValidityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
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
class CertificateStatusType:
    CertStatusOK: Optional[VerificationResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    RevocationInfo: Optional["CertificateStatusType.RevocationInfo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    RevocationEvidence: Optional[
        "CertificateStatusType.RevocationEvidence"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )

    @dataclass
    class RevocationInfo:
        RevocationDate: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
                "required": True,
            },
        )
        RevocationReason: Optional[VerificationResultType] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
                "required": True,
            },
        )

    @dataclass
    class RevocationEvidence:
        CRLValidity: Optional[CRLValidityType] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            },
        )
        CRLReference: Optional[CRLIdentifierType] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            },
        )
        OCSPValidity: Optional[OCSPValidityType] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            },
        )
        OCSPReference: Optional[OCSPIdentifierType] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            },
        )
        Other: Optional[AnyType] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            },
        )


@dataclass
class EvidenceRecordReport(EvidenceRecordValidityType):
    class Meta:
        namespace = (
            "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#"
        )


@dataclass
class IndividualOCSPReport(OCSPValidityType):
    class Meta:
        namespace = (
            "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#"
        )


@dataclass
class RevocationValuesType:
    CRLValues: Optional["RevocationValuesType.CRLValues"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    OCSPValues: Optional["RevocationValuesType.OCSPValues"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    OtherValues: Optional[AnyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class CRLValues:
        VerifiedCRL: List[CRLValidityType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
                "min_occurs": 1,
            },
        )

    @dataclass
    class OCSPValues:
        VerifiedOCSPResponse: List[OCSPValidityType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
                "min_occurs": 1,
            },
        )


@dataclass
class SignerRoleType:
    ClaimedRoles: Optional[ClaimedRolesListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    CertifiedRoles: Optional[CertifiedRolesListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )


@dataclass
class CertificateValidityType:
    CertificateIdentifier: Optional[X509IssuerSerialType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    Subject: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    ChainingOK: Optional[VerificationResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    ValidityPeriodOK: Optional[VerificationResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    ExtensionsOK: Optional[VerificationResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    CertificateValue: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "format": "base64",
        },
    )
    CertificateContent: Optional[CertificateContentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    SignatureOK: Optional[SignatureValidityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    CertificateStatus: Optional[CertificateStatusType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )


@dataclass
class SignedSignaturePropertiesType:
    SigningTime: Optional[SigningTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    SigningCertificate: Optional[SigningCertificate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    SignaturePolicyIdentifier: Optional[SignaturePolicyIdentifier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    SignatureProductionPlace: Optional[SignatureProductionPlace] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    Location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    SignerRole: Optional[SignerRoleType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )


@dataclass
class CertificatePathValidityVerificationDetailType:
    CertificateValidity: List[CertificateValidityType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    TSLValidity: Optional[TrustStatusListValidityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    TrustAnchor: Optional[VerificationResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )


@dataclass
class CertificateValuesType:
    EncapsulatedX509Certificate: List[CertificateValidityType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    OtherCertificate: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class IndividualCertificateReport(CertificateValidityType):
    class Meta:
        namespace = (
            "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#"
        )


@dataclass
class SignedPropertiesType:
    SignedSignatureProperties: Optional[SignedSignaturePropertiesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    SignedDataObjectProperties: Optional[SignedDataObjectPropertiesType] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            },
        )
    )
    Other: Optional[AnyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SignedObjectIdentifierType:
    DigestAlgAndValue: Optional[DigestAlgAndValueType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    CanonicalizationMethod: Optional[CanonicalizationMethod] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    SignedProperties: Optional[SignedPropertiesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    SignatureValue: Optional[SignatureValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    Other: Optional[AnyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    WhichDocument: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    XPath: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    Offset: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    FieldName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class UnsignedSignaturePropertiesType:
    CounterSignature: List[SignatureValidityType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    SignatureTimeStamp: List[TimeStampValidityType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    CompleteCertificateRefs: List[CompleteCertificateRefs] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    CompleteRevocationRefs: List[CompleteRevocationRefs] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    AttributeCertificateRefs: List[AttributeCertificateRefs] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    AttributeRevocationRefs: List[AttributeRevocationRefs] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    SigAndRefsTimeStamp: List[TimeStampValidityType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    RefsOnlyTimeStamp: List[TimeStampValidityType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    CertificateValues: List[CertificateValuesType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    RevocationValues: List[RevocationValuesType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    AttrAuthoritiesCertValues: List[CertificateValuesType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    AttributeRevocationValues: List[RevocationValuesType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    ArchiveTimeStamp: List[TimeStampValidityType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class IndividualReportType:
    SignedObjectIdentifier: Optional[SignedObjectIdentifierType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    Result: Optional[Result] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
            "required": True,
        },
    )
    Details: Optional[AnyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )


@dataclass
class UnsignedPropertiesType:
    UnsignedSignatureProperties: Optional[UnsignedSignaturePropertiesType] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            },
        )
    )
    UnsignedDataObjectProperties: Optional[UnsignedDataObjectProperties] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            },
        )
    )
    Other: Optional[AnyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class PropertiesType:
    SignedProperties: Optional[SignedPropertiesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    UnsignedProperties: Optional[UnsignedPropertiesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    Target: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class VerificationReportType:
    VerificationTimeInfo: Optional[VerificationTimeInfo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
        },
    )
    VerifierIdentity: Optional[IdentifierType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    IndividualReport: List[IndividualReportType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )


@dataclass
class DetailedSignatureReportType:
    FormatOK: Optional[VerificationResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    Properties: Optional[PropertiesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    VerifyManifestResults: Optional[VerifyManifestResults] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
        },
    )
    SignatureHasVisibleContent: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
        },
    )
    SignatureOK: Optional[SignatureValidityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )
    CertificatePathValidity: Optional[CertificatePathValidityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            "required": True,
        },
    )


@dataclass
class VerificationReport(VerificationReportType):
    class Meta:
        namespace = (
            "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#"
        )


@dataclass
class DetailedSignatureReport(DetailedSignatureReportType):
    class Meta:
        namespace = (
            "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#"
        )
