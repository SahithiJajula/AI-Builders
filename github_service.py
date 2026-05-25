import requests

def fetch_repo(repo):

    url=f"https://api.github.com/repos/{repo}/contents"

    response=requests.get(url)

    if response.status_code!=200:

        return ""

    files=response.json()

    collected=""

    for file in files:

        name=file["name"]

        if name.endswith(

        (

        ".py",

        ".js",

        ".java",

        ".cpp",

        ".c"

        )

        ):

            raw=requests.get(

            file["download_url"]

            )

            collected+=raw.text

    return collected
