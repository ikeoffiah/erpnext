import React from 'react';

interface CheckFieldProps {
    label: string;
    value: boolean;
    onChange: (val: boolean) => void;
}

export const CheckField: React.FC<CheckFieldProps> = ({ label, value, onChange }) => (
    <div className="field-container checkbox">
        <input
            type="checkbox"
            id={label}
            checked={!!value}
            onChange={(e) => onChange(e.target.checked)}
        />
        <label htmlFor={label}>{label}</label>
    </div>
);
