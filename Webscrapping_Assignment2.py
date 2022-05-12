#!/usr/bin/env python
# coding: utf-8

# WEBSCRAPING ASSIGNMENT - 2 (using selenium)

Q1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10 jobs data. This task will be done in following steps:

This task will be done in following steps:
    
1. First get the webpage https://www.naukri.com/
    
2. Enter “Data Analyst” in “Skill, Designations, Companies” field and enter “Bangalore” in “enter the location” field.

3. Then click the search button.

4. Then scrape the data for the first 10 jobs results you get.

5. Finally create a dataframe of the scraped data.

Note: All of the above steps have to be done in code. No step is to be done manually.

# In[1]:


#import required libraries
import selenium
import pandas as pd
from selenium import webdriver
import time
import warnings
warnings.filterwarnings("ignore")


# In[2]:


##calling webdriver and getting into website
driver = webdriver.Chrome(r"C:\Users\youra\OneDrive\Desktop\SAI_dsp35\Datatrained\chromedriver.exe")
driver.get('https://www.naukri.com')


# In[3]:


##Entering required input element in job search field
desig = driver.find_element_by_class_name("suggestor-input")
desig.send_keys('Data Analyst')


# In[4]:


#Entering required input in location search field
loc = driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div/div[3]/div/div/div/input")
loc.send_keys('Bangalore')   


# In[5]:


#clicking search button
search = driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div/div[6]")
search.click()


# In[6]:


title = []
comp = []
loc = []
exp = []


# In[7]:


#scraping all the required data by xpath route


# In[8]:


title_tags = driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
for i in title_tags:
    title.append(i.text) 


# In[9]:


company_tags = driver.find_elements_by_xpath("//a[@class='subTitle ellipsis fleft']")
for i in company_tags:
    comp.append(i.text) 


# In[10]:


experienc_tags = driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi experience']/span[1]")
for i in experienc_tags:
    exp.append(i.text) 


# In[11]:


location_tags = driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi location']/span[1]")
for i in location_tags:
    loc.append(i.text) 


# In[12]:


#Closing the web browser after scraping
driver.close()


# In[13]:


# saving data into a data frame
jobs = pd.DataFrame({'Job-title':title[0:10], 'Company_name':comp[0:10], 'Job-location':loc[0:10], 'Experience_required':exp[0:10]})   


# In[14]:


jobs

Q2: Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.
This task will be done in following steps:
1. First get the webpage https://www.naukri.com/
2. Enter “Data Scientist” in “Skill, Designations, Companies” field and enter “Bangalore” in “enter the location” field.
3. Then click the search button.
4. Then scrape the data for the first 10 jobs results you get.
5. Finally create a dataframe of the scraped data.
Note: All of the above steps have to be done in code. No step is to be done manually.
# In[15]:


#import required libraries
import selenium
import pandas as pd
from selenium import webdriver
import time
import warnings
warnings.filterwarnings("ignore")


# In[16]:


##calling webdriver and getting into website
driver = webdriver.Chrome(r"C:\Users\youra\OneDrive\Desktop\SAI_dsp35\Datatrained\chromedriver.exe")
driver.get('https://www.naukri.com')


# In[17]:


##Entering required input element in job search field
desig = driver.find_element_by_class_name("suggestor-input")
desig.send_keys('Data Scientist')


# In[18]:


#Entering required input in location search field
loc = driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div/div[3]/div/div/div/input")
loc.send_keys('Bangalore')
     


# In[19]:


#clicking search button
search = driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div/div[6]")
search.click()


# In[20]:


title = []
comp = []
loc = []
    


# In[21]:


#scraping all the required data by xpath route


# In[22]:


title_tags = driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
for i in title_tags:
        title.append(i.text) 


# In[23]:


company_tags = driver.find_elements_by_xpath("//a[@class='subTitle ellipsis fleft']")
for i in company_tags:
        comp.append(i.text) 


# In[24]:


location_tags = driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi location']/span[1]")
for i in location_tags:
        loc.append(i.text) 


# In[25]:


#Closing the web browser after scraping
driver.close()


# In[26]:


