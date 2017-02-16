from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import sys

#accepts a property uri string e.g. property/3611-bell-st-norfolk-va-23513/id-400028631997/ returns list of image_urls



driver = webdriver.Chrome('vendor/chromedriver/chromedriver')
final_dict={}
final_output = []
temp_output=[]
uri_param = "property/3611-bell-st-norfolk-va-23513/id-400028631997/"


driver.get("http://homes.com/"+uri_param)
time.sleep(2)
images=driver.find_elements_by_class_name("img")
print('images:')
print(images)
for image in images:
    final_output.append(image.get_attribute("src"))
print(final_output)
gallerySize=driver.find_element_by_xpath('//*[@id="main"]/article/div[2]/div[1]/div[3]/div/div[1]/div[1]/div/div/div/div[1]/div/span[2]')
print('gallery size:')
print(gallerySize)
print("gallerySize Text:" +gallerySize.text)
gallerySizeint = int(gallerySize.text)
# for item in gallerySize:
#     print(item.text)
#     gallerySizeint= int(item.text)
basewebsite = final_output[0]
print(basewebsite)

for i in range(1,gallerySizeint+1):
    temp_output.append(basewebsite.replace('_1',"_"+str(i)))

print(temp_output)

find_single_image = driver.find_element_by_class_name("img")
print('image:')
print(find_single_image.get_attribute("src"))
# siteaslist = basewebsite.split('/')
# print(siteaslist)
# last_part=siteaslist[-1]
# print(last_part)
# last_part_minus_extension = last_part.split('.')[0]
# print(last_part_minus_extension)
# image_number = last_part_minus_extension.split('_')[1]
# print(image_number)
# for i in range(0,gallerySizeint):
#      temp_output.append(str(image_number))
#      image_number = int(image_number)+1
# print(temp_output)


driver.quit()