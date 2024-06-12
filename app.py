import streamlit as st


option=st.sidebar.selectbox('SELECT ONE',['Home Page','Country-Wise Analysis','Rating-Wise Analysis','Room-Types Analysis','Traveller-Types Analysis','Booked_Wise Analysis','Reviewed-Wise Analysis','Nightly-Stay Analysis'])
def load_home_page():
    st.title('Seashell Suites and Villas')
    st.image('56659478.jpg')

def load_Country_Wise_Analysis():
    st.title('Country-Wise Analysis')
    st.write("This section provides an analysis of Seashell Suites and Villas reviews based on country.")

def load_rating_Wise_Analysis():
    st.title('Rating-Wise Analysis')
    st.write("This section provides an analysis of Seashell Suites and Villas reviews based on rating.")
def load_room_type_Wise_Analysis():
    st.title('Room-Types Analysis')
    st.write("This section provides an analysis of Seashell Suites and Villas reviews based on room types.")

def load_traveller_types_Wise_Analysis():
    st.title('Traveller-Types Analysis')
    st.write("This section provides an analysis of Seashell Suites and Villas reviews based on traveller types.")
def load_booked_Wise_Analysis():
    st.title('Booked_Wise Analysis')
    st.write("This section provides an analysis of Seashell Suites and Villas reviews based on booked.")
def load_reviewed_Wise_Analysis():
    st.title('Reviewed-Wise Analysis')
    st.write("This section provides an analysis of Seashell Suites and Villas reviews based on reviewed.")

def load_Nightly_Stay_Analysis():
    st.title('Nightly-Stay Analysis')
    st.write("This section provides an analysis of Seashell Suites and Villas reviews based on nightly_stay.")



if option == 'Home Page':
    load_home_page()

elif option == 'Country-Wise Analysis':
    load_Country_Wise_Analysis()

elif option == 'Rating-Wise Analysis':
    load_rating_Wise_Analysis()

elif option == 'Room-Types Analysis':
    load_room_type_Wise_Analysis()

elif option == 'Traveller-Types Analysis':
    load_traveller_types_Wise_Analysis()

elif option == 'Booked_Wise Analysis':
    load_booked_Wise_Analysis()

elif option == 'Reviewed-Wise Analysis':
    load_reviewed_Wise_Analysis()

else:
    load_Nightly_Stay_Analysis()