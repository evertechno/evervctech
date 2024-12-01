import streamlit as st
import google.generativeai as genai
import random
import time

# Configure the API key securely from Streamlit's secrets
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Streamlit App UI
st.title("AI Sales Competitor Simulation")
st.write("""
    This advanced simulation allows you to train by interacting with AI-driven competitors in different sales scenarios.
    Choose a sales scenario, customize your competitor's profile, and simulate a conversation for better sales training.
""")

# Scenario Selection
scenario = st.selectbox(
    "Select a Sales Scenario:",
    ["Negotiating Price", "Handling Objections", "Product Pitch", "Closing a Deal", "Upselling", "Cross-selling", "Discount Negotiation", "Consultative Selling"]
)

# Competitor Profile Customization
competitor_style = st.selectbox(
    "Select Competitor Style:",
    ["Aggressive", "Passive", "Price-sensitive", "Value-driven", "Relationship-focused", "Hard-nosed", "Emotional", "Data-driven"]
)

# Additional Competitor Customization
competitor_tone = st.selectbox(
    "Select Competitor Tone:",
    ["Friendly", "Formal", "Assertive", "Sarcastic", "Nervous", "Optimistic", "Defensive", "Neutral"]
)

competitor_expertise = st.slider(
    "Competitor Expertise Level (1-10):",
    1, 10, 5
)

# Additional Interaction Customization
sales_experience = st.slider(
    "Your Sales Experience (1-10):",
    1, 10, 5
)

emotion_detection = st.checkbox("Enable Emotion Detection for Competitor Responses")

# Prompt input field for additional context or specifics
additional_context = st.text_input("Additional Context (optional):", "")

