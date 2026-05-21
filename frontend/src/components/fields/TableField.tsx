import React from 'react';

interface TableFieldProps {
    label: string;
    value: any[];
    onChange: (val: any[]) => void;
}

export const TableField: React.FC<TableFieldProps> = ({ label, value = [], onChange }) => (
    <div className="field-container table">
        <label>{label}</label>
        <table>
            <thead>
                <tr>
                    <th>#</th>
                    <th>Data</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                {value.map((row, idx) => (
                    <tr key={idx}>
                        <td>{idx + 1}</td>
                        <td>{JSON.stringify(row)}</td>
                        <td>
                            <button type="button" onClick={() => onChange(value.filter((_, i) => i !== idx))}>Remove</button>
                        </td>
                    </tr>
                ))}
            </tbody>
        </table>
        <button type="button" onClick={() => onChange([...value, {}])}>Add Row</button>
    </div>
);
