const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));

// Função para compilar o Sass
function compilarSass(done) {
  gulp.src('./frontend/sass/**/*.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('./frontend/assets/css'));
  done();
}

// Função para monitorar os arquivos em busca de mudanças
function observarArquivos() {
  gulp.watch('./frontend/sass/**/*.scss', compilarSass);
}

// Exporta as funções
exports.sass = compilarSass;
exports.watch = observarArquivos;

// Define a tarefa padrão que executa ambas as funções
exports.default = gulp.series(compilarSass, observarArquivos);