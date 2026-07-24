import streamlit as st
import pandas as pd
from datetime import date, datetime

# ============================================================
# PAGE 1 — ADMIN / BOSS MASTER CONTROL CENTER
# FIRSTCHOICE INFRA PROPERTY HUB
#
# UPDATED VERSION
#
# NEW NAVIGATION:
# 1. 🏠 Dashboard Overview
# 2. 👥 User Management
# 3. 🏡 Property Management
# 4. 📢 Advertisement Management
# 5. 💳 Payments & Subscriptions
# 6. 💰 Revenue & Reports
# 7. 👨‍💼 Managers & Staff
# 8. 🔔 Alerts & Moderation
# 9. 🔐 Security & Audit Logs
# 10. ⚡ Quick Actions
#
# NOTE:
# यह version demo/local data के साथ काम करेगा.
# Production में database/API से data connect किया जा सकता है.
# ============================================================


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Admin Master Control Center | FirstChoice Property Hub",
    page_icon="👑",
    layout="wide"
)


# ============================================================
# ADMIN SECURITY CHECK
# ============================================================

user_role = st.session_state.get(
    "user_role",
    "admin"
)

if user_role != "admin":

    st.error(
        "🚫 Access Denied — This page is only available to Admin / Boss."
    )

    st.stop()


# ============================================================
# SESSION STATE
# ============================================================

if "admin_action_log" not in st.session_state:

    st.session_state.admin_action_log = []


if "approved_users" not in st.session_state:

    st.session_state.approved_users = []


if "rejected_users" not in st.session_state:

    st.session_state.rejected_users = []


if "approved_properties" not in st.session_state:

    st.session_state.approved_properties = []


if "rejected_properties" not in st.session_state:

    st.session_state.rejected_properties = []


if "approved_ads" not in st.session_state:

    st.session_state.approved_ads = []


if "rejected_ads" not in st.session_state:

    st.session_state.rejected_ads = []


# ============================================================
# HELPER FUNCTION
# ============================================================

def add_audit_log(
    action,
    target,
    details=""
):

    st.session_state.admin_action_log.append({

        "Date & Time":
        datetime.now().strftime(
            "%d %b %Y %I:%M %p"
        ),

        "Admin":
        "Admin / Boss",

        "Action":
        action,

        "Target":
        target,

        "Details":
        details

    })


# ============================================================
# PREMIUM MULTICOLOUR CSS
# ============================================================

st.markdown("""
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

    visibility:
    hidden;

}

#MainMenu {

    visibility:
    hidden;

}

footer {

    visibility:
    hidden;

}


/* ============================================================
HERO
============================================================ */

.hero {

    padding:
    48px;

    border-radius:
    36px;

    color:
    white;

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
    rgba(
        37,
        99,
        235,
        0.32
    );

    margin-bottom:
    30px;

}

.hero h1 {

    font-size:
    44px;

    font-weight:
    900;

}

.hero p {

    font-size:
    18px;

    line-height:
    1.8;

}


/* ============================================================
SECTION
============================================================ */

.section {

    margin-top:
    30px;

    margin-bottom:
    22px;

    padding:
    28px 32px;

    border-radius:
    28px;

    color:
    white;

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
    rgba(
        79,
        70,
        229,
        0.22
    );

}

.section h2 {

    margin:
    0;

    font-size:
    28px;

    font-weight:
    900;

}


/* ============================================================
CARD
============================================================ */

.card {

    padding:
    25px;

    border-radius:
    24px;

    background:
    linear-gradient(
        135deg,
        #FFFFFF,
        #F5F3FF,
        #EFF6FF
    );

    border:
    1px solid
    #E0E7FF;

    box-shadow:
    0 10px 30px
    rgba(
        0,
        0,
        0,
        0.06
    );

    margin-bottom:
    18px;

}


/* ============================================================
REVENUE
============================================================ */

.revenue {

    padding:
    32px;

    border-radius:
    28px;

    color:
    white;

    background:
    linear-gradient(
        135deg,
        #047857,
        #059669,
        #10B981
    );

    box-shadow:
    0 20px 55px
    rgba(
        5,
        150,
        105,
        0.25
    );

}


/* ============================================================
ALERT
============================================================ */

.alert {

    padding:
    30px;

    border-radius:
    28px;

    color:
    white;

    background:
    linear-gradient(
        135deg,
        #B45309,
        #F59E0B,
        #F97316
    );

}


/* ============================================================
DANGER
============================================================ */

.danger {

    padding:
    30px;

    border-radius:
    28px;

    color:
    white;

    background:
    linear-gradient(
        135deg,
        #991B1B,
        #DC2626,
        #EF4444
    );

}


/* ============================================================
NAVIGATION
============================================================ */

.nav-box {

    padding:
    18px;

    border-radius:
    20px;

    background:
    linear-gradient(
        135deg,
        #FFFFFF,
        #EEF2FF
    );

    border:
    1px solid
    #CBD5E1;

    margin-bottom:
    20px;

}


/* ============================================================
MOBILE
============================================================ */

@media (
    max-width:
    768px
) {

    .hero {

        padding:
        30px;

    }

    .hero h1 {

        font-size:
        32px;

    }

}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<h1>
👑 Admin / Boss Master Control Center
</h1>

<p>
Welcome to the central command dashboard of
<b>FirstChoice Property Hub</b>.
</p>

<p>
Complete control over users, property listings,
advertisements, subscriptions, payments, revenue,
managers, staff, security and company activities.
</p>

</div>
""", unsafe_allow_html=True)


