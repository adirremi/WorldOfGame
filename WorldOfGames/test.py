
from selenium import webdriver
from time import sleep



def test_scores_service():
    print("test is start")
    driver = webdriver.Chrome(executable_path="/Users/adirremi/Desktop/chromedriver2")
    driver.get("http://0.0.0.0:8777/ScoreFlask")
    firstrank = driver.find_element_by_xpath("/html/body/table/tbody/tr[3]/td[2]").text
    secrank = driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td[2]").text
    #print(firstrank,secrank)
    sleep(3)
    if int(firstrank) < 1000:
        if int(secrank) > 1:
            print('all good')
            return True
    print('something went wrong')
    return False

def main_function():
    code = test_scores_service()
    if code:
        exit(0)
    else:
        exit(-1)


#test part
print("test part is starting")
print(main_function())