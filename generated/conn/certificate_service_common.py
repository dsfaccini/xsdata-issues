from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

__NAMESPACE__ = "http://ws.gematik.de/conn/CertificateServiceCommon/v2.0"


class CertRefEnum(Enum):
    C_AUT = "C.AUT"
    C_ENC = "C.ENC"
    C_SIG = "C.SIG"
    C_QES = "C.QES"


class CheckCertificateDetailEnum(Enum):
    CERT_SIG_ERROR = "CERT_SIG_ERROR"
    BUILD_CHAIN_FAILED = "BUILD_CHAIN_FAILED"
    CHECK_REVOCATION_FAILED = "CHECK_REVOCATION_FAILED"
    CERT_REVOKED = "CERT_REVOKED"
    CERT_EXPIRED = "CERT_EXPIRED"
    CERT_BAD_FORMAT = "CERT_BAD_FORMAT"
    POLICY_ERROR = "POLICY_ERROR"
    QC_STATEMENT_ERROR = "QC_STATEMENT_ERROR"
    WRONG_ROLE = "WRONG_ROLE"
    UNKNOWN_CRITICAL_EXTENSIONS = "UNKNOWN_CRITICAL_EXTENSIONS"
    CERT_REVOKED_AFTER = "CERT_REVOKED_AFTER"
    NO_REVOCATION_CHECK = "NO_REVOCATION_CHECK"
    TSL_OUT_OF_DATE = "TSL_OUT_OF_DATE"
    QUALIFIED = "QUALIFIED"


@dataclass
class X509Certificate:
    class Meta:
        namespace = "http://ws.gematik.de/conn/CertificateServiceCommon/v2.0"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "format": "base64",
        },
    )


@dataclass
class CheckCertificateDetailsType:
    CheckCertificateDetail: List[CheckCertificateDetailEnum] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://ws.gematik.de/conn/CertificateServiceCommon/v2.0",
        },
    )


@dataclass
class X509DataInfoListType:
    X509DataInfo: List["X509DataInfoListType.X509DataInfo"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://ws.gematik.de/conn/CertificateServiceCommon/v2.0",
            "min_occurs": 1,
        },
    )

    @dataclass
    class X509DataInfo:
        CertRef: Optional[CertRefEnum] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.gematik.de/conn/CertificateServiceCommon/v2.0",
                "required": True,
            },
        )
        X509Data: Optional["X509DataInfoListType.X509DataInfo.X509Data"] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://ws.gematik.de/conn/CertificateServiceCommon/v2.0",
                },
            )
        )

        @dataclass
        class X509Data:
            X509IssuerSerial: Optional[
                "X509DataInfoListType.X509DataInfo.X509Data.X509IssuerSerial"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://ws.gematik.de/conn/CertificateServiceCommon/v2.0",
                    "required": True,
                },
            )
            X509SubjectName: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://ws.gematik.de/conn/CertificateServiceCommon/v2.0",
                    "required": True,
                },
            )
            X509Certificate: Optional[X509Certificate] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://ws.gematik.de/conn/CertificateServiceCommon/v2.0",
                    "required": True,
                },
            )

            @dataclass
            class X509IssuerSerial:
                X509IssuerName: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://ws.gematik.de/conn/CertificateServiceCommon/v2.0",
                        "required": True,
                    },
                )
                X509SerialNumber: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://ws.gematik.de/conn/CertificateServiceCommon/v2.0",
                        "required": True,
                    },
                )


@dataclass
class CheckCertificateDetails(CheckCertificateDetailsType):
    class Meta:
        namespace = "http://ws.gematik.de/conn/CertificateServiceCommon/v2.0"


@dataclass
class X509DataInfoList(X509DataInfoListType):
    class Meta:
        namespace = "http://ws.gematik.de/conn/CertificateServiceCommon/v2.0"
