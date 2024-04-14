from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime, XmlDuration

from generated.conn.connector_common import (
    CardHandle,
    Status,
    XslStylesheet,
)
from generated.conn.connector_common import (
    DocumentType as connector_commonDocumentType,
)
from generated.conn.connector_context import Context
from generated.ext.oasis_dss_core_schema_v1_0_os import (
    AdditionalKeyInfo,
    Base64Data,
    DocumentBaseType,
    IncludeObject,
    Properties,
    ReturnUpdatedSignature,
    Schemas,
    SignatureObject,
    SignaturePlacement,
    SignatureType,
    UpdatedSignature,
    UseVerificationTimeType,
    VerifyManifestResults,
)
from generated.ext.oasis_dssx_1_0_profiles_sigpolicy_schema_cd01 import (
    GenerateUnderSignaturePolicy,
)
from generated.ext.oasis_dssx_1_0_profiles_vr_cd1 import (
    ReturnVerificationReport,
    VerificationReport,
)
from generated.tel.error.telematik_error import Error


class ComfortSignatureStatusEnum(Enum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


@dataclass
class CounterSignatureMarker:
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    SignatureValueReference: List[
        "CounterSignatureMarker.SignatureValueReference"
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class SignatureValueReference:
        IdRef: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class Deselected:
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class DisplayableAttributes:
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    DisplayableAttribute: List[
        "DisplayableAttributes.DisplayableAttribute"
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class DisplayableAttribute:
        Key: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "max_length": 80,
            },
        )
        Value: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "max_length": 8000,
            },
        )


@dataclass
class IncludeEContent:
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class IncludeRevocationInfo:
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class JobNumber:
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    value: str = field(
        default="",
        metadata={
            "pattern": r"[A-Z][A-Z][A-Z]-[0-9][0-9][0-9]",
        },
    )


@dataclass
class ReferenceToSignerCertificate:
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class ShortText:
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    value: str = field(
        default="",
        metadata={
            "max_length": 30,
            "pattern": r"[a-zA-Z 0-9_.\-äöüÄÖÜß]*",
        },
    )


class SignDocument_Crypt(Enum):
    RSA = "RSA"
    ECC = "ECC"
    RSA_ECC = "RSA_ECC"


class SignatureForm_value(Enum):
    URN_OASIS_NAMES_TC_DSS_1_0_PROFILES_AD_ES_FORMS_BES = (
        "urn:oasis:names:tc:dss:1.0:profiles:AdES:forms:BES"
    )
    URN_OASIS_NAMES_TC_DSS_1_0_PROFILES_AD_ES_FORMS_ES_T = (
        "urn:oasis:names:tc:dss:1.0:profiles:AdES:forms:ES-T"
    )
    URN_OASIS_NAMES_TC_DSS_1_0_PROFILES_AD_ES_FORMS_ES_C = (
        "urn:oasis:names:tc:dss:1.0:profiles:AdES:forms:ES-C"
    )
    URN_OASIS_NAMES_TC_DSS_1_0_PROFILES_AD_ES_FORMS_ES_X = (
        "urn:oasis:names:tc:dss:1.0:profiles:AdES:forms:ES-X"
    )
    URN_OASIS_NAMES_TC_DSS_1_0_PROFILES_AD_ES_FORMS_ES_X_L = (
        "urn:oasis:names:tc:dss:1.0:profiles:AdES:forms:ES-X-L"
    )


class SignatureModeEnum(Enum):
    PIN = "PIN"
    COMFORT = "COMFORT"


class SignatureSchemes_value(Enum):
    RSASSA_PSS = "RSASSA-PSS"
    RSASSA_PKCS1_V1_5 = "RSASSA-PKCS1-v1_5"


class TvMode_value(Enum):
    """
    :cvar NONE: Keine Anzeige im Trusted Viewer
    :cvar UNCONFIRMED: Anzeige im Trusted Viewer, aber ohne Warten auf
        Benutzerbestätigung
    :cvar CONFIRMED: Anzeige im Trusted Viewer mit Benutzerbestätigung
    """

    NONE = "NONE"
    UNCONFIRMED = "UNCONFIRMED"
    CONFIRMED = "CONFIRMED"


