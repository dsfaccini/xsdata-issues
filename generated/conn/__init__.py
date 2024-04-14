from generated.conn.certificate_service_common import (
    CertRefEnum,
    CheckCertificateDetailEnum,
    CheckCertificateDetails,
    CheckCertificateDetailsType,
    X509Certificate,
    X509DataInfoList,
    X509DataInfoListType,
)
from generated.conn.connector_common import (
    AttachmentType,
    CardHandle,
    ClientSystemId,
    Connector,
    EhcHandle,
    ErrorState,
    ErrorState_Severity,
    ErrorState_Type,
    HpcHandle,
    MandantId,
    OperatingState,
    Result,
    Result_value,
    SmcHandle,
    Status,
    UserId,
    VPNSISStatus_ConnectionStatus,
    VPNTIStatus_ConnectionStatus,
    WorkplaceId,
    WorkplaceIds,
    XmlSchema,
    XslStylesheet,
)
from generated.conn.connector_common import (
    Document as connector_commonDocument,
)
from generated.conn.connector_common import (
    DocumentType as connector_commonDocumentType,
)
from generated.conn.connector_context import (
    Context,
    ContextType,
)
from generated.conn.signature_service_v7_5_6 import (
    ActivateComfortSignature,
    ActivateComfortSignatureResponse,
    BinaryDocumentType,
    BinaryString,
    ComfortSignatureStatusEnum,
    CounterSignatureMarker,
    DeactivateComfortSignature,
    DeactivateComfortSignatureResponse,
    Deselected,
    DisplayableAttributes,
    DocumentWithSignature,
    ExternalAuthenticate,
    ExternalAuthenticateResponse,
    GetJobNumber,
    GetJobNumberResponse,
    GetSignatureMode,
    GetSignatureModeResponse,
    IncludeEContent,
    IncludeRevocationInfo,
    JobNumber,
    ReferenceToSignerCertificate,
    SessionInfo,
    ShortText,
    SignatureForm,
    SignatureForm_value,
    SignatureMode,
    SignatureModeEnum,
    SignatureSchemes,
    SignatureSchemes_value,
    SignatureServicePortType_ActivateComfortSignature,
    SignatureServicePortType_ActivateComfortSignature_input,
    SignatureServicePortType_ActivateComfortSignature_output,
    SignatureServicePortType_DeactivateComfortSignature,
    SignatureServicePortType_DeactivateComfortSignature_input,
    SignatureServicePortType_DeactivateComfortSignature_output,
    SignatureServicePortType_GetJobNumber,
    SignatureServicePortType_GetJobNumber_input,
    SignatureServicePortType_GetJobNumber_output,
    SignatureServicePortType_GetSignatureMode,
    SignatureServicePortType_GetSignatureMode_input,
    SignatureServicePortType_GetSignatureMode_output,
    SignatureServicePortType_SignDocument,
    SignatureServicePortType_SignDocument_input,
    SignatureServicePortType_SignDocument_output,
    SignatureServicePortType_StopSignature,
    SignatureServicePortType_StopSignature_input,
    SignatureServicePortType_StopSignature_output,
    SignatureServicePortType_VerifyDocument,
    SignatureServicePortType_VerifyDocument_input,
    SignatureServicePortType_VerifyDocument_output,
    SignDocument,
    SignDocument_Crypt,
    SignDocumentResponse,
    SignRequest,
    SignResponse,
    StopSignature,
    StopSignatureResponse,
    TvMode,
    TvMode_value,
    UseVerificationTime,
    VerificationResultType,
    VerificationResultType_HighLevelResult,
    VerificationResultType_TimestampType,
    VerifyDocument,
    VerifyDocumentResponse,
    ViewerInfo,
)
from generated.conn.signature_service_v7_5_6 import (
    Document as signature_service_v7_5_6Document,
)
from generated.conn.signature_service_v7_5_6 import (
    DocumentType as signature_service_v7_5_6DocumentType,
)

__all__ = [
    "CertRefEnum",
    "CheckCertificateDetailEnum",
    "CheckCertificateDetails",
    "CheckCertificateDetailsType",
    "X509Certificate",
    "X509DataInfoList",
    "X509DataInfoListType",
    "AttachmentType",
    "CardHandle",
    "ClientSystemId",
    "Connector",
    "connector_commonDocument",
    "connector_commonDocumentType",
    "EhcHandle",
    "ErrorState",
    "ErrorState_Severity",
    "ErrorState_Type",
    "HpcHandle",
    "MandantId",
    "OperatingState",
    "Result",
    "Result_value",
    "SmcHandle",
    "Status",
    "UserId",
    "VPNSISStatus_ConnectionStatus",
    "VPNTIStatus_ConnectionStatus",
    "WorkplaceId",
    "WorkplaceIds",
    "XmlSchema",
    "XslStylesheet",
    "Context",
    "ContextType",
    "ActivateComfortSignature",
    "ActivateComfortSignatureResponse",
    "BinaryDocumentType",
    "BinaryString",
    "ComfortSignatureStatusEnum",
    "CounterSignatureMarker",
    "DeactivateComfortSignature",
    "DeactivateComfortSignatureResponse",
    "Deselected",
    "DisplayableAttributes",
    "signature_service_v7_5_6Document",
    "signature_service_v7_5_6DocumentType",
    "DocumentWithSignature",
    "ExternalAuthenticate",
    "ExternalAuthenticateResponse",
    "GetJobNumber",
    "GetJobNumberResponse",
    "GetSignatureMode",
    "GetSignatureModeResponse",
    "IncludeEContent",
    "IncludeRevocationInfo",
    "JobNumber",
    "ReferenceToSignerCertificate",
    "SessionInfo",
    "ShortText",
    "SignDocument",
    "SignDocumentResponse",
    "SignDocument_Crypt",
    "SignRequest",
    "SignResponse",
    "SignatureForm",
    "SignatureForm_value",
    "SignatureMode",
    "SignatureModeEnum",
    "SignatureSchemes",
    "SignatureSchemes_value",
    "SignatureServicePortType_ActivateComfortSignature",
    "SignatureServicePortType_ActivateComfortSignature_input",
    "SignatureServicePortType_ActivateComfortSignature_output",
    "SignatureServicePortType_DeactivateComfortSignature",
    "SignatureServicePortType_DeactivateComfortSignature_input",
    "SignatureServicePortType_DeactivateComfortSignature_output",
    "SignatureServicePortType_GetJobNumber",
    "SignatureServicePortType_GetJobNumber_input",
    "SignatureServicePortType_GetJobNumber_output",
    "SignatureServicePortType_GetSignatureMode",
    "SignatureServicePortType_GetSignatureMode_input",
    "SignatureServicePortType_GetSignatureMode_output",
    "SignatureServicePortType_SignDocument",
    "SignatureServicePortType_SignDocument_input",
    "SignatureServicePortType_SignDocument_output",
    "SignatureServicePortType_StopSignature",
    "SignatureServicePortType_StopSignature_input",
    "SignatureServicePortType_StopSignature_output",
    "SignatureServicePortType_VerifyDocument",
    "SignatureServicePortType_VerifyDocument_input",
    "SignatureServicePortType_VerifyDocument_output",
    "StopSignature",
    "StopSignatureResponse",
    "TvMode",
    "TvMode_value",
    "UseVerificationTime",
    "VerificationResultType",
    "VerificationResultType_HighLevelResult",
    "VerificationResultType_TimestampType",
    "VerifyDocument",
    "VerifyDocumentResponse",
    "ViewerInfo",
]