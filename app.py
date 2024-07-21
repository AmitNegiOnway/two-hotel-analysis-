import streamlit as st
import pandas as pd
from plotly import express as px
st.set_page_config(layout='wide')
option =st.sidebar.selectbox('select one ',['About ','Taj Fort Aguada Resort & Spa','Seashell Suites and Villas'])
df=pd.read_csv('seashell.csv')
dff=pd.read_csv('clean_Taj_Fort_Aguada_Resort_&_Spa.csv')
df['rating']=df.rating.astype('int64')

df['booked']=pd.to_datetime(df['booked'])
df['booked_month']=df['booked'].dt.month_name()
df['booked_year']=df['booked'].dt.year

dff['booked']=pd.to_datetime(df['booked'])
dff['booked_month']=dff['booked'].dt.month_name()
dff['booked_year']=dff['booked'].dt.year

dff['booked_year']=dff.booked_year.astype(str).str.split('.').str.get(0)



df['room_types']=df.room_types.str.strip()
dff['room_types']=dff.room_types.str.strip()




def load_home_page():
    import streamlit as st

    import streamlit as st

    # Set the page configuration

    # Define CSS styles
    st.markdown("""
        <style>
        .main {
            font-family: Arial, sans-serif;
            color: #333;
            line-height: 1.6;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        .section-title {
            font-size: 24px;
            margin-top: 20px;
            border-bottom: 2px solid #2c3e50;
            padding-bottom: 10px;
        }
        .content {
            margin-top: 20px;
        }
        .content ul {
            margin-left: 20px;
        }
        .highlight {
            color: #e74c3c;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

    # Title of the application
    st.markdown("<h1 class='main'>Resort Reviews Analysis</h1>", unsafe_allow_html=True)

    # About Section
    st.markdown("<h2 class='section-title'>About</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class='content'>
            <p>
                This Streamlit web application is designed to provide a comprehensive comparison and analysis of reviews for two prominent resorts in Goa: 
                <strong>Seashell Suites and Villas in Candolim</strong>, and <strong>Taj Fort Aguada Resort & Spa</strong>. The application leverages various Python libraries, including Streamlit for web app creation, Pandas for data manipulation, and Plotly Express for interactive visualizations.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Taj Fort Aguada Resort & Spa, Goa Section
    st.markdown("<h2 class='section-title'>Taj Fort Aguada Resort & Spa, Goa</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class='content'>
            <p>
                This section focuses on the Taj Fort Aguada Resort & Spa. It begins by reading the review data for this resort from a CSV file. The data includes various columns such as reviewer name, review date, review text, and ratings. The application then performs several analytical tasks, including:
            </p>
            <ul>
                <li><strong>Displaying Raw Data:</strong> The raw review data is displayed in a table format using Streamlit's <code>st.dataframe</code> method, allowing users to view the complete dataset.</li>
                <li><strong>Visualizing Ratings:</strong> A bar chart is created using Plotly Express to show the distribution of ratings for the resort. This helps users understand the overall rating trends.</li>
                <li><strong>Top Positive and Negative Reviews:</strong> The application identifies and displays the top positive and negative reviews based on the review ratings. This provides insights into the strengths and weaknesses of the resort as perceived by guests.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # Seashell Suites and Villas, Candolim Goa Section
    st.markdown("<h2 class='section-title'>Seashell Suites and Villas, Candolim Goa</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class='content'>
            <p>
                Similar to the previous section, this part of the application is dedicated to Seashell Suites and Villas in Candolim. It follows the same structure and analytical approach:
            </p>
            <ul>
                <li><strong>Displaying Raw Data:</strong> The review data for Seashell Suites and Villas is read from a CSV file and displayed in a table format.</li>
                <li><strong>Visualizing Ratings:</strong> A bar chart is generated to show the distribution of ratings for this resort.</li>
                <li><strong>Top Positive and Negative Reviews:</strong> The application extracts and presents the top positive and negative reviews to highlight the key aspects of guest experiences at this resort.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # Comparison Section
    st.markdown("<h2 class='section-title'>Comparison Section</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class='content'>
            <p>
                The "Comparison" section is a crucial part of the application as it directly compares the reviews of the two resorts. This section aims to provide users with a side-by-side comparison to help them make a more informed choice. The comparison includes:
            </p>
            <ul>
                <li><span class="highlight">Rating Distributions:</span> Two bar charts are displayed side by side, showing the rating distributions for both resorts. This visual comparison helps users quickly grasp how each resort fares in terms of guest satisfaction.</li>
                <li><span class="highlight">Word Cloud Analysis:</span> The application generates word clouds for both resorts using the review text. Word clouds are visual representations of the most frequently used words in the reviews, providing insights into common themes and topics mentioned by guests.</li>
                <li><span class="highlight">Statistical Comparison:</span> Basic statistical metrics, such as average ratings and the number of reviews, are calculated and displayed for both resorts. This quantitative comparison adds depth to the analysis.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # Additional Analyses
    st.markdown("""
        <div class='section-content'>
            <p>
                The "Additional Analyses" section dives deeper into various aspects of the review data, offering a comprehensive understanding of different factors influencing guest satisfaction. This section includes:
            </p>
            <ul>
                <li><span class="highlight">Country-Wise Analysis:</span> This analysis breaks down review data based on the geographical location of the reviewers. It provides insights into how guests from different countries perceive each resort and identifies any notable differences in sentiment or ratings between reviewers from various countries.</li>
                <li><span class="highlight">Rating-Wise Analysis:</span> This section examines the distribution of ratings across various categories, such as service quality, amenities, and value for money. It helps in understanding how different aspects of the resorts are rated by guests and identifies patterns and trends in the ratings.</li>
                <li><span class="highlight">Room-Types Analysis:</span> Here, the review data is categorized based on the type of room booked by guests. This analysis reveals how different room types impact guest satisfaction and overall ratings, highlighting preferences and experiences associated with various room types.</li>
                <li><span class="highlight">Booked-Wise Analysis:</span> This analysis focuses on reviews based on the booking type, such as direct bookings, third-party bookings, or group bookings. It explores how the booking channel influences guest satisfaction and overall ratings, providing insights into correlations between booking types and guest experiences.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # Sentiment Analysis Section
    st.markdown("<h2 class='section-title'>Sentiment Analysis</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class='content'>
            <p>
                The "Sentiment Analysis" section delves into the sentiment expressed in the reviews. Sentiment analysis is a natural language processing technique used to determine whether a piece of text expresses positive, negative, or neutral sentiments. This section includes:
            </p>
            <ul>
                <li><strong>Sentiment Distribution:</strong> A pie chart is created to show the distribution of positive, negative, and neutral sentiments in the reviews for each resort. This visualization helps users understand the overall sentiment trends.</li>
                <li><strong>Sentiment Over Time:</strong> Line charts are used to display how sentiments have changed over time. This can be particularly useful to identify any trends or shifts in guest satisfaction.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # Web Scraping and Data Gathering
    st.markdown("<h2 class='section-title'>Web Scraping and Data Gathering</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class='content'>
            <p>
                In addition to analyzing existing review data, the application also has the capability to gather data through web scraping. The user can perform web scraping on Booking.com to collect the latest reviews for the two resorts. This involves writing a web scraping script using libraries such as BeautifulSoup and Requests to extract review data from Booking.com pages. The collected data can then be saved to CSV files, which can be read by the application for further analysis. This feature ensures that the application remains up-to-date with the most recent guest reviews, providing users with the latest insights.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Implementation Details
    st.markdown("<h2 class='section-title'>Implementation Details</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class='content'>
            <p>
                The implementation of this application involves several key steps:
            </p>
            <ul>
                <li><strong>Data Collection:</strong> Review data for the two resorts is collected from Booking.com using web scraping techniques. This data is saved in CSV files for easy access.</li>
                <li><strong>Data Cleaning:</strong> The collected data is cleaned and preprocessed to ensure it is in a suitable format for analysis. This includes handling missing values, converting date formats, and standardizing text data.</li>
                <li><strong>Data Analysis and Visualization:</strong> The cleaned data is analyzed using Pandas to calculate statistical metrics and generate insights. Visualizations are created using Plotly Express to provide interactive and informative charts.</li>
                <li><strong>Sentiment Analysis:</strong> Natural language processing techniques are used to perform sentiment analysis on the review text. This involves using pre-trained sentiment analysis models to classify the sentiment of each review.</li>
                <li><strong>Streamlit Interface:</strong> The analyzed data and visualizations are integrated into a Streamlit web application. The application is designed with a user-friendly interface, allowing users to easily navigate through different sections and interact with the data.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # Conclusion
    st.markdown("<h2 class='section-title'>Conclusion</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class='content'>
            <p>
                This Streamlit web application provides a robust platform for analyzing and comparing guest reviews for Seashell Suites and Villas in Candolim, and Taj Fort Aguada Resort & Spa. By leveraging web scraping, data analysis, and visualization techniques, the application offers valuable insights into guest experiences, helping potential visitors make informed decisions. The sentiment analysis feature adds an additional layer of understanding by revealing the emotional tone of the reviews. Overall, the application serves as a powerful tool for both resort management and prospective guests, promoting transparency and informed decision-making in the hospitality industry.
            </p>
        </div>
    """, unsafe_allow_html=True)


def load_Seashell():


    tab1, tab2, tab3, tab4, tab5,  = st.tabs(
        ['Home Page', 'Country-Wise Analysis', 'Rating-Wise Analysis', 'Room-Types Analysis',
          'Booked_Wise Analysis'])

    with tab1:
        st.title('Seashell Suites and Villas')
        st.image('56659478.jpg')


        st.markdown("""
            <style>
            .main {
                font-family: Arial, sans-serif;
                color: #333;
                line-height: 1.6;
            }
            h1, h2, h3 {
                color: #2c3e50;
            }
            .section-title {
                font-size: 24px;
                margin-top: 20px;
                border-bottom: 2px solid #2c3e50;
                padding-bottom: 10px;
            }
            .content {
                margin-top: 20px;
            }
            .content ul {
                margin-left: 20px;
            }
            .highlight {
                color: #e74c3c;
                font-weight: bold;
            }
            .links a {
                color: #3498db;
                text-decoration: none;
            }
            .links a:hover {
                text-decoration: underline;
            }
            </style>
        """, unsafe_allow_html=True)

        # Title of the application
        st.markdown("<h1 class='main'>Seashell Suites and Villas: A Luxurious Oasis in Candolim, Goa</h1>",
                    unsafe_allow_html=True)

        # Prime Location Section
        st.markdown("<h2 class='section-title'>Prime Location</h2>", unsafe_allow_html=True)
        st.markdown("""
            <div class='content'>
                <p>
                    Seashell Suites and Villas enjoys a prime location in Pintos Vaddo, Candolim. The famed Candolim Beach lies just a short stroll away, inviting you to sink your toes into the golden sands and soak up the warm Goan sunshine. The area itself is abuzz with activity, offering a mix of trendy cafes, bustling restaurants, and vibrant nightlife for those seeking a taste of the local scene.
                </p>
            </div>
        """, unsafe_allow_html=True)

        # Accommodation Options Section
        st.markdown("<h2 class='section-title'>Accommodation Options</h2>", unsafe_allow_html=True)
        st.markdown("""
            <div class='content'>
                <p>
                    Seashell Suites and Villas caters to a variety of travelers, offering two distinct accommodation options:
                </p>
                <ul>
                    <li><strong>Junior Suites:</strong> These well-furnished suites boast a large bedroom that opens into a comfortable sitting area. Each suite features a private balcony with either pool or garden views, an ensuite bathroom with a shower, air conditioning, a refrigerator, a microwave, an electric kettle, and complimentary Wi-Fi. Perfect for couples or solo travelers, the spacious layout ensures a comfortable and relaxing stay.</li>
                    <li><strong>Three-Bedroom Villas:</strong> Ideal for families or groups of friends, these expansive villas offer a haven of privacy and relaxation. Featuring three bedrooms with attached bathrooms boasting showers, each villa also includes a spacious lounge area with flat-screen TVs. The large balconies provide the perfect spot to unwind and enjoy stunning pool or garden views. Villas come fully equipped with air conditioning, a refrigerator, a microwave, an electric kettle, and complimentary Wi-Fi.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

        # Unwinding at the Resort Section
        st.markdown("<h2 class='section-title'>Unwinding at the Resort</h2>", unsafe_allow_html=True)
        st.markdown("""
            <div class='content'>
                <p>
                    Stepping into Seashell Suites and Villas feels like entering a luxurious oasis. Three crystal-clear swimming pools offer the perfect place to cool off and soak up the sun. Whether you prefer lounging by the pool with a refreshing drink or indulging in a refreshing dip, the resort caters to every mood. For those seeking some light exercise, a well-equipped gym is available on-site.
                </p>
            </div>
        """, unsafe_allow_html=True)

        # Gastronomic Delights Section
        st.markdown("<h2 class='section-title'>Gastronomic Delights</h2>", unsafe_allow_html=True)
        st.markdown("""
            <div class='content'>
                <p>
                    Seashell Suites and Villas features the delectable "Neptune's Harvest," a multi-cuisine restaurant that tantalizes taste buds with a diverse menu. From traditional Goan delicacies to Indian classics, continental favorites, and even a selection of Chinese dishes, the restaurant caters to a wide range of palates. The breakfast buffet is consistently praised for its impressive spread, featuring live counters and a variety of delicious options to fuel your day.
                </p>
            </div>
        """, unsafe_allow_html=True)

        # Exceptional Service Section
        st.markdown("<h2 class='section-title'>Exceptional Service</h2>", unsafe_allow_html=True)
        st.markdown("""
            <div class='content'>
                <p>
                    Seashell Suites and Villas prides itself on its warm and welcoming atmosphere, largely due to the exceptional service offered by its friendly and helpful staff. Reviews consistently highlight the personalized attention and genuine care provided by the team, ensuring a truly unforgettable stay.
                </p>
            </div>
        """, unsafe_allow_html=True)

        # Exploring the Surroundings Section
        st.markdown("<h2 class='section-title'>Exploring the Surroundings</h2>", unsafe_allow_html=True)
        st.markdown("""
            <div class='content'>
                <p>
                    While the resort itself offers a complete and luxurious experience, the vibrant surroundings of Candolim beckon further exploration. Venture out and discover the charming beach shacks serving fresh seafood cocktails, explore the local shops brimming with Goan handicrafts, or indulge in an evening of pulsating nightlife. The iconic Shanta Durga Temple, situated 4 kilometers away, offers a glimpse into the region's rich cultural heritage. For a taste of adventure, consider exploring the bustling markets of Panjim or embarking on a thrilling water sports adventure off Candolim Beach.
                </p>
                <p>
                    Seashell Suites and Villas offers the perfect blend of luxury, comfort, and exceptional service, making it a quintessential Goan getaway. Whether you seek a relaxing retreat by the pool, a base for exploring the vibrant surroundings, or a luxurious haven to indulge in with loved ones, Seashell Suites and Villas promises a truly unforgettable experience.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with tab2:
        st.title('Country-Wise Analysis')
        st.write("This section provides an analysis of Seashell Suites and Villas reviews based on country.")
        st.subheader('Overall')
        col1,col2 = st.columns(2)


        # Add content to the first column
        with col1:
            st.subheader('Top 10 Nationalities of Hotel Guests')

            con = df['country'].value_counts().head(10).reset_index(name='count').rename(columns={'index': 'country'})

            # Plotting the pie chart
            fig = px.pie(con, values='count', names='country', title='Top 10 Countries by Count')
            st.plotly_chart(fig)

        # Add content to the second colums


        with col2:

            st.subheader('Top 10 Nationalities by Average Hotel Rating')
            dff = df[['country', 'rating']]
            dff = dff.groupby('country').agg({'rating': 'mean'}).reset_index().round(1)
            con = df['country'].value_counts().head(10).index

            # Filter the mean ratings to include only the top 10 countries by count
            dff = dff[dff['country'].isin(con)]
            dff = dff.sort_values(by='rating', ascending=False)
            fig = px.bar(dff, x='country', y='rating', text='rating', labels={'rating': 'Average Rating'})
            fig.update_layout(height=500)
            st.plotly_chart(fig)


        col1,col2 = st.columns(2)


        with col1:
            st.subheader('Avergae Stay Night And No.of Tourist')

            high = df['country'].value_counts()
            high_dict = high.to_dict()
            nigh = df.groupby('country')['nights'].mean().round(1)
            nigh_dict = nigh.to_dict()
            px.set_mapbox_access_token('YOUR_MAPBOX_ACCESS_TOKEN')
            fig = px.scatter_mapbox(df, lat='latitude', lon='longitude', hover_name='country',
                                    hover_data={
                                        'No. of Tourist': [high_dict.get(country, '') for country in df['country']],
                                        'Avg. Stay Night': [nigh_dict.get(country, '') for country in df['country']]},
                                    mapbox_style="carto-positron",
                                    zoom=1)
            fig.update_traces(hovertemplate="<b>%{hovertext}</b><br>" +
                                            "No. of Tourist: %{customdata[0]}<br>" +
                                            "Avg. Stay Night: %{customdata[1]}<br>")
            fig.update_layout( height=600)
            st.plotly_chart(fig)


        with col2:
            st.subheader('Top Destinations: Discover Where Guests Enjoy the Longest Stays at Our Hotel')

            ok = df.groupby('country').nights.mean().sort_values(ascending=False).head(10).reset_index(
                name='Avg. Nights')
            fig=px.bar(ok, x='country', y='Avg. Nights')
            st.plotly_chart(fig)







        st.selectbox('Select Country',sorted(df.country.str.strip().unique().tolist()))

    with tab3:
        st.title('Rating-Wise Analysis')
        st.write("This section provides an analysis of Seashell Suites and Villas reviews based on rating.")

        select = st.selectbox('Select Rating', sorted(df.rating.unique())).round(0)
        select = int(select)

        total = int(df[df.rating == select].count().country)


        col1,col2=st.columns(2)

        with col1:
            st.metric('Global Participation in Hotel Ratings', select, total)
        with col2:
            total = df[df.rating == select].country.count()
            total_night = df[df.rating == select].nights.sum()
            avg_stay=(total_night / total).round(1)
            st.metric("Average Stay Duration per Rating Category", select, avg_stay)


        st.subheader('Countries by Hotel Ratings')
        rate_con = df[df.rating == select].country.value_counts().reset_index(name='rating').rename(
                columns={'index': 'country'})
        fig = px.bar(rate_con, x='country', y='rating', text_auto=True)
        fig.update_layout(width=1300,height=700)
        st.plotly_chart(fig)


        col1, col2 = st.columns(2)

        with col1:
            st.subheader('Room Type Preferences Across Guest Ratings')
            ok = df[df.rating == select]
            ok = ok.room_types.value_counts().reset_index(name='counts').rename(columns={'index': 'room_types'})
            fig=px.bar(ok, x='room_types', y='counts', text_auto=True)

            st.plotly_chart(fig)

        with col2:
            st.subheader('Total Nights Stayed per Room Type by Guest Ratings')

            rock = df[df.rating == select]
            fig = px.sunburst(rock, path=['rating', 'room_types'], values='nights', color='room_types')

            # fig.update_layout(height=500,width=400)
            st.plotly_chart(fig)



    with tab4:
        st.title('Room-Types Analysis')
        st.write("This section provides an analysis of Seashell Suites and Villas reviews based on room types.")


        col1,col2=st.columns(2)
        with col1:

            st.subheader('custumer booked room type')
            room_type = df['room_types'].value_counts().reset_index(name='count').rename(columns={'index': 'room_type'})
            fig=px.pie(room_type, values='count', names='room_types')
            st.plotly_chart(fig)


        with col2:

            st.subheader('sum of booked night')
            night= df.groupby('room_types').nights.sum().reset_index(name='total night').rename(columns={'index': 'room types'})
            fig=px.bar(night,x='room_types',y='total night',text_auto=True)
            st.plotly_chart(fig)




        st.title('ROOMS TYPES METRIC - RATING')

        col1,col2,col3,col4=st.columns(4)
        mean = df.groupby('room_types').rating.mean().reset_index()

        with col1:
            st.metric('Junior Suite with King Bed',mean.rating.iloc[0].round(2))


        with col2:
            st.metric('Junior Suite with Twin Bed',mean.rating.iloc[1].round(2))


        with col3:
            st.metric('Three-Bedroom Villa',mean.rating.iloc[2].round(2))


        with col4:
            st.metric('Junior Suite with King Bed',mean.rating.iloc[3].round(2))


    with tab5:
        st.title('Booked_Wise Analysis')
        st.write("This section provides an analysis of Seashell Suites and Villas reviews based on booked.")

        year=st.selectbox('select year',sorted(df.booked_year.unique()))

        col1,col2=st.columns(2)

        with col1:
            st.subheader('room types ')
            filtered_df = df[df.booked_year == year]
            top_year = filtered_df['room_types'].value_counts()
            top_year = top_year.reset_index(name='COUNTS').rename(columns={'index': 'ROOM_TYPES'})
            fig = px.bar(top_year, x='room_types', y='COUNTS', text_auto=True, log_y=True)
            fig.update_layout(

                xaxis_title='Room Types',
                yaxis_title='Counts',
                font=dict(size=14)
            )
            st.plotly_chart(fig)

        with col2:
            st.subheader('traveller types ')
            filtered_df = df[df.booked_year == year]
            traveler_type = filtered_df['traveler_type'].value_counts()
            traveler_type = traveler_type.reset_index(name='COUNTS').rename(columns={'index': 'traveler_type'})
            fig = px.bar(traveler_type, x='traveler_type', y='COUNTS', text_auto=True, log_y=True)
            fig.update_layout(
                xaxis_title='Traveler Type',
                yaxis_title='Count',
                font=dict(size=14)
            )
            st.plotly_chart(fig)



        st.subheader('Top country visitors')
        filtered_df=df[df.booked_year == year]
        top_year = filtered_df.country.value_counts()
        top_year = top_year.reset_index(name='counts').rename(columns={'index': 'country'})
        fig=px.bar(top_year, x='country', y='counts', text_auto=True,width=1350,height=500)
        st.plotly_chart(fig)




        st.subheader('Room Type With Total Nights')
        pivot_table = df.pivot_table(index='booked_year', columns='room_types', values='nights', aggfunc='sum')
        pivot_table = df.pivot_table(index='booked_year', columns='room_types', values='nights', aggfunc='sum')
        # Rename the columns if necessary
        pivot_table = pivot_table.rename(columns=lambda x: f'Total Night - {x}')
        # Convert pivot table to long format for plotly
        long_df = pivot_table.reset_index().melt(id_vars='booked_year', var_name='room_types', value_name='Total Night')
        # Create the bar plot
        fig=px.bar(long_df, x='booked_year', y='Total Night', color='room_types', barmode='group', text_auto=True,log_y=True,width=1350,height=500)
        st.plotly_chart(fig)




        # MONTH ANALYSIS

        st.title('MONTH WISE ANALYSIS')
        month_order = [
            'January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December', 'Unknown'
        ]
        select_month = st.selectbox('select year', month_order)

        filtered_df = df[(df['booked_year'] == year) & (df['booked_month'] == select_month)]

        col1, col2 = st.columns(2)

        with col1:
            st.subheader(f'Room Types in  - {select_month}')

            top_year = filtered_df['room_types'].value_counts()
            top_year = top_year.reset_index(name='COUNTS').rename(columns={'index': 'ROOM_TYPES'})
            fig = px.bar(top_year, x='room_types', y='COUNTS', text_auto=True, log_y=True)
            st.plotly_chart(fig)

        with col2:
            st.subheader(f'Traveller Type in  - {select_month}')

            traveler_type = filtered_df['traveler_type'].value_counts()
            traveler_type = traveler_type.reset_index(name='COUNTS').rename(columns={'index': 'traveler_type'})
            fig = px.bar(traveler_type, x='traveler_type', y='COUNTS', text_auto=True, log_y=True)
            st.plotly_chart(fig)

        st.subheader(f'Top country visitors in  - {select_month}')
        top_year = filtered_df.country.value_counts()
        top_year = top_year.reset_index(name='counts').rename(columns={'index': 'country'})
        fig = px.bar(top_year, x='country', y='counts', text_auto=True, width=1350, height=500)
        st.plotly_chart(fig)

        line = df[df.booked_year == year].booked_month.value_counts().reset_index(name='count').rename(
            columns={'index': 'Months'})
        fig = px.line(line, x='booked_month', y='count')
        st.plotly_chart(fig)



def load_taj_fort():


    tab1, tab2, tab3, tab4,tab5,= st.tabs(['Home Page', 'Country-Wise Analysis', 'Rating-Wise Analysis', 'Room-Types Analysis', 'Booked_Wise Analysis'])

    with tab1:
        st.title('Taj Fort Aguada Resort & Spa')
        st.image('113048694.jpg')


        # Define CSS styles
        st.markdown("""
            <style>
            .main {
                font-family: Arial, sans-serif;
                color: #333;
                line-height: 1.6;
            }
            h1, h2, h3 {
                color: #2c3e50;
            }
            .section-title {
                font-size: 24px;
                margin-top: 20px;
                border-bottom: 2px solid #2c3e50;
                padding-bottom: 10px;
            }
            .content {
                margin-top: 20px;
            }
            .content ul {
                margin-left: 20px;
            }
            .highlight {
                color: #e74c3c;
                font-weight: bold;
            }
            .links a {
                color: #3498db;
                text-decoration: none;
            }
            .links a:hover {
                text-decoration: underline;
            }
            </style>
        """, unsafe_allow_html=True)

        # Title of the application
        st.markdown("<h1 class='main'>Luxurious Escape at Taj Fort Aguada Resort & Spa, Goa</h1>",
                    unsafe_allow_html=True)

        # Location Section
        st.markdown("<h2 class='section-title'>Location</h2>", unsafe_allow_html=True)
        st.markdown("""
            <div class='content'>
                <p>
                    The Taj Fort Aguada Resort & Spa is a premier beachfront resort nestled in Candolim, North Goa. It boasts a picturesque location overlooking the stunning Sinquerim and Candolim beach stretch and the historic 16th-century Fort Aguada. This puts you right next to the Arabian Sea with beautiful views and direct beach access.
                </p>
            </div>
        """, unsafe_allow_html=True)

        # Tourist Spots Nearby Section
        st.markdown("<h2 class='section-title'>Tourist Spots Nearby</h2>", unsafe_allow_html=True)
        st.markdown("""
            <div class='content'>
                <ul>
                    <li><strong>Fort Aguada:</strong> The 17th-century Portuguese fort, integrated within the resort grounds, is a must-visit for history buffs.</li>
                    <li><strong>Sinquerim Beach and Candolim Beach:</strong> Relax on the pristine golden sands, enjoy water sports, or soak up the vibrant beach scene.</li>
                    <li><strong>Calangute Beach:</strong> Known for its lively atmosphere and bustling markets, this beach is a short distance away.</li>
                    <li><strong>Anjuna Market:</strong> Explore the famous Wednesday Flea Market for souvenirs, handicrafts, and local charm.</li>
                    <li><strong>Aguada Spice Plantation:</strong> Learn about the rich history and cultivation of Goan spices.</li>
                    <li><strong>Old Goa Churches:</strong> Explore the UNESCO World Heritage Site showcasing Goa's colonial past with iconic churches like the Basilica of Bom Jesus.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

        # About the Resort Section
        st.markdown("<h2 class='section-title'>About the Resort</h2>", unsafe_allow_html=True)
        st.markdown("""
            <div class='content'>
                <p>
                    Steeped in history and luxury, Taj Fort Aguada is Goa's first resort and a renowned destination for celebrities and discerning travelers. Here's what awaits you:
                </p>
                <ul>
                    <li><strong>Portuguese-inspired architecture:</strong> Enjoy the elegant charm of the resort's architecture with manicured lawns and a serene ambiance.</li>
                    <li><strong>Airy Rooms and Suites:</strong> Choose from luxuriously appointed rooms and suites, many offering breathtaking sea views and private balconies.</li>
                    <li><strong>World-class Dining:</strong> Indulge in a culinary journey with diverse restaurants like the iconic Paper Moon (Italian), Morisco (seafood), Kokum Kitchen (global cuisine), and SFX (lounge bar).</li>
                    <li><strong>Jiva Spa:</strong> Pamper yourself at the renowned Jiva Spa with a variety of rejuvenating treatments.</li>
                    <li><strong>Outdoor Pool:</strong> Relax by the inviting pool with stunning ocean views.</li>
                    <li><strong>Other Amenities:</strong> Fitness facilities, water sports (may be available seasonally), kids' club, and impeccable Taj hospitality are just a few highlights.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

        # For More Information Section
        st.markdown("<h2 class='section-title'>For More Information</h2>", unsafe_allow_html=True)
        st.markdown("""
            <div class='content links'>
                <p>
                    To learn more about the Taj Fort Aguada Resort & Spa, Goa, you can visit their official website: 
                    <a href="https://www.tajhotels.com/en-in/hotels/taj-fort-aguada-goa" target="_blank">Taj Fort Aguada Resort & Spa Official Website</a>
                </p>
                <p>
                    Here are some additional resources you might find helpful:
                </p>
                <ul>
                    <li><a href="https://www.booking.com/hotel/in/fort-aguada-beach-resort.html" target="_blank">Booking.com</a></li>
                    <li><a href="https://www.tripadvisor.com/Hotels-g297604-zfb11003-Goa-Hotels.html" target="_blank">Tripadvisor Reviews</a></li>
                </ul>
                <p>
                    Remember:
                </p>
                <ul>
                    <li>Prices can vary depending on the season and room type.</li>
                    <li>Check for special offers and packages on the Taj website.</li>
                </ul>
                <p>
                    I hope this helps you plan your luxurious escape to the beautiful Taj Fort Aguada Resort & Spa!
                </p>
            </div>
        """, unsafe_allow_html=True)

    with tab2:
        st.title('Country-Wise Analysis')
        st.write("This section provides an analysis of Taj Fort Aguada Resort & Spa reviews based on country.")

        col1, col2  = st.columns(2)

        # Add content to the first column
        with col1:
            st.subheader('Top 10 Nationalities of Hotel Guests')

            con = dff['country'].value_counts().head(10).reset_index(name='count').rename(columns={'index': 'country'})

            # Plotting the pie chart
            fig = px.pie(con, values='count', names='country', title='Top 10 Countries by Count')
            st.plotly_chart(fig)

        # Add content to the second column

        with col2:
            st.subheader('Top 10 Nationalities by Average Hotel Rating')

            new = dff[['country', 'rating']]
            new = new.groupby('country').agg({'rating': 'mean'}).reset_index().round(1)
            con = dff['country'].value_counts().head(10).index

            # Filter the mean ratings to include only the top 10 countries by count
            new = new[new['country'].isin(con)]
            new = new.sort_values(by='rating', ascending=False)
            fig = px.bar(new, x='country', y='rating', text='rating', labels={'rating': 'Average Rating'})
            fig.update_layout(height=500)
            st.plotly_chart(fig)




        col1,col2=st.columns(2)

        with col1:
            st.subheader('Avergae Stay Night And No.of Tourist')
            high = dff['country'].value_counts()
            high_dict = high.to_dict()
            nigh = dff.groupby('country')['nights'].mean().round(1)
            nigh_dict = nigh.to_dict()
            px.set_mapbox_access_token('YOUR_MAPBOX_ACCESS_TOKEN')
            fig = px.scatter_mapbox(dff, lat='latiude', lon='longitude', hover_name='country',
                                    hover_data={
                                        'No. of Tourist': [high_dict.get(country, '') for country in dff['country']],
                                        'Avg. Stay Night': [nigh_dict.get(country, '') for country in dff['country']]},
                                    mapbox_style="carto-positron",
                                    zoom=1)
            fig.update_traces(hovertemplate="<b>%{hovertext}</b><br>" +
                                            "No. of Tourist: %{customdata[0]}<br>" +
                                            "Avg. Stay Night: %{customdata[1]}<br>")

            fig.update_layout(height=600)
            st.plotly_chart(fig)

        with col2:
            with col2:
                st.subheader('Top Destinations: Discover Where Guests Enjoy the Longest Stays at Our Hotel')
                ok = dff.groupby('country').nights.mean().sort_values(ascending=False).head(10).reset_index(
                    name='Avg. Nights')
                fig=px.bar(ok, x='country', y='Avg. Nights')
                st.plotly_chart(fig)


        st.selectbox('Select Country',sorted(df.country.str.strip().unique().tolist()))





    with tab3:
        st.title('Rating-Wise Analysis')
        st.write("This section provides an analysis of Taj Fort Aguada Resort & Spa reviews based on rating.")
        select=st.selectbox('Select Rating', sorted(dff.rating.unique())).round(0)
        select=int(select)


        total=int(dff[dff.rating == select].count().country)

        col1, col2 = st.columns(2)

        with col1:
            st.metric('Global Participation in Hotel Ratings', select, total)
        with col2:
            total = dff[dff.rating == select].country.count()
            total_night = dff[dff.rating == select].nights.sum()
            avg_stay = (total_night / total).round(1)
            st.metric("Average Stay Duration per Rating Category", select, avg_stay)

        rate_con = dff[dff.rating == select].country.value_counts().reset_index(name='rating').rename(
                    columns={'index': 'country'})

        st.subheader('Countries by Hotel Ratings')
        fig = px.bar(rate_con, x='country', y='rating', text_auto=True)
        fig.update_layout(width=1300, height=700)
        st.plotly_chart(fig)


        col1, col2 = st.columns(2)

        with col1:
            st.subheader('Room Type Preferences Across Guest Ratings')
            ok = dff[dff.rating == select]
            ok = ok.room_types.value_counts().reset_index(name='counts').rename(columns={'index': 'room_types'})
            fig=px.bar(ok, x='room_types', y='counts', text_auto=True)
            st.plotly_chart(fig)



        with col2:
            st.subheader('Total Nights Stayed per Room Type by Guest Ratings')

            rock = dff[dff.rating == select]
            fig =px.sunburst(rock, path=['rating', 'room_types'], values='nights', color='room_types')

            #fig.update_layout(height=500,width=400)
            st.plotly_chart(fig)



    with tab4:
        st.title('Room-Types Analysis')
        st.write("This section provides an analysis of Taj Fort Aguada Resort & Spa reviews based on room types.")

        col1, col2 = st.columns(2)
        with col1:
            st.subheader('custumer booked room type')
            room_type = dff['room_types'].value_counts().reset_index(name='count').rename(columns={'index': 'room_type'})
            fig = px.pie(room_type, values='count', names='room_types')
            st.plotly_chart(fig)

        with col2:
            st.subheader('sum of booked night')
            night = dff.groupby('room_types').nights.sum().reset_index(name='total night').rename(
                columns={'index': 'room types'})
            fig = px.bar(night, x='room_types', y='total night', text_auto=True)
            st.plotly_chart(fig)

        st.title('ROOMS TYPES METRIC - RATING')

        col1, col2, col3, col4,col5= st.columns(5)
        mean = dff.groupby('room_types').rating.mean().reset_index()

        with col1:
            st.metric( mean.room_types.iloc[0],  mean.rating.iloc[0].round(2))

        with col2:
            st.metric(mean.room_types.iloc[1], mean.rating.iloc[1].round(2))
        with col3:
            st.metric(mean.room_types.iloc[2], mean.rating.iloc[2].round(2))
        with col4:
            st.metric(mean.room_types.iloc[3], mean.rating.iloc[3].round(2))
        with col5:
            st.metric(mean.room_types.iloc[4], mean.rating.iloc[4].round(2))



        col1, col2, col3, col4, col5 = st.columns(5)
        mean = dff.groupby('room_types').rating.mean().reset_index()

        with col1:
            st.metric(mean.room_types.iloc[5], mean.rating.iloc[5].round(2))

        with col2:
            st.metric(mean.room_types.iloc[6], mean.rating.iloc[6].round(2))
        with col3:
            st.metric(mean.room_types.iloc[7], mean.rating.iloc[7].round(2))
        with col4:
            st.metric(mean.room_types.iloc[8], mean.rating.iloc[8].round(2))
        with col5:
            st.metric(mean.room_types.iloc[9], mean.rating.iloc[9].round(2))




        col1, col2, col3, col4= st.columns(4)
        mean = dff.groupby('room_types').rating.mean().reset_index()

        with col1:
            st.metric(mean.room_types.iloc[10], mean.rating.iloc[10].round(2))

        with col2:
            st.metric(mean.room_types.iloc[11], mean.rating.iloc[11].round(2))
        with col3:
            st.metric(mean.room_types.iloc[12], mean.rating.iloc[12].round(2))
        with col4:
            st.metric(mean.room_types.iloc[13], mean.rating.iloc[13].round(2))








    with tab5:
        st.title('Booked_Wise Analysis')
        st.write("This section provides an analysis of Taj Fort Aguada Resort & Spa reviews based on booked.")

        year = st.selectbox('select year', sorted(dff.booked_year.unique()))

        col1, col2 = st.columns(2)

        with col1:
            st.subheader('room types ')
            filtered_df = dff[dff.booked_year == year]
            top_year = filtered_df['room_types'].value_counts()
            top_year = top_year.reset_index(name='COUNTS').rename(columns={'index': 'ROOM_TYPES'})
            fig = px.bar(top_year, x='room_types', y='COUNTS', text_auto=True, log_y=True)
            st.plotly_chart(fig)

        with col2:
            st.subheader('traveller types ')
            filtered_df = dff[dff.booked_year == year]
            traveler_type = filtered_df['traveler_type'].value_counts()
            traveler_type = traveler_type.reset_index(name='COUNTS').rename(columns={'index': 'traveler_type'})
            fig = px.bar(traveler_type, x='traveler_type', y='COUNTS', text_auto=True, log_y=True)
            st.plotly_chart(fig)

        st.subheader('Top country visitors')
        filtered_df = dff[dff.booked_year == year]
        top_year = filtered_df.country.value_counts()
        top_year = top_year.reset_index(name='counts').rename(columns={'index': 'country'})
        fig = px.bar(top_year, x='country', y='counts', text_auto=True,width=1350, height=500)
        st.plotly_chart(fig)




        st.subheader('Room Type With Total Nights')
        pivot_table = dff.pivot_table(index='booked_year', columns='room_types', values='nights', aggfunc='sum')
        pivot_table = dff.pivot_table(index='booked_year', columns='room_types', values='nights', aggfunc='sum')
        # Rename the columns if necessary
        pivot_table = pivot_table.rename(columns=lambda x: f'Total Night - {x}')
        # Convert pivot table to long format for plotly
        long_df = pivot_table.reset_index().melt(id_vars='booked_year', var_name='room_types', value_name='Total Night')
        # Create the bar plot
        fig = px.bar(long_df, x='booked_year', y='Total Night', color='room_types', barmode='group', text_auto=True,log_y=True, width=1350, height=500)
        st.plotly_chart(fig)




        # MONTH ANALYSIS

        st.title('MONTH WISE ANALYSIS')
        month_order = [
            'January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December', 'Unknown'
        ]
        select_month = st.selectbox('select year', month_order)


        filtered_df = dff[(dff['booked_year'] == year) & (dff['booked_month'] == select_month)]

        col1, col2 = st.columns(2)

        with col1:
            st.subheader(f'Room Types in  - {select_month}')

            top_year = filtered_df['room_types'].value_counts()
            top_year = top_year.reset_index(name='COUNTS').rename(columns={'index': 'ROOM_TYPES'})
            fig = px.bar(top_year, x='room_types', y='COUNTS', text_auto=True, log_y=True)
            st.plotly_chart(fig)





        with col2:
            st.subheader(f'Traveller Type in  - {select_month}')

            traveler_type = filtered_df['traveler_type'].value_counts()
            traveler_type = traveler_type.reset_index(name='COUNTS').rename(columns={'index': 'traveler_type'})
            fig = px.bar(traveler_type, x='traveler_type', y='COUNTS', text_auto=True, log_y=True)
            st.plotly_chart(fig)

        st.subheader(f'Top country visitors in  - {select_month}')
        top_year = filtered_df.country.value_counts()
        top_year = top_year.reset_index(name='counts').rename(columns={'index': 'country'})
        fig = px.bar(top_year, x='country', y='counts', text_auto=True,width=1350, height=500)
        st.plotly_chart(fig)

        line = dff[dff.booked_year == year].booked_month.value_counts().reset_index(name='count').rename(
            columns={'index': 'Months'})
        fig=px.line(line,x='booked_month',y='count')
        st.plotly_chart(fig)



if option == 'Seashell Suites and Villas':
    load_Seashell()
elif option == 'Taj Fort Aguada Resort & Spa':
    load_taj_fort()
else:
    load_home_page()