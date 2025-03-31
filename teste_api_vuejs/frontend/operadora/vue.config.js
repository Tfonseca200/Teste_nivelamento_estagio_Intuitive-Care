const { defineConfig } = require('@vue/cli-service')
const path = require('path') // Adicione esta linha no topo

module.exports = defineConfig({
  transpileDependencies: true,
  
  chainWebpack: (config) => {
    // Configuração explícita para o Babel Loader
    config.module
      .rule('js')
      .use('babel-loader')
      .loader('babel-loader')
      .tap((options) => ({
        ...options,
        configFile: path.resolve(__dirname, 'babel.config.js'), // Caminho absoluto
        babelrc: false // Ignora arquivos .babelrc
      }))
  },
  
  // Opcional: Configuração para melhorar o linting
  lintOnSave: process.env.NODE_ENV !== 'production'
})