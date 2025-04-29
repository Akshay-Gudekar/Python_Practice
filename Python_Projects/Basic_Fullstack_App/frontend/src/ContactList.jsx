import React from "react"

const ContactList = ({ contacts, updateContact, updateCallback }) => {
    const onDelete = async (id) => {
        try {
            const options = {
                method: "DELETE"
            }
            const response = await fetch(`http://127.0.0.1:5000/delete_contact/${id}`, options)
            if (response.status === 200) {
                updateCallback()
            } else {
                console.error("Failed to delete")
            }
        } catch (error) {
            alert(error)
        }
    }

    
      return (
        <div className="container">
          <div className="header">
            <h1 className="text-2xl font-bold">Contact Management</h1>
            <button 
              className="button button-primary"
              onClick={() => updateContact({})}
            >
              Add New Contact
            </button>
          </div>
    
          <div className="contact-grid">
            <table>
              <thead>
                <tr>
                  <th>First Name</th>
                  <th>Last Name</th>
                  <th>Email</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                {contacts.map((contact) => (
                  <tr key={contact.id}>
                    <td>{contact.firstName}</td>
                    <td>{contact.lastName}</td>
                    <td className="text-slate-600">{contact.email}</td>
                    <td className="actions-cell">
                      <button
                        className="button button-primary"
                        onClick={() => updateContact(contact)}
                      >
                        Edit
                      </button>
                      <button
                        className="button button-danger"
                        onClick={() => onDelete(contact.id)}
                      >
                        Delete
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      );
    };


export default ContactList;