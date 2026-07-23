import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Property Document Vault | FirstChoice Property Hub",
    page_icon="📁",
    layout="wide"
)

st.title("📁 Smart Property Document Vault")

st.info(
    "Property Document Vault is currently under development."
)

st.subheader("🏡 Property Details")

property_name = st.text_input(
    "🏠 Property Name",
    value="My Property"
)

property_id = st.text_input(
    "🆔 Property ID",
    value="FC-PROP-001"
)

owner_name = st.text_input(
    "👤 Owner / Buyer Name"
)

st.subheader("📤 Upload Property Document")

document_name = st.text_input(
    "📄 Document Name",
    value="Property Document"
)

uploaded_file = st.file_uploader(
    "📤 Choose Document",
    type=["pdf", "jpg", "jpeg", "png", "doc", "docx"]
)

document_status = st.selectbox(
    "🔍 Verification Status",
    [
        "Pending",
        "Under Review",
        "Verified",
        "Requires Attention"
    ]
)

expiry_date = st.date_input(
    "📅 Expiry / Review Date",
    value=date.today()
)

confidential = st.checkbox(
    "🔐 Mark as Confidential"
)

if st.button(
    "📤 ADD DOCUMENT TO VAULT",
    use_container_width=True
):
    if uploaded_file:
        st.success(
            f"✅ {document_name} added to Property Document Vault."
        )
    else:
        st.warning(
            "⚠️ Please select a document first."
        )
