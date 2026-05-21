export interface DoctypeField {
    fieldname: string;
    fieldtype: string;
    label: string;
    options?: string;
    reqd?: number;
    hidden?: number;
    read_only?: number;
}

export interface DoctypeMetadata {
    name: string;
    fields: DoctypeField[];
}
