import requests
from bs4 import BeautifulSoup

print("""
예시 : 
검색할 단어를 입력해주세요 : pkgconfig
찾을 issue 페이지 링크를 붙여넣어 주세요 : https://github.com/csi2115-f21/scripts/issues
""")
word = input("검색할 단어를 입력해주세요 : ")
URLs = input("찾을 issue 페이지 링크를 붙여넣어 주세요 : ")

print(type(URLs))

issue_store = requests.get(URLs)
issue_store.raise_for_status()
print(issue_store)  # <Response [200]>

issue_soup = BeautifulSoup(issue_store.text, "lxml")
max_open = issue_soup.find("span", {"class": "opened-by"}).get_text()
num = []
for i in range(max_open.index('#')+1, max_open.index('#') + 5):
    if max_open[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        break
    else:
        num.append(max_open[i])

max_num = int(''.join(map(str, num)))

print(max_num)
result = []
print(f"doing well..")

for n in range(1, max_num+1):
    if n % 5 == 0:
        print(f"{n} doing..")

    page_url = URLs + "/" + str(n)
    page_store = requests.get(page_url)
    page_store.raise_for_status()

    page_soup = BeautifulSoup(page_store.text, 'lxml')
    isOpen = page_soup.find("span", {"class": "State"}).get_text()
    isOpen = isOpen.strip('\n')
    contents = page_soup.find_all(
        "tr", {"class": "d-block"})
    for content in contents:
        co_text = content.get_text()
        if word in co_text:
            print(
                f"\nI found {word} from number #{n} and It is {str(isOpen)} Issue!")
            print(f"Do you wanna go there? {page_url}")
            result.append(n)
            break
if len(result) == 0:
    print(f"I am Sorry, I couldn't find {word} from anywhere.")
else:
    for r in range(len(result)):
        print(f"# {result[r]} ", URLs + "/" + str(result[r]))
