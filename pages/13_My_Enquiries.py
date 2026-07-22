import streamlit as st
from datetime import date

# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 13 - SMART ENQUIRY & LEAD MANAGEMENT CRM
# ============================================================

st.set_page_config(
    page_title="My Enquiries | FirstChoice Property Hub",
    page_icon="💬",
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

/* BRAND */

.brand {

    background:
    linear-gradient(
        135deg,
        #071952,
        #2563EB,
        #7C3AED,
        #EC4899
    );

    padding: 22px 32px;

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

/* HERO */

.hero {

    margin-top: 28px;

    padding: 45px;

    border-radius: 32px;

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
    0 25px 70px
    rgba(37,99,235,0.25);
}

.hero-title {

    font-size: 42px;

    font-weight: 900;
}

.hero-subtitle {

    font-size: 16px;

    color:
    rgba(255,255,255,0.88);
}

/* SECTION */

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
}

.section-title {

    font-size: 27px;

    font-weight: 900;
}

.section-subtitle {

    font-size: 13px;

    color:
    rgba(255,255,255,0.82);
}

/* STAT CARD */

.stat-card {

    padding: 25px;

    border-radius: 25px;

    background: white;

    box-shadow:
    0 12px 35px
    rgba(0,0,0,0.07);

    min-height: 145px;
}

.stat-number {

    font-size: 34px;

    font-weight: 900;

    color: #4C1D95;
}

.stat-label {

    font-size: 14px;

    color: #64748B;
}

/* LEAD CARD */

.lead-card {

    background: white;

    padding: 28px;

    border-radius: 28px;

    box-shadow:
    0 15px 40px
    rgba(0,0,0,0.07);

    margin-bottom: 25px;
}

/* HOT */

.hot {

    color: #DC2626;

    font-weight: 900;
}

/* WARM */

.warm {

    color: #D97706;

    font-weight: 900;
}

/* COLD */

.cold {

    color: #2563EB;

    font-weight: 900;
}

/* AI */

.ai-card {

    padding: 35px;

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

/* FOOTER */

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
PROPERTY HUB • SMART REAL ESTATE CRM
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<div class="hero-title">
💬 My Enquiries & Leads
</div>

<div class="hero-subtitle">
Manage buyer enquiries, follow-ups, site visits and
real estate opportunities from one powerful dashboard.
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# DASHBOARD STATISTICS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📊 Lead Overview
</div>

<div class="section-subtitle">
Track your buyer interest and conversion pipeline.
</div>

</div>
""", unsafe_allow_html=True)


stats = [

    ("💬", "Total Enquiries", "428"),

    ("🔥", "Hot Leads", "64"),

    ("🟠", "Warm Leads", "128"),

    ("🔵", "Cold Leads", "236"),

    ("📅", "Site Visits", "86"),

    ("🤝", "Converted", "18")

]


stat_cols = st.columns(3)


for index, stat in enumerate(stats):

    with stat_cols[index % 3]:

        st.markdown(
            f"""
            <div class="stat-card">

            <div style="font-size:35px;">
            {stat[0]}
            </div>

            <div class="stat-number">
            {stat[2]}
            </div>

            <div class="stat-label">
            {stat[1]}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# LEAD FILTERS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🔎 Search & Filter Leads
</div>

<div class="section-subtitle">
Find the right buyer or enquiry quickly.
</div>

</div>
""", unsafe_allow_html=True)


f1, f2, f3 = st.columns(3)


with f1:

    lead_status = st.selectbox(

        "Lead Status",

        [
            "All Leads",
            "New",
            "Contacted",
            "Follow-up",
            "Site Visit",
            "Negotiation",
            "Converted",
            "Lost"
        ]

    )


with f2:

    lead_priority = st.selectbox(

        "Lead Priority",

        [
            "All",
            "🔥 Hot",
            "🟠 Warm",
            "🔵 Cold"
        ]

    )


with f3:

    lead_search = st.text_input(

        "Search Lead",

        placeholder=
        "Search buyer name, mobile or property"

    )


# ============================================================
# DEMO LEADS
# ============================================================

leads = [

    {

        "name":
        "Rahul Sharma",

        "mobile":
        "+91 XXXXX XXXXX",

        "property":
        "Premium 3 BHK Luxury Apartment",

        "location":
        "Civil Lines, Nagpur",

        "priority":
        "🔥 Hot",

        "status":
        "Negotiation",

        "source":
        "Property Search",

        "date":
        "Today"

    },

    {

        "name":
        "Priya Verma",

        "mobile":
        "+91 XXXXX XXXXX",

        "property":
        "Luxury Independent Villa",

        "location":
        "Baner, Pune",

        "priority":
        "🟠 Warm",

        "status":
        "Site Visit",

        "source":
        "Google Search",

        "date":
        "Yesterday"

    },

    {

        "name":
        "Amit Patel",

        "mobile":
        "+91 XXXXX XXXXX",

        "property":
        "Premium Residential Plot",

        "location":
        "Wardha Road, Nagpur",

        "priority":
        "🔵 Cold",

        "status":
        "New",

        "source":
        "Social Media",

        "date":
        "2 Days Ago"

    }

]


# ============================================================
# LEAD CARDS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
👥 Buyer Enquiries
</div>

<div class="section-subtitle">
Manage and follow up with your potential customers.
</div>

</div>
""", unsafe_allow_html=True)


for index, lead in enumerate(leads):

    st.markdown(
        f"""
        <div class="lead-card">

        <h2>
        👤 {lead['name']}
        </h2>

        <p>
        📱 {lead['mobile']}
        </p>

        <hr>

        <p>
        🏠 <b>Interested Property:</b>
        {lead['property']}
        </p>

        <p>
        📍 {lead['location']}
        </p>

        <p>
        🎯 <b>Priority:</b>
        {lead['priority']}
        </p>

        <p>
        🔄 <b>Status:</b>
        {lead['status']}
        </p>

        <p>
        🌐 <b>Lead Source:</b>
        {lead['source']}
        </p>

        <p>
        🕒 <b>Received:</b>
        {lead['date']}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    c1, c2, c3, c4 = st.columns(4)


    with c1:

        if st.button(

            "📞 Call",

            key=f"call_{index}",

            use_container_width=True

        ):

            st.info(

                "Calling feature will connect to the verified mobile system."

            )


    with c2:

        if st.button(

            "💬 Message",

            key=f"message_{index}",

            use_container_width=True

        ):

            st.info(

                "Secure messaging system will open."

            )


    with c3:

        if st.button(

            "📅 Site Visit",

            key=f"site_{index}",

            use_container_width=True

        ):

            st.success(

                "Site visit scheduling started."

            )


    with c4:

        if st.button(

            "📝 Follow-up",

            key=f"follow_{index}",

            use_container_width=True

        ):

            st.info(

                "Follow-up manager will open."

            )


    st.write("")


# ============================================================
# FOLLOW-UP MANAGER
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📅 Follow-up Manager
</div>

<div class="section-subtitle">
Never miss an important buyer follow-up.
</div>

</div>
""", unsafe_allow_html=True)


fu1, fu2 = st.columns(2)


with fu1:

    followup_date = st.date_input(

        "Next Follow-up Date",

        value=date.today()

    )


with fu2:

    followup_time = st.selectbox(

        "Preferred Follow-up Time",

        [

            "10:00 AM",

            "12:00 PM",

            "2:00 PM",

            "4:00 PM",

            "6:00 PM",

            "8:00 PM"

        ]

    )


followup_note = st.text_area(

    "Follow-up Note",

    placeholder=
    "Example: Buyer wants to negotiate price and visit property next weekend."

)


if st.button(

    "📌 SAVE FOLLOW-UP",

    use_container_width=True

):

    st.success(

        "Follow-up successfully scheduled."

    )


# ============================================================
# AI SMART LEAD ASSISTANT
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🤖 FirstChoice Smart Lead Assistant
</div>

<div class="section-subtitle">
Future AI-powered lead intelligence for real estate professionals.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="ai-card">

<h2>
🧠 Smart Lead Recommendations
</h2>

<p>
🔥 <b>High Priority:</b>
Rahul Sharma appears highly interested and has entered
the negotiation stage.
</p>

<p>
📅 <b>Recommended Action:</b>
Schedule a personal call and offer a property site visit.
</p>

<p>
🎯 <b>Conversion Opportunity:</b>
Your hot leads have a higher probability of conversion.
</p>

<p>
🤖 Future AI features will analyse enquiry behaviour,
response patterns and buyer preferences to help
property professionals prioritise their next action.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# LEAD SOURCE ANALYTICS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📈 Lead Source Performance
</div>

<div class="section-subtitle">
Understand where your best buyers are coming from.
</div>

</div>
""", unsafe_allow_html=True)


s1, s2, s3 = st.columns(3)


with s1:

    st.metric(

        "🔎 Property Search",

        "184 Leads",

        "+24%"

    )


with s2:

    st.metric(

        "🌐 Google Search",

        "126 Leads",

        "+18%"

    )


with s3:

    st.metric(

        "📱 Social Media",

        "118 Leads",

        "+12%"

    )


# ============================================================
# CRM DIFFERENTIATOR
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🚀 FirstChoice Smart CRM
</div>

<div class="section-subtitle">
More than a property portal.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="ai-card">

<h2>
🏆 From Property Listing to Deal Closure
</h2>

<p>
FirstChoice Property Hub is designed to help
owners, agents and builders manage their complete
customer journey.
</p>

<p>
🏠 Property Listing
</p>

<p>
🔎 Buyer Discovery
</p>

<p>
💬 Enquiry
</p>

<p>
📞 Communication
</p>

<p>
📅 Site Visit
</p>

<p>
🤝 Negotiation
</p>

<p>
✅ Deal Closure
</p>

<p>
📊 Performance Analytics
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
