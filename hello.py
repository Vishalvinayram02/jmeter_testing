import time
import webbrowser
import subprocess
import platform

video_url = ["https://www.youtube.com/watch?v=CCZlSC2xcm4&list=PLASEZhYPXbUyGXInhW3cowJ2OXkcTtL5q&index=10","https://www.youtube.com/watch?v=PP_BHsZXG3A&list=PLASEZhYPXbUyGXInhW3cowJ2OXkcTtL5q&index=11","https://www.youtube.com/watch?v=Pum1sD4Eq6o&list=PLASEZhYPXbUyGXInhW3cowJ2OXkcTtL5q&index=12","https://www.youtube.com/watch?v=lMF_-RNjLkM&list=PLASEZhYPXbUyGXInhW3cowJ2OXkcTtL5q&index=13","https://www.youtube.com/watch?v=t_bjJIrSICE&list=PLASEZhYPXbUyGXInhW3cowJ2OXkcTtL5q&index=14"]

while True:
    for i in range(0,len(video_url)):
        webbrowser.open(video_url[i])
        time.sleep(20)  # Sleep for 20 seconds


        # Determine the operating system
        
# from selenium import webdriver
# import time

# video_url = "https://youtu.be/kPcQdmKBey4"

# # Create a new instance of the Chrome browser
# driver = webdriver.Chrome()
# while 1:

# # Open the URL in a new tab
#     driver.get(video_url)cha

#     # Wait for 20 seconds
#     time.sleep(20)

#     # Close the current tab
#     driver.close()

#     # Quit the browser
# driver.quit()