import React from 'react';
import { BrowserRouter, Routes, Route, Link, useParams } from 'react-router-dom';
import modulesMetadata from '../../core/modules_metadata.json';

const Home = () => (
    <div style={{ padding: '20px' }}>
        <h1>ERPNext (Migrated to Django/React)</h1>
        <p>Explore the migrated modules below:</p>
        <nav>
            <ul style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '10px' }}>
                <li><Link to="/banking">Banking Module</Link></li>
                {Object.keys(modulesMetadata).sort().map(mod => (
                    <li key={mod}><Link to={`/desk/${mod.toLowerCase()}`}>{mod}</Link></li>
                ))}
            </ul>
        </nav>
    </div>
);

const ModuleDesk = () => {
    const { module } = useParams();
    const moduleName = Object.keys(modulesMetadata).find(m => m.toLowerCase() === module);
    const doctypes = moduleName ? (modulesMetadata as any)[moduleName] : [];

    return (
        <div style={{ padding: '20px' }}>
            <Link to="/">← Back to Home</Link>
            <h2>{module?.toUpperCase()} Desk</h2>
            <p>Documents in this module:</p>
            <ul style={{ maxHeight: '400px', overflowY: 'auto' }}>
                {doctypes.map((dt: any) => (
                    <li key={dt.name}><Link to={dt.route}>{dt.label}</Link></li>
                ))}
            </ul>
        </div>
    );
};

const DoctypeView = () => {
    const { doctype, name } = useParams();
    return (
        <div style={{ padding: '20px' }}>
            <button onClick={() => window.history.back()}>← Back</button>
            <h2>{doctype} - {name || 'New'}</h2>
            <p>Metadata-driven form for <strong>{doctype}</strong> will load here.</p>
            <div style={{ border: '1px solid #ccc', padding: '20px', borderRadius: '8px' }}>
                {/* Mock Form */}
                <div>
                    <label>Name: </label>
                    <input type="text" placeholder="Enter value..." />
                </div>
                <button style={{ marginTop: '10px' }}>Save {doctype}</button>
            </div>
        </div>
    );
};

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/desk/:module" element={<ModuleDesk />} />
                <Route path="/desk/:module/:doctype" element={<DoctypeView />} />
                <Route path="/desk/:module/:doctype/:name" element={<DoctypeView />} />
            </Routes>
        </BrowserRouter>
    );
}

export default App;
