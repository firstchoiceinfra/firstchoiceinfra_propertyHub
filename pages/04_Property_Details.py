import streamlit as st
import math

# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 04 — PROPERTY DETAILS
# ============================================================

st.set_page_config(
    page_title="Property Details | FirstChoice Infra Property Hub",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# PREMIUM MULTINATIONAL UI
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

/* Hide Streamlit default menu */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background:
    linear-gradient(
        180deg,
        #071952,
        #1E1B4B,
        #4C1D95
    );
}

[data-testid="stSidebar"] * {
    color: white !important;
}

/* Main Hero */
.hero {
    padding: 45px;
    border-radius: 35px;
    color: white;
    margin-bottom: 30px;

    background:
    linear-gradient(
        135deg,
        #020617,
        #1D4ED8,
        #7C3AED,
        #DB2777
    );

    box-shadow:
    0 25px 70px
    rgba(37,99,235,0.30);
}

.hero h1 {
    font-size: 45px;
    font-weight: 900;
}

.hero p {
    font-size: 18px;
}

/* Section */
.section {
    padding: 28px 32px;
    border-radius: 28px;
    color: white;
    margin-top: 30px;
    margin-bottom: 25px;

    background:
    linear-gradient(
        135deg,
        #071952,
        #2563EB,
        #7C3AED,
        #EC4899
    );

    box-shadow:
    0 15px 40px
    rgba(37,99,235,0.20);
}

/* Cards */
.card {
    padding: 28px;
    border-radius: 28px;
    background:
    linear-gradient(
        135deg,
        #FFFFFF,
        #F5F3FF,
        #EFF6FF
    );

    border: 1px solid #E0E7FF;

    box-shadow:
    0 15px 40px
    rgba(0,0,0,0.07);

    margin-bottom: 20px;
}

/* Property Image */
.property-image {
    width: 100%;
    height: 430px;
    border-radius: 30px;
    object-fit: cover;

    box-shadow:
    0 20px 50px
    rgba(0,0,0,0.20);
}

/* Price */
.price-box {
    padding: 30px;
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
    0 20px 50px
    rgba(5,150,105,0.25);
}

/* EMI */
.emi-box {
    padding: 30px;
    border-radius: 30px;

    background:
    linear-gradient(
        135deg,
        #EEF2FF,
        #F5F3FF,
        #FAE8FF
    );

    border: 1px solid #DDD6FE;

    box-shadow:
    0 15px 40px
    rgba(99,102,241,0.12);
}

/* Contact */
.contact-box {
    padding: 30px;
    border-radius: 30px;
    color: white;

    background:
    linear-gradient(
        135deg,
        #0F172A,
        #1E3A8A,
        #312E81
    );
}

