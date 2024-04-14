from dataclasses import dataclass, field
from typing import Optional

from generated.conn.connector_common import (
    ClientSystemId,
    MandantId,
    UserId,
    WorkplaceId,
)

__NAMESPACE__ = "http://ws.gematik.de/conn/ConnectorContext/v2.0"


@dataclass
class ContextType:
    """
    :ivar MandantId: Die ID des Mandanten.
    :ivar ClientSystemId: Die ID des Clientsystems, von dem bzw. für das
        der Aufruf des Konnektors erfolgt. Unter einem Clientsystem wird
        hier ein einzelnes oder eine Gruppe von Systemen verstanden,
        welche im LAN des Leistungserbringers auf die Clientsystem-
        Schnittstelle des Konnektors zugreifen.
    :ivar WorkplaceId: Die ID des Arbeitsplatzes, von dem bzw. für den
        der Aufruf des Konnektors erfolgt. Bei fachlichen Aufrufen ist
        sie immer erforderlich.
    :ivar UserId: Die ID des Nutzers im Primärsystem. Ist nur dann
        erforderlich, falls ein HBA verwendet wird.
    """

    MandantId: Optional[MandantId] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ws.gematik.de/conn/ConnectorCommon/v5.0",
            "required": True,
        },
    )
    ClientSystemId: Optional[ClientSystemId] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ws.gematik.de/conn/ConnectorCommon/v5.0",
            "required": True,
        },
    )
    WorkplaceId: Optional[WorkplaceId] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ws.gematik.de/conn/ConnectorCommon/v5.0",
            "required": True,
        },
    )
    UserId: Optional[UserId] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ws.gematik.de/conn/ConnectorCommon/v5.0",
        },
    )


@dataclass
class Context(ContextType):
    class Meta:
        namespace = "http://ws.gematik.de/conn/ConnectorContext/v2.0"
