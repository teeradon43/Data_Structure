def score_sort(n_lst,p_lst,g_lst,m,index,n):
    if m+1 == n:
        return n_lst, p_lst, g_lst # end of sort :: return what ?
    if index == m:
        return score_sort(n_lst,p_lst,g_lst,m+1,n-1,n)
    
    if (p_lst[index] == p_lst[index-1] and g_lst[index] > g_lst[index-1]) or (p_lst[index] > p_lst[index-1]):
        n_lst[index], n_lst[index-1] = n_lst[index-1], n_lst[index]
        p_lst[index], p_lst[index-1] = p_lst[index-1], p_lst[index]
        g_lst[index], g_lst[index-1] = g_lst[index-1], g_lst[index]
        
    return score_sort(n_lst,p_lst,g_lst,m,index-1,n)

inp = input('Enter Input : ').split('/')
name_li = []
points_li = []
gd_li = []
for team in inp:
    name, wins, loss, draws, scored, conceded = team.split(',')
    name_li.append(name)
    points_li.append(int(wins)*3+int(draws))
    gd_li.append(int(scored)-int(conceded))

n_win,p_win,g_win = score_sort(name_li,points_li,gd_li,0,len(name_li)-1,len(name_li))
print('== results ==')
for i in range(len(n_win)):
    print("['%s', {'points': %d}, {'gd': %d}]" %(n_win[i], p_win[i],g_win[i]))