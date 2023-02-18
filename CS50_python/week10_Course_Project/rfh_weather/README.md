# Forecast of well-being for weather dependent people.
#### Video Demo:  https://youtu.be/TN-Vh9TmwUw
#### Description:

Hi all! My name is Vitaly, now I live in Astana, Kazakhstan.

I present to you my program for weather dependent (people whose well-being is
highly dependent on the state of the weather)

I noticed a long time ago that my well-being often depends heavily on the state of
environment, pressure, wind speed and gusts, magnetic
storms. When the values become extreme, the head hurts,
blood pressure rises and the condition worsens in general.

To predict how I feel, I began to monitor the weather and its parameters in 
order to understand what exactly and how affects my condition.

I am faced with the fact that few sites or programs present data in a 
convenient format, and almost never have all the data on one site.
As a result, you have to look at the data on several sites and compare them.
This is inconvenient, since in this case it is difficult to link all the
parameters into one
picture and find dependencies.

Before creating the program, I defined the parameters that must be mandatory 
in the program.

- air pressure
- degree of change to previous values
- wind speed
- gusts of wind (produce momentary changes in pressure)
- KP-Index (the index shows the strength of magnetic storms)

In addition to these data, the program has standard temperature data.

It was decided to make a program that will combine these parameters in one 
place, color alerts were made for the convenience of displaying parameters -
which visually signal dangerous values and simplify working with the program.

Color indication of dangerous values in two versions: Slight excess - yellow 
color, strong excess - red color. The more red indicators you see, the more 
likely you are to feel unwell, increase blood pressure, and have a headache.

I also made my own M-Index which is based on the above values, but it is still
configurable.

For more accurate work, a module for collecting well-being statistics has been
added to the program. It asks for your current state, and writes to a file 
saving your state and the current value of the weather parameters.

With sufficient data accumulation, statistics can be processed by a module with 
neural networks.

At the moment the program only has a command line interface, but at the 
moment I'm already working on creating a front-end for the program using 
the Django framework.
I'm also working on optimizing and reducing code reuse.
In the future, I plan to develop the project and make it a separate site and
application.

#### How do I use the program?
Well, firstly - three times a day I open the program and give a description
of my state of health for the accumulation of statistics.
If I see red values of wind gusts, pressure or KP index - then on this day 
I will try not to plan a workout, if possible - I will postpone important things.

If you suffer from poor health due to weather factors - please take care
not to experience physical exertion during this time, and if you need
medication - take it with you.

#### project.py
The main program file with logic and functions responsible for printing to
the command line with warning alerts through colorama

### weatherdata.py
The file contains two classes, each of which is responsible for the weather
on the ground and space weather, respectively. The classes have methods 
that collect data via api or, as in the case of kp-index forecast,
information is taken from a text file.

### sw_k_for.txt
Updated file with forecast of magnetic storms

### get_selffeel_data.py
File with functions for collecting and recording data for statistical analysis.
The data is written to the file data_ml/selffeel_data_vetrof@gmail.com.csv

### link:
How geomagnetic activity affects cardiovascular disease:
[https://ehjournal.biomedcentral.com/articles/10.1186/s12940-019-0516-0](https://ehjournal.biomedcentral.com/articles/10.1186/s12940-019-0516-0)

What is meteopathy?:
[https://meteoagent.com/weather-pains-meteoropathy](https://meteoagent.com/weather-pains-meteoropathy)

### API:
Data for the formation of current values and forecast are obtained via the API:
KP-Index from [https://www.swpc.noaa.gov](https://www.swpc.noaa.gov/)
Weather data from [https://www.weatherapi.com/](https://www.weatherapi.com/)

### email:
If you have any questions, you can write to me at vetrof@gmail.com