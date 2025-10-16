
from supabase import create_client

# Replace with your actual Supabase project URL and anon key
SUPABASE_URL = "https://kbohrthtkhjrcfmkxyuh.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imtib2hydGh0a2hqcmNmbWt4eXVoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjA1NTQ1MTksImV4cCI6MjA3NjEzMDUxOX0.CAJUDA4cSplorG4xhLhX7-_OWkV879yZHHXUG8t8__s"

# Create Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Function to insert a user
def insert_user(name, goal, days_per_week, equipment):
    data = {
        "name": name,
        "goal": goal,
        "days_per_week": days_per_week,
        "equipment": equipment
    }
    return supabase.table("users").insert(data).execute()

# Function to insert a workout program
def insert_program(user_id, date, block_type, exercise, sets, reps, rest):
    data = {
        "user_id": user_id,
        "date": date,
        "block_type": block_type,
        "exercise": exercise,
        "sets": sets,
        "reps": reps,
        "rest": rest
    }
    return supabase.table("programs").insert(data).execute()

# Function to insert a workout log
def insert_log(user_id, date, exercise, weight, sets, reps, time, rpe):
    data = {
        "user_id": user_id,
        "date": date,
        "exercise": exercise,
        "weight": weight,
        "sets": sets,
        "reps": reps,
        "time": time,
        "rpe": rpe
    }
    return supabase.table("logs").insert(data).execute()

# Function to fetch all users
def get_users():
    return supabase.table("users").select("*").execute()

# Function to fetch programs for a specific date
def get_programs_by_date(date):
    return supabase.table("programs").select("*").eq("date", date).execute()

# Function to fetch logs for a specific user
def get_logs_by_user(user_id):
    return supabase.table("logs").select("*").eq("user_id", user_id).execute()
