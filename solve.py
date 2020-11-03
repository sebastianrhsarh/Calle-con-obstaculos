from sys import stdin
from collections import deque
deltas,board = [(-1,1),(-1,0),(-1,-1)],None


def print_board(b):
    """
    Este procedimiento imprime el tablero dado por parametro b
    """
    for l in b: 
        print(*l)


def rebuild_path(path,tg):
    """
    esta funcion recibe una matriz con los padres de cada nodo --> 'path'
    y retorna una lista con el camino para llegar hasta tg, tg es una tupla, por ejemplo --> (1,1) o (2,2)
    que significa que se quiere conocer el camino para llegar a la posicion de la matriz (1,1) o (2,2)

    Si no hay camino al tg devuelve una lista con solo el tg
    """
    i,j = tg
    ans = [tg]
    while((i != -1 and j != -1) and path[i][j] != (i,j)):
        ans.append((path[i][j]))
        i,j = path[i][j]
    ans.reverse()
    return ans



def bfs(u):
    """
    Esta funcion hace un bfs para encontrar el camino mas corto dese el nodo u--> el nodo u es una tupla (0,0) o (1,1)
    desde donde inicia el bfs (coordenada de la matriz)

    """
    global board
    q,found,ans,path,visited = deque(),False,list(),[[(-1,-1) for _ in range(len(board[0]))] for _ in range(len(board))],[[None for _ in range(len(board[0]))] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[i])):
            visited[i][j] = False if board[i][j] != 'x' else True
    q.append(u)
    dist,max_dist = [[0 for _ in range(len(board[0]))] for _ in range(len(board))],0
    i_u,j_u = u
    l_i,l_j = u
    visited[i_u][j_u] = True
    path[i_u][j_u] = (i_u,j_u)
    while(len(q) and not found):
        i_u,j_u = q.popleft()
        for i,j in deltas:
            if(0 <= i_u+i < len(board) and 0 <= j_u+j < len(board[0]) and not visited[i_u+i][j_u+j]): 
                path[i_u+i][j_u+j] = (i_u,j_u)
                visited[i_u+i][j_u+j] = True
                dist[i_u+i][j_u+j] = dist[i_u][j_u]+1
                q.append((i_u+i,j_u+j))

        l_i,l_j,max_dist = i_u,j_u,max(max_dist,dist[i_u][j_u])

    ans = rebuild_path(path,(l_i,l_j))
    return ans,max_dist
    

def solve():
    global board
    path,fit,max_fit,max_path = None,0,0,None
    for i in range(len(board[0])):#por todas las columnas mando a hacer un bfs desde la fila 0
        path,fit = bfs((len(board)-1,i))
        max_path = list(path) if fit > max_fit else max_path
        max_fit = max(fit,max_fit)
    for i,j in max_path:
        board[i][j] = 'O'
    print_board(board)
    print("Fit:",max_fit+1)


def main():
    global board
    line = stdin.readline().strip()
    while len(line) and line != "" and line != "\n":
        r,c = map(int,line.split(","))
        board = list()
        for _ in range(r):
            line = stdin.readline().strip()
            board.append([c for c in line])
      
        solve()
        print("\n\n")
        line = stdin.readline().strip()
main()