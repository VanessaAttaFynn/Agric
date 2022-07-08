import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd
import plotly.express as px
import io 
import pyodbc
import plotly.figure_factory as ff
import pickle
import joblib  

st.set_page_config(page_title='Dataware Demo Platform', layout='wide')

if 'load_data' not in st.session_state:
    st.session_state.load_data = False


## Function that loads the data
@st.cache(suppress_st_warning=True)
def db_access(query, values=None):
    """Function to access database and collect data
    Args:
        query: query from user to extract data
    Returns:
        data: resulting data from query
    """
    # define database properties
    connection_string = ("Driver={SQL Server};"
                        "Server=DESKTOP-JIKIMCG;"
                        "Database=Dataware;"
                        "Trusted_Connection=yes;")
    
    # make connection
    connection = pyodbc.connect(connection_string)
    
    # read and load data
    data = pd.read_sql(query, connection, params=values)

    return data

@st.cache(suppress_st_warning=True)
def get_data():
    # queries to run
    query1 = " SELECT * FROM [dbo].[Customer_BioData] "
    query2 = " SELECT * FROM [dbo].[Customer_Transaction] "
    query3 = " SELECT * FROM [dbo].[Customer_CropYield] "

    # run query to load data
    cust = db_access(query1)
    trans = db_access(query2)
    crop = db_access(query3)

    return cust, trans, crop



# maintain the state of the app after changes to code
if st.session_state.load_data:
    st.session_state.load_data = True


st.sidebar.image('Images/logo.png', width=300)
st.sidebar.markdown('##')



# Creating the sidebar menu
with st.sidebar:
    choose = option_menu("Demo Platform", ["About", "Customer 360", "Credit Score", "Crop Yield", 
                        "Plant Disease", "Export Forecasting", "Contact"],
                         icons=['building', 'person-circle', 'cash-coin', 'flower1','flower3', 
                         'graph-up-arrow', 'person-rolodex'],
                         menu_icon="menu-app", default_index=0,
                         styles={"nav-link": {"--hover-color": "#eee"}}
                        )





#-----------------------------------------------------------------------------------------------------------------------
# THIS IS THE ABOUT SECTION
#------------------------------------------------------------------------------------------------------------------------

