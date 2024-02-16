

@app.post("/tasks")
async def add_task(
        task: STaskAdd
):
    tasks.append(task)
    return {"ok": True}




'''
@app.get("/tasks")
def get_tasks():
    task = STask(name="Zapishi taski v notion")
    return {"data": task}
'''
