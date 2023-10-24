import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
st.set_page_config(layout="wide")
st.sidebar.title('Navigation')
page = st.sidebar.radio("Go to", ('Home', 'Creative Entreprenuers', 'Barriers', 'Space Needs'))

class Homepage:

    def load_data():
        # Load the data
        path = "./2023-cleaned-survey.xlsx"
        df = pd.read_excel(path)

        return df

    def plot_gender(df):
        # Processing the gender column
        genders = {
            'Prefer not to say': 'N/A',
            'Female': 'F',
            'Male': 'M',
            'Non-binary': 'NB',
        }

        df['Identified Gender'] = df['Identified Gender'].replace(genders)
        df['Identified Gender'] = pd.Categorical(df['Identified Gender'], categories=['N/A', 'F', 'M', 'NB'])


        #plot
        plt.figure(figsize=(10, 5))
        sns.countplot(data=df, x=df['Identified Gender'], color='skyblue')
        plt.title('Distribution of Gender', fontsize=35)
        plt.xlabel('Gender')
        plt.yticks(np.arange(0, 110, 10))
        plt.ylabel('Number of Participants')
        st.pyplot(plt.gcf())

        st.markdown("""The chart showcases the gender distribution among survey participants, highlighting categories such as N/A, F (Female), M (Male), and NB (Non-Binary). Despite some differences in the counts, each gender category is fairly represented. While the "N/A" category leads in numbers, both "M" and "NB" have comparable counts, with "F" being slightly less represented, yet still substantially included. Overall, the distribution remains fairly even across the board.""")

    def plot_age(df):
        age_ranges = {
        'Older Adults (Age 65+)': '65+',
        'Children/Youth (Age 0-18)': '0-18',
        'Adults (Age 25-64)': '25-64',
        'Prefer not to say': 'N/A',
        'Young Adults (Age 19-24)': '19-24'
        }

        df['Age'] = df['Age'].replace(age_ranges)
        df['Age'] = pd.Categorical(df['Age'], categories=['0-18', '19-24', '25-64', '65+', 'N/A'], ordered=True)


        #plot
        plt.figure(figsize=(10, 5))
        sns.countplot(data=df, x=df['Age'], color='skyblue')
        plt.title('Distribution of Age', fontsize=35)
        plt.xlabel('Age')
        plt.ylabel('Number of Participants')
        st.pyplot(plt.gcf())
        st.markdown("""The chart depicts the age distribution of survey participants, highlighting age brackets such as 0-18, 19-24, 25-64, 65+, and N/A. Despite some variations, each age category is fairly represented. The 25-64 age bracket has the most participants, whereas the 0-18 and N/A groups display comparable and slightly lesser counts. Overall, the distribution maintains a balanced representation across different age groups.""")

    def plot_race(df):
        df['Select Your Race/Ethnicity'] = df['Select Your Race/Ethnicity'].replace({
        'Hispanic or Latinx': 'Hispanic/Latinx',
        'Native Hawaiian or Other Pacific Islander': 'Pacific Islander',
        'Black or African American': 'Black/African American', 
        'Prefer not to say': "None"
        })

        #plot
        plt.figure(figsize=(10, 5))
        sns.countplot(data=df, y='Select Your Race/Ethnicity', color='skyblue', orient='h', order=df['Select Your Race/Ethnicity'].value_counts().index)
        plt.title('Distribution of Race/Ethnicity', fontsize=30)
        plt.xlabel('Number of Participants')
        plt.ylabel('Race/Ethnicity')
        plt.xticks(np.arange(0, 51, 2))
        st.pyplot(plt.gcf())

        st.markdown("""The chart illustrates the distribution of race/ethnicity among survey participants. The representation of Hispanic/Latinx, Black/African American, White, None, and Other is fairly even. Overall, the survey showcases a balanced distribution across different racial and ethnic backgrounds.""")
    def plot_location(df):
        plt.figure(figsize=(10, 5))
        sns.countplot(data=df, x='Describe Your Location', color='skyblue')
        plt.title('Distribution of Location Types', fontsize=30)
        plt.xlabel('Location Types')
        plt.ylabel('Number of Participants')
        st.pyplot(plt.gcf())

        st.markdown("""The chart displays a fairly even distribution of location types among survey participants. While Urban areas have a slight edge, Suburban and Rural areas are closely matched in representation, indicating a well-balanced input across all location types.""")

    def plot_responses(df):
        primary_fields = {
        'Creative Worker (In-house graphic designers, copywriters, art directors employed at a business working in the creative industries)': 'Creative Worker',
        'Arts Administrator (Theater managers, development staff, executive directors, program coordinators at an arts-based business usually a non-profit, e.g., at a museum, symphony, theater, etc.)': 'Arts Administrator',
        'Arts Funder (Foundations; national, state, and local arts agencies)': 'Arts Funder',
        'Business Professional (Attorneys, bankers, CPAs, other professionals working in small to large businesses outside of the creative industries)': 'Business Professional',
        'Civic and/or Social Service Worker (Social worker, government employee, NGO working outside the arts)': 'Civic/Social Service Worker',
        'Creative Entrepreneurs (Artists, performers, makers, creatives of all disciplines, self-employed)': 'Creative Entrepreneur',
        'Arts Educator or Teaching Artist (Art teachers, music teachers, teaching artists, dance teachers, visiting artists)': 'Arts Educator/Teaching Artist'
        }

        df['Describe Your Primary Role in Creative Sector'] = df['Describe Your Primary Role in Creative Sector'].replace(primary_fields)

        plt.figure(figsize=(50, 15))
        plot = sns.countplot(data=df, x='Describe Your Primary Role in Creative Sector', orient='h', color="skyblue")
        plt.title('Distribution of Primary Role in Creative Sector', fontsize=60)
        plt.xlabel('Primary Role in Creative Sector', fontsize=50)
        plt.ylabel('Number of Participants', fontsize=50)
        plt.xticks(fontsize=30)

        st.pyplot(plt.gcf())

    def heatmap(df):
        membership_populations = {
        'K-12 Students': 'K-12 Students',
        'Individuals living in neighborhoods with limited access to the arts': 'Limited Access to Arts',
        'New Americans (immigrants and refugees)*': 'New Americans',
        'Military Veterans/Active Duty Personnel': 'Military',
        'Individuals with disabilities': 'Disabled',
        'Individual who is currently incarcerated': 'Incarcerated',
        'Individuals with Limited English Proficiency': 'Limited English Proficiency',
        'LGBTQI+ Individuals': 'LGBTQI+',
        'Prefer not to say': "None",
        'Individuals living in hospitals': 'Hospitalized',
        'People of Color (American Indian/Alaska Native': 'People of Color'
        }

        df['Identify Membership in Given Populations'] = df['Identify Membership in Given Populations'].replace(membership_populations)

        #plot
        plt.figure(figsize=(3,60))
        
        
        pivot_table = pd.pivot_table(df, index='Describe Your Primary Role in Creative Sector', aggfunc=lambda x: x.notnull().sum())
        pivot_table = pivot_table.T # swap x and y axis
        sns.heatmap(pivot_table, cmap='Reds', annot=True, fmt='g')
        plt.xlabel('Roles', fontsize=50) # swap x and y axis labels
        plt.ylabel('Questions', fontsize=50)

        plt.yticks(fontsize=12)
        plt.xticks(fontsize=12)
        st.pyplot(plt.gcf())

        st.markdown("""As you can see from the heat map above, the questions being answered within this survey is very depended on the roles of the respondents. This is because the survey asked each role different sets of questions. 
                        
                        """)
    def builder():
        # Main Page Heading
        st.title("Creative Community Insights: Nashville")
        
        # Introduction
        st.write("""
        Welcome to the Creative Community Insights platform, developed in partnership with a dedicated non-profit organization in Nashville that prioritizes the welfare and happiness of the creative community.
        """)
        
        # Background Information
        st.header("Background")
        st.write("""
        This non-profit company reached out with the intention of delving deeper into the voices of the creative community. They conducted a comprehensive survey targeting various roles within this vibrant industry. The goal was simple but significant: to gain insights from this data to foster an even more supportive environment for every creative soul in Nashville.
        """)
        
        # Features
        st.header("Features")
        st.markdown("""
        - **Data Analysis & Cleaning:** We've ensured the data from the survey is both accurate and relevant, removing any noise that could lead to misleading conclusions.
        - **Interactive UI:** Here, you can experience the survey results in this interactive, user-friendly graphical interface. 
        - **Insightful Questions Answered:** For more insightful analysis, we've delved deep into the data using Jupyter Notebooks, bringing forward insightful answers that can pave the way for impactful decision-making.You can access these notebooks in this [repository](https://github.com/dsi-principles-prog-F2023/ai_midterm-team/tree/main)
        """)

        

        
        df = Homepage.load_data()
        
        st.title('Demographics Breakdown')
        st.markdown("""
        Here, you can view the demographics of the survey respondents. You can go ahead by selecting the appropriate demographic breakdown for this survey.
        """)
        # Dropdown for demographic selection
        options = ['Gender', 'Age', 'Race/Ethnicity', 'Location']
        selection = st.selectbox('Select a Demographic to View:', options)

        # Display the appropriate plot based on selection
        if selection == 'Gender':
            Homepage.plot_gender(df)
        elif selection == 'Age':
            Homepage.plot_age(df)
        elif selection == 'Race/Ethnicity':
            Homepage.plot_race(df)
        elif selection == 'Location':
            Homepage.plot_location(df)

        st.title('Roles of Respondents')
        st.markdown("""Here, you can view the roles of the survey respondents.""")
        Homepage.plot_responses(df)
        st.markdown("""
        As shown in the graph above. The creative roles responded to this survey include: Creative Worker, Arts Administrator, Arts Funder, Business Professional, Civic/Social Worker, Creative Entrepreneur, and Arts Educator/Teaching Artist. There are 50 respondants for each creative roles in this survey, this is because the survey was designed to have 50 respondants for each creative roles.
                    

        """)

        st.markdown("""To see what questions each role responded to within the survey, click the button to veiw a detailed heatmap [wait for 5 seconds]: """)
        show_plot = st.button("Show Plot")
        if show_plot:
            Homepage.heatmap(df)

        st.markdown("<div style='text-align: right'>Data Scientists:  </div>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: right'>Sarah Auch, Aryaan Upadhyay, Zheling Zhang, Chong Zhao</div>", unsafe_allow_html=True)

