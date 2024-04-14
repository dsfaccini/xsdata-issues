from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional

from xsdata.models.datatype import XmlDateTime

from generated.ext.xenc_schema import (
    EncryptedData,
    EncryptedKey,
)
from generated.ext.xmldsig_core_schema import (
    KeyInfo,
    Signature,
)

__NAMESPACE__ = "urn:oasis:names:tc:SAML:2.0:assertion"


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
            "required": True,
        },
    )


@dataclass
class AssertionIDRef:
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:2.0:assertion"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class AssertionURIRef:
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:2.0:assertion"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class AttributeValue:
    class Meta:
        nillable = True
        namespace = "urn:oasis:names:tc:SAML:2.0:assertion"

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
        namespace = "urn:oasis:names:tc:SAML:2.0:assertion"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class AuthenticatingAuthority:
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:2.0:assertion"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class AuthnContextClassRef:
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:2.0:assertion"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class AuthnContextDecl:
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:2.0:assertion"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AuthnContextDeclRef:
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:2.0:assertion"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class BaseIDAbstractType:
    NameQualifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    SPNameQualifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ConditionAbstractType:
    pass


class DecisionType(Enum):
    PERMIT = "Permit"
    DENY = "Deny"
    INDETERMINATE = "Indeterminate"


@dataclass
class NameIDType:
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
    SPNameQualifier: Optional[str] = field(
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
    SPProvidedID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class StatementAbstractType:
    pass


@dataclass
class SubjectConfirmationDataType:
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
    Recipient: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    InResponseTo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    Address: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
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
class SubjectLocalityType:
    Address: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    DNSName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Action(ActionType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:2.0:assertion"


@dataclass
class AttributeType:
    AttributeValue: List[AttributeValue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
            "nillable": True,
        },
    )
    Name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    NameFormat: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    FriendlyName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )


@dataclass
class AudienceRestrictionType(ConditionAbstractType):
    Audience: List[Audience] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
            "min_occurs": 1,
        },
    )


@dataclass
class AuthnContextType:
    AuthnContextClassRef: Optional[AuthnContextClassRef] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
            "required": True,
        },
    )
    AuthnContextDecl: List[AuthnContextDecl] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    AuthnContextDeclRef: List[AuthnContextDeclRef] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    AuthenticatingAuthority: List[AuthenticatingAuthority] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
        },
    )


@dataclass
class BaseID(BaseIDAbstractType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:2.0:assertion"


@dataclass
class Condition(ConditionAbstractType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:2.0:assertion"


@dataclass
class EncryptedElementType:
    EncryptedData: Optional[EncryptedData] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/04/xmlenc#",
            "required": True,
        },
    )
    EncryptedKey: List[EncryptedKey] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/04/xmlenc#",
        },
    )


@dataclass
class Issuer(NameIDType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:2.0:assertion"


@dataclass
class KeyInfoConfirmationDataType(SubjectConfirmationDataType):
    other_attributes: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    KeyInfo: List[KeyInfo] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
        },
    )


