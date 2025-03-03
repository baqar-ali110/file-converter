import streamlit as st  
import pandas as pd
import os
from io import BytesIO

# 🎯 Streamlit title
st.title("📂 File Converter Web App")

# 🎯to upload file
uploaded_file = st.file_uploader("Upload a file", type=["csv", "xlsx", "txt"])

# 🎯 Agar file upload hui hai to usko read karna
if uploaded_file is not None:
    file_name = uploaded_file.name

    # 🎯 File type detect karna
    if file_name.endswith(".csv"):
        df = pd.read_csv(uploaded_file) 
    elif file_name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)
    elif file_name.endswith(".txt"):
        df = pd.read_csv(uploaded_file, delimiter="\t") 
    else:
        st.error("⚠️ Unsupported file format")
        st.stop()

    # 🎯 To Show The Preview 
    st.write("📌 **File Preview:**")
    st.dataframe(df.head())

    # 🎯 Format Selection 
    format_option = st.selectbox("Select output format:", ["CSV", "Excel","Word"])

    # 🎯 convert file and download 
    if st.button("Convert and Download"):
        output_buffer = BytesIO()

        if format_option == "CSV":
            df.to_csv(output_buffer, index=False)
            file_ext = "csv"
        elif format_option == "Excel":
            df.to_excel(output_buffer, index=False, engine="xlsxwriter")
            file_ext = "xlsx"

        output_buffer.seek(0)  
        st.download_button(
            label=f"📥 Download {file_ext.upper()} File",
            data=output_buffer,
            file_name=f"converted_file.{file_ext}",
            mime=f"text/{file_ext}" if file_ext == "csv" else "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )


