import { test, expect } from '@playwright/test';

const API_BASE_URL = process.env.API_BASE_URL || 'http://localhost:5000';

test.describe('Name Analysis API Tests', () => {
  
  test('health endpoint returns 200', async ({ request }) => {
    const response = await request.get(`${API_BASE_URL}/api/nameanalysis/health`);
    expect(response.status()).toBe(200);
    
    const responseBody = await response.json();
    expect(responseBody).toHaveProperty('Status', 'Healthy');
  });

  test('analyze endpoint accepts valid name', async ({ request }) => {
    const response = await request.post(`${API_BASE_URL}/api/nameanalysis/analyze`, {
      data: {
        name: 'John'
      }
    });
    
    expect(response.status()).toBe(200);
    
    const responseBody = await response.json();
    expect(responseBody).toHaveProperty('name', 'John');
    expect(responseBody).toHaveProperty('origin');
    expect(responseBody).toHaveProperty('meaning');
  });

  test('analyze endpoint rejects empty name', async ({ request }) => {
    const response = await request.post(`${API_BASE_URL}/api/nameanalysis/analyze`, {
      data: {
        name: ''
      }
    });
    
    expect(response.status()).toBe(400);
  });

});
