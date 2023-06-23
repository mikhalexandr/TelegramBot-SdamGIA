import requests


def remove_commas(string):
    trans_table = {ord("'"): None}
    return string.translate(trans_table)


def get_cheat_image():
    url = "https://5-ege.ru/wp-content/uploads/2012/04/matematika-formuly.jpg"
    response = requests.get(url)
    with open("image1.png", 'wb') as f:
        f.write(response.content)
    return response.content

