#working properly!

if __name__ == '__main__':
    li = []
    N = int(input('Number of tasks: '))
    for _ in range(N):
        data = list(input('Type the command: ').split())
        if data[0] == 'append':
            li.append(int(data[1]))
        elif data[0] == 'insert':
            li.insert((int(data[1])),int(data[2]))
        elif data[0] == 'sort':
            li.sort()
        elif data[0] == 'reverse':
            li.reverse()
        elif data[0] == 'pop':
            li.pop()
        elif data[0] == 'remove':
            li.remove(int(data[1]))
        elif data[0] == 'print':
            print(li)
            
