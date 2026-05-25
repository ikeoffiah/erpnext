// src/components/BankList.tsx
import React, { useEffect, useState } from 'react';
import './BankList.css';

interface Bank {
  id: number;
  bank_name: string;
  swift_number?: string;
  website?: string;
  address_html?: string;
  contact_html?: string;
  plaid_access_token?: string;
}

const BankList: React.FC = () => {
  const [banks, setBanks] = useState<Bank[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch('/api/bank/')
      .then((res) => {
        if (!res.ok) {
          throw new Error(`HTTP ${res.status}`);
        }
        return res.json();
      })
      .then((data) => {
        setBanks(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div className="bank-list loading">Loading banks...</div>;
  }

  if (error) {
    return <div className="bank-list error">Error: {error}</div>;
  }

  return (
    <section className="bank-list">
      <h2 className="bank-list__title">Banks</h2>
      {banks.length === 0 ? (
        <p>No banks available.</p>
      ) : (
        <ul className="bank-list__grid">
          {banks.map((bank) => (
            <li key={bank.id} className="bank-list__item">
              <h3 className="bank-list__name">{bank.bank_name}</h3>
              {bank.swift_number && (
                <p className="bank-list__detail"><strong>SWIFT:</strong> {bank.swift_number}</p>
              )}
              {bank.website && (
                <p className="bank-list__detail"><strong>Website:</strong> <a href={bank.website} target="_blank" rel="noopener noreferrer">{bank.website}</a></p>
              )}
            </li>
          ))}
        </ul>
      )}
    </section>
  );
};

export default BankList;
