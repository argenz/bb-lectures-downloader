# Blackboard Collaborate Lecture Downloader

This scraper downloads lecture videos from Blackboard Collaborate, the Bocconi university courses platform. 

This was build because the lectures recordings remain available only for 24h after the lecture, so students that want to keep the recordings for revision have to log in daily to download them. 
I built this scraper that automates the retrival of the recording links for all lectures on a given day, based a specific lecture icalendar link provided by the university. 

To make it 100% hands free, I installed this script on AWS and set up a trigger to execute it daily, and configured the download of the lectures to an S3 bucket. 
The cloud configuration part is not explained here, but if you want to do the same and need help sentting it up reach out to me on Linkedin https://www.linkedin.com/in/fcra/.

# Usage
The webdriver-manager automatically fetches the latest webdriver version, hence the LATEST Google Chrome version is required. 

To run:  
1. Download the repository  
2. Open terminal, navigate to directory of the repositiory. cd /path 
3. Install required packages with: 
''' pip3 install -r requirements.txt ''' 
4. Change config.py file with your information.
5. In terminal run python3 main.py 

