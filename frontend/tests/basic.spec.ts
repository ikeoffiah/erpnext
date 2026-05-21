import { test, expect } from '@playwright/test';

test('homepage loads and shows migrated modules', async ({ page }) => {
  await page.goto('/');
  await expect(page.getByText('ERPNext (Migrated to Django/React)')).toBeVisible();
  // Check if a standard module like 'accounts' is present
  await expect(page.getByRole('link', { name: 'accounts', exact: false })).toBeVisible();
});

test('navigation to a module desk', async ({ page }) => {
  await page.goto('/');
  await page.getByRole('link', { name: 'accounts', exact: false }).first().click();
  await expect(page.getByText('ACCOUNTS Desk')).toBeVisible();
});