st.caption(
    f"📅 Dashboard Date: "
    f"{date.today().strftime('%d %B %Y')}"
)


# ============================================================
# MAIN NAVIGATION
# ============================================================

st.markdown("""
<div class="section">

<h2>
🧭 Admin Navigation Center
</h2>

</div>
""", unsafe_allow_html=True)


admin_page = st.selectbox(

    "Select Admin Section",

    [

        "🏠 Dashboard Overview",

        "👥 User Management",

        "🏡 Property Management",

        "📢 Advertisement Management",

        "💳 Payments & Subscriptions",

        "💰 Revenue & Reports",

        "👨‍💼 Managers & Staff",

        "🔔 Alerts & Moderation",

        "🔐 Security & Audit Logs",

        "⚡ Quick Actions"

    ],

    key="admin_navigation"

)


# ################################################################
# PAGE 1 — DASHBOARD OVERVIEW
# ################################################################

if admin_page == "🏠 Dashboard Overview":

    st.markdown("""
    <div class="section">

    <h2>
    📊 Complete Company Overview
    </h2>

    </div>
    """, unsafe_allow_html=True)


    c1, c2, c3, c4 = st.columns(4)


    with c1:

        st.metric(
            "👥 Total Users",
            "12,480"
        )


    with c2:

        st.metric(
            "🟢 Active Users",
            "9,860"
        )


    with c3:

        st.metric(
            "🔴 Inactive Users",
            "2,620"
        )


    with c4:

        st.metric(
            "🏠 Total Properties",
            "3,245"
        )


    c5, c6, c7, c8 = st.columns(4)


    with c5:

        st.metric(
            "📢 Total Ads",
            "4,860"
        )


    with c6:

        st.metric(
            "👨‍💼 Managers",
            "42"
        )


    with c7:

        st.metric(
            "👤 Staff / Executives",
            "185"
        )


    with c8:

        st.metric(
            "⭐ Paid Subscribers",
            "1,240"
        )


    # ========================================================
    # PENDING ACTIONS
    # ========================================================

    st.markdown("""
    <div class="section">

    <h2>
    🚨 Admin Pending Actions
    </h2>

    </div>
    """, unsafe_allow_html=True)


    p1, p2, p3, p4 = st.columns(4)


    with p1:

        st.metric(
            "👤 User Requests",
            "27"
        )


    with p2:

        st.metric(
            "🏠 Property Approvals",
            "18"
        )


    with p3:

        st.metric(
            "📢 Ad Approvals",
            "35"
        )


    with p4:

        st.metric(
            "💳 Payment Reviews",
            "6"
        )


    st.markdown("""
    <div class="alert">

    <h2>
    ⚡ Admin Action Required
    </h2>

    <p>
    Pending requests and approvals are waiting for your review.
    </p>

    <p>
    Use the Admin Navigation Center to manage
    Users, Properties, Ads and Payments.
    </p>

    </div>
    """, unsafe_allow_html=True)


    # ========================================================
    # COMPANY SNAPSHOT
    # ========================================================

    st.markdown("""
    <div class="section">

    <h2>
    📈 Company Performance Snapshot
    </h2>

    </div>
    """, unsafe_allow_html=True)


    snapshot_data = {

        "Metric": [

            "New Users This Month",

            "New Properties",

            "New Advertisements",

            "Subscription Revenue",

            "Property Views",

            "Lead Enquiries"

        ],

        "Value": [

            "1,240",

            "186",

            "425",

            "₹24,85,600",

            "1,85,420",

            "12,860"

        ]

    }


    st.dataframe(

        pd.DataFrame(
            snapshot_data
        ),

        use_container_width=True,

        hide_index=True

    )


