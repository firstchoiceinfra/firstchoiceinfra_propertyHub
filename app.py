import streamlit as st
import random

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="FirstChoice Infra Property Hub",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =====================================================
# SESSION STATE
# =====================================================

if "show_login" not in st.session_state:
    st.session_state.show_login = False

if "otp_sent" not in st.session_state:
    st.session_state.otp_sent = False

if "demo_otp" not in st.session_state:
    st.session_state.demo_otp = None

if "verified" not in st.session_state:
    st.session_state.verified = False

if "mobile" not in st.session_state:
    st.session_state.mobile = ""

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown(
    """
    <style>

    .main {
        background-color: #f5f7fb;
    }

    .hero {
        background: linear-gradient(135deg, #0b1f3a, #123f73);
        padding: 45px;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
    }

    .hero h1 {
        font-size: 42px;
        margin-bottom: 10px;
    }

    .hero p {
        font-size: 18px;
        opacity: 0.9;
    }

    .section-title {
        font-size: 28px;
        font-weight: bold;
        color: #0b1f3a;
        margin-top: 30px;
        margin-bottom: 20px;
    }

    .category-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.06);
        margin-bottom: 15px;
    }

    .category-icon {
        font-size: 40px;
    }

    .property-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.06);
        margin-bottom: 20px;
    }

    .login-box {
        background: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0px 5px 20px rgba(0,0,0,0.10);
        margin-top: 20px;
        margin-bottom: 30px;
    }

    .footer {
        margin-top: 50px;
        padding: 30px;
        background: #0b1f3a;
        color: white;
        text-align: center;
        border-radius: 15px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =====================================================
# HEADER
# =====================================================

col1, col2 = st.columns([3, 1])

with col1:
    st.markdown(
        """
        <h2 style="color:#0b1f3a;">
        🏠 FirstChoice Infra Property Hub
        </h2>
        """,
        unsafe_allow_html=True
    )

with col2:
    if st.button(
        "🔐 Login / Register",
        use_container_width=True
    ):
        st.session_state.show_login = True
        st.rerun()

# =====================================================
# LOGIN / REGISTER MODULE
# =====================================================

if st.session_state.show_login:

    st.markdown(
        """
        <div class="login-box">

        <h2 style="color:#0b1f3a;">
        🔐 Property Hub Login / Registration
        </h2>

        <p>
        Login or create your FirstChoice Property Hub account
        using your mobile number.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    login_col1, login_col2 = st.columns([2, 1])

    with login_col1:

        mobile = st.text_input(
            "📱 Enter Current Mobile Number",
            placeholder="Enter 10 digit mobile number",
            max_chars=10
        )

    with login_col2:

        st.write("")
        st.write("")

        if st.button(
            "📨 Send OTP",
            use_container_width=True
        ):

            if len(mobile) != 10 or not mobile.isdigit():

                st.error(
                    "Please enter a valid 10 digit mobile number."
                )

            else:

                otp = random.randint(
                    100000,
                    999999
                )

                st.session_state.mobile = mobile
                st.session_state.demo_otp = otp
                st.session_state.otp_sent = True

                st.success(
                    "OTP generated successfully."
                )

                st.info(
                    f"Demo OTP: {otp}"
                )

    # =================================================
    # OTP VERIFICATION
    # =================================================

    if st.session_state.otp_sent:

        st.markdown("---")

        st.subheader("🔑 Verify Mobile Number")

        entered_otp = st.text_input(
            "Enter 6 Digit OTP",
            max_chars=6
        )

        if st.button(
            "✅ Verify OTP",
            use_container_width=True
        ):

            if entered_otp == str(
                st.session_state.demo_otp
            ):

                st.session_state.verified = True

                st.success(
                    "✅ Mobile number verified successfully!"
                )

            else:

                st.error(
                    "❌ Invalid OTP. Please try again."
                )

    # =================================================
    # CREATE FIRSTCHOICE PROFILE
    # =================================================

    if st.session_state.verified:

        st.markdown("---")

        st.subheader(
            "👤 Create Your FirstChoice Profile"
        )

        profile_col1, profile_col2 = st.columns(2)

        with profile_col1:

            full_name = st.text_input(
                "Full Name"
            )

            email = st.text_input(
                "Email Address"
            )

            city = st.text_input(
                "City"
            )

        with profile_col2:

            user_type = st.selectbox(
                "Select Account Type",
                [
                    "Buyer",
                    "Owner / Seller",
                    "Tenant",
                    "Real Estate Agent",
                    "Builder / Developer",
                    "Business Partner"
                ]
            )

            user_id_type = st.selectbox(
                "Identity Verification",
                [
                    "Mobile Verified",
                    "Mobile + KYC Verification (Coming Soon)"
                ]
            )

        if st.button(
            "🚀 Create My FirstChoice ID",
            use_container_width=True
        ):

            if not full_name or not city:

                st.warning(
                    "Please enter your Full Name and City."
                )

            else:

                firstchoice_id = (
                    "FC-"
                    + st.session_state.mobile[-4:]
                    + "-"
                    + str(random.randint(1000, 9999))
                )

                st.success(
                    "🎉 Your FirstChoice Property Hub ID has been created!"
                )

                st.info(
                    f"🆔 FirstChoice ID: {firstchoice_id}"
                )

                st.write(
                    f"👤 Name: **{full_name}**"
                )

                st.write(
                    f"📱 Mobile: **+91 {st.session_state.mobile}**"
                )

                st.write(
                    f"🏷️ Account Type: **{user_type}**"
                )

                st.write(
                    f"📍 City: **{city}**"
                )

                st.success(
                    "✅ Your profile is ready."
                )

    st.markdown("---")

    if st.button(
        "⬅️ Back to Property Hub",
        use_container_width=True
    ):

        st.session_state.show_login = False
        st.rerun()

# =====================================================
# HERO SECTION
# =====================================================

if not st.session_state.show_login:

    st.markdown(
        """
        <div class="hero">

            <h1>Find Your Perfect Property</h1>

            <p>
            Buy • Rent • Sell • New Projects • Plots • Commercial
            </p>

            <p>
            India's Smart Property Marketplace
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    # =================================================
    # SEARCH SECTION
    # =================================================

    st.markdown(
        '<div class="section-title">🔍 Search Properties</div>',
        unsafe_allow_html=True
    )

    search_col1, search_col2, search_col3 = st.columns(3)

    with search_col1:

        purpose = st.selectbox(
            "Looking For",
            [
                "Buy",
                "Rent",
                "New Projects",
                "Plots & Land",
                "Commercial"
            ]
        )

    with search_col2:

        property_type = st.selectbox(
            "Property Type",
            [
                "All Properties",
                "Apartment",
                "Villa",
                "Independent House",
                "Plot",
                "Office",
                "Shop",
                "Warehouse",
                "Agricultural Land"
            ]
        )

    with search_col3:

        location = st.text_input(
            "📍 City / Locality",
            placeholder="Enter city or locality"
        )

    col4, col5, col6 = st.columns(3)

    with col4:

        min_budget = st.number_input(
            "Minimum Budget (₹)",
            min_value=0,
            step=100000
        )

    with col5:

        max_budget = st.number_input(
            "Maximum Budget (₹)",
            min_value=0,
            step=100000
        )

    with col6:

        search_button = st.button(
            "🔍 Search Property",
            use_container_width=True
        )

    if search_button:

        if location:

            st.success(
                f"Searching {purpose} properties in {location}"
            )

        else:

            st.warning(
                "Please enter a city or locality."
            )

    # =================================================
    # PROPERTY CATEGORIES
    # =================================================

    st.markdown(
        '<div class="section-title">🏘️ Explore Properties</div>',
        unsafe_allow_html=True
    )

    categories = [
        ("🏢", "Apartments"),
        ("🏡", "Villas"),
        ("🏠", "Independent Houses"),
        ("🌳", "Plots & Land"),
        ("🏬", "Commercial"),
        ("🏗️", "New Projects"),
    ]

    cols = st.columns(6)

    for i, category in enumerate(categories):

        with cols[i]:

            st.markdown(
                f"""
                <div class="category-card">

                    <div class="category-icon">
                        {category[0]}
                    </div>

                    <b>{category[1]}</b>

                </div>
                """,
                unsafe_allow_html=True
            )

    # =================================================
    # FEATURED PROPERTIES
    # =================================================

    st.markdown(
        '<div class="section-title">⭐ Featured Properties</div>',
        unsafe_allow_html=True
    )

    properties = [

        {
            "title": "Premium 3 BHK Apartment",
            "location": "Nagpur, Maharashtra",
            "price": "₹85 Lakh",
            "area": "1,850 Sq.Ft."
        },

        {
            "title": "Luxury Villa",
            "location": "Pune, Maharashtra",
            "price": "₹1.75 Crore",
            "area": "3,200 Sq.Ft."
        },

        {
            "title": "Residential Plot",
            "location": "Nashik, Maharashtra",
            "price": "₹35 Lakh",
            "area": "2,000 Sq.Ft."
        }

    ]

    property_cols = st.columns(3)

    for i, property_data in enumerate(properties):

        with property_cols[i]:

            st.markdown(
                f"""
                <div class="property-card">

                    <h3>{property_data["title"]}</h3>

                    <p>📍 {property_data["location"]}</p>

                    <h3>{property_data["price"]}</h3>

                    <p>📐 {property_data["area"]}</p>

                </div>
                """,
                unsafe_allow_html=True
            )

            st.button(
                "View Property",
                key=f"property_{i}",
                use_container_width=True
            )

    # =================================================
    # WHY FIRSTCHOICE PROPERTY HUB
    # =================================================

    st.markdown(
        '<div class="section-title">✨ Why FirstChoice Property Hub?</div>',
        unsafe_allow_html=True
    )

    why_col1, why_col2, why_col3, why_col4 = st.columns(4)

    features = [

        ("🔐", "Verified Users"),
        ("🏠", "Verified Properties"),
        ("📱", "Mobile Verified"),
        ("🛡️", "Secure Platform")

    ]

    for col, feature in zip(
        [why_col1, why_col2, why_col3, why_col4],
        features
    ):

        with col:

            st.markdown(
                f"""
                <div class="category-card">

                    <div class="category-icon">
                        {feature[0]}
                    </div>

                    <b>{feature[1]}</b>

                </div>
                """,
                unsafe_allow_html=True
            )

    # =================================================
    # POST PROPERTY
    # =================================================

    st.markdown(
        '<div class="section-title">🏠 Want to Sell or Rent Your Property?</div>',
        unsafe_allow_html=True
    )

    post_col1, post_col2 = st.columns([3, 1])

    with post_col1:

        st.write(
            "List your property and reach buyers and tenants across India."
        )

    with post_col2:

        st.button(
            "➕ Post Your Property",
            use_container_width=True
        )

    # =================================================
    # FOOTER
    # =================================================

    st.markdown(
        """
        <div class="footer">

            <h3>FirstChoice Infra Property Hub</h3>

            <p>
            India's Smart Real Estate Marketplace
            </p>

            <p>
            Buy • Sell • Rent • Invest
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )
