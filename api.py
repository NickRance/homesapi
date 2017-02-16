from flask import Flask
from flask_restful import Resource, Api, request
from selenium import webdriver
import json
import sys
import time

##Web Server Code

app = Flask(__name__)
api = Api(app)

class Server(Resource):
    def get(self):
        uri_param = request.args.get('uri')
        #return (json.dumps(uri_to_imagelist(uri_param)))
        #call_processingonblah()
        return {'result':uri_to_imagelist(uri_param)}

api.add_resource(Server, '/')


##Backend Code

def uri_to_imagelist(uri):
    final_image_list = []
    uri_param = uri
    driver = webdriver.Chrome('chromedriver/chromedriver')
    driver.get("http://homes.com/" + uri_param)
    time.sleep(3)
    first_image_url = driver.find_element_by_class_name("img").get_attribute("src")
    gallerySize = int((driver.find_element_by_xpath(
        '//*[@id="main"]/article/div[2]/div[1]/div[3]/div/div[1]/div[1]/div/div/div/div[1]/div/span[2]')).text)
    for i in range(1, gallerySize + 1):
        final_image_list.append(first_image_url.replace('_1', "_" + str(i)))
    # print(first_image_url, file=sys.stderr)
    driver.quit()
    return final_image_list



if __name__ == '__main__':
    app.run(debug=True)