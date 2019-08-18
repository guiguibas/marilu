module.exports = {
  lintOnSave: false,
  css: {
    loaderOptions: {
      sass: {
        data: `
        @import "@/scss/_spacing.scss";
        @import "@/scss/_grid.scss";
        `,
      },
    },
  },
};
