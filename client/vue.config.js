const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
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
