from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
def main():
    global w
    w.get('https://wenku.baidu.com/view/38f873e6a32d7375a51780af?aggId=4a8db36d834d2b160b4e767f5acfa1c7aa008286&fr=catalogMain_text_ernie_recall_backup_new%3Awk_recommend_main2&_wkts_=1700488538167&bdQuery=%E9%98%BF%E6%88%BF%E5%AE%AB%E8%B5%8B%E7%BF%BB%E8%AF%91PPT')
    sleep(2)
    css='div[data-v-04431faa][class="btn unfold"]'
    while True:
        try:
            e=w.find_element(By.CSS_SELECTOR,css)
            break
        except:
            pass
    w.execute_script('arguments[0].click();',e)
    print('done.')
    html = w.execute_script("return document.documentElement.outerHTML")
    with open('html.html','w',encoding='utf-8') as f:
        f.write(html)
    css='p[v-pre]'
    es=w.find_elements(By.CSS_SELECTOR,css)
    s=''
    for element in es:
        s+=e.text+'\n'
    print(len(es))
    input()
    print(s)
    pass


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    w=webdriver.Edge()
    main()
