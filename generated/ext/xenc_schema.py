from dataclasses import dataclass, field
from typing import Dict, List, Optional, Type

from generated.ext.xmldsig_core_schema import (
    KeyInfo,
    KeyInfoType,
    Transform,
)

__NAMESPACE__ = "http://www.w3.org/2001/04/xmlenc#"


@dataclass
class DHKeyValueType:
    P: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/04/xmlenc#",
            "format": "base64",
        },
    )
    Q: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/04/xmlenc#",
            "format": "base64",
        },
    )
    Generator: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/04/xmlenc#",
            "format": "base64",
        },
    )
    Public: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/04/xmlenc#",
            "required": True,
            "format": "base64",
        },
    )
    seed: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/04/xmlenc#",
            "format": "base64",
        },
    )
    pgenCounter: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/04/xmlenc#",
            "format": "base64",
        },
    )


@dataclass
class EncryptionMethodType:
    Algorithm: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "KeySize",
                    "type": int,
                    "namespace": "http://www.w3.org/2001/04/xmlenc#",
                },
                {
                    "name": "OAEPparams",
                    "type": bytes,
                    "namespace": "http://www.w3.org/2001/04/xmlenc#",
                    "format": "base64",
                },
            ),
        },
    )


@dataclass
class EncryptionPropertyType:
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
    w3_orgXML1998namespace_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class ReferenceType:
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    URI: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class AgreementMethodType:
    Algorithm: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "KA-Nonce",
                    "type": bytes,
                    "namespace": "http://www.w3.org/2001/04/xmlenc#",
                    "format": "base64",
                },
                {
                    "name": "OriginatorKeyInfo",
                    "type": Type["AgreementMethodType.OriginatorKeyInfo"],
                    "namespace": "http://www.w3.org/2001/04/xmlenc#",
                },
                {
                    "name": "RecipientKeyInfo",
                    "type": Type["AgreementMethodType.RecipientKeyInfo"],
                    "namespace": "http://www.w3.org/2001/04/xmlenc#",
                },
            ),
        },
    )

    @dataclass
    class OriginatorKeyInfo(KeyInfoType):
        pass

    @dataclass
    class RecipientKeyInfo(KeyInfoType):
        pass


@dataclass
class DHKeyValue(DHKeyValueType):
    class Meta:
        namespace = "http://www.w3.org/2001/04/xmlenc#"


@dataclass
class EncryptionProperty(EncryptionPropertyType):
    class Meta:
        namespace = "http://www.w3.org/2001/04/xmlenc#"


@dataclass
class ReferenceList:
    class Meta:
        namespace = "http://www.w3.org/2001/04/xmlenc#"

    DataReference: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    KeyReference: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class TransformsType:
    Transform: List[Transform] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
        },
    )


@dataclass
class AgreementMethod(AgreementMethodType):
    class Meta:
        namespace = "http://www.w3.org/2001/04/xmlenc#"


@dataclass
class CipherReferenceType:
    Transforms: Optional[TransformsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/04/xmlenc#",
        },
    )
    URI: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class EncryptionPropertiesType:
    EncryptionProperty: List[EncryptionProperty] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/04/xmlenc#",
            "min_occurs": 1,
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class CipherReference(CipherReferenceType):
    class Meta:
        namespace = "http://www.w3.org/2001/04/xmlenc#"


@dataclass
class EncryptionProperties(EncryptionPropertiesType):
    class Meta:
        namespace = "http://www.w3.org/2001/04/xmlenc#"


@dataclass
class CipherDataType:
    CipherValue: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/04/xmlenc#",
            "format": "base64",
        },
    )
    CipherReference: Optional[CipherReference] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/04/xmlenc#",
        },
    )


@dataclass
class CipherData(CipherDataType):
    class Meta:
        namespace = "http://www.w3.org/2001/04/xmlenc#"


@dataclass
class EncryptedType:
    EncryptionMethod: Optional[EncryptionMethodType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/04/xmlenc#",
        },
    )
    KeyInfo: Optional[KeyInfo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    CipherData: Optional[CipherData] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/04/xmlenc#",
            "required": True,
        },
    )
    EncryptionProperties: Optional[EncryptionProperties] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/04/xmlenc#",
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    Type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
    MimeType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    Encoding: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class EncryptedDataType(EncryptedType):
    pass


@dataclass
class EncryptedKeyType(EncryptedType):
    ReferenceList: Optional[ReferenceList] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/04/xmlenc#",
        },
    )
    CarriedKeyName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/04/xmlenc#",
        },
    )
    Recipient: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class EncryptedData(EncryptedDataType):
    class Meta:
        namespace = "http://www.w3.org/2001/04/xmlenc#"


@dataclass
class EncryptedKey(EncryptedKeyType):
    class Meta:
        namespace = "http://www.w3.org/2001/04/xmlenc#"
