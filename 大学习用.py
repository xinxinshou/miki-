s='''
南琨	2020-07-20
李迅	2020-07-20
任瑞凯	2020-07-20
祝高	2020-07-20
仝博宇	2020-07-20
兰远翔	2020-07-20
郑涵渝	2020-07-20
赵常闯	2020-07-20
冯大仕	2020-07-20
倪孝宝	2020-07-20
岳佳乐	2020-07-20
郭宏驰	2020-07-20
何建	2020-07-20
郭鹏	2020-07-20
李家鑫	2020-07-20
戴致金	2020-07-20
高若彬	2020-07-20
蒋杰名	2020-07-20
袁先宇	2020-07-20
丁克凡	2020-07-20
李从政	2020-07-20
孙靖森	2020-07-20
任梦妍	2020-07-20
甘君龙	2020-07-20
郑薛健	2020-07-20
丁喆立	2020-07-20
胡玉城	2020-07-20
戴雨乔	2020-07-20
曾玲斌	2020-07-20
唐志远	2020-07-20
康志远	2020-07-20
李飞翔	2020-07-20
冯阳	2020-07-20
朱晓颖	2020-07-20
李子迈	2020-07-20
何旻	2020-07-20
方静静	2020-07-20
'''
lis=s.split()
n=0
s2=['冯阳','胡玉城','李子迈','郑涵渝','朱晓颖','曾玲斌','康志远','李家鑫','李飞翔','姜公淳','梁宇飞','戴雨乔']
print("应到",len(s2),"人")
for n in range(len(s2)):
    if(s2[n] not in lis):
        print(s2[n])
        n+=1
        print(n)