# INVITATION BOT - To send request


from urllib import request
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as exceptions
from selenium.webdriver.common.keys import Keys

import selenium.webdriver.common.keys
import time
import pandas as pd

def ll_login(e,p):
    email=data['Account'][e]
    password=data['Password'][p]
    linkedin_username=email
    linkedin_password=password
    global driver
    options= webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_experimental_option("detach",True)
    try:
        driver=webdriver.Chrome(chrome_options=options,executable_path=r'chromedriver.exe')
    except exceptions.WebDriverException:
        print("Get a newer version of driver!")
    
    try:
        driver.get("https://www.linkedin.com/login")
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,"username"))).send_keys(linkedin_username)
        # WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,"password"))).send_keys(linkedin_password)
        driver.find_element_by_id("password").send_keys(linkedin_password)
        # siggn = driver.find_element_by_id("password")
        # siggn.click()
        time.sleep(5)
        driver.find_element_by_xpath("//button[contains(text(),'Sign in')]").click()
        
        
    except ImportError:
        print("Closing Program!")

    try:
        driver.find_element_by_css_selector("input.form__input--text.input_verification_pin")
        otp=input("OTP: ")
        driver.find_element_by_css_selector("input.form__input--text.input_verification_pin").send_keys(otp)
        time.sleep(1)
        driver.find_element_by_css_selector("button.form__submit.form__submit--stretch").click()
    except exceptions.WebDriverException:
        print("No OTP Required")

