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
            // Route to Django REST API
            const res = await fetch(`/api/${doctype.toLowerCase()}s/`);
            return res.json();
        }
    }
};

export const useFrappe = () => {
    return {
        call: frappe.call
    };
};

(window as any).frappe = frappe;
