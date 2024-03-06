import asyncio
from datetime import datetime
import json


async def task_1():
    with open("data_1.json", "r") as file:
        data = json.load(file)
    print("Task 1 completed")
    await task_2(data)


async def task_2(data):
    ls = [[], [], []]
    for i in data["cars"]:
        ls[0].append(i["name"])
        ls[1].append(i["brand"])
        ls[2].append(i["price"])
    data_y = {
            "names": f"{ls[0]}",
            "brands": f"{ls[1]}",
            "price": f"{ls[2]}"
            }
    with open("data_2.json", "w") as f:
        json.dump(data_y, f, indent=6)
    print("Task 2 completed")


async def main():
    await asyncio.gather(task_1())


if __name__ == "__main__":
    asyncio.run(main())

