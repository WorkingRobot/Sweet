var gulp = require('gulp');
var sass = require('gulp-sass')(require('node-sass'));
var exec = require('gulp-exec');

gulp.task('default',function() {
    return gulp.src('*/**.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('.'));
});
