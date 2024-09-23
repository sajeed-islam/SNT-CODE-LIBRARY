import streamlit as st


# Title of the app
st.title("Epidemiological Stratification")

# Dropdown menu for data management options
data_option = st.sidebar.selectbox(
    "Choose a epidemiological stratification option:",
    (
        'None',
        'Reporting Rate per Variable',
        'Group and Merge data frame',
        'Crude Incidence by Year',
        'Testing Positivity Rate',
        'Adjusted Incidence by Year',
        'Option to select Incidence',
        'Risk Categorization'
        
    )
)

# Dropdown menu for content options
content_option = st.selectbox(
    "Choose what to view:",
    (
        'None',
        'See R Code',
        'Explanation of R Code',
        'See Python Code',
        'Explanation of Python Code',
        'Sample Output'
    )
)

# Sample R and Python code and images for different options
r_code_shapefiles = """
#START









# PLACE HOLDER CODE BLOCK FOR REPORTING RATE PER VARIABLES GOES HERE












# END

"""

python_code_shapefiles = """
#START









# PLACE HOLDER CODE BLOCK FOR REPORTING RATE PER VARIABLES GOES HERE












# END
"""

r_code_health_facilities = """
#START









# PLACE HOLDER CODE BLOCK FOR REPORTING RATE PER VARIABLES GOES HERE












# END
"""

python_code_health_facilities = """
#START









# PLACE HOLDER CODE BLOCK FOR REPORTING RATE PER VARIABLES GOES HERE












# END
"""

# Explanations
explanation_r_shapefiles = """

# START
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
# END
"""

explanation_r_health_facilities = """
# START
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
# END
"""

explanation_python_health_facilities = """
# START
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
# END
"""

# Sample images for different options
sample_output_shapefiles_r = "https://github.com/mohamedsillahkanu/si/blob/99ccc5bd8425859a0a801f01ca713e36edbd0c21/MAP_R.png?raw=true"
sample_output_shapefiles_python = "https://github.com/mohamedsillahkanu/si/blob/d3705941c975aeab86e701d0d2093b38052a50e2/MAP_PYTHON.png?raw=true"

sample_output_health_facilities_r = "https://github.com/mohamedsillahkanu/si/blob/d3705941c975aeab86e701d0d2093b38052a50e2/MAP_PYTHON.png?raw=true"  # Replace with actual image URL
sample_output_health_facilities_python = "https://github.com/mohamedsillahkanu/si/blob/d3705941c975aeab86e701d0d2093b38052a50e2/MAP_PYTHON.png?raw=true" 

sample_output_routine_case_data_dhis2_r = "https://github.com/mohamedsillahkanu/si/blob/d3705941c975aeab86e701d0d2093b38052a50e2/MAP_PYTHON.png?raw=true" # Replace with actual image URL
sample_output_routine_case_data_dhis2_python = "https://example.com/dhis2_image.png"  # Replace with actual image URL

sample_output_DHS_Data_r = "https://github.com/mohamedsillahkanu/si/blob/d3705941c975aeab86e701d0d2093b38052a50e2/MAP_PYTHON.png?raw=true"  # Replace with actual image URL
sample_output_DHS_Data_python = "https://github.com/mohamedsillahkanu/si/blob/d3705941c975aeab86e701d0d2093b38052a50e2/MAP_PYTHON.png?raw=true"  # Replace with actual image URL

sample_output_Climate_Data_r = "https://github.com/mohamedsillahkanu/si/blob/d3705941c975aeab86e701d0d2093b38052a50e2/MAP_PYTHON.png?raw=true"  # Replace with actual image URL
sample_output_Climate_Data_python = "https://github.com/mohamedsillahkanu/si/blob/d3705941c975aeab86e701d0d2093b38052a50e2/MAP_PYTHON.png?raw=true"  # Replace with actual image URL


sample_output_LMIS_Data_r = "https://github.com/mohamedsillahkanu/si/blob/d3705941c975aeab86e701d0d2093b38052a50e2/MAP_PYTHON.png?raw=true"  # Replace with actual image URL
sample_output_LMIS_Data_python = "https://github.com/mohamedsillahkanu/si/blob/d3705941c975aeab86e701d0d2093b38052a50e2/MAP_PYTHON.png?raw=true"  # Replace with actual image URL

sample_output_Modeled_Data_r = "https://github.com/mohamedsillahkanu/si/blob/d3705941c975aeab86e701d0d2093b38052a50e2/MAP_PYTHON.png?raw=true"  # Replace with actual image URL
sample_output_Modeled_Data_python = "https://github.com/mohamedsillahkanu/si/blob/d3705941c975aeab86e701d0d2093b38052a50e2/MAP_PYTHON.png?raw=true"  # Replace with actual image URL

sample_output_Population_Data_r = "https://github.com/mohamedsillahkanu/si/blob/d3705941c975aeab86e701d0d2093b38052a50e2/MAP_PYTHON.png?raw=true"  # Replace with actual image URL
sample_output_Population_Data = "https://github.com/mohamedsillahkanu/si/blob/d3705941c975aeab86e701d0d2093b38052a50e2/MAP_PYTHON.png?raw=true"  # Replace with actual image URL

