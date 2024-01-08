from fastapi import FastAPI

from duckduckgo_search import DDGS

import mojito




app = FastAPI()

@app.get("/api/python")
def hello_world():

    rlist=[]

    with DDGS() as ddgs:
        keywords = 'tesla'
        ddgs_videos_gen = ddgs.videos(
        keywords,
        region="wt-wt",
        safesearch="off",
        timelimit="w",
        resolution="high",
        duration="medium",
        max_results=100,
        )
        for r in ddgs_videos_gen:
            print(r)
    rlist.append(mojito.__version__)

    # print(''.join(rlist))
    return {"message": ''.join(rlist)}