import React, { useState } from 'react';
import { DoctypeMetadata } from '../core/types';
import { DataField } from './fields/DataField';
import { LinkField } from './fields/LinkField';

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
                if (field.fieldtype === 'Data') {
                    return (
                        <DataField
                            key={field.fieldname}
                            label={field.label}
                            value={formData[field.fieldname]}
                            onChange={(val) => handleChange(field.fieldname, val)}
                            required={!!field.reqd}
                        />
                    );
                }
                if (field.fieldtype === 'Link') {
                    return (
                        <LinkField
                            key={field.fieldname}
                            label={field.label}
                            options={field.options || ''}
                            value={formData[field.fieldname]}
                            onChange={(val) => handleChange(field.fieldname, val)}
                        />
                    );
                }
                return null;
            })}
            <button type="submit">Save</button>
        </form>
    );
};
