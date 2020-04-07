import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

def update_question_links(question_links):
  with open('question_links.txt') as f:
    links =  f.read()

  links = links.split('\n')

  for each in links:
    if '/problems/' in each:
      question_links.append(each)

def get_question(question_link):
  #This example requires Selenium WebDriver 3.13 or newer
  with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get(question_link)
    wait.until(lambda d: d.find_element_by_tag_name("p"))

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    print('-------------------------------------------')
    print(soup.title.string.split('|')[0])
    print('-------------------------------------------')

    description_div = soup.find_all(class_="description__24sA")[0]

    question_text = description_div.find_all(["p", "pre", "li"])

    for node in question_text:
      print(node)
    
    
    
def main():
  question_links = []
  update_question_links(question_links)
  
  TEST_LEETCODE_1 = "https://leetcode.com/problems/regular-expression-matching/"
  TEST_LEETCODE_2 = "https://leetcode.com/problems/count-of-smaller-numbers-after-self/"

  get_question(TEST_LEETCODE_1)

  # for each_question_link in question_links:
  #   try:
  #     print(get_question(each_question_link))
  #     print('------------------------------')

  #   except:
  #     continue

if __name__=='__main__':
  print('\n')
  main()
  