# Button to generate response
if st.button("Simulate Competitor Response"):
    try:
        # Prepare the prompt based on scenario and competitor style
        prompt = f"""
        Sales Scenario: {scenario}
        Competitor Style: {competitor_style}
        Competitor Tone: {competitor_tone}
        Competitor Expertise: {competitor_expertise}
        Your Sales Experience Level: {sales_experience}
        """
        if additional_context:
            prompt += f"Additional Context: {additional_context}\n"
        if emotion_detection:
            prompt += "Enable emotion detection for a more personalized and reactive response."

        # Load and configure the Gemini model
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Generate multiple responses to show variability
        responses = []
        for _ in range(3):  # Generate 3 different responses
            response = model.generate_content(prompt)
            responses.append(response.text)
        
        # Randomly select a response to simulate variability in the competitor's approach
        selected_response = random.choice(responses)
        
        # Display the competitor's response
        st.write("Competitor's Response:")
        st.write(selected_response)
        
        # Sales Tips and Analysis
        st.write("\n### Sales Tips for this Scenario:")
        if "discount" in selected_response.lower():
            st.write("- Consider offering value before discussing discounts.")
            st.write("- Be careful with deep discounts; make sure to justify the value you're providing.")
        elif "objection" in selected_response.lower():
            st.write("- Address objections empathetically, and always steer the conversation back to value.")
            st.write("- Validate the customer's concern and offer a solution.")
        elif "price" in selected_response.lower():
            st.write("- Always highlight the benefits and value of your product before diving into price negotiations.")
            st.write("- Keep the conversation focused on how your solution can meet the customer's needs.")
        elif "upsell" in selected_response.lower():
            st.write("- Highlight additional features or packages that could benefit the customer.")
            st.write("- Emphasize how an upgrade can provide long-term value and satisfaction.")
        else:
            st.write("- Always personalize your pitch based on the customer’s needs and preferences.")
        
        # Scenario progression: introduce progressive difficulty
        difficulty_level = st.selectbox("Set Difficulty Level", ["Easy", "Medium", "Hard", "Expert"])
        if difficulty_level == "Medium":
            st.write("Competitor is slightly tougher now. Prepare for more complex objections.")
        elif difficulty_level == "Hard":
            st.write("Competitor is very tough now. Expect complex negotiations and hardball tactics.")
        elif difficulty_level == "Expert":
            st.write("You're facing an expert competitor. Prepare for intense negotiation and persuasion techniques.")

        # Continue the conversation: simulate another round of dialogue
        follow_up = st.text_input("Your Response to Competitor (optional):")
        if follow_up:
            follow_up_prompt = f"Customer's Response: {follow_up}\nCompetitor Style: {competitor_style}\nSales Scenario: {scenario}\n"
            follow_up_response = model.generate_content(follow_up_prompt)
            st.write("Competitor's Follow-Up Response:")
            st.write(follow_up_response.text)

        # Performance analytics (example: tracking responses and difficulty)
        st.write(f"\n### Performance Analytics:")
        st.write(f"Scenario: {scenario}")
        st.write(f"Competitor Style: {competitor_style}, Tone: {competitor_tone}, Expertise: {competitor_expertise}")
        st.write(f"Difficulty Level: {difficulty_level}")
        st.write(f"Your Sales Experience: {sales_experience}")

        # Suggesting Sales Resources (based on scenario)
        if "objection" in scenario.lower():
            st.write("You might find these resources helpful:")
            st.write("- [Handling Objections: A Guide](https://www.salestraining.com/objections-guide)")
            st.write("- [Effective Negotiation Techniques](https://www.salesnegotiation.com/techniques)")
        elif "upselling" in scenario.lower():
            st.write("Check out these resources to improve your upselling skills:")
            st.write("- [How to Master Upselling](https://www.salestraining.com/upselling-guide)")
        elif "cross-selling" in scenario.lower():
            st.write("- [Cross-Selling Strategies](https://www.salestraining.com/cross-selling-strategies)")

        # Time-Based Performance Tracking
        start_time = time.time()
        st.write("Start negotiating and responding.")
        end_time = time.time()
        time_spent = round(end_time - start_time, 2)
        st.write(f"Time spent on this scenario: {time_spent} seconds")

        # Emotional Intelligence Tracking
        if emotion_detection:
            st.write("Emotion detection activated. Analyzing competitor's emotional tone...")
            if "angry" in selected_response.lower():
                st.write("- Competitor seems frustrated. Stay calm and show empathy.")
            elif "sarcastic" in selected_response.lower():
                st.write("- Competitor might be challenging your approach. Stay positive and assertive.")
            else:
                st.write("- Competitor seems neutral. Proceed with your strategy.")

        # Adaptive Scenario Path (dependent on prior responses)
        scenario_path = st.selectbox("Do you want to continue with the same scenario or switch?", ["Continue", "Switch Scenario"])
        if scenario_path == "Switch Scenario":
            st.write("Switching scenario... Choose another scenario to continue training.")
        elif scenario_path == "Continue":
            st.write("Continuing the current scenario... Keep practicing!")
        
        # Customer Insights (simulating customer persona)
        customer_persona = random.choice(["Price-sensitive", "Value-driven", "Brand-loyal", "Innovative", "Skeptical"])
        st.write(f"\n### Customer Persona:")
        st.write(f"Customer Persona: {customer_persona}")
        st.write("- Tailor your responses based on the customer's persona for better engagement.")

        # Strategy Recommendations (based on user responses)
        if "discount" in selected_response.lower():
            st.write("It seems your competitor is trying to push a discount. Instead of conceding to price, focus on the long-term value.")
        elif "objection" in selected_response.lower():
            st.write("You're handling objections well. Keep addressing their concerns and redirecting them back to the value your product provides.")
        else:
            st.write("Good pitch! Stay focused on how your product solves the customer's problems, and be ready for follow-up questions.")

        # Emotional Feedback for User's Response
        user_emotion = st.radio("How do you feel about your response?", ["Confident", "Uncertain", "Defensive", "Optimistic", "Frustrated"])
        st.write(f"Your emotional feedback: {user_emotion}")
        if user_emotion == "Frustrated":
            st.write("Take a deep breath. Focus on the benefits of your product and how it can resolve their pain points.")
        
        # Long-Term Strategy Feedback
        st.write("\n### Long-Term Strategy Feedback:")
        st.write("- Keep practicing objection handling techniques and pushing for value-based conversations.")
        st.write("- If you’re dealing with aggressive competitors, focus on staying calm and using facts to support your arguments.")
    
    except Exception as e:
        st.error(f"Error: {e}")
