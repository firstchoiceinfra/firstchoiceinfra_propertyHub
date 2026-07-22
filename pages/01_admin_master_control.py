import streamlit as st
from datetime import date, datetime

# ============================================================
# PAGE 1 — ADMIN / BOSS MASTER CONTROL CENTER
# FIRSTCHOICE INFRA PROPERTY HUB
# ============================================================

st.set_page_config(
    page_title="Admin Master Control Center | FirstChoice Property Hub",
    page_icon="👑",
    layout="wide"
)

# ============================================================
# ADMIN SECURITY CHECK
# ============================================================

# IMPORTANT:
# Production version में actual login system से
# st.session_state["user_role"] set होना चाहिए.

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
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

.hero {

    padding: 50px;

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

    margin-bottom: 30px;
}

.hero h1 {

    font-size: 44px;

    font-weight: 900;

}

.hero p {

    font-size: 18px;

    line-height: 1.8;

}

.section {

    margin-top: 30px;

    margin-bottom: 22px;

    padding: 28px 32px;

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

    font-size: 28px;

    font-weight: 900;

}

.card {

    padding: 25px;

    border-radius: 24px;

    background:
    linear-gradient(
        135deg,
        #FFFFFF,
        #F5F3FF,
        #EFF6FF
    );

    border:
    1px solid #E0E7FF;

    box-shadow:
    0 10px 30px
    rgba(0,0,0,0.06);

    margin-bottom: 18px;

}

.revenue {

    padding: 32px;

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
    0 20px 55px
    rgba(5,150,105,0.25);

}

.alert {

    padding: 30px;

    border-radius: 28px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #B45309,
        #F59E0B,
        #F97316
    );

}

.danger {

    padding: 30px;

    border-radius: 28px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #991B1B,
        #DC2626,
        #EF4444
    );

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
FirstChoice Property Hub.
</p>

<p>
Complete control over users, requests, properties,
advertisements, subscriptions, revenue and company activity.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# CURRENT DATE
# ============================================================

st.caption(
    f"📅 Dashboard Date: {date.today().strftime('%d %B %Y')}"
)


# ============================================================
# COMPANY OVERVIEW
# ============================================================

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


# ============================================================
# PENDING ACTIONS
# ============================================================

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
There are pending requests and approvals waiting for your review.
</p>

<p>
Please check User Requests, Property Approvals,
Advertisement Approvals and Payment Reviews.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# USER REQUEST MANAGEMENT
# ============================================================

st.markdown("""
<div class="section">

<h2>
👤 User Request Management
</h2>

</div>
""", unsafe_allow_html=True)


request_type = st.selectbox(

    "Select Request Type",

    [
        "All Requests",
        "New User Registration",
        "Buyer Request",
        "Owner Request",
        "Agent Request",
        "Builder Request",
        "Manager Request",
        "Staff Request"
    ]

)


request_search = st.text_input(

    "🔍 Search Request",

    placeholder="Search by name, mobile or email"

)


requests = [

    {
        "name": "Rahul Sharma",
        "role": "Buyer",
        "date": "22 Jul 2026",
        "status": "Pending"
    },

    {
        "name": "Amit Properties",
        "role": "Agent",
        "date": "22 Jul 2026",
        "status": "Pending"
    },

    {
        "name": "XYZ Builders",
        "role": "Builder",
        "date": "21 Jul 2026",
        "status": "Pending"
    }

]


for i, request in enumerate(requests):

    c1, c2, c3, c4 = st.columns([2, 1, 1, 2])


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
            request["date"]
        )


    with c4:

        approve, reject = st.columns(2)


        with approve:

            if st.button(
                "✅ Accept",
                key=f"approve_user_{i}"
            ):

                st.success(
                    f"{request['name']} accepted."
                )


        with reject:

            if st.button(
                "❌ Reject",
                key=f"reject_user_{i}"
            ):

                st.error(
                    f"{request['name']} rejected."
                )


# ============================================================
# PROPERTY APPROVAL
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏠 Property & Listing Approval Control
</h2>

</div>
""", unsafe_allow_html=True)


property_action = st.selectbox(

    "Select Property Action",

    [
        "All Pending Properties",
        "Approve Property",
        "Reject Property",
        "Suspend Property",
        "Feature Property"
    ]

)


property_name = st.text_input(

    "🔍 Search Property",

    placeholder="Enter property name or property ID"

)


prop1, prop2, prop3, prop4 = st.columns(4)


with prop1:

    st.metric(
        "⏳ Pending",
        "18"
    )


with prop2:

    st.metric(
        "✅ Approved",
        "3,120"
    )


with prop3:

    st.metric(
        "❌ Rejected",
        "92"
    )


with prop4:

    st.metric(
        "🚫 Suspended",
        "33"
    )


a1, a2, a3 = st.columns(3)


with a1:

    if st.button(
        "✅ APPROVE PROPERTY",
        use_container_width=True
    ):

        st.success(
            "Property approval action initiated."
        )


with a2:

    if st.button(
        "❌ REJECT PROPERTY",
        use_container_width=True
    ):

        st.warning(
            "Property rejection action initiated."
        )


with a3:

    if st.button(
        "🚫 SUSPEND PROPERTY",
        use_container_width=True
    ):

        st.error(
            "Property suspension action initiated."
        )


# ============================================================
# ADVERTISEMENT MANAGEMENT
# ============================================================

st.markdown("""
<div class="section">

<h2>
📢 Advertisement Management
</h2>

