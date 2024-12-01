import streamlit as st
import google.generativeai as genai

# Configure the API key securely from Streamlit's secrets
# Make sure to add GOOGLE_API_KEY in secrets.toml (for local) or Streamlit Cloud Secrets
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Streamlit App UI
st.title("Fundraising & Fund Management with AI")
st.write("Use generative AI to optimize your fundraising and fund management processes.")

# Sidebar for selecting which tool to use
tool_selection = st.sidebar.selectbox(
    "Select a tool",
    [
        "Competitive Fund Tracker Bot",
        "LP Sentiment Analysis Bot",
        "Pitch Personalizer Bot",
        "Carry Calculator Bot",
        "Vintage Diversification Optimizer Bot",
    ]
)

# Competitive Fund Tracker Bot
if tool_selection == "Competitive Fund Tracker Bot":
    st.header("Competitive Fund Tracker Bot")
    st.write("Monitor other funds raising capital and benchmark your fund's performance.")
    
    # Input field for fund tracking
    fund_name = st.text_input("Enter your fund name:", "")
    competition_data = st.text_area("Enter competitor data (fund names, capital raised, etc.):", "")
    
    if st.button("Analyze Competition"):
        try:
            # Send data to Gemini to analyze
            prompt = f"Analyze the competitive landscape for {fund_name} compared to the following competitors: {competition_data}. Provide a benchmark of performance."
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(prompt)
            
            # Display response
            st.write("Analysis:")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")

# LP Sentiment Analysis Bot
elif tool_selection == "LP Sentiment Analysis Bot":
    st.header("LP Sentiment Analysis Bot")
    st.write("Analyze LP emails and conversations to detect hesitations or enthusiasm.")
    
    # Input field for LP email/text data
    lp_conversation = st.text_area("Enter LP email or conversation text:", "")
    
    if st.button("Analyze Sentiment"):
        try:
            # Send data to Gemini to analyze sentiment
            prompt = f"Analyze the sentiment of the following LP conversation and detect any signs of hesitation or enthusiasm: {lp_conversation}"
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(prompt)
            
            # Display response
            st.write("Sentiment Analysis:")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")

# Pitch Personalizer Bot
elif tool_selection == "Pitch Personalizer Bot":
    st.header("Pitch Personalizer Bot")
    st.write("Customize fundraising pitches based on LPs' investment history and preferences.")
    
    # Input field for LP preferences
    lp_history = st.text_area("Enter LP's investment history and preferences:", "")
    
    if st.button("Personalize Pitch"):
        try:
            # Send data to Gemini to generate personalized pitch
            prompt = f"Personalize a fundraising pitch for an LP with the following investment history and preferences: {lp_history}. Provide a tailored message."
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(prompt)
            
            # Display response
            st.write("Personalized Pitch:")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")

# Carry Calculator Bot
elif tool_selection == "Carry Calculator Bot":
    st.header("Carry Calculator Bot")
    st.write("Instantly calculate potential carried interest scenarios for various deal structures.")
    
    # Input fields for carry calculation parameters
    deal_structure = st.selectbox("Select deal structure:", ["Traditional", "Hurdle Rate", "European Waterfall", "American Waterfall"])
    total_fund = st.number_input("Enter total fund size ($):", min_value=1_000_000)
    carry_percentage = st.slider("Select carry percentage:", 0, 50, 20)
    
    if st.button("Calculate Carry"):
        try:
            # Send data to Gemini to calculate carry
            prompt = f"Calculate the carried interest for a {deal_structure} deal structure with a total fund size of ${total_fund} and a carry percentage of {carry_percentage}%. Provide a detailed breakdown of the potential carried interest."
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(prompt)
            
            # Display response
            st.write("Carry Interest Calculation:")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")

# Vintage Diversification Optimizer Bot
elif tool_selection == "Vintage Diversification Optimizer Bot":
    st.header("Vintage Diversification Optimizer Bot")
    st.write("Advise on fund allocation to achieve a balanced vintage diversification strategy.")
    
    # Input fields for vintage diversification
    total_allocation = st.number_input("Enter total fund allocation ($):", min_value=1_000_000)
    vintage_years = st.text_area("Enter the vintage years and fund allocation (e.g., 2020: 40%, 2021: 30%, etc.):", "")
    
    if st.button("Optimize Diversification"):
        try:
            # Send data to Gemini to optimize vintage diversification
            prompt = f"Advise on how to optimize vintage diversification for a total fund allocation of ${total_allocation} with the following vintage years and allocations: {vintage_years}. Provide suggestions for better diversification."
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(prompt)
            
            # Display response
            st.write("Vintage Diversification Optimization:")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")

