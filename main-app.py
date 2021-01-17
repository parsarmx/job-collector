from selenium import webdriver
import pyautogui
import pyperclip

with open("D:\Projects\parsa.txt", "w", encoding="utf-8") as file:
    j = 1
    while j <= 7:
        if j <= 7:
            i = 0
            j1 = str(j)
            path = "C:\Program Files (x86)\chromedriver.exe"
            pager = 'https://jobinja.ir/collection/%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D9%86%D9%88%DB%8C%D8%B3-PYTHON?filters%5Bkeywords%5D%5B0%5D=python&page='
            page = (pager + j1)
            print(page)
            print('Collecting Data...')
            driver = webdriver.Chrome(path)
            driver.get(page)
            title = driver.title
            search = driver.find_element_by_name("keyword")
            mains = driver.find_elements_by_class_name("c-jobListView__titleLink")  # semat
            main = driver.find_element_by_class_name("c-jobListView__titleLink")
            for main in mains:
                link = driver.find_element_by_link_text(main.text)
                link.click()
                pyautogui.press('f6')
                pyautogui.hotkey('ctrl', 'c')
                my_url = pyperclip.paste()
                file.write(my_url + "\n")

                i += 1
            j += 1
            driver.quit()

        else:
            quit()
