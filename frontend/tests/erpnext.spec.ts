import { test, expect } from '@playwright/test';

test.describe('ERPNext Migrated App', () => {
  test('homepage loads and shows links', async ({ page }) => {
    await page.goto('/');
    await expect(page.getByText('ERPNext (Migrated to Django/React)')).toBeVisible();
    await expect(page.getByRole('link', { name: 'Banking Module' })).toBeVisible();
  });

  test('navigation to accounts module and back', async ({ page }) => {
    await page.goto('/');
    await page.getByRole('link', { name: 'accounts', exact: false }).first().click();
    await expect(page.getByText('ACCOUNTS Desk')).toBeVisible();
    await page.getByRole('link', { name: 'Back to Home' }).click();
    await expect(page).toHaveURL(/\/$/);
  });

  test('mock doctype form interaction', async ({ page }) => {
    await page.goto('/desk/accounts/Account');
    await expect(page.getByText('Account - New')).toBeVisible();
    await page.getByPlaceholder('Enter value...').fill('Test Account');
    await page.getByRole('button', { name: 'Save Account' }).click();
    // Since it's a mock form for now, we just ensure it doesn't crash
    await expect(page.getByText('Account - New')).toBeVisible();
  });
});