class VerificationResultType_HighLevelResult(Enum):
    VALID = "VALID"
    INCONCLUSIVE = "INCONCLUSIVE"
    INVALID = "INVALID"


class VerificationResultType_TimestampType(Enum):
    SIGNATURE_EMBEDDED_TIMESTAMP = "SIGNATURE_EMBEDDED_TIMESTAMP"
    QUALIFIED_TIMESTAMP = "QUALIFIED_TIMESTAMP"
    USER_DEFINED_TIMESTAMP = "USER_DEFINED_TIMESTAMP"
    SYSTEM_TIMESTAMP = "SYSTEM_TIMESTAMP"


@dataclass
class ActivateComfortSignature:
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    CardHandle: Optional[CardHandle] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ws.gematik.de/conn/ConnectorCommon/v5.0",
            "required": True,
        },
    )
    Context: Optional[Context] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ws.gematik.de/conn/ConnectorContext/v2.0",
            "required": True,
        },
    )


@dataclass
class BinaryDocumentType(DocumentBaseType):
    class Meta:
        target_namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    Base64Data: Optional[Base64Data] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
            "required": True,
        },
    )


@dataclass
class DeactivateComfortSignature:
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    CardHandle: List[CardHandle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://ws.gematik.de/conn/ConnectorCommon/v5.0",
            "min_occurs": 1,
        },
    )


@dataclass
class DeactivateComfortSignatureResponse:
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    Status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ws.gematik.de/conn/ConnectorCommon/v5.0",
            "required": True,
        },
    )


@dataclass
class DocumentType(connector_commonDocumentType):
    class Meta:
        target_namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    ShortText: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ExternalAuthenticateResponse:
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    Status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ws.gematik.de/conn/ConnectorCommon/v5.0",
            "required": True,
        },
    )
    SignatureObject: Optional[SignatureObject] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
        },
    )


@dataclass
class GetJobNumber:
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    Context: Optional[Context] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ws.gematik.de/conn/ConnectorContext/v2.0",
            "required": True,
        },
    )


@dataclass
class GetJobNumberResponse:
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    JobNumber: Optional[JobNumber] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class GetSignatureMode:
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    CardHandle: Optional[CardHandle] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ws.gematik.de/conn/ConnectorCommon/v5.0",
            "required": True,
        },
    )
    Context: Optional[Context] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ws.gematik.de/conn/ConnectorContext/v2.0",
            "required": True,
        },
    )


@dataclass
class SignatureForm:
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    value: Optional[SignatureForm_value] = field(default=None)


@dataclass
class SignatureMode:
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    value: Optional[SignatureModeEnum] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class SignatureSchemes:
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    value: Optional[SignatureSchemes_value] = field(default=None)


@dataclass
class StopSignature:
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    Context: Optional[Context] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ws.gematik.de/conn/ConnectorContext/v2.0",
            "required": True,
        },
    )
    JobNumber: Optional[JobNumber] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class StopSignatureResponse:
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    Status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ws.gematik.de/conn/ConnectorCommon/v5.0",
            "required": True,
        },
    )


@dataclass
class TvMode:
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    value: TvMode_value = field(default=TvMode_value.UNCONFIRMED)


@dataclass
class UseVerificationTime(UseVerificationTimeType):
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"


@dataclass
class VerificationResultType:
    class Meta:
        target_namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    HighLevelResult: Optional[VerificationResultType_HighLevelResult] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ws.gematik.de/conn/SignatureService/v7.5",
            "required": True,
        },
    )
    TimestampType: Optional[VerificationResultType_TimestampType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ws.gematik.de/conn/SignatureService/v7.5",
            "required": True,
        },
    )
    Timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ws.gematik.de/conn/SignatureService/v7.5",
            "required": True,
        },
    )


