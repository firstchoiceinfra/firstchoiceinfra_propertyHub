import streamlit as st

# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 10 - PREMIUM PROPERTY DETAILS
# ============================================================

st.set_page_config(
    page_title="Property Details | FirstChoice Property Hub",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# PREMIUM CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background:
    linear-gradient(
        135deg,
        #F7F9FF 0%,
        #FFF7F3 35%,
        #F7F1FF 70%,
        #EFFCFF 100%
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

/* ============================================================
BRAND
============================================================ */

.brand {

    background:
    linear-gradient(
        135deg,
        #071952,
        #2563EB,
        #7C3AED,
        #EC4899
    );

    padding: 20px 32px;

    border-radius: 24px;

    color: white;

    box-shadow:
    0 18px 50px
    rgba(37,99,235,0.22);
}

.brand-title {

    font-size: 28px;

    font-weight: 900;

    letter-spacing: 2px;
}

.brand-subtitle {

    font-size: 11px;

    letter-spacing: 4px;

    color: #FDE68A;
}

/* ============================================================
HERO
============================================================ */

.hero {

    margin-top: 28px;

    padding: 38px 42px;

    border-radius: 30px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #071952,
        #2563EB,
        #7C3AED,
        #EC4899
    );

    box-shadow:
    0 22px 60px
    rgba(37,99,235,0.25);

    position: relative;

    overflow: hidden;
}

.hero-title {

    font-size: 40px;

    font-weight: 900;

    position: relative;

    z-index: 2;
}

.hero-subtitle {

    font-size: 16px;

    color:
    rgba(255,255,255,0.86);

    position: relative;

    z-index: 2;
}

/* ============================================================
SECTION HEADER
============================================================ */

.section-header {

    margin-top: 35px;

    margin-bottom: 22px;

    padding: 22px 30px;

    border-radius: 22px;

    background:
    linear-gradient(
        135deg,
        #071952,
        #2563EB,
        #7C3AED,
        #EC4899
    );

    color: white;

    box-shadow:
    0 12px 35px
    rgba(37,99,235,0.18);

    position: relative;

    overflow: hidden;
}

.section-title {

    font-size: 27px;

    font-weight: 900;

    position: relative;

    z-index: 2;
}

.section-subtitle {

    font-size: 13px;

    color:
    rgba(255,255,255,0.82);

    position: relative;

    z-index: 2;
}

/* ============================================================
PROPERTY IMAGE
============================================================ */

.main-image {

    width: 100%;

    height: 500px;

    object-fit: cover;

    border-radius: 30px;

    box-shadow:
    0 20px 50px
    rgba(0,0,0,0.15);
}

/* ============================================================
PRICE CARD
============================================================ */

.price-card {

    background: white;

    padding: 32px;

    border-radius: 28px;

    box-shadow:
    0 15px 40px
    rgba(0,0,0,0.08);
}

/* ============================================================
FEATURE CARD
============================================================ */

.feature-card {

    background: white;

    padding: 25px;

    border-radius: 22px;

    text-align: center;

    min-height: 140px;

    box-shadow:
    0 10px 30px
    rgba(0,0,0,0.06);
}

/* ============================================================
BADGES
============================================================ */

.badge {

    display: inline-block;

    padding: 8px 15px;

    border-radius: 30px;

    font-size: 11px;

    font-weight: 800;

    color: white;

    margin-right: 5px;
}

.verified {

    background:
    linear-gradient(
        135deg,
        #059669,
        #22C55E
    );
}

.premium {

    background:
    linear-gradient(
        135deg,
        #7C3AED,
        #EC4899
    );
}

.featured {

    background:
    linear-gradient(
        135deg,
        #F97316,
        #EF4444
    );
}

/* ============================================================
OWNER CARD
============================================================ */

.owner-card {

    background: white;

    padding: 30px;

    border-radius: 28px;

    box-shadow:
    0 15px 40px
    rgba(0,0,0,0.08);
}

/* ============================================================
VIDEO
============================================================ */

.video-card {

    background:
    linear-gradient(
        135deg,
        #071952,
        #1E1B4B
    );

    padding: 35px;

    border-radius: 28px;

    color: white;

    text-align: center;
}

/* ============================================================
MAP
============================================================ */

.map-card {

    height: 300px;

    border-radius: 28px;

    background:
    linear-gradient(
        135deg,
        #DBEAFE,
        #EDE9FE,
        #FCE7F3
    );

    display: flex;

    align-items: center;

    justify-content: center;

    text-align: center;

    box-shadow:
    0 12px 35px
    rgba(0,0,0,0.07);
}

/* ============================================================
PREMIUM CTA
============================================================ */

.premium-card {

    padding: 42px;

    border-radius: 30px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #071952,
        #4C1D95,
        #7C3AED,
        #EC4899
    );

    box-shadow:
    0 22px 60px
    rgba(124,58,237,0.25);
}

