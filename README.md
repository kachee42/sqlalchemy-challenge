# Hawaii Weather Analysis

This code analyses the rain and temperature data for 9 weather stations on Hawaii from 1/1/2010 to 8/23/2017.

# Methods

- Use sqlalchemy to connect to and query data from hawaii.sqlite
- Graph results of query using matplotlib and pandas
- Use Flask to create basic API to return specified rain and temperature data

# Analysis

The rain data in the measurements table was analyzed and the latest year of data was isolated and plotted in a bar graph as follows:
![image](https://user-images.githubusercontent.com/118322354/222807816-fee59b31-41ee-4284-8b6e-5d085baedbd6.png)

Summary statistics were calculated for the latest year of rain data and the following is the result of those calculations:
![image](https://user-images.githubusercontent.com/118322354/222808075-cc8af088-8dc5-43e8-aaf2-4a0b22f1bab1.png)

The station with the most data points was determined and lowest, highest, and average temperatures at that station were calculated as follows:
![image](https://user-images.githubusercontent.com/118322354/222808426-d0987a56-e3c7-4204-9ff2-a7f9291ddccd.png)

The temperature data for the latest year at the most active station was isolated and the results were plotted in a histogram with 12 bins as follows:
![image](https://user-images.githubusercontent.com/118322354/222808883-acc85c2f-1c3f-4100-92e6-957d700d32fb.png)

# API

A python script using flask was used to create an API homepage that lists all of the possible routes as follows:
![image](https://user-images.githubusercontent.com/118322354/222810930-9ad9018b-225d-4fce-8a78-07bcaaaa9b14.png)

Precipitation data for the latest year of data was queried and placed into the /api/v1.0/precipitation route as follows:
![image](https://user-images.githubusercontent.com/118322354/222811473-47a09b38-5079-4ec4-9a37-134de08e5d5e.png)

The list of stations and their names were queried and placed into the /api/v1.0/stations route as follows:
![image](https://user-images.githubusercontent.com/118322354/222811785-6431ac72-b5db-4cbe-962b-16fbd0921025.png)

The dates and temperatures of the latest year at the most active station were queried and place into the /api/v1.0/tobs route as follows:
![image](https://user-images.githubusercontent.com/118322354/222812124-d526e6c6-80b1-4ed5-9df6-ca8c90b22a1d.png)

The mimum, maximum, and average temperatures of the temperature data from the user input start date in the route to the last date in the data set was calculated and placed into the /api/v1.0/start-date route. The following is that data with an example date:
![image](https://user-images.githubusercontent.com/118322354/222813010-1a36245b-79bb-4f18-aec4-95e80670fb6f.png)

The mimum, maximum, and average temperatures of the temperature data from the user input start date in the route to the user input end date was calculated and placed into the /api/v1.0/start-date/end-date route. The following is that data with example dates:
![image](https://user-images.githubusercontent.com/118322354/222813337-dc58f285-fd38-4552-a408-ce83b1476112.png)
