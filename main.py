import streamlit as st
import pandas as pd

def main():
    st.title("Excel Sheet Analysis")
    
    # File upload
    uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx", "xls"])
    
    if uploaded_file is not None:
        try:
            # Read Excel file
            xls = pd.ExcelFile(uploaded_file)
            sheet_names = xls.sheet_names
            selected_sheet = st.selectbox("Select a sheet", sheet_names)
            df = pd.read_excel(xls, sheet_name=selected_sheet)
            
            # Display uploaded data
            st.write("Uploaded Data (Sheet: {})".format(selected_sheet))
            st.write(df)
            
            # Perform analysis
            st.write("Data Analysis:")
            st.write("Summary Statistics:")
            st.write(df.describe())
            
            # You can perform more analysis here
            
        except Exception as e:
            st.error("An error occurred: {}".format(e))

if __name__ == "__main__":
    main()
