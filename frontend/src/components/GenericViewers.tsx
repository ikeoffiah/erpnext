import React from 'react';

export const ReportViewer: React.FC<{ reportName: string }> = ({ reportName }) => (
    <div className="report-viewer">
        <h1>Report: {reportName}</h1>
        <p>This is a placeholder for the migrated {reportName} report logic.</p>
    </div>
);

export const PageViewer: React.FC<{ pageName: string }> = ({ pageName }) => (
    <div className="page-viewer">
        <h1>Page: {pageName}</h1>
        <p>This is a placeholder for the migrated {pageName} page logic.</p>
    </div>
);
