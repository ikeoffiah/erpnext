import ModulePage from '../../components/ModulePage';
import BankAccountList from '../../components/BankAccountList';

export default function BankAccountsPage() {
  return (
    <ModulePage title="Bank Accounts" description="View and manage bank accounts">
      <BankAccountList />
    </ModulePage>
  );
}
