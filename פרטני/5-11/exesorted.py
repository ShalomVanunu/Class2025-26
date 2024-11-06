
dic_lst= [ ['123','rishon'], ['100', 'bne berak'],['200','nes ziona']]

def second_key(value):
    return value[1]

new_dic = sorted(dic_lst, key=second_key)

print(new_dic)