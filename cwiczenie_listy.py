content_list = [[2,8,9],[1,2,3],[3,5,6]]
#print(content_list[1][2],content_list[2][1])
#print(content_list[1][0])
#lista_2 = ["wyraz","xd","marchewka","brokół"]
def pick_3_element(lista): #funckja względem argumentu którym jest lista powyżej (zawsze będzie ta najświeższa)
    element = lista[1]
    #print(lista,element)
    return element
content_list.sort(reverse=False, key = pick_3_element)
print(content_list)
#print(lista_2)
