import csv
import json
from connect import connect


def get_group_id(cur, group_name):
    if not group_name:
        return None
    cur.execute("SELECT id FROM groups WHERE name = %s", (group_name,))
    result = cur.fetchone()
    if result:
        return result[0]
    cur.execute("INSERT INTO groups (name) VALUES (%s) RETURNING id", (group_name,))
    return cur.fetchone()[0]


def insert_from_csv(filename):
    conn = connect()
    cur = conn.cursor()

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            
            for row in reader:
                if len(row) < 7:
                    continue
                    
                name, surname, email, birthday, group_name, phone, phone_type = row
                
                group_id = None
                if group_name:
                    cur.execute("SELECT id FROM groups WHERE name = %s", (group_name,))
                    result = cur.fetchone()
                    if result:
                        group_id = result[0]
                    else:
                        cur.execute("INSERT INTO groups (name) VALUES (%s) RETURNING id", (group_name,))
                        group_id = cur.fetchone()[0]

                cur.execute("SELECT id FROM contacts WHERE name = %s AND surname = %s", (name, surname))
                existing = cur.fetchone()
                
                if existing:
                    contact_id = existing[0]
                    cur.execute(
                        "UPDATE contacts SET email=%s, birthday=%s, group_id=%s WHERE id=%s",
                        (email or None, birthday or None, group_id, contact_id)
                    )
                else:
                    cur.execute(
                        """INSERT INTO contacts (name, surname, email, birthday, group_id) 
                           VALUES (%s, %s, %s, %s, %s) RETURNING id""",
                        (name, surname, email or None, birthday or None, group_id)
                    )
                    contact_id = cur.fetchone()[0]

                if phone and phone_type.lower() in ['home', 'work', 'mobile']:
                    cur.execute(
                        "SELECT id FROM phones WHERE contact_id=%s AND phone=%s AND type=%s",
                        (contact_id, phone, phone_type.lower())
                    )
                    if not cur.fetchone():
                        cur.execute(
                            "INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)",
                            (contact_id, phone, phone_type.lower())
                        )
                
        conn.commit()
        print("CSV Import successful.")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()


