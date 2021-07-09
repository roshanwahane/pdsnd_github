
import time
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None) # to display all columns of the data

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ["chicago", "new york city", "washington"]
    while True:
        try:
            city = str(input("Which city would you like to see the data for? (Chicago, New York City, Washington):\n"))
            if city.lower() not in cities:
                print("Please enter correct city name.\n")
                continue
        except ValueError:
            print("Sorry, I didn't understand that.\n")
            #better try again... Return to the start of the loop
            continue
        else:
            #city was successfully parsed!
            #we're ready to exit the loop.
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    months_list = ["all", "january", "febuary", "march", "april", "may", "june", "july", "august", "september", "october",  "november",  "december"]
    while True:
        try:
            month = str(input("\nWhich month would you like to see the data for? (January-December or All):\n"))
            if month.lower() not in months_list:
                print("Please type correct month name.\n")
                continue
        except ValueError:
            print("Sorry, I didn't understand that.\n")
            #better try again... Return to the start of the loop
            continue
        else:
            #month was successfully parsed!
            #we're ready to exit the loop.
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days_list = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "all"]
    while True:
        try:
            day = str(input("\nWhich day would you like to see the data for? (Monday-Sunday or All):\n"))
            if day.lower() not in days_list:
                print("Please type correct day.\n")
                continue
        except ValueError:
            print("Sorry, I didn't understand that.\n")
            #better try again... Return to the start of the loop
            continue
        else:
            #day was successfully parsed!
            #we're ready to exit the loop.
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city.lower()])
    df["Start Time"] = pd.to_datetime(df["Start Time"]) #converting date to datetime
    df["Month"] = df["Start Time"].dt.month_name() #extracting month from date
    df["Day_of_week"] = df["Start Time"].dt.day_name() #extracting day of week from date
    
    if month.lower() != "all":
        df = df[df["Month"] == month.title()]
    
    if day.lower() != "all":
        df = df[df["Day_of_week"] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df["Month"].value_counts().idxmax()
    print("The most common month is: ", common_month)

    # TO DO: display the most common day of week
    common_dayofweek = df["Day_of_week"].value_counts().idxmax()
    print("The most common day of the week is: ", common_dayofweek)

    # TO DO: display the most common start hour
    df["Hour"] = df["Start Time"].dt.hour
    common_start_hour = df["Hour"].value_counts().idxmax()
    print("The most common start hour is: ", common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df["Start Station"].value_counts().idxmax()
    print("The most commonly used start station is: ", start_station)

    # TO DO: display most commonly used end station
    end_station = df["End Station"].value_counts().idxmax()
    print("The most commonly used end station is: ", end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combi_stat_stop_name = df.groupby(["Start Station", "End Station"]).size().idxmax()
    print("The most frequent combination of start station and end station trip is:\n", combi_stat_stop_name)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_travel_time = df["Trip Duration"].sum()
    print("The total travel time is: ", tot_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("The mean travel time is: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df["User Type"].value_counts()
    print("The counts of user types are:\n",user_type.to_string())
    
    
    if "Gender" in df.columns:
            # TO DO: Display counts of gender
            gender_counts = df["Gender"].value_counts()
            print("The gender counts are:\n",gender_counts.to_string())
    else:
        pass
        #print("Gender column is not available for this city.")
        
    if "Birth Year" in df.columns:
        # TO DO: Display earliest, most recent, and most common year of birth
        early_dob = df["Birth Year"].min()
        recent_dob = df["Birth Year"].max()
        common_dob = df["Birth Year"].mode()
        print("\nThe earliest year of birth is:",early_dob)
        print("\nThe most recent year of birth is:",recent_dob)
        print("\nThe most common year of birth is:",common_dob)
    else:
        pass
        #print("Birth year column is not available for this city.")
       
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def print_raw_data(df): #function to ask if the user wishes to see raw data
    start = 0
    end = 6
    while True:
        try:
            raw_data = str(input("Would you like to display individual data trip (5 rows)? Enter 'yes' or 'no':\n"))
            if raw_data.lower() not in ["yes", "no"]:
                print("Please type correct response.\n")
                continue
        except ValueError:
            print("Sorry, I didn't understand that.\n")
            #better try again... Return to the start of the loop
            continue
        else:
            if raw_data.lower() == "yes":
                print(df.iloc[start:end, :])
                start += 6
                end += 5
                continue
            else:
               break

            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        print_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no:\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
