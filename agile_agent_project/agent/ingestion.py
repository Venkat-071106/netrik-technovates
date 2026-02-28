import pandas as pd

class BacklogIngestionEngine:

    def load_data(self, file_path):
        df = pd.read_csv(file_path)
        
        required_columns = ["title", "user_story", "point"]

        for col in required_columns:
            if col not in df.columns:
                raise ValueError(f"Missing column: {col}")

        return df

    def convert_to_tickets(self, df):
        tickets = []

        for _, row in df.iterrows():
            ticket = {
                "id": str(row.get("id", "")),
                "title": str(row.get("title", "")),
                "description": str(row.get("description", "")),
                "status": str(row.get("status", "todo"))
            }

            tickets.append(ticket)

        return tickets