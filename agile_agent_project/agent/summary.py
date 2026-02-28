class SummaryGenerator:

    def generate(self, tickets):

        total = len(tickets)

        blocked = [t for t in tickets if t["depends_on"]]

        completed = [t for t in tickets if t["status"] == "done"]

        return {
            "total_tasks": total,
            "blocked_tasks": len(blocked),
            "completed_tasks": len(completed),
            "progress_percentage":
                round((len(completed) / total) * 100, 2)
                if total > 0 else 0
        }
