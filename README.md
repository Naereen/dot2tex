dot2tex - A Graphviz to LaTeX converter
=======================================

Hack on the [original dot2tex](https://github.com/kjellmf/dot2tex) project to port it to Python 3.

----

## Tests
### Testing for Python 2

```bash
cd /tmp/
git clone https://github.com/Naereen/dot2tex/
cd dot2tex
sudo pip2 install virtualenv
# activate virtualenv
virtualenv2 venv
./venv/bin/activate
type python2  # should be ./venv/bin/python2
type pip2  # should be ./venv/bin/pip2
pip2 install pyparsing
# examples
cd examples
for i in ./*.dot; do
    python2 ../dot2tex/dot2tex $i
done
echo "Examples passed!"
cd ..
# build and install in the virtualenv
python2 setup.py install
echo "Installed correctly!"
# tests
cd tests
for i in ./*.py; do
    python2 $i
done
echo "Tests passed!"
```

## Testing for Python 3

```bash
cd /tmp/
git clone https://github.com/Naereen/dot2tex/
cd dot2tex
sudo pip3 install virtualenv
# activate virtualenv
virtualenv3 venv
./venv/bin/activate
type python3  # should be ./venv/bin/python3
type pip3  # should be ./venv/bin/pip3
pip3 install pyparsing
# examples
cd examples
for i in ./*.dot; do
    python3 ../dot2tex/dot2tex $i
done
echo "Examples passed!"
cd ..
# build and install in the virtualenv
python3 setup.py install
echo "Installed correctly!"
# tests
cd tests
for i in ./*.py; do
    python3 $i
done
echo "Tests passed!"
```

----


### Author
> [Lilian Besson (Naereen)](https://github.com/Naereen/).

## :scroll: License ? [![GitHub license](https://img.shields.io/github/license/Naereen/generate-word-cloud.py.svg)](https://github.com/Naereen/generate-word-cloud.py/blob/master/LICENSE)
This plug-in is published under the terms of the [GPLv3 License](http://www.gnu.org/licenses/gpl.html) (file [LICENSE](LICENSE)),
© [Lilian Besson](https://GitHub.com/Naereen), 2016.

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/generate-word-cloud.py/graphs/commit-activity)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://GitHub.com/Naereen/ama)
[![Analytics](https://ga-beacon.appspot.com/UA-38514290-17/github.com/Naereen/generate-word-cloud.py/README.md?pixel)](https://GitHub.com/Naereen/generate-word-cloud.py/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

[![ForTheBadge uses-badges](http://ForTheBadge.com/images/badges/uses-badges.svg)](http://ForTheBadge.com)
[![ForTheBadge uses-git](http://ForTheBadge.com/images/badges/uses-git.svg)](https://GitHub.com/)

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/Naereen/)
