import { useState, useEffect } from 'react';
import ModulePage from '../../components/ModulePage';
import { DataTable, Column } from '../../components/DataTable';

interface Contact {
  name: string;
  customer_name: string;
  customer_group: string | null;
  territory: string | null;
}

export default function ContactsPage() {
  const [contacts, setContacts] = useState<Contact[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Currently using customer endpoint as a proxy for contacts
    fetch('/api/customer/')
      .then((res) => res.json())
      .then((data) => {
        setContacts(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error('Failed to fetch contacts:', err);
        setLoading(false);
      });
  }, []);

  const columns: Column<Contact>[] = [
    { key: 'name', header: 'ID' },
    { key: 'customer_name', header: 'Contact Name' },
    { key: 'customer_group', header: 'Group' },
    { key: 'territory', header: 'Territory' },
  ];

  return (
    <ModulePage title="Contacts" description="Manage contact persons and communication">
      <DataTable 
        data={contacts} 
        columns={columns} 
        isLoading={loading} 
        emptyMessage="No contacts found." 
      />
    </ModulePage>
  );
}