if choose == "About":    
    st.markdown("<h2 style='text-align:center;text-decoration:underline;text-underline-offset:0.7em;\
                text-decoration-color:#e8573f;'>ABOUT US</h2>", unsafe_allow_html=True)   

    st.markdown('##')
    st.markdown('##')
    st.markdown('##')

    col1, col2= st.columns([2, 2])
    with col1:
        image = Image.open('Images/about.png')
        new_image = image.resize((600, 350))
        st.image(new_image)
       
    with col2:
        st.markdown("<h4 style='font-weight:bold;'>ABOUT DATAWARE</h4><p style='text-align:justify;font-size:17px; \
                    font-family:'Lato' Sans-serif;'> \
                    Dataware is an award-winning African tech firm that provides big data, analytics, and cloud \
                    computing services. We strive to provide cutting edge data solutions to solve problems. \
                    </p><p style='font-weight:bold;font-size:20px;'>WHAT PROBLEM ARE WE SOLVING?</p>  \
                    <p style='text-align:justify;font-size:17px;font-family:'Lato' Sans-serif;'>In today’s global market, \
                    limited customer and operational insights prevents the innovative assessment of customers and risks \
                    which impacts business growth and sustainability. Our contribution to this effort is to provide an \
                    end to end customizable and scalable range of solutions to enable you to get deeper insights on \
                    customer behaviour and business operations to inform decision making in real time.</p>",
                    unsafe_allow_html=True)
    
    st.markdown("##")
    st.markdown("##")
    st.markdown("##")
    st.markdown("##")
    st.markdown("##")
  
    col3, col4, col5 = st.columns([0.5,2,0.5])
    with col4:
        st.image('Images/lucent.png')

        st.markdown("##")
        st.markdown("##")
        st.markdown("##")
        st.markdown("##")
        st.markdown("##")
        st.markdown("##")

    st.markdown("<h2 style='text-align:center;text-decoration:underline;text-underline-offset:0.7em;\
                text-decoration-color:#e8573f;'>OUR PRODUCTS</h2>", unsafe_allow_html=True)

    st.markdown("##")
    st.markdown("##")
    st.markdown("##")
  
    col3, col4, col5 = st.columns([1,1,1])
    with col3:
        st.markdown("<div style='background-color:#ffffff;text-align:left;border:2px solid #e8573f;border-radius:15px; \
                        padding:20px 20px;width:auto;height:400px;'> \
                        <h3 style='font-size:22px;'><svg xmlns='http://www.w3.org/2000/svg' width='50' height='50' fill='#e8573f' \
                        class='bi bi-clipboard-data' viewBox='0 0 16 16'> \
                        <path d='M4 11a1 1 0 1 1 2 0v1a1 1 0 1 1-2 0v-1zm6-4a1 1 0 1 1 2 0v5a1 1 0 1 1-2 0V7zM7 9a1 1 0 0 1 2 0v3a1 1 0 1 1-2 0V9z'/> \
                        <path d='M4 1.5H3a2 2 0 0 0-2 2V14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V3.5a2 2 0 0 0-2-2h-1v1h1a1 1 0 0 1 1 1V14a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V3.5a1 1 0 0 1 1-1h1v-1z'/> \
                        <path d='M9.5 1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-3a.5.5 0 0 1-.5-.5v-1a.5.5 0 0 1 .5-.5h3zm-3-1A1.5 1.5 0 0 0 5 1.5v1A1.5 1.5 0 0 0 6.5 4h3A1.5 1.5 0 0 0 11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3z'/> \
                        </svg>&nbsp;&nbsp;&nbsp;&nbsp;Lucent Business Intelligence</h3> \
                        <p style='font-size:18px;text-align:justify;'>Lucent BI is self-service, a trusted platform, provides insights and empowers business users. \
                        The Lucent BI platform processes and collects data from business operations to curate reports that \
                        provide a comprehensive view of your business.</p> \
                        <br><br><br>\
                        <a href='https://www.datawareghana.com/products/business-intelligence/' style='color:#e8573f;font-size:20px; \
                        text-decoration:None;'>Read More</a> \
                        </div>", 
                        unsafe_allow_html=True)
    with col4:
        st.markdown("<div style='background-color:#ffffff;text-align:left;border:2px solid #e8573f;border-radius:15px; \
                        padding:20px 20px;width:auto;height:400px;'> \
                        <h3 style='font-size:22px;'><svg xmlns='http://www.w3.org/2000/svg' width='50' height='50' fill='#e8573f' \
                        class='bi bi-person-video2' viewBox='0 0 16 16'> \
                        <path d='M10 9.05a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5Z'/> \
                        <path d='M2 1a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2H2ZM1 3a1 1 0 0 1 1-1h2v2H1V3Zm4 10V2h9a1 1 0 0 1 1 1v9c0 .285-.12.543-.31.725C14.15 11.494 12.822 10 10 10c-3.037 0-4.345 1.73-4.798 3H5Zm-4-2h3v2H2a1 1 0 0 1-1-1v-1Zm3-1H1V8h3v2Zm0-3H1V5h3v2Z'/> \
                        </svg>&nbsp;&nbsp;&nbsp;&nbsp;Lucent Customer Analytics</h3>\
                        <p style='font-size:18px;text-align:justify;'>Lucent Customer Analytics enables you to market precisely by segmenting prospects using insights \
                        derived from data and machine learning. Lucent’s AI driven models informs decision making related \
                        to selecting the best channel or mix of channels with a high level of accuracy.</p> \
                        <br><br>\
                        <a href='https://www.datawareghana.com/products/risk-360/' style='color:#e8573f;font-size:20px; \
                        text-decoration:None;'>Read More</a> \
                        </div>", 
                        unsafe_allow_html=True)
    with col5:
        st.markdown("<div style='background-color:#ffffff;text-align:left;border:2px solid #e8573f;border-radius:15px; \
                        padding:20px 20px;width:auto;height:400px;'> \
                        <h3 style='font-size:22px;'><svg xmlns='http://www.w3.org/2000/svg' width='50' height='50' fill='#e8573f' \
                        class='bi bi-radioactive' viewBox='0 0 16 16'> \
                        <path d='M8 1a7 7 0 1 0 0 14A7 7 0 0 0 8 1ZM0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8Z'/> \
                        <path d='M9.653 5.496A2.986 2.986 0 0 0 8 5c-.61 0-1.179.183-1.653.496L4.694 2.992A5.972 5.972 0 0 1 8 2c1.222 0 2.358.365 3.306.992L9.653 5.496Zm1.342 2.324a2.986 2.986 0 0 1-.884 2.312 3.01 3.01 0 0 1-.769.552l1.342 2.683c.57-.286 1.09-.66 1.538-1.103a5.986 5.986 0 0 0 1.767-4.624l-2.994.18Zm-5.679 5.548 1.342-2.684A3 3 0 0 1 5.005 7.82l-2.994-.18a6 6 0 0 0 3.306 5.728ZM10 8a2 2 0 1 1-4 0 2 2 0 0 1 4 0Z'/> \
                        </svg>&nbsp;&nbsp;&nbsp;&nbsp;Lucent Risk 360</h3>\
                        <p style='font-size:18px;text-align:justify;'>The risk associated with financial services grows as the service provider grows and adopts online and \
                        international transactions, new payment systems and technology. \
                        Lucent enables the usage of both structured and unstructured data, automating day to day assistance</p> \
                        <br><br>\
                        <a href='https://www.datawareghana.com/products/risk-360/' style='color:#e8573f;font-size:20px; \
                        text-decoration:None;'>Read More</a> \
                        </div>", 
                        unsafe_allow_html=True)










