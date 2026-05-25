import { useState, useEffect } from 'react';
import ModulePage from '../../components/ModulePage';
import { DataTable, Column } from '../../components/DataTable';

interface SalesInvoice {
  name: string;
  customer: string | null;
  posting_date: string;
  due_date: string | null;
  total: string | number;
  status: string;
}

export default function SalesInvoicesPage() {
  const [invoices, setInvoices] = useState<SalesInvoice[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/sales-invoice/')
      .then((res) => res.json())
      .then((data) => {
        setInvoices(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error('Failed to fetch sales invoices:', err);
        setLoading(false);
      });
  }, []);

  const columns: Column<SalesInvoice>[] = [
    { key: 'name', header: 'ID' },
    { key: 'customer', header: 'Customer ID' },
    { key: 'posting_date', header: 'Posting Date' },
    { key: 'due_date', header: 'Due Date' },
    { key: 'total', header: 'Total', render: (inv) => `$${Number(inv.total).toFixed(2)}` },
    { key: 'status', header: 'Status' },
  ];

  return (
    <ModulePage title="Sales Invoices" description="Create and manage sales invoices">
      <DataTable 
        data={invoices} 
        columns={columns} 
        isLoading={loading} 
        emptyMessage="No sales invoices found." 
      />
    </ModulePage>
  );
}
