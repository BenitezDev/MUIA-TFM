from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, os, json

# method to get the downloaded file name
def getDownLoadedFileName():
	driver.execute_script("window.open()")
	# switch to new tab
	driver.switch_to.window(driver.window_handles[-1])
	# navigate to chrome downloads
	driver.get('chrome://downloads')
	# return the file name once the download is completed
	return driver.execute_script("return document.querySelector('downloads-manager').shadowRoot.querySelector('#downloadsList downloads-item').shadowRoot.querySelector('div#content  #file-link').text")

def parseJSON(filename):
	with open(filename) as json_file:
		data = json.load(json_file)
		os.remove(filename)
		return data

def setupDriver():
	chrome_options = webdriver.ChromeOptions()
	# chrome_options.add_argument('headless')
	prefs = {"download.default_directory": os.getcwd()}
	chrome_options.add_experimental_option("prefs", prefs)


	# Provide the path of chromedriver present on your system.
	driver = webdriver.Chrome(executable_path="chromedriver",
							  chrome_options=chrome_options)
	driver.set_window_size(1080,1920)

def parseJSON(filename):
	# Send a get request to the url
	driver.get('https://www.f-uji.net/index.php?action=test')

	# fill the url
	element = driver.find_element(by=By.ID, value="pid")
	element.send_keys("https://doi.org/10.1186/2041-1480-4-37")

	# click the button
	driver.find_element(by=By.NAME, value="runtest").click()


	# wait and download the JSON
	try:
		element = WebDriverWait(driver, 30).until(
			EC.presence_of_element_located((By.NAME, "downloadtest"))
		)
		# download the JSON
		driver.get('https://www.f-uji.net/export.php')
		time.sleep(3)

		# get the file name
		file_name = getDownLoadedFileName()
		full_path = os.getcwd()  + "/" +  file_name

		data = parseJSON(full_path)
		print(data)

	finally:
		driver.quit()
		print("Done")


