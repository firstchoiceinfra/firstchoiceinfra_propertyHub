import streamlit as st
from datetime import datetime

# ============================================================
# PAGE 25 — PROPERTY COLLABORATION & ENQUIRY HUB
# FIRSTCHOICE INFRA PROPERTY HUB
#
# IMPORTANT FLOW:
# PAGE 2 — POST PROPERTY
#       ↓
# PROPERTY LISTING
#       ↓
# BUYER LIKES / SAVES / SHOWS INTEREST
#       ↓
# ENQUIRY GOES TO ORIGINAL PROPERTY POSTER
#       ↓
# POSTER DASHBOARD
#       ↓
# MESSAGE / FOLLOW-UP / SITE VISIT / TASK
# ============================================================

st.set_page_config(
    page_title="Property Collaboration & Enquiry Hub | FirstChoice Property Hub",
    page_icon="💬",
    layout="wide"
)

# ============================================================
# PREMIUM MULTICOLOUR UI
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

.card {
    padding: 28px;
    border-radius: 26px;

    background:
    linear-gradient(
        135deg,
        #FFFFFF,
        #F5F3FF,
        #EFF6FF
    );

    border: 1px solid #E0E7FF;

    box-shadow:
    0 12px 35px
    rgba(0,0,0,0.07);

    margin-bottom: 20px;
}

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

.success-card {
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
    0 18px 55px
    rgba(5,150,105,0.25);
}

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

.warning-card {
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

</style>
""", unsafe_allow_html=True)


# ============================================================
# SESSION STATE
# ============================================================

if "property_messages" not in st.session_state:
    st.session_state.property_messages = []

if "property_tasks" not in st.session_state:
    st.session_state.property_tasks = []

if "property_enquiries" not in st.session_state:
    st.session_state.property_enquiries = []

if "property_followups" not in st.session_state:
    st.session_state.property_followups = []

if "property_likes" not in st.session_state:
    st.session_state.property_likes = []

if "property_saved" not in st.session_state:
    st.session_state.property_saved = []


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<h1>
💬 Property Collaboration & Enquiry Hub
</h1>

<p>
Every property enquiry stays connected to the original
property poster.
</p>

<p>
❤️ Like • ⭐ Save • 👋 Interest • 📞 Enquiry •
📅 Site Visit • 💬 Chat • ✅ Follow-up • 🤝 Collaboration
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# SMART INTRO
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🤖 Smart Property Communication Centre
</h2>

<p>
When a buyer or interested user interacts with a property,
the enquiry is linked to the person who originally posted
that property.
</p>

<p>
This means the original Owner, Agent, Builder or Company
can receive and manage the enquiry directly.
</p>

<p>
<strong>
Property Post → Like / Interest → Enquiry → Original Poster
→ Communication → Follow-up → Site Visit → Deal
</strong>
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROPERTY LISTING CONNECTION
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏡 Property Listing Connection
</h2>

<p>
Select or enter the property whose collaboration workspace
you want to manage.
</p>

</div>
""", unsafe_allow_html=True)


c1, c2 = st.columns(2)


with c1:

    property_name = st.text_input(
        "🏠 Property Name",
        value="My Property"
    )


with c2:

    property_id = st.text_input(
        "🆔 Property ID",
        value="FC-PROPERTY-001"
    )


# ============================================================
# ORIGINAL PROPERTY POSTER
# ============================================================

st.markdown("""
<div class="section">

<h2>
👤 Original Property Poster
</h2>

<p>
Important: All property enquiries should be routed to
the original person who posted this property.
</p>

</div>
""", unsafe_allow_html=True)


p1, p2, p3 = st.columns(3)


with p1:

    poster_name = st.text_input(
        "👤 Property Posted By",
        value=""
    )


with p2:

    poster_role = st.selectbox(
        "👥 Poster Profile Type",
        [
            "Owner",
            "Agent / Broker",
            "Builder / Developer",
            "Company / Organization"
        ]
    )


with p3:

    poster_mobile = st.text_input(
        "📱 Poster Mobile Number",
        max_chars=10
    )


