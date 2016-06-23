# coding: UTF-8
import linecache

def make_graph(data_file,graph):#グラフを作る
    num = int(data_file.readline())#頂点の数
    
    for i in range(0,num):#各頂点の情報を作る
        vertex = {'name':data_file.readline().rstrip("\n"),'point1':100.0,'point2':0.0,'follow':[]}
        graph.append(vertex)
        
    num2 = int(data_file.readline())#辺の数

    for i in range(0,num2):#各頂点に辺の情報を入れる
        pre_foll= data_file.readline().split()
        previous=pre_foll[0]
        for j in range(0,num):
            if graph[j]['name']==previous:
                graph[j]['follow'].append(pre_foll[1].rstrip("\n"))
                break

    return(num,graph)

def page_rank(num,graph,times):#ページランクアルゴリズムの中身
    for l in range(0,times):
        for i in range(0,num):
            if not len(graph[i]['follow']) == 0:
                give_point=graph[i]['point1']/len(graph[i]['follow'])
                for j in range(0,len(graph[i]['follow'])):
                    for k in range(0,num):
                        if graph[i]['follow'][j]==graph[k]['name']:
                            graph[k]['point2'] += give_point
                            break
                    
                    
        for i in range(0,num):  
            graph[i]['point1']=graph[i]['point2']
            graph[i]['point2']=0.0
    return graph

def print_result(num,graph):
    for i in range(0,num): #結果の表示
        print graph[i]['name'],
        print ' '
        print graph[i]['point1']

    sum_point = 0#合っているかの確認
    for i in range(0,num):
        sum_point += graph[i]['point1']
    print "\naverage"
    print sum_point/num

    max=0#有名人は誰？
    for i in range(0,num):
        if(graph[i]['point1']>max):
            max=graph[i]['point1']
            fam=graph[i]['name']

    print "\nmost famous person is"
    print fam
    print max



        


#main関数
data_file = open('homework4/large_data.txt', 'r')
graph = []
times = 10#ページングアルゴリズムを回す回数（今は適当）

(num,graph)=make_graph(data_file,graph)#グラフを作る
graph = page_rank(num,graph,times)#ページランクアルゴリズムの中身
print_result(num,graph)#結果の表示
 

