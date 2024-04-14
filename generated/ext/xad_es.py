from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional

from xsdata.models.datatype import XmlDateTime

from generated.ext.xmldsig_core_schema import (
    CanonicalizationMethod,
    DigestMethod,
    DigestValue,
    Signature,
    Transforms,
    X509IssuerSerialType,
)

__NAMESPACE__ = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class AnyType:
    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
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
class CRLIdentifierType:
    Issuer: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        },
    )
    IssueTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        },
    )
    Number: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    URI: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class DocumentationReferencesType:
    DocumentationReference: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass
class EncapsulatedPKIDataType:
    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "format": "base64",
        },
    )
    Id: Optional[str] = field(
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
class IncludeType:
    URI: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    referencedData: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class IntegerListType:
    int_value: List[int] = field(
        default_factory=list,
        metadata={
            "name": "int",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )


class QualifierType(Enum):
    OIDAS_URI = "OIDAsURI"
    OIDAS_URN = "OIDAsURN"


@dataclass
class QualifyingPropertiesReferenceType:
    URI: Optional[str] = field(
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
class ResponderIDType:
    ByName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    ByKey: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "format": "base64",
        },
    )


@dataclass
class SPURI:
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class SignatureProductionPlaceType:
    City: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    StateOrProvince: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    PostalCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    CountryName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )


