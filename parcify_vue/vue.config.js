module.exports = {
  publicPath: 'http://127.0.0.1:8080',
  outputDir: '../static/dist',
  indexPath: '../../templates/_base_vue.html',

  configureWebpack: {
    devServer: {
      devMiddleware: {
        writeToDisk: true
      }
    }
  }
}
