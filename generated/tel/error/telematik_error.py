from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://ws.gematik.de/tel/error/v2.0"


@dataclass
class Error:
    class Meta:
        namespace = "http://ws.gematik.de/tel/error/v2.0"

    MessageID: str = field(
        default="",
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
    Trace: List["Error.Trace"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class Trace:
        EventID: str = field(
            default="",
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        Instance: str = field(
            default="",
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        LogReference: str = field(
            default="",
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        CompType: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        Code: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        Severity: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        ErrorType: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        ErrorText: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        Detail: Optional["Error.Trace.Detail"] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

        @dataclass
        class Detail:
            value: str = field(
                default="",
                metadata={
                    "required": True,
                },
            )
            Encoding: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                },
            )
