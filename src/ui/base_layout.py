import streamlit as st


def style_background_home():
    st.markdown("""
        <style>
            .stApp {
                background: #5865F2 !important;
            }

            /* Home page cards */
            .stApp div[data-testid="stColumn"] {
                background-color: #FFFFFF !important;
                padding: 2.5rem !important;
                border-radius: 5rem !important;
                box-shadow: 0 10px 30px rgba(0,0,0,0.08) !important;
            }

            /* Headings inside home cards must be dark */
            .stApp div[data-testid="stColumn"] h1,
            .stApp div[data-testid="stColumn"] h2,
            .stApp div[data-testid="stColumn"] h3,
            .stApp div[data-testid="stColumn"] h4,
            .stApp div[data-testid="stColumn"] p,
            .stApp div[data-testid="stColumn"] span,
            .stApp div[data-testid="stColumn"] label {
                color: #1F2235 !important;
                -webkit-text-fill-color: #1F2235 !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp {
                background: #E0E3FF !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

        /* ── Hide Streamlit chrome ── */
        #MainMenu, footer, header {
            visibility: hidden;
        }

        .block-container {
            padding-top: 1.5rem !important;
        }

        /* ── Typography ── */
        h1 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 3.5rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0rem !important;
            color: #1F2235 !important;
            -webkit-text-fill-color: #1F2235 !important;
        }

        h2 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 2rem !important;
            line-height: 0.9 !important;
            margin-bottom: 0rem !important;
            color: #1F2235 !important;
            -webkit-text-fill-color: #1F2235 !important;
        }

        h3, h4 {
            font-family: 'Outfit', sans-serif !important;
            color: #1F2235 !important;
            -webkit-text-fill-color: #1F2235 !important;
        }

        /* ── All body text / labels / paragraphs ── */
        p, li, span:not([data-testid]),
        .stMarkdown p,
        [data-testid="stMarkdownContainer"] p {
            font-family: 'Outfit', sans-serif !important;
            color: #4B5563 !important;
            -webkit-text-fill-color: #4B5563 !important;
        }

        /* ── Form labels — bold, dark ── */
        label,
        .stTextInput > label,
        .stTextArea > label,
        .stSelectbox > label,
        .stNumberInput > label,
        .stCameraInput > label,
        .stAudioInput > label,
        [data-testid="stWidgetLabel"] p,
        [data-testid="stWidgetLabel"] label,
        [data-testid="stWidgetLabel"] span {
            font-family: 'Outfit', sans-serif !important;
            font-weight: 600 !important;
            font-size: 0.95rem !important;
            color: #1F2235 !important;
            -webkit-text-fill-color: #1F2235 !important;
            opacity: 1 !important;
        }

        /* ── Input fields ── */
        .stTextInput input,
        .stTextArea textarea,
        .stNumberInput input,
        div[data-baseweb="input"] input,
        div[data-baseweb="textarea"] textarea {
            background-color: #FFFFFF !important;
            color: #111827 !important;
            -webkit-text-fill-color: #111827 !important;
            border: 1px solid #D1D5DB !important;
            border-radius: 12px !important;
            height: 52px !important;
            font-family: 'Outfit', sans-serif !important;
            font-size: 1rem !important;
            padding: 0 16px !important;
        }

        .stTextArea textarea {
            height: auto !important;
            padding: 12px 16px !important;
        }

        /* Focus state */
        .stTextInput input:focus,
        .stTextArea textarea:focus,
        div[data-baseweb="input"] input:focus {
            border-color: #5965F2 !important;
            box-shadow: 0 0 0 4px rgba(89,101,242,0.15) !important;
            outline: none !important;
        }

        /* ── Placeholder text ── */
        .stTextInput input::placeholder,
        .stTextArea textarea::placeholder,
        div[data-baseweb="input"] input::placeholder {
            color: #6B7280 !important;
            -webkit-text-fill-color: #6B7280 !important;
            opacity: 1 !important;
        }

        /* ── Selectbox ── */
        div[data-baseweb="select"] > div {
            background-color: #FFFFFF !important;
            border: 1px solid #D1D5DB !important;
            border-radius: 12px !important;
            min-height: 52px !important;
        }

        div[data-baseweb="select"] span,
        div[data-baseweb="select"] div {
            color: #111827 !important;
            -webkit-text-fill-color: #111827 !important;
            font-family: 'Outfit', sans-serif !important;
        }

        /* ── Buttons — primary ── */
        button {
            font-family: 'Outfit', sans-serif !important;
            font-weight: 600 !important;
            border-radius: 1.5rem !important;
            background-color: #5865F2 !important;
            color: #FFFFFF !important;
            -webkit-text-fill-color: #FFFFFF !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.2s ease, box-shadow 0.2s ease !important;
        }

        button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 20px rgba(89,101,242,0.3) !important;
        }

        /* ── Buttons — secondary (pink) ── */
        button[kind="secondary"] {
            background-color: #EB459E !important;
            color: #FFFFFF !important;
            -webkit-text-fill-color: #FFFFFF !important;
        }

        button[kind="secondary"]:hover {
            box-shadow: 0 8px 20px rgba(235,69,158,0.3) !important;
        }

        /* ── Buttons — tertiary (dark) ── */
        button[kind="tertiary"] {
            background-color: #1F2235 !important;
            color: #FFFFFF !important;
            -webkit-text-fill-color: #FFFFFF !important;
        }

        /* ── Divider ── */
        hr {
            border-color: #D1D5DB !important;
        }

        /* ── Alerts / info / warning / error boxes ── */
        [data-testid="stAlert"] p,
        [data-testid="stAlert"] span {
            color: #1F2235 !important;
            -webkit-text-fill-color: #1F2235 !important;
            opacity: 1 !important;
        }

        /* ── Spinner text ── */
        [data-testid="stSpinner"] p {
            color: #1F2235 !important;
            -webkit-text-fill-color: #1F2235 !important;
        }

        /* ── Subheader / st.subheader ── */
        [data-testid="stHeadingWithActionElements"] h3,
        [data-testid="stHeadingWithActionElements"] h2,
        [data-testid="stHeadingWithActionElements"] h1 {
            color: #1F2235 !important;
            -webkit-text-fill-color: #1F2235 !important;
        }

        /* ── Dataframe / table text ── */
        .stDataFrame td, .stDataFrame th {
            color: #1F2235 !important;
        }

        /* ── Toast / notification ── */
        [data-testid="stToast"] p {
            color: #1F2235 !important;
            -webkit-text-fill-color: #1F2235 !important;
        }

        /* ── Camera input label ── */
        [data-testid="stCameraInput"] span {
            color: #1F2235 !important;
            -webkit-text-fill-color: #1F2235 !important;
        }

        /* ── Container / card borders ── */
        [data-testid="stVerticalBlockBorderWrapper"] {
            background-color: #FFFFFF !important;
            border-radius: 24px !important;
            box-shadow: 0 10px 30px rgba(0,0,0,0.08) !important;
            border: 1px solid #E5E7EB !important;
        }

        </style>
    """, unsafe_allow_html=True)