def search_terms():
    k=1 #int(input("Enter no of Accounts :"))
    ll_login(0,0)
    n=len(names)
    print(n)
    m=(int)(n/k)
    print(m)
    r=(int)(n%k)
    print(r)
    c=0
    j=0
    e=0
    p=0
    k=k-1
    for i in names.iteritems():
        if j==m and k!=0:
            e=e+1
            p=p+1
            j=0
            k=k-1
            driver.close()
            ll_login(e,p)
        if r==0 :
            j=j+1
        else:
            r=r-1

        # extractig first name
        try:
            
            print("\n try 83")
            driver.get(i[1])
            time.sleep(8)
            driver.find_element_by_class_name('h1.text-heading-xlarge inline t-24 v-align-middle break-words')
            first_name = driver.find_element_by_css_selector("h1.text-heading-xlarge.inline.t-24.v-align-middle.break-words").text
            search_term = first_name.split()
            first_name = search_term[0]
            time.sleep(1)

            # If already connected 
            try: 
                print("\n try 93")
                
                driver.find_element_by_xpath("/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[1]/a").click()
                driver.find_element_by_css_selector("button.pvs-profile-actions__action.artdeco-button.artdeco-button--2.artdeco-button--primary.artdeco-button--disabled.ember-view").click()
                driver.find_element_by_css_selector("div.pvs-profile-actions > a.message-anywhere-button.pvs-profile-actions__action.artdeco-button").click()
                time.sleep(5)
                driver.find_element_by_css_selector("div.msg-form__contenteditable.t-14.t-black--light.t-normal.flex-grow-1.full-height.notranslate").send_keys('Hi '+ first_name + Keys.ENTER)
                time.sleep(4)
                driver.find_element_by_css_selector("button.msg-overlay-bubble-header__control.artdeco-button.artdeco-button--circle.artdeco-button--muted.artdeco-button--1.artdeco-button--tertiary.ember-view:nth-child(5)").click()
                print("Messaged: "+str(search_term[0])+" "+str(search_term[1]))
                c+=1
                time.sleep(3)
                continue

            # if not connect send connect 
            except exceptions.WebDriverException:
                print("except 107")

                # when connect button is showing
                try:
                    is_connect = driver.find_element_by_xpath("/html/body/div[5]/div[3]/div/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[1]/button/span").getText()
                    if(is_connect == "Connect" or is_connect == "connect"):
                        driver.find_element_by_xpath("/html/body/div[5]/div[3]/div/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[1]/button").click()
                    else :
                        is_connect = driver.find_element_by_xpath("/html/body/div[5]/div[3]/div/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[2]/button/span").getText()
                        if(is_connect == "Connect" or is_connect == "connect"):
                            driver.find_element_by_xpath("/html/body/div[5]/div[3]/div/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[2]/button").click()
                            
                    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[1]").click() # clicking on add note
                    time.sleep(5)
                    driver.find_element_by_class_name('connect-button-send-invite__custom-message').send_keys('Hi '+ first_name + ","+'\n'+message)
                    time.sleep(5)
                    driver.find_element_by_css_selector("button.ml1.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view").click()
                    print("Connection Request sent: "+str(str(search_term[0])+" "+str(search_term[1])))
                    time.sleep(3)
                    c+=1
                    continue
                    # is_connect = driver.find_element_by_xpath("/html/body/div[5]/div[3]/div/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[1]/button/span").text
                    # if(is_connect != "Connect" or is_connect != "connect"):
                    #     is_connect = driver.find_element_by_xpath("/html/body/div[5]/div[3]/div/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[2]/button").click()
                    # else:
                    #     is_connect.click()
                    # # print("try 112")
                    # # print("When connect button is showing")
                    # # driver.find_element_by_xpath("/html/body/div[5]/div[3]/div/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[1]/button/span").click()
                    # driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[1]/span").click()
                    # time.sleep(5)
                    # # driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div[1]/textarea").click().send_keys('Hi '+ first_name + ","+'\n'+message)
                    # # driver.find_element_by_css_selector("button.mr1.artdeco-button.artdeco-button--muted.artdeco-button--2.artdeco-button--secondary.ember-view").click()
                    # #print("entered3")
                    # driver.find_element_by_class_name('connect-button-send-invite__custom-message').send_keys('Hi '+ first_name + ","+'\n'+message)
                    # time.sleep(5)
                    # driver.find_element_by_css_selector("button.ml1.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view").click()
                    # print("Connection Request sent: "+str(str(search_term[0])+" "+str(search_term[1])))
                    # time.sleep(3)
                    # c+=1
                    # continue     

                    # print("\n try 110")
                    # driver.refresh()
                    # # driver.find_element_by_css_selector('div.pv-top-card-v2-ctas.pt2.display-flex > div.pvs-profile-actions > button.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view.pvs-profile-actions__action').click()
                    # driver.find_element_by_xpath("/html/body/d
                    # iv[5]/div[3]/div/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[1]/button").click()
                    # time.sleep(5)
                    # driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[1]").click()
                    # # driver.find_element_by_css_selector("button.mr1.artdeco-button.artdeco-button--muted.artdeco-button--2.artdeco-button--secondary.ember-view").click()
                    
                    # driver.find_element_by_class_name('connect-button-send-invite__custom-message').send_keys('Hi '+ first_name + ","+'\n'+message)
                    # time.sleep(4)
                    # driver.find_element_by_css_selector("button.ml1.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view").click()
                    # print("Connection Request sent: "+str(search_term[0])+" "+str(search_term[1]))
                    # c+=1
                    # time.sleep(3)
                    # continue

                # when connect button is in more 
                except exceptions.WebDriverException:
                    print("\n except 126")

                    # clicking on connect 
                    try:
                        print("\n try 131")
                        driver.find_element_by_css_selector("div.pv-top-card-v2-ctas.pt2.display-flex > div.pvs-profile-actions > div.artdeco-dropdown.artdeco-dropdown--placement-bottom.artdeco-dropdown--justification-left.ember-view > button.artdeco-dropdown__trigger.artdeco-dropdown__trigger--placement-bottom.ember-view.pvs-profile-actions__action.artdeco-button.artdeco-button--secondary.artdeco-button--muted.artdeco-button--2").click()
                        time.sleep(5)
                        button = driver.find_element_by_css_selector("div.pv-top-card-v2-ctas.pt2.display-flex > div.pvs-profile-actions > div.artdeco-dropdown.artdeco-dropdown--is-open.artdeco-dropdown--placement-bottom.artdeco-dropdown--justification-left.ember-view > div.pvs-overflow-actions-dropdown__content.artdeco-dropdown__content.artdeco-dropdown__content--is-open.artdeco-dropdown--is-dropdown-element.artdeco-dropdown__content--justification-left.artdeco-dropdown__content--placement-bottom.ember-view >div.artdeco-dropdown__content-inner> ul > li:nth-child(4) > div.display-flex.align-items-center.artdeco-dropdown__item.artdeco-dropdown__item--is-dropdown.ember-view").text
                        
                        b1=button.split()
                        button = b1[-1]
                        if button == "Connect" or button == "connect":
                            driver.find_element_by_css_selector("div.pv-top-card-v2-ctas.pt2.display-flex > div.pvs-profile-actions > div.artdeco-dropdown.artdeco-dropdown--is-open.artdeco-dropdown--placement-bottom.artdeco-dropdown--justification-left.ember-view > div.pvs-overflow-actions-dropdown__content.artdeco-dropdown__content.artdeco-dropdown__content--is-open.artdeco-dropdown--is-dropdown-element.artdeco-dropdown__content--justification-left.artdeco-dropdown__content--placement-bottom.ember-view >div.artdeco-dropdown__content-inner> ul > li:nth-child(4) > div.display-flex.align-items-center.artdeco-dropdown__item.artdeco-dropdown__item--is-dropdown.ember-view").click()                            
                        else :
                            driver.find_element_by_css_selector("div.pv-top-card-v2-ctas.pt2.display-flex > div.pvs-profile-actions > div.artdeco-dropdown.artdeco-dropdown--is-open.artdeco-dropdown--placement-bottom.artdeco-dropdown--justification-left.ember-view > div.pvs-overflow-actions-dropdown__content.artdeco-dropdown__content.artdeco-dropdown__content--is-open.artdeco-dropdown--is-dropdown-element.artdeco-dropdown__content--justification-left.artdeco-dropdown__content--placement-bottom.ember-view >div.artdeco-dropdown__content-inner> ul > li:nth-child(5) > div.display-flex.align-items-center.artdeco-dropdown__item.artdeco-dropdown__item--is-dropdown.ember-view").click()
                        time.sleep(5)
                        
                        # got clicked on connect button 


                        # adding for new condition
                        try :
                            print("\n try 148")
                            driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/button[4]").click()
                            time.sleep(2)
                            driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button/span").click()
                            
                            # sending note when connect is in more
                            try:
                                print("\n try 154")
                                #print("entered1")
                                #driver.find_element_by_css_selector("button.mr2.artdeco-button.artdeco-button--muted.artdeco-button--2.artdeco-button--secondary.ember-view").click()
                                #print("entered2")
                                driver.find_element_by_css_selector("button.mr1.artdeco-button.artdeco-button--muted.artdeco-button--2.artdeco-button--secondary.ember-view").click()
                                #print("entered3")
                                driver.find_element_by_class_name('connect-button-send-invite__custom-message').send_keys('Hi '+ first_name + ","+'\n'+message)
                                time.sleep(5)
                                driver.find_element_by_css_selector("button.ml1.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view").click()
                                print("Connection Request sent: "+str(str(search_term[0])+" "+str(search_term[1])))
                                time.sleep(3)
                                c+=1
                                continue      
                                
                                # request got send 


                            except exceptions.WebDriverException:
                                print("\n except 170")
                                time.sleep(5)
                                driver.find_element_by_css_selector("button.pv-recommendations__flow-close-btn").click()
                                time.sleep(5)
                                driver.find_element_by_css_selector("div.pvs-profile-actions > a.message-anywhere-button.pvs-profile-actions__action.artdeco-button").click()
                                time.sleep(5)
                                
                                driver.find_element_by_css_selector("div.msg-form__contenteditable.t-14.t-black--light.t-normal.flex-grow-1.full-height.notranslate").send_keys('Hi '+ first_name + Keys.ENTER)
                                time.sleep(4)
                                driver.find_element_by_css_selector("button.msg-overlay-bubble-header__control.artdeco-button.artdeco-button--circle.artdeco-button--muted.artdeco-button--1.artdeco-button--tertiary.ember-view:nth-child(5)").click()
                                print("Messaged: "+str(search_term[0])+" "+str(search_term[1]))
                                c+=1
                                continue

                        # if not asking "how you know that person"
                        except:
                            print("\n except 186")

                            # sending note when connect is in more
                            try:
                                print("\n try 192")
                                #print("entered1")
                                #driver.find_element_by_css_selector("button.mr2.artdeco-button.artdeco-button--muted.artdeco-button--2.artdeco-button--secondary.ember-view").click()
                                #print("entered2")
                                driver.find_element_by_css_selector("button.mr1.artdeco-button.artdeco-button--muted.artdeco-button--2.artdeco-button--secondary.ember-view").click()
                                #print("entered3")
                                driver.find_element_by_class_name('connect-button-send-invite__custom-message').send_keys('Hi '+ first_name + ","+'\n'+message)
                                time.sleep(5)
                                driver.find_element_by_css_selector("button.ml1.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view").click()
                                print("Connection Request sent: "+str(str(search_term[0])+" "+str(search_term[1])))
                                time.sleep(3)
                                c+=1
                                continue      
                                
                                # request got send 


                            except exceptions.WebDriverException:
                                print("\n except 207")
                                time.sleep(5)
                                driver.find_element_by_css_selector("button.pv-recommendations__flow-close-btn").click()
                                time.sleep(5)
                                driver.find_element_by_css_selector("div.pvs-profile-actions > a.message-anywhere-button.pvs-profile-actions__action.artdeco-button").click()
                                time.sleep(5)
                                
                                driver.find_element_by_css_selector("div.msg-form__contenteditable.t-14.t-black--light.t-normal.flex-grow-1.full-height.notranslate").send_keys('Hi '+ first_name + Keys.ENTER)
                                time.sleep(4)
                                driver.find_element_by_css_selector("button.msg-overlay-bubble-header__control.artdeco-button.artdeco-button--circle.artdeco-button--muted.artdeco-button--1.artdeco-button--tertiary.ember-view:nth-child(5)").click()
                                print("Messaged: "+str(search_term[0])+" "+str(search_term[1]))
                                c+=1
                                continue

                    # if it's already connected   
                    except exceptions.WebDriverException:
                        print("\n except 223")
                        print("Already Connected : "+str(str(search_term[0])+" "+str(search_term[1])))
                        continue
        
        # if request not sent 
        except :
            print("URL Error")
        
    print("Sent Invitations to : ",c)
    print("Request not sent to : ",n-c)
            
if __name__ == "__main__":
    
    data = pd.read_csv("Details.csv")
    
    message=data['Message'][0]
    names=data['URL']
    search_terms()