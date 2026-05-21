import React from 'react';

interface DataFieldProps {
    label: string;
    value: string;
    onChange: (val: string) => void;
    required?: boolean;
}

export const DataField: React.FC<DataFieldProps> = ({ label, value, onChange, required }) => (
    <div className="field-container">
        <label>{label} {required && '*'}</label>
        <input
            type="text"
            value={value || ''}
            onChange={(e) => onChange(e.target.value)}
            required={required}
        />
    </div>
);
