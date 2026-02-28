class ResourceAssignmentEngine:

    def assign(self, tickets):
        
        engineers = ["Dev_A", "Dev_B", "Dev_C"]
        assignments = {}

        index = 0

        for ticket in tickets:
            engineer = engineers[index % len(engineers)]
            assignments[ticket["id"]] = engineer
            index += 1

        return assignments