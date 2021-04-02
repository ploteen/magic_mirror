#!/bin/zsh

rm -r ../backend/static
rm ../backend/templates/index.html

npm run build
mv dist/static/ ../backend/
mv dist/index.html ../backend/templates/index.html