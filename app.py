import streamlit as st
from agent_with_tools import *

## configure page
st.set_page_config(
    page_title= "News AI Reporter",
    page_icon= "📰",
    layout = 'centered'
)


st.title(" AI NEWS REPORTER ")
st.markdown("Get the latest news with an enthusiastic  Stroytelling twist ")


if 'agent' not in st.session_state:
    st.session_state.agent = create_agent()

query = st.text_area(
    "What news would you like to hear about?",
    placeholder = "ask question",
    height = 100
)

if st.button("🔍 Get News", type="primary"):
    with st.spinner("Our AI reporter is gathering the latest information..."):
        
        try:
            
            ## Get and display the response
            
            response = get_news_repsonse(st.session_state.agent, query)
            st.markdown(response)
            
        except Exception as e:
                st.error(f"An error occurred: {str(e)}")


###### Add sidebar with information ##########
with st.sidebar:
        st.header("About")
        st.markdown("""
        This AI News Reporter uses:
        - Groq's deepseek-r1-distill-llama-70b model
        - DuckDuckGo search integration
        - Real-time news gathering capabilities
        
        Enter any news-related query, and the AI reporter will gather and present 
        the information in an engaging way!
        """)

        st.header("Tips")
        st.markdown("""
        - Be specific in your queries
        - Try asking about recent events
        - Include relevant details like dates or locations
        - Ask for specific aspects of a news story
        """)

