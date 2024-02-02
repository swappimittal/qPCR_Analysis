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
            
            if "Results by Well" in sheet_names:
                # Read only the "Results by Well" sheet
                df = pd.read_excel(xls, sheet_name="Results by Well", header=None)
                
                # Display data for the "Results by Well" sheet
                st.write("Sheet Name: Results by Well")
                st.write(df)
                
            else:
                st.write("Sheet 'Results By Well' not found in the uploaded file.")
            
        except Exception as e:
            st.error("An error occurred: {}".format(e))

if __name__ == "__main__":
    main()
