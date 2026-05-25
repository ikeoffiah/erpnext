import { useState, useEffect } from 'react';
import ModulePage from '../../components/ModulePage';
import { DataTable, Column } from '../../components/DataTable';

interface Lead {
  name: string;
  lead_name: string;
  company_name: string | null;
  email_id: string | null;
  mobile_no: string | null;
  status: string;
}

export default function LeadsPage() {
  const [leads, setLeads] = useState<Lead[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/lead/')
      .then((res) => res.json())
      .then((data) => {
        setLeads(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error('Failed to fetch leads:', err);
        setLoading(false);
      });
  }, []);

  const columns: Column<Lead>[] = [
    { key: 'name', header: 'ID' },
    { key: 'lead_name', header: 'Lead Name' },
    { key: 'company_name', header: 'Company' },
    { key: 'email_id', header: 'Email' },
    { key: 'mobile_no', header: 'Mobile' },
    { key: 'status', header: 'Status' },
  ];

  return (
    <ModulePage title="Leads" description="Track and manage prospective customers">
      <DataTable 
        data={leads} 
        columns={columns} 
        isLoading={loading} 
        emptyMessage="No leads found. Create your first lead to get started." 
      />
    </ModulePage>
  );
}