def insert_from_console():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    phone = input("Enter phone: ")
    phone_type = input("Enter phone type (home/work/mobile): ")

    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO contacts (name, surname) VALUES (%s, %s) RETURNING id",
            (name, surname)
        )
        contact_id = cur.fetchone()[0]
        
        cur.execute(
            "INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)",
            (contact_id, phone, phone_type)
        )
        conn.commit()
        print("Contact inserted successfully.")
    except Exception as e:
        print(f"Error inserting contact: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()


def delete_contact():
    value = input("Enter name, surname, or phone to delete: ")

    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute("CALL delete_contact(%s)", (value,))
        conn.commit()
        print("Contact deleted (if existed).")
    except Exception as e:
        print(f"Error deleting contact: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()


def export_to_json():
    conn = connect()
    cur = conn.cursor()
    
    cur.execute("""
        SELECT c.id, c.name, c.surname, c.email, TO_CHAR(c.birthday, 'YYYY-MM-DD'), g.name
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
    """)
    contacts_data = cur.fetchall()
    
    export_data = []
    for cid, name, surname, email, birthday, group_name in contacts_data:
        cur.execute("SELECT phone, type FROM phones WHERE contact_id = %s", (cid,))
        phones = [{"phone": p[0], "type": p[1]} for p in cur.fetchall()]
        
        export_data.append({
            "name": name,
            "surname": surname,
            "email": email,
            "birthday": birthday,
            "group": group_name,
            "phones": phones
        })

    with open("contacts_export.json", "w") as f:
        json.dump(export_data, f, indent=4)
    print("Exported successfully to contacts_export.json")
    
    cur.close()
    conn.close()


def import_from_json():
    filename = input("Enter JSON filename (e.g., contacts_export.json): ")
    conn = connect()
    cur = conn.cursor()
    
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            
        for item in data:
            # Check for duplicate
            cur.execute("SELECT id FROM contacts WHERE name = %s AND surname = %s", (item['name'], item['surname']))
            dup = cur.fetchone()
            
            if dup:
                choice = input(f"Duplicate found for {item['name']} {item['surname']}. (S)kip or (O)verwrite? ").lower()
                if choice == 's':
                    continue
                elif choice == 'o':
                    cur.execute("DELETE FROM contacts WHERE id = %s", (dup[0],)) # Cascade deletes phones
            
            group_id = get_group_id(cur, item.get('group'))
            cur.execute(
                """INSERT INTO contacts (name, surname, email, birthday, group_id) 
                   VALUES (%s, %s, %s, %s, %s) RETURNING id""",
                (item['name'], item.get('surname'), item.get('email'), item.get('birthday'), group_id)
            )
            new_id = cur.fetchone()[0]
            
            for p in item.get('phones', []):
                cur.execute(
                    "INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)",
                    (new_id, p['phone'], p['type'])
                )
        conn.commit()
        print("JSON Import complete.")
    except Exception as e:
        print(f"Error importing JSON: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()


def advanced_search_filter():
    print("\n--- Search & Filter ---")
    print("1. Filter by Group")
    print("2. Search by Email")
    print("3. Universal Search (Name/Email/Phone)")
    print("4. Show All (Sorted)")
    
    choice = input("Choose: ")
    conn = connect()
    cur = conn.cursor()
    
    if choice == "1":
        group = input("Enter group name: ")
        cur.execute("""
            SELECT c.name, c.surname, c.email FROM contacts c
            JOIN groups g ON c.group_id = g.id WHERE g.name ILIKE %s
        """, (group,))
        
    elif choice == "2":
        email = input("Enter email partial: ")
        cur.execute("SELECT name, surname, email FROM contacts WHERE email ILIKE %s", (f"%{email}%",))
        
    elif choice == "3":
        query = input("Enter search term: ")
        cur.execute("SELECT * FROM search_contacts(%s)", (query,))
        
    elif choice == "4":
        sort_by = input("Sort by (1) Name, (2) Birthday, (3) Date Added: ")
        order_clause = "ORDER BY name"
        if sort_by == "2": order_clause = "ORDER BY birthday NULLS LAST"
        elif sort_by == "3": order_clause = "ORDER BY created_at DESC"
        
        cur.execute(f"SELECT name, surname, birthday, created_at FROM contacts {order_clause}")
    else:
        print("Invalid choice.")
        cur.close()
        conn.close()
        return

    rows = cur.fetchall()
    if not rows:
        print("No results found.")
    for row in rows:
        print(row)
        
    cur.close()
    conn.close()


def paginated_navigation():
    try:
        limit = int(input("Enter items per page: "))
    except ValueError:
        print("Invalid number.")
        return
        
    offset = 0
    conn = connect()
    cur = conn.cursor()
    
    while True:
        cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
        rows = cur.fetchall()
        
        print(f"\n--- Page {offset//limit + 1} ---")
        if not rows:
            print("No contacts found on this page.")
        for row in rows:
            print(row)
            
        print("\n(N)ext page, (P)revious page, (Q)uit")
        action = input("Choose: ").lower()
        if action == 'n':
            offset += limit
        elif action == 'p':
            offset = max(0, offset - limit)
        elif action == 'q':
            break
            
    cur.close()
    conn.close()


def execute_procedures():
    print("\n--- Stored Procedures ---")
    print("1. Add new phone to contact")
    print("2. Move contact to group")
    choice = input("Choose: ")
    
    conn = connect()
    cur = conn.cursor()
    
    try:
        if choice == "1":
            name = input("Contact exact name: ")
            phone = input("New phone number: ")
            p_type = input("Type (home/work/mobile): ")
            cur.execute("CALL add_phone(%s, %s, %s)", (name, phone, p_type))
            conn.commit()
            print("Phone added.")
            
        elif choice == "2":
            name = input("Contact exact name: ")
            group = input("New group name: ")
            cur.execute("CALL move_to_group(%s, %s)", (name, group))
            conn.commit()
            print("Contact moved to group.")
    except Exception as e:
        print(f"Procedure error: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()


def main():
    while True:
        print("\n--- EXTENDED PHONEBOOK ---")
        print("1. Insert from CSV")
        print("2. Insert from console")
        print("3. Delete contact")
        print("4. Import from JSON")
        print("5. Export to JSON")
        print("6. Search / Filter / Sort")
        print("7. Paginated View")
        print("8. Run Stored Procedures (Add phone / Move group)")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            insert_from_csv("C:/Users/Roar/Documents/GitHub/PP2/TSIS1/contacts.csv")
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            import_from_json()
        elif choice == "5":
            export_to_json()
        elif choice == "6":
            advanced_search_filter()
        elif choice == "7":
            paginated_navigation()
        elif choice == "8":
            execute_procedures()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()