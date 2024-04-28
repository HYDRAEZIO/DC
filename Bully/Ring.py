class Process:
    def __init__(self, id):
        self.id = id
        self.active = True

class Ring:
    def __init__(self):
        self.processes = []
    
    def initialise_ring(self):
        no_of_processes = int(input("Enter number of processes: "))
        self.processes = [Process(i) for i in range(no_of_processes)]
    
    def get_max(self):
        max_id_index = -1
        for i, process in enumerate(self.processes):
            if process.active and (max_id_index == -1 or process.id > self.processes[max_id_index].id):
                max_id_index = i
        return max_id_index
    
    def perform_election(self):
        failing_process_index = self.get_max()
        print(f"Process no {self.processes[failing_process_index].id} fails")
        self.processes[failing_process_index].active = False

        initiator_process = int(input("Election Initiated by: "))
        prev = initiator_process
        next = (prev + 1) % len(self.processes)

        while True:
            if self.processes[next].active:
                print(f"Process {self.processes[prev].id} pass Election({self.processes[prev].id}) to {self.processes[next].id}")
                prev = next
            next = (next + 1) % len(self.processes)
            if next == initiator_process:
                break

        max_index = self.get_max()
        print(f"Process {self.processes[max_index].id} becomes coordinator")
        coordinator = self.processes[max_index].id
        prev = coordinator
        next = (prev + 1) % len(self.processes)

        while True:
            if self.processes[next].active:
                print(f"Process {self.processes[prev].id} pass Coordinator({coordinator}) message to process {self.processes[next].id}")
                prev = next
            next = (next + 1) % len(self.processes)
            if next == coordinator:
                print("End Of Election")
                break

if __name__ == "__main__":
    ring = Ring()
    ring.initialise_ring()
    ring.perform_election()
