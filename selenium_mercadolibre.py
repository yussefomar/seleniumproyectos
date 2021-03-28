import unittest
from pyunitreport import HTMLTestRunner
from time import sleep
from selenium import webdriver
 
 
 
class TestingMercadoLibre(unittest.TestCase):

	def setUp(self):
		self.driver= webdriver.Firefox(executable_path=r"C:\driverfirefox\geckodriver")
		driver=self.driver
		driver.get('https://www.mercadolibre.com')
		driver.maximize_window()
		#driver.set_window_size(800, 600)
	def test_search_ps4(self):
		driver=self.driver
		country=driver.find_element_by_id('CO')
		country.click()

		search_filed=driver.find_element_by_name('as_word')
		search_filed.click()
		search_filed.clear()
		search_filed.send_keys('playstation 4')
		search_filed.submit()
		sleep(3)	
		location=driver.find_element_by_partial_link_text('Bogotá D.C.')
		location.click()
		sleep(3)
		condition=driver.find_element_by_partial_link_text('Nuevo')
		condition.click()
		sleep(3)
		order_menu=driver.find_element_by_xpath('/html/body/main/div/div/section/div[1]/div/div/div[2]/div[1]/div/div/button')
		order_menu.click()
		sleep(3)
		
		high_price=driver.find_element_by_xpath('/html/body/main/div/div/section/div[1]/div/div/div[2]/div[1]/div/div/div/ul/li[3]/a/div/div')
		high_price.click()
		sleep(3)

		articles=[]
		prices=[]

		for i in range(1,5):
			article_name=driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{i}]/div/div/div[2]/div[1]/a/h2').text
			articles.append(article_name)
		 	#article_price=driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[1]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/span[1]').text
		 	#prices.append(article_price)
		#/html/body/main/div/div/section/div[1]/div/div/div[2]/div[1]/div/div/button
		print(articles,prices)
	def tearDown(self):
		self.driver.close()
		 
				
if __name__ == "__main__":
	unittest.main(
		verbosity=2,
		testRunner= HTMLTestRunner(
			output='mercadolibre-reporte',
			report_name='hackem-report')
		)				