from openai import OpenAI

import os

from dotenv import load_dotenv

load_dotenv()

client=OpenAI(

api_key=

os.getenv(

"OPENAI_KEY"

)

)

def analyze_code(code):

    security=[]

    bugs=[]

    performance=[]

    if "password=" in code:

        security.append(

        "Hardcoded password found"

        )

    if "eval(" in code:

        security.append(

        "Unsafe eval detected"

        )

    if "while True" in code:

        performance.append(

        "Potential infinite loop"

        )

    if "==" in code:

        bugs.append(

        "Review equality checks"

        )

    prompt=f"""

Review this code.

Give concise summary.

Code:

{code[:6000]}

"""

    try:

        response=

        client.chat.completions.create(

        model="gpt-4.1-mini",

        messages=[

        {

        "role":"user",

        "content":prompt

        }

        ]

        )

        summary=response.choices[0].message.content

    except:

        summary="AI unavailable"

    return(

    security,

    bugs,

    performance,

    summary

    )