#-------------------------------------------------------------------------------------------------------------------------
# THIS IS THE CUSTOMER 360 PAGE
#--------------------------------------------------------------------------------------------------------------------------
if choose == 'Customer 360':

    # load data
    try:
        cust, trans, crop = get_data()
    except:
        st.markdown("<h5 style='color:red;position:absolute;top:50%;left:50%;margin-right:-50%;transform:translate(-50%, -50%)'>Please Connect to the Right Network</h5>", 
                    unsafe_allow_html=True)

    col1, col2, col3 = st.columns([0.7,1,0.7])

    with col2:
        form = st.form(key='my_form1', clear_on_submit=False)
        customer_ID = form.text_input(label='Enter Customer ID')
        submit_button = form.form_submit_button(label='Show Details')

    # getting the data
    if submit_button:
        new = cust[cust['ID'] == int(customer_ID)]
        name = new['NAME'].iloc[0]
        gender = new['GENDER'].iloc[0]
        age = new['AGE'].iloc[0]
        region = new['REGION'].iloc[0]
        city = new['CITY'].iloc[0]
        education = new['EDUCATION'].iloc[0]
        experience = new['EXPERIENCE'].iloc[0]
        phone = new['PHONE'].iloc[0]
        email = new['EMAIL'].iloc[0]
        marital = new['MARITAL_STATUS'].iloc[0]
        house = new['HAS_HOUSE'].iloc[0]
        car = new['HAS_CAR'].iloc[0]
        size = new['FAMILY_SIZE'].iloc[0]
        occupation = new['OCCUPATION'].iloc[0]
        income = new['INCOME'].iloc[0]
        avg = new['AVG_MONTH'].iloc[0]
        credit = new['CREDIT_SCORE'].iloc[0]
        yield_sc = new['YIELD_SCORE'].iloc[0]
        area = crop['AREA_HA'].iloc[0]
        land_reg = crop['REGION'].iloc[0]
        crops = crop['CROP'].iloc[0]
        prod = crop['PRODUCTION_MT'].iloc[0]
        own = crop['OWNERSHIP'].iloc[0]
        yie = round(crop['YIELD_MT_HA'].iloc[0], 2)
        crop_city = crop['CITY'].iloc[0]


        # customer bio data
        cust_info = {'Details': ['Name', 'Gender', 'Age', 'Region', 'City', 'Education','Phone', 'Email', 
        'Marital Status', 'Occupation'], 
        'Values': [name, gender, age, region, city, education, phone, email, marital, occupation]}
        customer = pd.DataFrame(data=cust_info).set_index('Details')

        # customer bio data
        indicators = {'Details': ['Experience', 'Has House', 'Has Car', 'Family Size', 'Annual Income', 
        'Monthly Transaction (AVG)','Credit Score', 'Yield Score'], 
        'Values': [experience, house, car, size, income, avg, credit, yield_sc]}
        indi = pd.DataFrame(data=indicators).set_index('Details')

        # crop details
        crop_det = {'Details': ['Land Region', 'Land City', 'Ownership','Area(HA)', 'Crop', 'Production', 
        'Yield'], 
        'Values': [land_reg, crop_city, own, area, crops, prod, yie]}
        land = pd.DataFrame(data=crop_det).set_index('Details')

        # when customer has performed a cto
        if trans[trans['ID'] == int(customer_ID)].shape[0] > 0:
            cto = trans[trans['ID'] == int(customer_ID)].reset_index(drop=True)
            sm_tab = cto.drop(columns=['ID']).iloc[:, 0:].fillna(0)
            sm_tab = sm_tab.round(2)
            tot = round(sm_tab.sum(axis=1).iloc[0], 2)
            #sm_tab.iloc[0, :] = sm_tab.iloc[0, :].map('{:,.0f}'.format)
            full_tab = cto.drop(columns=['ID']).fillna(0)
            plot = pd.melt(full_tab, value_vars=full_tab.columns)

        # when customer has not performed any cto
        if trans[trans['ID'] == int(customer_ID)].shape[0] == 0:
            cto = trans[trans['ID'] == int(customer_ID)]
            cto.loc[0, :] = [int(customer_ID),0,0,0,0,0,0,0,0,0,0,0,0]
            cto.reset_index(drop=True)
            sm_tab = cto.drop(columns=['ID']).iloc[:, 0:].fillna(0)
            sm_tab = sm_tab.round(2)
            tot = round(sm_tab.sum(axis=1).iloc[0], 2)
            #sm_tab.iloc[0, :] = sm_tab.iloc[0, :].map('{:,.0f}'.format)
            full_tab = cto.drop(columns=['ID']).fillna(0)
            plot = pd.melt(sm_tab, value_vars=sm_tab.columns)

        
        st.markdown('#')
        st.markdown('#')
        icols1, icols2 = st.columns(2)
        with icols1:
            st.subheader('Customer Information')
            #st.markdown('#')
            fig = ff.create_table(customer, colorscale=[[0, '#e8573f'], [.5, '#ffffff'],[1, '#ffffff']], index=True)
            fig.update_layout(width=560, plot_bgcolor='rgba(0,0,0,0)', height=430, margin=dict(l=0, r=10, t=10, b=10))
            for i in range(len(fig.layout.annotations)):
                fig.layout.annotations[i].font.size = 15
            st.write(fig)

        with icols2:
            st.subheader('Indicators')
            #st.markdown('#')
            fig = ff.create_table(indi, colorscale=[[0, '#e8573f'], [.5, '#ffffff'],[1, '#ffffff']], index=True)
            fig.update_layout(width=560, plot_bgcolor='rgba(0,0,0,0)', height=430, margin=dict(l=0, r=10, t=10, b=10))
            for i in range(len(fig.layout.annotations)):
                fig.layout.annotations[i].font.size = 15
            st.write(fig)

        st.markdown('##')
        st.markdown('##')
        icols3, icols4 = st.columns(2)
        with icols3:
            st.subheader('Land Information')
            #st.markdown('#')
            fig = ff.create_table(land, colorscale=[[0, '#e8573f'], [.5, '#ffffff'],[1, '#ffffff']], index=True)
            fig.update_layout(width=560, plot_bgcolor='rgba(0,0,0,0)', height=430, margin=dict(l=0, r=10, t=10, b=10))
            for i in range(len(fig.layout.annotations)):
                fig.layout.annotations[i].font.size = 15
            st.write(fig)

        with icols4:
            st.subheader('Customer Monthly Transaction')
            st.markdown('##')

            fig = px.line(plot, 'variable', 'value', markers=True, color_discrete_sequence=['#FF7377'])

            # edit line chart
            fig.update_traces(textposition="top center")
            fig.update_layout(width=500, plot_bgcolor='rgba(0,0,0,0)',margin=dict(l=0, r=0, t=10, b=50), height=430, yaxis_title=None, xaxis_title=None, uniformtext_minsize=5)
            fig.update_xaxes(tickangle=45)
            st.write(fig)














#--------------------------------------------------------------------------------------------------------------------------
# THIS IS THE CROP YIELD PREDICTION PAGE
#--------------------------------------------------------------------------------------------------------------------------
if choose == 'Crop Yield':
    col1, col2, col3 = st.columns([0.3, 2, 0.3])
    with col2:
        st.markdown("""<style> .font {text-align:center;font-size:35px ; font-family: 'Lato' 'San-Serif'; color: #e8573f;}</style>""",unsafe_allow_html=True)
        st.markdown('<p class="font">Crop Yield Prediction</p>', unsafe_allow_html=True)

        with st.expander('Individual Prediction', expanded=True):

            # take input from user for prediction
            form = st.form(key='my_form', clear_on_submit=True)
            region = form.selectbox('Select Region', ['BRONG AHAFO','CENTRAL','EASTERN','GREATER ACCRA','NORTHERN REGION','UPPER EAST','UPPER WEST','VOLTA','WESTERN'])
            area = form.number_input(label='Area (HA)', min_value=0, format="%d")
            production = form.number_input(label='Total Crop Production', min_value=0, format="%d")
            crop = form.selectbox('Select Crop Name', ['COCOYAM','COWPEA','GROUNDNUT','MAIZE','MILLET','PLANTAIN','RICE','SORGHUM','SOYABEAN','YAM'])
            year = form.selectbox('Select Year', [2008, 2009, 2010, 2011, 2012, 2013])
            form.markdown('##')
            submit_button = form.form_submit_button(label='Submit')

            # once user clicks on submit
            if submit_button:

                # get the data user inputted
                d = {'Land Region':[region], 'Land Area':[area],'Crop Production': [production], 
                    'Crop Name':[crop], 'Year':[year]}

                # create a dataframe and display it
                data = pd.DataFrame(data=d)
                d2 = {'Details': data.columns, 'Input Data':data.iloc[0]}
                new_data = pd.DataFrame(data=d2)
                new_data.set_index('Details', inplace=True)

                st.markdown('##')

                # data visualization in table form
                st.markdown("<p style='color:green; font-family:Verdana;'>Input Data</p>", unsafe_allow_html=True)
                fig = ff.create_table(new_data, colorscale=[[0, '#6EB52F'], [.5, '#e5fddc'],[1, '#ffffff']], index=True, index_title='Assembly Components')
                for i in range(len(fig.layout.annotations)):
                    fig.layout.annotations[i].font.size = 18

                st.plotly_chart(fig, use_container_width=True)


                st.markdown('##')

                # load the trained model
                st.markdown("<p style='color:green; font-family:Verdana;'>Predicted Output</p>", unsafe_allow_html=True)

                model = joblib.load("Reg_model.pkl")

                # make prediction and round values to 0 decimal places

                y_pred = model.predict(data)

                # define names for columns
                pred_columns = ['Yield (MT/HA)']

                output_df = pd.DataFrame(y_pred, columns=pred_columns)
                    
                d3 = {'Land Details': output_df.columns, 'Predicted Yield': output_df.iloc[0]}

                final = pd.DataFrame(data=d3)
                final['Predicted Yield'] = final['Predicted Yield'].abs().astype('int')
                final.set_index('Land Details', inplace=True)

                # data visualization
                fig = ff.create_table(final, colorscale=[[0, '#6EB52F'], [.5, '#e5fddc'],[1, '#ffffff']], index=True, index_title='Assembly Components')
                for i in range(len(fig.layout.annotations)):
                    fig.layout.annotations[i].font.size = 18
                
                st.plotly_chart(fig, use_container_width=True)


            st.markdown('##')

        ##-----------------------------------------------------------------------------------------------------------------------------
        ## Page Layout - Batch Prediction
        ##----------------------------------------------------------------------------------------------------------------------------

        with st.expander('Batch Prediction'):

            # define the file uploader
            def file_upload(name):
                    uploaded_file = st.file_uploader('%s' % (name),key='%s' % (name), accept_multiple_files=False)
                    content = False
                    if uploaded_file is not None:
                        try:
                            uploaded_df = pd.read_csv(uploaded_file)
                            content = True
                            return content, uploaded_df
                        except:
                            try:
                                uploaded_df = pd.read_excel(uploaded_file)
                                content = True
                                return content, uploaded_df
                            except:
                                st.error('Please ensure file is .csv or .xlsx format and/or reupload file')
                                return content, None
                    else:
                        return content, None

            st.markdown('##')

            # define template file to be uploaded
            st.markdown("<p style='color:red; font-family: Verdana; font-size:1em;'>Please upload batch input data for crop yield prediction.\
                            See template below (.xlsx or .csv)</p>", unsafe_allow_html=True)

            # upload file in csv or excel format
            status, df = file_upload(" ")

            st.markdown('##')

            # once user clicks submit
            if st.button('Submit'):

                # make prediction
                def pred_model(model):
                    with open(model , 'rb') as f:
                        model = pickle.load(f)

                    # define names of columns
                    pred_columns = ['Yield']

                    # make predictions and round to zero decimal places
                    y_pred = model.predict(df)
                    output_df = pd.DataFrame(y_pred, columns=pred_columns)
                    output_df = output_df.abs().astype('int')
                    
                    # join input data to output data
                    result = pd.concat([df, output_df], axis=1, join='inner')

                    # set custom index range for dataframe
                    new_index = [str(i).zfill(6) for i in range(1, result.shape[0]+1)]
                    result.index = new_index

                    return result
                
                st.markdown('##')

                # make predictions and display output
                st.markdown("<p style='color:green; font-family: Verdana;'>Predicted Output</p>", unsafe_allow_html=True)
                pred_data = pred_model('./Reg_model.pkl')
                st.dataframe(pred_data)

                st.markdown('##')

                # user can download data here - remember to 'pip install xlsxwriter'
                name = 'yield' + '.xlsx'

                buffer = io.BytesIO()
                with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                    pred_data.to_excel(writer, index=True)
                    writer.save()

                st.download_button(label='Download Data', data=buffer, file_name=name, mime='application/vnd.ms-excel')







