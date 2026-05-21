import React from 'react';

interface SelectFieldProps {
    label: string;
    value: string;
    options: { label: string, value: string }[];
    onChange: (val: string) => void;
    required?: boolean;
}

export const SelectField: React.FC<SelectFieldProps> = ({ label, value, options, onChange, required }) => (
    <div className="field-container">
        <label>{label} {required && '*'}</label>
        <select value={value || ''} onChange={(e) => onChange(e.target.value)} required={required}>
            <option value="">Select...</option>
            {options.map(opt => (
                <option key={opt.value} value={opt.value}>{opt.label}</option>
            ))}
        </select>
    </div>
);