@dataclass
class ViewerInfo:
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    XslStyleSheets: Optional["ViewerInfo.XslStyleSheets"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class XslStyleSheets:
        XslStylesheet: List[XslStylesheet] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://ws.gematik.de/conn/ConnectorCommon/v5.0",
                "min_occurs": 1,
            },
        )


@dataclass
class SignatureServicePortType_ActivateComfortSignature_input:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = (
            "http://ws.gematik.de/conn/SignatureService/WSDL/v7.5"
        )

    Body: Optional[
        "SignatureServicePortType_ActivateComfortSignature_input.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ActivateComfortSignature: Optional[ActivateComfortSignature] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.gematik.de/conn/SignatureService/v7.5",
            },
        )


@dataclass
class SignatureServicePortType_DeactivateComfortSignature_input:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = (
            "http://ws.gematik.de/conn/SignatureService/WSDL/v7.5"
        )

    Body: Optional[
        "SignatureServicePortType_DeactivateComfortSignature_input.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        DeactivateComfortSignature: Optional[DeactivateComfortSignature] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://ws.gematik.de/conn/SignatureService/v7.5",
                },
            )
        )


@dataclass
class SignatureServicePortType_DeactivateComfortSignature_output:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = (
            "http://ws.gematik.de/conn/SignatureService/WSDL/v7.5"
        )

    Body: Optional[
        "SignatureServicePortType_DeactivateComfortSignature_output.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        DeactivateComfortSignatureResponse: Optional[
            DeactivateComfortSignatureResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.gematik.de/conn/SignatureService/v7.5",
            },
        )
        Fault: Optional[
            "SignatureServicePortType_DeactivateComfortSignature_output.Body.Fault"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: Optional[
                "SignatureServicePortType_DeactivateComfortSignature_output.Body.Fault.detail"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )

            @dataclass
            class detail:
                Error: Optional[Error] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://ws.gematik.de/tel/error/v2.0",
                    },
                )


@dataclass
class SignatureServicePortType_GetJobNumber_input:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = (
            "http://ws.gematik.de/conn/SignatureService/WSDL/v7.5"
        )

    Body: Optional["SignatureServicePortType_GetJobNumber_input.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        GetJobNumber: Optional[GetJobNumber] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.gematik.de/conn/SignatureService/v7.5",
            },
        )


@dataclass
class SignatureServicePortType_GetJobNumber_output:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = (
            "http://ws.gematik.de/conn/SignatureService/WSDL/v7.5"
        )

    Body: Optional["SignatureServicePortType_GetJobNumber_output.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        GetJobNumberResponse: Optional[GetJobNumberResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.gematik.de/conn/SignatureService/v7.5",
            },
        )
        Fault: Optional[
            "SignatureServicePortType_GetJobNumber_output.Body.Fault"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: Optional[
                "SignatureServicePortType_GetJobNumber_output.Body.Fault.detail"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )

            @dataclass
            class detail:
                Error: Optional[Error] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://ws.gematik.de/tel/error/v2.0",
                    },
                )


@dataclass
class SignatureServicePortType_GetSignatureMode_input:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = (
            "http://ws.gematik.de/conn/SignatureService/WSDL/v7.5"
        )

    Body: Optional["SignatureServicePortType_GetSignatureMode_input.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        GetSignatureMode: Optional[GetSignatureMode] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.gematik.de/conn/SignatureService/v7.5",
            },
        )


@dataclass
class SignatureServicePortType_StopSignature_input:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = (
            "http://ws.gematik.de/conn/SignatureService/WSDL/v7.5"
        )

    Body: Optional["SignatureServicePortType_StopSignature_input.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        StopSignature: Optional[StopSignature] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.gematik.de/conn/SignatureService/v7.5",
            },
        )


