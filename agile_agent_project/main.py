from agent.ingestion import BacklogIngestionEngine
from agent.summary import SummaryGenerator

engine = BacklogIngestionEngine()

df = engine.load_data(r"C:\Users\megha\Downloads\Agile-User-Story-Point-Estimation-master\Agile-User-Story-Point-Estimation-master\data_csv\data")
tickets = engine.convert_to_tickets(df)

print(tickets[:2])
from agent.assignment import ResourceAssignmentEngine

assign_engine = ResourceAssignmentEngine()
assignments = assign_engine.assign(tickets)

print(assignments)

summary_engine = SummaryGenerator()
summary = summary_engine.generate(tickets)

print("\n--- SPRINT SUMMARY ---")
print(summary)