/* Back */
.back-box {
    padding: 25px;
    border-radius: 25px;
    background: white;
    text-align: center;
    box-shadow:
    0 10px 35px
    rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

with st.sidebar:

    st.markdown("""
    <div style="text-align:center; padding:20px;">

    <h1>🏠 FirstChoice</h1>

    <h3>Property Hub</h3>

    <hr>

    <p>
    India's Next-Generation<br>
    Real Estate Marketplace
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📌 Property Platform")

    if st.button(
        "🏠 Home",
        use_container_width=True
    ):
        st.switch_page("app.py")

    if st.button(
        "🔐 Login & Registration",
        use_container_width=True
    ):
        st.switch_page(
            "pages/01_Login_Register.py"
        )

    if st.button(
        "🔎 Property Search",
        use_container_width=True
    ):
        st.switch_page(
            "pages/02_Property_Search.py"
        )

    if st.button(
        "🏡 Post Property",
        use_container_width=True
    ):
        st.switch_page(
            "pages/03_Post_Property.py"
        )

    st.markdown("---")

    st.markdown("""
    ### 🌟 Platform Features

    🏠 Buy Property

    🔑 Rent Property

    🏢 Commercial

    🌳 Land & Plot

    🏗️ New Projects

    📍 Smart Location

    🎥 Property Video

    🗺️ Google Location

    💰 EMI Calculator

    🤝 Local Services
    """)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<h1>
🏡 Premium Property Details
</h1>

<p>
Explore complete property information, location,
media, pricing, financing and nearby real-estate services.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROPERTY ID
# ============================================================

st.markdown("""
<div class="section">

<h2>
🔎 Select / Enter Property
</h2>

<p>
Enter a Property ID to view complete property information.
</p>

</div>
""", unsafe_allow_html=True)


property_id = st.text_input(
    "🏷️ Property ID",
    placeholder="Example: FCI-NGP-10001"
)


# ============================================================
# DEMO PROPERTY
# ============================================================

if not property_id:

    property_id = "FCI-NGP-10001"


# ============================================================
# PROPERTY MEDIA
# ============================================================

st.markdown("""
<div class="section">

<h2>
📸 Property Gallery & Video
</h2>

</div>
""", unsafe_allow_html=True)


image_url = st.text_input(
    "🖼️ Property Image URL",
    value="https://images.unsplash.com/photo-1600585154340-be6161a56a0c"
)


st.image(
    image_url,
    use_container_width=True,
    caption="Premium Property Preview"
)


video_url = st.text_input(
    "🎥 Property / Surrounding Video URL",
    placeholder="Paste video URL here"
)


if video_url:

    st.video(video_url)

else:

    st.info(
        "🎥 Property owner / agent can add a property or surrounding-area video."
    )


# ============================================================
# PROPERTY BASIC INFORMATION
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏠 Property Information
</h2>

</div>
""", unsafe_allow_html=True)


c1, c2, c3 = st.columns(3)


with c1:

    st.metric(
        "🏷️ Property ID",
        property_id
    )


with c2:

    st.metric(
        "🏠 Property Type",
        "Residential Plot"
    )


with c3:

    st.metric(
        "📌 Listing Status",
        "Available"
    )


c4, c5, c6 = st.columns(3)


with c4:

    st.metric(
        "📐 Area",
        "1,500 Sq.Ft."
    )


with c5:

    st.metric(
        "🛏️ Bedrooms",
        "N/A"
    )


with c6:

    st.metric(
        "🚗 Parking",
        "Available"
    )


# ============================================================
# LOCATION
# ============================================================

st.markdown("""
<div class="section">

<h2>
📍 Complete Property Location
</h2>

<p>
Country → State → City → Village / Town → Area
</p>

</div>
""", unsafe_allow_html=True)


loc1, loc2 = st.columns(2)


with loc1:

    st.write("🌍 **Country:** India")

    st.write("🗺️ **State:** Maharashtra")

    st.write("🏙️ **City:** Nagpur")


with loc2:

    st.write("🏘️ **Village / Town:** Nagpur")

    st.write("📍 **Area:** Other — Example Local Area")

    st.write("📮 **PIN Code:** 440001")


# ============================================================
# GOOGLE MAP
# ============================================================

st.markdown("""
<div class="section">

<h2>
🗺️ Google Location
</h2>

</div>
""", unsafe_allow_html=True)


map_link = st.text_input(
    "📍 Google Maps Link",
    placeholder="Paste Google Maps location link"
)


if map_link:

    st.markdown(
        f"""
        <a href="{map_link}"
        target="_blank">

        <button style="
        padding:15px 30px;
        border:none;
        border-radius:15px;
        background:#2563EB;
        color:white;
        font-size:17px;
        font-weight:bold;
        ">

        📍 OPEN PROPERTY LOCATION

        </button>

        </a>
        """,
        unsafe_allow_html=True
    )

else:

    st.info(
        "📍 Google Maps location will appear here when available."
    )


# ============================================================
# PRICE
# ============================================================

st.markdown("""
<div class="section">

<h2>
💰 Property Pricing
</h2>

</div>
""", unsafe_allow_html=True)


price = st.number_input(
    "💰 Property Price (₹)",
    min_value=0,
    value=5000000,
    step=100000
)


st.markdown(
    f"""
    <div class="price-box">

    <h2>
    💰 Property Price
    </h2>

    <h1>
    ₹{price:,.0f}
    </h1>

    <p>
    Final price may vary according to negotiation,
    taxes, registration and other applicable charges.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# EMI CALCULATOR
# UP TO 30 YEARS
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏦 Smart Home Loan EMI Calculator
</h2>

<p>
Calculate estimated monthly EMI for loan periods
from 1 year up to 30 years.
</p>

</div>
""", unsafe_allow_html=True)


emi1, emi2, emi3 = st.columns(3)


with emi1:

    loan_amount = st.number_input(
        "🏦 Loan Amount (₹)",
        min_value=0,
        value=4000000,
        step=100000
    )


with emi2:

    annual_interest = st.number_input(
        "📈 Annual Interest Rate (%)",
        min_value=0.0,
        max_value=30.0,
        value=8.5,
        step=0.1
    )


with emi3:

    loan_years = st.slider(
        "📅 Loan Tenure",
        min_value=1,
        max_value=30,
        value=20
    )


# EMI calculation

monthly_rate = annual_interest / 12 / 100

number_of_months = loan_years * 12


if monthly_rate > 0:

    emi = (
        loan_amount
        * monthly_rate
        * (1 + monthly_rate) ** number_of_months
    ) / (
        (1 + monthly_rate) ** number_of_months - 1
    )

else:

    emi = loan_amount / number_of_months


total_payment = emi * number_of_months

total_interest = total_payment - loan_amount


st.markdown("""
<div class="emi-box">

<h2>
📊 Estimated Loan Summary
</h2>

</div>
""", unsafe_allow_html=True)


e1, e2, e3 = st.columns(3)


with e1:

    st.metric(
        "💳 Monthly EMI",
        f"₹{emi:,.0f}"
    )


with e2:

    st.metric(
        "💰 Total Interest",
        f"₹{total_interest:,.0f}"
    )


with e3:

    st.metric(
        "🏦 Total Payment",
        f"₹{total_payment:,.0f}"
    )


st.caption(
    "⚠️ EMI is an estimated calculation. Actual loan terms depend on the lender, interest rate, eligibility and applicable charges."
)


# ============================================================
# PROPERTY DESCRIPTION
# ============================================================

st.markdown("""
<div class="section">

<h2>
📝 Property Description
</h2>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="card">

<h3>
🌟 Premium Residential Plot Opportunity
</h3>

<p>
This property is located in a developing area with
potential access to residential and commercial infrastructure.
</p>

<p>
The surrounding location, connectivity and nearby facilities
make this property suitable for residential development
and long-term investment.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# AMENITIES
# ============================================================

st.markdown("""
<div class="section">

<h2>
✨ Nearby Facilities & Amenities
</h2>

</div>
""", unsafe_allow_html=True)


a1, a2, a3, a4 = st.columns(4)


with a1:

    st.markdown("""
    <div class="card">
    🏫 School<br><br>
    Nearby educational facilities
    </div>
    """, unsafe_allow_html=True)


with a2:

    st.markdown("""
    <div class="card">
    🏥 Hospital<br><br>
    Healthcare facilities nearby
    </div>
    """, unsafe_allow_html=True)


with a3:

    st.markdown("""
    <div class="card">
    🛒 Market<br><br>
    Shopping and daily needs
    </div>
    """, unsafe_allow_html=True)


with a4:

    st.markdown("""
    <div class="card">
    🚗 Connectivity<br><br>
    Road and transport access
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# LOCAL PROPERTY SERVICES
# ============================================================

st.markdown("""
<div class="section">

<h2>
🤝 Nearby Property & Construction Services
</h2>

<p>
Find professionals and service providers required
for property development and construction.
</p>

</div>
""", unsafe_allow_html=True)


service_type = st.selectbox(

    "🔎 Select Service",

    [
        "🏛️ Architect",
        "🏗️ Builder",
        "🧱 Building Material Supplier",
        "🎨 Paint Shop",
        "🔨 Carpenter",
        "🚰 Plumber",
        "⚡ Electrician",
        "🏭 Fabrication",
        "🪟 Aluminium & Glass",
        "🛋️ Interior Designer",
        "🌳 Landscaping",
        "🔧 Other Services"
    ]

)


s1, s2 = st.columns(2)


with s1:

    st.markdown("""
    <div class="card">

    <h2>
    🏢 Verified Service Provider
    </h2>

    <h3>
    FirstChoice Professional Services
    </h3>

    <p>
    📍 Nagpur, Maharashtra
    </p>

    <p>
    ⭐ Verified Business Profile
    </p>

    </div>
    """, unsafe_allow_html=True)


with s2:

    st.markdown("""
    <div class="contact-box">

    <h2>
    📞 Contact Service Provider
    </h2>

    <p>
    Connect with local professionals
    for your property and construction needs.
    </p>

    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "📞 VIEW CONTACT",
        use_container_width=True
    ):

        st.success(
            "Contact details will be available after the service provider profile is verified."
        )


# ============================================================
# PROPERTY OWNER / AGENT
# ============================================================

st.markdown("""
<div class="section">

<h2>
👤 Property Contact
</h2>

</div>
""", unsafe_allow_html=True)


owner1, owner2 = st.columns(2)


with owner1:

    st.markdown("""
    <div class="card">

    <h2>
    👤 Verified Property Owner
    </h2>

    <p>
    ⭐ FirstChoice Verified Profile
    </p>

    <p>
    📍 Nagpur, Maharashtra
    </p>

    </div>
    """, unsafe_allow_html=True)


with owner2:

    if st.button(
        "📞 CONTACT OWNER",
        use_container_width=True
    ):

        st.info(
            "Login required to view owner contact details."
        )

    if st.button(
        "📩 SEND ENQUIRY",
        use_container_width=True
    ):

        st.success(
            "Your enquiry has been submitted."
        )


# ============================================================
# SAVE / SHARE / REPORT
# ============================================================

st.markdown("""
<div class="section">

<h2>
❤️ Property Actions
</h2>

</div>
""", unsafe_allow_html=True)


b1, b2, b3 = st.columns(3)


with b1:

    if st.button(
        "❤️ SAVE PROPERTY",
        use_container_width=True
    ):

        st.success(
            "Property saved to your favourites."
        )


with b2:

    if st.button(
        "📤 SHARE PROPERTY",
        use_container_width=True
    ):

        st.info(
            "Property sharing option activated."
        )


with b3:

    if st.button(
        "🚨 REPORT LISTING",
        use_container_width=True
    ):

        st.warning(
            "Report request submitted for review."
        )


# ============================================================
# BACK TO SEARCH
# ============================================================

st.markdown("""
<div class="back-box">

<h2>
⬅️ Continue Exploring Properties
</h2>

<p>
Return to Property Search and explore more listings.
</p>

</div>
""", unsafe_allow_html=True)


if st.button(
    "⬅️ BACK TO PROPERTY SEARCH",
    use_container_width=True
):

    st.switch_page(
        "pages/02_Property_Search.py"
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<br>

<div style="
padding:35px;
border-radius:30px;
background:linear-gradient(
135deg,
#071952,
#1E1B4B,
#4C1D95
);
color:white;
text-align:center;
">

<h2>
🏠 FIRSTCHOICE INFRA PROPERTY HUB
</h2>

<p>
Buy • Sell • Rent • Invest • Build • Discover
</p>

<p>
© FirstChoice Infra Property Hub
</p>

</div>
""", unsafe_allow_html=True)
