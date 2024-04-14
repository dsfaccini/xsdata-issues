from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xml.etree.ElementTree import QName

from xsdata.models.datatype import XmlDateTime

from generated.ext.xmldsig_core_schema import (
    KeyInfo,
    Signature,
)

__NAMESPACE__ = "urn:oasis:names:tc:SAML:1.0:assertion"


@dataclass
class ActionType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    Namespace: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class AssertionIDReference:
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:1.0:assertion"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class AttributeDesignatorType:
    AttributeName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    AttributeNamespace: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class AttributeValue:
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:1.0:assertion"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Audience:
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:1.0:assertion"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class AuthorityBindingType:
    AuthorityKind: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    Location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    Binding: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ConditionAbstractType:
    pass


@dataclass
class ConfirmationMethod:
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:1.0:assertion"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


class DecisionType(Enum):
    PERMIT = "Permit"
    DENY = "Deny"
    INDETERMINATE = "Indeterminate"


@dataclass
class NameIdentifierType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    NameQualifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    Format: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class StatementAbstractType:
    pass


@dataclass
class SubjectConfirmationData:
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:1.0:assertion"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class SubjectLocalityType:
    IPAddress: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    DNSAddress: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Action(ActionType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:1.0:assertion"


@dataclass
class AttributeDesignator(AttributeDesignatorType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:1.0:assertion"


@dataclass
class AttributeType(AttributeDesignatorType):
    AttributeValue: List[AttributeValue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:1.0:assertion",
            "min_occurs": 1,
        },
    )


@dataclass
class AudienceRestrictionConditionType(ConditionAbstractType):
    Audience: List[Audience] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:1.0:assertion",
            "min_occurs": 1,
        },
    )


@dataclass
class AuthorityBinding(AuthorityBindingType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:1.0:assertion"


@dataclass
class Condition(ConditionAbstractType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:1.0:assertion"


@dataclass
class DoNotCacheConditionType(ConditionAbstractType):
    pass


@dataclass
class NameIdentifier(NameIdentifierType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:1.0:assertion"


@dataclass
class Statement(StatementAbstractType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:1.0:assertion"


@dataclass
class SubjectConfirmationType:
    ConfirmationMethod: List[ConfirmationMethod] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:1.0:assertion",
            "min_occurs": 1,
        },
    )
    SubjectConfirmationData: Optional[SubjectConfirmationData] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:1.0:assertion",
        },
    )
    KeyInfo: Optional[KeyInfo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )


@dataclass
class SubjectLocality(SubjectLocalityType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:1.0:assertion"


@dataclass
class Attribute(AttributeType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:1.0:assertion"


@dataclass
class AudienceRestrictionCondition(AudienceRestrictionConditionType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:1.0:assertion"


@dataclass
class DoNotCacheCondition(DoNotCacheConditionType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:1.0:assertion"


@dataclass
class SubjectConfirmation(SubjectConfirmationType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:1.0:assertion"


@dataclass
class ConditionsType:
    AudienceRestrictionCondition: List[AudienceRestrictionCondition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:1.0:assertion",
        },
    )
    DoNotCacheCondition: List[DoNotCacheCondition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:1.0:assertion",
        },
    )
    Condition: List[Condition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:1.0:assertion",
        },
    )
    NotBefore: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    NotOnOrAfter: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SubjectType:
    NameIdentifier: Optional[NameIdentifier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:1.0:assertion",
            "required": True,
        },
    )
    SubjectConfirmation: List[SubjectConfirmation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:1.0:assertion",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequence": 1,
        },
    )


@dataclass
class Conditions(ConditionsType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:1.0:assertion"


@dataclass
class Subject(SubjectType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:1.0:assertion"


@dataclass
class SubjectStatementAbstractType(StatementAbstractType):
    Subject: Optional[Subject] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:1.0:assertion",
            "required": True,
        },
    )


@dataclass
class AttributeStatementType(SubjectStatementAbstractType):
    Attribute: List[Attribute] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:1.0:assertion",
            "min_occurs": 1,
        },
    )


@dataclass
class AuthenticationStatementType(SubjectStatementAbstractType):
    SubjectLocality: Optional[SubjectLocality] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:1.0:assertion",
        },
    )
    AuthorityBinding: List[AuthorityBinding] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:1.0:assertion",
        },
    )
    AuthenticationMethod: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    AuthenticationInstant: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class SubjectStatement(SubjectStatementAbstractType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:1.0:assertion"


@dataclass
class AttributeStatement(AttributeStatementType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:1.0:assertion"


@dataclass
class AuthenticationStatement(AuthenticationStatementType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:1.0:assertion"


@dataclass
class AssertionType:
    Conditions: Optional[Conditions] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:1.0:assertion",
        },
    )
    Advice: Optional["Advice"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:1.0:assertion",
        },
    )
    Statement: List[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:1.0:assertion",
        },
    )
    SubjectStatement: List[SubjectStatement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:1.0:assertion",
        },
    )
    AuthenticationStatement: List[AuthenticationStatement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:1.0:assertion",
        },
    )
    AuthorizationDecisionStatement: List["AuthorizationDecisionStatement"] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:oasis:names:tc:SAML:1.0:assertion",
            },
        )
    )
    AttributeStatement: List[AttributeStatement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:1.0:assertion",
        },
    )
    Signature: Optional[Signature] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    MajorVersion: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    MinorVersion: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    AssertionID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    Issuer: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    IssueInstant: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Assertion(AssertionType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:1.0:assertion"


@dataclass
class AdviceType:
    AssertionIDReference: List[AssertionIDReference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:1.0:assertion",
        },
    )
    Assertion: List[Assertion] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:1.0:assertion",
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
class EvidenceType:
    AssertionIDReference: List[AssertionIDReference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:1.0:assertion",
        },
    )
    Assertion: List[Assertion] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:1.0:assertion",
        },
    )


@dataclass
class Advice(AdviceType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:1.0:assertion"


@dataclass
class Evidence(EvidenceType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:1.0:assertion"


@dataclass
class AuthorizationDecisionStatementType(SubjectStatementAbstractType):
    Action: List[Action] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:1.0:assertion",
            "min_occurs": 1,
        },
    )
    Evidence: Optional[Evidence] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:1.0:assertion",
        },
    )
    Resource: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    Decision: Optional[DecisionType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class AuthorizationDecisionStatement(AuthorizationDecisionStatementType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:1.0:assertion"