# saving data into a data frame
jobs = pd.DataFrame({'Job-title':title[0:10], 'Company_name':comp[0:10], 'Job-location':loc[0:10]})   
    


# In[27]:


jobs

Q3: In this question you have to scrape data using the filters available on the webpage as shown below:
You have to use the location and salary filter.
You have to scrape data for “Data Scientist” designation for first 10 job results.
You have to scrape the job-title, job-location, company name, experience required. The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs
The task will be done as shown in the below steps:
1. first get the webpage https://www.naukri.com/
2. Enter “Data Scientist” in “Skill, Designations, and Companies” field.
3. Then click the search button.
4. Then apply the location filter and salary filter by checking the respective boxes
5. Then scrape the data for the first 10 jobs results you get.
6. Finally create a dataframe of the scraped data.
Note: All of the above steps have to be done in code. No step is to be done manually.        
        
# In[28]:


#import required libraries
import selenium
import pandas as pd
from selenium import webdriver
import time
import warnings
warnings.filterwarnings("ignore")


# In[29]:


##calling webdriver and getting into website
driver = webdriver.Chrome(r"C:\Users\youra\OneDrive\Desktop\SAI_dsp35\Datatrained\chromedriver.exe")
driver.get('https://www.naukri.com')


# In[30]:


#Entering required input element in job search field
desig = driver.find_element_by_class_name("suggestor-input")
desig.send_keys('Data Scientist')


# In[31]:


# code to click on the search button
  #clicking search button
search = driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div/div[6]")
search.click()


# In[33]:


# code to click on the location filter for "Delhi/NCR"
location_filter = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/section[1]/div[2]/div[4]/div[2]/div[3]/label/p/span[1]')
location_filter.click()


# In[36]:


# code to click on the salary filter for "3-6 Lakhs"
salary_filter = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/section[1]/div[2]/div[5]/div[2]/div[2]/label/p/span[1]')
salary_filter.click()


# In[ ]:





# In[ ]:


#scraping all the required data by xpath route


# In[37]:


title=[]
Title=driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
for i in Title:
    #print(i.text)
    title.append(i.text)
title[0:10]


# In[38]:


company_list=[]
company=driver.find_elements_by_xpath("//a[@class='subTitle ellipsis fleft']")
for i in company:
    company_list.append(i.text)
company_list[0:10]


# In[39]:


exp_list=[]
exp=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi experience']/span")
for i in exp:
    exp_list.append(i.text)
exp_list[0:10]


# In[40]:


# extract all the job locations including Bangalore and the others with it
jloc_list=[]
jloc=driver.find_elements_by_xpath('//li[@class="fleft grey-text br2 placeHolderLi location"]//span')
for i in jloc:
    jloc_list.append(i.text)
jloc_list[0:10]


# In[41]:


# checking the length for getting the data frame
print("Lengths of columns:",len(title), len(company_list), len(exp_list), len(jloc_list))


# In[42]:


# creating the data frame now
df = pd.DataFrame({})
df['Job Title']=title
df['Company Names']=company_list
df['Years of experience required']=exp_list
df['Job Locations']=jloc_list
df[0:10]

Q4: Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:
1. Brand
2. Product Description
3. Price
The attributes which you have to scrape is ticked marked in the below image.

To scrape the data you have to go through following steps:
1. Go to Flipkart webpage by url : https://www.flipkart.com/
2. Enter “sunglasses” in the search field where “search for products, brands andmore” is written and click the search icon
3. After that you will reach to the page having a lot of sunglasses. From this pageyou can scrap the required data as usual.

4. After scraping data from the first page, go to the “Next” Button at the bottom ofthe page , then click on it.
5. Now scrape data from this page as usual
6. Repeat this until you get data for 100 sunglasses.
Note: That all of the above steps have to be done by coding only and not manually
# In[43]:


#import required libraries 
import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
import time
from selenium.common.exceptions import NoSuchElementException


# In[44]:


#connect to webdriver
driver = webdriver.Chrome(r"C:\Users\youra\OneDrive\Desktop\SAI_dsp35\Datatrained\chromedriver.exe")
time.sleep(2)

#to get url
driver.get('https://www.flipkart.com/')


# In[45]:


# to close login pop up
driver.find_element_by_xpath("//button[@class='_2KpZ6l _2doB4z']").click()


