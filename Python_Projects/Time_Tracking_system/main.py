import pandas as pd
from datetime import datetime
import os
import sys

EXCEL_FILE = "time_tracker.xlsx"


# Initialize Excel file with required structure
def initialize_excel():
    if not os.path.exists(EXCEL_FILE):
        with pd.ExcelWriter(EXCEL_FILE, engine='openpyxl') as writer:
            # Users sheet
            pd.DataFrame(columns=["ID", "Name", "PIN", "TotalHours"]).to_excel(
                writer, sheet_name="Users", index=False)
            # Time entries sheet
            pd.DataFrame(columns=["UserID", "StartTime", "EndTime", "Duration"]).to_excel(
                writer, sheet_name="TimeEntries", index=False)


def get_users():
    return pd.read_excel(EXCEL_FILE, sheet_name="Users")


def get_time_entries():
    time_df = pd.read_excel(EXCEL_FILE, sheet_name="TimeEntries")
    # Add Duration column if missing (for backward compatibility)
    if 'Duration' not in time_df.columns:
        time_df['Duration'] = 0.0
    return time_df


def save_data(users_df, time_df):
    with pd.ExcelWriter(EXCEL_FILE, engine='openpyxl') as writer:
        users_df.to_excel(writer, sheet_name="Users", index=False)
        time_df.to_excel(writer, sheet_name="TimeEntries", index=False)


def add_user(name, pin):
    """Add new user with initial 0 hours"""
    users_df = get_users()

    if str(pin) in users_df["PIN"].astype(str).values:
        print("\nError: PIN already exists!")
        return

    new_id = users_df["ID"].max() + 1 if not users_df.empty else 1
    new_user = pd.DataFrame({
        "ID": [new_id],
        "Name": [name],
        "PIN": [pin],
        "TotalHours": [0.0]
    })

    users_df = pd.concat([users_df, new_user], ignore_index=True)
    save_data(users_df, get_time_entries())
    print(f"\nUser '{name}' added successfully!")


def clock_in():
    """Start a new work session"""
    pin = input("\nEnter PIN to clock in: ")
    users_df = get_users()
    time_df = get_time_entries()

    user = users_df[users_df["PIN"].astype(str) == str(pin)]
    if user.empty:
        print("\nInvalid PIN!")
        return

    user_id = user.iloc[0]["ID"]

    # Check for existing active session
    active_session = time_df[(time_df["UserID"] == user_id) & (time_df["EndTime"].isna())]
    if not active_session.empty:
        print("\nYou already have an active session!")
        return

    # Create new entry
    new_entry = pd.DataFrame({
        "UserID": [user_id],
        "StartTime": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        "EndTime": [None],
        "Duration": [0.0]
    })

    time_df = pd.concat([time_df, new_entry], ignore_index=True)
    save_data(users_df, time_df)
    print("\nClocked in successfully!")


def clock_out():
    """End current work session and calculate hours"""
    pin = input("\nEnter PIN to clock out: ")
    users_df = get_users()
    time_df = get_time_entries()

    user = users_df[users_df["PIN"].astype(str) == str(pin)]
    if user.empty:
        print("\nInvalid PIN!")
        return

    user_id = user.iloc[0]["ID"]
    user_idx = user.index[0]

    # Find active session
    active_session = time_df[(time_df["UserID"] == user_id) & (time_df["EndTime"].isna())]
    if active_session.empty:
        print("\nNo active session found!")
        return

    entry_idx = active_session.index[0]
    end_time = datetime.now()
    start_time = datetime.strptime(time_df.at[entry_idx, "StartTime"], "%Y-%m-%d %H:%M:%S")

    # Calculate duration in hours
    duration = round((end_time - start_time).total_seconds() / 3600, 2)

    # Update time entry
    time_df.at[entry_idx, "EndTime"] = end_time.strftime("%Y-%m-%d %H:%M:%S")
    time_df.at[entry_idx, "Duration"] = duration

    # Update total hours
    users_df.at[user_idx, "TotalHours"] += duration

    save_data(users_df, time_df)
    print(f"\nClocked out successfully!")
    print(f"Session duration: {duration} hours")
    print(f"Total hours worked: {users_df.at[user_idx, 'TotalHours']} hours")


def main_menu():
    initialize_excel()

    while True:
        print("\n" + "=" * 30)
        print(" TIME TRACKING SYSTEM")
        print("=" * 30)
        print("1. Clock In")
        print("2. Clock Out")
        print("3. Add New User")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            clock_in()
        elif choice == "2":
            clock_out()
        elif choice == "3":
            name = input("\nEnter employee name: ").strip()
            while True:
                pin = input("Set 4-digit PIN: ").strip()
                if len(pin) == 4 and pin.isdigit():
                    add_user(name, pin)
                    break
                print("Invalid PIN! Must be 4 digits (e.g., 1234)")
        elif choice == "4":
            print("\nThank you for using Time Tracker!")
            break
        else:
            print("\nInvalid choice! Please enter 1-4.")


def check_dependencies():
    try:
        import pandas
        import openpyxl
    except ImportError:
        print("Installing required packages...")
        os.system(f"{sys.executable} -m pip install pandas openpyxl")


if __name__ == "__main__":
    check_dependencies()
    main_menu()