import './ModulePage.css';

interface Props {
  title: string;
  description?: string;
  children?: React.ReactNode;
}

export default function ModulePage({ title, description, children }: Props) {
  return (
    <div className="module-page">
      <div className="module-page__header">
        <h1 className="module-page__title">{title}</h1>
        {description && <p className="module-page__desc">{description}</p>}
      </div>
      {children ? (
        <div className="module-page__content">{children}</div>
      ) : (
        <div className="module-page__coming-soon">
          <div className="module-page__badge">Coming Soon</div>
          <p>This module is being built. API endpoints and UI components will be wired up here.</p>
        </div>
      )}
    </div>
  );
}
