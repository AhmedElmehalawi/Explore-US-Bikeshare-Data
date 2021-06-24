# Explore US Bikeshare Data <br>
- The first project in the Professional Data Analysis Nanodegree from Udacity.

## Overview
- Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

- Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

- With the use of the data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. In this project, we’ll explore the system usage between three large cities: Chicago, New York City, and Washington.

## Tha Datasets
<b>Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:</b>
- Start Time (e.g., 2017-01-01 00:07:57)
- End Time (e.g., 2017-01-01 00:20:53)
- Trip Duration (in seconds - e.g., 776)
- Start Station (e.g., Broadway & Barry Ave)
- End Station (e.g., Sedgwick St & North Ave)
- User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:
- Gender
- Birth Year

## Statistics Computed
* <b>Popular times of travel</b>
  * Most common month
  * Most common day of week
  * Most common hour of day
* <b>Popular stations and trip</b>
  * Most common start station
  * Most common end station
  * Most common trip from start to end (i.e., most frequent combination of start station and end station)
* <b>Trip duration</b>
  * Total travel time
  * Average travel time
* <b>User info</b>
  * Counts of each user type
  * Counts of each gender (only available for NYC and Chicago)
  * Earliest, most recent, most common year of birth (only available for NYC and Chicago)
 
## How it works
<b>The script asks the user some information to give the computed statistics for the related data</b>
- Name of the city to see data for chicago, new york city or washington.
- Name of the month to filter by, or "all" to apply no month filter.
- Name of the day of week to filter by, or "all" to apply no day filter.

![01](https://user-images.githubusercontent.com/44305776/123330877-e1540280-d53e-11eb-9ac4-c80f92084f6b.png)<hr>

<b>After taking the three information from the user, the script starts computing the statistics.</b>
<b>After finishing, the script asks if the user would like to see raw data</b>
- If the user typed 'yes,'then the script should print 5 rows of the data at a time.
- If the user typed 'no' the script is gonna stop printing data and take him to the next step.

![02](https://user-images.githubusercontent.com/44305776/123330893-e44ef300-d53e-11eb-861e-45c65731044c.png)<hr>

<b>The Final step is to ask if the user would like to restart the program or not</b>
- If the user typed 'yes,'then the whole process is gonna be repeated.
- If the user typed 'no', it’s gonna be stopped.

![03](https://user-images.githubusercontent.com/44305776/123330908-e7e27a00-d53e-11eb-96bd-0a964ab1b594.png)<hr>

