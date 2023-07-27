const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');

const app = express();

const target = 'https://system-service-rubenpinxten.cloud.okteto.net/quotes/get/';
const corsProxy = createProxyMiddleware({ target, changeOrigin: true });

app.use('/api', corsProxy);

const port = 3000;
app.listen(port, () => {
  console.log(`Proxy server is running on http://localhost:${port}`);
});
