# Made by @Saksham Solanki

#------------------------------------ Importing Libraries ------------------------------------#
import speedtest
import os
import time
#---------------------------------------------------------------------------------------------#
#----------------------------------- Init files and tester -----------------------------------#
init = speedtest.Speedtest()
path = os.getcwd()
file = "data_speed.csv"
#---------------------------------------------------------------------------------------------#
#------------------------------------ Function to get data -----------------------------------#
def read():
    with open(path+"/"+file, 'r') as f:
        xc = f.read()
        f.close()
        return xc
#---------------------------------------------------------------------------------------------#
#------------------------------------ Function to get vars -----------------------------------#
def get_data():
    download_speed = init.download()
    upload_speed = init.upload()
    server_names = []
    init.get_servers(server_names)
    ping_speed = init.results.ping
    return download_speed, upload_speed, ping_speed
#---------------------------------------------------------------------------------------------#
#----------------------------------- Function to store data ----------------------------------#
def store_data():
    download, upload, ping = get_data()
    try:
        read()
    except:
        with open(path+"/"+file, 'w') as f:
            f.write("Download_Speed,Upload_Speed,Ping")
            f.close()
    data = read()
    with open(path+"/"+file, 'w') as f:
        f.write(data+'\n'+str(download)+','+str(upload)+','+str(ping))
        f.close()
#---------------------------------------------------------------------------------------------#
#------------------------------------- Main program Init -------------------------------------#
if __name__ == '__main__':

    while True:

        store_data()
        time.sleep(300) # Edit this to run it at any interval you want, default is 5 minutes
#---------------------------------------------------------------------------------------------#