import streamlit as st
from datetime import datetime, date
import uuid

# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 25
# PROPERTY POST + COLLABORATION + ENQUIRY HUB
#
# COMBINED:
# PAGE 2 + PAGE 25
#
# FEATURES:
# 🏡 Property Posting
# 🆔 Unique Property ID
# ❤️ Like
# ⭐ Save
# 👋 Interest
# 📩 Enquiry
# 👤 Original Property Poster
# 💬 Message Centre
# 📅 Follow-up
# ✅ Task Board
# 👥 Collaboration
# 📊 Activity Summary
# ⬅️ Back
# 🏠 Home
# 📋 Page Menu
#
# FILE:
# 25_property_collaboration_hub.py
# ============================================================


# ============================================================
# NAVIGATION IMPORT
# ============================================================

try:
    from navigation import show_navigation, set_current_page
except ImportError:

    def show_navigation():
        pass

    def set_current_page(current_page):
        pass


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Property Collaboration Hub | FirstChoice Infra",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# REGISTER CURRENT PAGE
# ============================================================

try:
    set_current_page(
        "25_property_collaboration_hub.py"
    )
except Exception:
    pass


# ============================================================
# COMMON NAVIGATION
# ============================================================

try:
    show_navigation()
except Exception:
    pass


# ============================================================
# SESSION STATE
# ============================================================

if "properties" not in st.session_state:
    st.session_state.properties = []


if "property_likes" not in st.session_state:
    st.session_state.property_likes = []


if "property_saved" not in st.session_state:
    st.session_state.property_saved = []


if "property_interests" not in st.session_state:
    st.session_state.property_interests = []


if "property_enquiries" not in st.session_state:
    st.session_state.property_enquiries = []


if "property_messages" not in st.session_state:
    st.session_state.property_messages = []


if "property_tasks" not in st.session_state:
    st.session_state.property_tasks = []


if "property_followups" not in st.session_state:
    st.session_state.property_followups = []


# ============================================================
# PREMIUM UI
# ============================================================

st.markdown(
    """
<style>

.stApp {

    background:
    linear-gradient(
        135deg,
        #F5F7FF 0%,
        #FFF7ED 35%,
        #FDF4FF 70%,
        #ECFEFF 100%
    );

}


header {

    visibility: hidden;

}


#MainMenu {

    visibility: hidden;

}


footer {

    visibility: hidden;

}


/* HERO */

.hero {

    padding: 52px;

    border-radius: 36px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #020617,
        #1D4ED8,
        #7C3AED,
        #DB2777
    );

    box-shadow:
    0 24px 75px
    rgba(37,99,235,0.32);

    margin-bottom: 32px;

}


.hero h1 {

    font-size: 46px;

    font-weight: 900;

}


.hero p {

    font-size: 18px;

    line-height: 1.8;

}


/* SECTION */

.section {

    margin-top: 32px;

    margin-bottom: 22px;

    padding: 30px 34px;

    border-radius: 28px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #1E3A8A,
        #4F46E5,
        #9333EA,
        #EC4899
    );

    box-shadow:
    0 14px 40px
    rgba(79,70,229,0.22);

}


.section h2 {

    margin: 0;

    font-size: 29px;

    font-weight: 900;

}


/* AI CARD */

.ai-card {

    padding: 32px;

    border-radius: 30px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #4C1D95,
        #7C3AED,
        #C026D3
    );

    box-shadow:
    0 18px 55px
    rgba(124,58,237,0.25);

}


/* TRUST */

.trust-card {

    padding: 32px;

    border-radius: 30px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #047857,
        #059669,
        #10B981
    );

    box-shadow:
    0 18px 55px
    rgba(5,150,105,0.25);

}


/* INFO */

.info-card {

    padding: 30px;

    border-radius: 28px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #0369A1,
        #0284C7,
        #06B6D4
    );

    box-shadow:
    0 18px 55px
    rgba(3,105,161,0.22);

}


/* PROPERTY ID */

.property-id-card {

    padding: 30px;

    border-radius: 28px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #047857,
        #059669,
        #10B981
    );

    box-shadow:
    0 18px 50px
    rgba(5,150,105,0.25);

    margin-top: 25px;

}


.property-id-card h1 {

    font-size: 36px;

    font-weight: 900;

}


/* POSTER */

.poster-card {

    padding: 30px;

    border-radius: 28px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #0F172A,
        #1E40AF,
        #7C3AED
    );

    box-shadow:
    0 18px 55px
    rgba(30,64,175,0.25);

}


/* ENQUIRY */

.enquiry-card {

    padding: 28px;

    border-radius: 26px;

    background:
    linear-gradient(
        135deg,
        #FFFFFF,
        #EFF6FF,
        #F5F3FF
    );

    border-left:
    6px solid #7C3AED;

    box-shadow:
    0 12px 35px
    rgba(0,0,0,0.08);

    margin-bottom: 18px;

}


/* FINAL */

.final-card {

    padding: 35px;

    border-radius: 30px;

    color: white;

    text-align: center;

    background:
    linear-gradient(
        135deg,
        #071952,
        #2563EB,
        #7C3AED,
        #EC4899
    );

    box-shadow:
    0 20px 60px
    rgba(124,58,237,0.25);

}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# HERO
# ============================================================

st.markdown(
    """
<div class="hero">

<h1>
🏡 Property Post & Collaboration Hub
</h1>

<p>
Post your property, connect with genuine buyers and manage
all property enquiries from one smart workspace.
</p>

<p>
📸 Photos • 🎥 Video • 📍 Location • 💰 Pricing
</p>

<p>
❤️ Likes • ⭐ Saves • 👋 Interest • 📩 Enquiries
</p>

<p>
💬 Messages • 📅 Follow-ups • ✅ Tasks •
🏠 Site Visits • 🤝 Collaboration • 📝 Booking
</p>

</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# SMART SYSTEM
# ============================================================

st.markdown(
    """
<div class="ai-card">

<h2>
🤖 Smart Property Connection System
</h2>

<p>
Every property receives a unique Property ID.
</p>

<p>
All Likes, Saves, Interests, Enquiries, Messages,
Tasks and Follow-ups remain connected to that Property ID.
</p>

<p>
The original property poster remains the primary enquiry
recipient for that property.
</p>

<p>
<strong>
Property Post → Property ID → Listing →
Like / Save / Interest → Enquiry →
Original Poster → Communication →
Follow-up → Site Visit → Negotiation → Booking
</strong>
</p>

</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# PROPERTY POSTING
# ============================================================

st.markdown(
    """
<div class="section">

<h2>
🏡 Step 1 — Post Your Property
</h2>

<p>
Create a complete property listing.
</p>

</div>
""",
    unsafe_allow_html=True
)


profile_type = st.radio(
    "👤 Who are you?",
    [
        "👤 Owner",
        "🏢 Agent / Broker",
        "🏗️ Builder / Developer",
        "🏛️ Company / Organization"
    ],
    horizontal=True
)


purpose = st.radio(
    "🎯 What do you want to do?",
    [
        "🏠 Sell",
        "🔑 Rent",
        "📈 Lease",
        "🤝 Joint Venture"
    ],
    horizontal=True
)


# ============================================================
# BASIC PROPERTY
# ============================================================

st.markdown(
    """
<div class="section">

<h2>
🏠 Property Information
</h2>

</div>
""",
    unsafe_allow_html=True
)


c1, c2 = st.columns(2)


with c1:

    property_title = st.text_input(
        "Property Title *",
        placeholder="Example: Premium 3 BHK Luxury Apartment"
    )


with c2:

    property_type = st.selectbox(
        "Property Type *",
        [
            "Apartment",
            "Flat",
            "Villa",
            "Independent House",
            "Plot",
            "Residential Land",
            "Farm Land",
            "Commercial Office",
            "Shop",
            "Warehouse",
            "Industrial Property",
            "Other"
        ]
    )


c3, c4, c5 = st.columns(3)


with c3:

    bhk = st.selectbox(
        "BHK",
        [
            "Not Applicable",
            "1 BHK",
            "2 BHK",
            "3 BHK",
            "4 BHK",
            "5 BHK",
            "5+ BHK"
        ]
    )


with c4:

    area = st.number_input(
        "Property Area (Sq.Ft.)",
        min_value=0,
        step=100
    )


with c5:

    property_age = st.selectbox(
        "Property Age",
        [
            "New Construction",
            "0–1 Year",
            "1–5 Years",
            "5–10 Years",
            "10+ Years"
        ]
    )


description = st.text_area(
    "Property Description",
    height=150,
    placeholder="Describe your property, features, surroundings and unique benefits..."
)


# ============================================================
# LOCATION
# ============================================================

st.markdown(
    """
<div class="section">

<h2>
📍 Property Location
</h2>

</div>
""",
    unsafe_allow_html=True
)


l1, l2 = st.columns(2)


with l1:

    state = st.selectbox(
        "State *",
        [
            "Maharashtra",
            "Madhya Pradesh",
            "Gujarat",
            "Karnataka",
            "Telangana",
            "Delhi",
            "Uttar Pradesh",
            "Rajasthan",
            "Tamil Nadu",
            "Other"
        ]
    )


with l2:

    city = st.text_input(
        "City *",
        placeholder="Example: Nagpur"
    )


l3, l4 = st.columns(2)


with l3:

    locality = st.text_input(
        "Locality / Area *",
        placeholder="Example: Civil Lines"
    )


with l4:

    pincode = st.text_input(
        "PIN Code *",
        max_chars=6,
        placeholder="440001"
    )


address = st.text_area(
    "Complete Property Address",
    placeholder="Enter complete address..."
)


# ============================================================
# PRICING
# ============================================================

st.markdown(
    """
<div class="section">

<h2>
💰 Pricing & Financial Details
</h2>

</div>
""",
    unsafe_allow_html=True
)


p1, p2, p3 = st.columns(3)


with p1:

    price = st.number_input(
        "Expected Price (₹)",
        min_value=0,
        step=100000
    )


with p2:

    price_negotiable = st.checkbox(
        "Price Negotiable"
    )


with p3:

    maintenance = st.number_input(
        "Monthly Maintenance (₹)",
        min_value=0,
        step=500
    )


# ============================================================
# AMENITIES
# ============================================================

st.markdown(
    """
<div class="section">

<h2>
✨ Property Amenities
</h2>

</div>
""",
    unsafe_allow_html=True
)


amenities = st.multiselect(
    "Available Amenities",
    [
        "🚗 Parking",
        "🏊 Swimming Pool",
        "🏋️ Gym",
        "🌳 Garden",
        "🔒 Security",
        "🛗 Lift",
        "⚡ Power Backup",
        "💧 Water Supply",
        "🔥 Gas Pipeline",
        "📶 Internet",
        "🏫 School Nearby",
        "🏥 Hospital Nearby",
        "🛒 Market Nearby",
        "🚇 Public Transport"
    ]
)


# ============================================================
# MEDIA
# ============================================================

st.markdown(
    """
<div class="section">

<h2>
📸 Property Photos & 🎥 Video
</h2>

</div>
""",
    unsafe_allow_html=True
)


photos = st.file_uploader(
    "Upload Property Photos",
    type=[
        "jpg",
        "jpeg",
        "png",
        "webp"
    ],
    accept_multiple_files=True
)


video = st.file_uploader(
    "Upload Property Video",
    type=[
        "mp4",
        "mov",
        "avi"
    ]
)


video_url = st.text_input(
    "Or paste YouTube / Property Video URL",
    placeholder="https://youtube.com/..."
)


if photos:

    st.success(
        f"{len(photos)} property photo(s) selected."
    )


if video:

    st.success(
        "Property video selected successfully."
    )


# ============================================================
# VERIFICATION
# ============================================================

st.markdown(
    """
<div class="section">

<h2>
🛡️ Identity & Property Verification
</h2>

</div>
""",
    unsafe_allow_html=True
)


st.markdown(
    """
<div class="trust-card">

<h2>
🛡️ Build Trust With Verified Listings
</h2>

<p>
Verified profiles may receive stronger trust signals
and better visibility in future versions.
</p>

<p>✅ Mobile Number Verification</p>
<p>✅ Identity Verification</p>
<p>✅ Property Ownership Verification</p>
<p>✅ RERA Verification for Applicable Projects</p>

</div>
""",
    unsafe_allow_html=True
)


v1, v2 = st.columns(2)


with v1:

    mobile = st.text_input(
        "Current Mobile Number *",
        max_chars=10,
        placeholder="10 digit mobile number"
    )


with v2:

    identity_type = st.selectbox(
        "Identity Verification",
        [
            "Verify Later",
            "Aadhaar-based Verification",
            "Other Government ID"
        ]
    )


st.info(
    "🔐 Aadhaar numbers should not be stored directly in the application. "
    "Production version में compliant KYC provider integrate किया जाएगा।"
)


# ============================================================
# CONTACT
# ============================================================

st.markdown(
    """
<div class="section">

<h2>
📞 Contact Preferences
</h2>

</div>
""",
    unsafe_allow_html=True
)


contact_options = st.multiselect(
    "Preferred Contact Methods",
    [
        "📞 Phone Call",
        "💬 WhatsApp",
        "✉️ Email",
        "💬 In-App Chat"
    ]
)


# ============================================================
# TERMS
# ============================================================

agree = st.checkbox(
    "I confirm that the information provided is accurate and I have the right to list this property."
)


# ============================================================
# SUBMIT
# ============================================================

st.markdown(
    """
<div class="final-card">

<h2>
🚀 Ready to Publish Your Property?
</h2>

<p>
Your Property ID will connect all future interactions.
</p>

</div>
""",
    unsafe_allow_html=True
)


if st.button(
    "🚀 SUBMIT PROPERTY LISTING",
    use_container_width=True
):

    if not property_title:

        st.error(
            "Please enter the Property Title."
        )

    elif not city:

        st.error(
            "Please enter the City."
        )

    elif not locality:

        st.error(
            "Please enter the Locality."
        )

    elif not mobile:

        st.error(
            "Please enter your current mobile number."
        )

    elif (
        len(mobile) != 10
        or not mobile.isdigit()
    ):

        st.error(
            "Please enter a valid 10-digit mobile number."
        )

    elif not agree:

        st.warning(
            "Please confirm the declaration before submitting."
        )

    else:

        # ====================================================
        # UNIQUE PROPERTY ID
        # ====================================================

        property_id = (
            "FC-PROP-"
            +
            uuid.uuid4()
            .hex[:8]
            .upper()
        )


        # ====================================================
        # ORIGINAL POSTER
        # ====================================================

        poster_id = st.session_state.get(
            "user_id",
            mobile
        )


        poster_name = st.session_state.get(
            "user_name",
            mobile
        )


        # ====================================================
        # PROPERTY DATA
        # ====================================================

        property_data = {

            "property_id":
            property_id,

            "poster_id":
            poster_id,

            "poster_name":
            poster_name,

            "poster_mobile":
            mobile,

            "poster_role":
            profile_type,

            "property_title":
            property_title,

            "property_type":
            property_type,

            "purpose":
            purpose,

            "bhk":
            bhk,

            "area":
            area,

            "property_age":
            property_age,

            "description":
            description,

            "state":
            state,

            "city":
            city,

            "locality":
            locality,

            "pincode":
            pincode,

            "address":
            address,

            "price":
            price,

            "price_negotiable":
            price_negotiable,

            "maintenance":
            maintenance,

            "amenities":
            amenities,

            "photo_count":
            len(photos)
            if photos
            else 0,

            "video_uploaded":
            True
            if video
            else False,

            "video_url":
            video_url,

            "identity_type":
            identity_type,

            "verification_status":
            "Pending",

            "contact_options":
            contact_options,

            "listing_status":
            "Pending Review",

            "created_at":
            datetime.now().strftime(
                "%d-%m-%Y %I:%M %p"
            )

        }


        # ====================================================
        # SAVE
        # ====================================================

        st.session_state.properties.append(
            property_data
        )


        st.session_state[
            "last_property_id"
        ] = property_id


        st.success(
            "🎉 Your property listing has been submitted successfully!"
        )


        st.markdown(
            f"""
<div class="property-id-card">

<p>
🆔 Your Unique Property ID
</p>

<h1>
{property_id}
</h1>

<p>
Keep this Property ID for tracking your property listing.
</p>

</div>
""",
            unsafe_allow_html=True
        )


        st.markdown(
            f"""
<div class="info-card">

<h3>
🔗 Smart Property Connection Activated
</h3>

<p>
<b>Property ID:</b>
{property_id}
</p>

<p>
<b>Property Posted By:</b>
{poster_name}
</p>

<p>
<b>Poster ID:</b>
{poster_id}
</p>

<p>
❤️ Likes, ⭐ Saves, 👋 Interests and 📩 Enquiries
will remain connected to this property.
</p>

</div>
""",
            unsafe_allow_html=True
        )


        st.info(
            "Next step: Mobile OTP verification and listing review."
        )


# ============================================================
# COLLABORATION WORKSPACE
# ============================================================

st.markdown(
    """
<div class="section">

<h2>
💬 Step 2 — Property Collaboration & Enquiry Workspace
</h2>

<p>
Select a posted property to manage its enquiries,
communication, tasks and follow-ups.
</p>

</div>
""",
    unsafe_allow_html=True
)


if st.session_state.properties:

    property_options = {

        f"{p['property_title']} | {p['property_id']}":
        p["property_id"]

        for p in st.session_state.properties

    }


    selected_property_label = st.selectbox(
        "🏡 Select Property",
        list(property_options.keys()),
        key="collaboration_property_selector"
    )


    selected_property_id = property_options[
        selected_property_label
    ]


    selected_property = next(

        (
            p

            for p in st.session_state.properties

            if p["property_id"]
            ==
            selected_property_id
        ),

        None

    )

else:

    selected_property = None

    selected_property_id = ""


    st.info(
        "📭 No property has been posted yet. "
        "Post a property above to activate the collaboration workspace."
    )


# ============================================================
# PROPERTY WORKSPACE
# ============================================================

if selected_property:

    property_id = selected_property["property_id"]

    property_name = selected_property["property_title"]

    poster_id = selected_property["poster_id"]

    poster_name = selected_property["poster_name"]

    poster_mobile = selected_property["poster_mobile"]

    poster_role = selected_property["poster_role"]


    # ========================================================
    # ORIGINAL POSTER
    # ========================================================

    st.markdown(
        """
<div class="section">

<h2>
👤 Original Property Poster
</h2>

</div>
""",
        unsafe_allow_html=True
    )


    st.markdown(
        f"""
<div class="poster-card">

<h2>
📌 Enquiry Routing Rule
</h2>

<p>
<strong>Property:</strong>
{property_name}
</p>

<p>
<strong>Property ID:</strong>
{property_id}
</p>

<p>
<strong>Original Poster:</strong>
{poster_name}
</p>

<p>
<strong>Poster ID:</strong>
{poster_id}
</p>

<p>
<strong>Role:</strong>
{poster_role}
</p>

<p>
<strong>Enquiries will be routed to:</strong>
{poster_mobile}
</p>

</div>
""",
        unsafe_allow_html=True
    )


    # ========================================================
    # INTERACTION
    # ========================================================

    st.markdown(
        """
<div class="section">

<h2>
❤️ Property Interest & Enquiry
</h2>

</div>
""",
        unsafe_allow_html=True
    )


    b1, b2, b3 = st.columns(3)


    with b1:

        interested_user = st.text_input(
            "👤 Interested User Name",
            key="workspace_interested_user"
        )


    with b2:

        interested_mobile = st.text_input(
            "📱 Interested User Mobile",
            max_chars=10,
            key="workspace_interested_mobile"
        )


    with b3:

        interested_email = st.text_input(
            "✉️ Email",
            key="workspace_interested_email"
        )


    i1, i2, i3 = st.columns(3)


    with i1:

        like_property = st.button(
            "❤️ LIKE PROPERTY",
            use_container_width=True,
            key="like_property_button"
        )


    with i2:

        save_property = st.button(
            "⭐ SAVE PROPERTY",
            use_container_width=True,
            key="save_property_button"
        )


    with i3:

        show_interest = st.button(
            "👋 I'M INTERESTED",
            use_container_width=True,
            key="interest_property_button"
        )


    if like_property:

        st.session_state.property_likes.append({

            "Property ID":
            property_id,

            "Property":
            property_name,

            "Original Poster ID":
            poster_id,

            "Interested User":
            interested_user,

            "Mobile":
            interested_mobile,

            "Time":
            datetime.now().strftime(
                "%d-%m-%Y %I:%M %p"
            )

        })

        st.success(
            "❤️ Property liked successfully."
        )


    if save_property:

        st.session_state.property_saved.append({

            "Property ID":
            property_id,

            "Property":
            property_name,

            "Original Poster ID":
            poster_id,

            "Saved By":
            interested_user,

            "Mobile":
            interested_mobile,

            "Time":
            datetime.now().strftime(
                "%d-%m-%Y %I:%M %p"
            )

        })

        st.success(
            "⭐ Property saved successfully."
        )


    if show_interest:

        st.session_state.property_interests.append({

            "Property ID":
            property_id,

            "Property":
            property_name,

            "Original Poster ID":
            poster_id,

            "Interested User":
            interested_user,

            "Mobile":
            interested_mobile,

            "Email":
            interested_email,

            "Time":
            datetime.now().strftime(
                "%d-%m-%Y %I:%M %p"
            )

        })

        st.success(
            "👋 Interest registered successfully."
        )


    # ========================================================
    # ENQUIRY
    # ========================================================

    st.markdown(
        """
<div class="section">

<h2>
📨 Send Enquiry to Original Property Poster
</h2>

</div>
""",
        unsafe_allow_html=True
    )


    enquiry_type = st.selectbox(
        "📌 Enquiry Type",
        [
            "General Property Enquiry",
            "Price Enquiry",
            "Request Property Details",
            "Request Call Back",
            "Request WhatsApp Contact",
            "Request Site Visit",
            "Booking Enquiry",
            "Investment Enquiry",
            "Loan / Finance Enquiry"
        ],
        key="workspace_enquiry_type"
    )


    enquiry_message = st.text_area(
        "💬 Enquiry Message",
        placeholder="Write your enquiry about this property...",
        key="workspace_enquiry_message"
    )


    if st.button(
        "📨 SEND ENQUIRY TO ORIGINAL PROPERTY POSTER",
        use_container_width=True,
        key="send_property_enquiry"
    ):

        if not interested_user:

            st.warning(
                "⚠️ Please enter interested user's name."
            )

        elif not interested_mobile:

            st.warning(
                "⚠️ Please enter interested user's mobile number."
            )

        else:

            new_enquiry = {

                "Property ID":
                property_id,

                "Property":
                property_name,

                "Poster ID":
                poster_id,

                "Poster Name":
                poster_name,

                "Poster Role":
                poster_role,

                "Poster Mobile":
                poster_mobile,

                "Interested User":
                interested_user,

                "Interested Mobile":
                interested_mobile,

                "Interested Email":
                interested_email,

                "Enquiry Type":
                enquiry_type,

                "Message":
                enquiry_message,

                "Status":
                "New",

                "Created":
                datetime.now().strftime(
                    "%d-%m-%Y %I:%M %p"
                )

            }


            st.session_state.property_enquiries.append(
                new_enquiry
            )


            st.success(
                f"✅ Enquiry sent to the original property poster: {poster_name}"
            )


    # ========================================================
    # POSTER ENQUIRY DASHBOARD
    # ========================================================

    st.markdown(
        """
<div class="section">

<h2>
📥 Property Poster Enquiry Dashboard
</h2>

</div>
""",
        unsafe_allow_html=True
    )


    poster_enquiries = [

        enquiry

        for enquiry
        in st.session_state.property_enquiries

        if enquiry["Property ID"]
        ==
        property_id

        and enquiry["Poster ID"]
        ==
        poster_id

    ]


    if poster_enquiries:

        for index, enquiry in enumerate(
            poster_enquiries
        ):

            st.markdown(
                f"""
<div class="enquiry-card">

<h3>
📨 {enquiry["Enquiry Type"]}
</h3>

<p>
<strong>Property:</strong>
{enquiry["Property"]}
</p>

<p>
<strong>Interested User:</strong>
{enquiry["Interested User"]}
</p>

<p>
<strong>Mobile:</strong>
{enquiry["Interested Mobile"]}
</p>

<p>
<strong>Email:</strong>
{enquiry["Interested Email"]}
</p>

<p>
<strong>Message:</strong>
{enquiry["Message"]}
</p>

<p>
<strong>Received:</strong>
{enquiry["Created"]}
</p>

<p>
<strong>Status:</strong>
{enquiry["Status"]}
</p>

</div>
""",
                unsafe_allow_html=True
            )


            new_status = st.selectbox(

                "Update Enquiry Status",

                [
                    "New",
                    "Contacted",
                    "Follow-up",
                    "Site Visit Scheduled",
                    "Negotiation",
                    "Booking in Progress",
                    "Closed",
                    "Not Interested"
                ],

                key=f"enquiry_status_{property_id}_{index}"

            )


            if st.button(
                "🔄 UPDATE ENQUIRY STATUS",
                key=f"update_enquiry_{property_id}_{index}",
                use_container_width=True
            ):

                for item in st.session_state.property_enquiries:

                    if (
                        item["Property ID"]
                        ==
                        enquiry["Property ID"]

                        and item["Created"]
                        ==
                        enquiry["Created"]
                    ):

                        item["Status"] = new_status


                st.success(
                    "✅ Enquiry status updated."
                )


    else:

        st.info(
            "📭 No enquiries received for this property yet."
        )


    # ========================================================
    # MESSAGE CENTRE
    # ========================================================

    st.markdown(
        """
<div class="section">

<h2>
💬 Property Message Centre
</h2>

</div>
""",
        unsafe_allow_html=True
    )


    message_type = st.selectbox(
        "📌 Message Type",
        [
            "General Enquiry",
            "Property Information",
            "Site Visit",
            "Price Discussion",
            "Document Request",
            "Loan Discussion",
            "Legal Query",
            "Booking Query"
        ],
        key="workspace_message_type"
    )


    message_text = st.text_area(
        "💬 Write Message",
        placeholder="Type your property-related message...",
        key="workspace_message_text"
    )


    current_user = st.text_input(
        "👤 Your Name",
        value=interested_user,
        key="workspace_current_user"
    )


    user_role = st.selectbox(
        "👥 Your Role",
        [
            "Buyer",
            "Seller",
            "Builder",
            "Agent",
            "Executive",
            "Legal Consultant",
            "Loan Consultant"
        ],
        key="workspace_user_role"
    )


    if st.button(
        "📨 SEND PROPERTY MESSAGE",
        use_container_width=True,
        key="send_property_message"
    ):

        if not message_text:

            st.warning(
                "⚠️ Please enter a message."
            )

        else:

            st.session_state.property_messages.append({

                "Property ID":
                property_id,

                "Property":
                property_name,

                "Poster ID":
                poster_id,

                "Time":
                datetime.now().strftime(
                    "%d-%m-%Y %I:%M %p"
                ),

                "From":
                current_user,

                "Role":
                user_role,

                "Message Type":
                message_type,

                "Message":
                message_text

            })

            st.success(
                "✅ Message added to Property Communication Centre."
            )


    # ========================================================
    # MESSAGE HISTORY
    # ========================================================

    property_messages = [

        message

        for message
        in st.session_state.property_messages

        if message["Property ID"]
        ==
        property_id

    ]


    if property_messages:

        st.markdown(
            """
<div class="section">

<h2>
🕒 Property Communication History
</h2>

</div>
""",
            unsafe_allow_html=True
        )


        st.dataframe(
            property_messages,
            use_container_width=True,
            hide_index=True
        )


    # ========================================================
    # TASK MANAGEMENT
    # ========================================================

    st.markdown(
        """
<div class="section">

<h2>
✅ Property Transaction Task Board
</h2>

</div>
""",
        unsafe_allow_html=True
    )


    t1, t2 = st.columns(2)


    with t1:

        task_title = st.text_input(
            "📌 Task Name",
            placeholder="Example: Collect Sale Agreement",
            key="workspace_task_title"
        )


    with t2:

        task_owner = st.text_input(
            "👤 Assigned To",
            key="workspace_task_owner"
        )


    t3, t4 = st.columns(2)


    with t3:

        task_priority = st.selectbox(
            "🚦 Priority",
            [
                "Low",
                "Medium",
                "High",
                "Urgent"
            ],
            key="workspace_task_priority"
        )


    with t4:

        task_status = st.selectbox(
            "📊 Task Status",
            [
                "Pending",
                "In Progress",
                "Completed"
            ],
            key="workspace_task_status"
        )


    if st.button(
        "➕ ADD PROPERTY TASK",
        use_container_width=True,
        key="add_property_task"
    ):

        if not task_title:

            st.warning(
                "⚠️ Please enter a task name."
            )

        else:

            st.session_state.property_tasks.append({

                "Property ID":
                property_id,

                "Property":
                property_name,

                "Task":
                task_title,

                "Assigned To":
                task_owner,

                "Priority":
                task_priority,

                "Status":
                task_status,

                "Created":
                datetime.now().strftime(
                    "%d-%m-%Y %I:%M %p"
                )

            })

            st.success(
                "✅ Task added successfully."
            )


    # ========================================================
    # TASK LIST
    # ========================================================

    property_tasks = [

        task

        for task
        in st.session_state.property_tasks

        if task["Property ID"]
        ==
        property_id

    ]


    if property_tasks:

        st.dataframe(
            property_tasks,
            use_container_width=True,
            hide_index=True
        )


    # ========================================================
    # FOLLOW-UP
    # ========================================================

    st.markdown(
        """
<div class="section">

<h2>
📅 Follow-Up Reminder
</h2>

</div>
""",
        unsafe_allow_html=True
    )


    r1, r2 = st.columns(2)


    with r1:

        reminder_title = st.text_input(
            "🔔 Reminder Title",
            key="workspace_reminder_title"
        )


    with r2:

        reminder_date = st.date_input(
            "📅 Follow-Up Date",
            value=date.today(),
            key="workspace_reminder_date"
        )


    reminder_notes = st.text_area(
        "📝 Reminder Notes",
        key="workspace_reminder_notes"
    )


    if st.button(
        "🔔 CREATE FOLLOW-UP REMINDER",
        use_container_width=True,
        key="create_followup"
    ):

        st.session_state.property_followups.append({

            "Property ID":
            property_id,

            "Property":
            property_name,

            "Title":
            reminder_title,

            "Date":
            str(reminder_date),

            "Notes":
            reminder_notes,

            "Created":
            datetime.now().strftime(
                "%d-%m-%Y %I:%M %p"
            )

        })

        st.success(
            f"✅ Follow-up reminder created for {reminder_date}."
        )


    # ========================================================
    # COLLABORATION MEMBERS
    # ========================================================

    st.markdown(
        """
<div class="section">

<h2>
👥 Collaboration Members
</h2>

</div>
""",
        unsafe_allow_html=True
    )


    members = st.multiselect(
        "Select people involved in this property transaction",
        [
            "Buyer",
            "Seller",
            "Builder",
            "Agent",
            "Sales Executive",
            "Legal Consultant",
            "Loan Consultant",
            "Property Manager",
            "Admin"
        ],
        key="workspace_members"
    )


    if members:

        st.markdown(
            f"""
<div class="info-card">

<h2>
👥 Active Collaboration Team
</h2>

<p>
{", ".join(members)}
</p>

</div>
""",
            unsafe_allow_html=True
        )


    # ========================================================
    # ACTIVITY SUMMARY
    # ========================================================

    st.markdown(
        """
<div class="section">

<h2>
📊 Collaboration & Enquiry Activity
</h2>

</div>
""",
        unsafe_allow_html=True
    )


    property_likes = [

        x

        for x
        in st.session_state.property_likes

        if x["Property ID"]
        ==
        property_id

    ]


    property_saved = [

        x

        for x
        in st.session_state.property_saved

        if x["Property ID"]
        ==
        property_id

    ]


    property_interests = [

        x

        for x
        in st.session_state.property_interests

        if x["Property ID"]
        ==
        property_id

    ]


    m1, m2, m3, m4, m5, m6 = st.columns(6)


    with m1:

        st.metric(
            "❤️ Likes",
            len(property_likes)
        )


    with m2:

        st.metric(
            "⭐ Saved",
            len(property_saved)
        )


    with m3:

        st.metric(
            "👋 Interests",
            len(property_interests)
        )


    with m4:

        st.metric(
            "📨 Enquiries",
            len(poster_enquiries)
        )


    with m5:

        st.metric(
            "💬 Messages",
            len(property_messages)
        )


    with m6:

        completed_tasks = len(

            [

                x

                for x
                in property_tasks

                if x["Status"]
                ==
                "Completed"

            ]

        )

        st.metric(
            "🎯 Completed Tasks",
            completed_tasks
        )


# ============================================================
# CURRENT PROPERTY LISTINGS
# ============================================================

st.markdown(
    """
<div class="section">

<h2>
🏡 Property Listings
</h2>

</div>
""",
    unsafe_allow_html=True
)


if st.session_state.properties:

    for property_item in st.session_state.properties:

        st.markdown(
            f"""
<div class="info-card">

<h3>
🏠 {property_item['property_title']}
</h3>

<p>
🆔 <b>Property ID:</b>
{property_item['property_id']}
</p>

<p>
👤 <b>Posted By:</b>
{property_item['poster_name']}
</p>

<p>
📍 {property_item['city']},
{property_item['locality']}
</p>

<p>
💰 ₹{property_item['price']:,.0f}
</p>

<p>
📊 <b>Status:</b>
{property_item['listing_status']}
</p>

</div>
""",
            unsafe_allow_html=True
        )


else:

    st.info(
        "📭 No property listings available yet."
    )


# ============================================================
# FINAL WORKFLOW
# ============================================================

st.markdown(
    """
<div class="ai-card">

<h2>
🚀 Smart Property Collaboration Workflow
</h2>

<p>
🏡 Property Posted
&nbsp; → &nbsp;
🆔 Unique Property ID
</p>

<p>
❤️ Like
&nbsp; → &nbsp;
⭐ Save
&nbsp; → &nbsp;
👋 Interest
&nbsp; → &nbsp;
📨 Enquiry
</p>

<p>
📨 Enquiry → Original Property Poster
</p>

<p>
💬 Message
&nbsp; → &nbsp;
📅 Follow-up
&nbsp; → &nbsp;
🏠 Site Visit
&nbsp; → &nbsp;
🤝 Negotiation
&nbsp; → &nbsp;
📝 Booking
</p>

<p>
All activity remains connected to the same Property ID.
</p>

</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# FINAL NOTICE
# ============================================================

st.markdown(
    """
<div class="trust-card">

<h2>
🏠 One Property — One Property ID — One Original Poster
</h2>

<p>
The original person who posts the property remains connected
to that property record.
</p>

<p>
All Likes, Saves, Interests, Enquiries, Messages,
Tasks and Follow-ups remain linked to the same Property ID.
</p>

<p>
Production version में यही Property ID database,
logged-in user account, notifications, WhatsApp,
email and CRM workflow से connect किया जा सकता है।
</p>

</div>
""",
    unsafe_allow_html=True
)
