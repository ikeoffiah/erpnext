import ERPNextApp from './apps/erpnext/App';
import BankingApp from './apps/banking/App';
import { Routes, Route, BrowserRouter } from 'react-router-dom';

function App() {
  // Use simple conditional rendering for apps or a shared router
  // For this foundation, we will route /banking to BankingApp and others to ERPNextApp

  if (window.location.pathname.startsWith('/banking')) {
    return <BankingApp />;
  }

  return <ERPNextApp />;
}

export default App;
