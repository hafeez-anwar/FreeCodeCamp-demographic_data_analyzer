import pandas as pd

def calculate_demographic_data(print_data=True):
    #---------------------------- TASK 1----------------------------------------
    # Read data from file
    df = pd.read_csv('data/adult.data.csv')
    #---------------------------- TASK 1----------------------------------------

    #---------------------------- TASK 2----------------------------------------
    # How many of each race are represented in this dataset?
    # This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    #---------------------------- TASK 2----------------------------------------

    #---------------------------- TASK 3----------------------------------------
    # What is the average age of men?
    # Extract the column of SEX
    column_sex = df['sex']
    # Extract the column of AGE
    column_age = df['age']
    # Calculate MEAN of AGE column where SEX is MALE
    average_age_men = round((column_age[column_sex=='Male']).mean(),1)
    #---------------------------- TASK 3----------------------------------------

    #---------------------------- TASK 4----------------------------------------
    # What is the percentage of people who have a Bachelor's degree?
    # Number of people whose EDUCATION is bachelors
    x = sum(df['education']=='Bachelors')
    # Percentage of those people
    y = (x/df.shape[0])*100
    # Rounding the percentage to one decimal position
    percentage_bachelors = round(y,1)
    #---------------------------- TASK 4----------------------------------------

    #---------------------------- TASK 5----------------------------------------
    # What percentage of people with advanced education
    # (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?

    # Extract all the people with higher degrees and make their
    # separate dataframe
    higher_education = df[(df['education']=='Bachelors') | \
                        (df['education']=='Masters') | \
                        (df['education']=='Doctorate')]
    # Number of highly educated people who earn more than 50K
    x = sum(higher_education['salary']=='>50K')
    # Percentage
    y = (x/higher_education.shape[0])*100
    # Rounding to one decimal position
    higher_education_rich = round(y,1)
    #---------------------------- TASK 5----------------------------------------

    #---------------------------- TASK 6----------------------------------------
    # What percentage of people without advanced education make more than 50K?
    # Extract all the people who do not have higher degrees and make their
    # separate dataframe
    lower_education = df[(df['education']!='Bachelors') & \
                            (df['education']!='Masters') & \
                            (df['education']!='Doctorate')]

    # Number of people NOT highly education
    x = sum(lower_education['salary']=='>50K')
    # Percentage
    y = (x/lower_education.shape[0])*100
    # Rounding to one decimal position
    lower_education_rich = round(y,1)
    #---------------------------- TASK 6----------------------------------------

    #---------------------------- TASK 7----------------------------------------
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    #---------------------------- TASK 7----------------------------------------

    #---------------------------- TASK 8----------------------------------------
    # What percentage of the people who work the minimum number of hours per
    # week have a salary of >50K?

    # Extract the hours_per_week and salary columns from the Dataframe
    work_column = df['hours-per-week']
    salary_column = df['salary']

    # Find those rows of salary column where the work column has MIN value
    n = salary_column[work_column==work_column.min()]

    # Now, find the number of workers who work MIN and PAID >50K
    num_min_workers = sum(n=='>50K')

    # Calculate their Percentage
    rich_percentage = int((num_min_workers/n.shape[0])*100)
    #---------------------------- TASK 8----------------------------------------

    #---------------------------- TASK 9----------------------------------------
    # The following statement will return a dataframe based on the salary
    # column >50K
    rich_ = df[df['salary']=='>50K']

    # The count of unique values in the new dataframe is then divide on the
    # count of unique values in the complete dataframe, which gives the ratio
    # of rich people in each country in a series
    x = rich_['native-country'].value_counts()/ \
            df['native-country'].value_counts()

    # The ratio is then transformed to percentages.
    y = x*100

    # Now with the following statement, we retrieve the index name where the
    # MAX percentage occurs
    country_name = y.index[y==y.max()]
    highest_earning_country = country_name[0]
    highest_earning_country_percentage = round(y.max(),1)
    #---------------------------- TASK 9----------------------------------------

    #---------------------------- TASK 10----------------------------------------
    # Make a new Dataframe where the native country is INDIA and SALARY is >50K
    rich_indians = df[(df['native-country']=='India') & (df['salary']=='>50K')]

    # Get the number of occurances of unique occupations in descending order,
    # which gives a series
    rich_indians_occupations = rich_indians['occupation'].value_counts()

    # Get the name of the first occupation using index name at first position
    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = rich_indians_occupations.index[0]
    #---------------------------- TASK 10----------------------------------------

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
