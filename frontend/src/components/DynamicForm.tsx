import React, { useState } from 'react';
import { DoctypeMetadata } from '../core/types';
import { DataField } from './fields/DataField';
import { LinkField } from './fields/LinkField';
import { SelectField } from './fields/SelectField';
import { CheckField } from './fields/CheckField';
import { TableField } from './fields/TableField';

interface DynamicFormProps {
    metadata: DoctypeMetadata;
    initialData?: any;
    onSubmit: (data: any) => void;
}

export const DynamicForm: React.FC<DynamicFormProps> = ({ metadata, initialData = {}, onSubmit }) => {
    const [formData, setFormData] = useState(initialData);

    const handleChange = (fieldname: string, value: any) => {
        setFormData({ ...formData, [fieldname]: value });
    };

    return (
        <form onSubmit={(e) => { e.preventDefault(); onSubmit(formData); }}>
            <h2>{metadata.name}</h2>
            {metadata.fields.map(field => {
                if (field.hidden) return null;

                const commonProps = {
                    key: field.fieldname,
                    label: field.label,
                    value: formData[field.fieldname],
                    onChange: (val: any) => handleChange(field.fieldname, val),
                    required: !!field.reqd
                };

                switch (field.fieldtype) {
                    case 'Data':
                        return <DataField {...commonProps} />;
                    case 'Link':
                        return <LinkField {...commonProps} options={field.options || ''} />;
                    case 'Select':
                        const choices = field.options?.split('\n').filter(c => c.trim()).map(c => ({ label: c.trim(), value: c.trim() })) || [];
                        return <SelectField {...commonProps} options={choices} />;
                    case 'Check':
                        return <CheckField {...commonProps} />;
                    case 'Table':
                        return <TableField {...commonProps} />;
                    default:
                        return null;
                }
            })}
            <button type="submit" style={{ marginTop: '20px' }}>Save Document</button>
        </form>
    );
};
