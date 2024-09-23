import streamlit as st


# Title of the app
st.title("Review of past interventions")

# Dropdown menu for data management options
data_option = st.sidebar.selectbox(
    "Choose a epidemiological stratification option:",
    (
        'None',
        'EPI Coverage and Dropout Rate',
        'IPTp and ANC Coverage',
        'PMC (Prevention of Malaria in Pregnancy)',
        'SC (Seasonal Malaria Chemoprevention)',
        'Malaria Vaccine',
        'ITN Ownership, Access, Usage and Type',
        'IRS (Indoor Residual Spray)',
        'LSM (Larval Source Management)',
        'Assessing the Quality of Case Management'
        
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

explanation_python_shapefiles = """

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
if data_option == 'EPI Coverage and Dropout Rate':
    st.subheader("EPI Coverage and Dropout Rate")
    
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

elif data_option == 'IPTp and ANC Coverage':
    st.subheader("IPTp and ANC Coverage")
    
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

elif data_option == 'PMC (Prevention of Malaria in Pregnancy)':
    st.subheader("PMC (Prevention of Malaria in Pregnancy")
    
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


elif data_option == 'SC (Seasonal Malaria Chemoprevention)':
    st.subheader("SC (Seasonal Malaria Chemoprevention)")
    
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

elif data_option == 'Malaria Vacinne':
    st.subheader("Malaria Vacinne")
    
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

elif data_option == 'ITN Ownership, Access, Usage and Type':
    st.subheader("ITN Ownership, Access, Usage and Type")
    
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



elif data_option == 'IRS (Indoor Residual Spray)':
    st.subheader("IRS (Indoor Residual Spray)")
    
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



elif data_option == 'LSM (Larval Source Management)':
    st.subheader("LSM (Larval Source Management)")
    
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



elif data_option == 'Assessing the Quality of Case Management':
    st.subheader("Assessing the Quality of Case Management")
    
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
