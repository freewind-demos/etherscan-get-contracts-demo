import requests
import re
from pathlib import Path

ROOT = Path(__file__).parent

for i in range(1, 20):
    url = "https://etherscan.io/contractsVerified/{}".format(i)
    content = requests.get(url).text
    urls = re.compile(r"(?<=href=')/address/.*?(?=')").findall(content)
    print(urls)
    for url in urls:
        code_url = "https://etherscan.io{}".format(url)
        code_page = requests.get(code_url).text
        # print(code_page)
        code = re.compile("(?<=<pre class='js-sourcecopyarea' id='editor' style='height: 330px; max-height: 450px; margin-top: 5px;'>).*?(?=</pre)", re.DOTALL).findall(code_page)
        print(code)
        file_name = re.compile("(?<=address/).*?(?=#)").findall(url)[0]
        (ROOT / "solidity-files" / "{}.sol".format(file_name)).write_text(code[0])