@dataclass
class SigningTime:
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Any_type(AnyType):
    class Meta:
        name = "Any"
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class CRLValuesType:
    EncapsulatedCRLValue: List[EncapsulatedPKIDataType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass
class CertificateValuesType:
    EncapsulatedX509Certificate: List[EncapsulatedPKIDataType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    OtherCertificate: List[AnyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
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
    CertifiedRole: List[EncapsulatedPKIDataType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass
class ClaimedRolesListType:
    ClaimedRole: List[AnyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass
class CommitmentTypeQualifiersListType:
    CommitmentTypeQualifier: List[AnyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )


@dataclass
class CounterSignatureType:
    Signature: Optional[Signature] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        },
    )


@dataclass
class DigestAlgAndValueType:
    DigestMethod: Optional[DigestMethod] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
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


@dataclass
class EncapsulatedPKIData(EncapsulatedPKIDataType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class IdentifierType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    Qualifier: Optional[QualifierType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Include(IncludeType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class NoticeReferenceType:
    Organization: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        },
    )
    NoticeNumbers: Optional[IntegerListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        },
    )


@dataclass
class OCSPIdentifierType:
    ResponderID: Optional[ResponderIDType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        },
    )
    ProducedAt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        },
    )
    URI: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class OCSPValuesType:
    EncapsulatedOCSPValue: List[EncapsulatedPKIDataType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass
class OtherCertStatusRefsType:
    OtherRef: List[AnyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass
class OtherCertStatusValuesType:
    OtherValue: List[AnyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass
class QualifyingPropertiesReference(QualifyingPropertiesReferenceType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class ReferenceInfoType:
    DigestMethod: Optional[DigestMethod] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
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
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    URI: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SigPolicyQualifiersListType:
    SigPolicyQualifier: List[AnyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass
class SignatureProductionPlace(SignatureProductionPlaceType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class UnsignedDataObjectPropertiesType:
    UnsignedDataObjectProperty: List[AnyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
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
class AttrAuthoritiesCertValues(CertificateValuesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class CRLRefType:
    DigestAlgAndValue: Optional[DigestAlgAndValueType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        },
    )
    CRLIdentifier: Optional[CRLIdentifierType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )


@dataclass
class CertIDType:
    CertDigest: Optional[DigestAlgAndValueType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        },
    )
    IssuerSerial: Optional[X509IssuerSerialType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        },
    )
    URI: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class CertificateValues(CertificateValuesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class CounterSignature(CounterSignatureType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class OCSPRefType:
    OCSPIdentifier: Optional[OCSPIdentifierType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        },
    )
    DigestAlgAndValue: Optional[DigestAlgAndValueType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )


@dataclass
class ObjectIdentifierType:
    Identifier: Optional[IdentifierType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        },
    )
    Description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    DocumentationReferences: Optional[DocumentationReferencesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )


@dataclass
class ReferenceInfo(ReferenceInfoType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class RevocationValuesType:
    CRLValues: Optional[CRLValuesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    OCSPValues: Optional[OCSPValuesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    OtherValues: Optional[OtherCertStatusValuesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SPUserNoticeType:
    NoticeRef: Optional[NoticeReferenceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    ExplicitText: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )


@dataclass
class SignerRoleType:
    ClaimedRoles: Optional[ClaimedRolesListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    CertifiedRoles: Optional[CertifiedRolesListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )


@dataclass
class UnsignedDataObjectProperties(UnsignedDataObjectPropertiesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class AttributeRevocationValues(RevocationValuesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class CRLRefsType:
    CRLRef: List[CRLRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass
class CertIDListType:
    Cert: List[CertIDType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass
class CommitmentTypeIndicationType:
    CommitmentTypeId: Optional[ObjectIdentifierType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        },
    )
    ObjectReference: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    AllSignedDataObjects: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    CommitmentTypeQualifiers: Optional[CommitmentTypeQualifiersListType] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            },
        )
    )


@dataclass
class DataObjectFormatType:
    Description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    ObjectIdentifier: Optional[ObjectIdentifierType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    MimeType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    Encoding: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    ObjectReference: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class GenericTimeStampType:
    Include: List[Include] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    ReferenceInfo: List[ReferenceInfo] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    CanonicalizationMethod: Optional[CanonicalizationMethod] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    EncapsulatedTimeStamp: List[EncapsulatedPKIDataType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    XMLTimeStamp: List[AnyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class OCSPRefsType:
    OCSPRef: List[OCSPRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass
class ObjectIdentifier(ObjectIdentifierType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class RevocationValues(RevocationValuesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class SPUserNotice(SPUserNoticeType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class SignaturePolicyIdType:
    SigPolicyId: Optional[ObjectIdentifierType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        },
    )
    Transforms: Optional[Transforms] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    SigPolicyHash: Optional[DigestAlgAndValueType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "required": True,
        },
    )
    SigPolicyQualifiers: Optional[SigPolicyQualifiersListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )


@dataclass
class SignerRole(SignerRoleType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class CommitmentTypeIndication(CommitmentTypeIndicationType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class CompleteCertificateRefsType:
    CertRefs: Optional[CertIDListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
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
class CompleteRevocationRefsType:
    CRLRefs: Optional[CRLRefsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    OCSPRefs: Optional[OCSPRefsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    OtherRefs: Optional[OtherCertStatusRefsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class DataObjectFormat(DataObjectFormatType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class OtherTimeStampType(GenericTimeStampType):
    Include: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    ReferenceInfo: List[ReferenceInfo] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass
class SignaturePolicyIdentifierType:
    SignaturePolicyId: Optional[SignaturePolicyIdType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    SignaturePolicyImplied: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )


@dataclass
class SigningCertificate(CertIDListType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class XAdESTimeStampType(GenericTimeStampType):
    ReferenceInfo: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class AllDataObjectsTimeStamp(XAdESTimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class ArchiveTimeStamp(XAdESTimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class AttributeCertificateRefs(CompleteCertificateRefsType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class AttributeRevocationRefs(CompleteRevocationRefsType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class CompleteCertificateRefs(CompleteCertificateRefsType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class CompleteRevocationRefs(CompleteRevocationRefsType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class IndividualDataObjectsTimeStamp(XAdESTimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class OtherTimeStamp(OtherTimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class RefsOnlyTimeStamp(XAdESTimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class SigAndRefsTimeStamp(XAdESTimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class SignaturePolicyIdentifier(SignaturePolicyIdentifierType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class SignatureTimeStamp(XAdESTimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class SignedDataObjectPropertiesType:
    DataObjectFormat: List[DataObjectFormatType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    CommitmentTypeIndication: List[CommitmentTypeIndicationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    AllDataObjectsTimeStamp: List[XAdESTimeStampType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    IndividualDataObjectsTimeStamp: List[XAdESTimeStampType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SignedSignaturePropertiesType:
    SigningTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    SigningCertificate: Optional[CertIDListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    SignaturePolicyIdentifier: Optional[SignaturePolicyIdentifierType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    SignatureProductionPlace: Optional[SignatureProductionPlaceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    SignerRole: Optional[SignerRoleType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class UnsignedSignaturePropertiesType:
    CounterSignature: List[CounterSignatureType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    SignatureTimeStamp: List[XAdESTimeStampType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    CompleteCertificateRefs: List[CompleteCertificateRefsType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    CompleteRevocationRefs: List[CompleteRevocationRefsType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    AttributeCertificateRefs: List[CompleteCertificateRefsType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    AttributeRevocationRefs: List[CompleteRevocationRefsType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    SigAndRefsTimeStamp: List[XAdESTimeStampType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    RefsOnlyTimeStamp: List[XAdESTimeStampType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    CertificateValues: List[CertificateValuesType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    RevocationValues: List[RevocationValuesType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    AttrAuthoritiesCertValues: List[CertificateValuesType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    AttributeRevocationValues: List[RevocationValuesType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    ArchiveTimeStamp: List[XAdESTimeStampType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class XAdESTimeStamp(XAdESTimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class SignedDataObjectProperties(SignedDataObjectPropertiesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class SignedPropertiesType:
    SignedSignatureProperties: Optional[SignedSignaturePropertiesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    SignedDataObjectProperties: Optional[SignedDataObjectPropertiesType] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            },
        )
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SignedSignatureProperties(SignedSignaturePropertiesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class UnsignedPropertiesType:
    UnsignedSignatureProperties: Optional[UnsignedSignaturePropertiesType] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            },
        )
    )
    UnsignedDataObjectProperties: Optional[
        UnsignedDataObjectPropertiesType
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class UnsignedSignatureProperties(UnsignedSignaturePropertiesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class QualifyingPropertiesType:
    SignedProperties: Optional[SignedPropertiesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    UnsignedProperties: Optional[UnsignedPropertiesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    Target: Optional[str] = field(
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
class SignedProperties(SignedPropertiesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class UnsignedProperties(UnsignedPropertiesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass
class QualifyingProperties(QualifyingPropertiesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"
