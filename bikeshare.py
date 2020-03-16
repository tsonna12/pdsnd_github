import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#cities = ['New York City', 'Chicago', 'Washington']
cities = ['new york city', 'chicago', 'washington']
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
months = ['january', 'february', 'march', 'april', 'may', 'june']
WEEKDAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
      city = input("\nWhich city would you like to filter by? Kindly between New York City, Chicago and Washington?\n")
      city = city.lower()
      if city not in cities:
        print("I am sorry, I didn't catch that. Try again.")
        continue
      else:
        break


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      month = input("\nWhich month would you like to filter by? Kindly between January, February, March, April, May, June or type 'all' if you do not have any preference\n")
      month = month.lower()
      if month not in MONTHS:
        print("I am sorry, I didn't catch that. Try again.")
        continue
      else:
        break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input("\nDo you need a particular day? If that is the case, kindly enter the day as follows: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all'             if you do not have any preference.\n")
      day = day.lower()
      if day not in WEEKDAYS:
        print("I am sorry, I didn't catch that. Try again.")
        continue
      else:
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
    ## load data file  
    city = city.lower()
    df = pd.read_csv(CITY_DATA[city])
 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':        
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    p_month = df['month'].mode()[0]
    print('Most Common Month:', p_month)

    # TO DO: display the most common day of week
    p_day = df['day_of_week'].mode()[0]
    print('Most Common day:', p_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    p_hour = df['hour'].mode()[0]
    print('Most Common Hour:', p_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', Start_Station)

    # TO DO: display most commonly used end station
    End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station:', End_Station)

    # TO DO: display most frequent combination of start station and end station trip
    #Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    #print('\nMost Commonly used combination of start station and end station trip:', Start_Station, " & ", End_Station)
    combine_stations = df['Start Station'] + "*" + df['End Station']
    common_station = combine_stations.value_counts().idxmax()
    #print('Most frequent used combinations are:\n{} \nto\n{}'.format(common_station.split('*')[0], common_station.split('*')[1]))
    print('Most frequent used combinations are:\n{} \nto\n{}'.format(common_station.split('*')[0], common_station.split('*')[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Time = sum(df['Trip Duration'])
    print('Total travel time:', Total_Time/86400, " Days")

    # TO DO: display mean travel time
    Mean_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Time/60, " Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    # TO DO: Display counts of gender
    try:
      g_types = df['Gender'].value_counts()
      print('\nGender Types:\n', g_types)
    except KeyError:
      print("\nGender Types:\nThere is no data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      Early_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Early_Year)
    except KeyError:
      print("\nEarliest Year:\nThere is no data available for this month.")

    try:
      Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nThere is no data available for this month.")

    try:
      Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', Common_Year)
    except KeyError:
      print("\nMost Common Year:\nThere is no data available for this month.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    user_input = input('Do you want to see raw data? Enter yes or no.\n')
    line_number = 0

    while 1 == 1 :
        if user_input.lower() != 'no':
            print(df.iloc[line_number : line_number + 5])
            line_number += 5
            user_input = input('\nDo you want to see more raw data? Enter yes or no.\n')
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
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
                break



if __name__ == "__main__":
	main()