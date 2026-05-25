import ModulePage from '../../components/ModulePage';
import BankList from '../../components/BankList';

export default function BanksPage() {
  return (
    <ModulePage title="Banks" description="Manage your bank connections">
      <BankList />
    </ModulePage>
  );
}
