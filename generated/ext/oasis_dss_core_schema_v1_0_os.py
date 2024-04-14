from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime, XmlDuration

from generated.ext.oasis_sstc_saml_schema_assertion_1_1 import (
    NameIdentifierType,
)
from generated.ext.xmldsig_core_schema import (
    DigestMethod,
    DigestValue,
    KeyInfo,
    Signature,
    Transforms,
)

__NAMESPACE__ = "urn:oasis:names:tc:dss:1.0:core:schema"


@dataclass
class AdditionalProfile:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class AdditionalTimeInfoType:
    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    Type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
    Ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class AnyType:
    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Base64Data:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "format": "base64",
        },
    )
    MimeType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Base64Signature:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "format": "base64",
        },
    )
    Type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )


@dataclass
class DocumentBaseType:
    ID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    RefURI: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    RefType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    SchemaRefs: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass
class IncludeObject:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    WhichDocument: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    hasObjectTagsAndAttributesSet: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    ObjId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    createReference: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class InlineXMLType:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    ignorePIs: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    ignoreComments: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class InternationalStringType:
    value: str = field(
        default="",
        metadata={
            "required": True,
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
class Language:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class ManifestResult:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    ReferenceXpath: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    Status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ReturnProcessingDetails:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class ReturnSignerIdentity:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class ReturnSigningTimeInfo:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class ReturnTransformedDocument:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    WhichReference: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ReturnUpdatedSignature:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    Type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )


@dataclass
class ReturnVerificationTimeInfo:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class ServicePolicy:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class SignaturePlacement:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    XPathAfter: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    XPathFirstChildOf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    WhichDocument: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    CreateEnvelopedSignature: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SignaturePtr:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

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


@dataclass
class SignatureType:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class SigningTimeInfoType:
    SigningTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
            "required": True,
        },
    )
    SigningTimeBoundaries: Optional[
        "SigningTimeInfoType.SigningTimeBoundaries"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
        },
    )

    @dataclass
    class SigningTimeBoundaries:
        LowerBoundary: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
            },
        )
        UpperBoundary: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
            },
        )


@dataclass
class UpdateSignatureInstructionType:
    Type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )


@dataclass
class UseVerificationTime:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class UseVerificationTimeType:
    CurrentTime: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
        },
    )
    SpecificTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
        },
    )
    other_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )


@dataclass
class AddTimestamp(UpdateSignatureInstructionType):
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"


@dataclass
class AdditionalKeyInfo:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    KeyInfo: Optional[KeyInfo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        },
    )


@dataclass
class AdditionalTimeInfo(AdditionalTimeInfoType):
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"


@dataclass
class AttachmentReferenceType:
    DigestMethod: Optional[DigestMethod] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    DigestValue: Optional[DigestValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    AttRefURI: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    MimeType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ClaimedIdentity:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    Name: Optional[NameIdentifierType] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    SupportingInfo: Optional[AnyType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class DetailType:
    Code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
        },
    )
    Message: Optional[InternationalStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
        },
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    Type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class DocumentHash(DocumentBaseType):
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    Transforms: Optional[Transforms] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    DigestMethod: Optional[DigestMethod] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    DigestValue: Optional[DigestValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        },
    )
    WhichReference: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class IntendedAudience:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    Recipient: List[NameIdentifierType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class KeySelector:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    KeyInfo: Optional[KeyInfo] = field(
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
        },
    )


@dataclass
class OptionalInputs(AnyType):
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"


@dataclass
class OptionalOutputs(AnyType):
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"


