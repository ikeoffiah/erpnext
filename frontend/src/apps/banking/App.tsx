import { useEffect } from 'react'
import { BrowserRouter, Navigate, Route, Routes } from 'react-router-dom'
import { Toaster } from '@/components/ui/sonner'
import BankReconciliation from '@/pages/BankReconciliation'
import { TooltipProvider } from '@/components/ui/tooltip'
import BankStatementImporter from '@/pages/BankStatementImporter'
import { LucideProvider } from 'lucide-react'
import { ThemeProvider } from '@/components/ui/theme-provider'
import ViewBankStatementImportLog from '@/pages/ViewBankStatementImportLog'
import BankStatementImporterContainer from '@/pages/BankStatementImporterContainer'

// Simplified for Django Migration
function App() {
	return (
		<LucideProvider strokeWidth={1.5}>
			<TooltipProvider>
				<ThemeProvider defaultTheme="system">
					<BrowserRouter basename="/banking">
						<Routes>
							<Route index element={<BankReconciliation />} />
							<Route path="/statement-importer" element={<BankStatementImporterContainer />}>
								<Route index element={<BankStatementImporter />} />
								<Route path=":id" element={<ViewBankStatementImportLog />} />
							</Route>
							<Route path="*" element={<Navigate to="/" />} />
						</Routes>
					</BrowserRouter>
					<Toaster richColors />
				</ThemeProvider>
			</TooltipProvider>
		</LucideProvider>
	)
}

export default App