# ################################################################
# PAGE 2 — USER MANAGEMENT
# ################################################################

elif admin_page == "👥 User Management":

    st.markdown("""
    <div class="section">

    <h2>
    👥 User Request & Account Management
    </h2>

    </div>
    """, unsafe_allow_html=True)


    u1, u2, u3, u4 = st.columns(4)


    with u1:

        st.metric(
            "👥 Total Users",
            "12,480"
        )


    with u2:

        st.metric(
            "🟢 Active",
            "9,860"
        )


    with u3:

        st.metric(
            "⏳ Pending",
            "27"
        )


    with u4:

        st.metric(
            "🚫 Suspended",
            "43"
        )


    request_type = st.selectbox(

        "Select User Type",

        [

            "All Users",

            "Buyer",

            "Owner",

            "Agent",

            "Builder",

            "Manager",

            "Staff / Executive"

        ]

    )


    request_search = st.text_input(

        "🔍 Search User",

        placeholder=
        "Search by name, mobile or email"

    )


    requests = [

        {

            "name":
            "Rahul Sharma",

            "role":
            "Buyer",

            "mobile":
            "9876543210",

            "date":
            "22 Jul 2026",

            "status":
            "Pending"

        },

        {

            "name":
            "Amit Properties",

            "role":
            "Agent",

            "mobile":
            "9876500000",

            "date":
            "22 Jul 2026",

            "status":
            "Pending"

        },

        {

            "name":
            "XYZ Builders",

            "role":
            "Builder",

            "mobile":
            "9876511111",

            "date":
            "21 Jul 2026",

            "status":
            "Pending"

        }

    ]


    for i, request in enumerate(
        requests
    ):

        if request["role"] != request_type and request_type != "All Users":

            continue


        if request_search:

            search_text = (

                request["name"]
                +
                request["mobile"]

            ).lower()


            if request_search.lower() not in search_text:

                continue


        st.markdown(
            '<div class="card">',
            unsafe_allow_html=True
        )


        c1, c2, c3, c4 = st.columns(
            [2, 1, 2, 2]
        )


        with c1:

            st.write(
                f"👤 **{request['name']}**"
            )


        with c2:

            st.write(
                request["role"]
            )


        with c3:

            st.write(
                f"📱 {request['mobile']}"
            )


        with c4:

            approve, reject = st.columns(2)


            with approve:

                if st.button(

                    "✅ Accept",

                    key=
                    f"user_accept_{i}"

                ):

                    st.session_state.approved_users.append(
                        request["name"]
                    )


                    add_audit_log(

                        "User Approved",

                        request["name"],

                        request["role"]

                    )


                    st.success(
                        f"{request['name']} accepted."
                    )


            with reject:

                if st.button(

                    "❌ Reject",

                    key=
                    f"user_reject_{i}"

                ):

                    st.session_state.rejected_users.append(
                        request["name"]
                    )


                    add_audit_log(

                        "User Rejected",

                        request["name"],

                        request["role"]

                    )


                    st.error(
                        f"{request['name']} rejected."
                    )


        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


# ################################################################
# PAGE 3 — PROPERTY MANAGEMENT
# ################################################################