class Creative:

    @staticmethod
    def creative_UI():
        df = pd.read_excel("./2023-cleaned-survey.xlsx")
        column_names = df.columns

        st.title("Creative Entrepreneurs")
        st.markdown("The following section of the dashboard has been developed to help the audience get a better insight about the creative respondents of the survey")
        st.write("From the dropdown below please choose one of the 4 options to better understand the respondents' creativity!")

        options = st.selectbox("Choose an option:", [
            "Figure for types of creative practice", 
            "Figure for years of creative practice experience",
            "Percentage of income from various sources", 
            "Pre/post COVID annual income, typical annual income from creative practice"
        ])

        if options == "Figure for types of creative practice":
            Creative.plot_creative_roles_distribution(df)
        elif options == "Figure for years of creative practice experience":
            Creative.figure_for_years_of_creative_existence(df)
        elif options == "Percentage of income from various sources":
            Creative.percentage_of_income(df)
        elif options == "Pre/post COVID annual income, typical annual income from creative practice":
                Creative.pre_vs_post(df)

    @staticmethod
    def plot_creative_roles_distribution(dataframe):
        df = pd.read_excel("./2023-cleaned-survey.xlsx")
        st.header("Distribution of creative activities in primary sector")
                                
        st.text("\n")
            
        st.markdown("This is a graph which shows the distribution of creative activities that the respondents take part in")
        st.text("\n")

        category_dict = {
            'Comedy': 'Performing Arts',
            'Calligraphy': 'Visual Arts',
            'Pottery': 'Crafts',
            'Ceramics': 'Crafts',
            'Crafts': 'Crafts',
            'Magic': 'Performing Arts',
            'Glass Blowing': 'Crafts',
            'Puppetry': 'Performing Arts',
            'Woodworking': 'Crafts',
            'Mime': 'Performing Arts',
            'Dance Choreography': 'Performing Arts',
            'Singing': 'Music',
            'Performance Art': 'Performing Arts',
            'Poetry': 'Literary Arts',
            'Printmaking': 'Visual Arts',
            'Metalworking': 'Crafts',
            'Theater': 'Performing Arts',
            'Fashion Design': 'Fashion',
            'Culinary Arts': 'Culinary Arts',
            'Art Curation': 'Visual Arts',
            'Graffiti': 'Visual Arts',
            'Digital Art': 'Media Arts',
            'Art Teaching': 'Education',
            'Photography': 'Visual Arts',
            'Graphic Design': 'Media Arts',
            'Dance': 'Performing Arts',
            'Textile Art': 'Crafts',
            'Web Design': 'Media Arts',
            'Installation Art': 'Visual Arts',
            'Mixed Media Art': 'Visual Arts',
            'Drawing': 'Visual Arts',
            'Sculpting': 'Visual Arts',
            'Painting': 'Visual Arts',
            'Music Production': 'Music',
            'Acting': 'Performing Arts',
            'Jewelry Making': 'Crafts',
            'Video Art': 'Media Arts',
            'Illustration': 'Visual Arts',
            'Film Making': 'Media Arts',
            'Street Art': 'Visual Arts',
            'Stand-up Comedy': 'Performing Arts',
            'Animation': 'Media Arts',
            'Writing': 'Literary Arts',
            'Game Design': 'Media Arts'
        }

        df['Primary Creative Activity'] = df['Primary Creative Activity'].replace(category_dict)

        fig, ax = plt.subplots(figsize=(18, 14))

            # Plotting on the 'ax' object
        df['Primary Creative Activity'].value_counts().plot(kind='barh', color='lightcoral', ax=ax)
        ax.set_title("Distribution of Primary Creative Activities")
        ax.set_xlabel("Count")
        ax.set_ylabel("Creative Activity")
        ax.invert_yaxis()  # To display the bar with the highest count at the top

        st.pyplot(fig)
            

            
        st.markdown("""
    <style>
        .justify-text {
            text-align: justify;
        }
    </style>
    <div class="justify-text">
        The bar chart showcases the distribution of primary creative activities among all the roles in this survey. "Visual Arts" is the most predominant activity, with the highest count nearing 25 individuals, followed by "Performing Arts." Other categories, such as "Music," "Literary Arts," "Education," "Fashion," and "Culinary Arts," have relatively fewer participants, each with counts less than 10.
    </div>
""", unsafe_allow_html=True)


    @staticmethod
    def figure_for_years_of_creative_existence(dataframe):
        df = pd.read_excel("./2023-cleaned-survey.xlsx")
        st.header("Distribution of experience in creative practice")
        
        fig, ax = plt.subplots(figsize=(15, 8))

        # Plotting on the 'ax' object
        df['Years of Professional Creative Practice'].value_counts().plot(kind='barh', color='mediumseagreen', ax=ax)
        ax.set_title("Distribution of Years of Professional Creative Practice")
        ax.set_xlabel("Count")
        ax.set_ylabel("Years of Practice")
        ax.invert_yaxis()  # To display the bar with the highest count at the top

        st.pyplot(fig)
        
        st.text("\n")
        
        
        st.markdown("""
    <style>
        .justify-text {
            text-align: justify;
        }
    </style>
    <div class="justify-text">
        The presented graph provides an in-depth examination of the years of professional creative practice reported by the respondents. 
        This visualization captures the journey of creative professionals, emphasizing the spectrum of experience they bring to the table. 
        Categories range from those just beginning their artistic journey with "0-2 years" to seasoned experts boasting "20+ years" in the field. 
        Notably, a significant number of respondents fall within the "3-5 years" bracket, indicating a cluster of emerging professionals. 
        On the other hand, the representation of those with "10-14 years" and "15-19 years" of experience showcases the depth and continuity of 
        creative endeavors in the community.
    """, unsafe_allow_html=True)
            

    @staticmethod
    def percentage_of_income(dataframe):
        df = pd.read_excel("./2023-cleaned-survey.xlsx")
        st.header("Percentage of income from various sources")
        
        
            
        st.markdown("This is a graph which showcases the percentage of income from various sources")
        
        # Filter columns that contain the word "income"
        income_columns = [col for col in df.columns if "income" in col.lower()]
        
        # Columns related to percentage of income sources
        income_source_columns = income_columns[4:]

        # Define colors for each box in the boxplot
        colors = ['red', 'blue', 'green', 'yellow', 'cyan', 'magenta']

        # Plotting
        fig, ax = plt.subplots(figsize=(15, 8))

        # Plotting the boxplot for income source columns with specified colors
        bp = df[income_source_columns].boxplot(vert=False, ax=ax, patch_artist=True, return_type='dict')

        # Coloring each box
        for patch, color in zip(bp['boxes'], colors):
            patch.set_facecolor(color)

        # Title and labels
        ax.set_title("Distribution of Percentage of Income from Various Sources", fontsize=16)
        ax.set_xlabel("Percentage", fontsize=14)
        ax.set_ylabel("Income Source", fontsize=14)
        ax.grid(False)
        # Adjust x-axis ticks, format for clarity, and set limit
        ax.xaxis.set_tick_params(labelsize=12)
        ax.xaxis.set_major_locator(plt.MaxNLocator(10))  # Limit the number of ticks for better visibility

        # Set x-axis limit to 1.6%
        ax.set_xlim(0, 1.6)

        # Format tick labels as percentages
        labels = ['{:.1f}%'.format(val) for val in ax.get_xticks()]
        ax.set_xticklabels(labels)

        plt.tight_layout()
        
        

        st.pyplot(fig)
        
        
        st.markdown("""
    <style>
        .justify-text {
            text-align: justify;
        }
        .bold-text {
            font-weight: bold;
        }
    </style>
    <div class="justify-text">
        <p>
            This boxplot provides insights into the distribution of income percentages from various sources among survey respondents. Key features of the visualization include:
        </p>
        <ul>
            <li>Each <span class="bold-text">horizontal box</span> denotes the interquartile range (IQR) for an income source. The median is represented by a line inside each box.</li>
            <li>Whiskers extend to indicate data within <span class="bold-text">1.5 times the IQR</span>. Data points outside the whiskers are outliers.</li>
            <li>The x-axis, which represents income percentages, is limited to <span class="bold-text">1.6%</span>, focusing on the main data distribution.</li>
        </ul>
        <p>
            Income sources are color-coded as follows:
        </p>
        <ul>
            <li><span style="color:red" class="bold-text">Red</span>: Full-time artistic employment</li>
            <li><span style="color:blue" class="bold-text">Blue</span>: Part-time artistic employment</li>
            <li><span style="color:green" class="bold-text">Green</span>: Freelance/contract artistic work</li>
            <li><span style="color:yellow" class="bold-text">Yellow</span>: Full-time non-artistic employment</li>
            <li><span style="color:cyan" class="bold-text">Cyan</span>: Part-time non-artistic employment</li>
            <li><span style="color:magenta" class="bold-text">Magenta</span>: Non-artistic freelance/contract work</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

    @staticmethod
    def pre_vs_post(dataframe):
        df = pd.read_excel("./2023-cleaned-survey.xlsx")
        st.header("Annual income pre and post covid for creative workers")
                
        st.markdown("This is a graph which showcases the respondent's income pre and post covid")

        # Melt the data to long format
        df_melt = df.melt(value_vars=['Income Details BEFORE COVID-19 Typical annual income from artistic/creative practice', 'Income Details POST COVID-19 RESTRICTIONS (2022) Annual income from artistic/creative practice'], var_name='Income Details')

        # Plot the data using a horizontal bar chart with hue
        sns.countplot(y='value', hue='Income Details', data=df_melt)

        # Set the y-axis label
        plt.ylabel('Typical annual income from artistic/creative practice')
        legend = ['Before', 'After']
        plt.legend(legend, loc='upper right')
        # Show the plot

        plt.tight_layout()

        st.pyplot(plt.gcf())
        
        st.text("\n")
        

        st.markdown("""
    <style>
        .justify-text {
            text-align: justify;
        }
    </style>
    <div class="justify-text">
        The bar chart visualizes the distribution of individuals' typical annual income from artistic/creative practice, both before and after a certain event or change. The income brackets range from "$0 – 10,000" to "$75,001 or above." Notably, after the event, there's a significant increase in the number of individuals earning "$25,001 – 50,000" and a noticeable decrease in the "$0 – 10,000" range, suggesting an overall improvement in income for the surveyed group.
    </div>
""", unsafe_allow_html=True)

class Space:
    def load_data():
        df = pd.read_excel('./2023-cleaned-survey.xlsx')
        return df

    def plot_space_needs_for_AE_TA(df):
        ae_ta_df = df[df['Describe Your Primary Role in Creative Sector'] == 'Arts Educator or Teaching Artist (Art teachers, music teachers, teaching artists, dance teachers, visiting artists)']
        current_space = 'What type of space do you mainly use for your creative work?'
        
        fig, ax = plt.subplots()
        ax.barh(ae_ta_df[current_space].value_counts().index, ae_ta_df['What type of space do you mainly use for your creative work?'].value_counts().values)
        ax.set_ylabel('Type of Space')
        ax.set_xlabel('Count')
        ax.grid(axis='y', alpha=0.5)
        ax.set_title('Space Needs Identified by Teaching Artists/Educators')
        
        st.pyplot(fig)

    def plot_space_needs_for_CE(df):
        ce_df = df[df['Describe Your Primary Role in Creative Sector'] == 'Creative Entrepreneurs (Artists, performers, makers, creatives of all disciplines, self-employed)']
        current_space = 'What type of space do you mainly use for your creative work?'
        fig, ax = plt.subplots()
        ax.barh(ce_df[current_space].value_counts().index,ce_df[current_space].value_counts().values)
        ax.set_ylabel('Type of Space')
        ax.set_xlabel('Count')
        ax.grid(axis='y', alpha=0.5)
        ax.set_title('Space Needs Identified by Teaching Artists/Educators')
        
        
        st.pyplot(fig)

    def plot_space_needs_for_AA(df):
        aa_df = df[df['Describe Your Primary Role in Creative Sector'] == 'Arts Administrator (Theater managers, development staff, executive directors, program coordinators at an arts-based business usually a non-profit, e.g., at a museum, symphony, theater, etc.)']
        colaborating_col = "How important are the following space types/amenities to your creative practice or business? Collaboration/networking events"
        spaces = 'How important are the following space types/amenities to your creative practice or business? Photography studio/dark room'
        space_or_amenity_columns = [col for col in aa_df.columns if 'how important' in col.lower()]
        value_mapping = {
            "Not at all important": 1,
            "Nice to have but not important": 2,
            "Somewhat important": 3,
            "Critically important": 4
        }

        for col in space_or_amenity_columns:
            aa_df[col] = aa_df[col].replace(value_mapping)

        aa_df = aa_df.dropna(subset=space_or_amenity_columns)

        melted_df = aa_df.melt(id_vars=[colaborating_col], value_vars=space_or_amenity_columns, var_name='Amenity', value_name='Rating')

        amenity_list = []
        for i in space_or_amenity_columns:
            word_list = i.split()
            index = word_list.index('business?')
            rest_of_string = ' '.join(word_list[index+1:])
            amenity_list.append(rest_of_string)

        sns.set_style('whitegrid')
        sns.set_palette('husl')
        sns.set(rc={'figure.figsize':(12,8)})

        fig, ax = plt.subplots()
        sns.histplot(data=melted_df, y='Amenity', hue='Rating', multiple='stack', ax=ax)
        ax.set_title('Importance of Amenities for Arts Administrators')
        ax.set_xlabel('Frequency')
        ax.set_ylabel('Amenity')
        ax.set_yticklabels(amenity_list)
        st.pyplot(fig)

    def plot_space_needs_for_CW(df):
        cw_df = df[df['Describe Your Primary Role in Creative Sector'] == 'Creative Worker (In-house graphic designers, copywriters, art directors employed at a business working in the creative industries)']
        colaborating_col = "How important are the following space types/amenities to your creative practice or business? Collaboration/networking events"
        spaces = 'How important are the following space types/amenities to your creative practice or business? Photography studio/dark room'
        space_or_amenity_columns = [col for col in cw_df.columns if 'how important' in col.lower()]
        value_mapping = {
            "Not at all important": 1,
            "Nice to have but not important": 2,
            "Somewhat important": 3,
            "Critically important": 4
        }

        for col in space_or_amenity_columns:
            cw_df[col] = cw_df[col].replace(value_mapping)

        cw_df = cw_df.dropna(subset=space_or_amenity_columns)

        melted_df = cw_df.melt(id_vars=[colaborating_col], value_vars=space_or_amenity_columns, var_name='Amenity', value_name='Rating')

        amenity_list = []
        for i in space_or_amenity_columns:
            word_list = i.split()
            index = word_list.index('business?')
            rest_of_string = ' '.join(word_list[index+1:])
            amenity_list.append(rest_of_string)

        sns.set_style('whitegrid')
        sns.set_palette('husl')
        sns.set(rc={'figure.figsize':(12,8)})

        fig, ax = plt.subplots()
        sns.histplot(data=melted_df, y='Amenity', hue='Rating', multiple='stack', ax=ax)
        ax.set_title('Importance of Amenities for Creative Workers')
        ax.set_xlabel('Frequency')
        ax.set_ylabel('Amenity')
        ax.set_yticklabels(amenity_list)
        st.pyplot(fig)

    def plot_future_space_needs_of_amenity_ce(df):
        ce_df = df[df['Describe Your Primary Role in Creative Sector'] == 'Creative Entrepreneurs (Artists, performers, makers, creatives of all disciplines, self-employed)']
        photo_studio_col = 'Rate the importance of each amenity when considering a move to a new space Photography studio'
        amenity_columns = [col for col in ce_df.columns if 'amenity' in col.lower()]

        value_mapping = {
            "Not at all important": 1,
            "Nice to have but not important": 2,
            "Somewhat important": 3,
            "Critically important": 4
        }

        for col in amenity_columns:
            ce_df[col] = ce_df[col].replace(value_mapping)

        ce_df = ce_df.dropna(subset=amenity_columns)

        melted_df = ce_df.melt(id_vars=[photo_studio_col], value_vars=amenity_columns, var_name='Amenity', value_name='Rating')

        amenity_list = []
        for i in amenity_columns:
            word_list = i.split()
            index = word_list.index('space')
            rest_of_string = ' '.join(word_list[index+1:])
            amenity_list.append(rest_of_string)

        sns.set_style('whitegrid')
        sns.set_palette('husl')
        sns.set(rc={'figure.figsize':(12,8)})

        fig, ax = plt.subplots()
        sns.histplot(data=melted_df, y='Amenity', hue='Rating', multiple='stack', ax=ax)
        ax.set_title('Importance of Amenities for Creative Entrepreneurs for Future Space')
        ax.set_xlabel('Frequency')
        ax.set_ylabel('Amenity')
        ax.set_yticklabels(amenity_list)
        st.pyplot(fig)

    def plot_future_space_needs_of_amenity_ta(df):

        ta_df = df[df['Describe Your Primary Role in Creative Sector'] == 'Arts Educator or Teaching Artist (Art teachers, music teachers, teaching artists, dance teachers, visiting artists)']
        photo_studio_col = 'Rate the importance of each amenity when considering a move to a new space Photography studio'
        amenity_columns = [col for col in ta_df.columns if 'amenity' in col.lower()]

        value_mapping = {
            "Not at all important": 1,
            "Nice to have but not important": 2,
            "Somewhat important": 3,
            "Critically important": 4
        }

        for col in amenity_columns:
            ta_df[col] = ta_df[col].replace(value_mapping)

        ta_df = ta_df.dropna(subset=amenity_columns)

        melted_df = ta_df.melt(id_vars=[photo_studio_col], value_vars=amenity_columns, var_name='Amenity', value_name='Rating')

        amenity_list = []
        for i in amenity_columns:
            word_list = i.split()
            index = word_list.index('space')
            rest_of_string = ' '.join(word_list[index+1:])
            amenity_list.append(rest_of_string)

        sns.set_style('whitegrid')
        sns.set_palette('husl')
        sns.set(rc={'figure.figsize':(12,8)})

        fig, ax = plt.subplots()
        sns.histplot(data=melted_df, y='Amenity', hue='Rating', multiple='stack', ax=ax)
        ax.set_title('Importance of Amenities for Teaching Artists/Educators for Future Space')
        ax.set_xlabel('Frequency')
        ax.set_ylabel('Amenity')
        ax.set_yticklabels(amenity_list)
        st.pyplot(fig)

    def plot_future_space_needs_of_amenity_aa(df):
        #The categorization dictionary is interpretated by AI and cross checked by the project team.
        categoried_dictionary = {
            'Member Discounts': 'Special Services',
            'Mail and Package Handling Services': 'Facilities and Infrastructure',
            'Reception Services': 'Facilities and Infrastructure',
            'Flexible Membership Plans': 'Facilities and Infrastructure',
            'Collaboration and networking opportunities': 'Work Environment and Productivity',
            'Mentorship Programs': 'Networking and Community',
            'Member-driven workshops and seminars': 'Networking and Community',
            'Air Conditioning and Heating': 'Facilities and Infrastructure',
            'Kitchen and coffee facilities': 'Facilities and Infrastructure',
            'Fitness Center/Wellness Programs': 'Special Services',
            'Outdoor Space': 'Facilities and Infrastructure',
            'Private Meeting Rooms': 'Facilities and Infrastructure',
            'Secure storage lockers': 'Facilities and Infrastructure',
            'Phone Booths': 'Facilities and Infrastructure',
            'Conference Rooms': 'Facilities and Infrastructure',
            'Access to printing and scanning facilities': 'Facilities and Infrastructure',
            'Clean Restrooms': 'Facilities and Infrastructure',
            'Dedicated Desks': 'Facilities and Infrastructure',
            'Ergonomic Furniture': 'Facilities and Infrastructure',
            'Ample Lighting': 'Facilities and Infrastructure',
            'Event Spaces': 'Facilities and Infrastructure',
            'Pet-friendly policies': 'Facilities and Infrastructure',
            'High-Speed Internet': 'Facilities and Infrastructure',
            'Projector and Screen': 'Facilities and Infrastructure',
            'Lounge and relaxation areas': 'Facilities and Infrastructure',
            '24/7 Access': 'Facilities and Infrastructure',
            'Mail and package handling': 'Facilities and Infrastructure',
            'Event and workshop hosting opportunities': 'Facilities and Infrastructure',
            'Kitchen Facilities': 'Facilities and Infrastructure',
            'On-Site Cafe': 'Facilities and Infrastructure',
            'Ergonomic furniture': 'Facilities and Infrastructure',
            'Comfortable Seating': 'Facilities and Infrastructure',
            'On-site support and maintenance services': 'Facilities and Infrastructure',
            'On-site tech support': 'Facilities and Infrastructure',
            'Affordable and competitive pricing': 'Facilities and Infrastructure',
            'Mail and Package Handling': 'Facilities and Infrastructure',
            'Gallery Space for Exhibiting': 'Facilities and Infrastructure',
            'Collaborative Environment': 'Work Environment and Productivity',
            'Diverse and Comfortable Workspaces': 'Work Environment and Productivity',
            'Friendly Community': 'Networking and Community',
            'Storage Space': 'Facilities and Infrastructure',
            'Printing Services': 'Facilities and Infrastructure',
            'Diverse and inclusive environment': 'Comfort and Inclusivity',
            'Fitness Center': 'Special Services',
            'Affordable Rent': 'Facilities and Infrastructure',
            'On-Site Technical Support': 'Facilities and Infrastructure',
            'Bike storage and shower facilities': 'Facilities and Infrastructure',
            'Wheelchair Accessibility': 'Facilities and Infrastructure',
            'Accessible Location': 'Facilities and Infrastructure',
            'Printer and scanner access': 'Facilities and Infrastructure',
            'Security Cameras': 'Facilities and Infrastructure',
            'Networking Opportunities': 'Networking and Community',
            'Collaboration Spaces': 'Work Environment and Productivity',
            'Recreational Facilities': 'Facilities and Infrastructure',
            'Printing and Copying Services': 'Facilities and Infrastructure',
            'Member discounts and perks': 'Special Services',
            'Digital Equipment': 'Facilities and Infrastructure',
            'Pet-Friendly': 'Comfort and Inclusivity',
            'Mail and package handling services': 'Facilities and Infrastructure',
            'Access to Legal and Business Advisors': 'Special Services',
            'Childcare Services': 'Special Services',
            'Reception and Front Desk Services': 'Facilities and Infrastructure',
            'High-speed internet and digital resources': 'Facilities and Infrastructure',
            'Workshops and Classes': 'Networking and Community',
            'Networking and Social Events': 'Networking and Community',
            'Sound System': 'Facilities and Infrastructure',
            'Quiet zones for focused work': 'Work Environment and Productivity',
            'Makerspace with Tools': 'Facilities and Infrastructure',
            'Kitchen and Break Areas': 'Facilities and Infrastructure',
            'Dedicated Desk Space': 'Facilities and Infrastructure',
            'Shower Facilities': 'Facilities and Infrastructure',
            'Bike Storage': 'Facilities and Infrastructure',
            'Free Coffee and Tea': 'Facilities and Infrastructure',
            'Free Parking': 'Facilities and Infrastructure',
            'Art Supplies': 'Facilities and Infrastructure',
            'Storage Lockers': 'Facilities and Infrastructure',
            'Security Features': 'Facilities and Infrastructure',
            'Environmentally sustainable practices': 'Comfort and Inclusivity',
            'Flexible Lease Terms': 'Facilities and Infrastructure',
            'Quiet Zones': 'Work Environment and Productivity',
            'Accessibility features': 'Facilities and Infrastructure',
            'Outdoor Areas': 'Facilities and Infrastructure',
            'Showcase Events': 'Facilities and Infrastructure',
            'Outdoor Workspaces': 'Facilities and Infrastructure',
            'Outdoor and recreational spaces': 'Facilities and Infrastructure',
            'Professional and friendly management': 'Comfort and Inclusivity',
            'Networking Events': 'Networking and Community',
            'Event Space': 'Facilities and Infrastructure',
            'Soundproof Rooms': 'Facilities and Infrastructure',
            'Access to mentorship and professional development': 'Networking and Community',
            'Security and privacy measures': 'Facilities and Infrastructure',
            'Counseling and Mentorship': 'Special Services',
            'Regular networking events': 'Networking and Community',
            'Conference and meeting rooms availability': 'Facilities and Infrastructure',
            'Private Phone Booths': 'Facilities and Infrastructure',
            'Lounge Area': 'Facilities and Infrastructure',
            'Flexible desk arrangements': 'Work Environment and Productivity',
            'Flexible and diverse working spaces': 'Work Environment and Productivity',
            'Workshop and fabrication tools': 'Facilities and Infrastructure',
            'Green and Sustainable Features': 'Comfort and Inclusivity',
            'Green and sustainable practices': 'Comfort and Inclusivity',
            'Conference Rooms with AV Equipment': 'Facilities and Infrastructure',
            'Availability of equipment and technology': 'Facilities and Infrastructure',
            'Security': 'Facilities and Infrastructure',
            'Access to mentors and advisors': 'Networking and Community',
            'Cafeteria/Coffee Shop': 'Facilities and Infrastructure',
            '24/7 access and flexibility': 'Facilities and Infrastructure',
            'Proximity to public transportation and parking': 'Facilities and Infrastructure',
            'Comfortable and ergonomic furniture': 'Facilities and Infrastructure',
            '24/7 access': 'Facilities and Infrastructure',
            'Kitchen and break room amenities': 'Facilities and Infrastructure',
            'Inclusive and accessible design': 'Comfort and Inclusivity',
            'Friendly and inspiring community': 'Networking and Community'
        }


        aa_df = df[df['Describe Your Primary Role in Creative Sector']=='Arts Administrator (Theater managers, development staff, executive directors, program coordinators at an arts-based business usually a non-profit, e.g., at a museum, symphony, theater, etc.)']
        additional_space = 'What additional features are important to you for an arts-business co-working space?'
        aa_df[additional_space] = aa_df[additional_space].replace(categoried_dictionary)

        values = aa_df['What additional features are important to you for an arts-business co-working space?'].dropna().value_counts()
        values_dict = values.to_dict()
        aspects = list(values_dict.keys())
        colors = plt.cm.tab20c(np.linspace(0, 1, len(aspects)))
        value_counts = aa_df[additional_space].value_counts()

        fig, ax = plt.subplots()
        ax.barh(aa_df[additional_space].value_counts().index, aa_df[additional_space].value_counts().values, color=colors)

        ax.set_yticklabels(list(value_counts.index), fontsize=8)
        ax.set_xlabel('Frequency')
        ax.set_ylabel('Additional Features')
        ax.set_title('Distribution of Importance of Additional Features for Future Space of Arts Administrators')


        for tick in ax.yaxis.get_ticklabels():
            tick.set_ha('right')
        st.pyplot(fig)

    def plot_future_space_needs_of_amenity_cw(df):
    #The categorization dictionary is interpretated by AI and cross checked by the project team.
        categoried_dictionary = {
            'Member Discounts': 'Special Services',
            'Mail and Package Handling Services': 'Facilities and Infrastructure',
            'Reception Services': 'Facilities and Infrastructure',
            'Flexible Membership Plans': 'Facilities and Infrastructure',
            'Collaboration and networking opportunities': 'Work Environment and Productivity',
            'Mentorship Programs': 'Networking and Community',
            'Member-driven workshops and seminars': 'Networking and Community',
            'Air Conditioning and Heating': 'Facilities and Infrastructure',
            'Kitchen and coffee facilities': 'Facilities and Infrastructure',
            'Fitness Center/Wellness Programs': 'Special Services',
            'Outdoor Space': 'Facilities and Infrastructure',
            'Private Meeting Rooms': 'Facilities and Infrastructure',
            'Secure storage lockers': 'Facilities and Infrastructure',
            'Phone Booths': 'Facilities and Infrastructure',
            'Conference Rooms': 'Facilities and Infrastructure',
            'Access to printing and scanning facilities': 'Facilities and Infrastructure',
            'Clean Restrooms': 'Facilities and Infrastructure',
            'Dedicated Desks': 'Facilities and Infrastructure',
            'Ergonomic Furniture': 'Facilities and Infrastructure',
            'Ample Lighting': 'Facilities and Infrastructure',
            'Event Spaces': 'Facilities and Infrastructure',
            'Pet-friendly policies': 'Facilities and Infrastructure',
            'High-Speed Internet': 'Facilities and Infrastructure',
            'Projector and Screen': 'Facilities and Infrastructure',
            'Lounge and relaxation areas': 'Facilities and Infrastructure',
            '24/7 Access': 'Facilities and Infrastructure',
            'Mail and package handling': 'Facilities and Infrastructure',
            'Event and workshop hosting opportunities': 'Facilities and Infrastructure',
            'Kitchen Facilities': 'Facilities and Infrastructure',
            'On-Site Cafe': 'Facilities and Infrastructure',
            'Ergonomic furniture': 'Facilities and Infrastructure',
            'Comfortable Seating': 'Facilities and Infrastructure',
            'On-site support and maintenance services': 'Facilities and Infrastructure',
            'On-site tech support': 'Facilities and Infrastructure',
            'Affordable and competitive pricing': 'Facilities and Infrastructure',
            'Mail and Package Handling': 'Facilities and Infrastructure',
            'Gallery Space for Exhibiting': 'Facilities and Infrastructure',
            'Collaborative Environment': 'Work Environment and Productivity',
            'Diverse and Comfortable Workspaces': 'Work Environment and Productivity',
            'Friendly Community': 'Networking and Community',
            'Storage Space': 'Facilities and Infrastructure',
            'Printing Services': 'Facilities and Infrastructure',
            'Diverse and inclusive environment': 'Comfort and Inclusivity',
            'Fitness Center': 'Special Services',
            'Affordable Rent': 'Facilities and Infrastructure',
            'On-Site Technical Support': 'Facilities and Infrastructure',
            'Bike storage and shower facilities': 'Facilities and Infrastructure',
            'Wheelchair Accessibility': 'Facilities and Infrastructure',
            'Accessible Location': 'Facilities and Infrastructure',
            'Printer and scanner access': 'Facilities and Infrastructure',
            'Security Cameras': 'Facilities and Infrastructure',
            'Networking Opportunities': 'Networking and Community',
            'Collaboration Spaces': 'Work Environment and Productivity',
            'Recreational Facilities': 'Facilities and Infrastructure',
            'Printing and Copying Services': 'Facilities and Infrastructure',
            'Member discounts and perks': 'Special Services',
            'Digital Equipment': 'Facilities and Infrastructure',
            'Pet-Friendly': 'Comfort and Inclusivity',
            'Mail and package handling services': 'Facilities and Infrastructure',
            'Access to Legal and Business Advisors': 'Special Services',
            'Childcare Services': 'Special Services',
            'Reception and Front Desk Services': 'Facilities and Infrastructure',
            'High-speed internet and digital resources': 'Facilities and Infrastructure',
            'Workshops and Classes': 'Networking and Community',
            'Networking and Social Events': 'Networking and Community',
            'Sound System': 'Facilities and Infrastructure',
            'Quiet zones for focused work': 'Work Environment and Productivity',
            'Makerspace with Tools': 'Facilities and Infrastructure',
            'Kitchen and Break Areas': 'Facilities and Infrastructure',
            'Dedicated Desk Space': 'Facilities and Infrastructure',
            'Shower Facilities': 'Facilities and Infrastructure',
            'Bike Storage': 'Facilities and Infrastructure',
            'Free Coffee and Tea': 'Facilities and Infrastructure',
            'Free Parking': 'Facilities and Infrastructure',
            'Art Supplies': 'Facilities and Infrastructure',
            'Storage Lockers': 'Facilities and Infrastructure',
            'Security Features': 'Facilities and Infrastructure',
            'Environmentally sustainable practices': 'Comfort and Inclusivity',
            'Flexible Lease Terms': 'Facilities and Infrastructure',
            'Quiet Zones': 'Work Environment and Productivity',
            'Accessibility features': 'Facilities and Infrastructure',
            'Outdoor Areas': 'Facilities and Infrastructure',
            'Showcase Events': 'Facilities and Infrastructure',
            'Outdoor Workspaces': 'Facilities and Infrastructure',
            'Outdoor and recreational spaces': 'Facilities and Infrastructure',
            'Professional and friendly management': 'Comfort and Inclusivity',
            'Networking Events': 'Networking and Community',
            'Event Space': 'Facilities and Infrastructure',
            'Soundproof Rooms': 'Facilities and Infrastructure',
            'Access to mentorship and professional development': 'Networking and Community',
            'Security and privacy measures': 'Facilities and Infrastructure',
            'Counseling and Mentorship': 'Special Services',
            'Regular networking events': 'Networking and Community',
            'Conference and meeting rooms availability': 'Facilities and Infrastructure',
            'Private Phone Booths': 'Facilities and Infrastructure',
            'Lounge Area': 'Facilities and Infrastructure',
            'Flexible desk arrangements': 'Work Environment and Productivity',
            'Flexible and diverse working spaces': 'Work Environment and Productivity',
            'Workshop and fabrication tools': 'Facilities and Infrastructure',
            'Green and Sustainable Features': 'Comfort and Inclusivity',
            'Green and sustainable practices': 'Comfort and Inclusivity',
            'Conference Rooms with AV Equipment': 'Facilities and Infrastructure',
            'Availability of equipment and technology': 'Facilities and Infrastructure',
            'Security': 'Facilities and Infrastructure',
            'Access to mentors and advisors': 'Networking and Community',
            'Cafeteria/Coffee Shop': 'Facilities and Infrastructure',
            '24/7 access and flexibility': 'Facilities and Infrastructure',
            'Proximity to public transportation and parking': 'Facilities and Infrastructure',
            'Comfortable and ergonomic furniture': 'Facilities and Infrastructure',
            '24/7 access': 'Facilities and Infrastructure',
            'Kitchen and break room amenities': 'Facilities and Infrastructure',
            'Inclusive and accessible design': 'Comfort and Inclusivity',
            'Friendly and inspiring community': 'Networking and Community'
        }


        cw_df = df[df['Describe Your Primary Role in Creative Sector'] == 'Creative Worker (In-house graphic designers, copywriters, art directors employed at a business working in the creative industries)']
        additional_space = 'What additional features are important to you for an arts-business co-working space?'

        cw_df[additional_space] = cw_df[additional_space].replace(categoried_dictionary)

        values = cw_df[additional_space].dropna().value_counts()
        values_dict = values.to_dict()
        colors = plt.cm.tab20c(np.linspace(0, 1, len(values_dict)))
        value_counts = cw_df[additional_space].value_counts()

        fig, ax = plt.subplots()
        ax.barh(cw_df[additional_space].value_counts().index, cw_df[additional_space].value_counts().values, color=colors)

        ax.set_yticklabels(list(value_counts.index), fontsize=8)
        ax.set_xticks(range(0, max(value_counts.values)+1, 2))
        ax.set_xlabel('Frequency')
        ax.set_ylabel('Additional Features')
        ax.set_title('Distribution of Importance of Additional Features for Future Space of Creative Workers')

        st.pyplot(fig)

    def AE_TA_top3(df):
        shorten_roles = ['AE_TA', 'CE']
        roles = ['Arts Educator or Teaching Artist (Art teachers, music teachers, teaching artists, dance teachers, visiting artists)', 'Creative Entrepreneurs (Artists, performers, makers, creatives of all disciplines, self-employed)']
        fig, ax = plt.subplots()
        colors = ['#1f77b4', '#ff7f0e']
        
        for i, role in enumerate(roles):
            role_df = df[df['Describe Your Primary Role in Creative Sector'] == role]
            current_space = 'What type of space do you mainly use for your creative work?'
            
            categories = role_df[current_space].value_counts().sort_values(ascending=False).head(3).index
            
            ax.barh(categories, role_df[current_space].value_counts()[categories].values, color=colors[i])
        
        ax.set_ylabel('Type of Space')
        ax.set_xlabel('Count')
        ax.grid(axis='y', alpha=0.5)
        ax.set_title('Top 3 Space Needs Identified by Arts Educators/Teaching Artists and Creative Entrepreneurs')
        ax.legend(shorten_roles)
        
        st.pyplot(fig)

    def CW_top3(df):
        cw_df =df[df['Describe Your Primary Role in Creative Sector'] == 'Creative Worker (In-house graphic designers, copywriters, art directors employed at a business working in the creative industries)']
        colaborating_col = "How important are the following space types/amenities to your creative practice or business? Collaboration/networking events"
        spaces = 'How important are the following space types/amenities to your creative practice or business? Photography studio/dark room'
        space_or_amenity_columns = [col for col in cw_df.columns if 'how important' in col.lower()]
        value_mapping = {
            "Not at all important": 1,
            "Nice to have but not important": 2,
            "Somewhat important": 3,
            "Critically important": 4
            }

        for col in space_or_amenity_columns:
            cw_df[col] = cw_df[col].replace(value_mapping)

        cw_df = cw_df.dropna(subset=space_or_amenity_columns) 

        melted_df = cw_df.melt(id_vars=[colaborating_col], value_vars=space_or_amenity_columns, var_name='Amenity', value_name='Rating')

        mean_ratings = melted_df.groupby('Amenity')['Rating'].mean().sort_values(ascending=False)

        top3 = mean_ratings.head(3)

        top3_list = top3.index.tolist()
        temp_list = []
        for i in top3_list:
            word_list = i.split()
            index = word_list.index('business?')
            rest_of_string = ' '.join(word_list[index+1:])
            temp_list.append(rest_of_string)
        

        fig, ax = plt.subplots()
        ax.barh(temp_list, top3.values, color='blue')

        for i, v in enumerate(top3.values):
            ax.text(v + 0.1, i, str(round(v, 2)), color='blue', fontweight='bold')

        ax.set_title('Top 3 Amenities for Creative Workers')
        ax.set_xlabel('Mean Rating')
        ax.set_ylabel('Amenity')

        st.pyplot(fig)

    def AA_top3(df):
        aa_df = df[df['Describe Your Primary Role in Creative Sector'] == 'Arts Administrator (Theater managers, development staff, executive directors, program coordinators at an arts-based business usually a non-profit, e.g., at a museum, symphony, theater, etc.)']
        collaborating_col = "How important are the following space types/amenities to your creative practice or business? Collaboration/networking events"
        space_or_amenity_columns = [col for col in aa_df.columns if 'how important' in col.lower()]
        value_mapping = {
            "Not at all important": 1,
            "Nice to have but not important": 2,
            "Somewhat important": 3,
            "Critically important": 4
        }

        for col in space_or_amenity_columns:
            aa_df[col] = aa_df[col].replace(value_mapping)

        aa_df = aa_df.dropna(subset=space_or_amenity_columns)

        melted_df = aa_df.melt(id_vars=[collaborating_col], value_vars=space_or_amenity_columns, var_name='Amenity', value_name='Rating')

        mean_ratings = melted_df.groupby('Amenity')['Rating'].mean().sort_values(ascending=False)

        top3_amenities = mean_ratings.head(3)

        top3_list = top3_amenities.index.tolist()
        temp_list = []
        for i in top3_list:
            word_list = i.split()
            index = word_list.index('business?')
            rest_of_string = ' '.join(word_list[index+1:])
            temp_list.append(rest_of_string)

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.barh(temp_list, top3_amenities.values, color='blue')
        ax.set_title('Top 3 Amenities for Arts Administrators')
        ax.set_xlabel('Mean Rating')
        ax.set_ylabel('Amenity')
        ax.grid(axis='x', alpha=0.5)

        for i, v in enumerate(top3_amenities.values):
            ax.text(v + 0.1, i, str(round(v, 2)), color='blue', fontweight='bold')

        st.pyplot(fig)

    def builder():
        st.title("Space Needed")
        df = Space.load_data()

        st.markdown('## Space Need by Teaching Artists/Educators and Creative Entrepreneurs')
        st.markdown('In this part, we will look at the space need of Teaching Artists/Educators and Creative Entrepreneurs by looking at the answer they respond to the survey questions.')
        st.markdown('Slecet the group of people you are interested in and the plot you want to see by selecting under the dropdown menu.')
        options1 = ['Teaching Artists/Educators', 'Creative Entrepreneurs']
        selection1 = st.selectbox('Select the plot you interested in', options1)

        if selection1 == 'Teaching Artists/Educators':
            st.markdown("### Figure for Space Needs Identified by *Teaching Artists/Educators*")
            Space.plot_space_needs_for_AE_TA(df)
            st.markdown('The bar chart depicts the different types of workspace preferences identified by Teaching Artists/Educators. The most commonly preferred spaces are *"My work does not require designated space"*, *"Home, dedicated workspace in separate structure"*, and *"Studio at home and studio share. I need to use both due to a lack"* followed closely by *"Workspace outside the home: sole/private"* and *"Workspace outside the home: other"*. In contrast, the least preferred spaces are *"Home, informal workspace"* and *"Home, dedicated workspace"*.')
        elif selection1 == 'Creative Entrepreneurs':
            st.markdown("### Figure for Space Needs Identified by *Creative Entrepreneurs*")
            Space.plot_space_needs_for_CE(df)
            st.markdown('The bar chart illustrates the various space needs expressed by Teaching Artists/Educators. *"Home, informal workspace"* emerges as the most prevalent choice, with *"Currently building new space"* and *"Workspace outside the home: other"* following closely. On the other end of the spectrum, the least preferred options include *"Workspace outside the home: solo/private"* and *"I do not have the space I need for my art or creative work"*.')

        st.markdown('## Space Need by Creative Worker and Art Administrator')
        st.markdown('In thie part, we will look at the space need of Creative Worker and Art Administrator by looking at the answer they respond to the survey questions.')
        st.markdown('Slecet the group of people you are interested in and the plot you want to see by selecting under the dropdown menu.')
        options2 = ['Art Administrators', 'Creative Workers']
        selection2 = st.selectbox('Select the plot you interested in', options2)
        if selection2 == 'Art Administrators':
            st.markdown("### Figure for Space Needs Identified by *Art Administrators*")
            Space.plot_space_needs_for_AA(df)
            st.markdown('This stacked barplot illustrates the importance of various amenities for Arts Administrators, with shading corresponding to ratings from 1 to 4. Amenities like *"Projector/screening equipment"* and *"Theater/auditorium (100+ seats)"* are highly rated, indicating they are deemed very important. In contrast, amenities such as *"Photography studio/dark room"* and *"Music recording studio"* received a lower frequency of high ratings, suggesting they may be of lesser priority to Arts Administrators.')
        elif selection2 == 'Creative Workers':
            st.markdown("### Figure for Space Needs Identified by *Creative Workers*")
            Space.plot_space_needs_for_CW(df)
            st.markdown('The stacked barplot presents the importance ratings of various amenities for Arts Administrators, with different shades of purple indicating the frequency of each rating. The *"Computer Lab"* received the highest importance, with most respondents giving it a rating of 4. Conversely, amenities like *"Theater/auditorium (<100 seats)"* and *"Music practice room"* have a more balanced spread across all ratings, suggesting varied perceptions of their significance among the respondents.')

        st.markdown('## *Future* Space Need by Teaching Artists/Educators and Creative Entrepreneurs/Creative Workers/Art Administrators')
        st.markdown('Then we could invstigate into the future space that could be needed among different group of people. However, there is no direct answer from the participants. Instead, we could look at the importance of different amenities for different groups of people which could tell us how would the future space be like for those people.')
        st.markdown('Slecet the group of people you are interested in and the plot you want to see by selecting under the dropdown menu.')
        options3 = ['Creative Entrepreneurs', 'Teaching Artists/Educators', 'Art Administrators', 'Creative Workers']
        selection3 = st.selectbox('Select the plot you interested in', options3)
        if selection3 == 'Creative Entrepreneurs':
            st.markdown("### Figure for Future Space Needs Identified by *Creative Entrepreneurs*")
            Space.plot_future_space_needs_of_amenity_ce(df)
            st.markdown('This stacked barplot depicts the significance of various amenities for creative entrepreneurs based on their ratings from 1 to 4. Amenities such as *"Individual artist studio (any discipline)"* has most frequent high ratings followed by *"Music recording studio"* and *"Computer lab"*, suggesting their paramount importance to this group. On the other hand, facilities like *"Theater/auditorium (100+ seats)"* and *"Shared artist studio"* display a more distributed set of ratings, indicating a diverse range of opinions about their relevance.')
        elif selection3 == 'Teaching Artists/Educators':
            st.markdown("### Figure for Future Space Needs Identified by *Teaching Artists/Educators*")
            Space.plot_future_space_needs_of_amenity_ta(df)
            st.markdown('The stacked barplot showcases the perceived importance of different amenities to Teaching Artists/Educators, rated on a scale of 1 to 4. Facilities such as *"Writing room or quiet area"* and *"Secure storage/lockers"* have received high ratings, indicating they are essential for this group. Conversely, amenities like *"Theater/auditorium (<100seats)"* has a lower frequency of top ratings, suggesting this amenity may be less critical to Teaching Artists/Educators.')
        elif selection3 == 'Art Administrators':
            st.markdown("### Figure for Future Space Needs Identified by *Art Administrators*")
            Space.plot_future_space_needs_of_amenity_aa(df)
            st.markdown('The chart presents the distribution of importance for various additional features desired in future spaces for arts administrators. *"Inclusive and accessible design"*, *"Fitness Center/Wellness Programs"*, *"Access to printing and scanning facilities"*, *"Event and workshop hosting opportunities"*, *"On-site support and maintenance services"*, and *"Affordable and competitive pricing"* stand out with a notably higher frequency, emphasizing their primary importance among the arts administrators. Conversely, other features such as *"Mail and Package Handling Services"* and *"Diverse and Comfortable Workspaces"* display equally minimal frequency, suggesting that these may be of lesser significance or already satisfactorily met in existing setups.')
        elif selection3 == 'Creative Workers':
            st.markdown("### Figure for Future Space Needs Identified by *Creative Workers*")
            Space.plot_future_space_needs_of_amenity_cw(df)
            st.markdown('In this visualization, each additional feature tailored for a future space of creative workers has been given an equal frequency of 1, suggesting that the data represents a uniform distribution of feature importance. This could imply that all features are deemed equally significant by the respondents or that the data is presented without differentiation. Thus, to make informed decisions or derive meaningful insights, further granular data or supplementary context might be required.')

        st.markdown('## Top 3 Space Needs Identified by Different Groups of People')
        st.markdown('Finally, we could look at the top 3 space needs identified by different groups of people. The top 3 space needs are identified by the frequency of each space need. The top 3 space needs are the ones with the highest frequency or the high rating from the participants.')
        st.markdown('Slecet the group of people you are interested in and the plot you want to see by selecting under the dropdown menu.')
        options4 = ['Teaching Artists/Educators and Creative Entrepreneurs', 'Creative Workers', 'Art Administrators']
        selection4 = st.selectbox('Select the plot you interested in', options4)
        
        if selection4 == 'Teaching Artists/Educators and Creative Entrepreneurs':
            st.markdown("### Figure for Top 3 Space Needs Identified by *Teaching Artists/Educators* and *Creative Entrepreneurs*")
            Space.AE_TA_top3(df)  
            st.markdown('In this barplot, it shows the top 3 space needed for the Teaching Artists/Educators. The top 3 space needs are *"My work does not require designated space"*, *"Home, dedicated workspace in separate structure"*, and *"Studio at home and studio share. I need to use both due to a lack"*. Additionally, it shows the top 3 space needed for the Creative Entrepreneurs. The top 3 space needs are *"Home, informal workspace"*, *"Currently building new space"*, and *"Workspace outside the home: other"*.')
        elif selection4 == 'Creative Workers':
            st.markdown("### Figure for Top 3 Space Needs Identified by *Creative Workers*")
            Space.CW_top3(df)
            st.markdown('In this barplot, it shows the top 3 spaces needed by the Creative Workers. The top 3 space needs are *"Computer Lab"*, *"Theater/auditorium (100+ seats)"*, and *"Theater/auditorium (<100 seats)"*. It implies that the creative workers need a space with a computer lab, a theater with 100+ seats, and a theater with less than 100 seats.')
        elif selection4 == 'Art Administrators':
            st.markdown("### Figure for Top 3 Space Needs Identified by *Art Administrators*")
            Space.AA_top3(df)
            st.markdown('In this barplot, it shows the top 3 spaces needed by the Art Administrators. The top 3 space needs are *"Projector/screening equipment"*, *"Theater/auditorium (100+ seats)"*, and *"Theater/auditorium (<100 seats)"*. It implies that the art administrators need a space with a projector/screening equipment, a theater with 100+ seats, and a theater with less than 100 seats.')

class barriers:
    def load_ArtsEducator():
        # Load the data
        ArtsEducator_cleaned_empty = pd.read_excel("./ProcessedData/ArtsEducator_cleaned_empty.xlsx")

        return ArtsEducator_cleaned_empty

    def load_CreativeEntrepreneurs():
        # Load the data
        CreativeEntrepreneurs_cleaned_empty = pd.read_excel("./ProcessedData/CreativeEntrepreneurs_cleaned_empty.xlsx")

        return CreativeEntrepreneurs_cleaned_empty

    def load_CivicSocialServiceWorker():
        # Load the data
        CivicSocialServiceWorker_cleaned_empty = pd.read_excel("./ProcessedData/CivicSocialServiceWorker_cleaned_empty.xlsx")

        return CivicSocialServiceWorker_cleaned_empty

    def load_BusinessProfessional():
        # Load the data
        BusinessProfessional_cleaned_empty = pd.read_excel("./ProcessedData/BusinessProfessional_cleaned_empty.xlsx")

        return BusinessProfessional_cleaned_empty

    def load_ArtsFunder():
        # Load the data
        ArtsFunder_cleaned_empty = pd.read_excel("./ProcessedData/ArtsFunder_cleaned_empty.xlsx")

        return ArtsFunder_cleaned_empty

    def load_ArtsAdministrator():
        # Load the data
        ArtsAdministrator_cleaned_empty = pd.read_excel("./ProcessedData/ArtsAdministrator_cleaned_empty.xlsx")

        return ArtsAdministrator_cleaned_empty

    def load_CreativeWorker():
        # Load the data
        CreativeWorker_cleaned_empty = pd.read_excel("./ProcessedData/CreativeWorker_cleaned_empty.xlsx")

        return CreativeWorker_cleaned_empty

    def load_df_clean_empty():
        # Load the data
        df_cleaned_empty = pd.read_excel("./ProcessedData/df_cleaned_empty.xlsx")

        return df_cleaned_empty

    def load_combined_df():
        # Load the data
        combined_df = df_cleaned_empty = pd.read_excel("./ProcessedData/combined_df.xlsx")

        return combined_df






    def plot_CreativeEntrepreneurs(CreativeEntrepreneurs_cleaned_empty):
        # Processing the gender column
        # Identify columns with the word “barrier” in their names
        barrier_columns = [col for col in CreativeEntrepreneurs_cleaned_empty.columns if 'barrier' in col.lower()]

        # Define a mapping for the specified transformations
        value_mapping = {
            "1 - No impact": 1,
            "1 - No Impact": 1,
            "2 - Little impact": 2,
            "2 - Little Impact": 2,
            "3 - Some impact": 3,
            "3 - Some Impact": 3,
            "4 - Significant impact": 4,
            "5 - Highly impactful": 5,
            "5 - Most impactful": 5
        }

        
        # Apply the transformations to  the relevant columns
        CreativeEntrepreneurs_cleaned_empty[barrier_columns] = CreativeEntrepreneurs_cleaned_empty[barrier_columns].replace(value_mapping)
        CreativeEntrepreneurs_cleaned_empty[barrier_columns].head()

        

        # Filtering columns that include the word "barrier"
        barrier_columns = [col for col in CreativeEntrepreneurs_cleaned_empty.columns if 'barrier' in col.lower()]

        # Calculating the mean for each of those columns
        barrier_means = CreativeEntrepreneurs_cleaned_empty[barrier_columns].mean()

        # Filtering columns with mean value of 3 or greater
        filtered_means = barrier_means[barrier_means >= 3]

        # Plotting the filtered data
        plt.figure(figsize=(15, 7))
        filtered_means.plot(kind='barh', color='skyblue')
        plt.title("Significant Barriers faced by Creative Entrepreneurs", fontsize=20)
        plt.xlabel('Mean Value', fontsize=15)
        plt.ylabel('Barrier Types', fontsize=15)
        yticks = plt.yticks()[0]
        
        custom_labels = ['Lack of necessary equipment and/or technology', 'Access to affordable performance/presentation space', 'Access to funding', 'Transportation', 'Inability to host in-person events']
        plt.yticks(yticks, custom_labels)

        st.pyplot(plt.gcf())
        st.markdown("""##### Caption:""")
        st.markdown("""This chart illustrates the top barriers faced by Creative Entrepreneurs based on survey responses. The barriers are ranked by their mean values, with higher values indicating greater impact. The most significant barrier for Creative Entrepreneurs is the lack of necessary equipment and/or technology. The y-axis displays the barriers with a mean value greater than 3. On the x-axis, the average rating is shown on a scale of 1 to 5: 1 signifies no impact, 2 denotes little impact, 3 represents some impact, 4 stands for significant impact, and 5 indicates high impact.""") 


    def plot_ArtsAdministrators(ArtsAdministrator_cleaned_empty):
        # Processing the gender column
        # Identify columns with the word “barrier” in their names
        barrier_columns = [col for col in ArtsAdministrator_cleaned_empty.columns if 'barrier' in col.lower()]

        # Define a mapping for the specified transformations
        value_mapping = {
            "1 - No impact": 1,
            "1 - No Impact": 1,
            "2 - Little impact": 2,
            "2 - Little Impact": 2,
            "3 - Some impact": 3,
            "3 - Some Impact": 3,
            "4 - Significant impact": 4,
            "5 - Highly impactful": 5,
            "5 - Most impactful": 5
        }

        # Apply the transformations to the relevant columns
        ArtsAdministrator_cleaned_empty[barrier_columns] = ArtsAdministrator_cleaned_empty[barrier_columns].replace(value_mapping)
        ArtsAdministrator_cleaned_empty[barrier_columns].head()


        # Filtering columns that include the word "barrier"
        barrier_columns = [col for col in ArtsAdministrator_cleaned_empty.columns if 'barrier' in col.lower()]

        # Calculating the mean for each of those columns
        barrier_means = ArtsAdministrator_cleaned_empty[barrier_columns].mean()

        # Filtering columns with mean value of 3 or greater
        filtered_means = barrier_means[barrier_means >= 3]

        # Plotting the filtered data
        plt.figure(figsize=(15, 10))
        filtered_means.plot(kind='barh', color='skyblue')
        plt.title("Significant Barriers faced by Arts Administrator")
        plt.xlabel('Mean Value')
        plt.ylabel('Barrier Types')
        plt.tight_layout()

        yticks = plt.yticks()[0]
        custom_labels = ['Access to qualified talent to hire', 'Board development', 'No formal undergraduate, graduate, or informal technical skills training in your field', 'Lack of support from the private sector/business community', 'Transportation', 'Expecting audiance habits to change post-pandemic']
        plt.yticks(yticks, custom_labels)


        st.pyplot(plt.gcf())
        st.markdown("""##### Caption:""")
        st.markdown("""The chart presents the most prominent challenges faced by Arts Administrators. Among the top barriers are the lack of formal undergraduate, graduate, or informal technical skills training in your field, as well as limited access to qualified talent for hiring. The y-axis displays the barriers with a mean value greater than 3. On the x-axis, the average rating is shown on a scale of 1 to 5: 1 signifies no impact, 2 denotes little impact, 3 represents some impact, 4 stands for significant impact, and 5 indicates high impact.""") 


    def plot_CreativeWorker(CreativeWorker_cleaned_empty):
        # Processing the gender column
        # Identify columns with the word “barrier” in their names
        barrier_columns = [col for col in CreativeWorker_cleaned_empty.columns if 'barrier' in col.lower()]

        # Define a mapping for the specified transformations
        value_mapping = {
            "1 - No impact": 1,
            "1 - No Impact": 1,
            "2 - Little impact": 2,
            "2 - Little Impact": 2,
            "3 - Some impact": 3,
            "3 - Some Impact": 3,
            "4 - Significant impact": 4,
            "5 - Highly impactful": 5,
            "5 - Most impactful": 5
        }

        # Apply the transformations to the relevant columns
        CreativeWorker_cleaned_empty[barrier_columns] = CreativeWorker_cleaned_empty[barrier_columns].replace(value_mapping)
        CreativeWorker_cleaned_empty[barrier_columns].head()


        # Filtering columns that include the word "barrier"
        barrier_columns = [col for col in CreativeWorker_cleaned_empty.columns if 'barrier' in col.lower()]

        # Calculating the mean for each of those columns
        barrier_means = CreativeWorker_cleaned_empty[barrier_columns].mean()

        # Filtering columns with mean value of 3 or greater
        filtered_means = barrier_means[barrier_means >= 3]

        # Plotting the filtered data
        plt.figure(figsize=(15, 7))
        filtered_means.plot(kind='barh', color='skyblue')
        plt.title("Significant Barriers faced by Creative Worker")
        plt.xlabel('Mean Value')
        plt.ylabel('Barrier Types')

        yticks = plt.yticks()[0]
        custom_labels = ['Access to affordable creative practice/development space', 'Access to affordable performance/presentation space', 'Access to funding', 'Access to qualified talent to hire', 'Board development', 'Lack of business management knowledge', 'Not enough of an audiance for your work', 'Lack of support from private sector/business community', 'Too many competing priorities, not enough time']
        plt.yticks(yticks, custom_labels)

        plt.tight_layout()

        st.pyplot(plt.gcf())
        st.markdown("""##### Caption:""")
        st.markdown("""Highlighting the chief concerns of Creative Workers, this visualization underscores the impact of having too many competing priorities and insufficient time, as well as limited access to qualified talent for hiring.The y-axis displays the barriers with a mean value greater than 3. On the x-axis, the average rating is shown on a scale of 1 to 5: 1 signifies no impact, 2 denotes little impact, 3 represents some impact, 4 stands for significant impact, and 5 indicates high impact.""") 


    def plot_ArtsCreative(combined_df):
        # Processing the gender column
        # Identify columns with the word “barrier” in their names
        barrier_columns = [col for col in combined_df.columns if 'barrier' in col.lower()]

        # Define a mapping for the specified transformations
        value_mapping = {
            "1 - No impact": 1,
            "1 - No Impact": 1,
            "2 - Little impact": 2,
            "2 - Little Impact": 2,
            "3 - Some impact": 3,
            "3 - Some Impact": 3,
            "4 - Significant impact": 4,
            "5 - Highly impactful": 5,
            "5 - Most impactful": 5
        }

        # Apply the transformations to the relevant columns
        combined_df[barrier_columns] = combined_df[barrier_columns].replace(value_mapping)
        


        # Filtering columns that include the word "barrier"
        barrier_columns = [col for col in combined_df.columns if 'barrier' in col.lower()]

        # Calculating the mean for each of those columns
        barrier_means = combined_df[barrier_columns].mean()

        # Filtering columns with mean value of 3 or greater
        filtered_means = barrier_means[barrier_means >= 3]

        # Plotting the filtered data
        plt.figure(figsize=(15, 7))
        filtered_means.plot(kind='barh', color='skyblue')
        plt.title("Significant Barriers faced by Arts Administrators and Creative Worker")
        plt.xlabel('Mean Value')
        plt.ylabel('Barrier Types')

        yticks = plt.yticks()[0]
        custom_labels = ['Access to affordable creative practice/development space', 'Access to qualified talent to hire', 'Board development', 'No formal undergraduate, graduate, or informal technical skills training in your field', 'Lack of support from private sector/business community', 'Too many competing priorities, not enough time']
        plt.yticks(yticks, custom_labels)

        plt.tight_layout()

        st.pyplot(plt.gcf())
        st.markdown("""##### Caption:""")
        st.markdown("""Highlighting the chief concerns of Arts Administrators and Creative Workers, this visualization underscores the significance of access qualified talent to hire. The y-axis displays the barriers with a mean value greater than 3. On the x-axis, the average rating is shown on a scale of 1 to 5: 1 signifies no impact, 2 denotes little impact, 3 represents some impact, 4 stands for significant impact, and 5 indicates high impact.""") 


    def plot_Comparing(CreativeWorker_cleaned_empty,ArtsAdministrator_cleaned_empty,CreativeEntrepreneurs_cleaned_empty):
        # Define the value mapping
        value_mapping = {
            "1 - No impact": 1,
            "1 - No Impact": 1,
            "2 - Little impact": 2,
            "2 - Little Impact": 2,
            "3 - Some impact": 3,
            "3 - Some Impact": 3,
            "4 - Significant impact": 4,
            "5 - Highly impactful": 5,
            "5 - Most impactful": 5
        }

        # Extract barrier columns and apply transformations for CreativeEntrepreneurs_cleaned_empty
        barrier_columns_ce = [col for col in CreativeEntrepreneurs_cleaned_empty.columns if 'barrier' in col.lower()]
        CreativeEntrepreneurs_cleaned_empty[barrier_columns_ce] = CreativeEntrepreneurs_cleaned_empty[barrier_columns_ce].replace(value_mapping)

        # Extract barrier columns and apply transformations for ArtsAdministrator_cleaned_empty
        barrier_columns_aa = [col for col in ArtsAdministrator_cleaned_empty.columns if 'barrier' in col.lower()]
        ArtsAdministrator_cleaned_empty[barrier_columns_aa] = ArtsAdministrator_cleaned_empty[barrier_columns_aa].replace(value_mapping)

        # Extract barrier columns and apply transformations for CreativeWorker_cleaned_empty
        barrier_columns_cw = [col for col in CreativeWorker_cleaned_empty.columns if 'barrier' in col.lower()]
        CreativeWorker_cleaned_empty[barrier_columns_cw] = CreativeWorker_cleaned_empty[barrier_columns_cw].replace(value_mapping)


        # Get top 3 barriers for each dataframe
        top_3_ce = CreativeEntrepreneurs_cleaned_empty[barrier_columns_ce].mean().sort_values(ascending=False).head(3)
        top_3_aa = ArtsAdministrator_cleaned_empty[barrier_columns_aa].mean().sort_values(ascending=False).head(3)
        top_3_cw = CreativeWorker_cleaned_empty[barrier_columns_cw].mean().sort_values(ascending=False).head(3)

        
        # Plotting horizontal bar charts

        fig, ax = plt.subplots(3, 1, figsize=(12, 12))

        # Plot for Creative Entrepreneurs
        ax[0].barh(top_3_ce.index, top_3_ce.values, color='purple', alpha=0.7)
        ax[0].set_title('Top 3 Barriers for Creative Entrepreneurs')
        ax[0].invert_yaxis()  # To display the highest barrier at the top
        ax[0].set_xlabel('Mean Value')
        ax[0].set_yticklabels(['Lack of necessary equipment and/or technology', 'Transportation', 'Lack of necessary equipment and/or technology'])

        # Plot for Arts Administrators
        ax[1].barh(top_3_aa.index, top_3_aa.values, color='pink', alpha=0.7)
        ax[1].set_title('Top 3 Barriers for Arts Administrators')
        ax[1].invert_yaxis()
        ax[1].set_xlabel('Mean Value')
        ax[1].set_yticklabels(['No formal undergraduate, graduate, or informal technical skills in your field', 'Access to qualified talent to hire', 'Board development'])

        # Plot for Creative Workers
        ax[2].barh(top_3_cw.index, top_3_cw.values, color='lightblue', alpha=0.7)
        ax[2].set_title('Top 3 Barriers for Creative Workers')
        ax[2].invert_yaxis()
        ax[2].set_xlabel('Mean Value')
        ax[2].set_yticklabels(['Too many competing priorities, not enough time', 'Access to qualified talent to hire', 'Lack of support from the private sector/business comminity'])

        plt.tight_layout()

        st.pyplot(plt.gcf())
        st.markdown("""##### Caption:""")
        st.markdown("""Comparative Analysis of the Top 3 Barriers Faced by Creative Entrepreneurs, Arts Administrators, and Creative Workers. The y-axis displays the barriers with a mean value greater than 3. On the x-axis, the average rating is shown on a scale of 1 to 5: 1 signifies no impact, 2 denotes little impact, 3 represents some impact, 4 stands for significant impact, and 5 indicates high impact.""")

        st.markdown("""##### Insights:""")
        st.markdown(""" While each group deems barriers as being more significant than others, the average rating for the top barriers hovers around 3. This suggests that there isn't a standout barrier to prioritize uniquely for individual role groups. The only barrier that both Arts Administrators and Creative Workers share as a top concern is access to qualified talent for hiring.""")
        




    def builder():
        # Main Page Heading
        st.title("Barriers to the Creative Community")
        
        # Introduction
        st.write("""
        In the dynamic world of creative industries, professionals often navigate a myriad of challenges that can hinder their growth and potential. While the landscape of opportunities has expanded, so have the barriers that creative individuals confront. This section delves into the specific obstacles faced by different roles within the creative sector: Creative Entrepreneurs, Arts Administrators and Creative Workers, and Teaching Artists. By shedding light on these barriers, we aim to provide a comprehensive understanding of the challenges inherent in these roles. Additionally, a comparative analysis of the top three barriers for each group offers insights into the magnitude and commonality of the challenges across these roles. Through these figures, we hope to not only elucidate the hurdles but also inspire discussions and solutions that can pave the way for a more supportive creative ecosystem.
        """)
        
        # Background Information
        st.header("Key Information:")
        st.write("""
        To interpret the data presented in these figures, it's essential to first explain the survey method regarding barriers faced by the different groups.
                Each group was asked to rate specific barriers on a scale of 1 to 5, where:

            1. No impact
            2. Little impact
            3. Some impact
            4. Significant impact
            5. Highly impactful
        An example question might be, "Rate the barriers to success in your organization regarding access to affordable performance/presentation space."

        It's important to note that not all groups were surveyed in the same manner. Arts Administrators and Creative Workers were posed the same questions. In contrast, Creative Entrepreneurs were presented with different questions, and neither Arts Educators / Teaching Artists were asked to rate barriers at all.
        """)
        


        ArtsEducator_cleaned_empty = barriers.load_ArtsEducator()
        CreativeEntrepreneurs_cleaned_empty = barriers.load_CreativeEntrepreneurs()
        CivicSocialServiceWorker_cleaned_empty = barriers.load_CivicSocialServiceWorker()
        BusinessProfessional_cleaned_empty = barriers.load_BusinessProfessional()
        ArtsFunder_cleaned_empty = barriers.load_ArtsFunder()
        ArtsAdministrator_cleaned_empty = barriers.load_ArtsAdministrator()
        CreativeWorker_cleaned_empty = barriers.load_CreativeWorker()
        df_cleaned_empty = barriers.load_df_clean_empty()
        combined_df = barriers.load_combined_df()


        options = ['Barriers faced by Creative Entrepreneurs', 'Barriers faced by Arts Administrators', 'Barriers faced by Creative Workers', 'Barriers faced by Arts Administrators and Creative Workers','Comparing Top Barriers for Creative Entrepreneurs, Arts Administrators, and Creative Workers']
        selection = st.selectbox('Select a Figure:', options)

        # Display the appropriate plot based on selection
        if selection == 'Barriers faced by Creative Entrepreneurs':
            barriers.plot_CreativeEntrepreneurs(CreativeEntrepreneurs_cleaned_empty)
        elif selection == 'Barriers faced by Arts Administrators':
            barriers.plot_ArtsAdministrators(ArtsAdministrator_cleaned_empty)
        elif selection == 'Barriers faced by Creative Workers':
            barriers.plot_CreativeWorker(CreativeWorker_cleaned_empty)
        elif selection == 'Barriers faced by Arts Administrators and Creative Workers':
            barriers.plot_ArtsCreative(combined_df)
        elif selection == 'Comparing Top Barriers for Creative Entrepreneurs, Arts Administrators, and Creative Workers':
            barriers.plot_Comparing(CreativeWorker_cleaned_empty,ArtsAdministrator_cleaned_empty,CreativeEntrepreneurs_cleaned_empty)



if page == "Home":
    Homepage.builder()
elif page == "Creative Entreprenuers":
    Creative.creative_UI()
elif page == "Space Needs":
    Space.builder()
elif page == "Barriers":
    barriers.builder()