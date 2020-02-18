def read(data):
    ''
    ''' This function should receive a dictionary (see the json file format) and return a list of rows
    For example: 
    data = {
            "names": ["Son", "Thao"], 
            "posted_at": ["16/02/2020 22:37", "16/02/2020 22:39"],
            "messages": ["Hello", "Hi"]
            }

    rows = [
            ("Son", "16/02/2020 22:37", "Hello"), 
            ("Thao", "16/02/2020 22:39", "Hi")
            ]
    Bonus: You might want to show the latest messages first. How would you do that?
    '''
    # Your code here
    rows = []
    # adding a tuple for each dictionary entry
    for i in range(len(data["messages"])):
        rows += [(data["names"][i], data["posted_at"][i], data["messages"][i])]

    return rows


def write(rows, name, message):
    from datetime import datetime
    ''' This function should receive a list of rows, a name and a message (string), and return a dictionary.
    For example:
    rows = [
            ("Thao", "16/02/2020 22:39", "Hi"),
            ("Son", "16/02/2020 22:37", "Hello")
            ]
    name = "Anonymous"
    message = "Hello world"
    
    data = {
            "names": ["Son", "Thao", "Anonymous"], 
            "posted_at": ["16/02/2020 22:37", "16/02/2020 22:39", "<current system date time>"],
            "messages": ["Hello", "Hi", "Hello world"]
            }
    Note also the format of the date time should be the same as in the original data.
    '''
    # Your code here
    data = {"names": [], "posted_at": [], "messages": []}
    for row in rows:
        data["names"].append(row[0])
        data["posted_at"].append(row[1])
        data["messages"].append(row[2])

    data["names"].append(name)
    data["posted_at"].append(datetime.now().strftime("%d/%m/%Y %H:%M"))
    data["messages"].append(message)

    # print(type(datetime.now().isoformat()))
    return data


def checkLen(rows):
    ''
    ''' This function should return the length of rows. 
    We also want to show maximum 20 messages on our message board.
    If there are more than 20 in the data file, you should show the 20 latest messages.
    '''
    # Your code here
    return len(rows)