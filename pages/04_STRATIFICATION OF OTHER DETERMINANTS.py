import streamlit as st


# Title of the app
st.title("Stratification of other determinants")

# Dropdown menu for data management options
data_option = st.sidebar.selectbox(
    "Choose a Stratification of other determinants option:",
    (
        'None',
        'Access to Care',
        'Seasonality',
        'Insecticide Resistance',
        'Anti-Malaria Drug Resistance'
        
        
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
sample_output_shapefiles_r = "https://github.com/sajeed-islam/SNT-CODE-LIBRARY/blob/c4bb53b4a8ea48bbd23ea876dd77699a33623fb4/Blank imaGE.png?raw=true"
sample_output_shapefiles_python = "https://github.com/sajeed-islam/SNT-CODE-LIBRARY/blob/c4bb53b4a8ea48bbd23ea876dd77699a33623fb4/Blank imaGE.png?raw=true"

sample_output_health_facilities_r = "https://github.com/sajeed-islam/SNT-CODE-LIBRARY/blob/c4bb53b4a8ea48bbd23ea876dd77699a33623fb4/Blank imaGE.png?raw=true"
sample_output_health_facilities_python = "https://github.com/sajeed-islam/SNT-CODE-LIBRARY/blob/c4bb53b4a8ea48bbd23ea876dd77699a33623fb4/Blank imaGE.png?raw=true"

sample_output_routine_case_data_dhis2_r = "https://github.com/sajeed-islam/SNT-CODE-LIBRARY/blob/c4bb53b4a8ea48bbd23ea876dd77699a33623fb4/Blank imaGE.png?raw=true"
sample_output_routine_case_data_dhis2_python = "https://github.com/sajeed-islam/SNT-CODE-LIBRARY/blob/c4bb53b4a8ea48bbd23ea876dd77699a33623fb4/Blank imaGE.png?raw=true"

sample_output_DHS_Data_r = "https://github.com/sajeed-islam/SNT-CODE-LIBRARY/blob/c4bb53b4a8ea48bbd23ea876dd77699a33623fb4/Blank imaGE.png?raw=true"
sample_output_DHS_Data_python = "https://github.com/sajeed-islam/SNT-CODE-LIBRARY/blob/c4bb53b4a8ea48bbd23ea876dd77699a33623fb4/Blank imaGE.png?raw=true"

sample_output_Climate_Data_r = "https://github.com/sajeed-islam/SNT-CODE-LIBRARY/blob/c4bb53b4a8ea48bbd23ea876dd77699a33623fb4/Blank imaGE.png?raw=true"
sample_output_Climate_Data_python = "https://github.com/sajeed-islam/SNT-CODE-LIBRARY/blob/c4bb53b4a8ea48bbd23ea876dd77699a33623fb4/Blank imaGE.png?raw=true"


sample_output_LMIS_Data_r = "https://github.com/sajeed-islam/SNT-CODE-LIBRARY/blob/c4bb53b4a8ea48bbd23ea876dd77699a33623fb4/Blank imaGE.png?raw=true"
sample_output_LMIS_Data_python = "https://github.com/sajeed-islam/SNT-CODE-LIBRARY/blob/c4bb53b4a8ea48bbd23ea876dd77699a33623fb4/Blank imaGE.png?raw=true"

sample_output_Modeled_Data_r = "https://github.com/sajeed-islam/SNT-CODE-LIBRARY/blob/c4bb53b4a8ea48bbd23ea876dd77699a33623fb4/Blank imaGE.png?raw=true"
sample_output_Modeled_Data_python = "https://github.com/sajeed-islam/SNT-CODE-LIBRARY/blob/c4bb53b4a8ea48bbd23ea876dd77699a33623fb4/Blank imaGE.png?raw=true"

sample_output_Population_Data_r = "https://github.com/sajeed-islam/SNT-CODE-LIBRARY/blob/c4bb53b4a8ea48bbd23ea876dd77699a33623fb4/Blank imaGE.png?raw=true"
sample_output_Population_Data = "https://github.com/sajeed-islam/SNT-CODE-LIBRARY/blob/c4bb53b4a8ea48bbd23ea876dd77699a33623fb4/Blank imaGE.png?raw=true"

# Display content based on selected options
if data_option == 'Access to Care':
    st.subheader("Access to Care")
    
    if content_option == 'See R Code':
        st.code(r_code_shapefiles, language='r')
    elif content_option == 'See Python Code':
        st.code(python_code_shapefiles, language='python')
    elif content_option == 'Explanation of R Code':
        st.write(explanation_r_shapefiles)
    elif content_option == 'Explanation of Python Code':
        st.write(explanation_python_shapefiles)
    elif content_option == 'Sample Output':
        st.image(sample_output_shapefiles_r, caption="Sample output of the Access to Care R code")
        st.image(sample_output_shapefiles_python, caption="Sample output of the Access to Care Python code")

elif data_option == 'Seasonality':
    st.subheader("Seasonality")
    
    if content_option == 'See R Code':
        st.code(r_code_health_facilities, language='r')
    elif content_option == 'See Python Code':
        st.code(python_code_health_facilities, language='python')
    elif content_option == 'Explanation of R Code':
        st.write(explanation_r_health_facilities)
    elif content_option == 'Explanation of Python Code':
        st.write(explanation_python_health_facilities)
    elif content_option == 'Sample Output':
        st.image(sample_output_health_facilities_r, caption="Sample output of the Seasonality R code")
        st.image(sample_output_health_facilities_python, caption="Sample output of the Seasonality Python code")

elif data_option == 'Insecticide Resistance':
    st.subheader("Insecticide Resistance")
    
    if content_option == 'See R Code':
        st.code(r_code_health_facilities, language='r')
    elif content_option == 'See Python Code':
        st.code(python_code_health_facilities, language='python')
    elif content_option == 'Explanation of R Code':
        st.write(explanation_r_health_facilities)
    elif content_option == 'Explanation of Python Code':
        st.write(explanation_python_health_facilities)
    elif content_option == 'Sample Output':
        st.image(sample_output_health_facilities_r, caption="Sample output of the Insecticide Resistance R code")
        st.image(sample_output_health_facilities_python, caption="Sample output of the Insecticide Resistance Python code")


elif data_option == 'Anti-Malaria Drug Resistance':
    st.subheader("Anti-Malaria Drug Resistance")
    
    if content_option == 'See R Code':
        st.code(r_code_health_facilities, language='r')
    elif content_option == 'See Python Code':
        st.code(python_code_health_facilities, language='python')
    elif content_option == 'Explanation of R Code':
        st.write(explanation_r_health_facilities)
    elif content_option == 'Explanation of Python Code':
        st.write(explanation_python_health_facilities)
    elif content_option == 'Sample Output':
        st.image(sample_output_health_facilities_r, caption="Sample output of the Anti-Malaria Drug Resistance R code")
        st.image(sample_output_health_facilities_python, caption="Sample output of the Anti-Malaria Drug Resistance Python code")


# Add similar conditions for other data options if needed