# In[46]:


#finding elements for job search bar
search_job = driver.find_element_by_class_name('_3704LK')
search_job.send_keys("sunglasses")


# In[47]:


search_button = driver.find_element_by_xpath("//button[@class='L0Z3Pu']").click()


# In[48]:


url ='https://www.flipkart.com/search?q=sunglasses&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
#to get url
driver.get(url)


# In[49]:


element_list = []

for page in range (0,4):
    page_url = "https://www.flipkart.com/search?q=sunglasses&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + str(page)
    driver = webdriver.Chrome(r"C:\Users\youra\OneDrive\Desktop\SAI_dsp35\Datatrained\chromedriver.exe")
    driver.get(page_url)
    brand_tag = driver.find_elements_by_class_name('_2WkVRV')
    product_tag = driver.find_elements_by_class_name('IRpwTa')
    price_tag = driver.find_elements_by_class_name('_30jeq3')
    discount_tag = driver.find_elements_by_class_name('_3Ay6Sb')
    
    for i in range(len(brand_tag)):
        element_list.append([brand_tag[i].text,product_tag[i].text,price_tag[i].text,discount_tag[i].text])
element_list
    


# In[50]:


sunglass = pd.DataFrame(element_list)
sunglass.columns = ['Brand','Product Description','Price','Discount']
sunglass[:100]


# In[51]:


driver.close

Q5: Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link: https://www.flipkart.com/apple-iphone-11-black-64-gb-includes- earpods-power- adapter/p/itm0f37c2240b217?pid=MOBFKCTSVZAXUHGR&lid=LSTMOBFKC TSVZAXUHGREPBFGI&marketplace.
When you will open the above link you will reach to the below shown webpage .
As shown in the above page you have to scrape the tick marked attributes.These are:
1. Rating
2. Review summary
3. Full review
4. You have to scrape this data for first 100 reviews.
Note: All the steps required during scraping should be done through code only and not manually.

# In[52]:


#import required libraries 
import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
import time
from selenium.common.exceptions import NoSuchElementException


# In[53]:


# get drivers
driver = webdriver.Chrome(r"C:\Users\youra\OneDrive\Desktop\SAI_dsp35\Datatrained\chromedriver.exe")
time.sleep(2)


# In[54]:


#get url
url = "https://www.flipkart.com/apple-iphone-11-black-64-gb-includes- earpods-poweradapter/p/itm0f37c2240b217?pid=MOBFKCTSVZAXUHGR&lid=LSTMOBFKTSVZAXUHGREPBFGI&marketplace"
driver.get(url)


# In[55]:


# to find all elements and from different pages and save them in list
element_list1 = []

for page in range (0,14):
    page_url = "https://www.flipkart.com/apple-iphone-11-black-64-gb-includes-earpods-power-adapter/product-reviews/itm0f37c2240b217?pid=MOBFKCTSVZAXUHGR&lid=LSTMOBFKCTSVZAXUHGR3IXQLM&marketplace=FLIPKART&page=" + str(page)
    driver = webdriver.Chrome(r"C:\Users\youra\OneDrive\Desktop\SAI_dsp35\Datatrained\chromedriver.exe")
    driver.get(page_url)
    rating_tag = driver.find_elements_by_xpath(".//div[@class='row']//div[@class='_3LWZlK _1BLPMq']")
    summary_tag = driver.find_elements_by_class_name('_2-N8zT')
    review_tag = driver.find_elements_by_class_name('t-ZTKy')
    
    for i in range(len(rating_tag)):
        element_list1.append([rating_tag[i].text,summary_tag[i].text,review_tag[i].text])
element_list1
    


# In[56]:


# making dataframe
iphone = pd.DataFrame(element_list1)
iphone.columns = ['Ratings','Review Summary','Full Review']
iphone[:100]


# In[57]:


driver.close

Q6: Scrape data for first 100 sneakers you find when you visit flipkart.com andsearch for “sneakers” in the search field.
You have to scrape 4 attributes of each sneaker:
1. Brand
2. Product Description
3. Price
As shown in the below image, you have to scrape the tick marked attributes.
Note: All the steps required during scraping should be done through code only and not manually
# In[58]:


