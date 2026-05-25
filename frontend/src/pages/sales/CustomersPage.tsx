import { useState, useEffect } from 'react';
import ModulePage from '../../components/ModulePage';
import { DataTable, Column } from '../../components/DataTable';

interface Customer {
  name: string;
  customer_name: string;
  customer_group: string | null;
  territory: string | null;
}

export default function CustomersPage() {
  const [customers, setCustomers] = useState<Customer[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/customer/')
      .then((res) => res.json())
      .then((data) => {
        setCustomers(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error('Failed to fetch customers:', err);
        setLoading(false);
      });
  }, []);

  const columns: Column<Customer>[] = [
    { key: 'name', header: 'ID' },
    { key: 'customer_name', header: 'Customer Name' },
    { key: 'customer_group', header: 'Group' },
    { key: 'territory', header: 'Territory' },
  ];

  return (
    <ModulePage title="Customers" description="Manage customer master data">
      <DataTable 
        data={customers} 
        columns={columns} 
        isLoading={loading} 
        emptyMessage="No customers found. Create your first customer." 
      />
    </ModulePage>
  );
}
