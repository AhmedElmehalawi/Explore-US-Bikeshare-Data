import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input(
            'Which city would you like to see data for chicago, new york city or washington?\n').lower()

        if city not in ('chicago', 'new york city', 'washington'):
            print("Please choose between chicago, new york city or washington")
            continue
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input(
            "Enter a month from {january, february, march, april, may, june} to filter by or 'all' to apply no month filter: ").lower()

        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print("Please Enter a Month from 'january, february, march, april, may, june' or type 'all' to apply no filter")
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter Day: ").lower()
        if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print("Please Enter a valid day or type 'all' to apply no filter")
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

    # Reading the .csv file of the city the user has specified as df.
    df = pd.read_csv(CITY_DATA[city])

    # Pandas df filtered by month and day of the specified city.
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    df['month'] = df['Start Time'].dt.month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df
# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month is: ", df['month'].value_counts().idxmax())

    # display the most common day of week
    print("The most common day is: ",
          df['day_of_week'].value_counts().idxmax())

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common start hour is: ",
          df['hour'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most commonly used start station is: ",
          df['Start Station'].value_counts().idxmax())

    # display most commonly used end station
    print("The most commonly used end station is: ",
          df['End Station'].value_counts().idxmax())

    # display most frequent combination of start station and end station trip
    print("The most frequent combination of start station and end station trip")
    most_common_start_and_end_stations = df.groupby(
        ['Start Station', 'End Station']).size().nlargest(1)
    print(most_common_start_and_end_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum() / 3600.0
    print("Total travel time in hours is: ", total_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean() / 3600.0
    print("Mean travel time in hours is: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    # P.S: In our case Washington has no gender data, so we’ll skip it if the user specified Washington.
    if 'Gender' in df:
        user_gender = df['Gender'].value_counts()
        print(user_gender)
    else:
        print('Washington has no Gender Data.')

    # Display earliest, most recent, and most common year of birth
    # P.S: In our case Washington has no birth year data, so we’ll skip it if the user specified Washington.
    if 'Birth Year' in df:
        earliest_year_of_birth = int(df['Birth Year'].min())
        most_recent_year_of_birth = int(df['Birth Year'].max())
        most_common_year_of_birth = int(
            df['Birth Year'].value_counts().idxmax())
        print("The earliest year of birth is:", earliest_year_of_birth, ", The most recent year is:",
              most_recent_year_of_birth, "and the most common year is: ", most_common_year_of_birth)
    else:
        print('Washington has no Birth Year Data.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def get_raw_data(df):
    """
        Asking the user whether they’d like to see the raw data.
        If the user typed 'yes,'then the script should print 5 rows of the data at a time.
        If the user tuped 'no' the script is gonna take him to the next step which is restarting the program.
    """

    view_data = input(
        '\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while(True):
        if view_data == 'yes':
            print(df[start_loc: start_loc+5])
            start_loc += 5
            view_data = input(
                "Do you like to continue viewing the next 5 rows?: ").lower()
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
        get_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
