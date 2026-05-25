import { useState, useEffect } from 'react';
import ModulePage from '../../components/ModulePage';
import { DataTable, Column } from '../../components/DataTable';

interface Opportunity {
  name: string;
  opportunity_from: string;
  party_name: string | null;
  opportunity_amount: string | number;
  status: string;
}

export default function OpportunitiesPage() {
  const [opportunities, setOpportunities] = useState<Opportunity[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/opportunity/')
      .then((res) => res.json())
      .then((data) => {
        setOpportunities(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error('Failed to fetch opportunities:', err);
        setLoading(false);
      });
  }, []);

  const columns: Column<Opportunity>[] = [
    { key: 'name', header: 'ID' },
    { key: 'party_name', header: 'Party Name' },
    { key: 'opportunity_from', header: 'From' },
    { key: 'opportunity_amount', header: 'Amount', render: (opp) => `$${Number(opp.opportunity_amount).toFixed(2)}` },
    { key: 'status', header: 'Status' },
  ];

  return (
    <ModulePage title="Opportunities" description="Manage sales opportunities and pipeline">
      <DataTable 
        data={opportunities} 
        columns={columns} 
        isLoading={loading} 
        emptyMessage="No opportunities found. Add an opportunity to track your pipeline." 
      />
    </ModulePage>
  );
}
