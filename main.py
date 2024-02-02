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
            
            if "Results" in sheet_names:
                # Read only the "Results" sheet
                df = pd.read_excel(xls, sheet_name="Results", header=None)
                
                # Slice the DataFrame to extract desired portion
                sliced_df = df.iloc[12:27, 3:26]  # Rows 13 to 28, Columns 4 to 27
                
                # Display data for the sliced portion of the "Results" sheet
                st.write("Sheet Name: Results (Rows 13-28, Columns 4-27)")
                st.write(sliced_df)
                
            else:
                st.write("Sheet 'Results' not found in the uploaded file.")
            
        except Exception as e:
            st.error("An error occurred: {}".format(e))

if __name__ == "__main__":
    main()