#import required libraries 
import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
import time
from selenium.common.exceptions import NoSuchElementException


# In[59]:


#connect to webdriver
driver = webdriver.Chrome(r"C:\Users\youra\OneDrive\Desktop\SAI_dsp35\Datatrained\chromedriver.exe")
time.sleep(2)

#to get url
driver.get('https://www.flipkart.com/')


# In[60]:


# to close login pop up
driver.find_element_by_xpath("//button[@class='_2KpZ6l _2doB4z']").click()


# In[61]:


#finding elements for sneaker search bar
search_job = driver.find_element_by_class_name('_3704LK')
search_job.send_keys("sneaker")


# In[63]:


search_button = driver.find_element_by_xpath("//button[@class='L0Z3Pu']").click()


# In[64]:


url ='https://www.flipkart.com/search?q=sneaker&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
#to get url
driver.get(url)


# In[65]:


# to find all elements and from different pages and save them in list
element_list3 = []

for page in range (0,4):
    page_url = "https://www.flipkart.com/search?q=sneaker&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + str(page)
    driver = webdriver.Chrome(r"C:\Users\youra\OneDrive\Desktop\SAI_dsp35\Datatrained\chromedriver.exe")
    driver.get(page_url)
    brand_tag = driver.find_elements_by_class_name('_2WkVRV')
    product_tag = driver.find_elements_by_class_name('IRpwTa')
    price_tag = driver.find_elements_by_class_name('_30jeq3')
    discount_tag = driver.find_elements_by_class_name('_3Ay6Sb')
    
    for i in range(len(brand_tag)):
        element_list3.append([brand_tag[i].text,product_tag[i].text,price_tag[i].text,discount_tag[i].text])
element_list3


# In[66]:


#making of dataframe
sneakers = pd.DataFrame(element_list3)
sneakers.columns = ['Brand','Product Description','Price','Discount']
sneakers[:100]


# In[67]:


driver.close

Q7: Go to the link - https://www.myntra.com/shoes
Set Price filter to “Rs. 7149 to Rs. 14099 ” , Color filter to “Black”, as shown inthe below image.
And then scrape First 100 shoes data you get. The data should include “Brand” of the shoes , Short Shoe description, price of the shoe as shown in the below image.
Note: Applying the filter and scraping the data, everything should be done through code only and there should not be any manual step.
# In[68]:


#import required libraries 
import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
import time
from selenium.common.exceptions import NoSuchElementException


# In[69]:


#connect to webdriver
driver = webdriver.Chrome(r"C:\Users\youra\OneDrive\Desktop\SAI_dsp35\Datatrained\chromedriver.exe")
time.sleep(2)

#to get url
driver.get('https://www.myntra.com/shoes')


# In[70]:


# applying price filter
price_tab = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/main/div[3]/div[1]/section/div/div[5]/ul/li[2]/label/div')
price_tab.click()


# In[71]:


# applying color filter
color_tab = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/main/div[3]/div[1]/section/div/div[6]/ul/li[1]/label/div')
color_tab.click()


# In[72]:


# to find all elements and from different pages and save them in list
element_list4 = []

for page in range (0,2):
    page_url = "https://www.myntra.com/shoes?f=Color%3ABlack_36454f&rf=Price%3A7187.0_14125.0_7187.0%20TO%2014125.0" + str(page)
    driver = webdriver.Chrome(r"C:\Users\youra\OneDrive\Desktop\SAI_dsp35\Datatrained\chromedriver.exe")
    driver.get(page_url)
    brand_tag = driver.find_elements_by_class_name('product-brand')
    description_tag = driver.find_elements_by_xpath(".//div[@class='product-productMetaInfo']//h4[@class='product-product']")
    price_tag = driver.find_elements_by_xpath("//div[@class='product-price']")
    
    for i in range(len(brand_tag)):
        element_list4.append([brand_tag[i].text,description_tag[i].text,price_tag[i].text])
element_list4
    


# In[73]:


#making of dataframe
shoes = pd.DataFrame(element_list4)
shoes.columns = ['Brand','Product Description','Price']
shoes


# In[74]:


driver.close

