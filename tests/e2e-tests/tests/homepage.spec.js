import { test, expect } from '@playwright/test';

test.describe('Know Your Name AI - Basic Functionality', () => {
  
  test('homepage loads successfully', async ({ page }) => {
    await page.goto('/');
    await expect(page).toHaveTitle(/Know Your Name/i);
  });

  test('can submit a name for analysis', async ({ page }) => {
    await page.goto('/');
    
    // Find the name input field
    const nameInput = page.locator('input[type="text"]').first();
    await nameInput.fill('John');
    
    // Click analyze button
    const analyzeButton = page.locator('button:has-text("Analyze")');
    await analyzeButton.click();
    
    // Wait for results
    await expect(page.locator('.analysis-result')).toBeVisible({ timeout: 10000 });
  });

  test('displays error for empty name', async ({ page }) => {
    await page.goto('/');
    
    // Click analyze button without entering a name
    const analyzeButton = page.locator('button:has-text("Analyze")');
    await analyzeButton.click();
    
    // Should show error message
    await expect(page.locator('.error-message')).toBeVisible();
  });

});