@dataclass
class NameID(NameIDType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:2.0:assertion"


@dataclass
class OneTimeUseType(ConditionAbstractType):
    pass


@dataclass
class ProxyRestrictionType(ConditionAbstractType):
    Audience: List[Audience] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
        },
    )
    Count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Statement(StatementAbstractType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:2.0:assertion"


@dataclass
class SubjectConfirmationData(SubjectConfirmationDataType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:2.0:assertion"


@dataclass
class SubjectLocality(SubjectLocalityType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:2.0:assertion"


@dataclass
class Attribute(AttributeType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:2.0:assertion"


@dataclass
class AudienceRestriction(AudienceRestrictionType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:2.0:assertion"


@dataclass
class AuthnContext(AuthnContextType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:2.0:assertion"


@dataclass
class EncryptedAssertion(EncryptedElementType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:2.0:assertion"


@dataclass
class EncryptedAttribute(EncryptedElementType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:2.0:assertion"


@dataclass
class EncryptedID(EncryptedElementType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:2.0:assertion"


@dataclass
class OneTimeUse(OneTimeUseType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:2.0:assertion"


@dataclass
class ProxyRestriction(ProxyRestrictionType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:2.0:assertion"


@dataclass
class AttributeStatementType(StatementAbstractType):
    Attribute: List[Attribute] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
        },
    )
    EncryptedAttribute: List[EncryptedAttribute] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
        },
    )


@dataclass
class AuthnStatementType(StatementAbstractType):
    SubjectLocality: Optional[SubjectLocality] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
        },
    )
    AuthnContext: Optional[AuthnContext] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
            "required": True,
        },
    )
    AuthnInstant: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    SessionIndex: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    SessionNotOnOrAfter: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ConditionsType:
    Condition: List[Condition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
        },
    )
    AudienceRestriction: List[AudienceRestriction] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
        },
    )
    OneTimeUse: List[OneTimeUse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
        },
    )
    ProxyRestriction: List[ProxyRestriction] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
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
class SubjectConfirmationType:
    BaseID: Optional[BaseID] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
        },
    )
    NameID: Optional[NameID] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
        },
    )
    EncryptedID: Optional[EncryptedID] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
        },
    )
    SubjectConfirmationData: Optional[SubjectConfirmationData] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
        },
    )
    Method: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class AttributeStatement(AttributeStatementType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:2.0:assertion"


@dataclass
class AuthnStatement(AuthnStatementType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:2.0:assertion"


@dataclass
class Conditions(ConditionsType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:2.0:assertion"


@dataclass
class SubjectConfirmation(SubjectConfirmationType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:2.0:assertion"


@dataclass
class SubjectType:
    BaseID: Optional[BaseID] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
        },
    )
    NameID: Optional[NameID] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
        },
    )
    EncryptedID: Optional[EncryptedID] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
        },
    )
    SubjectConfirmation: List[SubjectConfirmation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
            "min_occurs": 1,
            "sequence": 1,
        },
    )


@dataclass
class Subject(SubjectType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:2.0:assertion"


@dataclass
class AssertionType:
    Issuer: Optional[Issuer] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
            "required": True,
        },
    )
    Signature: Optional[Signature] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    Subject: Optional[Subject] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
        },
    )
    Conditions: Optional[Conditions] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
        },
    )
    Advice: Optional["Advice"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
        },
    )
    Statement: List[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
        },
    )
    AuthnStatement: List[AuthnStatement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
        },
    )
    AuthzDecisionStatement: List["AuthzDecisionStatement"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
        },
    )
    AttributeStatement: List[AttributeStatement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
        },
    )
    Version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    ID: Optional[str] = field(
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
        namespace = "urn:oasis:names:tc:SAML:2.0:assertion"


@dataclass
class AdviceType:
    AssertionIDRef: List[AssertionIDRef] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
        },
    )
    AssertionURIRef: List[AssertionURIRef] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
        },
    )
    Assertion: List[Assertion] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
        },
    )
    EncryptedAssertion: List[EncryptedAssertion] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
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
    AssertionIDRef: List[AssertionIDRef] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
        },
    )
    AssertionURIRef: List[AssertionURIRef] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
        },
    )
    Assertion: List[Assertion] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
        },
    )
    EncryptedAssertion: List[EncryptedAssertion] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
        },
    )


@dataclass
class Advice(AdviceType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:2.0:assertion"


@dataclass
class Evidence(EvidenceType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:2.0:assertion"


@dataclass
class AuthzDecisionStatementType(StatementAbstractType):
    Action: List[Action] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
            "min_occurs": 1,
        },
    )
    Evidence: Optional[Evidence] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:SAML:2.0:assertion",
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
class AuthzDecisionStatement(AuthzDecisionStatementType):
    class Meta:
        namespace = "urn:oasis:names:tc:SAML:2.0:assertion"
