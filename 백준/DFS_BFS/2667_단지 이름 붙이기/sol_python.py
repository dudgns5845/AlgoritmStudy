# #좌표 이동 방식
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# n  = int(input())
# #map
# board = []

# #방문 지도
# visit = [[-1]*n for _ in range(n)]

# #단지 크기 저장
# danji = []

# count = 0

# #지도 입력하기
# for i in range(n):
#     board.append(list(input()))

# #지도 출력
# for i in range(n):
#     for j in range(n):
#         print(board[i][j],end =' ')
#     print()


# def DFS(x,y):

#     #ssibal jjocgatta!!!!
#     global count
#     global dx,dy

#     #아파트가 있고 방문한 적이 없을때만 카운트해준다
#     if board [x][y] == '1' and visit[x][y] == -1:
#         #방문 표시하기
#         visit[x][y] = 1
#         print(x,y,count)
#         count += 1
    
#     #그리고 나서 다음 상하좌우 탐색을 실시해준다
#     for i in range(4):

#         #새로 탐색할 좌표 생성
#         new_x = x + dx[i]
#         new_y = y + dx[i]

#         #지도의 범위를 넘어가지 않을 때만 탐색을 실시한다
#         if new_x >=0 and new_x<n and new_y>=0 and new_y <n:
#             DFS(x,y)


# DFS(0,0)


# # for i in range(n):
# #     for j in range(n):
# #         DFS(i,j)
# #         if(count != 0):
# #             danji.append(count)
# #         count = 0

# #방문 기록 출력
# for i in range(n):
#     for j in range(n):
#         print(visit[i][j], end = ' ' )
#     print()

# print(danji)
# print(len(danji))



n = int(input())
board = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

danji_cnt = []


for i in range(n):
    board.append(list(input()))

def BFS(x,y):
    que = [[x,y]]
    #일단 방문하면 0처리
    board[x][y] = '0'
    count = 1

    while que:
        a,b = que[0][0], que[0][1]
        del que[0]

        for j in range(4):
            new_x = a + dx[j]
            new_y = b + dy[j]

            if 0<= new_x and new_x< n and 0<= new_y and new_y<n and board[new_x][new_y] == '1':
                board[new_x][new_y] = '0'
                que.append([new_x,new_y])
                count+=1

    danji_cnt.append(count)

for i in range(n):
    for j in range(n):
        if board[i][j] == '1':
            BFS(i,j)

danji_cnt.sort()
print(len(danji_cnt))
for i in danji_cnt:
    print(i)
        