@dataclass
class SignatureServicePortType_StopSignature_output:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = (
            "http://ws.gematik.de/conn/SignatureService/WSDL/v7.5"
        )

    Body: Optional["SignatureServicePortType_StopSignature_output.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        StopSignatureResponse: Optional[StopSignatureResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.gematik.de/conn/SignatureService/v7.5",
            },
        )
        Fault: Optional[
            "SignatureServicePortType_StopSignature_output.Body.Fault"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: Optional[
                "SignatureServicePortType_StopSignature_output.Body.Fault.detail"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )

            @dataclass
            class detail:
                Error: Optional[Error] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://ws.gematik.de/tel/error/v2.0",
                    },
                )


@dataclass
class ActivateComfortSignatureResponse:
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    Status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ws.gematik.de/conn/ConnectorCommon/v5.0",
            "required": True,
        },
    )
    SignatureMode: Optional[SignatureMode] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class BinaryString(BinaryDocumentType):
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"


@dataclass
class Document(DocumentType):
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"


@dataclass
class DocumentWithSignature(DocumentType):
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"


@dataclass
class SessionInfo:
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    SignatureMode: Optional[SignatureMode] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    CountRemaining: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 250,
        },
    )
    TimeRemaining: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SignatureServicePortType_ActivateComfortSignature_output:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = (
            "http://ws.gematik.de/conn/SignatureService/WSDL/v7.5"
        )

    Body: Optional[
        "SignatureServicePortType_ActivateComfortSignature_output.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ActivateComfortSignatureResponse: Optional[
            ActivateComfortSignatureResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.gematik.de/conn/SignatureService/v7.5",
            },
        )
        Fault: Optional[
            "SignatureServicePortType_ActivateComfortSignature_output.Body.Fault"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: Optional[
                "SignatureServicePortType_ActivateComfortSignature_output.Body.Fault.detail"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )

            @dataclass
            class detail:
                Error: Optional[Error] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://ws.gematik.de/tel/error/v2.0",
                    },
                )


class SignatureServicePortType_DeactivateComfortSignature:
    style = "document"
    location = "http://ti-konnektor/signatureservice"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://ws.gematik.de/conn/SignatureService/v7.5#DeactivateComfortSignature"
    input = SignatureServicePortType_DeactivateComfortSignature_input
    output = SignatureServicePortType_DeactivateComfortSignature_output


class SignatureServicePortType_GetJobNumber:
    style = "document"
    location = "http://ti-konnektor/signatureservice"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://ws.gematik.de/conn/SignatureService/v7.5#GetJobNumber"
    input = SignatureServicePortType_GetJobNumber_input
    output = SignatureServicePortType_GetJobNumber_output


class SignatureServicePortType_StopSignature:
    style = "document"
    location = "http://ti-konnektor/signatureservice"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = (
        "http://ws.gematik.de/conn/SignatureService/v7.5#StopSignature"
    )
    input = SignatureServicePortType_StopSignature_input
    output = SignatureServicePortType_StopSignature_output


@dataclass
class ExternalAuthenticate:
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    CardHandle: Optional[CardHandle] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ws.gematik.de/conn/ConnectorCommon/v5.0",
            "required": True,
        },
    )
    Context: Optional[Context] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ws.gematik.de/conn/ConnectorContext/v2.0",
            "required": True,
        },
    )
    OptionalInputs: Optional["ExternalAuthenticate.OptionalInputs"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    BinaryString: Optional[BinaryString] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )

    @dataclass
    class OptionalInputs:
        SignatureType: Optional[SignatureType] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
            },
        )
        SignatureSchemes: Optional[SignatureSchemes] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )


@dataclass
class GetSignatureModeResponse:
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    Status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ws.gematik.de/conn/ConnectorCommon/v5.0",
            "required": True,
        },
    )
    ComfortSignatureStatus: Optional[ComfortSignatureStatusEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    ComfortSignatureMax: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 250,
        },
    )
    ComfortSignatureTimer: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    SessionInfo: Optional[SessionInfo] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class SignRequest:
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    OptionalInputs: Optional["SignRequest.OptionalInputs"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Document: Optional[Document] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    IncludeRevocationInfo: Optional[IncludeRevocationInfo] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    RequestID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )

    @dataclass
    class OptionalInputs:
        SignatureType: Optional[SignatureType] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
            },
        )
        Properties: Optional[Properties] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
            },
        )
        IncludeEContent: Optional[IncludeEContent] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        IncludeObjects: Optional[
            "SignRequest.OptionalInputs.IncludeObjects"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        SignaturePlacement: Optional[SignaturePlacement] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
            },
        )
        ReturnUpdatedSignature: Optional[ReturnUpdatedSignature] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
            },
        )
        Schemas: Optional[Schemas] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
            },
        )
        GenerateUnderSignaturePolicy: Optional[
            GenerateUnderSignaturePolicy
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:SignaturePolicy:schema#",
            },
        )
        ViewerInfo: Optional[ViewerInfo] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

        @dataclass
        class IncludeObjects:
            IncludeObject: List[IncludeObject] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
                    "min_occurs": 1,
                },
            )


@dataclass
class SignResponse:
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    Status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ws.gematik.de/conn/ConnectorCommon/v5.0",
            "required": True,
        },
    )
    OptionalOutputs: Optional["SignResponse.OptionalOutputs"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    SignatureObject: Optional[SignatureObject] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
        },
    )
    RequestID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )

    @dataclass
    class OptionalOutputs:
        DocumentWithSignature: Optional[DocumentWithSignature] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        VerificationReport: Optional[VerificationReport] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            },
        )


@dataclass
class VerifyDocument:
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    Context: Optional[Context] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ws.gematik.de/conn/ConnectorContext/v2.0",
            "required": True,
        },
    )
    TvMode: Optional[TvMode] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    OptionalInputs: Optional["VerifyDocument.OptionalInputs"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Document: Optional[Document] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    SignatureObject: Optional[SignatureObject] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
        },
    )
    IncludeRevocationInfo: Optional[IncludeRevocationInfo] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )

    @dataclass
    class OptionalInputs:
        VerifyManifests: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        UseVerificationTime: Optional[UseVerificationTime] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        AdditionalKeyInfo: Optional[AdditionalKeyInfo] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
            },
        )
        ReturnVerificationReport: Optional[ReturnVerificationReport] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            },
        )
        Schemas: Optional[Schemas] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
            },
        )
        ViewerInfo: Optional[ViewerInfo] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )


@dataclass
class VerifyDocumentResponse:
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    Status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ws.gematik.de/conn/ConnectorCommon/v5.0",
            "required": True,
        },
    )
    VerificationResult: Optional[VerificationResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    OptionalOutputs: Optional["VerifyDocumentResponse.OptionalOutputs"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class OptionalOutputs:
        VerifyManifestResults: Optional[VerifyManifestResults] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
            },
        )
        DocumentWithSignature: Optional[DocumentWithSignature] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        UpdatedSignature: Optional[UpdatedSignature] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
            },
        )
        VerificationReport: Optional[VerificationReport] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:verificationreport:schema#",
            },
        )


class SignatureServicePortType_ActivateComfortSignature:
    style = "document"
    location = "http://ti-konnektor/signatureservice"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://ws.gematik.de/conn/SignatureService/v7.5#ActivateComfortSignature"
    input = SignatureServicePortType_ActivateComfortSignature_input
    output = SignatureServicePortType_ActivateComfortSignature_output


@dataclass
class SignatureServicePortType_GetSignatureMode_output:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = (
            "http://ws.gematik.de/conn/SignatureService/WSDL/v7.5"
        )

    Body: Optional["SignatureServicePortType_GetSignatureMode_output.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        GetSignatureModeResponse: Optional[GetSignatureModeResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.gematik.de/conn/SignatureService/v7.5",
            },
        )
        Fault: Optional[
            "SignatureServicePortType_GetSignatureMode_output.Body.Fault"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: Optional[
                "SignatureServicePortType_GetSignatureMode_output.Body.Fault.detail"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )

            @dataclass
            class detail:
                Error: Optional[Error] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://ws.gematik.de/tel/error/v2.0",
                    },
                )