elif admin_page == "🏡 Property Management":

    st.markdown("""
    <div class="section">

    <h2>
    🏡 Property & Listing Management
    </h2>

    </div>
    """, unsafe_allow_html=True)


    p1, p2, p3, p4 = st.columns(4)


    with p1:

        st.metric(
            "⏳ Pending",
            "18"
        )


    with p2:

        st.metric(
            "✅ Approved",
            "3,120"
        )


    with p3:

        st.metric(
            "❌ Rejected",
            "92"
        )


    with p4:

        st.metric(
            "🚫 Suspended",
            "33"
        )


    property_action = st.selectbox(

        "Property Action",

        [

            "Review Pending Properties",

            "Approve Property",

            "Reject Property",

            "Suspend Property",

            "Feature Property"

        ]

    )


    property_search = st.text_input(

        "🔍 Search Property",

        placeholder=
        "Property name, ID or owner"

    )


    properties = [

        {

            "id":
            "FC-1001",

            "name":
            "Green Valley Residency",

            "owner":
            "Rahul Sharma",

            "location":
            "Nagpur",

            "status":
            "Pending"

        },

        {

            "id":
            "FC-1002",

            "name":
            "FirstChoice Heights",

            "owner":
            "ABC Builders",

            "location":
            "Pune",

            "status":
            "Pending"

        },

        {

            "id":
            "FC-1003",

            "name":
            "Premium City",

            "owner":
            "XYZ Developers",

            "location":
            "Mumbai",

            "status":
            "Pending"

        }

    ]


    for i, prop in enumerate(
        properties
    ):

        if property_search:

            search_text = (

                prop["id"]
                +
                prop["name"]
                +
                prop["owner"]
                +
                prop["location"]

            ).lower()


            if property_search.lower() not in search_text:

                continue


        st.markdown(
            '<div class="card">',
            unsafe_allow_html=True
        )


        c1, c2, c3, c4 = st.columns(
            [1, 2, 2, 2]
        )


        with c1:

            st.write(
                f"**{prop['id']}**"
            )


        with c2:

            st.write(
                f"🏠 {prop['name']}"
            )


        with c3:

            st.write(
                f"👤 {prop['owner']}"
            )


        with c4:

            a, b, c = st.columns(3)


            with a:

                if st.button(

                    "✅",

                    key=
                    f"property_approve_{i}"

                ):

                    st.session_state.approved_properties.append(
                        prop["id"]
                    )


                    add_audit_log(

                        "Property Approved",

                        prop["id"],

                        prop["name"]

                    )


                    st.success(
                        "Property Approved"
                    )


            with b:

                if st.button(

                    "❌",

                    key=
                    f"property_reject_{i}"

                ):

                    st.session_state.rejected_properties.append(
                        prop["id"]
                    )


                    add_audit_log(

                        "Property Rejected",

                        prop["id"],

                        prop["name"]

                    )


                    st.warning(
                        "Property Rejected"
                    )


            with c:

                if st.button(

                    "🚫",

                    key=
                    f"property_suspend_{i}"

                ):

                    add_audit_log(

                        "Property Suspended",

                        prop["id"],

                        prop["name"]

                    )


                    st.error(
                        "Property Suspended"
                    )


        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


# ################################################################
# PAGE 4 — ADVERTISEMENT MANAGEMENT
# ################################################################