/* ============================================================
FOOTER
============================================================ */

.footer {

    margin-top: 60px;

    padding: 45px;

    border-radius: 28px;

    color: white;

    text-align: center;

    background:
    linear-gradient(
        135deg,
        #071952,
        #1E1B4B
    );
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# BRAND
# ============================================================

st.markdown("""
<div class="brand">

<div class="brand-title">
🏠 FIRSTCHOICE INFRA
</div>

<div class="brand-subtitle">
PROPERTY HUB • INDIA'S SMART REAL ESTATE MARKETPLACE
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROPERTY HERO
# ============================================================

st.markdown("""
<div class="hero">

<div class="hero-title">
🏡 Premium 3 BHK Luxury Apartment
</div>

<div class="hero-subtitle">
📍 Civil Lines, Nagpur, Maharashtra
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# MAIN IMAGE
# ============================================================

st.markdown("""
<img
class="main-image"
src="https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=1600&q=90"
>
""", unsafe_allow_html=True)


# ============================================================
# PROPERTY BADGES
# ============================================================

st.write("")

b1,b2,b3 = st.columns(3)

with b1:

    st.markdown(
        '<span class="badge verified">🛡️ VERIFIED PROPERTY</span>',
        unsafe_allow_html=True
    )

with b2:

    st.markdown(
        '<span class="badge premium">⭐ PREMIUM LISTING</span>',
        unsafe_allow_html=True
    )

with b3:

    st.markdown(
        '<span class="badge featured">🔥 FEATURED PROPERTY</span>',
        unsafe_allow_html=True
    )


# ============================================================
# PRICE + QUICK ACTION
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
💰 Property Overview
</div>

<div class="section-subtitle">
Important information about this property.
</div>

</div>
""", unsafe_allow_html=True)


p1,p2 = st.columns([2,1])


with p1:

    st.markdown("""
    <div class="price-card">

    <h1 style="color:#7C3AED;">
    ₹1.25 Crore
    </h1>

    <p>
    💰 Estimated EMI starting from ₹85,000/month
    </p>

    <hr>

    <h3>
    📍 Civil Lines, Nagpur
    </h3>

    <p>
    Maharashtra, India
    </p>

    <p>
    🛡️ Owner Identity Verification Available
    </p>

    <p>
    📱 Mobile Number Verified
    </p>

    </div>
    """, unsafe_allow_html=True)


with p2:

    if st.button(
        "❤️ Save Property",
        use_container_width=True
    ):

        st.success(
            "Property saved."
        )

    if st.button(
        "⚖️ Add to Compare",
        use_container_width=True
    ):

        st.info(
            "Added to comparison list."
        )

    if st.button(
        "📤 Share Property",
        use_container_width=True
    ):

        st.success(
            "Share link generated."
        )


# ============================================================
# PROPERTY FEATURES
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🏠 Property Highlights
</div>

<div class="section-subtitle">
Key features and specifications.
</div>

</div>
""", unsafe_allow_html=True)


features = [

    ("🛏️","Bedrooms","3 BHK"),

    ("🚿","Bathrooms","3"),

    ("📐","Built-up Area","1,850 Sq.Ft"),

    ("🏢","Property Type","Apartment"),

    ("🚗","Parking","2 Cars"),

    ("🏗️","Property Age","New Construction")

]


feature_cols = st.columns(3)


for index, feature in enumerate(features):

    with feature_cols[index % 3]:

        st.markdown(
            f"""
            <div class="feature-card">

            <div style="font-size:38px;">
            {feature[0]}
            </div>

            <h3>
            {feature[1]}
            </h3>

            <p>
            {feature[2]}
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    if index % 3 == 2:

        st.write("")


# ============================================================
# PROPERTY DESCRIPTION
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📝 About This Property
</div>

<div class="section-subtitle">
Detailed property description.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="price-card">

<h2>
Experience Premium Urban Living
</h2>

<p>
This premium 3 BHK residence is designed for modern
families seeking comfort, luxury and convenience in
one of Nagpur's highly desirable residential locations.
</p>

<p>
The property features spacious interiors, premium
finishing, modern architecture and excellent connectivity
to major business, education and lifestyle destinations.
</p>

<p>
FirstChoice Property Hub will provide verified property
information and owner verification features to help
buyers make informed real estate decisions.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# AMENITIES
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
✨ Premium Amenities
</div>

<div class="section-subtitle">
Lifestyle features available with this property.
</div>

</div>
""", unsafe_allow_html=True)


amenities = [

    "🏊 Swimming Pool",

    "🏋️ Fitness Centre",

    "🌳 Landscaped Garden",

    "🔒 24/7 Security",

    "⚡ Power Backup",

    "🛗 High Speed Elevators",

    "🚗 Covered Parking",

    "🎥 CCTV Surveillance",

    "🎮 Children's Play Area",

    "🏢 Club House",

    "🔥 Fire Safety",

    "📶 High Speed Internet"

]


amenity_cols = st.columns(4)


for index, amenity in enumerate(amenities):

    with amenity_cols[index % 4]:

        st.success(
            amenity
        )


# ============================================================
# PROPERTY VIDEO
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🎥 Property Video Tour
</div>

<div class="section-subtitle">
Experience the property before scheduling your visit.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="video-card">

<h2>
🎬 Virtual Property Tour
</h2>

<p>
A professional property video can be displayed here.
</p>

</div>
""", unsafe_allow_html=True)


video_url = st.text_input(

    "Property Video URL",

    placeholder="Paste YouTube or video URL here"

)


if video_url:

    try:

        st.video(
            video_url
        )

    except:

        st.warning(
            "Please enter a valid video URL."
        )


# ============================================================
# LOCATION
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📍 Property Location
</div>

<div class="section-subtitle">
Explore the neighbourhood and nearby locations.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="map-card">

<div>

<h2>
📍 Civil Lines, Nagpur
</h2>

<p>
Interactive Google Maps integration
will be connected in the production version.
</p>

</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# OWNER / AGENT
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
👤 Owner / Agent Information
</div>

<div class="section-subtitle">
Connect with the property owner or authorised representative.
</div>

</div>
""", unsafe_allow_html=True)


