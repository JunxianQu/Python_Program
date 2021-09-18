def todict(json):
    json_tuple = json.split("\"")
    print(json_tuple)

    s = []  # key栈
    ans = {}  # the final answer

    # con1作为一个字典List来用。每当遇到一个{，就执行ans_temp.append(dict())，在ans_temp中加一个空字典，用于添加子字典。

    # con2每当遇到一个}，就执行ans_temp.pop()，弹出一个子字典作为value元素。至于弹出的字典属于哪个key，再分为两种讨论

    # con3第一种，是直接到了file的根目录，也就是该字典对应的key是第一层{}中的元素，如username1。这种情况下，直接让ans[key] = ans_temp.pop()就可以了。file根目录的条件，就是这里的元素不在任何一个子{}。有两个等同的判断方式，第一个是key栈pop后为空，第二个是ans_temp在pop后为空。

    # con4第二种情况，就是弹出的字典仍然是file的子目录中的元素，如username2、3、4、5、6、7、8、9。这种情况，ans_temp.pop()的结果，应该是此时ans_temp[len(ans_temp)]字典中的元素。即应有ans_temp[len(ans_temp)][key] = ans_temp.pop()
    ans_temp = []

    for i in range(1, len(json_tuple)):  # 从1开始计数。第一个{忽略不计
        ti = json_tuple[i]

        if '{' in ti:  # 对应上面的con1
            ans_temp.append(dict())

        elif i < len(json_tuple) - 1 and ":" in json_tuple[i + 1]:  # 后面的元素含有":"时，说明这个元素为key值，压入key栈s
            s.append(ti)

        elif '}' in ti:  # 对应con2
            size = ti.count('}', 0, len(ti))  # 数}数量
            if (i == len(json_tuple) - 1):  # 如果到了最后一个元素，要去除一个}的计数，因为第一个{忽略不计了
                size = size - 1
            while (size > 1):  # 如果}数目比1大，说明还没到根目录，对应con4
                temp = {}
                ans_temp[len(ans_temp) - 1][s.pop()] = ans_temp.pop()
                size = size - 1
            if len(ans_temp) == 1:  # 到了根目录，对应con3
                ans[s.pop()] = ans_temp.pop()
            elif size == 1:  # 没到根目录，对应的场景是{1:{2:{3:4},5:6}}中跟在4后面的}的位置
                ans_temp[len(ans_temp) - 1][s.pop()] = ans_temp.pop()

        elif ':' in ti or ',' in ti:  # 无关元素跳过
            continue
        #
        else:  # 中间value值压入ans_temp或者ans的计算
            if len(s) == 1:  # key栈只有一个key，那就是在根目录了，
                ans[s.pop()] = ti
            elif len(s) > 1:  # 还没到根目录，那就将元素压入ans_temp[len(ans_temp)-1]中。这里，ans_temp的最后一个子字典，就是该key：value对应所处的括号区域
                ans_temp[len(ans_temp) - 1][s.pop()] = ti
    return ans

with open("to_dic.json") as file:
  print(file.read())