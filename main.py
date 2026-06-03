from fastapi import FastAPI
from models import contact
from db import get_connection
app = FastAPI()
@app.post('/contact')
def add_contact(contact: contact):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    INSERT INTO contacts(name, phone, email)
    VALUES(%s, %s, %s)
    """
    values = (
        contact.name,
        contact.phone,
        contact.email
    )
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Contact added successfully"}
@app.get("/contacts")
def get_contacts():
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    cursor.execute("select * from contacts")
    contacts=cursor.fetchall()
    cursor.close()
    conn.close()
    return contacts
@app.put("/contacts/{contact_id}")
def update_contact(contact_id: int, contact: contact):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    UPDATE contacts
    SET name=%s,
        phone=%s,
        email=%s
    WHERE contact_id=%s
    """
    values = (
        contact.name,
        contact.phone,
        contact.email,
        contact_id
    )
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Contact Updated Successfully"}
@app.delete("/contacts/{contact_id}")
def delete_contact(contact_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    DELETE FROM contacts
    WHERE contact_id=%s
    """
    cursor.execute(query, (contact_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Contact Deleted Successfully"}
@app.get("/search")
def search_contact(name: str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
    SELECT *
    FROM contacts
    WHERE name LIKE %s
    """
    cursor.execute(query, (f"%{name}%",))
    contacts = cursor.fetchall()
    cursor.close()
    conn.close()
    return contacts
    