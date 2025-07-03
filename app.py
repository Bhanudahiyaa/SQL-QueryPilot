import streamlit as st
import google.generativeai as genai


genai.configure(api_key="AIzaSyA70viEjmSoRe2XWoAEjsiaI4EbZ003pI0")  


model = genai.GenerativeModel("models/gemini-1.5-flash")

def main():
    st.set_page_config(page_title="SQL QueryPilot", page_icon=":robot_face:")
    st.markdown(
        """
        <div style="text-align: center;">
            <h1>🧠 SQL QueryPilot</h1>
            <h3>I can help you write SQL queries!</h3>
            <p>Type your SQL-related question below and I'll generate a query for you.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    prompt = st.text_area("🔍 Enter your SQL-related question:")
    if st.button("Generate SQL Query") and prompt.strip():
        with st.spinner("Generating query..."):

            template = """
Create a SQL query snippet using the below text:
'''
{text_input}
'''
I just want a SQL Query.
"""
            formatted_template = template.format(text_input=prompt)

            try:
                response = model.generate_content(formatted_template)
                sql_query = response.text.strip()
                sql_query = sql_query.replace("```sql", "").replace("```", "").strip()

                
                st.markdown("---")
                st.subheader("Create a SQL query snippet using the below text:")
                st.code(prompt, language="markdown")
                st.markdown("**I just want a SQL Query.**")
                st.code(sql_query, language="sql")

                expected_output = """
What would be the expected response of this SQL query snippet:
```
{sql_query}
```
Provide sample tabular response with no explanation:
"""
                expected_output_formatted = expected_output.format(sql_query=sql_query)
                eoutput = model.generate_content(expected_output_formatted)
                eoutput = eoutput.text.strip()
                

                explanation = """
Explain the SQL query snippet:
```
{sql_query}
```
provide a detailed explanation of the query, including its purpose, how it works, and any important details.
"""
                explanation_formatted = explanation.format(sql_query=sql_query)
                explanation = model.generate_content(explanation_formatted)
                explanation = explanation.text.strip()
                

                with st.container():
                    st.success("✅ SQL Query generated successfully!")
                    st.code(sql_query, language="sql")

                    st.success("✅ Expected Output of this SQL Query:")
                    st.markdown(eoutput)

                    st.success("✅ Explanation of the SQL Query:")
                    st.markdown(explanation)

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()