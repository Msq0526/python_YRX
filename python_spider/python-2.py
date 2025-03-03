import requests
from bs4 import BeautifulSoup
import re

url = 'http://www.glidedsky.com/level/web/crawler-basic-1'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'Cookie':'footprints=eyJpdiI6Im82U1M2eEk5K0ZZOU1BN1VNaGtzcUE9PSIsInZhbHVlIjoia2t6NjNCSkNudTBCajRrREhORzJCZThlTlwvdlMrOFFrMHpkTmthT2ZkMDNPbFJhN25IZWl0TzhlcFo0dzhRMlMiLCJtYWMiOiI3ZDk0ZDRkMjFhMTJhNzVkMzNhYjc3ZjQ2NWE1MGRkZmRmNzQ1NGIyZmYwMjMzZDliOTgzMTU2YzI1ODcxMWY3In0%3D; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6InhrcmsrcUJ4dmNqQmJmOGd5SlZIN1E9PSIsInZhbHVlIjoiRXc5M1FBQ2NJbkFoNjJGVkJnTjRXSWwzRFNycXNWSWVPcXNFRDhsMDR4dXpoUk4wd0ZQdVJWRGdXdDdmOUNhOEI3WDAxMytKTDhpM0pMMFwvSTlmRjk0TW9BZHFWQ2dWXC91STNpMnB0TFM0R09Va0dnb2VZcytnNkg4ckNMU0htSVhQRVRhalpHeVVWbG9IbFZLTVwvb3hROVU3dlgzXC9NRms2SlFnVXlVMEp0WT0iLCJtYWMiOiJmOWU1ZjdjYmIwODFkODMzNzZlZDI5NWUyN2UyYjRkMThmYTg4OThmMzExNTI0NDk2YjM0ZTYyZDEwZjgzNGExIn0%3D; XSRF-TOKEN=eyJpdiI6IkxnV2hzMFhQMnJ2R2ErZmlrTW9USVE9PSIsInZhbHVlIjoic3U1R2M4UEFnV2Zld3BlSjl6eUJKc0RIN2JmUXFiSXlMbXg2dFYyWXE0R1wvbXhuNlJoXC9NVlwvV1hoaFFSNWlxKyIsIm1hYyI6IjNmYjc2ZTQ2YmVmYWE3YTliZDMxMjU4MzhjYjczNWJiYTA0NDk1NzRhMzE2MGM5NmU2Mjk2NGNmNjQ4NzFmYjcifQ%3D%3D; glidedsky_session=eyJpdiI6IjFsV0Y3VERVc0E5U3NsWVRtT21PelE9PSIsInZhbHVlIjoiUjU3eXkwaCsxb1ZHclY3NkNWOXZ2ZG5SUUhjXC91TWluOExzNnpNOVwvanVMQTg3Rzl0czVJSVVKenp1N3hoRjIyIiwibWFjIjoiNzg3OWJiNGQ0MGMyNzYzMTI1M2UwOTI5YTk0MDA0ODUzZjNkZmVkN2ZlZjA4OGE4NmI0NmZiNmE4NmEyNzQ4OCJ9'

}

num = 0

response = requests.get(url, headers=headers).text
soup = BeautifulSoup(response,'html.parser')
for temp in soup.find_all('div',{'class':'col-md-1'}):
    temp = int(temp.text.strip())
    num += temp
print(num)