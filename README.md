# Internet_speed_monitering_system
This is a simple python program which when you start running, after that every 10 minutes it will save ping, upload speed and download speed in a .csv file. 
### How does this works?
It actually is a pretty straight forward program. It uses a library named as speedtest-cli to get upload speed, download speed and ping by connecting to a random server present near you. After that all of that data is stored in a file named as data_speed.csv. This data is logged every 5 minutes and varies according to your net usage.
### Is this program useful?
That's the first and the only question which might pop up in your head, its good I'm prepared with an answer!, Well the thing is that after parsing this data for a few days I found few of the things: 
1. My ping is usually between 100 - 500
2. Whenever I'm downloading something the ping spikes upto 600
3. While surfing youtube, 400 - 650
4. While netflix and chill, 200 - 500
5. When 2 devices are connected - 300 (on minimum)

If We see this data carefully then we can draw out a few things. First being, we can make another program which will parse this data, it'll look for these conditions, if it sees any spikes then it'll inform us. This data can also be used to check if someone has hacked you, because suddenly getting higher pings isn't something common! I'll be creating this program soon and will update more as I add!!