Q8: Go to webpage https://www.amazon.in/
Enter “Laptop” in the search field and then click the search icon.
Then set CPU Type filter to “Intel Core i7” and “Intel Core i9” as shown in the below image:
    After setting the filters scrape first 10 laptops data. You have to scrape 3 attributesfor each laptop:
1. Title
2. Ratings
3. Price
As shown in the below image as the tick marked attributes.
Note: All the steps required during scraping should be done through code only and not manually.
# In[75]:


#import required libraries 
import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
import time
from selenium.common.exceptions import NoSuchElementException


# In[76]:


#connect to webdriver
driver = webdriver.Chrome(r"C:\Users\youra\OneDrive\Desktop\SAI_dsp35\Datatrained\chromedriver.exe")
time.sleep(2)

#to get url
driver.get(' https://www.amazon.in/')


# In[77]:


#finding elements for search bar and input laptop
search_product = driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']")
search_product.send_keys("Laptop")


# In[78]:


# to click search 
search_button = driver.find_element_by_xpath('//*[@id="nav-search-submit-button"]')
search_button.click()


# In[79]:


# to select i7 core model button
model = driver.find_element_by_xpath('//*[@id="p_n_feature_thirteen_browse-bin/12598163031"]/span/a/div/label/i')
model.click()


# In[80]:


a-icon a-icon-star-medium a-star-medium-4


# In[92]:


# to find brand  name of laptops
brands = driver.find_elements_by_xpath('//span[@class="a-size-medium a-color-base a-text-normal"]')
brands[:10]

brand = []
for i in brands:
    title =  i.text
    brand.append(title)
brand[:10]


# In[83]:


# to find ratings of the laptops
rating_tag = driver.find_elements_by_xpath("//span[@class='a-size-base a-color-base s-bold-weight-text']")
rating_tag[:10]

rating=[]
for i in rating_tag:
    title = (i.text)
    rating.append(title)
rating[:10]


# In[93]:


#making of dataframe from collected data
laptop = pd.DataFrame({})
laptop['Brand']=brand[:10]
laptop['Product Rating'] = rating[:10]
laptop

    


# In[ ]:


driver.close

Q9: Write a python program to scrape data for first 10 job results for Data Scientist Designation in Noida location. You have to scrape company name, No. of days ago when job was posted, Rating of the company. This task will be done in following steps:
1. First get the webpage https://www.ambitionbox.com/
2. Click on the Job option as shown in the image
3. After reaching to the next webpage, In place of “Search by Designations, Companies, Skills” enter “Data Scientist” and click on search button.
4. You will reach to the following web page click on location and in place of “Search location” enter “Noida” and select location “Noida”.
5. Then scrape the data for the first 10 jobs results you get on the above shown page.
6. Finally create a dataframe of the scraped data.
Note: All the steps required during scraping should be done through code only and not manually.

# In[94]:


#import required libraries 
import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
import time
from selenium.common.exceptions import NoSuchElementException


# In[95]:


#connect to webdriver
driver = webdriver.Chrome(r"C:\Users\youra\OneDrive\Desktop\SAI_dsp35\Datatrained\chromedriver.exe")
time.sleep(2)

#to get url
driver.get('https://www.ambitionbox.com/')


# In[96]:


# to select job link from main page
job_link = driver.find_element_by_xpath('/html/body/div[1]/nav/nav/a[6]').click()
job_link


# In[97]:


# get url
url = 'https://www.ambitionbox.com/jobs'
driver.get(url)


# In[98]:


# to search and click on data scientist in search bar
search_job = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div[1]/div/div/div/div/span/input')
search_job.send_keys("Data Scientist")


# In[99]:


search_button = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div[1]/div/div/div/button/span')
search_button.click()


# In[100]:


# to click location tab 
location = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[2]/div[1]/i')
location.click()


# In[101]:


# to click Noida in location
city = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div[3]/div[1]/div[5]/div/label')
city.click()


# In[102]:


url = 'https://www.ambitionbox.com/jobs/search?tag=Data%20Scientist&location=Noida'
driver.get(url)


# In[103]:


# to get company name
company = []
company_tag = driver.find_elements_by_xpath("//p[@class='company body-medium']")
company_tag

for i in company_tag:
    title = i.text
    company.append(title)