@dataclass
class SignatureServicePortType_VerifyDocument_input:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = (
            "http://ws.gematik.de/conn/SignatureService/WSDL/v7.5"
        )

    Body: Optional["SignatureServicePortType_VerifyDocument_input.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        VerifyDocument: Optional[VerifyDocument] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.gematik.de/conn/SignatureService/v7.5",
            },
        )


@dataclass
class SignatureServicePortType_VerifyDocument_output:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = (
            "http://ws.gematik.de/conn/SignatureService/WSDL/v7.5"
        )

    Body: Optional["SignatureServicePortType_VerifyDocument_output.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        VerifyDocumentResponse: Optional[VerifyDocumentResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.gematik.de/conn/SignatureService/v7.5",
            },
        )
        Fault: Optional[
            "SignatureServicePortType_VerifyDocument_output.Body.Fault"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: Optional[
                "SignatureServicePortType_VerifyDocument_output.Body.Fault.detail"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )

            @dataclass
            class detail:
                Error: Optional[Error] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://ws.gematik.de/tel/error/v2.0",
                    },
                )


@dataclass
class SignDocument:
    """
    :ivar CardHandle:
    :ivar Crypt:
    :ivar Context:
    :ivar TvMode:
    :ivar JobNumber: Am Konnektor verpflichtend, am Signaturproxy
        optional
    :ivar SignRequest:
    """

    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    CardHandle: Optional[CardHandle] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ws.gematik.de/conn/ConnectorCommon/v5.0",
            "required": True,
        },
    )
    Crypt: Optional[SignDocument_Crypt] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Context: Optional[Context] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ws.gematik.de/conn/ConnectorContext/v2.0",
            "required": True,
        },
    )
    TvMode: Optional[TvMode] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    JobNumber: Optional[JobNumber] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    SignRequest: List[SignRequest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class SignDocumentResponse:
    class Meta:
        namespace = "http://ws.gematik.de/conn/SignatureService/v7.5"

    SignResponse: List[SignResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


class SignatureServicePortType_GetSignatureMode:
    style = "document"
    location = "http://ti-konnektor/signatureservice"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = (
        "http://ws.gematik.de/conn/SignatureService/v7.5#GetSignatureMode"
    )
    input = SignatureServicePortType_GetSignatureMode_input
    output = SignatureServicePortType_GetSignatureMode_output


@dataclass
class SignatureServicePortType_SignDocument_input:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = (
            "http://ws.gematik.de/conn/SignatureService/WSDL/v7.5"
        )

    Body: Optional["SignatureServicePortType_SignDocument_input.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        SignDocument: Optional[SignDocument] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.gematik.de/conn/SignatureService/v7.5",
            },
        )


@dataclass
class SignatureServicePortType_SignDocument_output:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = (
            "http://ws.gematik.de/conn/SignatureService/WSDL/v7.5"
        )

    Body: Optional["SignatureServicePortType_SignDocument_output.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        SignDocumentResponse: Optional[SignDocumentResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.gematik.de/conn/SignatureService/v7.5",
            },
        )
        Fault: Optional[
            "SignatureServicePortType_SignDocument_output.Body.Fault"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: Optional[
                "SignatureServicePortType_SignDocument_output.Body.Fault.detail"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )

            @dataclass
            class detail:
                Error: Optional[Error] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://ws.gematik.de/tel/error/v2.0",
                    },
                )


class SignatureServicePortType_VerifyDocument:
    style = "document"
    location = "http://ti-konnektor/signatureservice"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = (
        "http://ws.gematik.de/conn/SignatureService/v7.5#VerifyDocument"
    )
    input = SignatureServicePortType_VerifyDocument_input
    output = SignatureServicePortType_VerifyDocument_output


class SignatureServicePortType_SignDocument:
    style = "document"
    location = "http://ti-konnektor/signatureservice"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://ws.gematik.de/conn/SignatureService/v7.5#SignDocument"
    input = SignatureServicePortType_SignDocument_input
    output = SignatureServicePortType_SignDocument_output
