// src/components/BankAccountList.tsx
import React, { useEffect, useState } from 'react';
import './BankAccountList.css';

interface BankAccount {
  id: number;
  account_name: string;
  bank: number; // bank id
  account_type: number;
  is_default: boolean;
  is_company_account: boolean;
  company: number;
  disabled: boolean;
}

const BankAccountList: React.FC = () => {
  const [accounts, setAccounts] = useState<BankAccount[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch('/api/bank-account/')
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.json();
      })
      .then((data) => {
        setAccounts(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <div className="bank-account-list loading">Loading accounts...</div>;
  if (error) return <div className="bank-account-list error">Error: {error}</div>;

  return (
    <section className="bank-account-list">
      <h2 className="bank-account-list__title">Bank Accounts</h2>
      {accounts.length === 0 ? (
        <p>No bank accounts available.</p>
      ) : (
        <ul className="bank-account-list__grid">
          {accounts.map((acc) => (
            <li key={acc.id} className="bank-account-list__item">
              <h3 className="bank-account-list__name">{acc.account_name}</h3>
              <p className="bank-account-list__detail"><strong>Bank ID:</strong> {acc.bank}</p>
              <p className="bank-account-list__detail"><strong>Account Type ID:</strong> {acc.account_type}</p>
              <p className="bank-account-list__detail"><strong>Company ID:</strong> {acc.company}</p>
              <p className="bank-account-list__detail"><strong>Default:</strong> {acc.is_default ? 'Yes' : 'No'}</p>
            </li>
          ))}
        </ul>
      )}
    </section>
  );
};

export default BankAccountList;