@dataclass
class Property:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    Identifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    Value: Optional[AnyType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RequesterIdentity:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    Name: Optional[NameIdentifierType] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    SupportingInfo: Optional[AnyType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Result:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    ResultMajor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    ResultMinor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ResultMessage: Optional[InternationalStringType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ReturnTimestampedSignature(UpdateSignatureInstructionType):
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"


@dataclass
class SignedReference:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    Transforms: Optional[Transforms] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    WhichDocument: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    RefURI: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    RefId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SignerIdentity(NameIdentifierType):
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"


@dataclass
class SigningTimeInfo(SigningTimeInfoType):
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"


@dataclass
class TimeSignatureInstructionType(UpdateSignatureInstructionType):
    TimeStampTheGivenSignature: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Timestamp:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    Signature: Optional[Signature] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    RFC3161TimeStampToken: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "format": "base64",
        },
    )
    Other: Optional[AnyType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class TransformedData(DocumentBaseType):
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    Transforms: Optional[Transforms] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    Base64Data: Optional[Base64Data] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    WhichReference: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TstInfo:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    SerialNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    CreationTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    Policy: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ErrorBound: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Ordered: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    TSA: Optional[NameIdentifierType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class VerifyManifestResultsType:
    ManifestResult: List[ManifestResult] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
            "min_occurs": 1,
        },
    )


@dataclass
class AttachmentReference(AttachmentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"


@dataclass
class ProcessingDetails:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    ValidDetail: List[DetailType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    IndeterminateDetail: List[DetailType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    InvalidDetail: List[DetailType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class PropertiesType:
    Property: List[Property] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
            "min_occurs": 1,
        },
    )


@dataclass
class ResponseBaseType:
    Result: Optional[Result] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
            "required": True,
        },
    )
    OptionalOutputs: Optional[OptionalOutputs] = field(
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
        },
    )
    Profile: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class SignatureObject:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    Signature: Optional[Signature] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    Timestamp: Optional[Timestamp] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Base64Signature: Optional[Base64Signature] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    SignaturePtr: Optional[SignaturePtr] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Other: Optional[AnyType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    SchemaRefs: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass
class SignedReferences:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    SignedReference: List[SignedReference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class VerificationTimeInfoType:
    VerificationTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
            "required": True,
        },
    )
    AdditionalTimeInfo: List[AdditionalTimeInfo] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
        },
    )


@dataclass
class VerifyManifestResults(VerifyManifestResultsType):
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"


@dataclass
class DocumentType(DocumentBaseType):
    InlineXML: Optional[InlineXMLType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
        },
    )
    Base64XML: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
            "format": "base64",
        },
    )
    EscapedXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
        },
    )
    Base64Data: Optional[Base64Data] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
        },
    )
    AttachmentReference: Optional[AttachmentReference] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
        },
    )


@dataclass
class Properties:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    SignedProperties: Optional[PropertiesType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    UnsignedProperties: Optional[PropertiesType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Response(ResponseBaseType):
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"


@dataclass
class SignResponse(ResponseBaseType):
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    SignatureObject: Optional[SignatureObject] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class UpdatedSignatureType:
    SignatureObject: Optional[SignatureObject] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
            "required": True,
        },
    )
    Type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )


@dataclass
class VerificationTimeInfo(VerificationTimeInfoType):
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"


@dataclass
class VerifyResponse(ResponseBaseType):
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"


@dataclass
class Document(DocumentType):
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"


@dataclass
class Schema(DocumentType):
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"


@dataclass
class TimestampedSignature(UpdatedSignatureType):
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"


@dataclass
class UpdatedSignature(UpdatedSignatureType):
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"


@dataclass
class DocumentWithSignature:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    Document: Optional[Document] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class InputDocuments:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    Document: List[Document] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    TransformedData: List[TransformedData] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    DocumentHash: List[DocumentHash] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    Other: List[AnyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class SchemasType:
    Schema: List[Schema] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
            "min_occurs": 1,
        },
    )


@dataclass
class TransformedDocument:
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    Document: Optional[Document] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    WhichReference: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class RequestBaseType:
    OptionalInputs: Optional[OptionalInputs] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss:1.0:core:schema",
        },
    )
    InputDocuments: Optional[InputDocuments] = field(
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
        },
    )
    Profile: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Schemas(SchemasType):
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"


@dataclass
class SignRequest(RequestBaseType):
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"


@dataclass
class VerifyRequest(RequestBaseType):
    class Meta:
        namespace = "urn:oasis:names:tc:dss:1.0:core:schema"

    SignatureObject: Optional[SignatureObject] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
