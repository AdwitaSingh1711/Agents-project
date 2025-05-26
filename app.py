import streamlit as st
from agents import Agent_Manager
from utils.logger import logger
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    st.set_page_config(
        page_title="Multi-Agent AI system", layout = "wide"
    )

    st.title("Multi Agent AI system with Validation and Collaboration")

    st.sidebar.title("Select Task")

    task = st.sidebar.selectbox(
        "Choose a Task: ",[
            "Summarise Medical Text",
            "Write and Refine Article",
            "Sanitise Medical Data (PHI)"
        ]
    )

    agent_manager = Agent_Manager(max_retries=2, verbose=True)

    if task=="Summarise Medical Text":
        summarise_section(agent_manager)
    

    elif task=="Write and Refine Article":
        write_and_refine_article_section(agent_manager)

    elif task=="Sanitise Medical Data (PHI)":
        sanitize_data_section(agent_manager)

def summarise_section(agent_manager):
    st.header("Summarise Medical Text")

    text = st.text_area("Enter medical text to summarise:", height = 200)
    if st.button("Summarise"):
        if text:
            main_agent = agent_manager.get_agent("summarise")
            validator_agent = agent_manager.get_agent("summarise_validator")

            with st.spinner("Summarising..."):
                try:
                    summary = main_agent.execute(text)
                    st.subheader("Summary:")
                    st.write(summary)
                except Exception as e:
                    st.error(f"Error:{e}")
                    logger.error(f"Summarisation Agent Error: {e}")
                    return 
                    
            with st.spinner("Validating Summary..."):
                try:
                    validation = validator_agent.execute(original_text= text, summary = summary)
                    st.subheader("Validation:")
                    st.write(validation)
                except Exception as e:
                    st.error(f"Error: {e}")
                    logger.error(f"Summary Validation Error: {e}")
                        
            
        else:
            st.warning("Please enter some text to summarise.")
    
def write_and_refine_article_section(agent_manager):
    st.header("Write and Refine Research Article")
    topic = st.text_input("Enter the topic for the research article:")
    outline = st.text_area("Enter an outline (optional):", height=150)
    if st.button("Write and Refine Article"):
        if topic:
            writer_agent = agent_manager.get_agent("write_Article")
            refiner_agent = agent_manager.get_agent("refiner")
            validator_agent = agent_manager.get_agent("validator")
            with st.spinner("Writing article..."):
                try:
                    draft = writer_agent.execute(topic, outline)
                    st.subheader("Draft Article:")
                    st.write(draft)
                except Exception as e:
                    st.error(f"Error: {e}")
                    logger.error(f"WriteArticleAgent Error: {e}")
                    return

            with st.spinner("Refining article..."):
                try:
                    refined_article = refiner_agent.execute(draft)
                    st.subheader("Refined Article:")
                    st.write(refined_article)
                except Exception as e:
                    st.error(f"Refinement Error: {e}")
                    logger.error(f"RefinerAgent Error: {e}")
                    return

            with st.spinner("Validating article..."):
                try:
                    validation = validator_agent.execute(topic=topic, article=refined_article)
                    st.subheader("Validation:")
                    st.write(validation)
                except Exception as e:
                    st.error(f"Validation Error: {e}")
                    logger.error(f"ValidatorAgent Error: {e}")
        else:
            st.warning("Please enter a topic for the research article.")
    

def sanitize_data_section(agent_manager):
    st.header("Sanitize Medical Data (PHI)")
    medical_data = st.text_area("Enter medical data to sanitize:", height=200)
    if st.button("Sanitize Data"):
        if medical_data:
            main_agent = agent_manager.get_agent("sanitise_Data")
            validator_agent = agent_manager.get_agent("sanitise_data_validator")
            with st.spinner("Sanitizing data..."):
                try:
                    sanitized_data = main_agent.execute(medical_data)
                    st.subheader("Sanitized Data:")
                    st.write(sanitized_data)
                except Exception as e:
                    st.error(f"Error: {e}")
                    logger.error(f"SanitizeDataAgent Error: {e}")
                    return

            with st.spinner("Validating sanitized data..."):
                try:
                    validation = validator_agent.execute(original_data=medical_data, sanitized_data=sanitized_data)
                    st.subheader("Validation:")
                    st.write(validation)
                except Exception as e:
                    st.error(f"Validation Error: {e}")
                    logger.error(f"SanitizeDataValidatorAgent Error: {e}")
        else:
            st.warning("Please enter medical data to sanitize.")

if __name__ == "__main__":
    main()
