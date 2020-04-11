import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import sys

def update_question_links(question_links):
  with open('question_links.txt') as f:
    links =  f.read()

  links = links.split('\n')

  for each in links:
    if '/problems/' in each:
      linkSplit = each.split('/')
      question_links.append([each, linkSplit[4]])

def get_question(question_link, file):
  #This example requires Selenium WebDriver 3.13 or newer
  with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get(question_link)
    wait.until(lambda d: d.find_element_by_tag_name("p"))

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    file.write('-------------------------------------------\n')
    file.write(soup.title.string.split('|')[0] + '\n')
    file.write('-------------------------------------------\n')

    description_div = soup.find_all(class_="description__24sA")[0]

    question_text = description_div.find_all(["p", "pre", "li"])

    for node in question_text:
      if node.name == "li":
        file.write('- ' + node.get_text() + "\n")
      else:
        file.write(node.get_text() )
  
def main():
  print('Now finding problems')
  question_links = []
  update_question_links(question_links)

  for each_question_link in question_links:
    problemTitle = each_question_link[1]
    print(f"Now parsing {problemTitle}")
    with open(f"problems\{problemTitle}.txt", 'w') as file:
      get_question(each_question_link[0], file)

if __name__=='__main__':
  print('\n')
  main()
  