#--------------------------------------------------------------------------------------------------------------------------
# THIS IS THE CREDIT RATING PAGE
#--------------------------------------------------------------------------------------------------------------------------










#--------------------------------------------------------------------------------------------------------------------------
# THIS IS THE PLANT DISEASE PREDICTION PAGE
#--------------------------------------------------------------------------------------------------------------------------










#--------------------------------------------------------------------------------------------------------------------------
# THIS IS THE EXPORT PREDICTION PAGE
#--------------------------------------------------------------------------------------------------------------------------













#--------------------------------------------------------------------------------------------------------------------------
# THIS IS THE CONTACT US PAGE
#--------------------------------------------------------------------------------------------------------------------------

if choose == 'Contact':

    st.markdown("<h2 style='text-align:center;text-decoration:underline;text-underline-offset:0.7em;\
                text-decoration-color:#e8573f;'>CONTACT US</h2>", unsafe_allow_html=True)

    st.markdown('#')
    st.markdown('#')
    st.markdown('#')

    cols1, cols2, cols3, cols4 = st.columns([1,1,1,1])
    
    with cols1:
        st.markdown("<div style='background-color:#e8573f;text-align:center;border:2px solid #e8573f;border-radius:15px; \
                        padding:20px 20px;width:auto;height:200px;'> \
                        <h3 style='font-size:25px;color:#ffffff'>Corporate Head Office</h3> \
                        <p style='font-size:20px; color:#ffffff'> \
                        Mövenpick Ambassador Hotel <br> Emporium, 9th Floor Independence Avenue – Accra</p></div>", 
                        unsafe_allow_html=True)

    with cols2:
        st.markdown("<div style='background-color:#ffffff;text-align:center;border:2px solid #e8573f;border-radius:15px; \
                        padding:50px 20px;width:auto;height:200px;'> \
                        <h3 style='font-size:25px;'>Telephone</h3> \
                        <p style='font-size:20px;'>Tel: +233 (0) 30 263 3269</p></div>", 
                        unsafe_allow_html=True)

    with cols3:
        st.markdown("<div style='background-color:#ffffff;text-align:center;border:2px solid #e8573f;border-radius:15px; \
                        padding:50px 20px;width:auto;height:200px;'> \
                        <h3 style='font-size:25px;'>Email</h3> \
                        <p style='font-size:20px;'>info@datawareghana.com</p></div>", 
                        unsafe_allow_html=True)                   

    with cols4:
        st.markdown("<div style='background-color:#ffffff;text-align:center;border:2px solid #e8573f;border-radius:15px; \
                        padding:50px 20px;width:auto;height:200px;'> \
                        <h3 style='font-size:25px;'>Corporate Office Hour</h3> \
                        <p style='font-size:20px;'>Mon – Fri: 9:00am – 4:30pm GMT</p></div>", 
                        unsafe_allow_html=True)  


    st.markdown('#')
    st.markdown('#')
    st.markdown('#')

    col1, col2, col3 = st.columns([0.3, 2, 0.3])
    with col2:
        st.markdown("""<style> .font {text-align:center;font-size:35px ; font-family: 'Lato' 'San-Serif'; color: #e8573f;}</style>""",unsafe_allow_html=True)
        st.markdown('<p class="font">Contact Form</p>', unsafe_allow_html=True)

        with st.form(key='form2', clear_on_submit=True):
            Name = st.text_input(label='Name', placeholder='John Doe', ) 
            Email = st.text_input(label='Email', placeholder='john.doe@gmail.com') 
            Subject = st.text_input(label='Subject') 
            Message = st.text_input(label='Message', max_chars=250)
            submit = st.form_submit_button('Submit')
            if submit:
                st.markdown('#')
                st.write('Thanks for your contacting us. We will respond to your questions or inquiries as soon as possible!')

    st.markdown('#')
    st.markdown('#')
    st.markdown('#')
    st.markdown('#')

    dat = pd.DataFrame([[5.55419849617552, -0.20252726185676254]], columns=['latitude','longitude'])
    st.map(dat, use_container_width=True)

