const { defineConfig } = require('@vue/cli-service')
const webpack = require('webpack');
module.exports = defineConfig({
  transpileDependencies: true,
  configureWebpack: {
    plugins: [
      new webpack.ProgressPlugin()
    ],
  },
})
/*
module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:4000',  // Ваш сервер Django
        changeOrigin: true,  // Позволяет проксировать запросы с другого порта
        pathRewrite: {
          '^/api': '',  // Убирает /api из запроса, если нужно
        },
      },
    },
  },
};
*/