</div>
""", unsafe_allow_html=True)


ad1, ad2, ad3, ad4 = st.columns(4)


with ad1:

    st.metric(
        "📢 Total Ads",
        "4,860"
    )


with ad2:

    st.metric(
        "⏳ Pending",
        "35"
    )


with ad3:

    st.metric(
        "✅ Approved",
        "4,510"
    )


with ad4:

    st.metric(
        "❌ Rejected",
        "315"
    )


ad_action = st.selectbox(

    "Advertisement Action",

    [
        "Review Pending Ads",
        "Approve Ad",
        "Reject Ad",
        "Suspend Ad",
        "Remove Ad"
    ]

)


ad1, ad2, ad3 = st.columns(3)


with ad1:

    if st.button(
        "✅ ACCEPT AD",
        use_container_width=True
    ):

        st.success(
            "Advertisement approved."
        )


with ad2:

    if st.button(
        "❌ REJECT AD",
        use_container_width=True
    ):

        st.warning(
            "Advertisement rejected."
        )


with ad3:

    if st.button(
        "🚫 REMOVE / SUSPEND",
        use_container_width=True
    ):

        st.error(
            "Advertisement action completed."
        )


# ============================================================
# SUBSCRIPTION & REVENUE
# ============================================================

st.markdown("""
<div class="section">

<h2>
💰 Subscription & Company Revenue
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


rev1, rev2, rev3, rev4 = st.columns(4)


with rev1:

    st.metric(
        "💳 Paid Subscriptions",
        "1,240"
    )


with rev2:

    st.metric(
        "🟢 Active Plans",
        "1,180"
    )


with rev3:

    st.metric(
        "⏳ Pending Payments",
        "24"
    )


with rev4:

    st.metric(
        "❌ Failed Payments",
        "12"
    )


# ============================================================
# PAYMENT HISTORY
# ============================================================

st.markdown("""
<div class="section">

<h2>
💳 Subscription Payment History
</h2>

</div>
""", unsafe_allow_html=True)


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

    placeholder="Search transaction ID or user"

)


payment_data = [

    {
        "User": "Rahul Sharma",
        "Plan": "Premium",
        "Amount": "₹999",
        "Date": "22 Jul 2026",
        "Status": "Successful"
    },

    {
        "User": "ABC Properties",
        "Plan": "Business",
        "Amount": "₹4,999",
        "Date": "21 Jul 2026",
        "Status": "Successful"
    },

    {
        "User": "XYZ Builders",
        "Plan": "Enterprise",
        "Amount": "₹9,999",
        "Date": "20 Jul 2026",
        "Status": "Successful"
    }

]


st.dataframe(

    payment_data,

    use_container_width=True,

    hide_index=True

)


# ============================================================
# USER ACTIVITY
# ============================================================

st.markdown("""
<div class="section">

<h2>
📈 User Activity Monitoring
</h2>

</div>
""", unsafe_allow_html=True)


u1, u2, u3, u4 = st.columns(4)


with u1:

    st.metric(
        "🟢 Online Today",
        "2,480"
    )


with u2:

    st.metric(
        "📅 Active This Week",
        "7,850"
    )


with u3:

    st.metric(
        "📅 Active This Month",
        "9,860"
    )


with u4:

    st.metric(
        "💤 Inactive",
        "2,620"
    )


# ============================================================
# MANAGER & STAFF OVERVIEW
# ============================================================

st.markdown("""
<div class="section">

<h2>
👨‍💼 Manager & Staff Overview
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


if st.button(

    "👥 OPEN DOWNLINE & TEAM MANAGEMENT",

    use_container_width=True

):

    st.info(

        "Opening Admin Downline Management..."

    )


# ============================================================
# COMPANY ALERTS
# ============================================================

st.markdown("""
<div class="section">

<h2>
🔔 Important Company Alerts
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


for alert in alerts:

    st.warning(
        alert
    )


# ============================================================
# ADMIN QUICK ACTIONS
# ============================================================

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

        st.info(
            "User Management opened."
        )


with q2:

    if st.button(
        "🏠 Manage Properties",
        use_container_width=True
    ):

        st.info(
            "Property Management opened."
        )


with q3:

    if st.button(
        "📢 Manage Advertisements",
        use_container_width=True
    ):

        st.info(
            "Advertisement Management opened."
        )


q4, q5, q6 = st.columns(3)


with q4:

    if st.button(
        "💰 Revenue Reports",
        use_container_width=True
    ):

        st.info(
            "Revenue Reports opened."
        )


with q5:

    if st.button(
        "👥 Downline Management",
        use_container_width=True
    ):

        st.info(
            "Downline Management opened."
        )


with q6:

    if st.button(
        "⚙️ System Settings",
        use_container_width=True
    ):

        st.info(
            "System Settings opened."
        )


# ============================================================
# ADMIN SECURITY NOTICE
# ============================================================

st.markdown("""
<div class="danger">

<h2>
🔐 Admin Security
</h2>

<p>
This dashboard contains sensitive company information.
Only authorized Admin / Boss accounts should have access.
</p>

<p>
Production version में हर action का Audit Log रखा जाएगा:
किस Admin ने कौन सा User approve किया, कौन सी Ad reject की,
कब subscription revenue report देखी और कौन सा account suspend किया।
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="card">

<h3>
👑 FirstChoice Property Hub — Admin Command Center
</h3>

<p>
Complete company visibility and centralized control.
</p>

</div>
""", unsafe_allow_html=True)
