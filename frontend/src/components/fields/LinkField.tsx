import React from 'react';

interface LinkFieldProps {
    label: string;
    value: string;
    options: string;
    onChange: (val: string) => void;
}

export const LinkField: React.FC<LinkFieldProps> = ({ label, value, options, onChange }) => (
    <div className="field-container">
        <label>{label} (Link to {options})</label>
        <input
            type="text"
            placeholder={`Search ${options}...`}
            value={value || ''}
            onChange={(e) => onChange(e.target.value)}
        />
    </div>
);
