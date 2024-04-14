from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime

from generated.ext.oasis_dss_core_schema_v1_0_os import (
    Base64Data,
    DocumentBaseType,
)
from generated.tel.error.telematik_error import Error

__NAMESPACE__ = "http://ws.gematik.de/conn/ConnectorCommon/v5.0"


@dataclass
class AttachmentType:
    Data: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ws.gematik.de/conn/ConnectorCommon/v5.0",
            "required": True,
            "format": "base64",
        },
    )
    RefURI: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ws.gematik.de/conn/ConnectorCommon/v5.0",
            "required": True,
        },
    )


@dataclass
class CardHandle:
    class Meta:
        namespace = "http://ws.gematik.de/conn/ConnectorCommon/v5.0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 128,
        },
    )


@dataclass
class ClientSystemId:
    class Meta:
        namespace = "http://ws.gematik.de/conn/ConnectorCommon/v5.0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 64,
        },
    )


@dataclass
class EhcHandle:
    class Meta:
        namespace = "http://ws.gematik.de/conn/ConnectorCommon/v5.0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 128,
        },
    )


class ErrorState_Severity(Enum):
    FATAL = "Fatal"
    ERROR = "Error"
    WARNING = "Warning"
    INFO = "Info"


class ErrorState_Type(Enum):
    OPERATION = "Operation"
    SECURITY = "Security"
    INFRASTRUCTURE = "Infrastructure"


@dataclass
class HpcHandle:
    class Meta:
        namespace = "http://ws.gematik.de/conn/ConnectorCommon/v5.0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 128,
        },
    )


@dataclass
class MandantId:
    class Meta:
        namespace = "http://ws.gematik.de/conn/ConnectorCommon/v5.0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 64,
        },
    )


class Result_value(Enum):
    OK = "OK"
    WARNING = "Warning"


@dataclass
class SmcHandle:
    class Meta:
        namespace = "http://ws.gematik.de/conn/ConnectorCommon/v5.0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 128,
        },
    )


@dataclass
class UserId:
    class Meta:
        namespace = "http://ws.gematik.de/conn/ConnectorCommon/v5.0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 64,
        },
    )


class VPNSISStatus_ConnectionStatus(Enum):
    ONLINE = "Online"
    OFFLINE = "Offline"


class VPNTIStatus_ConnectionStatus(Enum):
    ONLINE = "Online"
    OFFLINE = "Offline"


@dataclass
class WorkplaceId:
    class Meta:
        namespace = "http://ws.gematik.de/conn/ConnectorCommon/v5.0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 64,
        },
    )


@dataclass
class DocumentType(DocumentBaseType):
    Base64XML: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ws.gematik.de/conn/ConnectorCommon/v5.0",
            "format": "base64",
        },
    )
    Base64Data: Optional[Base64Data] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
        },
    )


@dataclass
class ErrorState:
    class Meta:
        namespace = "http://ws.gematik.de/conn/ConnectorCommon/v5.0"

    ErrorCondition: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 128,
        },
    )
    Severity: Optional[ErrorState_Severity] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    Type_value: Optional[ErrorState_Type] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "required": True,
        },
    )
    Value: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    ValidFrom: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Result:
    """
    Enthält den Aussführungsstatus, entweder für die ganze Operation oder für einen
    einzelnen Schritt.
    """

    class Meta:
        namespace = "http://ws.gematik.de/conn/ConnectorCommon/v5.0"

    value: Optional[Result_value] = field(default=None)


@dataclass
class WorkplaceIds:
    class Meta:
        namespace = "http://ws.gematik.de/conn/ConnectorCommon/v5.0"

    WorkplaceId: List[WorkplaceId] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class XmlSchema(AttachmentType):
    class Meta:
        namespace = "http://ws.gematik.de/conn/ConnectorCommon/v5.0"


@dataclass
class XslStylesheet(AttachmentType):
    class Meta:
        namespace = "http://ws.gematik.de/conn/ConnectorCommon/v5.0"


@dataclass
class Document(DocumentType):
    class Meta:
        namespace = "http://ws.gematik.de/conn/ConnectorCommon/v5.0"


@dataclass
class OperatingState:
    class Meta:
        namespace = "http://ws.gematik.de/conn/ConnectorCommon/v5.0"

    ErrorState: List[ErrorState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Status:
    """Beschreibt den Status bzw.

    die aufgetretenen Fehler bei der Ausführung einer Operation.

    :ivar Result: Beschreibt den Ausführunggstatus der gesamten
        Operation. Mögliche Werte sind in der Enumeration ResultEnum
        angegeben. Allerdings können pro Operation weitere Werte
        definiert werden.
    :ivar Error:
    """

    class Meta:
        namespace = "http://ws.gematik.de/conn/ConnectorCommon/v5.0"

    Result: Optional[Result] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    Error: Optional[Error] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ws.gematik.de/tel/error/v2.0",
        },
    )


@dataclass
class Connector:
    class Meta:
        namespace = "http://ws.gematik.de/conn/ConnectorCommon/v5.0"

    VPNTIStatus: Optional["Connector.VPNTIStatus"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    VPNSISStatus: Optional["Connector.VPNSISStatus"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    OperatingState: Optional[OperatingState] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )

    @dataclass
    class VPNTIStatus:
        ConnectionStatus: Optional[VPNTIStatus_ConnectionStatus] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        Timestamp: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )

    @dataclass
    class VPNSISStatus:
        ConnectionStatus: Optional[VPNSISStatus_ConnectionStatus] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        Timestamp: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
