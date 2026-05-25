import { Outlet } from 'react-router-dom';
import Sidebar from './Sidebar';
import Topbar from './Topbar';
import './Layout.css';

export default function Layout() {
  return (
    <div className="layout">
      <aside className="layout__sidebar">
        <Sidebar />
      </aside>
      <header className="layout__topbar">
        <Topbar />
      </header>
      <main className="layout__main">
        <Outlet />
      </main>
    </div>
  );
}
