const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');
const app = express();

// Proxy configuration
app.use('/api', createProxyMiddleware({
 target: 'https://api.ussquash.com',
 changeOrigin: true,
 pathRewrite: {
   '^/api': '', // Remove '/api' prefix when forwarding to the target
 },
 onProxyReq: (proxyReq, req, res) => {
   // Add any custom headers or authentication here if needed
   // Example: proxyReq.setHeader('Authorization', 'Bearer YOUR_TOKEN');
 },
}));

// Start the server
const PORT = 3000;
app.listen(PORT, () => {
 console.log(`Proxy server is running at http://localhost:${PORT}`);
});