st.markdown(f"""
<div class="poster-card">

<h2>
📌 Enquiry Routing Rule
</h2>

<p>
<strong>Property:</strong> {property_name}
</p>

<p>
<strong>Property ID:</strong> {property_id}
</p>

<p>
<strong>Original Poster:</strong>
{poster_name if poster_name else "Not Connected Yet"}
</p>

<p>
<strong>Role:</strong> {poster_role}
</p>

<p>
<strong>Enquiries will be routed to:</strong>
{poster_mobile if poster_mobile else "Poster mobile not connected"}
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROPERTY INTERACTION
# ============================================================

st.markdown("""
<div class="section">

<h2>
❤️ Property Interest & Enquiry
</h2>

<p>
This section represents the actions a buyer or interested
user can take on the property listing.
</p>

</div>
""", unsafe_allow_html=True)


b1, b2, b3 = st.columns(3)


with b1:

    interested_user = st.text_input(
        "👤 Interested User Name"
    )


with b2:

    interested_mobile = st.text_input(
        "📱 Interested User Mobile",
        max_chars=10
    )


with b3:

    interested_email = st.text_input(
        "✉️ Email"
    )


i1, i2, i3, i4 = st.columns(4)


with i1:

    like_property = st.button(
        "❤️ LIKE PROPERTY",
        use_container_width=True
    )


with i2:

    save_property = st.button(
        "⭐ SAVE PROPERTY",
        use_container_width=True
    )


with i3:

    show_interest = st.button(
        "👋 I'M INTERESTED",
        use_container_width=True
    )


with i4:

    request_call = st.button(
        "📞 REQUEST CALL",
        use_container_width=True
    )


if like_property:

    st.session_state.property_likes.append({

        "Property ID":
        property_id,

        "Property":
        property_name,

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


# ============================================================
# CREATE ENQUIRY
# ============================================================

st.markdown("""
<div class="section">

<h2>
📨 Send Enquiry to Original Property Poster
</h2>

</div>
""", unsafe_allow_html=True)


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
    ]
)


enquiry_message = st.text_area(
    "💬 Enquiry Message",
    placeholder=
    "Write your enquiry about this property..."
)


if show_interest or request_call:

    if show_interest:

        enquiry_type = "I'm Interested"

    elif request_call:

        enquiry_type = "Request Call Back"


if st.button(
    "📨 SEND ENQUIRY TO PROPERTY POSTER",
    use_container_width=True
):

    if not interested_user:

        st.warning(
            "⚠️ Please enter interested user's name."
        )

    elif not interested_mobile:

        st.warning(
            "⚠️ Please enter interested user's mobile number."
        )

    elif not poster_name:

        st.error(
            "❌ Original Property Poster is not connected."
        )

    else:

        new_enquiry = {

            "Property ID":
            property_id,

            "Property":
            property_name,

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
            f"✅ Enquiry sent successfully to "
            f"{poster_name}, the original property poster."
        )

        if poster_mobile:

            st.info(
                f"📱 Enquiry destination: {poster_mobile}"
            )


# ============================================================
# POSTER ENQUIRY DASHBOARD
# ============================================================

st.markdown("""
<div class="section">

<h2>
📥 Property Poster Enquiry Dashboard
</h2>

<p>
Only enquiries connected to the original property poster
should appear here.
</p>

</div>
""", unsafe_allow_html=True)


poster_enquiries = [

    enquiry

    for enquiry
    in st.session_state.property_enquiries

    if enquiry["Property ID"] == property_id

    and enquiry["Poster Name"] == poster_name

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

            key=f"enquiry_status_{index}"

        )


        if st.button(
            "🔄 UPDATE ENQUIRY STATUS",
            key=f"update_enquiry_{index}",
            use_container_width=True
        ):

            for item in st.session_state.property_enquiries:

                if (
                    item["Property ID"]
                    == enquiry["Property ID"]

                    and item["Created"]
                    == enquiry["Created"]
                ):

                    item["Status"] = new_status


            st.success(
                "✅ Enquiry status updated."
            )

else:

    st.info(
        "📭 No enquiries received for this property yet."
    )


# ============================================================
# QUICK CONTACT
# ============================================================

st.markdown("""
<div class="section">

<h2>
📞 Property Contact
</h2>

</div>
""", unsafe_allow_html=True)


q1, q2, q3 = st.columns(3)


with q1:

    contact_name = st.text_input(
        "👤 Contact Person"
    )


with q2:

    contact_role = st.selectbox(
        "💼 Contact Role",
        [
            "Buyer",
            "Seller",
            "Builder",
            "Agent",
            "Executive",
            "Legal Consultant",
            "Loan Consultant"
        ]
    )


with q3:

    contact_mobile = st.text_input(
        "📱 Contact Mobile"
    )


# ============================================================
# MESSAGE CENTRE
# ============================================================

st.markdown("""
<div class="section">

<h2>
💬 Property Message Centre
</h2>

</div>
""", unsafe_allow_html=True)


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
    ]
)


message_text = st.text_area(
    "💬 Write Message",
    placeholder=
    "Type your property-related message..."
)


current_user = st.text_input(
    "👤 Your Name",
    value=interested_user
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
    ]
)


if st.button(
    "📨 SEND PROPERTY MESSAGE",
    use_container_width=True
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

            "Time":
            datetime.now().strftime(
                "%d-%m-%Y %I:%M %p"
            ),

            "From":
            current_user,

            "Role":
            user_role,

            "Message":
            message_text

        })

        st.success(
            "✅ Message added to Property Communication Centre."
        )


# ============================================================
# MESSAGE HISTORY
# ============================================================

property_messages = [

    message

    for message
    in st.session_state.property_messages

    if message["Property ID"] == property_id

]


if property_messages:

    st.markdown("""
    <div class="section">

    <h2>
    🕒 Property Communication History
    </h2>

    </div>
    """, unsafe_allow_html=True)


    st.dataframe(
        property_messages,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "💬 No property communication history yet."
    )


# ============================================================
# TASK MANAGEMENT
# ============================================================

st.markdown("""
<div class="section">

<h2>
✅ Property Transaction Task Board
</h2>

<p>
Create and track important tasks related to this property.
</p>

</div>
""", unsafe_allow_html=True)


t1, t2 = st.columns(2)


with t1:

    task_title = st.text_input(
        "📌 Task Name",
        placeholder=
        "Example: Collect Sale Agreement"
    )


with t2:

    task_owner = st.text_input(
        "👤 Assigned To"
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
        ]
    )


with t4:

    task_status = st.selectbox(
        "📊 Task Status",
        [
            "Pending",
            "In Progress",
            "Completed"
        ]
    )


if st.button(
    "➕ ADD PROPERTY TASK",
    use_container_width=True
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


# ============================================================
# TASK LIST
# ============================================================

property_tasks = [

    task

    for task
    in st.session_state.property_tasks

    if task["Property ID"] == property_id

]


if property_tasks:

    st.dataframe(
        property_tasks,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "📌 No tasks created yet."
    )


# ============================================================
# FOLLOW-UP REMINDER
# ============================================================

st.markdown("""
<div class="section">

<h2>
📅 Follow-Up Reminder
</h2>

</div>
""", unsafe_allow_html=True)


r1, r2 = st.columns(2)


with r1:

    reminder_title = st.text_input(
        "🔔 Reminder Title"
    )


with r2:

    reminder_date = st.date_input(
        "📅 Follow-Up Date"
    )


reminder_notes = st.text_area(
    "📝 Reminder Notes"
)


if st.button(
    "🔔 CREATE FOLLOW-UP REMINDER",
    use_container_width=True
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


# ============================================================
# FOLLOW-UP HISTORY
# ============================================================

property_followups = [

    followup

    for followup
    in st.session_state.property_followups

    if followup["Property ID"] == property_id

]


if property_followups:

    st.dataframe(
        property_followups,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# COLLABORATION MEMBERS
# ============================================================

st.markdown("""
<div class="section">

<h2>
👥 Collaboration Members
</h2>

</div>
""", unsafe_allow_html=True)


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
    ]
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


# ============================================================
# ACTIVITY SUMMARY
# ============================================================

st.markdown("""
<div class="section">

<h2>
📊 Collaboration & Enquiry Activity
</h2>

</div>
""", unsafe_allow_html=True)


property_likes = [

    like

    for like
    in st.session_state.property_likes

    if like["Property ID"] == property_id

]


property_saved = [

    saved

    for saved
    in st.session_state.property_saved

    if saved["Property ID"] == property_id

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
        "📨 Enquiries",
        len(poster_enquiries)
    )


with m4:

    st.metric(
        "💬 Messages",
        len(property_messages)
    )


with m5:

    completed_tasks = len(

        [
            x

            for x
            in property_tasks

            if x["Status"] == "Completed"

        ]

    )

    st.metric(
        "🎯 Completed",
        completed_tasks
    )


with m6:

    st.metric(
        "👥 Members",
        len(members)
    )


# ============================================================
# SMART COLLABORATION FEATURES
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🚀 Smart Property Collaboration Workflow
</h2>

<p>
❤️ User Likes Property
&nbsp; → &nbsp;
⭐ Saves Property
&nbsp; → &nbsp;
👋 Shows Interest
&nbsp; → &nbsp;
📨 Enquiry Created
</p>

<p>
📨 Enquiry is linked to Original Property Poster
&nbsp; → &nbsp;
💬 Communication
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
Future production integration can automatically connect
this workflow with the logged-in user account, property
database, notifications, WhatsApp, email and CRM.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# NOTICE
# ============================================================

st.markdown("""
<div class="success-card">

<h2>
🏠 One Property — One Owner — One Enquiry Destination
</h2>

<p>
The person who originally posts the property remains the
primary enquiry recipient. All buyer interest, enquiries,
communication and follow-ups remain connected to that
property record.
</p>

</div>
""", unsafe_allow_html=True)