elif admin_page == "📢 Advertisement Management":

    st.markdown("""
    <div class="section">

    <h2>
    📢 Advertisement Management Center
    </h2>

    </div>
    """, unsafe_allow_html=True)


    a1, a2, a3, a4 = st.columns(4)


    with a1:

        st.metric(
            "📢 Total Ads",
            "4,860"
        )


    with a2:

        st.metric(
            "⏳ Pending",
            "35"
        )


    with a3:

        st.metric(
            "✅ Approved",
            "4,510"
        )


    with a4:

        st.metric(
            "❌ Rejected",
            "315"
        )


    ad_search = st.text_input(

        "🔍 Search Advertisement",

        placeholder=
        "Search Ad ID, advertiser or property"

    )


    ads = [

        {

            "id":
            "AD-001",

            "advertiser":
            "ABC Properties",

            "property":
            "Premium Villa",

            "status":
            "Pending"

        },

        {

            "id":
            "AD-002",

            "advertiser":
            "XYZ Builders",

            "property":
            "Luxury Apartment",

            "status":
            "Pending"

        },

        {

            "id":
            "AD-003",

            "advertiser":
            "Rahul Properties",

            "property":
            "Residential Plot",

            "status":
            "Pending"

        }

    ]


    for i, ad in enumerate(
        ads
    ):

        if ad_search:

            search_text = (

                ad["id"]
                +
                ad["advertiser"]
                +
                ad["property"]

            ).lower()


            if ad_search.lower() not in search_text:

                continue


        c1, c2, c3, c4 = st.columns(
            [1, 2, 2, 2]
        )


        with c1:

            st.write(
                f"**{ad['id']}**"
            )


        with c2:

            st.write(
                ad["advertiser"]
            )


        with c3:

            st.write(
                ad["property"]
            )


        with c4:

            approve, reject = st.columns(2)


            with approve:

                if st.button(

                    "✅ Approve",

                    key=
                    f"ad_approve_{i}"

                ):

                    st.session_state.approved_ads.append(
                        ad["id"]
                    )


                    add_audit_log(

                        "Advertisement Approved",

                        ad["id"],

                        ad["property"]

                    )


                    st.success(
                        "Advertisement approved."
                    )


            with reject:

                if st.button(

                    "❌ Reject",

                    key=
                    f"ad_reject_{i}"

                ):

                    st.session_state.rejected_ads.append(
                        ad["id"]
                    )


                    add_audit_log(

                        "Advertisement Rejected",

                        ad["id"],

                        ad["property"]

                    )


                    st.warning(
                        "Advertisement rejected."
                    )


# ################################################################
# PAGE 5 — PAYMENTS & SUBSCRIPTIONS
# ################################################################

elif admin_page == "💳 Payments & Subscriptions":

    st.markdown("""
    <div class="section">

    <h2>
    💳 Subscription & Payment Management
    </h2>

    </div>
    """, unsafe_allow_html=True)


    p1, p2, p3, p4 = st.columns(4)


    with p1:

        st.metric(
            "⭐ Paid Subscribers",
            "1,240"
        )


    with p2:

        st.metric(
            "🟢 Active Plans",
            "1,180"
        )


    with p3:

        st.metric(
            "⏳ Pending",
            "24"
        )


    with p4:

        st.metric(
            "❌ Failed",
            "12"
        )


    payment_status = st.selectbox(

        "Payment Status",

        [

            "All",

            "Successful",

            "Pending",

            "Failed",

            "Refunded"

        ]

    )


    payment_search = st.text_input(

        "🔍 Search Payment",

        placeholder=
        "Transaction ID, user or plan"

    )


    payment_data = [

        {

            "Transaction ID":
            "TXN-10001",

            "User":
            "Rahul Sharma",

            "Plan":
            "Premium",

            "Amount":
            "₹999",

            "Date":
            "22 Jul 2026",

            "Status":
            "Successful"

        },

        {

            "Transaction ID":
            "TXN-10002",

            "User":
            "ABC Properties",

            "Plan":
            "Business",

            "Amount":
            "₹4,999",

            "Date":
            "21 Jul 2026",

            "Status":
            "Successful"

        },

        {

            "Transaction ID":
            "TXN-10003",

            "User":
            "XYZ Builders",

            "Plan":
            "Enterprise",

            "Amount":
            "₹9,999",

            "Date":
            "20 Jul 2026",

            "Status":
            "Successful"

        }

    ]


    payment_df = pd.DataFrame(
        payment_data
    )


    if payment_status != "All":

        payment_df = payment_df[
            payment_df["Status"]
            ==
            payment_status
        ]


    st.dataframe(

        payment_df,

        use_container_width=True,

        hide_index=True

    )


# ################################################################
# PAGE 6 — REVENUE & REPORTS
# ################################################################

