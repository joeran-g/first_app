import json


def get_data():
    with open("data/blog_data.json", 'r', encoding="UTF-8") as handle:
        data = json.load(handle)
        return data


def save_data(data_list:list[dict]):
    with open("data/blog_data.json", 'w', encoding="UTF-8") as handle:
        json.dump(data_list, handle)


def add(data_dict:dict):
    """ Adds a single dictionary to the JSON list of dicts."""
    data = get_data()
    data.append(data_dict)
    save_data(data)


def update(blog_id:int, title:str, content:str):
    """ Update title and content of the given blog id """
    data = get_data()
    for blog in data:
        if blog['id'] == blog_id:
            blog['title'] = title
            blog['content'] = content
    save_data(data)


def delete(blog_id:int):
    data = get_data()
    for blog in data:
        if blog['id'] == blog_id:
            data.remove(blog)
    save_data(data)

