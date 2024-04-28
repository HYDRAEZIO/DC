def elect(ele):
    global coordinator
    ele -= 1  # Adjust index since Python uses 0-based indexing
    coordinator = ele + 1
    for i in range(n):
        if priorities[ele] < priorities[i]:
            print(f"Election message is sent from {ele + 1} to {i + 1}")
            if statuses[i] == 1:
                elect(i + 1)

if __name__ == "__main__":
    print("Enter the number of processes:")
    n = int(input())
    statuses = []
    priorities = []
    
    for i in range(n):
        print(f"For process {i + 1}:")
        print("Status (1 for active, 0 for inactive):")
        status = int(input())
        statuses.append(status)
        print("Priority:")
        priority = int(input())
        priorities.append(priority)
    
    print("Which process will initiate the election?")
    ele = int(input())
    coordinator = 0
    elect(ele)
    print(f"Final coordinator is {coordinator}")
