var gulp = require('gulp');
var sass = require('gulp-sass')(require('node-sass'));
var exec = require('gulp-exec');


gulp.task('gtk3', function(done) {
    gulp.src('gtk-3.0/**/*.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('./gtk-3.0/'))
    done();
});

gulp.task('gtk4', function(done) {
    gulp.src('gtk-4.0/**/*.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('./gtk-4.0/'))
    done();
});

//Watch task
gulp.task('default',function() {
    gulp.watch('gtk-3.0/**/*.scss', gulp.series('gtk3'));
    gulp.watch('gtk-4.0/**/*.scss', gulp.series('gtk4'));
});
