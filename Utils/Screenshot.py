import base64
import time
from io import BytesIO
from PIL import Image
from selenium import webdriver



class Screenshot:

    def __init__(self,driver):
        self.driver = driver

    def full_page(self,screenshot_name):
        screenshot_data = self.driver.execute_cdp_cmd("Page.captureScreenshot", {
            "format": "png",
            "fromSurface": True,
            "captureBeyondViewport": True

        })

        image_data = base64.b64decode(screenshot_data['data'])
        image = Image.open(BytesIO(image_data))
        image.save(screenshot_name)

        print("Screenshot.png saved")

        time.sleep(1)

