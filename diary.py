import json
import os
from datetime import datetime

DIARY_FILE = "diary.json"

def load_entries():
    if not os.path.exists(DIARY_FILE):
        return []
    with open(DIARY_FILE, "r") as f:
        return json.load(f)
    

def save_entries(entries):
    with open(DIARY_FILE, "w") as f:
        json.dump(entries, f, indent=4)


def add_entry():
    date = datetime.now().strftime("%Y-%m-%d")
    print(f"Adding entry for {date}. Type your entry below (end with an empty line):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    content = "\n".join(lines)
    
    entries = load_entries()
    entries.append({"date": date, "content": content})
    save_entries(entries)
    print("Entry saved successfully!")


def view_entries():
    entries = load_entries()
    if not entries:
        print("No diary entries found.")
        return
    print(f"--- All Diary Entries ({len(entries)}) ---")
    for i, entry in enumerate(entries, 1):
        print(f"\nEntry #{i} - Date: {entry['date']}")
        print(entry['content'])
        print("-" * 30)


def search_entries():
    keyword = input("Enter a keyword or date (YYYY-MM-DD) to search: ").strip()
    entries = load_entries()
    results = []
    for entry in entries:
        if keyword in entry['date'] or keyword.lower() in entry['content'].lower():
            results.append(entry)
    if not results:
        print("No matching entries found.")
        return
    print(f"--- Search Results ({len(results)}) ---")
    for i, entry in enumerate(results, 1):
        print(f"\nEntry #{i} - Date: {entry['date']}")
        print(entry['content'])
        print("-" * 30)


def delete_entry():
    entries = load_entries()
    if not entries:
        print("No entries to delete.")
        return
    
    print("Select an entry to delete:")
    for i, entry in enumerate(entries, 1):
        print(f"{i}. Date: {entry['date']} - {entry['content'][:30].replace('\n', ' ')}...")
    
    try:
        choice = int(input("Enter the entry number to delete (or 0 to cancel): "))
        if choice == 0:
            print("Deletion cancelled.")
            return
        if 1 <= choice <= len(entries):
            deleted = entries.pop(choice - 1)
            save_entries(entries)
            print(f"Deleted entry from {deleted['date']}.")
        else:
            print("Invalid entry number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\n--- Personal Diary ---")
        print("1. Add new entry")
        print("2. View all entries")
        print("3. Search entries")
        print("4. Delete an entry")
        print("5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            search_entries()
        elif choice == "4":
            delete_entry()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()