Comparing 2 dependency extraction methods with compare2.py:

	Prerequisites:
		- Two TA style files containing the list of dependencies

	How to run:
		-Run the python script from the command line. Example: python compare2.py <method1TAFile> <method2TAFile>
		-There will be console output containing stats about common dependencies, and percentage similarities
		-There will be two generated json output files containing the generated dictionaries with each key being a dependent, and the corresponding values being a list of dependencies.

Comparing 3 dependency extraction methods with compare3.py:

	Prerequisites:
		- Three TA style files containing the list of dependencies
		
	How to run:
		-Run the python script from the command line. Example: python compare3.py <Method1TAFile> <method2TAFile> <method3TAFile>
		-There will be console output containing stats about common dependencies and percentage similarities