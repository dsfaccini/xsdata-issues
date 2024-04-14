from dataclasses import dataclass, field
from typing import List, Optional

from generated.ext.oasis_dssx_1_0_profiles_vr_cd1 import (
    SignedObjectIdentifierType,
)
from generated.ext.xad_es import DigestAlgAndValueType

__NAMESPACE__ = "urn:oasis:names:tc:dss-x:1.0:profiles:SignaturePolicy:schema#"


@dataclass
class ReturnSupportedSignaturePolicies:
    class Meta:
        namespace = (
            "urn:oasis:names:tc:dss-x:1.0:profiles:SignaturePolicy:schema#"
        )

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class SignatureIdentifier(SignedObjectIdentifierType):
    class Meta:
        namespace = (
            "urn:oasis:names:tc:dss-x:1.0:profiles:SignaturePolicy:schema#"
        )


@dataclass
class SignaturePolicyDetailsType:
    SignaturePolicyIdentifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:SignaturePolicy:schema#",
            "required": True,
        },
    )
    SignaturePolicyLocation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:SignaturePolicy:schema#",
        },
    )
    DigestAndAlgorithm: Optional[DigestAlgAndValueType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:SignaturePolicy:schema#",
        },
    )


@dataclass
class GenerateUnderSignaturePolicy(SignaturePolicyDetailsType):
    class Meta:
        namespace = (
            "urn:oasis:names:tc:dss-x:1.0:profiles:SignaturePolicy:schema#"
        )


@dataclass
class SignaturePolicy(SignaturePolicyDetailsType):
    class Meta:
        namespace = (
            "urn:oasis:names:tc:dss-x:1.0:profiles:SignaturePolicy:schema#"
        )


@dataclass
class SupportedSignaturePolicies:
    class Meta:
        namespace = (
            "urn:oasis:names:tc:dss-x:1.0:profiles:SignaturePolicy:schema#"
        )

    SupportedSignaturePolicy: List[SignaturePolicyDetailsType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class UsedSignaturePolicy(SignaturePolicyDetailsType):
    class Meta:
        namespace = (
            "urn:oasis:names:tc:dss-x:1.0:profiles:SignaturePolicy:schema#"
        )


@dataclass
class PolicySignaturePairType:
    SignatureIdentifier: Optional[SignatureIdentifier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:SignaturePolicy:schema#",
            "required": True,
        },
    )
    SignaturePolicy: Optional[SignaturePolicy] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:SignaturePolicy:schema#",
            "required": True,
        },
    )


@dataclass
class VerifiedUnderSignaturePolicyType:
    SignaturePolicy: Optional[SignaturePolicy] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:SignaturePolicy:schema#",
            "required": True,
        },
    )
    SignatureIdentifier: Optional[SignatureIdentifier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:SignaturePolicy:schema#",
        },
    )


@dataclass
class PolicySignaturePair(PolicySignaturePairType):
    class Meta:
        namespace = (
            "urn:oasis:names:tc:dss-x:1.0:profiles:SignaturePolicy:schema#"
        )


@dataclass
class VerifiedUnderSignaturePolicy(VerifiedUnderSignaturePolicyType):
    class Meta:
        namespace = (
            "urn:oasis:names:tc:dss-x:1.0:profiles:SignaturePolicy:schema#"
        )


@dataclass
class PolicySignaturePairsType:
    PolicySignaturePair: List[PolicySignaturePair] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:SignaturePolicy:schema#",
            "min_occurs": 1,
        },
    )


@dataclass
class ExplicitPolicies(PolicySignaturePairsType):
    class Meta:
        namespace = (
            "urn:oasis:names:tc:dss-x:1.0:profiles:SignaturePolicy:schema#"
        )


@dataclass
class VerifyUnderSignaturePolicyType:
    DefaultPolicy: Optional[SignaturePolicyDetailsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:SignaturePolicy:schema#",
        },
    )
    ExplicitPolicies: Optional[ExplicitPolicies] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:dss-x:1.0:profiles:SignaturePolicy:schema#",
        },
    )


@dataclass
class VerifyUnderSignaturePolicy(VerifyUnderSignaturePolicyType):
    class Meta:
        namespace = (
            "urn:oasis:names:tc:dss-x:1.0:profiles:SignaturePolicy:schema#"
        )