# Display content based on selected options
if data_option == 'Reporting Rate per Variable':
    st.subheader("Reporting Rate per Variable")
    
    if content_option == 'See R Code':
        st.code(r_code_shapefiles, language='r')
    elif content_option == 'See Python Code':
        st.code(python_code_shapefiles, language='python')
    elif content_option == 'Explanation of R Code':
        st.write(explanation_r_shapefiles)
    elif content_option == 'Explanation of Python Code':
        st.write(explanation_python_shapefiles)
    elif content_option == 'Sample Output':
        st.image(sample_output_shapefiles_r, caption="Sample output of the Shapefiles R code")
        st.image(sample_output_shapefiles_python, caption="Sample output of the Shapefiles Python code")

elif data_option == 'Group and Merge data frame':
    st.subheader("Group and Merge data frame")
    
    if content_option == 'See R Code':
        st.code(r_code_health_facilities, language='r')
    elif content_option == 'See Python Code':
        st.code(python_code_health_facilities, language='python')
    elif content_option == 'Explanation of R Code':
        st.write(explanation_r_health_facilities)
    elif content_option == 'Explanation of Python Code':
        st.write(explanation_python_health_facilities)
    elif content_option == 'Sample Output':
        st.image(sample_output_health_facilities_r, caption="Sample output of the Health Facilities R code")
        st.image(sample_output_health_facilities_python, caption="Sample output of the Health Facilities Python code")

elif data_option == 'Crude Incidence by Year':
    st.subheader("Crude Incidence by Year ")
    
    if content_option == 'See R Code':
        st.code(r_code_health_facilities, language='r')
    elif content_option == 'See Python Code':
        st.code(python_code_health_facilities, language='python')
    elif content_option == 'Explanation of R Code':
        st.write(explanation_r_health_facilities)
    elif content_option == 'Explanation of Python Code':
        st.write(explanation_python_health_facilities)
    elif content_option == 'Sample Output':
        st.image(sample_output_health_facilities_r, caption="Sample output of the Health Facilities R code")
        st.image(sample_output_health_facilities_python, caption="Sample output of the Health Facilities Python code")


elif data_option == 'Adjusted Incidence by Year':
    st.subheader("Adjusted Incidence by Year")
    
    if content_option == 'See R Code':
        st.code(r_code_health_facilities, language='r')
    elif content_option == 'See Python Code':
        st.code(python_code_health_facilities, language='python')
    elif content_option == 'Explanation of R Code':
        st.write(explanation_r_health_facilities)
    elif content_option == 'Explanation of Python Code':
        st.write(explanation_python_health_facilities)
    elif content_option == 'Sample Output':
        st.image(sample_output_health_facilities_r, caption="Sample output of the Health Facilities R code")
        st.image(sample_output_health_facilities_python, caption="Sample output of the Health Facilities Python code")

elif data_option == 'Option to Select Incidence':
    st.subheader("Option to Select Incidence")
    
    if content_option == 'See R Code':
        st.code(r_code_health_facilities, language='r')
    elif content_option == 'See Python Code':
        st.code(python_code_health_facilities, language='python')
    elif content_option == 'Explanation of R Code':
        st.write(explanation_r_health_facilities)
    elif content_option == 'Explanation of Python Code':
        st.write(explanation_python_health_facilities)
    elif content_option == 'Sample Output':
        st.image(sample_output_health_facilities_r, caption="Sample output of the Health Facilities R code")
        st.image(sample_output_health_facilities_python, caption="Sample output of the Health Facilities Python code")

elif data_option == 'Risk Categorization':
    st.subheader("Risk Categorization")
    
    if content_option == 'See R Code':
        st.code(r_code_health_facilities, language='r')
    elif content_option == 'See Python Code':
        st.code(python_code_health_facilities, language='python')
    elif content_option == 'Explanation of R Code':
        st.write(explanation_r_health_facilities)
    elif content_option == 'Explanation of Python Code':
        st.write(explanation_python_health_facilities)
    elif content_option == 'Sample Output':
        st.image(sample_output_health_facilities_r, caption="Sample output of the Health Facilities R code")
        st.image(sample_output_health_facilities_python, caption="Sample output of the Health Facilities Python code")



elif data_option == 'Testing Positivity Rate':
    st.subheader("Modeled Data Content")
    
    if content_option == 'See R Code':
        st.code(r_code_health_facilities, language='r')
    elif content_option == 'See Python Code':
        st.code(python_code_health_facilities, language='python')
    elif content_option == 'Explanation of R Code':
        st.write(explanation_r_health_facilities)
    elif content_option == 'Explanation of Python Code':
        st.write(explanation_python_health_facilities)
    elif content_option == 'Sample Output':
        st.image(sample_output_health_facilities_r, caption="Sample output of the Health Facilities R code")
        st.image(sample_output_health_facilities_python, caption="Sample output of the Health Facilities Python code")

# Add similar conditions for other data options if needed