o1,o2 = st.columns([1,2])


with o1:

    st.markdown("""
    <div class="owner-card">

    <h1>
    👤
    </h1>

    <h2>
    Verified Property Owner
    </h2>

    <p>
    🛡️ Identity Verification: Pending
    </p>

    <p>
    📱 Mobile: Verified
    </p>

    </div>
    """, unsafe_allow_html=True)


with o2:

    st.markdown("""
    <div class="owner-card">

    <h3>
    🛡️ Trust & Verification
    </h3>

    <p>
    FirstChoice Property Hub is designed to support
    secure identity and mobile verification for
    property owners and agents.
    </p>

    <p>
    In the production backend, KYC verification,
    property documents and ownership verification
    will be handled through secure verification services.
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# CONTACT
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
💬 Contact Property Owner
</div>

<div class="section-subtitle">
Send an enquiry or request more information.
</div>

</div>
""", unsafe_allow_html=True)


c1,c2 = st.columns(2)


with c1:

    name = st.text_input(
        "Your Name"
    )

    mobile = st.text_input(
        "Your Mobile Number"
    )


with c2:

    email = st.text_input(
        "Your Email"
    )

    enquiry_type = st.selectbox(
        "Enquiry Type",
        [
            "General Enquiry",
            "Request Price",
            "Request Site Visit",
            "Request Call Back",
            "Request More Photos",
            "Request Property Documents"
        ]
    )


message = st.text_area(

    "Message",

    placeholder="Write your enquiry..."

)


if st.button(

    "📤 SEND ENQUIRY",

    use_container_width=True

):

    if name and mobile:

        st.success(

            "Your enquiry has been submitted successfully."

        )

    else:

        st.warning(

            "Please enter your name and mobile number."

        )


# ============================================================
# SITE VISIT
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📅 Schedule a Property Visit
</div>

<div class="section-subtitle">
Choose your preferred date and time.
</div>

</div>
""", unsafe_allow_html=True)


sv1,sv2 = st.columns(2)


with sv1:

    visit_date = st.date_input(
        "Preferred Date"
    )


with sv2:

    visit_time = st.selectbox(

        "Preferred Time",

        [
            "10:00 AM",
            "11:00 AM",
            "12:00 PM",
            "2:00 PM",
            "4:00 PM",
            "5:00 PM"
        ]

    )


if st.button(

    "📅 REQUEST SITE VISIT",

    use_container_width=True

):

    st.success(

        f"""
        Site visit request submitted for
        {visit_date} at {visit_time}.
        """

    )


# ============================================================
# PREMIUM CTA
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
⭐ FirstChoice Property Protection
</div>

<div class="section-subtitle">
Future trust and verification ecosystem.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="premium-card">

<h2>
🛡️ Buy With Confidence
</h2>

<p>
FirstChoice Infra Property Hub is being designed
with a trust-first real estate ecosystem.
</p>

<p>
Future verification layers can include:

</p>

<p>
🪪 Identity Verification
</p>

<p>
📱 Mobile Verification
</p>

<p>
📄 Property Document Verification
</p>

<p>
🏠 Ownership Verification
</p>

<p>
🤝 Verified Agent / Builder Profiles
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

<h2>
🏠 FIRSTCHOICE INFRA PROPERTY HUB
</h2>

<p>
India's Next-Generation Real Estate Marketplace
</p>

<p>
Buy • Sell • Rent • Invest • Discover
</p>

<hr>

<small>
© FirstChoice Infra Property Hub
</small>

</div>
""", unsafe_allow_html=True)
