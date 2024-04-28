def print_load(servers, processes):
    each = processes // servers
    extra = processes % servers
    for i in range(servers):
        if extra > 0:
            total = each + 1
            extra -= 1
        else:
            total = each
        print(f"Server {chr(ord('A') + i)} has {total} Processes")

def main():
    servers = int(input("Enter the number of servers: "))
    processes = int(input("Enter the number of processes: "))
    
    while True:
        print_load(servers, processes)
        print("1. Add Servers 2. Remove Servers 3. Add Processes 4. Remove Processes 5. Exit: ", end='')
        choice = int(input())
        if choice == 1:
            servers += int(input("How many more servers?: "))
        elif choice == 2:
            servers -= int(input("How many servers to remove?: "))
        elif choice == 3:
            processes += int(input("How many more processes?: "))
        elif choice == 4:
            processes -= int(input("How many processes to remove?: "))
        elif choice == 5:
            break

if __name__ == "__main__":
    main()
