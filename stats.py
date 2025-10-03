def get_book_text(file_path):
    with open(file_path, encoding="utf-8") as f:
        return f.read()
    
def count_word(book_text):
    return len(book_text.split())


def count(book_text):
    dic = {}
    
    book_text.lower()
    for char in book_text.lower():
        if char in dic.keys():
            dic[char] += 1
        else :
            dic[char] = 1
    return dic


def sorted_count(char_dic):
    
    sorted_list = []
    item_dic = {}
    for item in char_dic.keys():
        if item.isalpha():
            sorted_list.append(char_dic.fromkeys(item,char_dic[item]))
    sorted_list.sort(key= lambda x:list(x.values()),reverse= True)   
    return sorted_list