import { useState, useEffect } from 'react';
import ModulePage from '../../components/ModulePage';
import { DataTable, Column } from '../../components/DataTable';

interface SalesOrder {
  name: string;
  customer: string | null;
  transaction_date: string;
  delivery_date: string | null;
  total: string | number;
  status: string;
}

export default function SalesOrdersPage() {
  const [orders, setOrders] = useState<SalesOrder[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/sales-order/')
      .then((res) => res.json())
      .then((data) => {
        setOrders(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error('Failed to fetch sales orders:', err);
        setLoading(false);
      });
  }, []);

  const columns: Column<SalesOrder>[] = [
    { key: 'name', header: 'ID' },
    { key: 'customer', header: 'Customer ID' },
    { key: 'transaction_date', header: 'Date' },
    { key: 'delivery_date', header: 'Delivery Date' },
    { key: 'total', header: 'Total', render: (order) => `$${Number(order.total).toFixed(2)}` },
    { key: 'status', header: 'Status' },
  ];

  return (
    <ModulePage title="Sales Orders" description="Manage confirmed sales orders">
      <DataTable 
        data={orders} 
        columns={columns} 
        isLoading={loading} 
        emptyMessage="No sales orders found." 
      />
    </ModulePage>
  );
}
