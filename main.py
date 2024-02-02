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
            
            # Iterate over each sheet
            for sheet_name in sheet_names:
                df = pd.read_excel(xls, sheet_name=sheet_name)
                
                # Display data for each sheet
                st.write("Sheet Name: {}".format(sheet_name))
                st.write(df)
                st.write("---")
            
        except Exception as e:
            st.error("An error occurred: {}".format(e))

if __name__ == "__main__":
    main()