elif admin_page == "💰 Revenue & Reports":

    st.markdown("""
    <div class="section">

    <h2>
    💰 Revenue & Business Reports
    </h2>

    </div>
    """, unsafe_allow_html=True)


    r1, r2 = st.columns(2)


    with r1:

        revenue_start = st.date_input(

            "📅 Start Date",

            value=date(

                date.today().year,

                1,

                1

            )

        )


    with r2:

        revenue_end = st.date_input(

            "📅 End Date",

            value=date.today()

        )


    if revenue_start > revenue_end:

        st.error(
            "Start Date cannot be after End Date."
        )


    else:

        st.markdown("""
        <div class="revenue">

        <h2>
        💰 Company Subscription Revenue
        </h2>

        <h1>
        ₹24,85,600
        </h1>

        <p>
        Selected Date Range Revenue
        </p>

        </div>
        """, unsafe_allow_html=True)


    report_type = st.selectbox(

        "📊 Select Report",

        [

            "Revenue Summary",

            "Subscription Report",

            "User Growth Report",

            "Property Growth Report",

            "Advertisement Report",

            "Payment Report"

        ]

    )


    if st.button(

        "📥 GENERATE REPORT",

        use_container_width=True

    ):

        add_audit_log(

            "Report Generated",

            report_type,

            f"{revenue_start} to {revenue_end}"

        )


        st.success(

            f"✅ {report_type} generated successfully."

        )


# ################################################################
# PAGE 7 — MANAGERS & STAFF
# ################################################################

elif admin_page == "👨‍💼 Managers & Staff":

    st.markdown("""
    <div class="section">

    <h2>
    👨‍💼 Manager & Staff Management
    </h2>

    </div>
    """, unsafe_allow_html=True)


    m1, m2, m3, m4 = st.columns(4)


    with m1:

        st.metric(
            "👨‍💼 Total Managers",
            "42"
        )


    with m2:

        st.metric(
            "🟢 Active Managers",
            "39"
        )


    with m3:

        st.metric(
            "👤 Total Staff",
            "185"
        )


    with m4:

        st.metric(
            "🟢 Active Staff",
            "168"
        )


    team_action = st.selectbox(

        "Team Management Action",

        [

            "View All Teams",

            "Manager Performance",

            "Staff Performance",

            "Create New Manager",

            "Create New Staff",

            "Suspend Account"

        ]

    )


    st.markdown("""
    <div class="card">

    <h3>
    👥 Team Hierarchy
    </h3>

    <p>
    👑 Admin / Boss
    </p>

    <p>
    └── 👨‍💼 Managers
    </p>

    <p>
    &nbsp;&nbsp;&nbsp;&nbsp;└── 👤 Executives / Staff
    </p>

    <p>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── 👥 Downline / Partners
    </p>

    </div>
    """, unsafe_allow_html=True)


    if st.button(

        "👥 OPEN DOWNLINE & TEAM MANAGEMENT",

        use_container_width=True

    ):

        add_audit_log(

            "Opened Team Management",

            "Downline",

            "Admin Team Management"

        )


        st.info(
            "Admin Downline Management module opened."
        )


# ################################################################
# PAGE 8 — ALERTS & MODERATION
# ################################################################

elif admin_page == "🔔 Alerts & Moderation":

    st.markdown("""
    <div class="section">

    <h2>
    🔔 Company Alerts & Moderation Center
    </h2>

    </div>
    """, unsafe_allow_html=True)


    alerts = [

        "⚠️ 27 new user requests are waiting for approval.",

        "🏠 18 property listings need verification.",

        "📢 35 advertisements are waiting for approval.",

        "💳 6 subscription payments need review.",

        "🚨 4 properties have been reported by users.",

        "🔐 3 user accounts have been flagged for suspicious activity."

    ]


    for i, alert in enumerate(
        alerts
    ):

        st.warning(
            alert
        )


        if st.button(

            "✅ Mark Reviewed",

            key=
            f"alert_review_{i}"

        ):

            add_audit_log(

                "Alert Reviewed",

                f"Alert {i + 1}",

                alert

            )


            st.success(
                "Alert marked as reviewed."
            )


# ################################################################
# PAGE 9 — SECURITY & AUDIT LOGS
# ################################################################

elif admin_page == "🔐 Security & Audit Logs":

    st.markdown("""
    <div class="section">

    <h2>
    🔐 Security & Admin Audit Center
    </h2>

    </div>
    """, unsafe_allow_html=True)


    s1, s2, s3, s4 = st.columns(4)


    with s1:

        st.metric(
            "🔐 Admin Login",
            "1"
        )


    with s2:

        st.metric(
            "🛡️ Security Alerts",
            "3"
        )


    with s3:

        st.metric(
            "📋 Audit Actions",
            len(
                st.session_state.admin_action_log
            )
        )


    with s4:

        st.metric(
            "🚨 Suspicious Accounts",
            "3"
        )


    st.markdown("""
    <div class="danger">

    <h2>
    🔐 Admin Security Notice
    </h2>

    <p>
    This dashboard contains sensitive company information.
    Only authorized Admin / Boss accounts should have access.
    </p>

    <p>
    Production version में हर Admin action का permanent Audit Log
    database में save किया जाना चाहिए.
    </p>

    </div>
    """, unsafe_allow_html=True)


    if st.session_state.admin_action_log:

        st.markdown("""
        <div class="section">

        <h2>
        📋 Recent Admin Activity
        </h2>

        </div>
        """, unsafe_allow_html=True)


        audit_df = pd.DataFrame(

            st.session_state.admin_action_log

        )


        st.dataframe(

            audit_df,

            use_container_width=True,

            hide_index=True

        )


    else:

        st.info(
            "No admin actions recorded in this session yet."
        )


    if st.button(

        "🗑️ CLEAR SESSION AUDIT LOG",

        use_container_width=True

    ):

        st.session_state.admin_action_log = []

        st.success(
            "Session audit log cleared."
        )


# ################################################################
# PAGE 10 — QUICK ACTIONS
# ################################################################

elif admin_page == "⚡ Quick Actions":

    st.markdown("""
    <div class="section">

    <h2>
    ⚡ Admin Quick Actions
    </h2>

    </div>
    """, unsafe_allow_html=True)


    q1, q2, q3 = st.columns(3)


    with q1:

        if st.button(

            "👤 Manage Users",

            use_container_width=True

        ):

            add_audit_log(

                "Quick Action",

                "User Management"

            )


            st.success(
                "User Management action selected."
            )


    with q2:

        if st.button(

            "🏠 Manage Properties",

            use_container_width=True

        ):

            add_audit_log(

                "Quick Action",

                "Property Management"

            )


            st.success(
                "Property Management action selected."
            )


    with q3:

        if st.button(

            "📢 Manage Advertisements",

            use_container_width=True

        ):

            add_audit_log(

                "Quick Action",

                "Advertisement Management"

            )


            st.success(
                "Advertisement Management action selected."
            )


    q4, q5, q6 = st.columns(3)


    with q4:

        if st.button(

            "💰 Revenue Reports",

            use_container_width=True

        ):

            add_audit_log(

                "Quick Action",

                "Revenue Reports"

            )


            st.success(
                "Revenue Reports action selected."
            )


    with q5:

        if st.button(

            "👥 Downline Management",

            use_container_width=True

        ):

            add_audit_log(

                "Quick Action",

                "Downline Management"

            )


            st.success(
                "Downline Management action selected."
            )


    with q6:

        if st.button(

            "⚙️ System Settings",

            use_container_width=True

        ):

            add_audit_log(

                "Quick Action",

                "System Settings"

            )


            st.success(
                "System Settings action selected."
            )


    # ========================================================
    # SYSTEM CONTROL
    # ========================================================

    st.markdown("""
    <div class="section">

    <h2>
    ⚙️ System Control
    </h2>

    </div>
    """, unsafe_allow_html=True)


    system_action = st.selectbox(

        "Select System Action",

        [

            "System Status",

            "Database Status",

            "Backup Database",

            "Clear Cache",

            "Maintenance Mode",

            "Notification Broadcast"

        ]

    )


    if st.button(

        "🚀 EXECUTE SYSTEM ACTION",

        use_container_width=True

    ):

        add_audit_log(

            "System Action",

            system_action,

            "Executed from Admin Quick Actions"

        )


        st.success(

            f"✅ System action executed: "
            f"{system_action}"

        )


# ============================================================
# GLOBAL FOOTER
# ============================================================

st.markdown("""
<div class="card">

<h3>
👑 FirstChoice Property Hub — Admin Command Center
</h3>

<p>
Complete company visibility, centralized control,
user management, property moderation, revenue monitoring,
team management and security audit.
</p>

<p>
<b>
Admin / Boss Access Only
</b>
</p>

</div>
""", unsafe_allow_html=True)
