import { useState, useEffect } from 'react';

export const frappe = {
    call: async ({ method, args }: { method: string, args?: any }) => {
        console.log(`Calling legacy method: ${method}`, args);
        const response = await fetch(`/api/rpc/?method=${method}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(args)
        });
        return response.json();
    },
    db: {
        get_list: async (doctype: string, filters: any) => {
            const res = await fetch(`/api/${doctype.toLowerCase()}s/`);
            return res.json();
        },
        get_doc: async (doctype: string, name: string) => {
            const res = await fetch(`/api/${doctype.toLowerCase()}s/${name}/`);
            return res.json();
        }
    }
};

export const useFrappe = () => {
    return {
        call: frappe.call
    };
};

export const useFrappeGetDocList = (doctype: string, options: any) => {
    const [data, setData] = useState<any[]>([]);
    useEffect(() => {
        frappe.db.get_list(doctype, options.filters).then(setData);
    }, [doctype, JSON.stringify(options)]);
    return { data, error: null, isLoading: !data };
};

export const useFrappeGetDoc = (doctype: string, name: string) => {
    const [data, setData] = useState<any>(null);
    useEffect(() => {
        if (name) frappe.db.get_doc(doctype, name).then(setData);
    }, [doctype, name]);
    return { data, error: null, isLoading: !data };
};

export const useFrappePostCall = (method: string) => {
    return {
        call: (args: any) => frappe.call({ method, args }),
        isMutating: false
    };
};

(window as any).frappe = frappe;
