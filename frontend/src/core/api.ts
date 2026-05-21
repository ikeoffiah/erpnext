export class DjangoClient {
    baseUrl: string;

    constructor(baseUrl: string = '/api') {
        this.baseUrl = baseUrl;
    }

    async get(resource: string) {
        const response = await fetch(`${this.baseUrl}/${resource}/`);
        return response.json();
    }

    async post(resource: string, data: any) {
        const response = await fetch(`${this.baseUrl}/${resource}/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        return response.json();
    }
}

export const api = new DjangoClient();