company[:10]

#To get how many days ago the job was posted
days = []
days_tag = driver.find_elements_by_xpath("//div[@class='other-info']//span[@class='body-small-l']")
days_tag

for i in days_tag:
    title = i.text
    days.append(title)
days[0:20:2]

#company rating
rating = []
rating_tag = driver.find_elements_by_xpath("//div[@class='rating-wrapper']//span[@class='body-small']")
rating_tag
for i in rating_tag:
    title = i.text
    rating.append(title)
rating[:10]


#making of dataframe from collected data
jobs = pd.DataFrame({})
jobs['Company Name']=company
jobs['Job posted'] = days[:10]
jobs['Rating'] = rating[:10]
jobs


# In[104]:


driver.close

Q10: Write a python program to scrape the salary data for Data Scientist designation.
You have to scrape Company name, Number of salaries, Average salary, Minsalary, Max Salary. The above task will be, done as shown in the below steps:
1. First get the webpage https://www.ambitionbox.com/
2. Click on the salaries option as shown in the image.
3. After reaching to the following webpage, In place of “Search Job Profile” enters “Data Scientist” and then click on “Data Scientist”.
You have to scrape the data ticked in the above image.
4. Scrape the data for the first 10 companies. Scrape the company name, total salary record, average salary, minimum salary, maximum salary, experience required.
5. Store the data in a dataframe.
Note: All the steps required during scraping should be done through code only and not manually
# In[105]:


#import required libraries 
import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
import time
from selenium.common.exceptions import NoSuchElementException


# In[106]:


#connect to webdriver
driver = webdriver.Chrome(r"C:\Users\youra\OneDrive\Desktop\SAI_dsp35\Datatrained\chromedriver.exe")
time.sleep(2)


#to get url
driver.get('https://www.ambitionbox.com/')


# In[107]:


#to select salary tab from main page
salary_link = driver.find_element_by_xpath('//a[@class="link salaries"]').click()
salary_link


# In[108]:


#to search for data scientist jobs in search bar
search_job = driver.find_element_by_xpath('//*[@id="jobProfileSearchbox"]')
search_job.send_keys("Data Scientist")


# In[111]:


#to click search bar
btn = driver.find_element_by_xpath('//*[@id="salaries"]/main/section[1]/div[2]/div[1]/span/div/div/div[1]/div/div/p').click()
btn


# In[112]:


#to get company names
company_tag = driver.find_elements_by_xpath("//div[@class='name']/a")
company_tag 

company = []
for i in company_tag:
    title = i.text
    company.append(title)
company

#to get salary records
salary_based = driver.find_elements_by_xpath("//div[@class='name']/span")
salary_based

salary = []

for i in salary_based:
    title = i.text
    salary.append(title)
salary

#TO get experience required
expirence = driver.find_elements_by_xpath("//div[@class='salaries sbold-list-header']")
expirence

expirence_years = []

for i in expirence:
    title = i.text
    expirence_years.append(title)
expirence_years

# to find minimum salary
min_salary = driver.find_elements_by_xpath("//div[@class='salary-values']/div[1]")
min_salary

minimum_salary = []

for i in min_salary:
    title = i.text
    minimum_salary.append(title)
minimum_salary

#to find maximaum salary
max_salary = driver.find_elements_by_xpath("//div[@class='salary-values']/div[2]")
max_salary

maximum_salary = []

for i in max_salary:
    title = i.text
    maximum_salary.append(title)
maximum_salary

#to find average salary
avg_salary = driver.find_elements_by_xpath("//p[@class='averageCtc']")
avg_salary

average_salary = []

for i in avg_salary:
    title = i.text
    average_salary.append(title)
average_salary


# In[113]:


#making of dataframe from collected data
jobs1 = pd.DataFrame({})
jobs1['Company Name']= company
jobs1['Total Salaries Record '] = salary
jobs1['Experience Required'] = expirence_years
jobs1['Minimum Salary']= minimum_salary
jobs1['Maximum']= maximum_salary 
jobs1['Average_salary']= average_salary
jobs1


# In[114]:


driver.close


# In[ ]:


####################################################################################################################


# In[ ]:


############################################################################################################################


# In[ ]:




