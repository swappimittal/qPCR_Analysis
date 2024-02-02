import streamlit as st
import pandas as pd

def find_string_in_sheet(sheet, target_string):
    """
    Finds the cell numbers containing the target string in a sheet.

    Args:
        sheet (DataFrame): The DataFrame representing the Excel sheet.
        target_string (str): The string to search for in the cells.

    Returns:
        List of tuples: Each tuple contains the row number and column number of a cell
        where the target string is found.
    """
    cell_numbers = []
    for i, row in enumerate(sheet.values):
        for j, cell in enumerate(row):
            if isinstance(cell, str) and target_string in cell:
                cell_numbers.append((i + 1, j + 1))  # Adding 1 to row and column indices to match Excel convention
    return cell_numbers

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
                
                # Find "<>" in each sheet
                cell_numbers = find_string_in_sheet(df, "<>")
                
                # Display data and cell numbers for each sheet
                st.write("Sheet Name: {}".format(sheet_name))
                st.write(df)
                if cell_numbers:
                    st.write("Cell numbers with '<>':")
                    for row, col in cell_numbers:
                        st.write("Row: {}, Column: {}".format(row, col))
                else:
                    st.write("No '<>' found in this sheet")
                st.write("---")
            
        except Exception as e:
            st.error("An error occurred: {}".format(e))

if __name__ == "__main__":
    main()
