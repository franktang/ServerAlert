
def frequency_check(data, list):
    actionSet = {"comment":"评论","answer":"回答","question":"提问"}
    list.reverse()
    count =0
    for target in list:
        if data['action']==target['action'] and data['time'] - target['time'] <=60:
            count+=1
    if count >=9:
        print(data['user'] + ",频繁"+actionSet.get(data['action']))
    list.reverse()
    

def duplication_check(data, list):
    actionSet = {"comment":"评论","answer":"回答","question":"提问"}
    list.reverse()
    count =0
    for target in list:
        if data['action']==target['action'] and data['content'] == target['content']:
            count+=1
    if count >=9:
        print(data['user'] + ",重复"+actionSet.get(data['action']))
    list.reverse()
   
def evaluate(data, list):
    frequency_check(data, list)
    duplication_check(data, list)
