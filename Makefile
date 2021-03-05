.PHONY: all website

pack: html pdf
html:
	rm -rf docs
	rm -rf website/_build
	cd website && rm -rf content
	# list folders with notebooks here. Notebooks must be present in _toc.yml.
	cp -r content website/
	# Build
	jupyter-book build website
	# Copy built site to docs
	cp -r website/_build/html docs
	rm -r website/_build
	# Move data to built website
	mkdir -p docs/content/data
	mv website/content/data/* docs/content/data/
	# Move figs to built website
	rm -rf docs/content/figs
	mv website/content/figs docs/content
	# Remove copied folders
	rm -rf website/content
	# No Jekyll on remote server
	touch docs/.nojekyll
pdf:
	rm -rf website/_build
	cd website && rm -rf content
	# list folders with notebooks here. Notebooks must be present in _toc.yml.
	cp -r content website/
	# Build
	jupyter-book build website/ --builder pdfhtml
	# Move over to docs
	mv website/_build/pdf/book.pdf content/gds4ae.pdf
	# Clean
	rm -rf website/content
	rm -r website/_build
test:
	rm -rf tests
	mkdir tests
	jupyter nbconvert --to notebook \
                      --execute \
                      --output-dir=tests \
                      --ExecutePreprocessor.timeout=600 \
                      --ExecutePreprocessor.ipython_hist_file='' \
                      content/notebooks/*.ipynb 

	rm -rf tests
	echo "########\n\nAll blocks passed\n\n########"
reset_docs:
	rm -r docs/*
	git checkout HEAD docs/
	git checkout HEAD content/gds4ae.pdf
