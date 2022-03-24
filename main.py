import time
from webdriver import SeleniumWebdriver
from config import username, password, ical_url
import logging as log
from session import RequestSession
from mycalendar import myCalendar
import sys

#DAILY Python SCRIPT RUN 

#create calendar instance 
cal = myCalendar(ical_url)
courseIds = cal.get_courseIds_today()

if len(courseIds)==0: sys.exit("You did not have lectures today.")

log.warning(f"Today's Lectures were: {courseIds}")

#start webdriver
driver = SeleniumWebdriver()
driver.login(username, password)

#start session 
mySession = RequestSession()
cookies = driver.get_cookies_dict()
mySession.update_cookies(cookies)

#begin scraping
for courseId in courseIds: 
    driver.nav_to_course(courseId)
    #time.sleep(10)
    driver.check_announcemements_and_skip()
    driver.view_recordings()
    buttons = driver.get_course_recordings_buttons()

    i=0
    for button in buttons: 
        recording_name = driver.get_lecture_name_from_button(button)
        driver.click_rec_button_and_open_rec_link(button, i)
        recording_url = driver.get_recording_url()
        
        filename = f"{courseId}_{recording_name}"
        
        mySession.download_file(filename, recording_url) #Specify correct path, possibly in the TEMP directory
        driver.close_rec_tab() #go back to main tab
        i+=2

mySession.close()
driver.quit() 

