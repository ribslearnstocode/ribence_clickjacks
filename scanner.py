# importing modules
import requests
import pyfiglet
from selenium import webdriver

# printing header
text = pyfiglet.figlet_format("RIBENCE")
print(text)

# getting url
url = input("Enter the target: ")
try: 
	if "https://" in url:
		convert = url
	else:
		convert = "https://"+url

	# checking for ClickJacking vulnerability
	header = requests.get(convert).headers
	if 'X-Frame-Options' in header:
		print(url+" isn't vulnerable to ClickJacking")
	else:
		print(url+" is vulnerable to ClickJacking")

	# checking weather the site has sitemap enabled or not
	sitemap = requests.get(convert+"/sitemap.xml")
	if sitemap.status_code==200:
		print("[+]Sitemap Enabled in "+url)
	else:
		print("[+]Sitemap Disabled in "+url)

	saveitas = input("Enter the file name to save the picture: ")
	DRIVER = 'chromedriver'
	driver = webdriver.Chrome(DRIVER)
	driver.get(convert)
	if '.png' in saveitas:
		screenshot = driver.save_screenshot(saveitas)
		print("Image is successfully saved on screenshots folder, do check it :) ")
	else:
		print("Please save the picture with .png extension :) ")
	driver.quit()
except:
	print("Please Enter the website name clearly :)")
