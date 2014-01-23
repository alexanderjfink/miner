module.exports = function(grunt) {

	grunt.initConfig({
		pkg: grunt.file.readJSON('package.json'),
		bowercopy: {
			options: {
				// Task-specific options go here
				clean: false,
				runBower: true,
			},
			libs: {
				options: {
					destPrefix: 'js',
				},
				files: {
					'jquery.js': 'jquery/jquery.min.js',
					'jquery.smooth-scroll.js': 'jquery.smooth-scroll/jquery.smooth-scroll.min.js'
				}

			}
		},
		jshint: {
			files: ['Gruntfile.js', 'js/**/*.js'],
			options: {
				// options here to override JSHint defaults
				globals: {
					jQuery: true,
					console: true,
					module: true,
					document: true
				}
			}
		},
		watch: {
			files: ['<%= jshint.files %>'],
			tasks: ['jshint']
		}
	});

	grunt.loadNpmTasks('grunt-contrib-jshint');
	grunt.loadNpmTasks('grunt-contrib-watch');
	grunt.loadNpmTasks('grunt-bowercopy');

	grunt.registerTask('default', ['jshint', 'bowercopy']);

};