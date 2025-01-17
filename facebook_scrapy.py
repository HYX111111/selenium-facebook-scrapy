from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 初始化浏览器驱动
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 打开 Facebook 登录页面
driver.get('https://www.facebook.com/')

# 等待页面加载
time.sleep(5)

# 找到用户名和密码输入框并输入
username_input = driver.find_element(By.ID, 'email')
username_input.send_keys('61571407847012')

password_input = driver.find_element(By.ID, 'pass')
password_input.send_keys('Bo0701loco1995')

# 找到登录按钮并点击
login_button = driver.find_element(By.NAME, 'login')
login_button.click()

# 等待登录完成
time.sleep(10)


# 假设我们要访问的人物 ID 为 '123456789'，根据人物 ID 访问页面
person_id = '61571407847012 '
driver.get(f'https://www.facebook.com/profile.php?id={person_id}')

# 等待页面加载
time.sleep(10)

# 尝试提取出生年月，这里假设出生年月在一个元素中，其 class 为 'birth-date'
birth_date_element = driver.find_element(By.CLASS_NAME, 'birth-date')
birth_date = birth_date_element.text
print(birth_date)

# 关闭浏览器
driver.quit()